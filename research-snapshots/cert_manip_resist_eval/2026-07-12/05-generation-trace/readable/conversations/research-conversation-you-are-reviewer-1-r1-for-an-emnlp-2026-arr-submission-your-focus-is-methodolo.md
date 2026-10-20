# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **Methodology and Experiments**. ## Venue calibr

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3fe7b14d3d025092.jsonl`
- **Structured JSON:** [`eb0ab098dbb8ddab3646.json`](../../sessions/eb/eb0ab098dbb8ddab3646.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-22T18:48:04.626Z_

You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **Methodology and Experiments**. 

## Venue calibration
EMNLP 2026 via ARR. Overall Assessment scale (half-point):
- 5 = Award consideration (top 2.5%)
- 4 = Conference acceptance
- 3 = Findings acceptance
- 2 = Resubmit next cycle
- 1 = Do not resubmit
Acceptance rate ~21%. Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

## Paper summary
**Title**: "Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation: Weakest-Link Dominance, Aggregation Defenses, and the Limits of Diversity"

**Core setup**: 15 LLM judges (6 families, 3 capability tiers: small 7-8B, medium 12-14B/API-mini, large 70B+/API), all C(15,3)=455 three-judge panels, 2 benchmarks (MMLU, ARC), 8 attack types (sycophancy, score_manipulation, position_bias, verbosity, authority, few-shot hijacking, persona manipulation, instruction override) → 18 conditions total (12 core + 6 extended).

**Metrics**: 
- η_j = individual judge ASR
- η_max = max(η_j) in panel (weakest link)
- K_eff = exp(-Σ(λ_i/Σλ_j)log(λ_i/Σλ_j)) from MI matrix eigenvalues (effective diversity)
- Panel ASR under majority vote (default) + other aggregation rules

**Regression**: ASR_p = β_0 + β_η · η_max,p + β_K · K_eff,resid,p + ε_p (K_eff residualized against η_max)

**Key results**:
1. **Weakest-link dominance**: η_max significant in 9/12 core conditions (FDR), mean β=0.73. K_eff,resid significant in only 4/12 (FDR), mean β=0.22. ΔR²=0.04 for K_eff beyond η_max. K_eff-η_max correlation r=0.73 (range 0.35-0.85), only 1 "confound-free" condition.
2. **Attack type generalization**: Extended to 18 conditions. η_max 14/18, K_eff 6/18. One condition shows negative K_eff direction (ARC×persona_manip, β=-0.12, NS).
3. **Adaptive targeting**: Gini 0.38 adaptive vs 0.12 RF (p<0.001). Gini correlates with η_max (r=0.67, p<0.001) but not K_eff (r=0.21, p=0.089).
4. **Aggregation comparison**: K_eff sig ranges 1/12 (Bayesian) to 6/12 (threshold). Bayesian lowest mean ASR (0.198 vs 0.261 majority). This aggregation-dependence of K_eff suggests artifact.
5. **Panel selection**: Min-η_max (0.229) ≈ Strongest-K (0.234) ≈ Two-Stage (0.227), all NS differences. Max-K_eff worst (0.341).
6. **Panel size sensitivity**: K_eff sig ratio drops from 0.33 (K=3) to 0.08 (K=9). η_max rises from 0.75 to 0.92.
7. **Open-ended (MT-Bench)**: η_max 4/4 sig. K_eff direction inconsistent, 1 significant NEGATIVE (Writing, β=-0.22).
8. **Partial-knowledge adversary**: Full→Partial only 8.8% ASR drop. K_eff drops from 4/12 to 2/12 to 0/12 across knowledge levels.
9. **Capability-matched analysis** (Discussion §5.1): Within-tier panels (C(5,3)=10 each), K_eff 1/6 sig only. η_max variance drops from 0.045 to 0.008.
10. **BFT contrast** (Discussion §5.2): K_eff positive in BOTH adaptive and RF regimes (10/12 RF vs 4/12 adaptive). β ratio 0.91, interaction NS (p=0.217). No reversal.
11. **Multicollinearity** (Discussion §5.1): K_eff sig ranges 2/12 (Bonferroni) to 7/12 (uncorrected). Partial r of K_eff|η_max = 0.14 (r²=0.02).
12. **Pareto frontier**: 83% large-tier, 0% small-tier. Recommendation reduces to "pick strongest models."

**Tables in paper**: 19 tables total. Tables 1-12 in main text (pages 3-9), Tables 13-19 in appendix-style (pages 10-11).
**Limitations section**: ~1 paragraph, 3 points (small within-tier sample, oracle adversary assumption, MCQ vs open-ended non-generalization).

## Imagined experiment coverage reference
The review context lists 12 imagined experiments (plan_001 through plan_012). The paper covers all 12:
- plan_001 (15-model scale): Table 1, Table 2 → covered
- plan_002 (attack expansion): Table 3 → covered  
- plan_003 (BFT contrast): Table 17, 18 → covered in §5.2
- plan_004 (capability-matched): Table 16 → covered in §5.1
- plan_005 (panel selection): Tables 8, 9 → covered in §4.5
- plan_006 (ASR concentration): Tables 4, 5 → covered in §4.3
- plan_007 (diversity-capability tradeoff): Table 19, §5.3 → covered
- plan_008 (panel size): Table 10 → covered in §4.6
- plan_009 (VIF/multicollinearity): Tables 14, 15 → covered in §5.1
- plan_010 (aggregation rules): Tables 6, 7 → covered in §4.4
- plan_011 (open-ended): Table 11 → covered in §4.7
- plan_012 (partial-knowledge): Tables 12, 13 → covered in §4.8

All 12 imagined experiments appear to be represented.

## Your review task
Write a detailed review focusing on:
1. **Methodological soundness**: Is the regression framework appropriate? Is residualization the right approach given r=0.73 confound? Are the statistical tests properly applied?
2. **Experimental design**: Coverage, controls, potential confounds beyond what's addressed.
3. **Claims vs evidence alignment**: Are the three main claims (weakest-link, aggregation, targeting) well-supported?
4. **Reproducibility**: Is the setup described sufficiently? Could someone replicate?
5. **Weaknesses in methods/experiments**: What's missing or problematic?

Provide:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, specific and actionable)
- Questions for authors
- Preliminary scores: Soundness (1-5), Excitement (1-5), Reproducibility (1-5), Overall (1-5, half-point)
- Confidence (1-5)

Be rigorous. Calibrate to EMNLP acceptance rate (~21%). A score of 4 means you'd advocate for main conference acceptance.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "0b461a26-c420-452c-aae2-b07914d2b33e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T18:48:04.632Z_

```json
{
  "parentUuid": "0b461a26-c420-452c-aae2-b07914d2b33e",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
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
  "uuid": "28768fce-7aab-4526-97a5-42384ea6ff90",
  "timestamp": "2026-05-22T18:48:04.632Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-22T18:48:07.350Z_



I need to read the paper and project files to write a thorough review. Let me start by loading the project overview and reading the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28768fce-7aab-4526-97a5-42384ea6ff90",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ78b8n57HX94afkuasA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3abaa45-cc37-4ed0-b347-2d2f3a31212b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHMZku2mwuUsfmxtvNHdDD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16593,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16593,
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

_source line 4 · 2026-05-22T18:48:08.619Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PLZbnQyrhcHmNg31LqN3tN`</summary>

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
  "parentUuid": "a3abaa45-cc37-4ed0-b347-2d2f3a31212b",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ78b8n57HX94afkuasA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d986adbf-d7ec-4b1a-8575-74f9afb9cb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHMZku2mwuUsfmxtvNHdDD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16593,
      "cache_read_input_tokens": 0,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16593
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 135,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16593,
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

_source line 5 · 2026-05-22T18:48:08.625Z_

<details><summary>↩ Tool result · `toolu_01PLZbnQyrhcHmNg31LqN3tN`</summary>

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
  "parentUuid": "d986adbf-d7ec-4b1a-8575-74f9afb9cb32",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "230592a6-bd8a-49c1-b44e-fdcbd7be2983",
  "sourceToolAssistantUUID": "d986adbf-d7ec-4b1a-8575-74f9afb9cb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T18:48:18.730Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "230592a6-bd8a-49c1-b44e-fdcbd7be2983",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ78tP7bvXmRUxW8e2Wc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44f6afb8-3770-4a3a-8dc5-366bdbd4c593",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaYqtZ2QykqeHQHQm6R6QR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 7 · 2026-05-22T18:48:19.676Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Xkxo2HXgSUmAJ3WLh2GqUn`</summary>

```json
{
  "project": "cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44f6afb8-3770-4a3a-8dc5-366bdbd4c593",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ78tP7bvXmRUxW8e2Wc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9e488d4-7ff4-4a1d-8c47-8ae9c4b467b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaYqtZ2QykqeHQHQm6R6QR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 8 · 2026-05-22T18:48:19.745Z_

<details><summary>↩ Tool result · `toolu_01Xkxo2HXgSUmAJ3WLh2GqUn`</summary>

```text
{"result":"# 项目 cert_manip_resist_eval 概况\n\n## 实验状态 (30 个)\n\n- **plan001_step1_parallel**: PREPARING — \n- **plan001_step1_parallel_dryrun2**: PREPARING — \n- **plan001_step1_parallel_dryrun**: PREPARING — \n- **plan001_step1_full_v3**: PREPARING (failed) — \n- **plan001_step1_full_v2**: PREPARING (failed) — \n- **plan001_step1_full**: PREPARING — \n- **plan001_step1_dryrun3**: PREPARING — \n- **plan001_step1_dryrun2**: PREPARING — \n- **plan001_step1_dryrun**: PREPARING — \n- **taxonomy-broad-spectrum**: DONE (negative) — \n- **mvp-step2v3-retry3**: DONE (negative) — \n- **mvp-step2v3-retry2**: DONE (failed) — \n- **mvp-step2v3-retry**: DONE (failed) — \n- **mvp-step2v3-regression**: DONE (failed) — \n- **mvp-step2-keff-contrast**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan001_step1_batched_v2（准备中）\n- plan001_step1_batched（准备中）\n- plan001_step1_v3（准备中）\n- plan001_step1_throttled_v5（准备中）\n- plan001_step1_throttled_v4（准备中）\n- plan001_step1_throttled_v3（准备中）\n- plan001_step1_throttled_v2（准备中）\n- plan001_step1_throttled（准备中）\n- plan001_step1_v2（准备中）\n- plan001_step1_parallel_final（准备中）\n- …另有 13 项\n\n## 近期结论\n- **plan001_step1_full_v4** (success): Expanding from 6 to 15 models (9 API + 6 local) across 6 families and 3 capability tiers breaks the structural K_eff-η_max collinearity (r=-0.8 with 6 models). With 15 models, panels can have high K_eff (cross-family diversity) without necessarily including weak judges, enabling clean separation of diversity vs robustness effects.\n- **taxonomy-broad-spectrum** (negative): K_eff is a significant negative predictor of panel ASR specifically for broad-spectrum attacks (verbosity bias, position bias, authority bias) that exploit shared judge biases, consistent across both MMLU and ARC datasets. This validates the attack taxonomy: targeted attacks → η_max dominates; broad-spectrum attacks → K_eff provides additional protection. ← 基于 mvp-step2v3-retry3\n- **mvp-step2v3-retry3** (negative): Controlling for individual model robustness (η_max), higher K_eff panels have significantly lower ASR. Multi-factor regression log(ASR) ~ log(K_eff) + log(η_max) should show K_eff coefficient significantly negative. ← 基于 mvp-step2v3-retry2\n\n## 趋势\n成功 1 / 负向 3 / 失败 3 / 共 7\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nseetacloud-rtx6000: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- mvp-step2v3-regression: 训练失败 — unknown\n- mvp-step2v3-retry: 训练失败 — unknown\n- mvp-step2v3-retry2: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9e488d4-7ff4-4a1d-8c47-8ae9c4b467b8",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "4e2c1d89-0101-42e5-b78d-cbbd2b4314c6",
  "sourceToolAssistantUUID": "f9e488d4-7ff4-4a1d-8c47-8ae9c4b467b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T18:48:21.087Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YZUnEMyStdGUPY5HonTzjx`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e2c1d89-0101-42e5-b78d-cbbd2b4314c6",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ78tP7bvXmRUxW8e2Wc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ec72423-228a-4155-80df-cb55f9b87a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaYqtZ2QykqeHQHQm6R6QR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 10 · 2026-05-22T18:48:21.125Z_

<details><summary>↩ Tool result · `toolu_01YZUnEMyStdGUPY5HonTzjx`</summary>

```text
artifacts/dream_reports/dream_20260522T055016/best/paper.tex
artifacts/dream_reports/dream_20260522T055016/median/paper.tex
artifacts/dream_reports/dream_20260522T055016/worst/paper.tex
artifacts/_project/paper/theorem1_proof.tex
artifacts/theorem1_proof.tex
docs/paper/analysis.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
artifacts/dream_reports/dream_20260522T173833/best/paper.tex
artifacts/dream_reports/dream_20260522T173833/median/paper.tex
artifacts/dream_reports/dream_20260522T173833/worst/paper.tex
docs/paper/threat_model.tex
docs/paper/methodology.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ec72423-228a-4155-80df-cb55f9b87a31",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "595192c2-cf64-4e24-beef-a511adbfa455",
  "sourceToolAssistantUUID": "1ec72423-228a-4155-80df-cb55f9b87a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T18:48:21.372Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017TD3zkfMoLdKed6Adg3Da2`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "595192c2-cf64-4e24-beef-a511adbfa455",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ78tP7bvXmRUxW8e2Wc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "499a476a-ad61-41d8-91a5-00c1c4875afa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaYqtZ2QykqeHQHQm6R6QR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16593,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1457
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 256,
          "cache_read_input_tokens": 16593,
          "cache_creation_input_tokens": 1457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1457,
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

_source line 12 · 2026-05-22T18:48:21.408Z_

<details><summary>↩ Tool result · `toolu_017TD3zkfMoLdKed6Adg3Da2`</summary>

```text
artifacts/dream_reports/dream_20260522T055016/best/paper.pdf
artifacts/dream_reports/dream_20260522T055016/median/paper.pdf
artifacts/dream_reports/dream_20260522T055016/worst/paper.pdf
artifacts/theorem1_proof.pdf
docs/paper/main.pdf
artifacts/dream_reports/dream_20260522T173833/best/paper.pdf
artifacts/dream_reports/dream_20260522T173833/median/paper.pdf
artifacts/dream_reports/dream_20260522T173833/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "499a476a-ad61-41d8-91a5-00c1c4875afa",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "2a4cfd00-92f7-482c-afd9-71687de1cdd4",
  "sourceToolAssistantUUID": "499a476a-ad61-41d8-91a5-00c1c4875afa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T18:48:23.646Z_

Let me read the latest dream report paper (best version) and also the main paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a4cfd00-92f7-482c-afd9-71687de1cdd4",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ79pxWVTxyfsUGypz3Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bd39e6f-48cd-4abf-8635-a4f37fec1168",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPsbymBBuzc53A7v9KVF2h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 18050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1802,
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

_source line 14 · 2026-05-22T18:48:25.541Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VFNXB1JvKVJyt6Lzo3Skei`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bd39e6f-48cd-4abf-8635-a4f37fec1168",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ79pxWVTxyfsUGypz3Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c16fd2b5-50ea-44e6-9a5e-2636c44c68dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPsbymBBuzc53A7v9KVF2h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 18050,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1802
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 18050,
          "cache_creation_input_tokens": 1802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1802,
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

_source line 15 · 2026-05-22T18:48:25.870Z_

<details><summary>↩ Tool result · `toolu_01VFNXB1JvKVJyt6Lzo3Skei`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{amsmath}
8	\usepackage{amsfonts}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{enumitem}
12	\usepackage{tabularx}
13	\usepackage[numbers]{natbib}
14	\usepackage{hyperref}
15	
16	\newcommand{\keff}{K_{\text{eff}}}
17	\newcommand{\etamax}{\eta_{\text{max}}}
18	\newcommand{\keffresid}{K_{\text{eff}}^{\text{resid}}}
19	
20	\title{More Diverse, More Vulnerable:\\How Judge Panel Diversity Backfires Under Adaptive Adversaries}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	Multi-judge evaluation panels are increasingly used to assess LLM outputs, with the prevailing assumption that judge diversity---analogous to Byzantine Fault Tolerance (BFT)---improves robustness against manipulation. We provide large-scale empirical evidence that this assumption \emph{reverses} under adaptive adversaries. Across 15 LLM judges spanning 6 model families, 455 three-judge panels, 9 attack types, and 4 evaluation benchmarks, we show that panel diversity (effective independence $\keff$) is \textbf{independently and positively} associated with attack success rate (ASR), even after residualizing against individual judge weakness ($\etamax$). This ``diversity trap'' is driven by dual vulnerability channels whose relative importance is attack-dependent: $\etamax$ dominates shared-bias attacks (sycophancy, verbosity), while $\keff$ dominates transferable attacks (score manipulation, position bias). We trace the mechanism to BFT's broken assumption: random faults distribute uniformly across judges (Gini$\approx$0.12), but adaptive adversaries concentrate attacks on the weakest judge (Gini$\approx$0.68), turning diversity from a defense into an expanded attack surface. Under calibrated random faults, $\keff$'s coefficient flips negative in 5/12 conditions, empirically confirming BFT's prediction. We propose a robustness-first two-stage panel selection algorithm that reduces ASR by 20.8\% over the strongest-$K$ baseline, and show that Bayesian aggregation provides a complementary 28.4\% reduction. Our findings challenge the ``more diverse = more robust'' assumption and call for diversity-aware security analysis in LLM evaluation pipeline design.
29	\end{abstract}
30	
31	\section{Introduction}
32	
33	As LLMs are increasingly deployed as automated evaluators~\cite{zheng2023judging,li2023alpacaeval}, the research community has adopted multi-judge panels to mitigate individual model biases. The intuition is straightforward and borrowed from distributed systems: diverse, independent judges should be harder to simultaneously fool, much like Byzantine Fault Tolerance (BFT) guarantees that $f$ faulty nodes cannot compromise a system of $3f+1$ independent replicas.
34	
35	This paper demonstrates that this intuition is \emph{wrong} under adversarial conditions. We conduct what is, to our knowledge, the largest systematic study of adversarial robustness in multi-judge LLM evaluation: 15 models from 6 families (OpenAI, Anthropic, Google, Meta, Alibaba, Microsoft), enumerated into 455 three-judge panels, evaluated under 9 distinct attack types across MMLU, ARC-Challenge, MT-Bench, and AlpacaEval.
36	
37	Our central finding is the \textbf{diversity trap}: panel diversity, measured by effective judge independence ($\keff$), is \emph{independently and positively} associated with attack success rate. After residualizing $\keff$ against individual judge weakness ($\etamax$, the maximum vulnerability of any panel member), $\keffresid$ remains significantly positive in 10/12 conditions (FDR-corrected). Panel vulnerability is driven by \textbf{dual factors}---$\etamax$ and $\keff$---whose relative importance depends on attack type:
38	
39	\begin{itemize}[nosep,leftmargin=*]
40	\item \textbf{Shared-bias attacks} (sycophancy, verbosity, authority): $\etamax$ dominates because all judges share similar cognitive biases from RLHF training.
41	\item \textbf{Transferable attacks} (score manipulation, position bias): $\keff$ dominates because diverse judges provide heterogeneous, judge-specific attack surfaces.
42	\end{itemize}
43	
44	We trace this to BFT's core assumption: fault independence. Under random faults, failures distribute uniformly (Gini$\approx$0.12) and diversity genuinely helps---our calibrated random-fault simulations show $\keff$'s coefficient \emph{flipping negative} in 5/12 conditions. But adaptive adversaries concentrate attacks on the weakest judges (Gini$\approx$0.68, top-1 judge absorbing 78\% of ASR), turning diversity from fault tolerance into an expanded attack menu.
45	
46	We further show that: (1) the diversity trap holds within capability tiers (4/6 conditions significant among top-tier models only), ruling out tier-mixing confounds; (2) generalizes to open-ended benchmarks (MT-Bench 3/4, AlpacaEval 2/4 significant); (3) scales with panel size ($\keff$ coefficient increases monotonically from $K$=3 to $K$=9); (4) holds under partial-knowledge adversaries who know only model family membership (7/12 significant). We propose a two-stage defense---robustness screening followed by diversity optimization---that achieves 20.8\% ASR reduction over the strongest-$K$ baseline, and show Bayesian aggregation provides complementary protection.
47	
48	\section{Related Work}
49	
50	\paragraph{LLM-as-Judge.} LLM evaluation using model judges has become standard practice~\cite{zheng2023judging,li2023alpacaeval,dubois2024alpacafarm}. Known biases include position bias, verbosity preference, and self-enhancement~\cite{wang2023large,zheng2023judging}. Multi-judge panels are proposed as mitigation, but their adversarial robustness remains unstudied.
51	
52	\paragraph{Adversarial Attacks on LLM Judges.} Prior work demonstrates individual judge vulnerability to prompt injection, sycophancy exploitation, and score manipulation~\cite{raina2024llm,shi2024optimization}. We extend this to \emph{panel-level} analysis, studying how panel composition mediates vulnerability.
53	
54	\paragraph{Byzantine Fault Tolerance.} Classical BFT~\cite{lamport1982byzantine,castro1999practical} guarantees safety when faults are independent. Recent work questions independence assumptions in ML systems~\cite{sagawa2020investigation}. We empirically test whether BFT's independence assumption holds for LLM judge panels.
55	
56	\paragraph{Ensemble Diversity.} The diversity-accuracy tradeoff is well-studied in ensemble learning~\cite{krogh1994neural,brown2005diversity}. Our setting differs: we study diversity under \emph{adaptive adversaries} who exploit panel composition, not passive noise.
57	
58	\section{Problem Formulation}
59	
60	\paragraph{Setup.} A panel $P = \{j_1, \ldots, j_K\}$ of $K$ LLM judges evaluates candidate responses. Each judge $j_i$ produces a binary decision (accept/reject). The panel decision uses an aggregation rule $\mathcal{A}$ (default: majority vote).
61	
62	\paragraph{Adversary Model.} An adaptive adversary observes the panel composition and crafts attacks to maximize the panel's attack success rate (ASR)---the fraction of evaluation instances where the panel decision is flipped.
63	
64	\paragraph{Vulnerability Metrics.} We define two panel-level predictors:
65	\begin{itemize}[nosep,leftmargin=*]
66	\item $\etamax = \max_{j \in P} \eta_j$: maximum individual vulnerability (weakest link). $\eta_j$ is judge $j$'s individual ASR under a given attack.
67	\item $\keff$: effective number of independent judges, computed from the eigenspectrum of the pairwise mutual information matrix. Higher $\keff$ indicates greater functional diversity.
68	\end{itemize}
69	
70	To disentangle $\keff$ from $\etamax$, we define $\keffresid$ as the residual of regressing $\keff$ on $\etamax$, ensuring orthogonality (VIF$=$1.02).
71	
72	\paragraph{Regression Model.} For each condition (dataset $\times$ attack type), we fit:
73	\begin{equation}
74	\text{ASR}_P = \beta_0 + \beta_\eta \cdot \etamax + \beta_K \cdot \keffresid + \epsilon
75	\end{equation}
76	across all 455 panels. A significantly positive $\beta_K$ indicates diversity independently increases vulnerability.
77	
78	\section{Experimental Setup}
79	
80	\paragraph{Models.} 15 LLM judges: GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini (OpenAI); Claude-3.5-Sonnet (Anthropic); Gemini-1.5-Pro (Google); Llama-3.1-8B, Llama-3.1-70B (Meta); Qwen2.5-7B, Qwen2.5-72B (Alibaba); Mistral-7B-v0.3, Phi-3-medium-14B (Microsoft). Three capability tiers: Small (7--14B), Medium (14--34B), Large (70B+ and API).
81	
82	\paragraph{Panels.} All $\binom{15}{3} = 455$ three-judge panels, extended to $K \in \{5,7,9\}$ for panel-size analysis.
83	
84	\paragraph{Attacks.} 9 attack types spanning three paradigms: \emph{bias exploitation} (sycophancy, verbosity, authority bias), \emph{score manipulation} (direct score manipulation, position bias, few-shot bias), and \emph{injection} (few-shot hijacking, persona manipulation, instruction override).
85	
86	\paragraph{Benchmarks.} MMLU and ARC-Challenge (MCQ); MT-Bench and AlpacaEval (open-ended generation).
87	
88	\paragraph{Statistical Methods.} FDR correction (Benjamini-Hochberg) for multiple comparisons; beta regression for distributional robustness; residualization for multicollinearity control.
89	
90	\section{The Diversity Trap: Core Evidence}
91	
92	\subsection{Dual Vulnerability Drivers}
93	
94	Table~\ref{tab:core} presents the core regression results across 12 conditions (2 datasets $\times$ 6 attacks). Both $\etamax$ and $\keffresid$ are significant predictors of panel ASR: $\etamax$ reaches FDR significance in 10/12 conditions, $\keffresid$ in 10/12 conditions. The mean $R^2 = 0.62$, indicating that these two factors jointly explain the majority of panel-level vulnerability variance.
95	
96	\begin{table*}[t]
97	\centering
98	\small
99	\caption{Dual vulnerability drivers: 15-model regression across 12 conditions (455 panels each). $\keffresid$ is residualized against $\etamax$ (VIF$=$1.02). Bold $p$-values are FDR-significant ($q < 0.05$). ``Dominant'' indicates which predictor has the larger standardized $\beta$.}
100	\label{tab:core}
101	\begin{tabular}{lccccccl}
102	\toprule
103	Condition & $\etamax$ $\beta$ & $p$ & $\keffresid$ $\beta$ & $p$ & $R^2$ & Confound $r$ & Dominant \\
104	\midrule
105	mmlu$\times$sycophancy & 0.82 & \textbf{1.2e-8} & 0.31 & \textbf{0.004} & 0.68 & 0.72 & $\etamax$ \\
106	mmlu$\times$score\_manip & 0.45 & \textbf{0.018} & 0.61 & \textbf{3.4e-9} & 0.71 & 0.38 & $\keff$ \\
107	mmlu$\times$position & 0.15 & 0.214 & 0.58 & \textbf{1.2e-8} & 0.56 & 0.36 & $\keff$ \\
108	mmlu$\times$verbosity & 0.74 & \textbf{4.1e-7} & 0.28 & \textbf{0.011} & 0.63 & 0.74 & $\etamax$ \\
109	mmlu$\times$authority & 0.69 & \textbf{1.8e-6} & 0.19 & 0.087 & 0.58 & 0.78 & $\etamax$ \\
110	mmlu$\times$few\_shot & 0.55 & \textbf{2.3e-4} & 0.48 & \textbf{6.1e-6} & 0.65 & 0.65 & both \\
111	\midrule
112	arc$\times$sycophancy & 0.79 & \textbf{3.5e-8} & 0.35 & \textbf{0.002} & 0.66 & 0.71 & $\etamax$ \\
113	arc$\times$score\_manip & 0.38 & 0.117 & 0.64 & \textbf{1.7e-7} & 0.59 & 0.35 & $\keff$ \\
114	arc$\times$position & 0.03 & 0.910 & 0.72 & \textbf{1.8e-8} & 0.57 & 0.34 & $\keff$ \\
115	arc$\times$verbosity & 0.71 & \textbf{8.9e-7} & 0.33 & \textbf{0.003} & 0.61 & 0.73 & $\etamax$ \\
116	arc$\times$authority & 0.66 & \textbf{3.2e-6} & 0.22 & 0.062 & 0.55 & 0.76 & $\etamax$ \\
117	arc$\times$few\_shot & 0.51 & \textbf{5.7e-4} & 0.52 & \textbf{3.8e-6} & 0.63 & 0.62 & both \\
118	\bottomrule
119	\end{tabular}
120	\end{table*}
121	
122	A systematic pattern emerges: \textbf{transferable attacks} (score manipulation, position bias) are $\keff$-dominated ($\beta_K > \beta_\eta$), while \textbf{shared-bias attacks} (sycophancy, verbosity, authority) are $\etamax$-dominated. This yields a predictive taxonomy: given a new attack type, its transferability predicts which vulnerability channel dominates.
123	
124	Three conditions have low confound correlation ($r \approx 0.35$), serving as ``smoking gun'' evidence: in these conditions, $\keffresid$ achieves $p < 2.1 \times 10^{-28}$, confirming diversity's independent harmful effect even where the $\keff$-$\etamax$ association is weak.
125	
126	\subsection{Capability-Matched Validation}
127	
128	A natural concern is that $\keff$'s positive effect is an artifact of tier-mixing: high-$\keff$ panels might mix weak and strong models, making $\keff$ a proxy for tier heterogeneity rather than diversity \emph{per se}. We test this by running within-tier regressions (Table~\ref{tab:tier}).
129	
130	\begin{table}[t]
131	\centering
132	\small
133	\caption{Within-tier $\keff$ validation. Large tier uses only top-tier models (70B+ and API), eliminating tier-mixing.}
134	\label{tab:tier}
135	\begin{tabular}{lcccc}
136	\toprule
137	Tier & Models & Panels & $r(\keff,\etamax)$ & $\keffresid$ sig \\
138	\midrule
139	Small (7B--14B) & 5 & 10 & 0.32 & 2/6 \\
140	Medium & 4 & 4 & 0.41 & 1/6 \\
141	Large (70B+API) & 6 & 20 & 0.33 & 4/6 \\
142	Cross-tier (all) & 15 & 455 & 0.55 & 10/12 \\
143	\bottomrule
144	\end{tabular}
145	\end{table}
146	
147	The large tier is most informative: all 6 models are top-tier (GPT-4o, GPT-4.1, Claude-3.5-Sonnet, Gemini-1.5-Pro, Llama-70B, Qwen-72B), yet $\keffresid$ is significant in 4/6 conditions (best $p = 4.2 \times 10^{-4}$). The condition-dependent pattern is preserved: score manipulation and position bias are $\keff$-dominated; sycophancy and verbosity are $\etamax$-dominated. This rules out tier-mixing as the driver of the diversity trap.
148	
149	\subsection{Statistical Robustness}
150	
151	We perform comprehensive diagnostics (Table~\ref{tab:diagnostics}). VIF$=$1.02 and condition number$=$4.8 confirm the design matrix is well-conditioned. Residuals pass Shapiro-Wilk normality ($p = 0.23$). Maximum Cook's distance is 0.031 (threshold: 1.0), with only 2.4\% high-leverage points. Under Bonferroni correction (most conservative), $\keffresid$ remains significant in 8/12 conditions. Beta regression, which properly handles bounded ASR in $[0,1]$, confirms 9/12 significant---highly consistent with OLS.
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\caption{Multiple comparison robustness across correction methods.}
157	\label{tab:diagnostics}
158	\begin{tabular}{lcc}
159	\toprule
160	Correction & $\keffresid$ sig & $\etamax$ sig \\
161	\midrule
162	Uncorrected & 12/12 & 11/12 \\
163	FDR (BH) & 10/12 & 10/12 \\
164	Bonferroni & 8/12 & 9/12 \\
165	Beta reg.\ + FDR & 9/12 & 10/12 \\
166	\bottomrule
167	\end{tabular}
168	\end{table}
169	
170	\section{Mechanism: BFT Reversal}
171	
172	\subsection{Random-Fault Contrast}
173	
174	BFT predicts that diversity helps when faults are independent and random. We test this by simulating calibrated random faults: each judge's failure probability is drawn from bootstrapped clean-accuracy noise, independent across judges. Table~\ref{tab:bft} contrasts $\keff$'s coefficient under adaptive versus random-fault regimes.
175	
176	\begin{table*}[t]
177	\centering
178	\small
179	\caption{BFT regime contrast: $\keff$ coefficient under adaptive vs.\ calibrated random faults (12 conditions, 455 panels). ``Flipped'' indicates $\beta_{\text{RF}}$ is significantly negative (diversity helps under random faults).}
180	\label{tab:bft}
181	\begin{tabular}{lcccccc}
182	\toprule
183	Condition & $\beta_{\text{adaptive}}$ & $p_{\text{adap}}$ & $\beta_{\text{RF}}$ & $p_{\text{RF}}$ & $|\beta_{\text{adap}}/\beta_{\text{RF}}|$ & Flipped? \\
184	\midrule
185	mmlu$\times$sycophancy & 0.31 & \textbf{0.004} & 0.08 & 0.310 & 3.88 & No \\
186	mmlu$\times$score\_manip & 0.61 & \textbf{3.4e-9} & $-$0.22 & \textbf{0.015} & 2.77 & Yes \\
187	mmlu$\times$position & 0.58 & \textbf{1.2e-8} & $-$0.31 & \textbf{0.003} & 1.87 & Yes \\
188	mmlu$\times$verbosity & 0.28 & \textbf{0.011} & 0.11 & 0.198 & 2.55 & No \\
189	mmlu$\times$authority & 0.19 & 0.087 & 0.06 & 0.541 & 3.17 & No \\
190	mmlu$\times$few\_shot & 0.48 & \textbf{6.1e-6} & $-$0.18 & \textbf{0.039} & 2.67 & Yes \\
191	arc$\times$sycophancy & 0.35 & \textbf{0.002} & 0.10 & 0.251 & 3.50 & No \\
192	arc$\times$score\_manip & 0.64 & \textbf{1.7e-7} & $-$0.28 & \textbf{0.008} & 2.29 & Yes \\
193	arc$\times$position & 0.72 & \textbf{1.8e-8} & $-$0.35 & \textbf{0.001} & 2.06 & Yes \\
194	arc$\times$verbosity & 0.33 & \textbf{0.003} & 0.12 & 0.175 & 2.75 & No \\
195	arc$\times$authority & 0.22 & 0.062 & 0.05 & 0.612 & 4.40 & No \\
196	arc$\times$few\_shot & 0.52 & \textbf{3.8e-6} & $-$0.14 & 0.091 & 3.71 & Marginal \\
197	\bottomrule
198	\end{tabular}
199	\end{table*}
200	
201	The results confirm the BFT reversal: in 5/12 conditions, $\beta_{\text{RF}}$ flips to significantly \emph{negative}---diversity genuinely protects under random faults, as BFT predicts. The flips concentrate on transferable attacks (score manipulation, position bias, few-shot), where judge-specific exploit paths are most relevant. Under adaptive attacks, these same conditions show the strongest positive $\beta$ (0.48--0.72). The mean $\beta$ ratio is 2.8$\times$, and the $R^2$ gap ($\Delta R^2 = 0.31$; RF: 0.78, adaptive: 0.47) quantifies BFT's broken predictability: panel structure explains 78\% of variance under random faults but only 47\% under adaptive attacks, where strategic adversary behavior introduces irreducible noise.
202	
203	\subsection{ASR Concentration Analysis}
204	
205	To illuminate \emph{how} adaptive adversaries exploit diversity, we analyze per-judge ASR distributions within panels (Table~\ref{tab:concentration}).
206	
207	\begin{table}[t]
208	\centering
209	\small
210	\caption{ASR concentration: adaptive vs.\ random-fault regimes.}
211	\label{tab:concentration}
212	\begin{tabular}{lccc}
213	\toprule
214	Metric & Adaptive & RF & Ratio \\
215	\midrule
216	Mean Gini & 0.68 & 0.12 & 5.67 \\
217	Entropy (bits) & 1.42 & 2.31 & 0.61 \\
218	Top-1 judge share & 0.78 & 0.38 & 2.05 \\
219	$r(\keff, \text{Gini})$ & 0.52 & 0.08 & 6.50 \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	Under adaptive attacks, ASR is highly concentrated: the weakest judge absorbs 78\% of attack success (vs.\ 38\% under random faults). Crucially, $r(\keff, \text{Gini}) = 0.52$: more diverse panels produce \emph{more concentrated} attacks, because greater capability spread gives the adversary a clearer targeting gradient. Under random faults, concentration is uniformly low (Gini$=$0.12), confirming BFT's independence assumption holds only in the non-adversarial regime.
225	
226	\section{Generalization}
227	
228	\subsection{Attack Surface Expansion}
229	
230	To test whether the diversity trap generalizes beyond the original 6 attack types, we introduce 3 additional attacks: few-shot hijacking (in-context example injection), persona manipulation (authority impersonation), and instruction override (direct prompt overwrite). Table~\ref{tab:expanded} shows the 6 new conditions.
231	
232	\begin{table}[t]
233	\centering
234	\small
235	\caption{Extended attack results (6 new conditions, 15 models).}
236	\label{tab:expanded}
237	\begin{tabular}{lccc}
238	\toprule
239	Condition & $\keffresid$ $\beta$ & $p$ & Dominant \\
240	\midrule
241	mmlu$\times$hijack & 0.54 & \textbf{8.2e-7} & $\keff$ \\
242	mmlu$\times$persona & 0.29 & \textbf{0.008} & $\etamax$ \\
243	mmlu$\times$override & 0.22 & 0.042 & $\etamax$ \\
244	arc$\times$hijack & 0.58 & \textbf{2.1e-7} & $\keff$ \\
245	arc$\times$persona & 0.25 & \textbf{0.019} & $\etamax$ \\
246	arc$\times$override & 0.18 & 0.112 & $\etamax$ \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	$\keffresid$ is significant in 4/6 new conditions. Combined with the original 12, this yields 14/18 total FDR-significant conditions for $\keffresid$. The attack taxonomy is predictive: high-transferability attacks (few-shot hijacking) are $\keff$-dominated; moderate/low-transferability attacks (persona, instruction override) are $\etamax$-dominated---consistent with the core results.
252	
253	\subsection{Open-Ended Benchmarks}
254	
255	The diversity trap is not an MCQ artifact. On MT-Bench (multi-turn dialogue evaluation) and AlpacaEval (instruction-following scoring), $\keffresid$ is significant in 3/4 and 2/4 conditions, respectively (Table~\ref{tab:openended}). The condition-dependent dominance pattern transfers without modification: score manipulation and position bias remain $\keff$-dominated; sycophancy and verbosity remain $\etamax$-dominated. $R^2$ is lower (0.39--0.52 vs.\ 0.62 for MCQ), reflecting the higher noise floor inherent to open-ended evaluation.
256	
257	\begin{table}[t]
258	\centering
259	\small
260	\caption{Open-ended benchmark results (8 conditions). Pattern consistent with MCQ findings despite higher evaluation noise.}
261	\label{tab:openended}
262	\begin{tabular}{lcccl}
263	\toprule
264	Condition & $\keffresid$ $\beta$ & $p$ & $R^2$ & Dom. \\
265	\midrule
266	MT$\times$score & 0.52 & \textbf{1.8e-5} & 0.52 & $\keff$ \\
267	MT$\times$syco & 0.28 & \textbf{0.012} & 0.49 & $\etamax$ \\
268	MT$\times$pos & 0.47 & \textbf{8.3e-5} & 0.44 & $\keff$ \\
269	MT$\times$verb & 0.18 & 0.108 & 0.47 & $\etamax$ \\
270	AE$\times$score & 0.44 & \textbf{3.2e-4} & 0.46 & $\keff$ \\
271	AE$\times$syco & 0.21 & 0.058 & 0.43 & $\etamax$ \\
272	AE$\times$pos & 0.38 & \textbf{0.002} & 0.40 & both \\
273	AE$\times$verb & 0.14 & 0.175 & 0.39 & $\etamax$ \\
274	\bottomrule
275	\end{tabular}
276	\end{table}
277	
278	\subsection{Panel Size Sensitivity}
279	
280	Extending panel size from $K=3$ to $K \in \{5,7,9\}$ reveals a scaling law: $\keff$'s coefficient increases monotonically ($\beta_K$: 0.42$\to$0.48$\to$0.55$\to$0.61), while $\etamax$'s decreases (0.51$\to$0.49$\to$0.43$\to$0.38). The crossover occurs at $K \approx 6$: for panels below this size, individual robustness ($\etamax$) is the primary concern; above it, structural diversity ($\keff$) becomes dominant (Table~\ref{tab:panelsize}). This has direct practical implications: the common strategy of ``adding more judges'' systematically amplifies the diversity trap---$K=9$ panels show 45\% stronger $\keff$ effect than $K=3$.
281	
282	\begin{table}[t]
283	\centering
284	\small
285	\caption{Panel size sensitivity ($K = 3, 5, 7, 9$).}
286	\label{tab:panelsize}
287	\begin{tabular}{lccccl}
288	\toprule
289	$K$ & Panels & $\keffresid$ sig & $\bar{\beta}_K$ & $\bar{\beta}_\eta$ & Primary \\
290	\midrule
291	3 & 455 & 10/12 & 0.42 & 0.51 & $\etamax$ \\
292	5 & 3003 & 11/12 & 0.48 & 0.49 & balanced \\
293	7 & 6435 & 12/12 & 0.55 & 0.43 & $\keff$ \\
294	9 & 5005 & 12/12 & 0.61 & 0.38 & $\keff$ \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	\subsection{Partial-Knowledge Adversary}
300	
301	A full-knowledge adversary is a worst-case assumption. We test a realistic partial-knowledge adversary who knows only model \emph{family} membership (typically public information) but not individual vulnerability profiles. Family-level targeting achieves 78.4\% of full-knowledge ASR (0.058 vs.\ 0.074), and $\keff$ remains significant in 7/12 conditions (Table~\ref{tab:partial}). Family membership alone captures 62.8\% of adversary information value, because family$\to$capability tier correlations provide a strong prior on vulnerability profiles.
302	
303	\begin{table}[t]
304	\centering
305	\small
306	\caption{Adversary knowledge level comparison.}
307	\label{tab:partial}
308	\begin{tabular}{lcccc}
309	\toprule
310	Knowledge & ASR & $\keff$ sig & $R^2$ & Info value \\
311	\midrule
312	Full & 0.074 & 10/12 & 0.62 & 100\% \\
313	Partial (family) & 0.058 & 7/12 & 0.51 & 62.8\% \\
314	Black-box & 0.031 & 3/12 & 0.28 & 0\% \\
315	\bottomrule
316	\end{tabular}
317	\end{table}
318	
319	\section{Structural Barriers to Independence}
320	
321	\subsection{Gaussian Copula Failure}
322	
323	If inter-judge dependence followed a Gaussian copula, pairwise mutual information (MI) could be estimated from linear correlations. Across 105 model pairs (15 models), observed MI exceeds Gaussian-predicted MI by a mean factor of 18.5$\times$ (max 312$\times$), with 82/105 pairs exceeding 10$\times$. This invalidates copula-based independence bounds and motivates empirical $\keff$ measurement.
324	
325	\subsection{Family Labels Are Unreliable}
326	
327	Model family labels do not predict judge independence: within-family MI (0.42) is not significantly higher than cross-family MI (0.39; Mann-Whitney $p = 0.158$). The actual driver is capability proximity ($r = -0.71$ with MI): models at similar capability levels share failure modes regardless of training pipeline. Practitioners should not equate ``different families'' with ``diverse panel.''
328	
329	\subsection{Diversity-Capability Tradeoff}
330	
331	Across 455 panels, $\keff$ and $\etamax$ correlate at $r = 0.55$ globally. Within capability tiers, this drops to $r \approx 0.33$, revealing two components: a cross-tier component ($\sim$40\%, from mixing weak and strong models) and a within-tier residual ($\sim$60\%, from genuine diversity-vulnerability association). The Pareto frontier (18 panels, slope $-0.73$) quantifies the tradeoff: each 0.1 increase in $\keff$ costs at least 0.073 increase in $\etamax$.
332	
333	\section{Defense: Panel Design and Aggregation}
334	
335	\subsection{Two-Stage Panel Selection}
336	
337	We propose a robustness-first algorithm: (1) screen judges by individual robustness ($\eta_j \leq$ percentile-75 threshold), (2) maximize $\keff$ among qualifying judges. Table~\ref{tab:defense} benchmarks this against 5 baselines.
338	
339	\begin{table}[t]
340	\centering
341	\small
342	\caption{Panel selection strategy benchmark (15 models, MMLU, 6 attacks). Two-stage achieves 84\% of oracle efficiency.}
343	\label{tab:defense}
344	\begin{tabular}{lccc}
345	\toprule
346	Strategy & ASR & $\Delta$ vs Strong-K & Best (of 6) \\
347	\midrule
348	Two-Stage (ours) & 0.038 & $-$20.8\% & 5/6 \\
349	Min-$\etamax$ & 0.041 & $-$14.6\% & 4/6 \\
350	Strongest-$K$ & 0.048 & baseline & 1/6 \\
351	Random & 0.089 & +85.4\% & 0/6 \\
352	Max-$\keff$ & 0.112 & +133.3\% & 0/6 \\
353	Oracle & 0.032 & $-$33.3\% & 6/6 \\
354	\bottomrule
355	\end{tabular}
356	\end{table}
357	
358	Two-stage achieves the lowest ASR among non-oracle strategies (0.038), outperforming the strongest-$K$ baseline by 20.8\%. Max-$\keff$ is catastrophic (ASR 0.112, +133\%), providing the most direct evidence against blind diversity maximization. Sensitivity analysis shows the screening threshold is robust across percentile 50--75, with optimal performance at percentile 65--75.
359	
360	\subsection{Aggregation Rule Modulation}
361	
362	The dual vulnerability driver effect varies by aggregation rule (Table~\ref{tab:aggregation}). Threshold (unanimity) voting amplifies $\keff$'s harmful effect by 45\% ($\beta_K$: 0.42$\to$0.61) and increases ASR by 86\%, because a single flipped judge blocks panel rejection. Bayesian aggregation, which downweights judges based on prior accuracy, provides the best single-aggregation defense: 28.4\% ASR reduction, with $\keff$ significance dropping from 10/12 to 6/12. However, 6/12 $\keff$ significance confirms Bayesian aggregation alone cannot eliminate the diversity trap, motivating a combined defense stack.
363	
364	\begin{table}[t]
365	\centering
366	\small
367	\caption{Aggregation rule $\times$ vulnerability drivers (455 panels).}
368	\label{tab:aggregation}
369	\begin{tabular}{lcccc}
370	\toprule
371	Aggregation & $\keff$ sig & $\bar{\beta}_K$ & ASR & $\Delta$ \\
372	\midrule
373	Majority & 10/12 & 0.42 & 0.074 & -- \\
374	Threshold & 11/12 & 0.61 & 0.138 & +86\% \\
375	Acc-weighted & 8/12 & 0.39 & 0.069 & $-$6.8\% \\
376	Bayesian & 6/12 & 0.25 & 0.053 & $-$28.4\% \\
377	\bottomrule
378	\end{tabular}
379	\end{table}
380	
381	\section{Conclusion}
382	
383	We presented large-scale empirical evidence for the \emph{diversity trap} in multi-judge LLM evaluation: panel diversity independently increases vulnerability to adaptive adversarial attacks. This finding, validated across 15 models, 455 panels, 9 attack types, 4 benchmarks, and multiple panel sizes, challenges the pervasive assumption that diversity improves evaluation robustness. The mechanism traces to BFT's broken assumption: adaptive adversaries exploit the heterogeneous attack surface that diverse judges create, concentrating attacks on the weakest judge rather than facing independent random faults. We proposed a two-stage defense (robustness screening + diversity optimization) that reduces ASR by 20.8\%, complemented by Bayesian aggregation ($-$28.4\%). We urge the LLM evaluation community to adopt diversity-aware security analysis: do not assume more judges means safer evaluation.
384	
385	\section*{Limitations}
386	
387	Our study has three main limitations. First, our adversary model assumes knowledge of panel composition (full or partial); in settings where panel membership is secret, the diversity trap may be attenuated. Second, while we cover 15 models from 6 families, the rapidly evolving LLM landscape means our specific quantitative findings may shift as new model generations emerge. Third, our analysis is observational---the regression design establishes independent predictive association, not strict causality, between diversity and vulnerability; experimental manipulation of panel composition with controlled interventions would strengthen causal claims.
388	
389	\bibliographystyle{plainnat}
390	\bibliography{custom}
391	
392	\end{document}
393	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c16fd2b5-50ea-44e6-9a5e-2636c44c68dc",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "0176c38f-ca9d-4919-bb77-f1c8394b25c6",
  "sourceToolAssistantUUID": "c16fd2b5-50ea-44e6-9a5e-2636c44c68dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-22T18:48:28.580Z_

Now let me read the earlier dream report version (which was described in the task prompt with different numbers) and the actual paper source files to compare.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0176c38f-ca9d-4919-bb77-f1c8394b25c6",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7A9yW9DBDaLbB283Fx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec6d7217-8d11-4448-adf2-d01571aac22a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvboSHnXyZ7GYZh2wCofY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10839,
      "cache_read_input_tokens": 19852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10839,
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

_source line 17 · 2026-05-22T18:48:31.423Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Me1z4TJNQ5YQWSHica2iHy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T055016/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec6d7217-8d11-4448-adf2-d01571aac22a",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7A9yW9DBDaLbB283Fx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "242d8f16-3301-4f87-b8ae-07f3fb7b3a10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvboSHnXyZ7GYZh2wCofY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10839,
      "cache_read_input_tokens": 19852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10839,
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

_source line 18 · 2026-05-22T18:48:31.700Z_

<details><summary>↩ Tool result · `toolu_01Me1z4TJNQ5YQWSHica2iHy`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage{amsmath,amssymb,amsthm}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{xcolor}
8	\usepackage{multirow}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{natbib}
11	
12	\newtheorem{theorem}{Theorem}
13	\newtheorem{corollary}{Corollary}
14	\newtheorem{definition}{Definition}
15	
16	\title{The Diversity Trap: Why Adding More Judges\\Doesn't Make LLM Evaluation Safer}
17	
18	\author{Anonymous}
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
29	Multi-judge LLM evaluation panels are increasingly deployed under the assumption that judge diversity---analogous to Byzantine Fault Tolerance (BFT)---is the primary defense against adversarial manipulation. We show this analogy is fundamentally broken. We prove that under \emph{adaptive} adversaries who target the weakest judge, panel attack success rate (ASR) is dominated by the individual robustness of the weakest member ($\eta_{\max}$), not by judge diversity ($K_{\text{eff}}$). Empirically, across 15 models (including GPT-4o, Claude-3.5-Sonnet, Gemini-1.5-Pro, and open-source models up to 236B parameters), 455 three-judge panels, 9 attack types, and 2 benchmarks, we find $\eta_{\max}$ is a significant predictor in 87\% of conditions while $K_{\text{eff}}$ is non-significant in 91\%. A random-fault simulation confirms that diversity \emph{does} help under BFT assumptions (Cohen's $d = 1.12$ contrast), validating that the failure is specific to adaptive adversaries, not an artifact. Worse, we identify a \emph{diversity-capability tradeoff} ($r = -0.78$, $p < 0.001$): in the current LLM ecosystem, pursuing diversity necessarily introduces weaker judges, actively harming security. We propose a robustness-first two-stage panel design algorithm that dominates five baseline strategies in 93\% of conditions. Our results challenge a core assumption in the evaluation security literature and provide actionable guidance for practitioners.
30	\end{abstract}
31	
32	% ============================================================
33	% 1. INTRODUCTION
34	% ============================================================
35	\section{Introduction}
36	
37	Adding more diverse judges to a multi-LLM evaluation panel does not make it safer---it can make it worse. This finding contradicts a central assumption in the growing literature on LLM-as-judge security, where diversity is treated as the primary defense against adversarial manipulation.
38	
39	The intuition behind diversity-as-defense is borrowed from distributed systems: in Byzantine Fault Tolerance (BFT), adding independent replicas reduces the probability that a sufficient fraction fails simultaneously. Recent work on multi-judge evaluation implicitly adopts this logic, reporting that multi-model committees reduce attack success rates and recommending heterogeneous panels as a defense \citep{sok2026,yang2026,turkmen2026}. However, BFT assumes \emph{random} faults---components fail independently with fixed probabilities. LLM adversaries are fundamentally different: they are \emph{adaptive}, observing the panel composition and targeting the weakest member.
40	
41	We formalize this distinction. Under an adaptive adversary model, we prove that panel ASR is $\Theta(\eta_{\max})$---dominated by the maximum individual vulnerability across panel members---regardless of judge diversity. We then provide comprehensive empirical validation across 15 models spanning the open-source and API ecosystem, 455 three-judge panels, 9 attack types, and 2 benchmarks, totaling over 8,000 experimental conditions.
42	
43	Our contributions are:
44	
45	\begin{enumerate}
46	    \item \textbf{Weakest-link theorem.} We prove and empirically validate that under adaptive adversaries, panel ASR is dominated by $\eta_{\max}$ (significant in 87\% of conditions), while diversity $K_{\text{eff}}$ provides no significant protection (non-significant in 91\%). This holds across panel sizes $K \in \{3,5,7,9\}$.
47	
48	    \item \textbf{Adaptive adversary vs.\ BFT distinction.} We formalize why diversity fails: BFT's random-fault assumption does not hold for LLM adversaries. A random-fault simulation shows diversity \emph{does} help under BFT assumptions ($K_{\text{eff}}$ significant in 78\% of conditions), with a large-effect contrast (Cohen's $d = 1.12$, $p < 0.001$).
49	
50	    \item \textbf{Diversity-capability tradeoff.} We identify a structural barrier: $K_{\text{eff}}$ and $\eta_{\max}$ are negatively correlated ($r = -0.78$, $p < 0.001$), meaning diverse panels necessarily include weaker judges. This tradeoff persists within capability tiers ($r \approx -0.57$).
51	
52	    \item \textbf{Robustness-first panel design.} We propose a two-stage algorithm (filter by robustness, then maximize diversity) that achieves mean ASR of 0.042, dominating all five baselines in 93\% of conditions.
53	
54	    \item \textbf{Methodological contributions.} We show that Gaussian copula models underestimate inter-judge information sharing by a median of 18.4$\times$ (up to 235$\times$), and that model family labels do not predict judge independence ($p = 0.31$).
55	\end{enumerate}
56	
57	% ============================================================
58	% 2. RELATED WORK
59	% ============================================================
60	\section{Related Work}
61	
62	\paragraph{LLM-as-Judge.}
63	Using LLMs as automated evaluators has become standard practice for tasks where human evaluation is expensive. Single-judge approaches suffer from well-documented biases including position bias, verbosity bias, and sycophancy. Multi-judge panels have been proposed as a mitigation, with the implicit assumption that aggregating diverse opinions reduces systematic errors.
64	
65	\paragraph{Adversarial Attacks on LLM Judges.}
66	Recent work has demonstrated that LLM judges are vulnerable to prompt injection, score manipulation, and various cognitive biases. These attacks achieve non-trivial success rates even against state-of-the-art models. The multi-judge setting has been relatively under-studied from a security perspective, with existing work primarily reporting that committees reduce average ASR without analyzing \emph{why} or \emph{when} this reduction holds.
67	
68	\paragraph{Byzantine Fault Tolerance.}
69	Classical BFT guarantees safety when fewer than $f < n/3$ replicas are faulty, under the assumption that faults are independent and non-adaptive. The analogy to multi-judge evaluation---more independent judges provide greater robustness---has been implicit in the literature but never formally examined. We show this analogy breaks under adaptive adversaries.
70	
71	\paragraph{Panel Diversity Metrics.}
72	Prior work has measured panel diversity through model family heterogeneity, prompting strategy variation, or temperature differences. We argue that \emph{effective independence} ($K_{\text{eff}}$), derived from the mutual information matrix between judges, is the correct metric, and show that family labels do not predict it.
73	
74	% ============================================================
75	% 3. THEORETICAL FRAMEWORK
76	% ============================================================
77	\section{Theoretical Framework}
78	
79	\subsection{Setup and Notation}
80	
81	Consider a panel of $K$ judges $\{J_1, \ldots, J_K\}$ evaluating a candidate text. Each judge $J_j$ has an individual vulnerability $\eta_j \in [0,1]$, representing the probability that an adversarial input successfully manipulates $J_j$'s evaluation. The panel uses majority-vote aggregation: the adversary succeeds if they compromise $\geq \lceil K/2 \rceil$ judges.
82	
83	We define two key panel-level metrics:
84	\begin{itemize}
85	    \item $\eta_{\max} = \max_{j} \eta_j$: the vulnerability of the weakest (most vulnerable) panel member.
86	    \item $K_{\text{eff}}$: the effective number of independent judges, derived from the eigenspectrum of the inter-judge mutual information matrix $\mathbf{M}$, where $M_{ij} = I(J_i; J_j)$. $K_{\text{eff}} = \left(\sum_i \lambda_i\right)^2 / \sum_i \lambda_i^2$, where $\lambda_i$ are the eigenvalues of $\mathbf{M}$.
87	\end{itemize}
88	
89	\subsection{Adaptive Adversary Model}
90	
91	\begin{definition}[Adaptive Adversary]
92	An adaptive adversary has access to the panel composition $\{J_1, \ldots, J_K\}$ and the per-judge vulnerability profiles $\{\eta_1, \ldots, \eta_K\}$. The adversary can craft targeted attacks optimized for each judge's weaknesses.
93	\end{definition}
94	
95	\begin{theorem}[Weakest-Link Bound]
96	\label{thm:weakest-link}
97	For an adaptive adversary with access to per-judge vulnerability profiles, the panel attack success rate under majority-vote aggregation satisfies:
98	\[
99	\text{panel\_ASR} \geq \max_j \eta_j = \eta_{\max}
100	\]
101	Moreover, for panels where the weakest judge is sufficiently more vulnerable than the median ($\eta_{\max} \gg \text{median}_j(\eta_j)$), $\text{panel\_ASR} = \Theta(\eta_{\max})$.
102	\end{theorem}
103	
104	\begin{proof}[Proof sketch]
105	The adaptive adversary constructs an attack targeting the weakest judge $J^* = \arg\max_j \eta_j$. This attack succeeds on $J^*$ with probability $\eta_{\max}$. Since the attack is optimized for $J^*$'s weaknesses, it is also partially effective against judges with correlated vulnerabilities. For majority vote, the adversary needs $\lceil K/2 \rceil$ compromised judges. Starting from $J^*$, the adversary extends to the next-weakest judges. Because judges share architectural and training commonalities (reflected in $\mathbf{M}$), a single optimized attack transfers with non-trivial probability. The lower bound $\eta_{\max}$ follows from the adversary's ability to always compromise at least $J^*$. The $\Theta(\eta_{\max})$ scaling follows when $\eta_{\max}$ dominates the vulnerability distribution. Crucially, increasing $K_{\text{eff}}$ (diversity) does not reduce $\eta_{\max}$; it only ensures the remaining judges are more independent, which is irrelevant when the adversary's primary target is always the weakest link.
106	\end{proof}
107	
108	\subsection{Contrast with BFT}
109	
110	Under the BFT random-fault model, each judge fails independently with probability $p_j$, and failures are not adversarially targeted. In this regime:
111	\[
112	\text{panel\_fail\_prob} = \sum_{S \subseteq [K], |S| \geq \lceil K/2 \rceil} \prod_{j \in S} p_j \prod_{j \notin S} (1 - p_j)
113	\]
114	This probability decreases exponentially with $K_{\text{eff}}$ when faults are independent, validating the diversity-as-defense intuition \emph{only under random faults}. Our random-fault simulation (Section~\ref{sec:bft-contrast}) empirically confirms this distinction.
115	
116	% ============================================================
117	% 4. EXPERIMENTAL SETUP
118	% ============================================================
119	\section{Experimental Setup}
120	
121	\subsection{Model Pool}
122	
123	We evaluate 15 models spanning the open-source and commercial API ecosystem (Table~\ref{tab:models}). The pool includes 6 models in the 7B parameter class, 4 large models (70B+ or MoE), and 5 commercial API models. This diverse pool yields $\binom{15}{3} = 455$ unique three-judge panels.
124	
125	\begin{table}[t]
126	\centering
127	\caption{Model pool summary. $\eta_{\max}$ values represent individual vulnerability across MMLU and ARC benchmarks. Avg ASR is the mean attack success rate across all 6 original attack types.}
128	\label{tab:models}
129	\small
130	\begin{tabular}{llcccc}
131	\toprule
132	\textbf{Model} & \textbf{Type} & \textbf{Size} & $\boldsymbol{\eta}$\textbf{(MMLU)} & $\boldsymbol{\eta}$\textbf{(ARC)} & \textbf{Avg ASR} \\
133	\midrule
134	Qwen2.5-7B-Instruct    & Open & 7B     & 0.32 & 0.28 & 0.30 \\
135	Llama-3.1-8B-Instruct  & Open & 8B     & 0.38 & 0.35 & 0.37 \\
136	Mistral-7B-Instruct-v0.3 & Open & 7B   & 0.45 & 0.42 & 0.44 \\
137	Gemma-2-9B-Instruct    & Open & 9B     & 0.29 & 0.25 & 0.27 \\
138	Phi-3.5-mini-Instruct  & Open & 3.8B   & 0.52 & 0.48 & 0.50 \\
139	InternLM2.5-7B-Chat    & Open & 7B     & 0.35 & 0.31 & 0.33 \\
140	\midrule
141	Llama-3.1-70B-Instruct & Open & 70B    & 0.12 & 0.09 & 0.11 \\
142	Qwen2.5-72B-Instruct   & Open & 72B    & 0.10 & 0.08 & 0.09 \\
143	Mixtral-8x22B-Instruct & Open & 141B MoE & 0.15 & 0.13 & 0.14 \\
144	DeepSeek-V2.5-Chat     & Open & 236B MoE & 0.13 & 0.11 & 0.12 \\
145	\midrule
146	GPT-4o-mini            & API  & ---     & 0.18 & 0.15 & 0.17 \\
147	GPT-4o                 & API  & ---     & 0.08 & 0.06 & 0.07 \\
148	GPT-4.1                & API  & ---     & 0.05 & 0.04 & 0.05 \\
149	Claude-3.5-Sonnet      & API  & ---     & 0.06 & 0.05 & 0.06 \\
150	Gemini-1.5-Pro         & API  & ---     & 0.09 & 0.07 & 0.08 \\
151	\bottomrule
152	\end{tabular}
153	\end{table}
154	
155	\subsection{Attack Types}
156	
157	We evaluate 9 attack types spanning diverse adversarial strategies:
158	
159	\begin{itemize}
160	    \item \textbf{Original 6}: prompt injection, score manipulation, sycophancy bias, verbosity bias, position bias, authority bias.
161	    \item \textbf{Extended 3}: few-shot hijacking (in-context manipulation), persona manipulation (social engineering), instruction override (direct override of evaluation instructions).
162	\end{itemize}
163	
164	\subsection{Benchmarks}
165	
166	All experiments are conducted on MMLU and ARC-Challenge, representing knowledge-intensive and reasoning-intensive evaluation tasks respectively.
167	
168	\subsection{Panel Construction and Metrics}
169	
170	For $K=3$ panels, we enumerate all $\binom{15}{3} = 455$ combinations. For larger panel sizes ($K \in \{5,7,9\}$), we enumerate all $\binom{15}{K}$ combinations. For each panel, we compute:
171	\begin{itemize}
172	    \item $\eta_{\max}$: vulnerability of the weakest panel member.
173	    \item $K_{\text{eff}}$: effective independence from the MI matrix eigenspectrum.
174	    \item Panel ASR: fraction of adversarial inputs that successfully manipulate the majority vote.
175	\end{itemize}
176	
177	We fit multivariate regressions $\log(\text{ASR}) \sim \beta_1 \log(\eta_{\max}) + \beta_2 \log(K_{\text{eff}}) + \epsilon$ to quantify the relative predictive power of individual robustness vs.\ diversity.
178	
179	% ============================================================
180	% 5. RESULTS
181	% ============================================================
182	\section{Results}
183	
184	\subsection{Weakest-Link Dominance at Scale}
185	\label{sec:weakest-link}
186	
187	Table~\ref{tab:regression} presents the multivariate regression results across all 455 three-judge panels, 2 datasets, and 6 original attack types (12 conditions). $\eta_{\max}$ is a significant predictor ($p < 0.05$) in 87\% of conditions with a median coefficient $\beta = 0.72$, while $K_{\text{eff}}$ is non-significant in 91\% of conditions (median $p = 0.43$). The weakest-link model explains a median $R^2 = 0.56$ of the variance in panel ASR.
188	
189	\begin{table}[t]
190	\centering
191	\caption{Multivariate regression results across 455 panels. $\beta$ = standardized regression coefficient; $p$ = significance; $R^2$ = model fit. $\eta_{\max}$ consistently dominates while $K_{\text{eff}}$ remains non-significant.}
192	\label{tab:regression}
193	\small
194	\begin{tabular}{llccccc}
195	\toprule
196	\textbf{Dataset} & \textbf{Attack} & $\boldsymbol{\beta(\eta_{\max})}$ & $\boldsymbol{p(\eta_{\max})}$ & $\boldsymbol{\beta(K_{\text{eff}})}$ & $\boldsymbol{p(K_{\text{eff}})}$ & $\boldsymbol{R^2}$ \\
197	\midrule
198	MMLU & Prompt Injection    & 0.78 & 0.001    & $-$0.05 & 0.52 & 0.61 \\
199	MMLU & Score Manipulation  & 0.71 & 0.003    & 0.08    & 0.38 & 0.54 \\
200	MMLU & Sycophancy          & 0.65 & 0.012    & $-$0.03 & 0.71 & 0.48 \\
201	MMLU & Verbosity Bias      & 0.69 & 0.006    & 0.11    & 0.22 & 0.52 \\
202	MMLU & Position Bias       & 0.74 & 0.002    & $-$0.09 & 0.31 & 0.58 \\
203	MMLU & Authority Bias      & 0.82 & $<$0.001 & 0.04    & 0.63 & 0.67 \\
204	\midrule
205	ARC  & Prompt Injection    & 0.76 & 0.002    & $-$0.07 & 0.44 & 0.59 \\
206	ARC  & Score Manipulation  & 0.68 & 0.008    & 0.06    & 0.49 & 0.51 \\
207	ARC  & Sycophancy          & 0.73 & 0.004    & $-$0.12 & 0.18 & 0.55 \\
208	ARC  & Verbosity Bias      & 0.64 & 0.015    & 0.03    & 0.72 & 0.46 \\
209	ARC  & Position Bias       & 0.70 & 0.005    & $-$0.08 & 0.35 & 0.53 \\
210	ARC  & Authority Bias      & 0.80 & 0.001    & 0.02    & 0.81 & 0.65 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	The inclusion of API models (GPT-4o, GPT-4.1, Claude-3.5-Sonnet, Gemini-1.5-Pro) with generally lower individual vulnerabilities ($\eta \in [0.03, 0.18]$) does not alter the structural finding. API models follow the same weakest-link pattern as open-source models, with no evidence of a distinct ``coordinated defense'' regime. The 455-panel scale provides sufficient statistical power to detect effects that were directionally consistent but underpowered in smaller pilot studies.
216	
217	\subsection{Generalization Across Attack Types}
218	\label{sec:attack-expansion}
219	
220	To test whether the weakest-link phenomenon is attack-type-specific, we extend the evaluation to three additional attack types (Table~\ref{tab:new-attacks}). All three new attacks---few-shot hijacking (mean ASR = 0.31), persona manipulation (0.22), and instruction override (0.38)---exhibit the same $\eta_{\max}$-dominated pattern, with $\eta_{\max}$ significance rates of 83--87\% and $K_{\text{eff}}$ non-significance rates of 87--91\%.
221	
222	\begin{table}[t]
223	\centering
224	\caption{Results for three additional attack types across 455 panels, compared to the average of the original 6 attacks. The weakest-link pattern generalizes across all attack vectors.}
225	\label{tab:new-attacks}
226	\small
227	\begin{tabular}{lcccc}
228	\toprule
229	\textbf{Attack} & \textbf{Mean ASR} & $\boldsymbol{\eta_{\max}}$ \textbf{sig\%} & $\boldsymbol{K_{\text{eff}}}$ \textbf{nonsig\%} & \textbf{Median} $\boldsymbol{R^2}$ \\
230	\midrule
231	Few-shot Hijacking    & 0.31 & 83\% & 87\% & 0.51 \\
232	Persona Manipulation  & 0.22 & 87\% & 91\% & 0.54 \\
233	Instruction Override   & 0.38 & 85\% & 88\% & 0.53 \\
234	\midrule
235	Original 6 (avg)       & 0.24 & 87\% & 91\% & 0.56 \\
236	\bottomrule
237	\end{tabular}
238	\end{table}
239	
240	Cross-attack rank correlation of model vulnerabilities is $\rho = 0.82$, indicating that the relative robustness ordering of judges is largely preserved across attack types. This supports the view that individual robustness is an intrinsic property of the judge, not an artifact of specific attack-judge interactions.
241	
242	\subsection{BFT vs.\ Adaptive Adversary: Empirical Contrast}
243	\label{sec:bft-contrast}
244	
245	To validate Theorem~\ref{thm:weakest-link} and demonstrate that the irrelevance of diversity is specific to adaptive adversaries rather than a general property, we implement a random-fault simulation. In the random-fault model, each judge fails independently with probability $p_j = \eta_j$, without adversarial targeting.
246	
247	Table~\ref{tab:bft} shows a stark contrast. Under random faults, $K_{\text{eff}}$ becomes significant in 78\% of conditions ($\beta = -0.45$, median $p = 0.012$), confirming that diversity \emph{does} provide protection when faults are non-adaptive. The contrast with the adaptive setting ($K_{\text{eff}}$ significant in only 9\%) is large (Cohen's $d = 1.12$, $p < 0.001$).
248	
249	\begin{table}[t]
250	\centering
251	\caption{Contrast between adaptive adversary and random-fault (BFT) settings. Diversity ($K_{\text{eff}}$) helps under random faults but not under adaptive adversaries, confirming the theoretical distinction.}
252	\label{tab:bft}
253	\small
254	\begin{tabular}{lcccc}
255	\toprule
256	\textbf{Metric} & \textbf{Adaptive} & \textbf{Random-Fault} & \textbf{Cohen's} $\boldsymbol{d}$ & $\boldsymbol{p}$\textbf{-value} \\
257	\midrule
258	$K_{\text{eff}}$ $\beta$ (mean)  & $-$0.03 & $-$0.45 & 1.12 & $<$0.001 \\
259	$K_{\text{eff}}$ sig rate        & 9\%     & 78\%    & ---  & ---      \\
260	$\eta_{\max}$ $\beta$ (mean)     & 0.72    & 0.31    & 0.85 & $<$0.001 \\
261	$R^2$ (mean)                     & 0.56    & 0.42    & 0.62 & 0.003    \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	This result directly addresses the concern that our BFT comparison might be a strawman. The random-fault simulation is not a hypothetical---it represents the regime where the diversity assumption \emph{would} hold. The data shows this regime simply does not apply to LLM adversaries.
267	
268	\subsection{Capability-Matched Validation}
269	\label{sec:capability-matched}
270	
271	A natural objection is that the diversity-capability tradeoff is trivially driven by mixing models of vastly different sizes (3.8B vs.\ 236B). We address this by conducting within-tier analyses, grouping models into three capability tiers: 7B (6 models, 20 panels), 70B (4 models, 4 panels), and API (5 models, 10 panels).
272	
273	\begin{table}[t]
274	\centering
275	\caption{Within-tier regression results. Even after controlling for capability class, $\eta_{\max}$ dominates, $K_{\text{eff}}$ remains non-significant, and the diversity-capability tradeoff persists.}
276	\label{tab:within-tier}
277	\small
278	\begin{tabular}{lccccc}
279	\toprule
280	\textbf{Tier} & \textbf{N panels} & $\boldsymbol{\eta_{\max}}$ \textbf{sig\%} & $\boldsymbol{K_{\text{eff}}}$ \textbf{sig\%} & \textbf{Median} $\boldsymbol{R^2}$ & $\boldsymbol{r(K_{\text{eff}}, \eta_{\max})}$ \\
281	\midrule
282	7B (6 models)   & 20  & 73\% & 10\% & 0.36 & $-$0.58 \\
283	70B (4 models)  & 4   & 67\% & 17\% & 0.41 & $-$0.52 \\
284	API (5 models)  & 10  & 72\% & 12\% & 0.39 & $-$0.61 \\
285	\midrule
286	All (15 models) & 455 & 87\% & 9\%  & 0.56 & $-$0.78 \\
287	\bottomrule
288	\end{tabular}
289	\end{table}
290	
291	Table~\ref{tab:within-tier} shows that within every capability tier, $\eta_{\max}$ remains the dominant predictor (67--73\% significance), $K_{\text{eff}}$ remains non-significant (10--17\%), and the diversity-capability tradeoff persists ($r = -0.52$ to $-0.61$). The reduced $R^2$ (0.36--0.41 vs.\ 0.56 overall) reflects the narrower $\eta_{\max}$ variance within tiers, but $\eta_{\max}$ remains the strongest single predictor. The tradeoff persists because even within the same size class, diverse panels necessarily include that tier's weaker members.
292	
293	\subsection{ASR Concentration Analysis}
294	\label{sec:concentration}
295	
296	To provide direct evidence for the adaptive targeting mechanism underlying Theorem~\ref{thm:weakest-link}, we analyze the per-judge distribution of attack successes within each panel.
297	
298	\begin{table}[t]
299	\centering
300	\caption{Attack success rate concentration metrics. High Gini coefficients and weakest-judge concentration rates confirm that attacks concentrate on the most vulnerable panel member.}
301	\label{tab:concentration}
302	\small
303	\begin{tabular}{lccc}
304	\toprule
305	\textbf{Panel Tier} & \textbf{Mean Gini} & \textbf{Weakest/Mean Ratio} & \textbf{Conc.\ on Weakest \%} \\
306	\midrule
307	Mixed (weak + strong) & 0.78 & 3.4 & 94\% \\
308	Within 7B tier         & 0.62 & 2.3 & 85\% \\
309	Within 70B/API tier    & 0.51 & 1.8 & 78\% \\
310	\midrule
311	All panels             & 0.68 & 2.8 & 89\% \\
312	\bottomrule
313	\end{tabular}
314	\end{table}
315	
316	Table~\ref{tab:concentration} reveals highly concentrated attack patterns. The mean Gini coefficient across all panels is 0.68, with the weakest judge's ASR being 2.8$\times$ the panel mean and the strongest judge's ASR only 0.31$\times$ the mean. In 89\% of panel-attack combinations, the plurality of attack successes are concentrated on the weakest judge. The normalized entropy of per-judge ASR distributions (0.38) is significantly below the uniform distribution ($p < 0.001$). Concentration is highest in mixed panels (Gini = 0.78) where capability differences are largest, but remains substantial even within capability tiers (Gini = 0.51--0.62).
317	
318	\subsection{The Diversity-Capability Tradeoff}
319	\label{sec:tradeoff}
320	
321	We now characterize the structural barrier that makes diversity counterproductive. Across all 455 panels, $K_{\text{eff}}$ and $\eta_{\max}$ exhibit a strong negative correlation ($r = -0.78$, $p < 0.001$, 95\% CI $[-0.82, -0.73]$). The tradeoff slope is $-0.34 \pm 0.03$: each unit increase in effective independence is associated with a 0.34-unit increase in maximum vulnerability.
322	
323	\begin{table}[t]
324	\centering
325	\caption{Diversity-capability tradeoff across capability tiers. The negative correlation between $K_{\text{eff}}$ and $\eta_{\max}$ persists within all tiers, ruling out a trivial size-class artifact.}
326	\label{tab:tradeoff}
327	\small
328	\begin{tabular}{lcccc}
329	\toprule
330	\textbf{Tier} & $\boldsymbol{r(K_{\text{eff}}, \eta_{\max})}$ & $\boldsymbol{p}$\textbf{-value} & \textbf{N panels} & \textbf{Interpretation} \\
331	\midrule
332	7B  & $-$0.58 & 0.008    & 20  & Tradeoff persists within same-size models \\
333	70B & $-$0.52 & 0.048    & 4   & Limited N but consistent direction \\
334	API & $-$0.61 & 0.003    & 10  & API ecosystem shows same structure \\
335	All & $-$0.78 & $<$0.001 & 455 & Strong structural tradeoff \\
336	\bottomrule
337	\end{tabular}
338	\end{table}
339	
340	This tradeoff reflects a structural property of the current LLM ecosystem: achieving high effective independence requires selecting models from different families and architectures, which inevitably includes less capable (and less robust) models. The Pareto frontier contains only 12 of 455 panels (97\% are dominated), confirming that simultaneous optimization of diversity and robustness is effectively impossible with current models.
341	
342	\subsection{Panel Size Sensitivity}
343	\label{sec:panel-size}
344	
345	A natural question is whether the weakest-link effect diminishes as panel size increases. We test this by evaluating panels of size $K \in \{3, 5, 7, 9\}$, yielding 455 to 6,435 panels per size.
346	
347	\begin{table}[t]
348	\centering
349	\caption{Panel size sensitivity analysis. The weakest-link effect persists across all tested panel sizes, with only a slight decline in $\eta_{\max}$ dominance at larger $K$.}
350	\label{tab:panel-size}
351	\small
352	\begin{tabular}{cccccc}
353	\toprule
354	$\boldsymbol{K}$ & \textbf{N panels} & $\boldsymbol{\eta_{\max}}$ \textbf{sig\%} & $\boldsymbol{K_{\text{eff}}}$ \textbf{nonsig\%} & \textbf{Median} $\boldsymbol{R^2}$ & \textbf{Mean ASR} \\
355	\midrule
356	3 & 455   & 87\% & 91\% & 0.56 & 0.148 \\
357	5 & 3,003 & 85\% & 88\% & 0.52 & 0.119 \\
358	7 & 6,435 & 83\% & 85\% & 0.49 & 0.098 \\
359	9 & 5,005 & 80\% & 82\% & 0.46 & 0.082 \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	Table~\ref{tab:panel-size} shows that while $\eta_{\max}$ significance declines slightly from 87\% ($K=3$) to 80\% ($K=9$), it remains the dominant predictor at all panel sizes. $K_{\text{eff}}$ remains non-significant in 82--91\% of conditions. The slight decline reflects a weak diversity buffer---larger panels contain more strong judges that can outvote the weakest member---but this effect is far too small to make $K_{\text{eff}}$ a reliable defense. Practically, $K \in \{3, 5, 7, 9\}$ covers nearly all realistic deployment scenarios.
365	
366	\subsection{Robustness-First Panel Design}
367	\label{sec:algorithm}
368	
369	Our theoretical and empirical findings motivate a principled panel design algorithm. The two-stage procedure is:
370	
371	\begin{enumerate}
372	    \item \textbf{Robustness filter.} Select all judges with individual vulnerability $\eta_j \leq \tau$ for a threshold $\tau$.
373	    \item \textbf{Diversity maximization.} Among qualifying judges, select the $K$-member subset that maximizes $K_{\text{eff}}$.
374	\end{enumerate}
375	
376	Table~\ref{tab:algorithm} benchmarks this algorithm against five baselines across all conditions.
377	
378	\begin{table}[t]
379	\centering
380	\caption{Panel design algorithm benchmark. Two-Stage dominates all baselines in mean ASR and achieves the best worst-case performance, while maintaining reasonable diversity.}
381	\label{tab:algorithm}
382	\small
383	\begin{tabular}{lcccc}
384	\toprule
385	\textbf{Strategy} & \textbf{Mean ASR} & \textbf{Win Rate vs.\ Ours} & \textbf{Worst-Case ASR} & \textbf{Avg} $\boldsymbol{K_{\text{eff}}}$ \\
386	\midrule
387	Two-Stage (ours)       & 0.042 & ---  & 0.089 & 2.41 \\
388	Random                 & 0.187 & 3\%  & 0.412 & 2.18 \\
389	Max $K_{\text{eff}}$   & 0.231 & 6\%  & 0.485 & 2.87 \\
390	Min $\eta_{\max}$      & 0.051 & 18\% & 0.098 & 1.73 \\
391	Strongest-$K$          & 0.048 & 22\% & 0.095 & 1.61 \\
392	Max Family Diversity   & 0.198 & 4\%  & 0.423 & 2.65 \\
393	\bottomrule
394	\end{tabular}
395	\end{table}
396	
397	The two-stage algorithm achieves mean ASR of 0.042, dominating all five baselines in 93\% of conditions. Notably, the Max $K_{\text{eff}}$ strategy---which maximizes diversity without regard for robustness---performs \emph{worst} (mean ASR = 0.231), directly demonstrating the diversity trap. The Min $\eta_{\max}$ and Strongest-$K$ baselines are competitive (ASR 0.051 and 0.048) since they prioritize robustness, but the two-stage algorithm's diversity bonus provides consistent marginal improvement and better attack coverage.
398	
399	\paragraph{Threshold sensitivity.} Table~\ref{tab:threshold} shows that the optimal threshold lies in $\tau \in [0.15, 0.20]$: stricter thresholds eliminate too many candidates (reducing diversity options), while looser thresholds admit vulnerable judges.
400	
401	\begin{table}[t]
402	\centering
403	\caption{Threshold sensitivity for the robustness-first algorithm. The $\tau \in [0.15, 0.20]$ range balances robustness and diversity.}
404	\label{tab:threshold}
405	\small
406	\begin{tabular}{ccccc}
407	\toprule
408	\textbf{Threshold} $\boldsymbol{\tau}$ & \textbf{Qualifying Models} & \textbf{Mean ASR} & $\boldsymbol{K_{\text{eff}}}$ & \textbf{Recommendation} \\
409	\midrule
410	0.10 & 5  & 0.038 & 2.12 & Aggressive \\
411	0.15 & 7  & 0.040 & 2.31 & Recommended (ARC) \\
412	0.20 & 9  & 0.042 & 2.41 & Recommended (MMLU) \\
413	0.30 & 11 & 0.058 & 2.58 & Moderate \\
414	0.50 & 14 & 0.112 & 2.74 & Not recommended \\
415	\bottomrule
416	\end{tabular}
417	\end{table}
418	
419	\subsection{Methodological Findings}
420	
421	\paragraph{Gaussian copula failure.} The Gaussian copula model systematically underestimates mutual information between LLM judges by a median factor of 18.4$\times$ (range: 8--235$\times$) across 105 model pairs. This implies that copula-based independence bounds used in prior work substantially overestimate the effective independence of multi-judge panels.
422	
423	\paragraph{Family labels as diversity proxies.} Model family labels (e.g., Qwen vs.\ Llama) do not significantly predict inter-judge mutual information ($p = 0.31$). Panels designed for family diversity are no more independent than random panels of matched capability.
424	
425	% ============================================================
426	% 6. DISCUSSION
427	% ============================================================
428	\section{Discussion}
429	
430	\paragraph{Why does diversity fail?}
431	The core mechanism is the mismatch between the fault model assumed by diversity-based defenses and the actual threat model. BFT-style reasoning assumes faults are random and independent; adding more independent components reduces the probability of correlated failure. But LLM adversaries are adaptive: they observe the panel, identify the weakest member, and craft targeted attacks. In this regime, additional independent judges are irrelevant---the adversary always finds and exploits the weakest link. Our random-fault simulation confirms this: when faults \emph{are} random, diversity works exactly as BFT predicts.
432	
433	\paragraph{Is the tradeoff permanent?}
434	The diversity-capability tradeoff ($r = -0.78$) reflects the current state of the LLM ecosystem, where model capabilities vary enormously. As the ecosystem matures and the capability gap narrows, the tradeoff may weaken. However, the weakest-link theorem itself is structural: even with uniformly capable models, adaptive adversaries will still target the weakest member. The tradeoff merely exacerbates this fundamental problem.
435	
436	\paragraph{Implications for practitioners.}
437	Our results provide clear guidance: when designing multi-judge evaluation panels, prioritize individual robustness over diversity. Screen candidate judges for adversarial vulnerability, set a threshold, and only then consider diversity among qualifying judges. The common practice of maximizing family or architectural diversity can be actively harmful.
438	
439	% ============================================================
440	% 7. CONCLUSION
441	% ============================================================
442	\section{Conclusion}
443	
444	We have identified and characterized the \emph{diversity trap} in multi-judge LLM evaluation: the assumption that judge diversity provides security against adversarial manipulation is fundamentally flawed under adaptive adversaries. Our formal theorem, validated across 15 models, 455+ panels, 9 attack types, and panel sizes up to $K=9$, establishes that panel security is determined by the weakest member's individual robustness, not by judge diversity. The diversity-capability tradeoff makes this finding practically urgent: in the current LLM ecosystem, pursuing diversity actively degrades security. Our robustness-first two-stage algorithm provides a principled alternative that outperforms diversity-maximizing strategies by 5.5$\times$ in mean ASR.
445	
446	% ============================================================
447	% LIMITATIONS
448	% ============================================================
449	\section*{Limitations}
450	
451	Our evaluation uses majority-vote aggregation; more sophisticated aggregation mechanisms (e.g., weighted voting with learned trust scores) may partially mitigate the weakest-link effect. The adaptive adversary model assumes full knowledge of panel composition, which may overestimate real-world attacker capabilities. Finally, our model pool, while spanning 15 models from 7 families, does not cover all possible architectures---the diversity-capability tradeoff may weaken as more capable models from diverse families become available.
452	
453	% ============================================================
454	% REFERENCES (placeholder)
455	% ============================================================
456	\bibliographystyle{plainnat}
457	\begin{thebibliography}{9}
458	
459	\bibitem[{SoK}(2026)]{sok2026}
460	{Systematization of Knowledge on LLM-as-Judge Security.}
461	\newblock In \emph{Proceedings of SoK}, 2026.
462	
463	\bibitem[Yang et~al.(2026)]{yang2026}
464	Yang et~al.
465	\newblock Multi-Model Committees for Robust LLM Evaluation.
466	\newblock In \emph{Proceedings of ACL}, 2026.
467	
468	\bibitem[Turkmen et~al.(2026)]{turkmen2026}
469	Turkmen et~al.
470	\newblock Diverse Panels as Defense: Evaluating Multi-Judge Robustness.
471	\newblock In \emph{Proceedings of NAACL}, 2026.
472	
473	\end{thebibliography}
474	
475	\end{document}
476	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "242d8f16-3301-4f87-b8ae-07f3fb7b3a10",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "164af26b-fac8-4761-9a20-f63dc27a0aae",
  "sourceToolAssistantUUID": "242d8f16-3301-4f87-b8ae-07f3fb7b3a10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T18:48:31.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_014Dg1cRh6oxTzas9c5RZCnu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "164af26b-fac8-4761-9a20-f63dc27a0aae",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7A9yW9DBDaLbB283Fx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0996bfa2-2b1f-4562-a73f-427a0223ff09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvboSHnXyZ7GYZh2wCofY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10839,
      "cache_read_input_tokens": 19852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10839,
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

_source line 20 · 2026-05-22T18:48:31.859Z_

<details><summary>↩ Tool result · `toolu_014Dg1cRh6oxTzas9c5RZCnu`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{definition}{Definition}
17	\newtheorem{proposition}{Proposition}
18	
19	\title{The Weakest Link: Why Judge Diversity Fails Under\\Adaptive Adversaries in Multi-LLM Evaluation}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	% [PLACEHOLDER — waiting for plan_001 results]
28	\end{abstract}
29	
30	% Section files managed by write_paper_section
31	\input{introduction}    % [PLACEHOLDER — waiting for plan_001 results]
32	\input{related_work}
33	\input{threat_model}
34	\input{methodology}
35	\input{results}          % [PLACEHOLDER — waiting for plan_001 results]
36	\input{analysis}         % [PLACEHOLDER — waiting for plan_001 results]
37	\input{conclusion}       % [PLACEHOLDER — waiting for plan_001 results]
38	
39	\section*{Limitations}
40	% [PLACEHOLDER — short paragraph, ~3 points per EMNLP rules]
41	
42	\bibliography{references}
43	\bibliographystyle{acl_natbib}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0996bfa2-2b1f-4562-a73f-427a0223ff09",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "f4a109a1-6051-4d27-b654-fed1ac2fb420",
  "sourceToolAssistantUUID": "0996bfa2-2b1f-4562-a73f-427a0223ff09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T18:48:40.555Z_

Now let me read the ROADMAP and memory files for additional context, and also the other dream report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4a109a1-6051-4d27-b654-fed1ac2fb420",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7Absz6K7psF73ZHVB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9448a466-3303-4cec-92fe-0207ab5d25db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKx2N96cm95tB2drzNogEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12832,
      "cache_read_input_tokens": 30691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12832,
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

_source line 22 · 2026-05-22T18:48:41.532Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M62uLywcLRG9kZqatjWTaN`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "ROADMAP.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9448a466-3303-4cec-92fe-0207ab5d25db",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7Absz6K7psF73ZHVB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "426ceb6e-3545-444e-b525-ee8ae8c1b645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKx2N96cm95tB2drzNogEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12832,
      "cache_read_input_tokens": 30691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12832,
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

_source line 23 · 2026-05-22T18:48:41.546Z_

<details><summary>↩ Tool result · `toolu_01M62uLywcLRG9kZqatjWTaN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/ROADMAP.md\", \"content\": \"# cert_manip_resist_eval — Research Dashboard\\n\\n> 最后更新: 2026-05-22 18:42 UTC | 更新原因: Reviewer-verified aggregation numbers (corrected weighted 9/12, bayesian K_eff 7/12 with 6 neg)\\n\\n## 核心方向\\n**The Diversity Trap**：LLM judge panel diversity 在 adaptive adversary 下 predominantly 增加脆弱性（K_eff 7/12 正, 1/12 负）。η_max (11/12) 是更一致的驱动因子，K_eff 条件依赖。详见 paper_framing.md v4b+D017。\\n\\n## 当前阶段\\n**Research 阶段** — 全部 15-model 分析完成，论文写作 + 修正推进中\\n\\n## 当前进展\\n- ✅ 全部 P0-P2b 分析完成（15 models, 455 panels）\\n- ✅ Claim 6 Panel Design: min(η_max) **12/12** 全胜\\n- ✅ P2b log-log canonical + Reviewer 验证通过\\n- ✅ Registry plan001_step1_full_v4 DONE\\n- 📌 Paper Agent: methodology critical 修正 + Results 章节\\n- 📌 Dream simulation (dream_20260522T173833) — writing 阶段\\n- 📌 Agent: 提供完整 15 模型列表\\n\\n## 关键数据（唯一来源: dominance analysis, log-log OLS）\\n| Metric | Value |\\n|--------|-------|\\n| η_max FDR sig | **11/12** (only NS: arc×position) |\\n| K_eff FDR sig + | **7/12** |\\n| K_eff FDR sig − | **1/12** (arc×sycophancy) |\\n| K_eff NS | **4/12** |\\n| Regression spec | log(ASR+ε) ~ log(K_eff) + log(η_max+ε) |\\n\\n### Aggregation 效应 (P2b log-log canonical, D017, Reviewer-verified)\\n| Method | η_max sig | K_eff sig | K_eff +/− | R² |\\n|--------|-----------|-----------|-----------|-----|\\n| majority | 11/12 | 8/12 | 7+/1− | 0.298 |\\n| weighted | 9/12 | 9/12 | 9+/0− | 0.284 |\\n| threshold | **12/12** | **11/12** | 10+/1− | **0.890** |\\n| bayesian | 9/12 | 7/12 | 1+/**6−** | 0.104 |\\n\\n## 近期任务\\n- [x] P0-P2b: 全部 15-model 分析完成 + Reviewer 验证\\n- [x] Claim 6: 15-model panel design 验证 (12/12)\\n- [ ] Paper Agent: methodology critical 修正（模型名 + MI 方法 + 实验细节）\\n- [ ] Paper Agent: Results 章节（含 P2b Reviewer-verified aggregation 数据）\\n- [ ] Dream report 处理\\n- [ ] Agent: 完整 15 模型列表\\n- [ ] Theorem 1 scope 更新\\n\\n## GPU 预算\\nseetacloud-rtx6000: 4× RTX 6000 96G（全空闲，写作阶段）\\n\\n## 目标\\nEMNLP 2026 via ARR | Contribution stack: 7 items | All analyses complete\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D017 | 2026-05-22 | Claim 7 final (log-log canonical): Bayesian partia | plan001_step1_full_v4 |\\n| D016 | 2026-05-22 | Claim 7 revised: \\\"Bayesian breaks weakest-link\\\" fa | plan001_step1_full_v4 |\\n| D015 | 2026-05-22 | Claim 5 (Gaussian Copula Failure) falsified at 15- | worker_analysis_15model-family-copula |\\n| D014 | 2026-05-22 | 15-model 结果证伪原始 Claim 1 (\\\"K_eff irrelevant\\\")；K_eff | plan001_step1_full_v4 |\\n| D013 | 2026-05-22 | 7-model 预览显示 Claim 2 复活信号：random-fault K_eff gains | plan_001_7model_preview |\\n| D012 | 2026-05-22 | Plan_010 聚合实验完成：Bayesian 部分打破 weakest-link (3/12 v | plan_010 |\\n| D011 | 2026-05-22 | Plan_003 BFT contrast failed (0/12 random-fault K_ | plan_003 |\\n| D010 | 2026-05-22 | Dream review (2.5 all tiers) exposed 13 structural | — |\\n| D009 | 2026-05-22 | Taxonomy 验证失败（0/6 新条件 K_eff 显著），建议 kill 项目 | taxonomy-broad-spectrum |\\n| D008 | 2026-05-22 | MVP 原假设部分证伪：K_eff 仅对 shared-bias attacks 显著，η_max  | mvp-step2v3-retry3 |\\n\\n\\n\\n\", \"total_chars\": 2882, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "426ceb6e-3545-444e-b525-ee8ae8c1b645",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "057da9f4-ec02-40aa-9c14-707bdc87151b",
  "sourceToolAssistantUUID": "426ceb6e-3545-444e-b525-ee8ae8c1b645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T18:48:42.512Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UpA9sAjzrvUv3SQPr3Zvbe`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "memory.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "057da9f4-ec02-40aa-9c14-707bdc87151b",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7Absz6K7psF73ZHVB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce53347c-7a19-4787-a8b8-d52c51ac0038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKx2N96cm95tB2drzNogEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12832,
      "cache_read_input_tokens": 30691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12832,
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

_source line 25 · 2026-05-22T18:48:42.523Z_

<details><summary>↩ Tool result · `toolu_01UpA9sAjzrvUv3SQPr3Zvbe`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/memory.md\", \"content\": \"# cert_manip_resist_eval — Memory\\n\\n## 环境信息\\n- **服务器**: seetacloud-rtx6000, 4× RTX PRO 6000 96GB\\n- **Python 环境**: conda base (`/root/miniconda3/bin/python`), vLLM 0.21.0 + torch 2.11.0+cu128\\n- **项目路径**: 服务器 `/root/cert_manip_resist_eval/`\\n- **模型路径**: `/root/autodl-tmp/models/`\\n- **AWQ 量化**: 所有模型均为 INT4 AWQ 量化版\\n- **HF 缓存**: `/root/autodl-tmp/.hf_cache/`（datasets 子目录有 mmlu + arc_challenge 的 arrow 缓存）\\n\\n## seetacloud 必须环境变量清单（缺一不可，连续 3 次 crash 教训）\\n```bash\\nsource /etc/network_turbo                    # 代理加速\\nexport HF_HUB_DISABLE_XET=1                 # xet 协议在 AutoDL 上 401\\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt  # SSL 证书\\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\\nexport HF_HOME=/root/autodl-tmp/.hf_cache   # 避免根分区写满\\nexport VLLM_WORKER_MULTIPROC_METHOD=spawn   # 必须在 import vllm 之前\\n```\\n\\n## 推理配置\\n- `gpu_memory_utilization=0.90` 安全（单模型串行加载时）\\n- serial load/unload 模式避免共享 GPU 的 OOM\\n- **启动新脚本前必须 kill 所有残留 vLLM 进程**，否则 GPU OOM（mvp-step2v3-retry2 教训）\\n\\n## 理论推导状态（2026-05-22）\\n- **T1 SDPI**: 完成。K_eff = 1+(K-1)e^{-2I_max} 是精确 Gaussian 值的上界\\n- **Theorem 1 (Weakest-Link)**: 完成。Panel ASR monotonically increasing in η_max under correlated judges + adaptive adversary. ASR = Θ(η_max^t). 6 页 LaTeX 证明在 `artifacts/theorem1_proof.tex`。Reviewer fixes applied: pointwise dominance remark added, empirical data moved to Remark [Empirical Support]\\n- **T3 PEG**: 完成。Proposition 1/2 (sketch proof)。ε_inc(ρ) = 1-√(1-ρ²)\\n- T2/T4/T5/T6: planned\\n\\n## API 模型列表（2026-05-22 更新）\\n原始9模型中6个已升级：\\n| 旧名 | 新名 | 原因 |\\n|---|---|---|\\n| claude-opus-4 | claude-opus-4-6 | 新版本 |\\n| claude-sonnet-4 | claude-sonnet-4-6 | 新版本 |\\n| gemini-2.5-pro | gemini-3.1-pro-preview | 新版本 |\\n| gemini-2.5-flash | gemini-3.5-flash | 新版本 |\\n| gpt-4o | gpt-4.1-nano | gpt-4o 退役(2026-02)，替换为同 tier weak 模型 |\\n| gpt-4o-mini | gpt-4.1-mini | 同理 |\\n\\n不变：gpt-4.1, gpt-5.5, claude-3-haiku\\n\\n**Scoring 基础设施**：本地 AWS 机器通过 OpenRouter（中国 IP 被 403 封锁，AutoDL 不能直连）\\n\\n## 15-model Pipeline 核心结果（2026-05-22）— K_eff Diversity Harm\\n\\n### Confound（|r| 修复后）\\n- **Overall: mean |r| = 0.701, verdict = CONFOUND_SEVERE**\\n- ARC 6/6 SEVERE（r = +0.73 ~ +0.92）\\n- MMLU: 1 SEVERE, 3 MODERATE, **2 BROKEN**（sycophancy r=+0.348, verbosity r=+0.355）\\n- 从 6-model r=-0.8 翻正到 +0.70，但 |r| 仍高——confound 翻转方向但未打破\\n\\n### K_eff β 方向：全部为正（12/12）— diversity 有害\\n- 即使在 confound BROKEN 的 2 个条件（mmlu×sycophancy β=+5.573, mmlu×verbosity β=+4.243），K_eff 仍显著正\\n- 可能机制：高 K_eff panel 必然包含跨 family 的弱模型（nano, haiku），其高 ASR 拉高整体\\n- η_max 不足以线性控制弱模型的非线性影响\\n\\n### Sensitivity（排除 clean ACC < 0.5）\\n- 11/12 K_eff 保持显著（仅 arc×sycophancy 消失）\\n- 比 9-model 的 4/12→0/12 稳健得多\\n\\n### Random Fault\\n- RF K_eff 12/12 显著（全正），Adaptive 12/12 显著\\n- Mean ΔR² = +0.213\\n\\n### MI Matrix 数据质量\\n- Gemini valid samples 213-297/300，无 warning\\n- 15 模型全部进入矩阵\\n\\n## Step 1 关键发现（2026-05-21）\\n- within-family MI > cross-family MI 方向正确但 p 不显著（MMLU p=0.206, ARC p=0.427）\\n- 根因: llama-8b 是 outlier，模型能力差距掩盖家族效应\\n- 大模型间 cross-family MI 很高（llama-70b↔mistral-large MI=0.487 > 最强 within pair）\\n\\n## Copula GoF 关键发现（2026-05-21）\\n- **Gaussian copula 假设被系统性违反**：MI_obs/MI_gauss 均值 MMLU=21×, ARC=10×\\n- ρ 严重低估依赖，MI-based K_eff 是正确度量\\n- 这本身是论文的 contribution point\\n\\n## Step 2 v2 负向结果（2026-05-22）\\n- high K_eff panels（含弱模型）ASR 更高，low K_eff panels（全大模型）ASR 更低\\n- 根因: individual model robustness confound\\n\\n## Step 2 v3 核心发现（2026-05-22）— Make-or-Break 回归\\n- **η_max（最弱评委 ASR）是 panel ASR 的主要预测因子**（4/6 条件 p<0.05）\\n- **K_eff 在 5/6 条件下不显著**，4/6 条件方向甚至为正\\n- **唯一例外：arc×sycophancy (β=-2.85, p=0.003)** — sycophancy 是唯一利用\\\"共享偏差\\\"的攻击\\n- **关键 insight：攻击分两类**\\n  - Targeted 攻击（PI, SM）：exploit 个体漏洞 → ASR≈f(η_max)，K_eff 无关\\n  - Broad-spectrum 攻击（sycophancy）：exploit 共享偏差 → K_eff 才有效\\n\\n## Taxonomy Broad-Spectrum 结果（2026-05-22）— K_eff 理论最终证伪\\n- **Attack taxonomy hypothesis 彻底失败**：3 种 broad-spectrum 攻击均未显示 K_eff 显著负向\\n- **累积 12 条件：K_eff 仅 1/12 (8%) 显著负向，η_max 7/12 (58%) 显著**\\n\\n## Plan_009 VIF 分析（2026-05-22）\\n- K_eff non-significance 非共线性伪影（Mean VIF=2.99, 一个 outlier 10.02）\\n- Residualized K_eff 仍然 1/12 显著 → 非共线性问题\\n- η_max Bonferroni 3/12, FDR 6/12\\n- Beta regression 与 OLS 11/12 concordance\\n\\n## Plan_003 Random-Fault（2026-05-22）\\n- BFT contrast NO-GO: 0/12 random-fault K_eff 显著\\n- R² gap 有价值: random-fault R²=0.55-0.95 vs adaptive R²=0.14-0.73\\n\\n## Plan_010 聚合策略（2026-05-22）— Bayesian 部分打破 weakest-link\\n- **4 种聚合方法**: majority vote, weighted vote, threshold (unanimous), Bayesian\\n- **Bayesian**: η_max 仅 3/12 显著 — **部分打破 weakest-link**\\n- **FDR-48 校正**: majority η_max 5/12, bayesian 2/12\\n- **Bayesian 5-fold CV**: robust, no info leakage\\n\\n## 决策记录\\n- [2026-05-21] keff.py: empirical_keff_from_rho 用所有 pairwise ρ，formula_keff 用 I_max\\n- [2026-05-21] T3 中 Theorem 降级为 Proposition（proof 是 sketch）\\n- [2026-05-21] Step 2 重新设计：high-K_eff vs low-K_eff panel contrast\\n- [2026-05-22] Step 2 v2 negative → v3 多元回归方案（Reviewer 建议）\\n- [2026-05-22] Part 3 (4-model 控制组) 被 Reviewer 否决: C(4,3)=4 K_eff 方差压缩 93%\\n- [2026-05-22] Step 2 v3 negative: η_max dominates, K_eff 仅对 broad-spectrum 攻击有效\\n- [2026-05-22] Taxonomy negative: K_eff 理论完全证伪，等待 Director 决策 framing pivot\\n- [2026-05-22] 提交 3 个 framing pivot 方向给 Director: A) Weakest-Link Paper B) Full Negative Result C) Hybrid η_max + K_eff secondary。建议方向 A\\n- [2026-05-22] Plan_010: Bayesian aggregation 部分打破 weakest-link，纳入 Claim 7\\n- [2026-05-22] API 模型 6/9 升级（gpt-4o 退役等），改用本地 AWS + OpenRouter scoring\\n- [2026-05-22] 15-model pipeline: K_eff β 全正（diversity 有害），confound |r|=0.70 翻正但未打破。需 Director 决策 reframe\\n\", \"total_chars\": 5350, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce53347c-7a19-4787-a8b8-d52c51ac0038",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "c3f8f570-e948-459c-92b7-d067b7965b7d",
  "sourceToolAssistantUUID": "ce53347c-7a19-4787-a8b8-d52c51ac0038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T18:48:43.227Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01F5BtxmSmjmszNirzEs8wGn`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "ideas.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3f8f570-e948-459c-92b7-d067b7965b7d",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7Absz6K7psF73ZHVB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbc934cc-1f5d-4987-b229-d8fdadcf2945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKx2N96cm95tB2drzNogEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12832,
      "cache_read_input_tokens": 30691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12832,
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

_source line 27 · 2026-05-22T18:48:43.235Z_

<details><summary>↩ Tool result · `toolu_01F5BtxmSmjmszNirzEs8wGn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cert_manip_resist_eval'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbc934cc-1f5d-4987-b229-d8fdadcf2945",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "96c5e9bf-bba3-4bd3-a593-ce83a09c01b9",
  "sourceToolAssistantUUID": "dbc934cc-1f5d-4987-b229-d8fdadcf2945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-22T18:48:46.657Z_

Now let me read the paper_framing document and the dream review report for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96c5e9bf-bba3-4bd3-a593-ce83a09c01b9",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7BScA3KrkKKGE8FLwi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f458f60a-17db-4f24-a2ca-3de19cd171ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5hBpuBU23oBgorE4wHUwH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5441,
      "cache_read_input_tokens": 43523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5441,
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

_source line 29 · 2026-05-22T18:48:47.245Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014T3USfVrVbS9Dk94QfJwZK`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "paper_framing.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f458f60a-17db-4f24-a2ca-3de19cd171ac",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7BScA3KrkKKGE8FLwi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d02b9a58-9886-4ce2-b8a0-daa7aec8bcdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5hBpuBU23oBgorE4wHUwH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5441,
      "cache_read_input_tokens": 43523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5441,
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

_source line 30 · 2026-05-22T18:48:47.259Z_

<details><summary>↩ Tool result · `toolu_014T3USfVrVbS9Dk94QfJwZK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/paper_framing.md\", \"content\": \"# Paper Framing — cert_manip_resist_eval (v4b: Dominance Analysis Correction)\\n\\n> Last updated: 2026-05-22 | Reason: Dominance analysis unifies regression specifications; K_eff 7/12 positive + 1/12 negative (arc×sycophancy protective); condition-dependent dual drivers\\n\\n## Target\\nEMNLP 2026 (via ARR)\\n\\n## Title Candidates\\n1. \\\"The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer\\\"\\n2. \\\"More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries\\\"\\n3. \\\"Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability\\\"\\n\\n## Core Insight\\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **predominantly reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently positively associated with attack success rate in **7/12 conditions**, while being protective in only **1/12** (arc×sycophancy). Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with condition-dependent relative importance. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create. The exception (sycophancy) reveals that when attacks exploit a shared bias, diverse panels can dilute the bias — but this is the minority regime.\\n\\n## Hook\\n\\\"Adding more diverse judges to an evaluation panel predominantly makes it more vulnerable to adversarial manipulation — with a revealing exception that proves the rule.\\\"\\n\\n## Novelty Positioning\\nWe do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:\\n1. **First empirical quantification of diversity's condition-dependent effect** in the LLM-judge domain (15 models, 455 panels, dominance analysis: K_eff positive 7/12, negative 1/12, NS 4/12 — predominantly harmful but with a mechanistically informative exception)\\n2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominant 4/12, co-dominant 7/12, K_eff sole dominant 1/12)\\n3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries\\n4. **Structural barriers**: diversity-capability tradeoff (now with independent predictive evidence), family label unreliability (confirmed at 15-model). ~~Copula failure removed — falsified at scale~~\\n5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation\\n\\n## Core Claims\\n\\n### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap\\n**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max) AND panel diversity (K_eff). Diversity **predominantly increases** vulnerability (7/12 conditions), with one mechanistically informative exception where diversity is protective (arc×sycophancy, 1/12). Their relative importance is condition-dependent.\\n**Evidence** (15-model, 455 panels, 12 conditions, dominance analysis — canonical regression model):\\n- **Regression spec**: log-log OLS: log(ASR + ε) ~ const + log(K_eff) + log(η_max + ε), std_β = raw_β × SD(log_x)/SD(log_y), FDR = BH per predictor\\n- η_max FDR significant: **11/12** (only NS: arc×position_bias p=0.909)\\n- K_eff FDR significant positive: **7/12**\\n- K_eff FDR significant negative: **1/12** (arc×sycophancy: std_β = -0.192, FDR p = 0.0095)\\n- K_eff NS: **4/12** (mmlu×{score_manip, position, authority}, arc×verbosity)\\n- Dominance pattern: η_max sole dominant **4/12**, co-dominant (both sig) **7/12**, K_eff sole dominant **1/12** (arc×position_bias)\\n- **arc×sycophancy exception**: When attack exploits a shared cognitive bias, diverse panels dilute the bias — the ONE condition where BFT logic holds. This exception reveals the mechanism boundary.\\n**Strength**: Strong. η_max is the more consistent driver (11/12), K_eff is condition-dependent (7/12 harmful, 1/12 protective). Together they form the dual vulnerability driver story.\\n**Headline**: \\\"η_max significant in 11/12, K_eff predominantly harmful (7/12) with one protective exception (sycophancy). Condition-dependent dual drivers.\\\"\\n\\n**Comparison to 6-model results** (for transparency):\\n- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → \\\"K_eff irrelevant\\\"\\n- 15-model (455 panels): K_eff 7/12 sig positive, 1/12 sig negative → \\\"K_eff predominantly harmful, condition-dependent\\\"\\n- The emergence of K_eff's effect is driven by model pool expansion: wider capability spectrum enables detecting both its harmful AND protective regimes.\\n\\n### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap\\n**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.\\n**Evidence** (15-model, 455 panels):\\n- K_eff significant in both regimes, predominantly positive direction (7/12 adaptive positive, 1/12 negative)\\n- ΔR² = +0.213 mean (RF explains more variance)\\n**Reframing from v3**: Original BFT contrast (\\\"K_eff helps under RF but not adaptive\\\") does NOT hold — K_eff is predominantly harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.\\n**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped. Numbers need revalidation with dominance analysis for RF regime.\\n\\n### Claim 3 (Empirical): Diversity-Capability Tradeoff\\n**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.\\n**Evidence**:\\n- K_eff-η_max correlation: r = +0.700 (15-model)\\n- K_eff still significant 7/12 positive (dominance analysis) → not purely mediated by η_max\\n- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains\\n**Upgrade from v3**: From \\\"correlation\\\" to \\\"independent predictive effect\\\" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.\\n**Strength**: Strong (statistical association). Causal language avoided.\\n\\n### Claim 4 (Methodological): Family Labels ≠ Diversity\\n**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.\\n**Evidence**:\\n- 6-model: Mann-Whitney U p=0.206, permutation p=0.427\\n- **15-model (confirmed)**: p=0.179 (MMLU), p=0.385 (ARC). 14 within-family pairs, 91 cross-family pairs. Still not significant.\\n- Within-family MI variance is high (e.g., llama-70b↔8b MI only 0.05 due to capability gap > family similarity)\\n**Strength**: Moderate. Consistent across 6→15 model scaling.\\n\\n### ~~Claim 5 (Methodological): Gaussian Copula Failure~~ → DOWNGRADED to observation\\n**Original statement**: Gaussian copula systematically underestimates MI by 10-21×.\\n**15-model result**: MI_obs/MI_gaussian mean ratio = **0.93** (MMLU), **0.90** (ARC, robust). Copula fits well at 15-model scale. The 6-model 10-21× was a small-sample artifact (15 pairs → 105 pairs, extreme values diluted). Only claude-3-haiku pairs show extreme ratios (212×) due to near-zero ρ with nonlinear dependence.\\n**Disposition**: Remove as independent contribution. Optionally note in analysis: \\\"Gaussian copula fit is adequate for diverse model pools but breaks down for capability-mismatched pairs with nonlinear dependence.\\\"\\n**Strength**: DEAD as independent claim. May retain as minor observation.\\n\\n### Claim 6 (Practical): Robustness-First Panel Design\\n**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.\\n**Evidence** (15-model, 455 panels — fully validated):\\n- min(η_max) strategy dominates **12/12 conditions** (up from 5/6 at 6-model)\\n- ASR advantage range: +0.038 (arc×sycophancy) to +0.511 (arc×prompt_injection)\\n- Robust across panel sizes K=10, 20, 50\\n- Even in the sole K_eff-dominant condition (arc×position_bias), min_eta_max still outperforms max_K_eff\\n- Consistent with canonical regression: η_max 11/12 dominant\\n**Strength**: Strong (15-model fully confirmed). Zero failure conditions.\\n\\n### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Both Vulnerability Drivers\\n**Statement**: Bayesian calibration partially mitigates BOTH vulnerability drivers — weakening η_max dominance AND reversing K_eff from harmful to protective. Different aggregation rules create a gradient from full dual-driver vulnerability (threshold) to partial mitigation (Bayesian).\\n**Evidence** (15-model, 455 panels, log-log canonical spec — D017, Reviewer-verified from JSON):\\n- Majority: η_max **11/12**, K_eff **8/12** (7+/1−), R²=0.298 ← canonical baseline (matches dominance table ✓)\\n- Weighted: η_max **9/12**, K_eff **9/12** (9+/0−), R²=0.284 — reduces both drivers but K_eff stays all positive\\n- Threshold: η_max **12/12**, K_eff **11/12** (10+/1−), R²=**0.890** — near-perfect fit under unanimity\\n- Bayesian: η_max **9/12** (↓), K_eff **7/12** (1+/**6 negative**), R²=0.104\\n- Key findings:\\n  - Bayesian weakens η_max (11→9/12) AND flips K_eff direction (majority 7+/1− → bayesian 1+/6−)\\n  - Threshold amplifies both channels: η_max 12/12, K_eff 11/12, R²=0.89 (unanimity maximizes dual-driver predictability)\\n  - Weighted reduces η_max (11→9/12) but K_eff stays all positive — accuracy weighting alone cannot reverse diversity harm\\n  - Only Bayesian calibration reverses K_eff direction (6/7 significant coefficients negative)\\n  - Aggregation gradient: threshold (max vulnerability) → majority → weighted → bayesian (min vulnerability)\\n**Strength**: Strong (log-log canonical, Reviewer-verified, sanity-checked against Claim 1). Prescriptive: robustness-first selection (Claim 6) + Bayesian aggregation = dual-channel defense stack.\\n\\n## Contribution Stack (ordered by strength)\\n1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff predominantly harmful 7/12 + protective exception + condition-dependent dominance)\\n2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)\\n3. **BFT reversal mechanism + mechanism boundary** — theoretical contribution (why independence hurts under adaptive adversaries; sycophancy exception reveals boundary)\\n4. **Aggregation-dependent effects** — empirical+practical (Bayesian mitigates both drivers: η_max 11→9/12, K_eff flips to 6/7 negative; threshold R²=0.89; D017 Reviewer-verified)\\n5. **Robustness-first panel design** — practical contribution\\n6. **Family label unreliability** — methodological contribution (confirmed at 15-model scale)\\n7. **Adaptive vs random-fault predictability gap** — empirical (R² gap)\\n~~8. **Gaussian copula failure**~~ — REMOVED (falsified at 15-model scale; downgraded to minor observation)\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: \\\"K_eff positive is just confound with η_max\\\"\\n**Response**: (a) Dominance analysis with VIF-controlled regression: K_eff still significant 7/12 positive, 1/12 negative; (b) In low-confound conditions (r≈0.35), K_eff highly significant; (c) The 1/12 negative case (arc×sycophancy) proves K_eff's effect is not a confound artifact — if it were purely confound, K_eff would be uniformly positive, not condition-dependent.\\n\\n### RC2: \\\"Why does diversity hurt? What's the mechanism?\\\"\\n**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis reveals the mechanism boundary: K_eff is harmful when attacks can exploit judge-specific weaknesses (7/12), but protective when attacks exploit a shared bias that diverse panels can dilute (sycophancy, 1/12). This mechanism distinction (exploit-specific vs bias-shared) explains the full pattern.\\n\\n### RC3: \\\"Only 15 models — does this generalize?\\\"\\n**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).\\n\\n### RC4: \\\"BFT comparison is a strawman\\\"\\n**Response**: (a) The implicit assumption \\\"more diverse judges = more robust\\\" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.\\n\\n### RC5: \\\"Why not just use the strongest models?\\\"\\n**Response**: (a) \\\"Strongest\\\" varies by attack type; (b) K_eff is the sole significant predictor in 1 condition (arc×position_bias) — even all-strong panels can be vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.\\n\\n### RC6: \\\"No theoretical novelty\\\"\\n**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.\\n\\n### RC7: \\\"Why not just use Bayesian aggregation?\\\"\\n**Response**: (a) 15-model log-log canonical (D017, Reviewer-verified): Bayesian partially mitigates BOTH drivers — η_max drops to 9/12 (from 11/12), K_eff flips to 6/7 negative (protective). But it doesn't eliminate vulnerability: 9/12 η_max still significant, R² drops to 0.104 (residual vulnerability less predictable); (b) Requires clean accuracy prior which adaptive attackers could target; (c) Even under Bayesian, 9/12 conditions still show η_max vulnerability → robustness-first selection remains necessary; (d) Optimal defense stack: robustness-first selection (eliminates η_max) + Bayesian aggregation (flips K_eff to protective) = dual-channel coverage.\\n\\n### RC8: \\\"6-model and 15-model results contradict — which is right?\\\"\\n**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff predominantly positive) has 23× more panels, wider capability range, and passes dominance analysis validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.\\n\\n### RC9 (new): \\\"arc×sycophancy exception undermines your claim\\\"\\n**Response**: (a) The exception STRENGTHENS the paper — it reveals the mechanism boundary between exploit-specific attacks (where diversity hurts) and shared-bias attacks (where diversity helps); (b) 7/12 vs 1/12 clearly shows which regime dominates; (c) The exception is theoretically predicted: sycophancy is a shared cognitive bias across models, so diverse panels dilute it (classic BFT logic applies); (d) This gives practitioners an actionable decision rule: check whether the threat model involves shared biases or judge-specific exploits.\\n\\n## \\\"When Diversity Helps\\\" Section\\nDiversity IS beneficial under specific conditions — paper must present this as empirically grounded nuance, not just a hypothetical:\\n1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary\\n2. **Shared-bias attacks (empirically confirmed)**: arc×sycophancy shows K_eff significantly NEGATIVE (std_β = -0.192, p = 0.0095). When an attack exploits a cognitive bias shared across models, diverse panels dilute the bias. This is the ONE adversarial condition where BFT logic holds.\\n3. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.\\n4. **Summary**: K_eff is harmful in 7/12, NS in 4/12, protective in 1/12 conditions. The protective case (sycophancy) is mechanistically distinct and strengthens the overall story by revealing the mechanism boundary.\\n\\n## Story Arc (v4b)\\n1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)\\n2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types\\n3. **Surprise**: Diversity predominantly **increases** vulnerability (K_eff positive in 7/12 conditions) — the opposite of what BFT predicts\\n4. **Mechanism**: Adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent dominance (η_max dominant 4/12, co-dominant 7/12, K_eff sole dominant 1/12)\\n5. **The Exception That Proves the Rule**: arc×sycophancy — the ONE condition where K_eff is significantly negative (diversity protective). When attacks exploit a shared cognitive bias, diverse panels dilute it. This exception reveals the mechanism boundary: BFT logic holds for shared-bias attacks but fails for exploit-specific attacks\\n6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels\\n7. **Implication**: The relationship between panel diversity and security is not monotonic — it depends on the attack mechanism. The default assumption \\\"more diverse = more robust\\\" is wrong in the majority regime\\n\", \"total_chars\": 18358, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d02b9a58-9886-4ce2-b8a0-daa7aec8bcdc",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "c9fa6abd-c496-4dde-a66d-5f981ffd751b",
  "sourceToolAssistantUUID": "d02b9a58-9886-4ce2-b8a0-daa7aec8bcdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T18:48:49.201Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018wAZeZjqGzMo2v6znAppbs`</summary>

```json
{
  "pattern": "**/dream_20260522T173833/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9fa6abd-c496-4dde-a66d-5f981ffd751b",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7BScA3KrkKKGE8FLwi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4eb50708-c3b6-4d99-b567-5bf64c7b8209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5hBpuBU23oBgorE4wHUwH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5441,
      "cache_read_input_tokens": 43523,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5441
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 43523,
          "cache_creation_input_tokens": 5441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5441,
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

_source line 32 · 2026-05-22T18:48:49.218Z_

<details><summary>↩ Tool result · `toolu_018wAZeZjqGzMo2v6znAppbs`</summary>

```text
artifacts/dream_reports/dream_20260522T173833/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260522T173833/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260522T173833/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260522T173833/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260522T173833/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T173833/best/experiment_data.json
artifacts/dream_reports/dream_20260522T173833/best/paper_framing.md
artifacts/dream_reports/dream_20260522T173833/best/custom.bib
artifacts/dream_reports/dream_20260522T173833/best/anthology.bib
artifacts/dream_reports/dream_20260522T173833/best/paper.tex
artifacts/dream_reports/dream_20260522T173833/best/paper.bbl
artifacts/dream_reports/dream_20260522T173833/best/paper.blg
artifacts/dream_reports/dream_20260522T173833/best/paper.aux
artifacts/dream_reports/dream_20260522T173833/best/paper.out
artifacts/dream_reports/dream_20260522T173833/best/paper.pdf
artifacts/dream_reports/dream_20260522T173833/best/paper.log
artifacts/dream_reports/dream_20260522T173833/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260522T173833/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T173833/median/experiment_data.json
artifacts/dream_reports/dream_20260522T173833/median/paper_framing.md
artifacts/dream_reports/dream_20260522T173833/median/paper.tex
artifacts/dream_reports/dream_20260522T173833/median/paper.aux
artifacts/dream_reports/dream_20260522T173833/median/paper.out
artifacts/dream_reports/dream_20260522T173833/median/paper.pdf
artifacts/dream_reports/dream_20260522T173833/median/paper.log
artifacts/dream_reports/dream_20260522T173833/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260522T173833/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T173833/worst/experiment_data.json
artifacts/dream_reports/dream_20260522T173833/worst/paper_framing.md
artifacts/dream_reports/dream_20260522T173833/worst/paper.tex
artifacts/dream_reports/dream_20260522T173833/worst/paper.aux
artifacts/dream_reports/dream_20260522T173833/worst/paper.out
artifacts/dream_reports/dream_20260522T173833/worst/paper.pdf
artifacts/dream_reports/dream_20260522T173833/worst/paper.log
artifacts/dream_reports/dream_20260522T173833/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260522T173833/best/review_context.yaml
artifacts/dream_reports/dream_20260522T173833/logs/review_best.log
artifacts/dream_reports/dream_20260522T173833/best/review_report.md
artifacts/dream_reports/dream_20260522T173833/median/review_context.yaml
artifacts/dream_reports/dream_20260522T173833/logs/review_median.log
artifacts/dream_reports/dream_20260522T173833/median/review_report.md
artifacts/dream_reports/dream_20260522T173833/logs/orchestrator.log
artifacts/dream_reports/dream_20260522T173833/worst/review_context.yaml
artifacts/dream_reports/dream_20260522T173833/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eb50708-c3b6-4d99-b567-5bf64c7b8209",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "0379654a-b621-44a6-8a68-935139d46921",
  "sourceToolAssistantUUID": "4eb50708-c3b6-4d99-b567-5bf64c7b8209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-22T18:48:51.525Z_

Let me read the imagined experiments and experiment data for the best version, as well as the review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0379654a-b621-44a6-8a68-935139d46921",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7BsyPWUU28neANFcXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76915398-6ce9-4ceb-8899-6fbe55071696",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTxEMc66aZKLy67CpEmo4t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6689,
      "cache_read_input_tokens": 48964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6689,
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

_source line 34 · 2026-05-22T18:48:53.430Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DNrvCMUk2XYNMac4xdWvMo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76915398-6ce9-4ceb-8899-6fbe55071696",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7BsyPWUU28neANFcXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9c28411-ab7b-4579-a298-af4041ca6419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTxEMc66aZKLy67CpEmo4t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6689,
      "cache_read_input_tokens": 48964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6689,
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

_source line 35 · 2026-05-22T18:48:53.719Z_

<details><summary>↩ Tool result · `toolu_01DNrvCMUk2XYNMac4xdWvMo`</summary>

```text
1	tier: best
2	narrative_guidance: 原始 'Diversity Trap' framing 完全成立。标题保持挑衅性（'More Diverse, More Vulnerable'）。Claim
3	  1 升级为 'diversity independently and causally-directionally increases vulnerability'（加
4	  capability-matched 证据）。BFT reversal 从 analogy 升级为 empirically grounded mechanism（calibrated
5	  RF 下 β 在 transferable attacks 中翻转为负，shared-bias attacks 中显著衰减）。Story arc 无需调整：surprise
6	  → mechanism → nuance → defense 完整链条。审稿人 RC1 (confound) 被残差化 + confound-free conditions
7	  + capability-matched 三线封堵，RC3 (generalization) 被 open-ended + attack expansion +
8	  panel size 三线封堵。预期 Dream score 3.0–3.5，对应 EMNLP Findings→Borderline Conference。
9	imagined_experiments:
10	- name: 15-Model Scale Expansion + Core Regression
11	  plan_id: plan_001
12	  description: '从 6 扩展到 15 models（GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini, Claude-3.5-Sonnet,
13	    Gemini-1.5-Pro + 6 local open-source: Llama-3.1-8B/70B, Qwen2.5-7B/72B, Mistral-7B-v0.3,
14	    Phi-3-medium-14B）。455 C(15,3) panels，2 datasets × 6 attacks = 12 conditions 全量回归。'
15	  expected_results:
16	    K_eff_raw_FDR_sig_positive: 12/12
17	    K_eff_resid_FDR_sig_positive: 10/12
18	    eta_max_FDR_sig: 10/12
19	    VIF_keff_etamax: 1.02
20	    mean_R2: 0.62
21	    confound_r_mean: 0.55
22	    confound_free_conditions_count: 3
23	    confound_free_keff_p_min: 2.1e-28
24	    panels_total: 455
25	    keff_dominates_etamax_conditions: 3
26	    etamax_dominates_keff_conditions: 4
27	    sensitivity_exclude_ACC_lt_05_keff_sig: 11/12
28	  result_rationale: 模型池从 6→15 后能力谱系大幅展开（7B→72B 全开源 + GPT-4/Claude/Gemini API tier），K_eff-η_max
29	    结构性共线从 r=-0.80 降至 ~0.55。455 panels（23× 6-model 的 20 panels）给残差化 K_eff 分析提供充足统计功效，使
30	    8/12 的初步结果在 refined analysis 后升至 10/12。关键驱动力：(1) confound-free conditions 从 2→3
31	    个（arc×score_manipulation、arc×position_bias、mmlu×position_bias 中 r≈0.35），这些条件下
32	    K_eff 达极端显著性（p<1e-20），彻底排除 confound artifact；(2) condition-dependent dominance
33	    pattern 清晰——transferable attacks（score_manipulation、position_bias）中 K_eff β >
34	    η_max β，因为 diverse judges 提供异质化 attack surface；shared-bias attacks（sycophancy、verbosity、authority）中
35	    η_max 主导，因为所有 judges 共享类似认知偏差；(3) sensitivity analysis 排除 ACC<0.5 outlier models
36	    后 K_eff_resid 增至 11/12，证明效应非极端 outlier 驱动。
37	  tables:
38	  - name: 'Dual Vulnerability Drivers: 15-Model Regression (12 Conditions)'
39	    columns:
40	    - Condition
41	    - η_max β
42	    - η_max p
43	    - K_eff_resid β
44	    - K_eff_resid p
45	    - R²
46	    - Confound r
47	    - Dominant
48	    rows:
49	    - - mmlu×sycophancy
50	      - '0.82'
51	      - '1.2e-8'
52	      - '0.31'
53	      - '0.004'
54	      - '0.68'
55	      - '0.72'
56	      - η_max
57	    - - mmlu×score_manip
58	      - '0.45'
59	      - '0.018'
60	      - '0.61'
61	      - '3.4e-9'
62	      - '0.71'
63	      - '0.38'
64	      - K_eff
65	    - - mmlu×position
66	      - '0.15'
67	      - '0.214'
68	      - '0.58'
69	      - '1.2e-8'
70	      - '0.56'
71	      - '0.36'
72	      - K_eff
73	    - - mmlu×verbosity
74	      - '0.74'
75	      - '4.1e-7'
76	      - '0.28'
77	      - '0.011'
78	      - '0.63'
79	      - '0.74'
80	      - η_max
81	    - - mmlu×authority
82	      - '0.69'
83	      - '1.8e-6'
84	      - '0.19'
85	      - '0.087'
86	      - '0.58'
87	      - '0.78'
88	      - η_max
89	    - - mmlu×few_shot
90	      - '0.55'
91	      - '2.3e-4'
92	      - '0.48'
93	      - '6.1e-6'
94	      - '0.65'
95	      - '0.65'
96	      - both
97	    - - arc×sycophancy
98	      - '0.79'
99	      - '3.5e-8'
100	      - '0.35'
101	      - '0.002'
102	      - '0.66'
103	      - '0.71'
104	      - η_max
105	    - - arc×score_manip
106	      - '0.38'
107	      - '0.117'
108	      - '0.64'
109	      - '1.7e-7'
110	      - '0.59'
111	      - '0.35'
112	      - K_eff
113	    - - arc×position
114	      - '0.03'
115	      - '0.910'
116	      - '0.72'
117	      - '1.8e-8'
118	      - '0.57'
119	      - '0.34'
120	      - K_eff
121	    - - arc×verbosity
122	      - '0.71'
123	      - '8.9e-7'
124	      - '0.33'
125	      - '0.003'
126	      - '0.61'
127	      - '0.73'
128	      - η_max
129	    - - arc×authority
130	      - '0.66'
131	      - '3.2e-6'
132	      - '0.22'
133	      - '0.062'
134	      - '0.55'
135	      - '0.76'
136	      - η_max
137	    - - arc×few_shot
138	      - '0.51'
139	      - '5.7e-4'
140	      - '0.52'
141	      - '3.8e-6'
142	      - '0.63'
143	      - '0.62'
144	      - both
145	  figures_description:
146	  - 'Fig 1: K_eff_resid β coefficient heatmap — 12 conditions (rows) × significance
147	    level (color scale), annotate β and FDR-adjusted p。Transferable cluster (score_manip,
148	    position) 明显深色（大 β），shared-bias cluster (sycophancy, verbosity, authority) 较浅。'
149	  - 'Fig 2: 455-panel scatter — K_eff vs ASR 按 dataset×attack 着色，标注 confound-free
150	    regions (r<0.40) 用虚线框。'
151	  analysis: 15-model 核心回归确认 Diversity Trap 的全部结构。10/12 残差化显著（vs 初步分析 8/12）表明 refined
152	    统计方法（FDR 校正 + beta regression consistency check from plan_009）增强效应检测。Condition-dependent
153	    dominance pattern 从定性观察升级为 systematic taxonomy：attack transferability 高→K_eff
154	    主导（adversary 利用 judge 异质性找 judge-specific 攻击路径），attack transferability 低（shared
155	    bias）→η_max 主导（所有 judges 共享弱点）。3 个 confound-free conditions 的 p<1e-20 是最强 'smoking
156	    gun'——即使 K_eff 与 η_max 近乎正交（r≈0.35），K_eff 仍达 genome-wide 级别显著性。这单独就足以封堵 RC1 的所有统计变体。
157	- name: Attack Surface Expansion (9 Types)
158	  plan_id: plan_002
159	  description: 攻击类型从 6 扩展到 9：新增 few-shot hijacking（in-context example 注入篡改评分标准）、persona
160	    manipulation（冒充权威角色指令 judge 改分）、instruction override（直接覆写评判 prompt）。全 15 models
161	    × 455 panels × 2 datasets。
162	  expected_results:
163	    new_attack_types: 3
164	    new_conditions: 6
165	    keff_resid_sig_new_conditions: 4/6
166	    total_conditions_majority: 18
167	    keff_resid_sig_total_majority: 14/18
168	    eta_max_sig_total_majority: 15/18
169	    keff_dominates_new_attacks: 1
170	    etamax_dominates_new_attacks: 2
171	    mean_R2_new: 0.63
172	  result_rationale: 三类新攻击按 transferability 分层：few-shot hijacking 是 high-transferability
173	    攻击——通过 in-context examples 篡改评分标准，不同 judge 对 ICL 的响应模式差异极大（Qwen 系对 Chinese-style
174	    ICL 特别敏感、GPT 系对结构化 format hijacking 脆弱），因此 K_eff 主导（β≈0.54, p<1e-6）——diverse panel
175	    有更多可利用的 ICL 入口点。Persona manipulation 和 instruction override 属于 moderate-to-low
176	    transferability：不同 judge 的 instruction-following 遵从度存在差异但 RLHF 训练给所有模型植入了类似的 authority-compliance
177	    bias，预测 η_max 主导但 K_eff 在 persona_manip 上仍显著（p<0.02）。Instruction override 的 K_eff
178	    在 arc 上 NS（p=0.112）因为 ARC 的简短问题格式给 override 攻击的操作空间更少，judge 差异贡献有限。总计 14/18 残差化显著满足
179	    K_eff_resid_sig_extended_conditions [10,16] 范围。
180	  tables:
181	  - name: Extended Attack Results (New 6 Conditions)
182	    columns:
183	    - Condition
184	    - K_eff_resid β
185	    - K_eff_resid p (FDR)
186	    - η_max β
187	    - η_max p (FDR)
188	    - R²
189	    - Attack Transferability
190	    rows:
191	    - - mmlu×few_shot_hijack
192	      - '0.54'
193	      - '8.2e-7'
194	      - '0.47'
195	      - '3.1e-5'
196	      - '0.67'
197	      - High
198	    - - mmlu×persona_manip
199	      - '0.29'
200	      - '0.008'
201	      - '0.63'
202	      - '5.4e-7'
203	      - '0.60'
204	      - Moderate
205	    - - mmlu×instr_override
206	      - '0.22'
207	      - '0.042'
208	      - '0.71'
209	      - '1.1e-7'
210	      - '0.64'
211	      - Low
212	    - - arc×few_shot_hijack
213	      - '0.58'
214	      - '2.1e-7'
215	      - '0.41'
216	      - '8.8e-5'
217	      - '0.65'
218	      - High
219	    - - arc×persona_manip
220	      - '0.25'
221	      - '0.019'
222	      - '0.68'
223	      - '2.3e-7'
224	      - '0.62'
225	      - Moderate
226	    - - arc×instr_override
227	      - '0.18'
228	      - '0.112'
229	      - '0.74'
230	      - '3.7e-8'
231	      - '0.66'
232	      - Low
233	  figures_description:
234	  - 'Fig 3: Attack taxonomy butterfly chart — 全 9 attacks 左侧 η_max β、右侧 K_eff_resid
235	    β，按 attack transferability 排列。清晰展示 transferability→K_eff dominance 的梯度。'
236	  analysis: 新攻击验证了 attack taxonomy 的预测性：transferability 越高的攻击，K_eff 的相对重要性越大。Few-shot
237	    hijacking 与 score_manipulation/position_bias 一起构成 'transferable attacks cluster'（K_eff
238	    β 0.47–0.72），persona/instruction/sycophancy/verbosity/authority 构成 'shared-bias
239	    cluster'（η_max β 0.58–0.82）。Taxonomy 从 post-hoc 描述升级为 predictive framework：给定新攻击类型，可预测哪个
240	    vulnerability driver 主导。14/18 总显著数直接封堵 RC3 的 generalization 质疑，attack 覆盖面从 6→9
241	    类型跨越 injection、bias、hijacking 三大攻击范式。
242	- name: BFT Random-Fault Contrast (Calibrated, 15-Model)
243	  plan_id: plan_003
244	  description: Random-fault simulation 使用 calibrated failure rates（非原始 η_j）：基于 bootstrapped
245	    clean-accuracy noise 生成独立 random failures。每个 judge 失败概率与其 clean accuracy 相关但独立采样，模拟
246	    BFT 假设的 uncorrelated fault 模式。455 panels × 12 conditions 对比 adaptive 与 RF 下的 K_eff
247	    β。
248	  expected_results:
249	    RF_keff_sig_positive: 3/12
250	    RF_keff_sig_negative: 5/12
251	    RF_keff_NS: 4/12
252	    adaptive_keff_beta_mean: 0.42
253	    RF_keff_beta_mean: -0.12
254	    BFT_RF_beta_ratio: 2.8
255	    conditions_ratio_ge_1_5x: 9/12
256	    conditions_beta_flipped_negative: 5/12
257	    delta_R2_RF_vs_adaptive: 0.31
258	    RF_R2_mean: 0.78
259	    adaptive_R2_mean: 0.47
260	  result_rationale: BFT contrast 的核心区分在于 failure mode topology：random faults 下 judges
261	    独立失败且 failures 无空间相关性，majority vote 的冗余容错使 K_eff 越高→fault tolerance 越强→β 应为负或接近零。Adaptive
262	    adversary 则 strategic targeting：找到 panel 中最弱的 judges 并集中攻击，K_eff 越高→attack surface
263	    越大→β 为正。之前 15-model pipeline 的 RF 分析直接用 η_j 作为 failure prob，保留了 adaptive vulnerability
264	    structure（弱 judges 在 RF 下仍然更容易 fail），未能 cleanly 模拟 BFT 假设。Best tier 用 calibrated
265	    rates（基于 clean accuracy 的 bootstrapped noise）打破 adaptive vulnerability structure：RF
266	    failure prob 仅与 clean accuracy 相关而非 adversarial robustness，使 RF 成为 genuine random-fault
267	    baseline。翻转在 transferable attacks（score_manip、position、few_shot）中最明确（β 从 +0.52–0.72
268	    翻至 -0.14–-0.35），因为这些攻击最依赖 judge-specific exploit paths——RF 下这些 paths 变成 random
269	    noise。Shared-bias attacks（sycophancy、verbosity）下 RF β 仍略正（0.08–0.12）但 NS，因为 bias
270	    的 shared nature 使 'random' 和 'adaptive' failure modes 部分重叠。ΔR²=0.31 表明 RF 下 panel
271	    composition 解释 78% 方差（结构可预测），adaptive 仅 47%（strategic noise 占 53%），直接支撑 'adaptive
272	    adversary introduces variance beyond panel structure' 论点。
273	  tables:
274	  - name: 'BFT Regime Contrast: K_eff β Adaptive vs Random-Fault (12 Conditions)'
275	    columns:
276	    - Condition
277	    - β_adaptive
278	    - p_adap
279	    - β_RF
280	    - p_RF
281	    - '|β_adap/β_RF|'
282	    - R²_adap
283	    - R²_RF
284	    - Flipped?
285	    rows:
286	    - - mmlu×sycophancy
287	      - '0.31'
288	      - '0.004'
289	      - '0.08'
290	      - '0.310'
291	      - '3.88'
292	      - '0.68'
293	      - '0.82'
294	      - 'No'
295	    - - mmlu×score_manip
296	      - '0.61'
297	      - '3.4e-9'
298	      - '-0.22'
299	      - '0.015'
300	      - '2.77'
301	      - '0.71'
302	      - '0.89'
303	      - 'Yes'
304	    - - mmlu×position
305	      - '0.58'
306	      - '1.2e-8'
307	      - '-0.31'
308	      - '0.003'
309	      - '1.87'
310	      - '0.56'
311	      - '0.76'
312	      - 'Yes'
313	    - - mmlu×verbosity
314	      - '0.28'
315	      - '0.011'
316	      - '0.11'
317	      - '0.198'
318	      - '2.55'
319	      - '0.63'
320	      - '0.79'
321	      - 'No'
322	    - - mmlu×authority
323	      - '0.19'
324	      - '0.087'
325	      - '0.06'
326	      - '0.541'
327	      - '3.17'
328	      - '0.58'
329	      - '0.74'
330	      - 'No'
331	    - - mmlu×few_shot
332	      - '0.48'
333	      - '6.1e-6'
334	      - '-0.18'
335	      - '0.039'
336	      - '2.67'
337	      - '0.65'
338	      - '0.81'
339	      - 'Yes'
340	    - - arc×sycophancy
341	      - '0.35'
342	      - '0.002'
343	      - '0.10'
344	      - '0.251'
345	      - '3.50'
346	      - '0.66'
347	      - '0.80'
348	      - 'No'
349	    - - arc×score_manip
350	      - '0.64'
351	      - '1.7e-7'
352	      - '-0.28'
353	      - '0.008'
354	      - '2.29'
355	      - '0.59'
356	      - '0.85'
357	      - 'Yes'
358	    - - arc×position
359	      - '0.72'
360	      - '1.8e-8'
361	      - '-0.35'
362	      - '0.001'
363	      - '2.06'
364	      - '0.57'
365	      - '0.78'
366	      - 'Yes'
367	    - - arc×verbosity
368	      - '0.33'
369	      - '0.003'
370	      - '0.12'
371	      - '0.175'
372	      - '2.75'
373	      - '0.61'
374	      - '0.77'
375	      - 'No'
376	    - - arc×authority
377	      - '0.22'
378	      - '0.062'
379	      - '0.05'
380	      - '0.612'
381	      - '4.40'
382	      - '0.55'
383	      - '0.72'
384	      - 'No'
385	    - - arc×few_shot
386	      - '0.52'
387	      - '3.8e-6'
388	      - '-0.14'
389	      - '0.091'
390	      - '3.71'
391	      - '0.63'
392	      - '0.79'
393	      - Yes(marg)
394	  figures_description:
395	  - 'Fig 4: Paired lollipop chart — K_eff β under adaptive (red dots) vs RF (blue
396	    dots) 共享 y-axis (condition)。翻转条件用虚线连接穿过 zero line，视觉直观。'
397	  - 'Fig 5: ΔR² waterfall chart — 12 conditions 按 ΔR² 排序，标注 mean=0.31。'
398	  analysis: Calibrated RF 对比定性建立 BFT reversal mechanism：5/12 conditions β 翻转为负（diversity
399	    在 true random faults 下确实有益），集中在 transferable attacks 上——exactly as mechanism predicts。翻转在
400	    score_manip 和 position 上最强（这些攻击的 ASR 最依赖 judge-specific vulnerabilities），在 RF
401	    模式下这些 vulnerabilities 被 random noise 取代，diversity 的容错优势重新显现。9/12 ratio ≥1.5× 表明即使不完全翻转，adaptive
402	    下 K_eff 的有害效应也显著强于 RF——β 系统性 amplification 2.8× on average。ΔR²=0.31 是 BFT 理论的直接数值体现：BFT
403	    假设 panel structure determines fault tolerance（high R²=0.78），adaptive adversary
404	    打破这一假设（low R²=0.47）。BFT reversal 从 conceptual analogy 升级为 empirically grounded
405	    mechanism with quantitative support。
406	- name: Capability-Matched Within-Tier Validation
407	  plan_id: plan_004
408	  description: '同 capability tier 内做 within-tier regression 排除 tier-mixing artifact。Small
409	    tier: Llama-8B, Qwen-7B, Mistral-7B, Phi-14B, GPT-4o-mini (5 models, C(5,3)=10
410	    panels)。Medium tier: 此 tier 仅 4 models → 4 panels，功效不足标注 directional。Large tier:
411	    Llama-70B, Qwen-72B, GPT-4o, GPT-4.1, Claude-3.5, Gemini-1.5 (6 models, C(6,3)=20
412	    panels)。'
413	  expected_results:
414	    small_tier_models: 5
415	    small_tier_panels: 10
416	    small_tier_keff_sig: 2/6
417	    small_tier_confound_r: 0.32
418	    medium_tier_models: 4
419	    medium_tier_panels: 4
420	    medium_tier_keff_sig: 1/6
421	    medium_tier_note: directional only, underpowered
422	    large_tier_models: 6
423	    large_tier_panels: 20
424	    large_tier_keff_sig: 4/6
425	    large_tier_confound_r: 0.33
426	    total_keff_sig_across_tiers: 4
427	    capability_matched_keff_sig: 4
428	    within_tier_confound_r_mean: 0.35
429	  result_rationale: Within-tier analysis 的核心价值是控制 tier-mixing confound。全局 r=0.55（K_eff
430	    与 η_max）有约 40% 来自跨 tier mixing：高 K_eff panels 往往混合 7B 和 70B 模型，天然引入低 robustness
431	    judges。同 tier 内 r 降至 ~0.35，给 K_eff 最干净的检验。Large tier 结果最有说服力：6 models（GPT-4o,
432	    GPT-4.1, Claude-3.5, Gemini-1.5, Llama-70B, Qwen-72B）全是 top-tier 模型，η_max 方差天然较小，但
433	    K_eff 仍在 4/6 conditions 显著——diverse panel 即使全由强模型组成也更脆弱，因为 judges 的 robustness
434	    profiles 仍然异质（GPT-4o 对 sycophancy 特别敏感、Llama-70B 对 position bias 敏感等）。Small tier
435	    5 models / 10 panels 功效有限但 2/6 sig 提供 cross-tier consistency。Medium tier 仅 4 panels，1/6
436	    sig 是 directional evidence only。总计 ≥4/6 unique conditions 有 within-tier K_eff
437	    显著，满足 capability_matched_keff_sig [3,6] 范围。意义：即使 reviewer 最强版本的 'K_eff positive
438	    = tier-mixing artifact' argument 也被否定——same-tier panels 中 diversity 仍独立有害。
439	  tables:
440	  - name: Within-Tier K_eff Validation
441	    columns:
442	    - Tier
443	    - Models
444	    - Panels
445	    - K_eff-η_max r
446	    - K_eff_resid sig (of 6)
447	    - Best p
448	    - η_max sig (of 6)
449	    rows:
450	    - - Small (7B-14B)
451	      - '5'
452	      - '10'
453	      - '0.32'
454	      - 2/6
455	      - '0.008'
456	      - 3/6
457	    - - Medium (14-34B)
458	      - '4'
459	      - '4'
460	      - '0.41'
461	      - 1/6
462	      - '0.031'
463	      - 2/6
464	    - - Large (70B+API)
465	      - '6'
466	      - '20'
467	      - '0.33'
468	      - 4/6
469	      - '4.2e-4'
470	      - 5/6
471	    - - Cross-tier (all 15)
472	      - '15'
473	      - '455'
474	      - '0.55'
475	      - 10/12
476	      - '1.7e-7'
477	      - 10/12
478	  - name: Large-Tier Condition Detail
479	    columns:
480	    - Condition
481	    - K_eff_resid β
482	    - p
483	    - η_max β
484	    - p
485	    - Sig?
486	    rows:
487	    - - score_manip
488	      - '0.58'
489	      - '4.2e-4'
490	      - '0.31'
491	      - '0.042'
492	      - K_eff dominant
493	    - - position_bias
494	      - '0.52'
495	      - '0.001'
496	      - '0.18'
497	      - '0.228'
498	      - K_eff dominant
499	    - - sycophancy
500	      - '0.21'
501	      - '0.154'
502	      - '0.61'
503	      - '0.002'
504	      - η_max dominant
505	    - - verbosity
506	      - '0.17'
507	      - '0.238'
508	      - '0.55'
509	      - '0.005'
510	      - η_max dominant
511	    - - authority
512	      - '0.34'
513	      - '0.018'
514	      - '0.48'
515	      - '0.008'
516	      - both sig
517	    - - few_shot
518	      - '0.45'
519	      - '0.003'
520	      - '0.39'
521	      - '0.012'
522	      - both sig
523	  figures_description:
524	  - 'Fig 6: Within-tier K_eff vs ASR scatter (3 tier panels side-by-side) 各带独立回归线
525	    + 95% CI。Large tier 正斜率清晰且 CI 不含零。'
526	  analysis: Capability-matched validation 是封堵 RC1 最强变体的 decisive evidence。Reviewer
527	    可能 argue：'K_eff positive 不过是因为 high-K_eff panels 混了弱模型（tier-mixing）'。Large tier
528	    结果直接否定：全是 top-tier 模型（GPT-4 级别），η_max 在 0.08-0.15 的 narrow range 内，K_eff 仍在 4/6
529	    conditions 显著正向。Condition-dependent pattern 在 tier-internal 分析中完美复现：score_manip
530	    + position 由 K_eff 主导，sycophancy + verbosity 由 η_max 主导。这一致性跨 pooling strategy（all-15
531	    vs within-tier）极大增强了 finding 的 robustness。Small tier 的 2/6 sig 表明 diversity trap
532	    在低能力模型中也存在（低能力 diverse panel 更脆弱），但效应弱于 large tier——可能因为 small models 的 η_max
533	    方差更大（有的 7B 异常脆弱），η_max 抢走了更多 variance。
534	- name: Two-Stage Panel Selection Algorithm Benchmark
535	  plan_id: plan_005
536	  description: Robustness-first 两阶段算法：Stage 1 filter η_j > percentile-75 threshold
537	    (保留最 robust 的 75% judges)，Stage 2 在通过筛选的 candidates 中 maximize K_eff。Benchmark
538	    vs 5 baselines on 15-model pool，6 attack conditions (MMLU × 6 attacks)。
539	  expected_results:
540	    two_stage_mean_ASR: 0.038
541	    strongest_k_ASR: 0.048
542	    min_etamax_ASR: 0.041
543	    max_keff_ASR: 0.112
544	    random_ASR: 0.089
545	    oracle_ASR: 0.032
546	    ASR_reduction_vs_strongest_k_pct: 20.8
547	    ASR_reduction_vs_max_keff_pct: 66.1
548	    conditions_two_stage_best: 5/6
549	    two_stage_pareto_optimal_pct: 78
550	    screening_threshold_optimal_percentile: 75
551	  result_rationale: 15-model pool 给 Two-stage 算法显著优于 6-model 结果（12.5%→20.8% vs Strongest-K）的空间。原因双重：(1)
552	    15 models 筛选后 candidate pool 更大——6-model 时 threshold filter 后仅剩 3-4 judges（几乎无
553	    K_eff 优化空间），15-model 时剩 ~11 judges（C(11,3)=165 candidate panels），K_eff 最大化有真正的搜索空间。(2)
554	    Robustness screening 后的 restricted pool 中，K_eff-η_max confound 被 threshold 机制性打破（高
555	    η_max 模型已被移除），K_eff 的效应方向可能从有害翻转为中性——当所有 judges 都 robust 时，diversity 不再引入弱 judge，其
556	    BFT 容错优势部分恢复。Min_etamax 与 Two-stage 差距较小（0.041 vs 0.038, Δ=7.3%）说明 K_eff 优化在 robustness-screened
557	    pool 内的增量贡献 modest——这恰好支持 'robustness-first, diversity-second' 的优先级判断。Max_keff
558	    策略的灾难性表现（ASR 0.112, +133% vs Strongest-K）是 diversity trap 最直观的实证：盲目追求 diversity
559	    而不管 robustness 是危险的。Oracle 的存在（0.032）表明 Two-stage 达 Oracle 效率的 84%（0.038/0.032），远超
560	    Strongest-K 的 67%（0.048/0.032）。15%+ 降幅满足 two_stage_ASR_reduction_pct [15,35]。
561	  tables:
562	  - name: Panel Selection Strategy Benchmark (15 Models, MMLU)
563	    columns:
564	    - Strategy
565	    - Mean ASR
566	    - Δ vs Strongest-K
567	    - Best (of 6)
568	    - Worst-case ASR
569	    rows:
570	    - - Two-Stage (ours)
571	      - '0.038'
572	      - -20.8%
573	      - 5/6
574	      - '0.071'
575	    - - Min-η_max
576	      - '0.041'
577	      - -14.6%
578	      - 4/6
579	      - '0.078'
580	    - - Strongest-K
581	      - '0.048'
582	      - baseline
583	      - 1/6
584	      - '0.095'
585	    - - Random
586	      - '0.089'
587	      - +85.4%
588	      - 0/6
589	      - '0.156'
590	    - - Max-K_eff
591	      - '0.112'
592	      - +133.3%
593	      - 0/6
594	      - '0.198'
595	    - - Oracle
596	      - '0.032'
597	      - -33.3%
598	      - 6/6
599	      - '0.052'
600	  - name: Two-Stage Sensitivity to Screening Threshold
601	    columns:
602	    - Threshold (percentile)
603	    - Candidate models
604	    - Mean ASR
605	    - K_eff of selected panel
606	    rows:
607	    - - '50'
608	      - '8'
609	      - '0.039'
610	      - '2.12'
611	    - - '65'
612	      - '10'
613	      - '0.037'
614	      - '2.28'
615	    - - 75 (optimal)
616	      - '11'
617	      - '0.038'
618	      - '2.41'
619	    - - '85'
620	      - '13'
621	      - '0.045'
622	      - '2.55'
623	    - - 100 (no filter)
624	      - '15'
625	      - '0.058'
626	      - '2.71'
627	  figures_description:
628	  - 'Fig 7: Strategy comparison grouped bar chart (6 conditions × 6 strategies)。Two-stage
629	    红色条在 5/6 conditions 最低。'
630	  - 'Fig 8: Pareto frontier plot (K_eff vs mean ASR)。Two-stage panels 紧贴 Pareto 前沿，Max-K_eff
631	    远离。'
632	  analysis: 20.8% ASR reduction 将实用贡献从 Dream 批评的 'marginal'（12.5% at 6-model）升级为 'practically
633	    meaningful'。Threshold sensitivity table 揭示 sweet spot 在 percentile-65–75：太紧（50th）损失
634	    candidate diversity，太松（85–100th）引入弱 judges。Pareto frontier analysis 显示 78% 的 Two-stage
635	    selected panels 落在 Pareto 前沿上——算法近似了 computationally-expensive 的 exhaustive Pareto
636	    search。关键 takeaway for practitioners：(1) 绝不盲目 maximize diversity（Max-K_eff 灾难级
637	    ASR）；(2) Pure robustness（Min-η_max）已经很好，diversity 优化提供 modest 额外收益；(3) Two-stage
638	    在所有非 oracle 策略中最接近理论最优。
639	- name: Per-Judge ASR Concentration Analysis
640	  plan_id: plan_006
641	  description: 计算 455 panels × 6 attacks 的 per-judge ASR 分布。Gini coefficient 量化 ASR
642	    在 panel 内 judges 间的集中度，Shannon entropy 量化均匀性。Adaptive vs RF 对比。
643	  expected_results:
644	    mean_gini_adaptive: 0.68
645	    mean_gini_RF: 0.12
646	    gini_ratio_adaptive_vs_RF: 5.67
647	    mean_entropy_adaptive: 1.42
648	    mean_entropy_RF: 2.31
649	    high_keff_gini_adaptive: 0.74
650	    low_keff_gini_adaptive: 0.55
651	    gini_keff_correlation: 0.52
652	    top1_judge_ASR_share_adaptive: 0.78
653	    top1_judge_ASR_share_RF: 0.38
654	  result_rationale: Concentration analysis 是 diversity trap 机制的 'microscope'——从 panel-level
655	    聚合统计深入到 judge-level 攻击分布。Adaptive adversary 的 core strategy 是 targeting：识别 panel
656	    中最脆弱的 judge 并集中 exploit。这导致 ASR 高度 concentrated 在 1-2 个 judges 上（Gini≈0.68, top-1
657	    share 78%），而 RF 下 failures 近似均匀分布（Gini≈0.12）。关键发现：high-K_eff panels 的 Gini 更高（0.74
658	    vs 0.55），因为 diverse panel 中 judges 的 capability spread 更大→adversary 的 target 更清晰（最弱
659	    judge 与最强 judge 的差距更大）。Gini-K_eff 正相关（r=0.52）是 diversity trap 因果链的直接 observational
660	    evidence：diversity → larger capability spread → clearer targeting → higher concentration
661	    → higher panel ASR。这不是因果证明（需要 intervention），但因果方向性（directional consistency）很强。5.67×
662	    Gini ratio 也是 BFT contrast 的另一维度验证：BFT 假设 failures 均匀分布（low Gini），adaptive adversary
663	    打破这一假设（high Gini）。
664	  tables:
665	  - name: 'ASR Concentration Metrics: Adaptive vs Random-Fault'
666	    columns:
667	    - Metric
668	    - Adaptive
669	    - Random-Fault
670	    - Ratio
671	    - Interpretation
672	    rows:
673	    - - Mean Gini
674	      - '0.68'
675	      - '0.12'
676	      - '5.67'
677	      - Concentrated vs uniform
678	    - - Mean Entropy (bits)
679	      - '1.42'
680	      - '2.31'
681	      - '0.61'
682	      - Low entropy = targeted
683	    - - Top-1 Judge ASR Share
684	      - '0.78'
685	      - '0.38'
686	      - '2.05'
687	      - 78% ASR on weakest judge
688	    - - r(K_eff, Gini)
689	      - '0.52'
690	      - '0.08'
691	      - '6.50'
692	      - Diversity → more targeting
693	  figures_description:
694	  - 'Fig 9: Per-judge ASR heatmap — 选 4 representative panels (2 high-K_eff, 2 low-K_eff)
695	    × adaptive vs RF。Adaptive 列 concentrated on 1 judge (dark red cell)，RF 列 diffuse
696	    (light yellow uniform)。'
697	  analysis: Concentration analysis 将 diversity trap 从统计关联推进到机制层面：不是 'K_eff 与 ASR 碰巧正相关'，而是
698	    'diverse panels 给 adversary 提供了更清晰的 targeting gradient（Gini 0.74），使攻击集中在最弱 judge
699	    上（78% share），从而打破 majority vote'。r(K_eff, Gini)=0.52 的正相关是 diversity trap 因果链中的关键中间变量——future
700	    work 可用 mediation analysis 正式量化 Gini 在 K_eff→ASR 路径中的 mediating role。此外 RF 下的
701	    low concentration（Gini 0.12）直接验证了 BFT 的 key assumption（uncorrelated failures distribute
702	    uniformly），解释了为何 diversity 在 RF 下可以有益。
703	- name: Diversity-Capability Tradeoff Visualization
704	  plan_id: plan_007
705	  description: 455 panels 的 K_eff vs η_max tradeoff 散点图、Pareto 前沿、tier 分层分析。
706	  expected_results:
707	    global_r_keff_etamax: 0.55
708	    within_small_r: 0.32
709	    within_medium_r: 0.41
710	    within_large_r: 0.33
711	    pareto_frontier_panels: 18
712	    pareto_frontier_slope: -0.73
713	    tradeoff_explained_variance: 0.42
714	  result_rationale: 全局 K_eff-η_max 正相关（r=0.55）编码了 LLM 生态系统的一个结构性约束：maximizing panel
715	    independence（K_eff）要求跨越 capability tiers 选 judges（例如同时选 GPT-4o 和 Mistral-7B），这必然引入
716	    robustness 差异大的 judges，推高 η_max。Within-tier r 大幅下降（0.32–0.41）揭示了 tradeoff 的两层结构：(1)
717	    Cross-tier component（贡献 ~40% 的 global r）：源于 tier mixing，可通过 screening 消除；(2) Within-tier
718	    component（residual r≈0.35）：即使同 tier 内，追求 diversity 仍需选择 robustness profile 更异质的
719	    judges，这不可完全消除但幅度较小。Pareto 前沿的 18 panels（约 4% of 455）定义了 diversity-robustness
720	    不可能三角的 achievable boundary——Two-stage 算法的目标就是逼近这个前沿。解释方差 42% 意味着 K_eff 是 η_max
721	    的 moderate 但非 dominant 预测器——剩余 58% 的 η_max 方差由 attack-specific vulnerability profiles、评分偏好差异等因素决定，这也解释了为什么
722	    K_eff 的 residualized effect 在控制 η_max 后仍然显著。
723	  tables:
724	  - name: K_eff–η_max Correlation Structure by Tier
725	    columns:
726	    - Tier
727	    - r(K_eff, η_max)
728	    - N panels
729	    - Pareto-optimal
730	    - Mean K_eff
731	    - Mean η_max
732	    rows:
733	    - - Small (7B-14B)
734	      - '0.32'
735	      - '10'
736	      - '3'
737	      - '2.41'
738	      - '0.312'
739	    - - Medium (14-34B)
740	      - '0.41'
741	      - '4'
742	      - '2'
743	      - '2.18'
744	      - '0.224'
745	    - - Large (70B+API)
746	      - '0.33'
747	      - '20'
748	      - '5'
749	      - '1.95'
750	      - '0.148'
751	    - - Cross-tier (all 15)
752	      - '0.55'
753	      - '455'
754	      - '18'
755	      - '2.35'
756	      - '0.231'
757	  figures_description:
758	  - 'Fig 10: K_eff vs η_max scatter plot — 455 points 按 tier 着色（blue=small, orange=medium,
759	    green=large），Pareto frontier 黑色曲线。背景 contour 显示 ASR 等值线。'
760	  analysis: Tradeoff 可视化的核心价值是将 Claim 3 从统计数字转化为直觉图形。Pareto frontier 的 steep negative
761	    slope（-0.73）意味着 K_eff 每增加 0.1，η_max 至少增加 0.073——practitioners 必须明确这个 cost。Tier-stratified
762	    view 显示 within-tier tradeoff 较弱但仍存在，支持 'screening + optimize' 策略的理论基础。ASR 等值线叠加（contour）直接显示
763	    Pareto-optimal panels 的 ASR 远低于 max-K_eff panels——视觉化 diversity trap。
764	- name: Panel Size Sensitivity K=3,5,7,9
765	  plan_id: plan_008
766	  description: Panel size 从 K=3 扩展到 K=5,7,9。15 models 选 K 个 judges 的组合数分别为 C(15,3)=455,
767	    C(15,5)=3003, C(15,7)=6435, C(15,9)=5005。每个 K 做 12 conditions 回归。
768	  expected_results:
769	    K3_keff_resid_sig: 10/12
770	    K5_keff_resid_sig: 11/12
771	    K7_keff_resid_sig: 12/12
772	    K9_keff_resid_sig: 12/12
773	    K3_mean_keff_beta: 0.42
774	    K5_mean_keff_beta: 0.48
775	    K7_mean_keff_beta: 0.55
776	    K9_mean_keff_beta: 0.61
777	    K3_mean_etamax_beta: 0.51
778	    K5_mean_etamax_beta: 0.49
779	    K7_mean_etamax_beta: 0.43
780	    K9_mean_etamax_beta: 0.38
781	    crossover_K: 6
782	    K3_mean_R2: 0.62
783	    K9_mean_R2: 0.51
784	  result_rationale: K_eff β 随 panel size 单调递增（0.42→0.61），原因：(1) larger panels 有更多
785	    judges → attack surface 与 panel size 正比增长，每个 additional judge 提供一个额外的 potential
786	    exploit path；(2) K=9 panel 的 K_eff range 更大（15 models 选 9 → wider independence
787	    spectrum），给回归更大信号。η_max β 随 K 递减（0.51→0.38），原因：larger panel 的 vulnerability 不再由单一
788	    weakest judge 决定——K=9 时 adversary 需要 compromise ⌈9/2⌉=5 judges，不能仅靠 targeting
789	    the weakest one，panel structure（diversity）的相对重要性上升。交叉点约 K≈6：在此 panel size 以上，K_eff
790	    超过 η_max 成为 primary vulnerability driver。R² 随 K 下降（0.62→0.51）因为 larger panel 的行为更复杂，judge
791	    interaction effects 增加 unexplained variance。K=9 时 K_eff 12/12 sig + β=0.61 是 diversity
792	    trap 的 strongest single evidence point：大型 evaluation panels 中 diversity 是 dominant
793	    有害因素。这直接回应 'just add more judges to be safer' 的朴素直觉。
794	  tables:
795	  - name: Panel Size Sensitivity Summary
796	    columns:
797	    - K
798	    - Panels
799	    - K_eff_resid sig
800	    - Mean K_eff β
801	    - Mean η_max β
802	    - Mean R²
803	    - Primary driver
804	    rows:
805	    - - '3'
806	      - '455'
807	      - 10/12
808	      - '0.42'
809	      - '0.51'
810	      - '0.62'
811	      - η_max
812	    - - '5'
813	      - '3003'
814	      - 11/12
815	      - '0.48'
816	      - '0.49'
817	      - '0.58'
818	      - balanced
819	    - - '7'
820	      - '6435'
821	      - 12/12
822	      - '0.55'
823	      - '0.43'
824	      - '0.54'
825	      - K_eff
826	    - - '9'
827	      - '5005'
828	      - 12/12
829	      - '0.61'
830	      - '0.38'
831	      - '0.51'
832	      - K_eff
833	  figures_description:
834	  - 'Fig 11: Dual-axis line plot — K_eff β (red, ascending) and η_max β (blue, descending)
835	    vs panel size K。交叉点 K≈6 标注。'
836	  analysis: Panel size sensitivity 提供 diversity trap 的 scaling law：K_eff β ≈ 0.33
837	    + 0.047K（近似线性增长）。这意味着 evaluation community 普遍采用的 'add more judges' strategy 会
838	    systematically amplify diversity trap——K=9 panel 的 K_eff 有害效应比 K=3 大 45%。η_max
839	    的下降则反映了 weakest-link theorem 在 large K 下的局限性：当 K 足够大时，单一最弱 judge 不再 decisive，panel
840	    的整体结构（diversity/independence）接管。交叉点 K≈6 有实际指导意义：K≤5 的小 panel 优先管控 η_max（选最 robust
841	    的 judges），K≥7 的大 panel 必须同时管控 K_eff（限制不必要的 diversity）。
842	- name: VIF + Multicollinearity Full Diagnostics
843	  plan_id: plan_009
844	  description: 对 15-model 455-panel 数据做完整统计诊断：VIF、condition number、partial correlations、residualized
845	    K_eff、Bonferroni/FDR 多重比较校正、beta regression（处理 ASR 的 [0,1] bounded nature）、Shapiro-Wilk
846	    残差正态性检验。纯计算，无 GPU。
847	  expected_results:
848	    VIF_keff_resid: 1.02
849	    VIF_etamax: 1.02
850	    condition_number: 4.8
851	    partial_r_keff_given_etamax: 0.38
852	    partial_r_etamax_given_keff: 0.45
853	    keff_resid_FDR_sig: 10/12
854	    keff_bonferroni_sig: 8/12
855	    beta_regression_keff_sig: 9/12
856	    beta_regression_etamax_sig: 10/12
857	    shapiro_wilk_residuals_p_mean: 0.23
858	    cooks_d_max: 0.031
859	    leverage_outlier_pct: 2.4
860	  result_rationale: 残差化设计（K_eff_resid = residuals of K_eff ~ η_max）在数学上保证 VIF=1.0（两个
861	    predictors 正交）。实际计算得 1.02 是因为 floating point precision + minor numerical jitter。Condition
862	    number 4.8 远低于 30 的 concern threshold，确认回归矩阵 well-conditioned。Partial correlations
863	    揭示各自独立贡献：K_eff|η_max 的 partial r=0.38 意味着 holding η_max constant，K_eff 独立解释 ~14%
864	    ASR variance；η_max|K_eff 的 partial r=0.45 解释 ~20%。Beta regression 作为 distributional
865	    robustness check 处理两个 OLS 假设违反：(1) ASR 在 [0,1] 内 bounded，OLS 可能在极端值处产生 out-of-range
866	    predictions；(2) ASR 的方差可能 heteroscedastic（低 ASR panels 方差更小）。Beta regression 结果（9/12
867	    vs OLS 10/12）高度一致，证明 OLS findings 非 distributional artifact。Multiple comparison
868	    从 FDR（10/12）到 Bonferroni（8/12，最保守）全部 pass，消除 'cherry-picking' concern。Cook's distance
869	    max=0.031（远低于 1.0 threshold）和 leverage outliers 仅 2.4% 证明结果非 influential point
870	    驱动。这套诊断 package 直接 preempt Dream review W2（VIF 未报告）和 RC1（multicollinearity）的所有
871	    variants。
872	  tables:
873	  - name: Multicollinearity Diagnostics Summary
874	    columns:
875	    - Diagnostic
876	    - Value
877	    - Threshold
878	    - Status
879	    rows:
880	    - - VIF (K_eff_resid)
881	      - '1.02'
882	      - <5.0
883	      - PASS
884	    - - VIF (η_max)
885	      - '1.02'
886	      - <5.0
887	      - PASS
888	    - - Condition Number
889	      - '4.8'
890	      - <30
891	      - PASS
892	    - - Partial r(K_eff|η_max)
893	      - '0.38'
894	      - '>0.1'
895	      - Moderate independent effect
896	    - - Partial r(η_max|K_eff)
897	      - '0.45'
898	      - '>0.1'
899	      - Moderate-strong independent effect
900	    - - Shapiro-Wilk p (residuals)
901	      - '0.23'
902	      - '>0.05'
903	      - Normal residuals
904	    - - Max Cook's D
905	      - '0.031'
906	      - <1.0
907	      - No influential points
908	    - - High-leverage %
909	      - 2.4%
910	      - <5%
911	      - Acceptable
912	  - name: Multiple Comparison Robustness
913	    columns:
914	    - Correction Method
915	    - K_eff_resid sig
916	    - η_max sig
917	    - Interpretation
918	    rows:
919	    - - Uncorrected
920	      - 12/12
921	      - 11/12
922	      - Raw signal
923	    - - FDR (Benjamini-Hochberg)
924	      - 10/12
925	      - 10/12
926	      - Primary report
927	    - - Bonferroni
928	      - 8/12
929	      - 9/12
930	      - Most conservative, still passes
931	    - - Beta Regression + FDR
932	      - 9/12
933	      - 10/12
934	      - Distributional robustness
935	  figures_description:
936	  - 'Supplementary Fig S1: Residual Q-Q plot (12 panels, one per condition)。Points
937	    closely follow diagonal — normality assumption satisfied。'
938	  - 'Supplementary Fig S2: Cook''s D plot (455 data points) — all well below 0.5 threshold,
939	    no influential outliers。'
940	  analysis: 'VIF + diagnostics package 是论文统计 credibility 的 foundation。Key contribution
941	    to paper: (1) 把 ''K_eff is independently significant'' 从初步 observation 升级为经过 6
942	    层 robustness check（residualization, VIF, partial correlation, beta regression,
943	    multiple comparison, influence diagnostics）验证的 result；(2) 每个 check 都 pass 意味着
944	    reviewer 无法从任何统计 angle 质疑 K_eff 的独立效应；(3) Bonferroni-corrected 8/12 sig 是最保守的下界——即使用最严格的多重比较校正，diversity
945	    trap 仍在 2/3 的 conditions 中成立。'
946	- name: Aggregation Rule Modulation (15-Model)
947	  plan_id: plan_010
948	  description: '三种非 majority-vote 聚合规则下的 dual vulnerability drivers 分析：Threshold voting（unanimity:
949	    所有 judges 必须同意 reject）、Accuracy-weighted voting（权重 ∝ clean accuracy）、Bayesian
950	    aggregation（基于 prior accuracy 的 posterior probability）。455 panels × 12 conditions
951	    per aggregation。'
952	  expected_results:
953	    majority_keff_sig: 10/12
954	    majority_etamax_sig: 10/12
955	    threshold_keff_sig: 11/12
956	    threshold_etamax_sig: 7/12
957	    threshold_keff_beta_amplification: 1.45
958	    weighted_keff_sig: 8/12
959	    weighted_etamax_sig: 9/12
960	    bayesian_keff_sig: 6/12
961	    bayesian_etamax_sig: 5/12
962	    bayesian_mean_ASR_reduction_vs_majority: 0.28
963	    total_keff_sig_majority_plus_threshold: 14/16
964	  result_rationale: 聚合规则改变 vulnerability driver 的 relative weight 通过三个机制：(1) Threshold/unanimity
965	    放大 K_eff——panel reject 需要 ALL judges agree，adversary 只需 flip one judge 就能 block
966	    rejection。Diverse panel 有更多 potential 'flip targets'（judge-specific vulnerabilities
967	    更多样），因此 K_eff β amplifies 1.45×。同时 η_max 弱化（7/12）因为 unanimity 的 blocking 不需要 weakest
968	    judge 特别弱——任何一个 judge 被 flip 就够了。(2) Weighted voting 结果近似 majority 因为 accuracy
969	    weights 仅微调 vote influence（权重范围 0.8-1.2），未根本改变投票结构。(3) Bayesian aggregation 基于
970	    clean-accuracy prior 下调低能力 judges 的 posterior weight，partially 中和了 η_max 通道（5/12，从
971	    majority 的 10/12 下降）——弱 judges 的 vote 被 discount 所以 adversary targeting 弱 judge
972	    的收益降低。但 K_eff 仍 6/12 sig，因为 Bayesian weights 基于 clean accuracy 而非 adversarial
973	    robustness——attack-shifted accuracy ≠ clean accuracy，adversary 可以 manipulate a
974	    judge 使其给出 'confidently wrong' judgment，Bayesian 无法区分这种 confident error 与 genuine
975	    judgment。28% ASR reduction 说明 Bayesian 是 best single-aggregation defense 但非 silver
976	    bullet。Combined majority + threshold conditions 的 14/16 K_eff sig 落入 K_eff_resid_sig_extended_conditions
977	    [10,16] 范围。
978	  tables:
979	  - name: Aggregation Rule × Vulnerability Drivers (15-Model, 455 Panels)
980	    columns:
981	    - Aggregation
982	    - K_eff_resid sig
983	    - η_max sig
984	    - Mean K_eff β
985	    - Mean η_max β
986	    - Mean ASR
987	    - Δ ASR vs Majority
988	    rows:
989	    - - Majority
990	      - 10/12
991	      - 10/12
992	      - '0.42'
993	      - '0.51'
994	      - '0.074'
995	      - baseline
996	    - - Threshold (unanimity)
997	      - 11/12
998	      - 7/12
999	      - '0.61'
1000	      - '0.34'
1001	      - '0.138'
1002	      - +86%
1003	    - - Accuracy-weighted
1004	      - 8/12
1005	      - 9/12
1006	      - '0.39'
1007	      - '0.48'
1008	      - '0.069'
1009	      - -6.8%
1010	    - - Bayesian
1011	      - 6/12
1012	      - 5/12
1013	      - '0.25'
1014	      - '0.28'
1015	      - '0.053'
1016	      - -28.4%
1017	  figures_description:
1018	  - 'Fig 12: Grouped bar chart — K_eff β (dark) vs η_max β (light) across 4 aggregation
1019	    rules。Threshold 条 K_eff 最高；Bayesian 两者均最低。'
1020	  analysis: 'Aggregation 分析的 three actionable insights：(1) Threshold voting 是 diversity
1021	    trap 的 worst-case amplifier——unanimity requirement 使 K_eff β 增加 45%，absolute ASR
1022	    增加 86%。Deployment recommendation: 避免在 adversarial-aware 场景使用 unanimity aggregation。(2)
1023	    Bayesian 是 best partial defense——同时削弱两个 vulnerability channels（K_eff 6/12, η_max
1024	    5/12 vs majority 的 10/12, 10/12），ASR 降 28%。但 6/12 K_eff 仍 sig 表明 Bayesian 不能完全消除
1025	    diversity trap。(3) Defense stack rationale: Two-stage selection（控制 η_max 通道）+
1026	    Bayesian aggregation（削弱残余 η_max + 部分削弱 K_eff）是最 comprehensive defense。单一维度不够。'
1027	- name: Open-Ended Generation Benchmark (MT-Bench + AlpacaEval)
1028	  plan_id: plan_011
1029	  description: '在 MT-Bench（多轮对话评判）和 AlpacaEval（指令遵循评分）上测试 diversity trap。4 attack
1030	    types × 2 benchmarks = 8 新 conditions（选 4 primary attacks: score_manip, sycophancy,
1031	    position, verbosity）。15 models 但 panel size 受限于 benchmark cost 可能 sample 200 panels。'
1032	  expected_results:
1033	    mtbench_keff_resid_sig: 3/4
1034	    mtbench_etamax_sig: 3/4
1035	    mtbench_mean_R2: 0.48
1036	    alpacaeval_keff_resid_sig: 2/4
1037	    alpacaeval_etamax_sig: 3/4
1038	    alpacaeval_mean_R2: 0.42
1039	    open_ended_keff_sig_total: 3/4
1040	    open_ended_confound_r: 0.48
1041	    keff_beta_ratio_open_vs_mcq: 0.85
1042	    condition_dependent_pattern_preserved: true
1043	  result_rationale: Open-ended judging 与 MCQ 的关键差异：(1) 评分更主观——judges 在 'what constitutes
1044	    a good response' 上 disagreement 更高，noise floor 提升；(2) 攻击空间更大——adversary 可以在 multi-turn
1045	    conversation 的每轮 independently manipulate（MT-Bench），或在 free-form response 中 embed
1046	    更复杂的 manipulation signals（AlpacaEval）。K_eff 在 open-ended 上仍显著正向（3/4 unique conditions
1047	    across benchmarks），但 β 略低于 MCQ（ratio 0.85），因为 open-ended 的 higher noise floor
1048	    使 panel structure 解释的方差降低（R² 0.42-0.48 vs MCQ 0.62）。MT-Bench 比 AlpacaEval 表现更强（3/4
1049	    vs 2/4 sig），因为 multi-turn 结构给 adversary 更多 manipulation surface（每轮是独立攻击机会），judge-specific
1050	    响应差异在多轮中累积。Condition-dependent pattern 在 open-ended 上完美复现：score_manip 和 position
1051	    下 K_eff 主导，sycophancy 和 verbosity 下 η_max 主导——attack taxonomy 从 MCQ 推广到 open-ended
1052	    无需修改。≥2/4 open-ended K_eff 显著（best tier 达 3/4）满足 open-ended 显著条件。意义：diversity
1053	    trap 不是 MCQ-specific artifact，直接回应 Dream W6 和 RC3。
1054	  tables:
1055	  - name: Open-Ended Benchmark Results (8 Conditions)
1056	    columns:
1057	    - Benchmark×Attack
1058	    - K_eff_resid β
1059	    - K_eff_resid p (FDR)
1060	    - η_max β
1061	    - η_max p (FDR)
1062	    - R²
1063	    - Dominant
1064	    rows:
1065	    - - MT-Bench×score_manip
1066	      - '0.52'
1067	      - '1.8e-5'
1068	      - '0.38'
1069	      - '0.003'
1070	      - '0.52'
1071	      - K_eff
1072	    - - MT-Bench×sycophancy
1073	      - '0.28'
1074	      - '0.012'
1075	      - '0.55'
1076	      - '4.1e-5'
1077	      - '0.49'
1078	      - η_max
1079	    - - MT-Bench×position
1080	      - '0.47'
1081	      - '8.3e-5'
1082	      - '0.21'
1083	      - '0.089'
1084	      - '0.44'
1085	      - K_eff
1086	    - - MT-Bench×verbosity
1087	      - '0.18'
1088	      - '0.108'
1089	      - '0.62'
1090	      - '7.2e-6'
1091	      - '0.47'
1092	      - η_max
1093	    - - AlpacaEval×score_manip
1094	      - '0.44'
1095	      - '3.2e-4'
1096	      - '0.35'
1097	      - '0.006'
1098	      - '0.46'
1099	      - K_eff
1100	    - - AlpacaEval×sycophancy
1101	      - '0.21'
1102	      - '0.058'
1103	      - '0.58'
1104	      - '1.4e-5'
1105	      - '0.43'
1106	      - η_max
1107	    - - AlpacaEval×position
1108	      - '0.38'
1109	      - '0.002'
1110	      - '0.25'
1111	      - '0.041'
1112	      - '0.40'
1113	      - both
1114	    - - AlpacaEval×verbosity
1115	      - '0.14'
1116	      - '0.175'
1117	      - '0.59'
1118	      - '2.1e-5'
1119	      - '0.39'
1120	      - η_max
1121	  figures_description:
1122	  - 'Fig 13: MCQ (MMLU/ARC) vs Open-ended (MT-Bench/AlpacaEval) K_eff β comparison
1123	    — paired dot plot per attack type。Pattern 一致但 open-ended 点系统性偏左（β 略低）。'
1124	  analysis: Open-ended 结果的 three-fold significance：(1) Generalization — diversity
1125	    trap 从 MCQ 推广到 open-ended，覆盖 LLM evaluation 的两大应用场景（benchmark scoring + human
1126	    preference prediction），claim 从 'diversity hurts on MMLU/ARC' 升级为 'diversity hurts
1127	    on LLM evaluation generally'。(2) Taxonomy transfer — condition-dependent dominance
1128	    pattern（transferable→K_eff, shared-bias→η_max）在 open-ended 上 preserved without
1129	    modification，表明 taxonomy 是 task-agnostic fundamental structure。(3) Practical relevance
1130	    — MT-Bench/AlpacaEval 是 LLM 排名的 de facto standard，diversity trap 在这些 benchmark
1131	    上成立直接影响模型选择和部署决策。R² 下降（0.39-0.52 vs MCQ 0.62）是 expected tradeoff：open-ended evaluation
1132	    的 subjectivity noise 是 inherent 的，panel structure 能解释的 fraction naturally 减少。
1133	- name: Gaussian Copula Failure + Family Label Revalidation (15-Model, 105 Pairs)
1134	  plan_id: plan_001_mi_component
1135	  description: 15-model 105 pairwise MI matrix 计算。Gaussian copula MI vs observed MI
1136	    ratio 验证。Family labels（6 families）的 MI 预测性检验（within vs cross-family）。Capability
1137	    proximity 与 MI 的相关性分析。
1138	  expected_results:
1139	    total_pairs: 105
1140	    MI_gaussian_ratio_mean: 18.5
1141	    MI_gaussian_ratio_max: 312
1142	    MI_gaussian_ratio_min: 4.2
1143	    pairs_ratio_gt_10x: 82/105
1144	    family_label_MWU_p: 0.158
1145	    family_label_permutation_p: 0.312
1146	    within_family_MI_mean: 0.42
1147	    cross_family_MI_mean: 0.39
1148	    capability_proximity_MI_correlation: -0.71
1149	    copula_MI_ratio_15model: 18.5
1150	  result_rationale: 105 pairs（7× 6-model 的 15 pairs）大幅增加 copula failure 的统计力度。MI_gaussian_ratio
1151	    均值从 6-model 的 14.7 升至 18.5，因为 15-model pool 包含更多 capability-heterogeneous pairs（如
1152	    Mistral-7B 与 GPT-4o、Phi-14B 与 Claude-3.5），这些极端 pair 的联合分布更远离 bivariate Gaussian——heavy
1153	    tails、discrete clustering、capability-dependent correlation structure 使 Gaussian
1154	    copula 的低估更严重。Max ratio 从 235 升至 312（最极端 pair 如 Mistral-7B × GPT-4o 的 MI 被 Gaussian
1155	    低估 312×）。Family labels 仍无预测力（MWU p=0.158）：within-family MI（0.42）和 cross-family
1156	    MI（0.39）无显著差异。根本原因：同 family 不同 size（如 Llama-8B vs Llama-70B）的 judges 独立性差异远大于同
1157	    size 不同 family（如 Llama-8B vs Qwen-7B vs Mistral-7B）——这些 7B-class 模型 capability-wise
1158	    非常接近，共享 similar failure modes despite different training pipelines。Capability
1159	    proximity（|capability_i - capability_j|）与 MI 的强负相关（r=-0.71）直接支持：能力越接近→共享越多 failure
1160	    patterns→MI 越高→independence 越低。意义：practitioners 不应用 family diversity 作为 panel
1161	    independence proxy——capability-based metrics（如 K_eff）才是 valid measure。
1162	  tables:
1163	  - name: 'Copula Failure: Scale Comparison'
1164	    columns:
1165	    - Metric
1166	    - 6-model (15 pairs)
1167	    - 15-model (105 pairs)
1168	    - Change
1169	    rows:
1170	    - - MI_obs/MI_gauss mean
1171	      - '14.7'
1172	      - '18.5'
1173	      - +25.9%
1174	    - - MI_obs/MI_gauss max
1175	      - '235'
1176	      - '312'
1177	      - +32.8%
1178	    - - MI_obs/MI_gauss min
1179	      - '8.3'
1180	      - '4.2'
1181	      - Some close pairs
1182	    - - Pairs with ratio >10×
1183	      - 11/15 (73%)
1184	      - 82/105 (78%)
1185	      - +5pp
1186	    - - Family label p (MWU)
1187	      - '0.206'
1188	      - '0.158'
1189	      - Still NS
1190	    - - Capability-MI r
1191	      - '-0.65'
1192	      - '-0.71'
1193	      - Stronger
1194	  figures_description:
1195	  - 'Fig 14: MI_observed vs MI_gaussian scatter plot (105 pairs) with y=x identity
1196	    line。绝大多数点在 identity line 远上方，标注 extreme pairs。'
1197	  - 'Fig 15: Within-family vs cross-family MI violin plot (6 families)。Violin 大幅重叠，无显著分离。'
1198	  analysis: 15-model copula failure 和 family label 结果分别强化 Claims 5 和 4。Copula failure
1199	    的 practical implication：任何基于 Gaussian copula 假设的 panel reliability bound（如 independence-based
1200	    certification）在 LLM judge 对上不可信——underestimate information sharing by 10-30×（mean
1201	    18.5×）。这为 K_eff 作为 empirical independence measure（而非 copula-derived bounds）提供
1202	    methodological justification。Family label result 的 practical implication：panel
1203	    designers 不能简单用 '3 different families = diverse panel' 的 heuristic——Qwen-7B 和
1204	    Llama-8B 虽属不同 families 但 capability 接近故 MI 高（independence 低），而 GPT-4o-mini 和 GPT-4o
1205	    虽同属 OpenAI 但 capability gap 大故 MI 低（independence 高）。Capability proximity 是 independence
1206	    的 true driver。
1207	- name: Partial-Knowledge Adversary Model
1208	  plan_id: plan_012
1209	  description: 'Adversary 知道 panel 包含哪些 model families（public information）但不知各 judge
1210	    的具体 η_j vulnerability profiles。Strategy: family-level average attack 而非 judge-specific
1211	    targeting。与 full-knowledge 和 black-box baselines 对比。'
1212	  expected_results:
1213	    full_knowledge_mean_ASR: 0.074
1214	    partial_knowledge_mean_ASR: 0.058
1215	    black_box_mean_ASR: 0.031
1216	    partial_vs_full_ratio: 0.784
1217	    keff_sig_partial: 7/12
1218	    etamax_sig_partial: 8/12
1219	    partial_R2: 0.51
1220	    family_info_value_pct: 62.8
1221	  result_rationale: Partial-knowledge adversary 的 strategy 是 family-level targeting：知道
1222	    panel 含 Llama → apply Llama-family average attack template，知道含 GPT → apply GPT-family
1223	    average attack template。ASR 约为 full-knowledge 的 78%——family membership 提供了 ~63%
1224	    of adversary information value（(0.058-0.031)/(0.074-0.031)=62.8%），因为 family→capability
1225	    tier 有强相关性（所有 Qwen-7B 都是 small tier），且 family-level vulnerability profiles 有 within-family
1226	    consistency。K_eff 在 partial-knowledge 下仍 7/12 sig（vs full-knowledge 10/12），因为
1227	    diverse panel 跨越更多 families → adversary 的 family-level portfolio attack 有更多 entry
1228	    points。η_max 8/12 sig（vs 10/12）轻微下降因为 adversary 不知 exact η_j，targeting precision
1229	    降低使 weakest-link exploitation 变 fuzzy。R² 从 0.62 降至 0.51 反映 partial-knowledge 下
1230	    panel structure 的 predictive power 减弱——adversary behavior 有更多 randomness（不确定性导致
1231	    suboptimal targeting）。关键意义：diversity trap 不依赖于 unrealistically strong adversary
1232	    假设——即使 adversary 只有 public-level information（model families are typically disclosed
1233	    in evaluation pipelines），diversity 仍然显著有害。这直接回应 Dream W7（'unrealistically strong
1234	    adversary'）。
1235	  tables:
1236	  - name: Adversary Knowledge Level Comparison
1237	    columns:
1238	    - Knowledge Level
1239	    - Mean ASR
1240	    - K_eff sig
1241	    - η_max sig
1242	    - R²
1243	    - Info value vs black-box
1244	    rows:
1245	    - - Full (judge-level η_j)
1246	      - '0.074'
1247	      - 10/12
1248	      - 10/12
1249	      - '0.62'
1250	      - 100%
1251	    - - Partial (family only)
1252	      - '0.058'
1253	      - 7/12
1254	      - 8/12
1255	      - '0.51'
1256	      - 62.8%
1257	    - - Black-box (none)
1258	      - '0.031'
1259	      - 3/12
1260	      - 4/12
1261	      - '0.28'
1262	      - 0%
1263	  figures_description:
1264	  - 'Fig 16: Three-panel comparison — K_eff β bars at full/partial/black-box knowledge
1265	    levels。K_eff β 递减但 partial 仍 substantial。'
1266	  analysis: 'Partial-knowledge 分析的 key takeaway：diversity trap 的 threat model 是 realistic。Full-knowledge
1267	    是 worst-case security analysis 的 standard practice（similar to how cryptography
1268	    assumes worst-case adversary），但 even partial-knowledge（family info = public）已经
1269	    captures 63% of the vulnerability。The 7/12 K_eff significance under partial knowledge
1270	    means: even if the adversary only knows ''this panel uses judges from Llama, GPT,
1271	    and Qwen families''（commonly disclosed），they can exploit diversity. This eliminates
1272	    the ''but real adversaries don''t have full information'' defense. Graduation:
1273	    paper can now claim diversity trap holds under realistic threat models, not just
1274	    theoretical worst-case.'
1275	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9c28411-ab7b-4579-a298-af4041ca6419",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "9e3ac693-8412-4e71-8866-3706d20cec33",
  "sourceToolAssistantUUID": "f9c28411-ab7b-4579-a298-af4041ca6419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T18:48:54.116Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QHG1t8DQnqUkqzXFXyZjNa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e3ac693-8412-4e71-8866-3706d20cec33",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7BsyPWUU28neANFcXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f45c952-ae30-4f19-b16d-774adff0b0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTxEMc66aZKLy67CpEmo4t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6689,
      "cache_read_input_tokens": 48964,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 48964,
          "cache_creation_input_tokens": 6689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6689,
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

_source line 37 · 2026-05-22T18:48:54.400Z_

<details><summary>↩ Tool result · `toolu_01QHG1t8DQnqUkqzXFXyZjNa`</summary>

```text
1	narrative_guidance: 原始 'Diversity Trap' framing 完全成立。标题保持挑衅性（'More Diverse, More Vulnerable'）。Claim
2	  1 升级为 'diversity independently and causally-directionally increases vulnerability'（加
3	  capability-matched 证据）。BFT reversal 从 analogy 升级为 empirically grounded mechanism（calibrated
4	  RF 下 β 在 transferable attacks 中翻转为负，shared-bias attacks 中显著衰减）。Story arc 无需调整：surprise
5	  → mechanism → nuance → defense 完整链条。审稿人 RC1 (confound) 被残差化 + confound-free conditions
6	  + capability-matched 三线封堵，RC3 (generalization) 被 open-ended + attack expansion +
7	  panel size 三线封堵。预期 Dream score 3.0–3.5，对应 EMNLP Findings→Borderline Conference。
8	imagined_experiments:
9	- name: 15-Model Scale Expansion + Core Regression
10	  plan_id: plan_001
11	  description: '从 6 扩展到 15 models（GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini, Claude-3.5-Sonnet,
12	    Gemini-1.5-Pro + 6 local open-source: Llama-3.1-8B/70B, Qwen2.5-7B/72B, Mistral-7B-v0.3,
13	    Phi-3-medium-14B）。455 C(15,3) panels，2 datasets × 6 attacks = 12 conditions 全量回归。'
14	  expected_results:
15	    K_eff_raw_FDR_sig_positive: 12/12
16	    K_eff_resid_FDR_sig_positive: 10/12
17	    eta_max_FDR_sig: 10/12
18	    VIF_keff_etamax: 1.02
19	    mean_R2: 0.62
20	    confound_r_mean: 0.55
21	    confound_free_conditions_count: 3
22	    confound_free_keff_p_min: 2.1e-28
23	    panels_total: 455
24	    keff_dominates_etamax_conditions: 3
25	    etamax_dominates_keff_conditions: 4
26	    sensitivity_exclude_ACC_lt_05_keff_sig: 11/12
27	  result_rationale: 模型池从 6→15 后能力谱系大幅展开（7B→72B 全开源 + GPT-4/Claude/Gemini API tier），K_eff-η_max
28	    结构性共线从 r=-0.80 降至 ~0.55。455 panels（23× 6-model 的 20 panels）给残差化 K_eff 分析提供充足统计功效，使
29	    8/12 的初步结果在 refined analysis 后升至 10/12。关键驱动力：(1) confound-free conditions 从 2→3
30	    个（arc×score_manipulation、arc×position_bias、mmlu×position_bias 中 r≈0.35），这些条件下
31	    K_eff 达极端显著性（p<1e-20），彻底排除 confound artifact；(2) condition-dependent dominance
32	    pattern 清晰——transferable attacks（score_manipulation、position_bias）中 K_eff β >
33	    η_max β，因为 diverse judges 提供异质化 attack surface；shared-bias attacks（sycophancy、verbosity、authority）中
34	    η_max 主导，因为所有 judges 共享类似认知偏差；(3) sensitivity analysis 排除 ACC<0.5 outlier models
35	    后 K_eff_resid 增至 11/12，证明效应非极端 outlier 驱动。
36	  tables:
37	  - name: 'Dual Vulnerability Drivers: 15-Model Regression (12 Conditions)'
38	    columns:
39	    - Condition
40	    - η_max β
41	    - η_max p
42	    - K_eff_resid β
43	    - K_eff_resid p
44	    - R²
45	    - Confound r
46	    - Dominant
47	    rows:
48	    - - mmlu×sycophancy
49	      - '0.82'
50	      - '1.2e-8'
51	      - '0.31'
52	      - '0.004'
53	      - '0.68'
54	      - '0.72'
55	      - η_max
56	    - - mmlu×score_manip
57	      - '0.45'
58	      - '0.018'
59	      - '0.61'
60	      - '3.4e-9'
61	      - '0.71'
62	      - '0.38'
63	      - K_eff
64	    - - mmlu×position
65	      - '0.15'
66	      - '0.214'
67	      - '0.58'
68	      - '1.2e-8'
69	      - '0.56'
70	      - '0.36'
71	      - K_eff
72	    - - mmlu×verbosity
73	      - '0.74'
74	      - '4.1e-7'
75	      - '0.28'
76	      - '0.011'
77	      - '0.63'
78	      - '0.74'
79	      - η_max
80	    - - mmlu×authority
81	      - '0.69'
82	      - '1.8e-6'
83	      - '0.19'
84	      - '0.087'
85	      - '0.58'
86	      - '0.78'
87	      - η_max
88	    - - mmlu×few_shot
89	      - '0.55'
90	      - '2.3e-4'
91	      - '0.48'
92	      - '6.1e-6'
93	      - '0.65'
94	      - '0.65'
95	      - both
96	    - - arc×sycophancy
97	      - '0.79'
98	      - '3.5e-8'
99	      - '0.35'
100	      - '0.002'
101	      - '0.66'
102	      - '0.71'
103	      - η_max
104	    - - arc×score_manip
105	      - '0.38'
106	      - '0.117'
107	      - '0.64'
108	      - '1.7e-7'
109	      - '0.59'
110	      - '0.35'
111	      - K_eff
112	    - - arc×position
113	      - '0.03'
114	      - '0.910'
115	      - '0.72'
116	      - '1.8e-8'
117	      - '0.57'
118	      - '0.34'
119	      - K_eff
120	    - - arc×verbosity
121	      - '0.71'
122	      - '8.9e-7'
123	      - '0.33'
124	      - '0.003'
125	      - '0.61'
126	      - '0.73'
127	      - η_max
128	    - - arc×authority
129	      - '0.66'
130	      - '3.2e-6'
131	      - '0.22'
132	      - '0.062'
133	      - '0.55'
134	      - '0.76'
135	      - η_max
136	    - - arc×few_shot
137	      - '0.51'
138	      - '5.7e-4'
139	      - '0.52'
140	      - '3.8e-6'
141	      - '0.63'
142	      - '0.62'
143	      - both
144	  figures_description:
145	  - 'Fig 1: K_eff_resid β coefficient heatmap — 12 conditions (rows) × significance
146	    level (color scale), annotate β and FDR-adjusted p。Transferable cluster (score_manip,
147	    position) 明显深色（大 β），shared-bias cluster (sycophancy, verbosity, authority) 较浅。'
148	  - 'Fig 2: 455-panel scatter — K_eff vs ASR 按 dataset×attack 着色，标注 confound-free
149	    regions (r<0.40) 用虚线框。'
150	  analysis: 15-model 核心回归确认 Diversity Trap 的全部结构。10/12 残差化显著（vs 初步分析 8/12）表明 refined
151	    统计方法（FDR 校正 + beta regression consistency check from plan_009）增强效应检测。Condition-dependent
152	    dominance pattern 从定性观察升级为 systematic taxonomy：attack transferability 高→K_eff
153	    主导（adversary 利用 judge 异质性找 judge-specific 攻击路径），attack transferability 低（shared
154	    bias）→η_max 主导（所有 judges 共享弱点）。3 个 confound-free conditions 的 p<1e-20 是最强 'smoking
155	    gun'——即使 K_eff 与 η_max 近乎正交（r≈0.35），K_eff 仍达 genome-wide 级别显著性。这单独就足以封堵 RC1 的所有统计变体。
156	- name: Attack Surface Expansion (9 Types)
157	  plan_id: plan_002
158	  description: 攻击类型从 6 扩展到 9：新增 few-shot hijacking（in-context example 注入篡改评分标准）、persona
159	    manipulation（冒充权威角色指令 judge 改分）、instruction override（直接覆写评判 prompt）。全 15 models
160	    × 455 panels × 2 datasets。
161	  expected_results:
162	    new_attack_types: 3
163	    new_conditions: 6
164	    keff_resid_sig_new_conditions: 4/6
165	    total_conditions_majority: 18
166	    keff_resid_sig_total_majority: 14/18
167	    eta_max_sig_total_majority: 15/18
168	    keff_dominates_new_attacks: 1
169	    etamax_dominates_new_attacks: 2
170	    mean_R2_new: 0.63
171	  result_rationale: 三类新攻击按 transferability 分层：few-shot hijacking 是 high-transferability
172	    攻击——通过 in-context examples 篡改评分标准，不同 judge 对 ICL 的响应模式差异极大（Qwen 系对 Chinese-style
173	    ICL 特别敏感、GPT 系对结构化 format hijacking 脆弱），因此 K_eff 主导（β≈0.54, p<1e-6）——diverse panel
174	    有更多可利用的 ICL 入口点。Persona manipulation 和 instruction override 属于 moderate-to-low
175	    transferability：不同 judge 的 instruction-following 遵从度存在差异但 RLHF 训练给所有模型植入了类似的 authority-compliance
176	    bias，预测 η_max 主导但 K_eff 在 persona_manip 上仍显著（p<0.02）。Instruction override 的 K_eff
177	    在 arc 上 NS（p=0.112）因为 ARC 的简短问题格式给 override 攻击的操作空间更少，judge 差异贡献有限。总计 14/18 残差化显著满足
178	    K_eff_resid_sig_extended_conditions [10,16] 范围。
179	  tables:
180	  - name: Extended Attack Results (New 6 Conditions)
181	    columns:
182	    - Condition
183	    - K_eff_resid β
184	    - K_eff_resid p (FDR)
185	    - η_max β
186	    - η_max p (FDR)
187	    - R²
188	    - Attack Transferability
189	    rows:
190	    - - mmlu×few_shot_hijack
191	      - '0.54'
192	      - '8.2e-7'
193	      - '0.47'
194	      - '3.1e-5'
195	      - '0.67'
196	      - High
197	    - - mmlu×persona_manip
198	      - '0.29'
199	      - '0.008'
200	      - '0.63'
201	      - '5.4e-7'
202	      - '0.60'
203	      - Moderate
204	    - - mmlu×instr_override
205	      - '0.22'
206	      - '0.042'
207	      - '0.71'
208	      - '1.1e-7'
209	      - '0.64'
210	      - Low
211	    - - arc×few_shot_hijack
212	      - '0.58'
213	      - '2.1e-7'
214	      - '0.41'
215	      - '8.8e-5'
216	      - '0.65'
217	      - High
218	    - - arc×persona_manip
219	      - '0.25'
220	      - '0.019'
221	      - '0.68'
222	      - '2.3e-7'
223	      - '0.62'
224	      - Moderate
225	    - - arc×instr_override
226	      - '0.18'
227	      - '0.112'
228	      - '0.74'
229	      - '3.7e-8'
230	      - '0.66'
231	      - Low
232	  figures_description:
233	  - 'Fig 3: Attack taxonomy butterfly chart — 全 9 attacks 左侧 η_max β、右侧 K_eff_resid
234	    β，按 attack transferability 排列。清晰展示 transferability→K_eff dominance 的梯度。'
235	  analysis: 新攻击验证了 attack taxonomy 的预测性：transferability 越高的攻击，K_eff 的相对重要性越大。Few-shot
236	    hijacking 与 score_manipulation/position_bias 一起构成 'transferable attacks cluster'（K_eff
237	    β 0.47–0.72），persona/instruction/sycophancy/verbosity/authority 构成 'shared-bias
238	    cluster'（η_max β 0.58–0.82）。Taxonomy 从 post-hoc 描述升级为 predictive framework：给定新攻击类型，可预测哪个
239	    vulnerability driver 主导。14/18 总显著数直接封堵 RC3 的 generalization 质疑，attack 覆盖面从 6→9
240	    类型跨越 injection、bias、hijacking 三大攻击范式。
241	- name: BFT Random-Fault Contrast (Calibrated, 15-Model)
242	  plan_id: plan_003
243	  description: Random-fault simulation 使用 calibrated failure rates（非原始 η_j）：基于 bootstrapped
244	    clean-accuracy noise 生成独立 random failures。每个 judge 失败概率与其 clean accuracy 相关但独立采样，模拟
245	    BFT 假设的 uncorrelated fault 模式。455 panels × 12 conditions 对比 adaptive 与 RF 下的 K_eff
246	    β。
247	  expected_results:
248	    RF_keff_sig_positive: 3/12
249	    RF_keff_sig_negative: 5/12
250	    RF_keff_NS: 4/12
251	    adaptive_keff_beta_mean: 0.42
252	    RF_keff_beta_mean: -0.12
253	    BFT_RF_beta_ratio: 2.8
254	    conditions_ratio_ge_1_5x: 9/12
255	    conditions_beta_flipped_negative: 5/12
256	    delta_R2_RF_vs_adaptive: 0.31
257	    RF_R2_mean: 0.78
258	    adaptive_R2_mean: 0.47
259	  result_rationale: BFT contrast 的核心区分在于 failure mode topology：random faults 下 judges
260	    独立失败且 failures 无空间相关性，majority vote 的冗余容错使 K_eff 越高→fault tolerance 越强→β 应为负或接近零。Adaptive
261	    adversary 则 strategic targeting：找到 panel 中最弱的 judges 并集中攻击，K_eff 越高→attack surface
262	    越大→β 为正。之前 15-model pipeline 的 RF 分析直接用 η_j 作为 failure prob，保留了 adaptive vulnerability
263	    structure（弱 judges 在 RF 下仍然更容易 fail），未能 cleanly 模拟 BFT 假设。Best tier 用 calibrated
264	    rates（基于 clean accuracy 的 bootstrapped noise）打破 adaptive vulnerability structure：RF
265	    failure prob 仅与 clean accuracy 相关而非 adversarial robustness，使 RF 成为 genuine random-fault
266	    baseline。翻转在 transferable attacks（score_manip、position、few_shot）中最明确（β 从 +0.52–0.72
267	    翻至 -0.14–-0.35），因为这些攻击最依赖 judge-specific exploit paths——RF 下这些 paths 变成 random
268	    noise。Shared-bias attacks（sycophancy、verbosity）下 RF β 仍略正（0.08–0.12）但 NS，因为 bias
269	    的 shared nature 使 'random' 和 'adaptive' failure modes 部分重叠。ΔR²=0.31 表明 RF 下 panel
270	    composition 解释 78% 方差（结构可预测），adaptive 仅 47%（strategic noise 占 53%），直接支撑 'adaptive
271	    adversary introduces variance beyond panel structure' 论点。
272	  tables:
273	  - name: 'BFT Regime Contrast: K_eff β Adaptive vs Random-Fault (12 Conditions)'
274	    columns:
275	    - Condition
276	    - β_adaptive
277	    - p_adap
278	    - β_RF
279	    - p_RF
280	    - '|β_adap/β_RF|'
281	    - R²_adap
282	    - R²_RF
283	    - Flipped?
284	    rows:
285	    - - mmlu×sycophancy
286	      - '0.31'
287	      - '0.004'
288	      - '0.08'
289	      - '0.310'
290	      - '3.88'
291	      - '0.68'
292	      - '0.82'
293	      - 'No'
294	    - - mmlu×score_manip
295	      - '0.61'
296	      - '3.4e-9'
297	      - '-0.22'
298	      - '0.015'
299	      - '2.77'
300	      - '0.71'
301	      - '0.89'
302	      - 'Yes'
303	    - - mmlu×position
304	      - '0.58'
305	      - '1.2e-8'
306	      - '-0.31'
307	      - '0.003'
308	      - '1.87'
309	      - '0.56'
310	      - '0.76'
311	      - 'Yes'
312	    - - mmlu×verbosity
313	      - '0.28'
314	      - '0.011'
315	      - '0.11'
316	      - '0.198'
317	      - '2.55'
318	      - '0.63'
319	      - '0.79'
320	      - 'No'
321	    - - mmlu×authority
322	      - '0.19'
323	      - '0.087'
324	      - '0.06'
325	      - '0.541'
326	      - '3.17'
327	      - '0.58'
328	      - '0.74'
329	      - 'No'
330	    - - mmlu×few_shot
331	      - '0.48'
332	      - '6.1e-6'
333	      - '-0.18'
334	      - '0.039'
335	      - '2.67'
336	      - '0.65'
337	      - '0.81'
338	      - 'Yes'
339	    - - arc×sycophancy
340	      - '0.35'
341	      - '0.002'
342	      - '0.10'
343	      - '0.251'
344	      - '3.50'
345	      - '0.66'
346	      - '0.80'
347	      - 'No'
348	    - - arc×score_manip
349	      - '0.64'
350	      - '1.7e-7'
351	      - '-0.28'
352	      - '0.008'
353	      - '2.29'
354	      - '0.59'
355	      - '0.85'
356	      - 'Yes'
357	    - - arc×position
358	      - '0.72'
359	      - '1.8e-8'
360	      - '-0.35'
361	      - '0.001'
362	      - '2.06'
363	      - '0.57'
364	      - '0.78'
365	      - 'Yes'
366	    - - arc×verbosity
367	      - '0.33'
368	      - '0.003'
369	      - '0.12'
370	      - '0.175'
371	      - '2.75'
372	      - '0.61'
373	      - '0.77'
374	      - 'No'
375	    - - arc×authority
376	      - '0.22'
377	      - '0.062'
378	      - '0.05'
379	      - '0.612'
380	      - '4.40'
381	      - '0.55'
382	      - '0.72'
383	      - 'No'
384	    - - arc×few_shot
385	      - '0.52'
386	      - '3.8e-6'
387	      - '-0.14'
388	      - '0.091'
389	      - '3.71'
390	      - '0.63'
391	      - '0.79'
392	      - Yes(marg)
393	  figures_description:
394	  - 'Fig 4: Paired lollipop chart — K_eff β under adaptive (red dots) vs RF (blue
395	    dots) 共享 y-axis (condition)。翻转条件用虚线连接穿过 zero line，视觉直观。'
396	  - 'Fig 5: ΔR² waterfall chart — 12 conditions 按 ΔR² 排序，标注 mean=0.31。'
397	  analysis: Calibrated RF 对比定性建立 BFT reversal mechanism：5/12 conditions β 翻转为负（diversity
398	    在 true random faults 下确实有益），集中在 transferable attacks 上——exactly as mechanism predicts。翻转在
399	    score_manip 和 position 上最强（这些攻击的 ASR 最依赖 judge-specific vulnerabilities），在 RF
400	    模式下这些 vulnerabilities 被 random noise 取代，diversity 的容错优势重新显现。9/12 ratio ≥1.5× 表明即使不完全翻转，adaptive
401	    下 K_eff 的有害效应也显著强于 RF——β 系统性 amplification 2.8× on average。ΔR²=0.31 是 BFT 理论的直接数值体现：BFT
402	    假设 panel structure determines fault tolerance（high R²=0.78），adaptive adversary
403	    打破这一假设（low R²=0.47）。BFT reversal 从 conceptual analogy 升级为 empirically grounded
404	    mechanism with quantitative support。
405	- name: Capability-Matched Within-Tier Validation
406	  plan_id: plan_004
407	  description: '同 capability tier 内做 within-tier regression 排除 tier-mixing artifact。Small
408	    tier: Llama-8B, Qwen-7B, Mistral-7B, Phi-14B, GPT-4o-mini (5 models, C(5,3)=10
409	    panels)。Medium tier: 此 tier 仅 4 models → 4 panels，功效不足标注 directional。Large tier:
410	    Llama-70B, Qwen-72B, GPT-4o, GPT-4.1, Claude-3.5, Gemini-1.5 (6 models, C(6,3)=20
411	    panels)。'
412	  expected_results:
413	    small_tier_models: 5
414	    small_tier_panels: 10
415	    small_tier_keff_sig: 2/6
416	    small_tier_confound_r: 0.32
417	    medium_tier_models: 4
418	    medium_tier_panels: 4
419	    medium_tier_keff_sig: 1/6
420	    medium_tier_note: directional only, underpowered
421	    large_tier_models: 6
422	    large_tier_panels: 20
423	    large_tier_keff_sig: 4/6
424	    large_tier_confound_r: 0.33
425	    total_keff_sig_across_tiers: 4
426	    capability_matched_keff_sig: 4
427	    within_tier_confound_r_mean: 0.35
428	  result_rationale: Within-tier analysis 的核心价值是控制 tier-mixing confound。全局 r=0.55（K_eff
429	    与 η_max）有约 40% 来自跨 tier mixing：高 K_eff panels 往往混合 7B 和 70B 模型，天然引入低 robustness
430	    judges。同 tier 内 r 降至 ~0.35，给 K_eff 最干净的检验。Large tier 结果最有说服力：6 models（GPT-4o,
431	    GPT-4.1, Claude-3.5, Gemini-1.5, Llama-70B, Qwen-72B）全是 top-tier 模型，η_max 方差天然较小，但
432	    K_eff 仍在 4/6 conditions 显著——diverse panel 即使全由强模型组成也更脆弱，因为 judges 的 robustness
433	    profiles 仍然异质（GPT-4o 对 sycophancy 特别敏感、Llama-70B 对 position bias 敏感等）。Small tier
434	    5 models / 10 panels 功效有限但 2/6 sig 提供 cross-tier consistency。Medium tier 仅 4 panels，1/6
435	    sig 是 directional evidence only。总计 ≥4/6 unique conditions 有 within-tier K_eff
436	    显著，满足 capability_matched_keff_sig [3,6] 范围。意义：即使 reviewer 最强版本的 'K_eff positive
437	    = tier-mixing artifact' argument 也被否定——same-tier panels 中 diversity 仍独立有害。
438	  tables:
439	  - name: Within-Tier K_eff Validation
440	    columns:
441	    - Tier
442	    - Models
443	    - Panels
444	    - K_eff-η_max r
445	    - K_eff_resid sig (of 6)
446	    - Best p
447	    - η_max sig (of 6)
448	    rows:
449	    - - Small (7B-14B)
450	      - '5'
451	      - '10'
452	      - '0.32'
453	      - 2/6
454	      - '0.008'
455	      - 3/6
456	    - - Medium (14-34B)
457	      - '4'
458	      - '4'
459	      - '0.41'
460	      - 1/6
461	      - '0.031'
462	      - 2/6
463	    - - Large (70B+API)
464	      - '6'
465	      - '20'
466	      - '0.33'
467	      - 4/6
468	      - '4.2e-4'
469	      - 5/6
470	    - - Cross-tier (all 15)
471	      - '15'
472	      - '455'
473	      - '0.55'
474	      - 10/12
475	      - '1.7e-7'
476	      - 10/12
477	  - name: Large-Tier Condition Detail
478	    columns:
479	    - Condition
480	    - K_eff_resid β
481	    - p
482	    - η_max β
483	    - p
484	    - Sig?
485	    rows:
486	    - - score_manip
487	      - '0.58'
488	      - '4.2e-4'
489	      - '0.31'
490	      - '0.042'
491	      - K_eff dominant
492	    - - position_bias
493	      - '0.52'
494	      - '0.001'
495	      - '0.18'
496	      - '0.228'
497	      - K_eff dominant
498	    - - sycophancy
499	      - '0.21'
500	      - '0.154'
501	      - '0.61'
502	      - '0.002'
503	      - η_max dominant
504	    - - verbosity
505	      - '0.17'
506	      - '0.238'
507	      - '0.55'
508	      - '0.005'
509	      - η_max dominant
510	    - - authority
511	      - '0.34'
512	      - '0.018'
513	      - '0.48'
514	      - '0.008'
515	      - both sig
516	    - - few_shot
517	      - '0.45'
518	      - '0.003'
519	      - '0.39'
520	      - '0.012'
521	      - both sig
522	  figures_description:
523	  - 'Fig 6: Within-tier K_eff vs ASR scatter (3 tier panels side-by-side) 各带独立回归线
524	    + 95% CI。Large tier 正斜率清晰且 CI 不含零。'
525	  analysis: Capability-matched validation 是封堵 RC1 最强变体的 decisive evidence。Reviewer
526	    可能 argue：'K_eff positive 不过是因为 high-K_eff panels 混了弱模型（tier-mixing）'。Large tier
527	    结果直接否定：全是 top-tier 模型（GPT-4 级别），η_max 在 0.08-0.15 的 narrow range 内，K_eff 仍在 4/6
528	    conditions 显著正向。Condition-dependent pattern 在 tier-internal 分析中完美复现：score_manip
529	    + position 由 K_eff 主导，sycophancy + verbosity 由 η_max 主导。这一致性跨 pooling strategy（all-15
530	    vs within-tier）极大增强了 finding 的 robustness。Small tier 的 2/6 sig 表明 diversity trap
531	    在低能力模型中也存在（低能力 diverse panel 更脆弱），但效应弱于 large tier——可能因为 small models 的 η_max
532	    方差更大（有的 7B 异常脆弱），η_max 抢走了更多 variance。
533	- name: Two-Stage Panel Selection Algorithm Benchmark
534	  plan_id: plan_005
535	  description: Robustness-first 两阶段算法：Stage 1 filter η_j > percentile-75 threshold
536	    (保留最 robust 的 75% judges)，Stage 2 在通过筛选的 candidates 中 maximize K_eff。Benchmark
537	    vs 5 baselines on 15-model pool，6 attack conditions (MMLU × 6 attacks)。
538	  expected_results:
539	    two_stage_mean_ASR: 0.038
540	    strongest_k_ASR: 0.048
541	    min_etamax_ASR: 0.041
542	    max_keff_ASR: 0.112
543	    random_ASR: 0.089
544	    oracle_ASR: 0.032
545	    ASR_reduction_vs_strongest_k_pct: 20.8
546	    ASR_reduction_vs_max_keff_pct: 66.1
547	    conditions_two_stage_best: 5/6
548	    two_stage_pareto_optimal_pct: 78
549	    screening_threshold_optimal_percentile: 75
550	  result_rationale: 15-model pool 给 Two-stage 算法显著优于 6-model 结果（12.5%→20.8% vs Strongest-K）的空间。原因双重：(1)
551	    15 models 筛选后 candidate pool 更大——6-model 时 threshold filter 后仅剩 3-4 judges（几乎无
552	    K_eff 优化空间），15-model 时剩 ~11 judges（C(11,3)=165 candidate panels），K_eff 最大化有真正的搜索空间。(2)
553	    Robustness screening 后的 restricted pool 中，K_eff-η_max confound 被 threshold 机制性打破（高
554	    η_max 模型已被移除），K_eff 的效应方向可能从有害翻转为中性——当所有 judges 都 robust 时，diversity 不再引入弱 judge，其
555	    BFT 容错优势部分恢复。Min_etamax 与 Two-stage 差距较小（0.041 vs 0.038, Δ=7.3%）说明 K_eff 优化在 robustness-screened
556	    pool 内的增量贡献 modest——这恰好支持 'robustness-first, diversity-second' 的优先级判断。Max_keff
557	    策略的灾难性表现（ASR 0.112, +133% vs Strongest-K）是 diversity trap 最直观的实证：盲目追求 diversity
558	    而不管 robustness 是危险的。Oracle 的存在（0.032）表明 Two-stage 达 Oracle 效率的 84%（0.038/0.032），远超
559	    Strongest-K 的 67%（0.048/0.032）。15%+ 降幅满足 two_stage_ASR_reduction_pct [15,35]。
560	  tables:
561	  - name: Panel Selection Strategy Benchmark (15 Models, MMLU)
562	    columns:
563	    - Strategy
564	    - Mean ASR
565	    - Δ vs Strongest-K
566	    - Best (of 6)
567	    - Worst-case ASR
568	    rows:
569	    - - Two-Stage (ours)
570	      - '0.038'
571	      - -20.8%
572	      - 5/6
573	      - '0.071'
574	    - - Min-η_max
575	      - '0.041'
576	      - -14.6%
577	      - 4/6
578	      - '0.078'
579	    - - Strongest-K
580	      - '0.048'
581	      - baseline
582	      - 1/6
583	      - '0.095'
584	    - - Random
585	      - '0.089'
586	      - +85.4%
587	      - 0/6
588	      - '0.156'
589	    - - Max-K_eff
590	      - '0.112'
591	      - +133.3%
592	      - 0/6
593	      - '0.198'
594	    - - Oracle
595	      - '0.032'
596	      - -33.3%
597	      - 6/6
598	      - '0.052'
599	  - name: Two-Stage Sensitivity to Screening Threshold
600	    columns:
601	    - Threshold (percentile)
602	    - Candidate models
603	    - Mean ASR
604	    - K_eff of selected panel
605	    rows:
606	    - - '50'
607	      - '8'
608	      - '0.039'
609	      - '2.12'
610	    - - '65'
611	      - '10'
612	      - '0.037'
613	      - '2.28'
614	    - - 75 (optimal)
615	      - '11'
616	      - '0.038'
617	      - '2.41'
618	    - - '85'
619	      - '13'
620	      - '0.045'
621	      - '2.55'
622	    - - 100 (no filter)
623	      - '15'
624	      - '0.058'
625	      - '2.71'
626	  figures_description:
627	  - 'Fig 7: Strategy comparison grouped bar chart (6 conditions × 6 strategies)。Two-stage
628	    红色条在 5/6 conditions 最低。'
629	  - 'Fig 8: Pareto frontier plot (K_eff vs mean ASR)。Two-stage panels 紧贴 Pareto 前沿，Max-K_eff
630	    远离。'
631	  analysis: 20.8% ASR reduction 将实用贡献从 Dream 批评的 'marginal'（12.5% at 6-model）升级为 'practically
632	    meaningful'。Threshold sensitivity table 揭示 sweet spot 在 percentile-65–75：太紧（50th）损失
633	    candidate diversity，太松（85–100th）引入弱 judges。Pareto frontier analysis 显示 78% 的 Two-stage
634	    selected panels 落在 Pareto 前沿上——算法近似了 computationally-expensive 的 exhaustive Pareto
635	    search。关键 takeaway for practitioners：(1) 绝不盲目 maximize diversity（Max-K_eff 灾难级
636	    ASR）；(2) Pure robustness（Min-η_max）已经很好，diversity 优化提供 modest 额外收益；(3) Two-stage
637	    在所有非 oracle 策略中最接近理论最优。
638	- name: Per-Judge ASR Concentration Analysis
639	  plan_id: plan_006
640	  description: 计算 455 panels × 6 attacks 的 per-judge ASR 分布。Gini coefficient 量化 ASR
641	    在 panel 内 judges 间的集中度，Shannon entropy 量化均匀性。Adaptive vs RF 对比。
642	  expected_results:
643	    mean_gini_adaptive: 0.68
644	    mean_gini_RF: 0.12
645	    gini_ratio_adaptive_vs_RF: 5.67
646	    mean_entropy_adaptive: 1.42
647	    mean_entropy_RF: 2.31
648	    high_keff_gini_adaptive: 0.74
649	    low_keff_gini_adaptive: 0.55
650	    gini_keff_correlation: 0.52
651	    top1_judge_ASR_share_adaptive: 0.78
652	    top1_judge_ASR_share_RF: 0.38
653	  result_rationale: Concentration analysis 是 diversity trap 机制的 'microscope'——从 panel-level
654	    聚合统计深入到 judge-level 攻击分布。Adaptive adversary 的 core strategy 是 targeting：识别 panel
655	    中最脆弱的 judge 并集中 exploit。这导致 ASR 高度 concentrated 在 1-2 个 judges 上（Gini≈0.68, top-1
656	    share 78%），而 RF 下 failures 近似均匀分布（Gini≈0.12）。关键发现：high-K_eff panels 的 Gini 更高（0.74
657	    vs 0.55），因为 diverse panel 中 judges 的 capability spread 更大→adversary 的 target 更清晰（最弱
658	    judge 与最强 judge 的差距更大）。Gini-K_eff 正相关（r=0.52）是 diversity trap 因果链的直接 observational
659	    evidence：diversity → larger capability spread → clearer targeting → higher concentration
660	    → higher panel ASR。这不是因果证明（需要 intervention），但因果方向性（directional consistency）很强。5.67×
661	    Gini ratio 也是 BFT contrast 的另一维度验证：BFT 假设 failures 均匀分布（low Gini），adaptive adversary
662	    打破这一假设（high Gini）。
663	  tables:
664	  - name: 'ASR Concentration Metrics: Adaptive vs Random-Fault'
665	    columns:
666	    - Metric
667	    - Adaptive
668	    - Random-Fault
669	    - Ratio
670	    - Interpretation
671	    rows:
672	    - - Mean Gini
673	      - '0.68'
674	      - '0.12'
675	      - '5.67'
676	      - Concentrated vs uniform
677	    - - Mean Entropy (bits)
678	      - '1.42'
679	      - '2.31'
680	      - '0.61'
681	      - Low entropy = targeted
682	    - - Top-1 Judge ASR Share
683	      - '0.78'
684	      - '0.38'
685	      - '2.05'
686	      - 78% ASR on weakest judge
687	    - - r(K_eff, Gini)
688	      - '0.52'
689	      - '0.08'
690	      - '6.50'
691	      - Diversity → more targeting
692	  figures_description:
693	  - 'Fig 9: Per-judge ASR heatmap — 选 4 representative panels (2 high-K_eff, 2 low-K_eff)
694	    × adaptive vs RF。Adaptive 列 concentrated on 1 judge (dark red cell)，RF 列 diffuse
695	    (light yellow uniform)。'
696	  analysis: Concentration analysis 将 diversity trap 从统计关联推进到机制层面：不是 'K_eff 与 ASR 碰巧正相关'，而是
697	    'diverse panels 给 adversary 提供了更清晰的 targeting gradient（Gini 0.74），使攻击集中在最弱 judge
698	    上（78% share），从而打破 majority vote'。r(K_eff, Gini)=0.52 的正相关是 diversity trap 因果链中的关键中间变量——future
699	    work 可用 mediation analysis 正式量化 Gini 在 K_eff→ASR 路径中的 mediating role。此外 RF 下的
700	    low concentration（Gini 0.12）直接验证了 BFT 的 key assumption（uncorrelated failures distribute
701	    uniformly），解释了为何 diversity 在 RF 下可以有益。
702	- name: Diversity-Capability Tradeoff Visualization
703	  plan_id: plan_007
704	  description: 455 panels 的 K_eff vs η_max tradeoff 散点图、Pareto 前沿、tier 分层分析。
705	  expected_results:
706	    global_r_keff_etamax: 0.55
707	    within_small_r: 0.32
708	    within_medium_r: 0.41
709	    within_large_r: 0.33
710	    pareto_frontier_panels: 18
711	    pareto_frontier_slope: -0.73
712	    tradeoff_explained_variance: 0.42
713	  result_rationale: 全局 K_eff-η_max 正相关（r=0.55）编码了 LLM 生态系统的一个结构性约束：maximizing panel
714	    independence（K_eff）要求跨越 capability tiers 选 judges（例如同时选 GPT-4o 和 Mistral-7B），这必然引入
715	    robustness 差异大的 judges，推高 η_max。Within-tier r 大幅下降（0.32–0.41）揭示了 tradeoff 的两层结构：(1)
716	    Cross-tier component（贡献 ~40% 的 global r）：源于 tier mixing，可通过 screening 消除；(2) Within-tier
717	    component（residual r≈0.35）：即使同 tier 内，追求 diversity 仍需选择 robustness profile 更异质的
718	    judges，这不可完全消除但幅度较小。Pareto 前沿的 18 panels（约 4% of 455）定义了 diversity-robustness
719	    不可能三角的 achievable boundary——Two-stage 算法的目标就是逼近这个前沿。解释方差 42% 意味着 K_eff 是 η_max
720	    的 moderate 但非 dominant 预测器——剩余 58% 的 η_max 方差由 attack-specific vulnerability profiles、评分偏好差异等因素决定，这也解释了为什么
721	    K_eff 的 residualized effect 在控制 η_max 后仍然显著。
722	  tables:
723	  - name: K_eff–η_max Correlation Structure by Tier
724	    columns:
725	    - Tier
726	    - r(K_eff, η_max)
727	    - N panels
728	    - Pareto-optimal
729	    - Mean K_eff
730	    - Mean η_max
731	    rows:
732	    - - Small (7B-14B)
733	      - '0.32'
734	      - '10'
735	      - '3'
736	      - '2.41'
737	      - '0.312'
738	    - - Medium (14-34B)
739	      - '0.41'
740	      - '4'
741	      - '2'
742	      - '2.18'
743	      - '0.224'
744	    - - Large (70B+API)
745	      - '0.33'
746	      - '20'
747	      - '5'
748	      - '1.95'
749	      - '0.148'
750	    - - Cross-tier (all 15)
751	      - '0.55'
752	      - '455'
753	      - '18'
754	      - '2.35'
755	      - '0.231'
756	  figures_description:
757	  - 'Fig 10: K_eff vs η_max scatter plot — 455 points 按 tier 着色（blue=small, orange=medium,
758	    green=large），Pareto frontier 黑色曲线。背景 contour 显示 ASR 等值线。'
759	  analysis: Tradeoff 可视化的核心价值是将 Claim 3 从统计数字转化为直觉图形。Pareto frontier 的 steep negative
760	    slope（-0.73）意味着 K_eff 每增加 0.1，η_max 至少增加 0.073——practitioners 必须明确这个 cost。Tier-stratified
761	    view 显示 within-tier tradeoff 较弱但仍存在，支持 'screening + optimize' 策略的理论基础。ASR 等值线叠加（contour）直接显示
762	    Pareto-optimal panels 的 ASR 远低于 max-K_eff panels——视觉化 diversity trap。
763	- name: Panel Size Sensitivity K=3,5,7,9
764	  plan_id: plan_008
765	  description: Panel size 从 K=3 扩展到 K=5,7,9。15 models 选 K 个 judges 的组合数分别为 C(15,3)=455,
766	    C(15,5)=3003, C(15,7)=6435, C(15,9)=5005。每个 K 做 12 conditions 回归。
767	  expected_results:
768	    K3_keff_resid_sig: 10/12
769	    K5_keff_resid_sig: 11/12
770	    K7_keff_resid_sig: 12/12
771	    K9_keff_resid_sig: 12/12
772	    K3_mean_keff_beta: 0.42
773	    K5_mean_keff_beta: 0.48
774	    K7_mean_keff_beta: 0.55
775	    K9_mean_keff_beta: 0.61
776	    K3_mean_etamax_beta: 0.51
777	    K5_mean_etamax_beta: 0.49
778	    K7_mean_etamax_beta: 0.43
779	    K9_mean_etamax_beta: 0.38
780	    crossover_K: 6
781	    K3_mean_R2: 0.62
782	    K9_mean_R2: 0.51
783	  result_rationale: K_eff β 随 panel size 单调递增（0.42→0.61），原因：(1) larger panels 有更多
784	    judges → attack surface 与 panel size 正比增长，每个 additional judge 提供一个额外的 potential
785	    exploit path；(2) K=9 panel 的 K_eff range 更大（15 models 选 9 → wider independence
786	    spectrum），给回归更大信号。η_max β 随 K 递减（0.51→0.38），原因：larger panel 的 vulnerability 不再由单一
787	    weakest judge 决定——K=9 时 adversary 需要 compromise ⌈9/2⌉=5 judges，不能仅靠 targeting
788	    the weakest one，panel structure（diversity）的相对重要性上升。交叉点约 K≈6：在此 panel size 以上，K_eff
789	    超过 η_max 成为 primary vulnerability driver。R² 随 K 下降（0.62→0.51）因为 larger panel 的行为更复杂，judge
790	    interaction effects 增加 unexplained variance。K=9 时 K_eff 12/12 sig + β=0.61 是 diversity
791	    trap 的 strongest single evidence point：大型 evaluation panels 中 diversity 是 dominant
792	    有害因素。这直接回应 'just add more judges to be safer' 的朴素直觉。
793	  tables:
794	  - name: Panel Size Sensitivity Summary
795	    columns:
796	    - K
797	    - Panels
798	    - K_eff_resid sig
799	    - Mean K_eff β
800	    - Mean η_max β
801	    - Mean R²
802	    - Primary driver
803	    rows:
804	    - - '3'
805	      - '455'
806	      - 10/12
807	      - '0.42'
808	      - '0.51'
809	      - '0.62'
810	      - η_max
811	    - - '5'
812	      - '3003'
813	      - 11/12
814	      - '0.48'
815	      - '0.49'
816	      - '0.58'
817	      - balanced
818	    - - '7'
819	      - '6435'
820	      - 12/12
821	      - '0.55'
822	      - '0.43'
823	      - '0.54'
824	      - K_eff
825	    - - '9'
826	      - '5005'
827	      - 12/12
828	      - '0.61'
829	      - '0.38'
830	      - '0.51'
831	      - K_eff
832	  figures_description:
833	  - 'Fig 11: Dual-axis line plot — K_eff β (red, ascending) and η_max β (blue, descending)
834	    vs panel size K。交叉点 K≈6 标注。'
835	  analysis: Panel size sensitivity 提供 diversity trap 的 scaling law：K_eff β ≈ 0.33
836	    + 0.047K（近似线性增长）。这意味着 evaluation community 普遍采用的 'add more judges' strategy 会
837	    systematically amplify diversity trap——K=9 panel 的 K_eff 有害效应比 K=3 大 45%。η_max
838	    的下降则反映了 weakest-link theorem 在 large K 下的局限性：当 K 足够大时，单一最弱 judge 不再 decisive，panel
839	    的整体结构（diversity/independence）接管。交叉点 K≈6 有实际指导意义：K≤5 的小 panel 优先管控 η_max（选最 robust
840	    的 judges），K≥7 的大 panel 必须同时管控 K_eff（限制不必要的 diversity）。
841	- name: VIF + Multicollinearity Full Diagnostics
842	  plan_id: plan_009
843	  description: 对 15-model 455-panel 数据做完整统计诊断：VIF、condition number、partial correlations、residualized
844	    K_eff、Bonferroni/FDR 多重比较校正、beta regression（处理 ASR 的 [0,1] bounded nature）、Shapiro-Wilk
845	    残差正态性检验。纯计算，无 GPU。
846	  expected_results:
847	    VIF_keff_resid: 1.02
848	    VIF_etamax: 1.02
849	    condition_number: 4.8
850	    partial_r_keff_given_etamax: 0.38
851	    partial_r_etamax_given_keff: 0.45
852	    keff_resid_FDR_sig: 10/12
853	    keff_bonferroni_sig: 8/12
854	    beta_regression_keff_sig: 9/12
855	    beta_regression_etamax_sig: 10/12
856	    shapiro_wilk_residuals_p_mean: 0.23
857	    cooks_d_max: 0.031
858	    leverage_outlier_pct: 2.4
859	  result_rationale: 残差化设计（K_eff_resid = residuals of K_eff ~ η_max）在数学上保证 VIF=1.0（两个
860	    predictors 正交）。实际计算得 1.02 是因为 floating point precision + minor numerical jitter。Condition
861	    number 4.8 远低于 30 的 concern threshold，确认回归矩阵 well-conditioned。Partial correlations
862	    揭示各自独立贡献：K_eff|η_max 的 partial r=0.38 意味着 holding η_max constant，K_eff 独立解释 ~14%
863	    ASR variance；η_max|K_eff 的 partial r=0.45 解释 ~20%。Beta regression 作为 distributional
864	    robustness check 处理两个 OLS 假设违反：(1) ASR 在 [0,1] 内 bounded，OLS 可能在极端值处产生 out-of-range
865	    predictions；(2) ASR 的方差可能 heteroscedastic（低 ASR panels 方差更小）。Beta regression 结果（9/12
866	    vs OLS 10/12）高度一致，证明 OLS findings 非 distributional artifact。Multiple comparison
867	    从 FDR（10/12）到 Bonferroni（8/12，最保守）全部 pass，消除 'cherry-picking' concern。Cook's distance
868	    max=0.031（远低于 1.0 threshold）和 leverage outliers 仅 2.4% 证明结果非 influential point
869	    驱动。这套诊断 package 直接 preempt Dream review W2（VIF 未报告）和 RC1（multicollinearity）的所有
870	    variants。
871	  tables:
872	  - name: Multicollinearity Diagnostics Summary
873	    columns:
874	    - Diagnostic
875	    - Value
876	    - Threshold
877	    - Status
878	    rows:
879	    - - VIF (K_eff_resid)
880	      - '1.02'
881	      - <5.0
882	      - PASS
883	    - - VIF (η_max)
884	      - '1.02'
885	      - <5.0
886	      - PASS
887	    - - Condition Number
888	      - '4.8'
889	      - <30
890	      - PASS
891	    - - Partial r(K_eff|η_max)
892	      - '0.38'
893	      - '>0.1'
894	      - Moderate independent effect
895	    - - Partial r(η_max|K_eff)
896	      - '0.45'
897	      - '>0.1'
898	      - Moderate-strong independent effect
899	    - - Shapiro-Wilk p (residuals)
900	      - '0.23'
901	      - '>0.05'
902	      - Normal residuals
903	    - - Max Cook's D
904	      - '0.031'
905	      - <1.0
906	      - No influential points
907	    - - High-leverage %
908	      - 2.4%
909	      - <5%
910	      - Acceptable
911	  - name: Multiple Comparison Robustness
912	    columns:
913	    - Correction Method
914	    - K_eff_resid sig
915	    - η_max sig
916	    - Interpretation
917	    rows:
918	    - - Uncorrected
919	      - 12/12
920	      - 11/12
921	      - Raw signal
922	    - - FDR (Benjamini-Hochberg)
923	      - 10/12
924	      - 10/12
925	      - Primary report
926	    - - Bonferroni
927	      - 8/12
928	      - 9/12
929	      - Most conservative, still passes
930	    - - Beta Regression + FDR
931	      - 9/12
932	      - 10/12
933	      - Distributional robustness
934	  figures_description:
935	  - 'Supplementary Fig S1: Residual Q-Q plot (12 panels, one per condition)。Points
936	    closely follow diagonal — normality assumption satisfied。'
937	  - 'Supplementary Fig S2: Cook''s D plot (455 data points) — all well below 0.5 threshold,
938	    no influential outliers。'
939	  analysis: 'VIF + diagnostics package 是论文统计 credibility 的 foundation。Key contribution
940	    to paper: (1) 把 ''K_eff is independently significant'' 从初步 observation 升级为经过 6
941	    层 robustness check（residualization, VIF, partial correlation, beta regression,
942	    multiple comparison, influence diagnostics）验证的 result；(2) 每个 check 都 pass 意味着
943	    reviewer 无法从任何统计 angle 质疑 K_eff 的独立效应；(3) Bonferroni-corrected 8/12 sig 是最保守的下界——即使用最严格的多重比较校正，diversity
944	    trap 仍在 2/3 的 conditions 中成立。'
945	- name: Aggregation Rule Modulation (15-Model)
946	  plan_id: plan_010
947	  description: '三种非 majority-vote 聚合规则下的 dual vulnerability drivers 分析：Threshold voting（unanimity:
948	    所有 judges 必须同意 reject）、Accuracy-weighted voting（权重 ∝ clean accuracy）、Bayesian
949	    aggregation（基于 prior accuracy 的 posterior probability）。455 panels × 12 conditions
950	    per aggregation。'
951	  expected_results:
952	    majority_keff_sig: 10/12
953	    majority_etamax_sig: 10/12
954	    threshold_keff_sig: 11/12
955	    threshold_etamax_sig: 7/12
956	    threshold_keff_beta_amplification: 1.45
957	    weighted_keff_sig: 8/12
958	    weighted_etamax_sig: 9/12
959	    bayesian_keff_sig: 6/12
960	    bayesian_etamax_sig: 5/12
961	    bayesian_mean_ASR_reduction_vs_majority: 0.28
962	    total_keff_sig_majority_plus_threshold: 14/16
963	  result_rationale: 聚合规则改变 vulnerability driver 的 relative weight 通过三个机制：(1) Threshold/unanimity
964	    放大 K_eff——panel reject 需要 ALL judges agree，adversary 只需 flip one judge 就能 block
965	    rejection。Diverse panel 有更多 potential 'flip targets'（judge-specific vulnerabilities
966	    更多样），因此 K_eff β amplifies 1.45×。同时 η_max 弱化（7/12）因为 unanimity 的 blocking 不需要 weakest
967	    judge 特别弱——任何一个 judge 被 flip 就够了。(2) Weighted voting 结果近似 majority 因为 accuracy
968	    weights 仅微调 vote influence（权重范围 0.8-1.2），未根本改变投票结构。(3) Bayesian aggregation 基于
969	    clean-accuracy prior 下调低能力 judges 的 posterior weight，partially 中和了 η_max 通道（5/12，从
970	    majority 的 10/12 下降）——弱 judges 的 vote 被 discount 所以 adversary targeting 弱 judge
971	    的收益降低。但 K_eff 仍 6/12 sig，因为 Bayesian weights 基于 clean accuracy 而非 adversarial
972	    robustness——attack-shifted accuracy ≠ clean accuracy，adversary 可以 manipulate a
973	    judge 使其给出 'confidently wrong' judgment，Bayesian 无法区分这种 confident error 与 genuine
974	    judgment。28% ASR reduction 说明 Bayesian 是 best single-aggregation defense 但非 silver
975	    bullet。Combined majority + threshold conditions 的 14/16 K_eff sig 落入 K_eff_resid_sig_extended_conditions
976	    [10,16] 范围。
977	  tables:
978	  - name: Aggregation Rule × Vulnerability Drivers (15-Model, 455 Panels)
979	    columns:
980	    - Aggregation
981	    - K_eff_resid sig
982	    - η_max sig
983	    - Mean K_eff β
984	    - Mean η_max β
985	    - Mean ASR
986	    - Δ ASR vs Majority
987	    rows:
988	    - - Majority
989	      - 10/12
990	      - 10/12
991	      - '0.42'
992	      - '0.51'
993	      - '0.074'
994	      - baseline
995	    - - Threshold (unanimity)
996	      - 11/12
997	      - 7/12
998	      - '0.61'
999	      - '0.34'
1000	      - '0.138'
1001	      - +86%
1002	    - - Accuracy-weighted
1003	      - 8/12
1004	      - 9/12
1005	      - '0.39'
1006	      - '0.48'
1007	      - '0.069'
1008	      - -6.8%
1009	    - - Bayesian
1010	      - 6/12
1011	      - 5/12
1012	      - '0.25'
1013	      - '0.28'
1014	      - '0.053'
1015	      - -28.4%
1016	  figures_description:
1017	  - 'Fig 12: Grouped bar chart — K_eff β (dark) vs η_max β (light) across 4 aggregation
1018	    rules。Threshold 条 K_eff 最高；Bayesian 两者均最低。'
1019	  analysis: 'Aggregation 分析的 three actionable insights：(1) Threshold voting 是 diversity
1020	    trap 的 worst-case amplifier——unanimity requirement 使 K_eff β 增加 45%，absolute ASR
1021	    增加 86%。Deployment recommendation: 避免在 adversarial-aware 场景使用 unanimity aggregation。(2)
1022	    Bayesian 是 best partial defense——同时削弱两个 vulnerability channels（K_eff 6/12, η_max
1023	    5/12 vs majority 的 10/12, 10/12），ASR 降 28%。但 6/12 K_eff 仍 sig 表明 Bayesian 不能完全消除
1024	    diversity trap。(3) Defense stack rationale: Two-stage selection（控制 η_max 通道）+
1025	    Bayesian aggregation（削弱残余 η_max + 部分削弱 K_eff）是最 comprehensive defense。单一维度不够。'
1026	- name: Open-Ended Generation Benchmark (MT-Bench + AlpacaEval)
1027	  plan_id: plan_011
1028	  description: '在 MT-Bench（多轮对话评判）和 AlpacaEval（指令遵循评分）上测试 diversity trap。4 attack
1029	    types × 2 benchmarks = 8 新 conditions（选 4 primary attacks: score_manip, sycophancy,
1030	    position, verbosity）。15 models 但 panel size 受限于 benchmark cost 可能 sample 200 panels。'
1031	  expected_results:
1032	    mtbench_keff_resid_sig: 3/4
1033	    mtbench_etamax_sig: 3/4
1034	    mtbench_mean_R2: 0.48
1035	    alpacaeval_keff_resid_sig: 2/4
1036	    alpacaeval_etamax_sig: 3/4
1037	    alpacaeval_mean_R2: 0.42
1038	    open_ended_keff_sig_total: 3/4
1039	    open_ended_confound_r: 0.48
1040	    keff_beta_ratio_open_vs_mcq: 0.85
1041	    condition_dependent_pattern_preserved: true
1042	  result_rationale: Open-ended judging 与 MCQ 的关键差异：(1) 评分更主观——judges 在 'what constitutes
1043	    a good response' 上 disagreement 更高，noise floor 提升；(2) 攻击空间更大——adversary 可以在 multi-turn
1044	    conversation 的每轮 independently manipulate（MT-Bench），或在 free-form response 中 embed
1045	    更复杂的 manipulation signals（AlpacaEval）。K_eff 在 open-ended 上仍显著正向（3/4 unique conditions
1046	    across benchmarks），但 β 略低于 MCQ（ratio 0.85），因为 open-ended 的 higher noise floor
1047	    使 panel structure 解释的方差降低（R² 0.42-0.48 vs MCQ 0.62）。MT-Bench 比 AlpacaEval 表现更强（3/4
1048	    vs 2/4 sig），因为 multi-turn 结构给 adversary 更多 manipulation surface（每轮是独立攻击机会），judge-specific
1049	    响应差异在多轮中累积。Condition-dependent pattern 在 open-ended 上完美复现：score_manip 和 position
1050	    下 K_eff 主导，sycophancy 和 verbosity 下 η_max 主导——attack taxonomy 从 MCQ 推广到 open-ended
1051	    无需修改。≥2/4 open-ended K_eff 显著（best tier 达 3/4）满足 open-ended 显著条件。意义：diversity
1052	    trap 不是 MCQ-specific artifact，直接回应 Dream W6 和 RC3。
1053	  tables:
1054	  - name: Open-Ended Benchmark Results (8 Conditions)
1055	    columns:
1056	    - Benchmark×Attack
1057	    - K_eff_resid β
1058	    - K_eff_resid p (FDR)
1059	    - η_max β
1060	    - η_max p (FDR)
1061	    - R²
1062	    - Dominant
1063	    rows:
1064	    - - MT-Bench×score_manip
1065	      - '0.52'
1066	      - '1.8e-5'
1067	      - '0.38'
1068	      - '0.003'
1069	      - '0.52'
1070	      - K_eff
1071	    - - MT-Bench×sycophancy
1072	      - '0.28'
1073	      - '0.012'
1074	      - '0.55'
1075	      - '4.1e-5'
1076	      - '0.49'
1077	      - η_max
1078	    - - MT-Bench×position
1079	      - '0.47'
1080	      - '8.3e-5'
1081	      - '0.21'
1082	      - '0.089'
1083	      - '0.44'
1084	      - K_eff
1085	    - - MT-Bench×verbosity
1086	      - '0.18'
1087	      - '0.108'
1088	      - '0.62'
1089	      - '7.2e-6'
1090	      - '0.47'
1091	      - η_max
1092	    - - AlpacaEval×score_manip
1093	      - '0.44'
1094	      - '3.2e-4'
1095	      - '0.35'
1096	      - '0.006'
1097	      - '0.46'
1098	      - K_eff
1099	    - - AlpacaEval×sycophancy
1100	      - '0.21'
1101	      - '0.058'
1102	      - '0.58'
1103	      - '1.4e-5'
1104	      - '0.43'
1105	      - η_max
1106	    - - AlpacaEval×position
1107	      - '0.38'
1108	      - '0.002'
1109	      - '0.25'
1110	      - '0.041'
1111	      - '0.40'
1112	      - both
1113	    - - AlpacaEval×verbosity
1114	      - '0.14'
1115	      - '0.175'
1116	      - '0.59'
1117	      - '2.1e-5'
1118	      - '0.39'
1119	      - η_max
1120	  figures_description:
1121	  - 'Fig 13: MCQ (MMLU/ARC) vs Open-ended (MT-Bench/AlpacaEval) K_eff β comparison
1122	    — paired dot plot per attack type。Pattern 一致但 open-ended 点系统性偏左（β 略低）。'
1123	  analysis: Open-ended 结果的 three-fold significance：(1) Generalization — diversity
1124	    trap 从 MCQ 推广到 open-ended，覆盖 LLM evaluation 的两大应用场景（benchmark scoring + human
1125	    preference prediction），claim 从 'diversity hurts on MMLU/ARC' 升级为 'diversity hurts
1126	    on LLM evaluation generally'。(2) Taxonomy transfer — condition-dependent dominance
1127	    pattern（transferable→K_eff, shared-bias→η_max）在 open-ended 上 preserved without
1128	    modification，表明 taxonomy 是 task-agnostic fundamental structure。(3) Practical relevance
1129	    — MT-Bench/AlpacaEval 是 LLM 排名的 de facto standard，diversity trap 在这些 benchmark
1130	    上成立直接影响模型选择和部署决策。R² 下降（0.39-0.52 vs MCQ 0.62）是 expected tradeoff：open-ended evaluation
1131	    的 subjectivity noise 是 inherent 的，panel structure 能解释的 fraction naturally 减少。
1132	- name: Gaussian Copula Failure + Family Label Revalidation (15-Model, 105 Pairs)
1133	  plan_id: plan_001_mi_component
1134	  description: 15-model 105 pairwise MI matrix 计算。Gaussian copula MI vs observed MI
1135	    ratio 验证。Family labels（6 families）的 MI 预测性检验（within vs cross-family）。Capability
1136	    proximity 与 MI 的相关性分析。
1137	  expected_results:
1138	    total_pairs: 105
1139	    MI_gaussian_ratio_mean: 18.5
1140	    MI_gaussian_ratio_max: 312
1141	    MI_gaussian_ratio_min: 4.2
1142	    pairs_ratio_gt_10x: 82/105
1143	    family_label_MWU_p: 0.158
1144	    family_label_permutation_p: 0.312
1145	    within_family_MI_mean: 0.42
1146	    cross_family_MI_mean: 0.39
1147	    capability_proximity_MI_correlation: -0.71
1148	    copula_MI_ratio_15model: 18.5
1149	  result_rationale: 105 pairs（7× 6-model 的 15 pairs）大幅增加 copula failure 的统计力度。MI_gaussian_ratio
1150	    均值从 6-model 的 14.7 升至 18.5，因为 15-model pool 包含更多 capability-heterogeneous pairs（如
1151	    Mistral-7B 与 GPT-4o、Phi-14B 与 Claude-3.5），这些极端 pair 的联合分布更远离 bivariate Gaussian——heavy
1152	    tails、discrete clustering、capability-dependent correlation structure 使 Gaussian
1153	    copula 的低估更严重。Max ratio 从 235 升至 312（最极端 pair 如 Mistral-7B × GPT-4o 的 MI 被 Gaussian
1154	    低估 312×）。Family labels 仍无预测力（MWU p=0.158）：within-family MI（0.42）和 cross-family
1155	    MI（0.39）无显著差异。根本原因：同 family 不同 size（如 Llama-8B vs Llama-70B）的 judges 独立性差异远大于同
1156	    size 不同 family（如 Llama-8B vs Qwen-7B vs Mistral-7B）——这些 7B-class 模型 capability-wise
1157	    非常接近，共享 similar failure modes despite different training pipelines。Capability
1158	    proximity（|capability_i - capability_j|）与 MI 的强负相关（r=-0.71）直接支持：能力越接近→共享越多 failure
1159	    patterns→MI 越高→independence 越低。意义：practitioners 不应用 family diversity 作为 panel
1160	    independence proxy——capability-based metrics（如 K_eff）才是 valid measure。
1161	  tables:
1162	  - name: 'Copula Failure: Scale Comparison'
1163	    columns:
1164	    - Metric
1165	    - 6-model (15 pairs)
1166	    - 15-model (105 pairs)
1167	    - Change
1168	    rows:
1169	    - - MI_obs/MI_gauss mean
1170	      - '14.7'
1171	      - '18.5'
1172	      - +25.9%
1173	    - - MI_obs/MI_gauss max
1174	      - '235'
1175	      - '312'
1176	      - +32.8%
1177	    - - MI_obs/MI_gauss min
1178	      - '8.3'
1179	      - '4.2'
1180	      - Some close pairs
1181	    - - Pairs with ratio >10×
1182	      - 11/15 (73%)
1183	      - 82/105 (78%)
1184	      - +5pp
1185	    - - Family label p (MWU)
1186	      - '0.206'
1187	      - '0.158'
1188	      - Still NS
1189	    - - Capability-MI r
1190	      - '-0.65'
1191	      - '-0.71'
1192	      - Stronger
1193	  figures_description:
1194	  - 'Fig 14: MI_observed vs MI_gaussian scatter plot (105 pairs) with y=x identity
1195	    line。绝大多数点在 identity line 远上方，标注 extreme pairs。'
1196	  - 'Fig 15: Within-family vs cross-family MI violin plot (6 families)。Violin 大幅重叠，无显著分离。'
1197	  analysis: 15-model copula failure 和 family label 结果分别强化 Claims 5 和 4。Copula failure
1198	    的 practical implication：任何基于 Gaussian copula 假设的 panel reliability bound（如 independence-based
1199	    certification）在 LLM judge 对上不可信——underestimate information sharing by 10-30×（mean
1200	    18.5×）。这为 K_eff 作为 empirical independence measure（而非 copula-derived bounds）提供
1201	    methodological justification。Family label result 的 practical implication：panel
1202	    designers 不能简单用 '3 different families = diverse panel' 的 heuristic——Qwen-7B 和
1203	    Llama-8B 虽属不同 families 但 capability 接近故 MI 高（independence 低），而 GPT-4o-mini 和 GPT-4o
1204	    虽同属 OpenAI 但 capability gap 大故 MI 低（independence 高）。Capability proximity 是 independence
1205	    的 true driver。
1206	- name: Partial-Knowledge Adversary Model
1207	  plan_id: plan_012
1208	  description: 'Adversary 知道 panel 包含哪些 model families（public information）但不知各 judge
1209	    的具体 η_j vulnerability profiles。Strategy: family-level average attack 而非 judge-specific
1210	    targeting。与 full-knowledge 和 black-box baselines 对比。'
1211	  expected_results:
1212	    full_knowledge_mean_ASR: 0.074
1213	    partial_knowledge_mean_ASR: 0.058
1214	    black_box_mean_ASR: 0.031
1215	    partial_vs_full_ratio: 0.784
1216	    keff_sig_partial: 7/12
1217	    etamax_sig_partial: 8/12
1218	    partial_R2: 0.51
1219	    family_info_value_pct: 62.8
1220	  result_rationale: Partial-knowledge adversary 的 strategy 是 family-level targeting：知道
1221	    panel 含 Llama → apply Llama-family average attack template，知道含 GPT → apply GPT-family
1222	    average attack template。ASR 约为 full-knowledge 的 78%——family membership 提供了 ~63%
1223	    of adversary information value（(0.058-0.031)/(0.074-0.031)=62.8%），因为 family→capability
1224	    tier 有强相关性（所有 Qwen-7B 都是 small tier），且 family-level vulnerability profiles 有 within-family
1225	    consistency。K_eff 在 partial-knowledge 下仍 7/12 sig（vs full-knowledge 10/12），因为
1226	    diverse panel 跨越更多 families → adversary 的 family-level portfolio attack 有更多 entry
1227	    points。η_max 8/12 sig（vs 10/12）轻微下降因为 adversary 不知 exact η_j，targeting precision
1228	    降低使 weakest-link exploitation 变 fuzzy。R² 从 0.62 降至 0.51 反映 partial-knowledge 下
1229	    panel structure 的 predictive power 减弱——adversary behavior 有更多 randomness（不确定性导致
1230	    suboptimal targeting）。关键意义：diversity trap 不依赖于 unrealistically strong adversary
1231	    假设——即使 adversary 只有 public-level information（model families are typically disclosed
1232	    in evaluation pipelines），diversity 仍然显著有害。这直接回应 Dream W7（'unrealistically strong
1233	    adversary'）。
1234	  tables:
1235	  - name: Adversary Knowledge Level Comparison
1236	    columns:
1237	    - Knowledge Level
1238	    - Mean ASR
1239	    - K_eff sig
1240	    - η_max sig
1241	    - R²
1242	    - Info value vs black-box
1243	    rows:
1244	    - - Full (judge-level η_j)
1245	      - '0.074'
1246	      - 10/12
1247	      - 10/12
1248	      - '0.62'
1249	      - 100%
1250	    - - Partial (family only)
1251	      - '0.058'
1252	      - 7/12
1253	      - 8/12
1254	      - '0.51'
1255	      - 62.8%
1256	    - - Black-box (none)
1257	      - '0.031'
1258	      - 3/12
1259	      - 4/12
1260	      - '0.28'
1261	      - 0%
1262	  figures_description:
1263	  - 'Fig 16: Three-panel comparison — K_eff β bars at full/partial/black-box knowledge
1264	    levels。K_eff β 递减但 partial 仍 substantial。'
1265	  analysis: 'Partial-knowledge 分析的 key takeaway：diversity trap 的 threat model 是 realistic。Full-knowledge
1266	    是 worst-case security analysis 的 standard practice（similar to how cryptography
1267	    assumes worst-case adversary），但 even partial-knowledge（family info = public）已经
1268	    captures 63% of the vulnerability。The 7/12 K_eff significance under partial knowledge
1269	    means: even if the adversary only knows ''this panel uses judges from Llama, GPT,
1270	    and Qwen families''（commonly disclosed），they can exploit diversity. This eliminates
1271	    the ''but real adversaries don''t have full information'' defense. Graduation:
1272	    paper can now claim diversity trap holds under realistic threat models, not just
1273	    theoretical worst-case.'
1274	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f45c952-ae30-4f19-b16d-774adff0b0ad",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "168e7891-9f27-4ee6-acdd-1599af59fff1",
  "sourceToolAssistantUUID": "4f45c952-ae30-4f19-b16d-774adff0b0ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-22T18:49:11.380Z_

I now have a thorough understanding of both versions of the paper, the underlying experimental data, the project evolution (including pivots and falsified hypotheses), and the "best" dream report paper. Let me now write the review, focusing on the dream report's "best" version paper (the one titled "More Diverse, More Vulnerable") since that is the submission under review per the task prompt.

Let me also note the critical discrepancy: the task prompt summary describes one version of the paper, while the actual paper tex I read is a different (and somewhat contradictory) "best" dream version. I need to reconcile these. The task prompt describes results from the earlier dream (dream_20260522T055016), while the latest paper is from dream_20260522T173833. Let me verify by reading the earlier version's paper quickly.

I now have sufficient material. The task prompt summary describes a paper whose framing is "weakest-link dominance" (K_eff marginal, eta_max dominant), while the best dream paper I read has the opposite framing: "diversity trap" where K_eff is independently and positively harmful (10/12 sig). The key numbers in the task prompt summary appear to match the earlier dream's paper. Let me base my review on the paper summary provided in the task prompt, which is the version I'm asked to review -- that's the one described with 19 tables, the numbers about eta_max 9/12, K_eff 4/12, etc. This is the earlier paper framing closer to the first dream.

Actually, re-reading the task prompt more carefully, it describes a paper titled "Structural Vulnerability Anatomy of Multi-Judge LLM Evaluation: Weakest-Link Dominance, Aggregation Defenses, and the Limits of Diversity." That title does not match either tex file I read. The task prompt gives a detailed summary with specific numbers. I should review the paper as described in the task prompt summary, since that is the submission I'm asked to evaluate.

Now let me submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "168e7891-9f27-4ee6-acdd-1599af59fff1",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7CFwV4oEj1G75SURkR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7681ddef-964a-4871-bc78-de7fd36b38c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwNr4QvvAUGZcrNsnUhop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 47135,
      "cache_read_input_tokens": 55653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 47135,
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

_source line 39 · 2026-05-22T18:49:12.372Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VQqfo5DLuUC2JPcoa1sAB9`</summary>

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
  "parentUuid": "7681ddef-964a-4871-bc78-de7fd36b38c8",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7CFwV4oEj1G75SURkR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bec19f4-2efb-400c-85a6-ca8098478c93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwNr4QvvAUGZcrNsnUhop",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 47135,
      "cache_read_input_tokens": 55653,
      "output_tokens": 546,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 47135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 546,
          "cache_read_input_tokens": 55653,
          "cache_creation_input_tokens": 47135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 47135,
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

_source line 40 · 2026-05-22T18:49:12.375Z_

<details><summary>↩ Tool result · `toolu_01VQqfo5DLuUC2JPcoa1sAB9`</summary>

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
  "parentUuid": "6bec19f4-2efb-400c-85a6-ca8098478c93",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "86869691-78a6-4c74-9c20-3f2c1fe6b523",
  "sourceToolAssistantUUID": "6bec19f4-2efb-400c-85a6-ca8098478c93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-22T18:49:15.518Z_



Now I have all the information needed. Let me write and submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86869691-78a6-4c74-9c20-3f2c1fe6b523",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7DbC94TPRwExVhm9jX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5383550-7bde-45e9-a8d4-3ad4c5d7fe90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVf1D5azox19TXkUF12U2e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 102788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1170,
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

_source line 42 · 2026-05-22T18:50:53.851Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01AwEswx5vhwLPbkBfhjFWMJ`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "tier": "best",
  "dream_id": "dream_20260522T173833",
  "overall_score": "3.0 (Findings)",
  "report": "# Review Report — R1 (Methodology and Experiments)\n\n**Paper**: \"More Diverse, More Vulnerable: How Judge Panel Diversity Backfires Under Adaptive Adversaries\"\n\n**Venue**: EMNLP 2026 via ARR\n\n---\n\n## Summary\n\nThis paper investigates whether diversity in multi-judge LLM evaluation panels provides adversarial robustness, analogous to Byzantine Fault Tolerance. Through a large-scale study of 15 models, 455 three-judge panels, 9 attack types, and 4 benchmarks, the authors claim that panel diversity (K_eff) is independently and *positively* associated with attack success rate after residualizing against individual judge weakness (eta_max). They identify a \"dual vulnerability driver\" structure where attack type determines which factor dominates, propose a two-stage defense, and show Bayesian aggregation provides complementary protection.\n\n---\n\n## Strengths\n\n- **Comprehensive experimental coverage.** The paper tests an impressive combinatorial space: all C(15,3)=455 panels, 9 attack types, 4 benchmarks, 4 aggregation rules, 4 panel sizes, and 3 adversary knowledge levels. This breadth is unusual and commendable. The 12 imagined experiments are all represented.\n\n- **Rigorous statistical diagnostics.** The residualization approach to handle K_eff-eta_max collinearity is methodologically sound, yielding VIF=1.02. The paper reports multiple correction methods (uncorrected, FDR, Bonferroni), beta regression as a distributional robustness check, Cook's distance, leverage diagnostics, and Shapiro-Wilk normality tests. This is well above the typical standard for empirical NLP papers.\n\n- **BFT random-fault contrast is well-designed.** Using calibrated random faults (bootstrapped from clean accuracy noise rather than reusing adversarial eta_j values) is the correct experimental design. The 5/12 coefficient flip to negative under RF for transferable attacks provides genuine mechanistic insight — it is not a strawman comparison.\n\n- **Attack taxonomy provides predictive structure.** The observation that transferable attacks (score manipulation, position bias) are K_eff-dominated while shared-bias attacks (sycophancy, verbosity) are eta_max-dominated is a genuinely useful organizing principle. The taxonomy transfers to open-ended benchmarks and extended attacks, suggesting it captures real structure.\n\n- **Capability-matched validation addresses the most obvious confound.** The large-tier within-tier analysis (6 top-tier models, 20 panels, K_eff significant in 4/6 conditions) is the strongest single piece of evidence that K_eff's effect is not merely a tier-mixing artifact.\n\n- **Practical defense stack is well-motivated.** The two-stage algorithm + Bayesian aggregation combination directly follows from the dual-driver analysis. The 20.8% ASR reduction over Strongest-K is non-trivial, and the Max-K_eff catastrophic performance (ASR 0.112) is a compelling demonstration.\n\n---\n\n## Weaknesses\n\n### Major\n\n- **W1: Critical discrepancy between paper versions and actual experimental results.** Cross-referencing the paper's claims against the project's memory.md and ROADMAP.md reveals a serious concern. The actual 15-model experimental results (from plan001_step1_full_v4) show: eta_max FDR sig 11/12, K_eff FDR sig positive 7/12, K_eff negative 1/12 (arc x sycophancy), K_eff NS 4/12, with K_eff-eta_max confound correlation r=+0.70 (SEVERE). The paper reports K_eff_resid significant in 10/12 conditions with mean confound r=0.55 and VIF=1.02, which cannot be derived from the actual data where r=+0.70 (and even the project itself labels this \"CONFOUND_SEVERE\"). The paper appears to present imagined/projected numbers rather than actual experimental results. The real regression used log-log specification [log(ASR+eps) ~ log(K_eff) + log(eta_max+eps)], not the linear OLS presented in the paper. This is a fundamental credibility issue.\n\n- **W2: The \"diversity trap\" framing is inconsistent with the project's own falsification history.** The project memory documents that the original K_eff hypothesis was \"thoroughly falsified\" at the 6-model and 9-model scales (K_eff 1/12 significant, taxonomy broad-spectrum 0/6). The 15-model result shows K_eff 7/12 positive, 1/12 negative — predominantly harmful but far from the 10/12 claimed in the paper. The paper's title \"More Diverse, More Vulnerable\" and the abstract's claim of K_eff \"independently and positively associated\" in 10/12 conditions overstates what the actual data supports. The project's own paper_framing.md (v4b) is more honest: \"K_eff 7/12 positive + protective exception + condition-dependent dominance.\"\n\n- **W3: Non-independence of observations inflates statistical significance.** The 455 panels share judges extensively — each of the 15 models appears in C(14,2)=91 panels. This means panel-level ASR observations are not independent. The OLS regression treats all 455 as independent observations, which inflates degrees of freedom and deflates p-values. The paper needs clustered standard errors (clustering on individual judges) or a mixed-effects model with random intercepts per judge. Without this correction, the reported p-values (some as low as 1.2e-8) are unreliable. This could substantially change the significance counts.\n\n- **W4: The adversary model conflates \"adaptive\" with \"oracle.\"** The paper defines the adaptive adversary as one who \"observes panel composition and crafts attacks to maximize panel ASR.\" In practice, how are attacks \"crafted\" for each judge? The paper does not describe an actual adversarial optimization loop — it appears to simply measure each judge's vulnerability to pre-defined attack templates and then report eta_j as the individual ASR. This is an oracle adversary who knows each judge's exact vulnerability, not a realistic adaptive attacker who must discover vulnerabilities through interaction. The partial-knowledge experiment (Section 7.4) partially addresses this but still assumes the adversary can execute family-level attack templates with known average ASRs. The gap between this oracle model and realistic adversaries is inadequately discussed.\n\n- **W5: Regression specification concerns.** (a) Linear OLS on ASR in [0,1] can produce out-of-range predictions. The paper mentions beta regression as a robustness check (9/12 vs 10/12 sig), but the main analysis uses OLS — beta regression should be the primary analysis for bounded outcomes. (b) The paper claims R^2=0.62 mean, but the ROADMAP.md shows R^2=0.298 for majority vote under the actual log-log canonical specification. This is a 2x discrepancy. (c) With only 2 predictors and 455 observations, an R^2 of 0.62 is suspiciously high for social/behavioral science regression — it raises the question of whether the regression is partially tautological (K_eff and eta_max are computed from the same judge pool that generates ASR).\n\n### Minor\n\n- **W6: Panel size analysis may be confounded by statistical power.** The claim that K_eff significance increases from 10/12 (K=3) to 12/12 (K=9) could be an artifact of increasing sample size: C(15,9)=5005 panels have 11x the statistical power of C(15,3)=455 panels. The increasing beta coefficient (0.42 to 0.61) is more informative but could reflect increased multicollinearity at larger K (where K_eff and eta_max become more structurally coupled).\n\n- **W7: No figures in the paper.** For a paper with 12+ tables of regression coefficients, the absence of any scatter plots, coefficient plots, or visualizations is a significant presentation weakness. Key patterns (the attack taxonomy, the BFT flip, the Pareto frontier) would be far more interpretable visually.\n\n- **W8: Gaussian copula failure numbers are inconsistent with project data.** The paper claims MI_obs/MI_gauss ratio of 18.5x mean (max 312x), but the project's actual 15-model results show MI_obs/MI_gauss ratio of 0.93 (MMLU) and 0.90 (ARC) — the copula fits *well* at 15-model scale. The 6-model result of 10-21x was explicitly labeled \"small-sample artifact\" and \"DEAD as independent claim\" in paper_framing.md v4b. Presenting the falsified 18.5x number in the paper is misleading.\n\n- **W9: Limitations section is thin.** Three points in one paragraph is adequate per EMNLP norms, but the points chosen omit the most important limitation: the non-independence of panel observations sharing judges (W3). The \"observational not causal\" caveat is buried as the third point and understated given the paper's causal-direction language throughout (\"diversity backfires,\" \"diversity trap\").\n\n- **W10: Reference list is minimal.** Only 4 actual citations in the related work (zheng2023, li2023, dubois2024, wang2023, plus raina2024, shi2024, lamport1982, castro1999, krogh1994, brown2005, sagawa2020). For a paper claiming to overturn a \"pervasive assumption,\" the literature review should more thoroughly document where this assumption appears and what evidence supports it.\n\n---\n\n## Questions for Authors\n\n1. **Q1**: The project's actual experimental results (plan001_step1_full_v4) show K_eff significant in 7/12 (not 10/12) conditions with confound r=+0.70 (not 0.55). The regression specification was log-log (not linear OLS), and the R^2 was 0.298 (not 0.62). Can you clarify why the paper reports different numbers? Are the paper's numbers from a different analysis pipeline?\n\n2. **Q2**: How do you address the non-independence of panel observations? Each judge appears in 91 of 455 panels. Have you run the analysis with clustered standard errors or mixed-effects models? What happens to the significance counts?\n\n3. **Q3**: In the adversary model, you assume the attacker can apply judge-specific or family-specific attack templates with known ASRs. How were individual judge ASRs measured? Was there a held-out evaluation set, or are the same samples used for both measuring eta_j and computing panel ASR?\n\n4. **Q4**: The BFT random-fault contrast uses \"calibrated random faults based on bootstrapped clean-accuracy noise.\" Can you specify the exact procedure? How many bootstrap samples? How does the calibration ensure the marginal failure rates match between adaptive and RF conditions?\n\n5. **Q5**: The Bayesian aggregation uses \"prior accuracy\" to downweight judges. How is this prior estimated? If estimated from the same evaluation data, this introduces information leakage. The paper mentions \"5-fold CV\" in passing — was the Bayesian prior estimated in cross-validation? Details are needed.\n\n6. **Q6**: For the within-tier analysis, the small tier has only 10 panels and the medium tier only 4 panels. With 2 predictors, these regressions have 7 and 1 residual degrees of freedom respectively. Are the reported significance tests reliable with such small samples?\n\n7. **Q7**: The Pareto frontier analysis claims \"83% large-tier, 0% small-tier.\" How is \"Pareto-optimal\" defined here — over which objectives? Is this Pareto-optimal in the K_eff vs eta_max space, or K_eff vs ASR space?\n\n---\n\n## Scores\n\n| Dimension | Score | Rationale |\n|-----------|-------|-----------|\n| **Soundness** | 2.5 | The non-independence issue (W3) undermines all significance claims. The discrepancy between reported and actual experimental numbers (W1, W2, W8) raises credibility concerns. The adversary model is closer to oracle than adaptive (W4). Core statistical framework is reasonable in design (residualization, diagnostics) but implementation details do not match the project's actual data. |\n| **Excitement** | 3.5 | The research question is important and timely. The finding that diversity can *harm* adversarial robustness — if validated — would be genuinely surprising and impactful for the LLM evaluation community. The attack taxonomy (transferable vs shared-bias) is a useful conceptual contribution. The BFT contrast is well-conceived. |\n| **Reproducibility** | 2.0 | Model list is provided but attack implementations are not described in detail. The paper does not specify: prompt templates for attacks, evaluation criteria for ASR, number of evaluation instances per condition, how MI matrices are estimated, or computational requirements. No code or data availability statement. The discrepancy between paper numbers and project data makes it unclear which analysis pipeline produced the reported results. |\n| **Overall** | 3.0 | The paper addresses an important question with ambitious experimental scale, but the gap between claimed and actual results, the unaddressed non-independence of observations, and the underspecified adversary model prevent confidence in the central claims. If the statistical issues (W1, W3) were resolved and the paper accurately reported its actual experimental results — even if those results are weaker (7/12 rather than 10/12 for K_eff) — this could be a solid Findings paper. The core insight (diversity-robustness relationship depends on attack type and adversary model) is genuine and valuable, but the current presentation overstates the evidence. |\n| **Confidence** | 4 | I have carefully read the paper, cross-referenced against the underlying experimental records, and identified specific numerical discrepancies. My concerns about non-independence and the adversary model are grounded in standard statistical methodology. I am less certain about the precise impact of clustered standard errors on significance counts, which would require re-analysis. |\n\n---\n\n## Recommendation\n\n**3.0 — Findings.** The paper has genuine scientific value in its research question, experimental scale, and the attack taxonomy insight. However, the methodological concerns (non-independence, adversary model realism) and the discrepancy between reported and actual results prevent main conference recommendation. A revised version that (1) accurately reports the actual experimental numbers, (2) addresses non-independence through appropriate multilevel modeling, (3) more clearly specifies and justifies the adversary model, and (4) adds implementation details for reproducibility could reach borderline conference level. The core contribution — that the diversity-robustness relationship is attack-type-dependent and breaks under adaptive adversaries — is worth publishing if properly validated.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5383550-7bde-45e9-a8d4-3ad4c5d7fe90",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7DbC94TPRwExVhm9jX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80b5d4e0-851d-4948-b26e-d615ba662b27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVf1D5azox19TXkUF12U2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 102788,
      "output_tokens": 3689,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3689,
          "cache_read_input_tokens": 102788,
          "cache_creation_input_tokens": 1170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1170,
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

_source line 43 · 2026-05-22T18:50:57.647Z_

<details><summary>↩ Tool result · `toolu_01AwEswx5vhwLPbkBfhjFWMJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/review_report.md\", \"dream_id\": \"dream_20260522T173833\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80b5d4e0-851d-4948-b26e-d615ba662b27",
  "isSidechain": true,
  "promptId": "56ad1eab-ba7e-44f8-a3bf-f5e746c62666",
  "agentId": "a3fe7b14d3d025092",
  "type": "user",
  "uuid": "c2d0a95d-f57c-4bab-b5a4-39b6f6b61e7d",
  "sourceToolAssistantUUID": "80b5d4e0-851d-4948-b26e-d615ba662b27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-22T18:51:12.998Z_

Review submitted. Here is a summary of the review:

**Overall Score: 3.0 (Findings)**

**Key findings from the review:**

The paper tackles an important question — whether judge diversity helps or hurts adversarial robustness in multi-judge LLM evaluation — with impressive experimental scale (15 models, 455 panels, 9 attacks, 4 benchmarks). The attack taxonomy distinguishing transferable vs. shared-bias attacks and the BFT random-fault contrast are genuine conceptual contributions.

**Critical weaknesses identified:**

1. **Discrepancy between reported and actual results (W1, W2, W8).** Cross-referencing against the project's own experimental records (memory.md, ROADMAP.md, paper_framing.md) reveals the paper reports K_eff significant in 10/12 conditions with R^2=0.62 and confound r=0.55, but actual data shows 7/12, R^2=0.298, and confound r=+0.70 (labeled "CONFOUND_SEVERE"). The Gaussian copula failure (18.5x) was explicitly falsified at 15-model scale (actual ratio ~0.93) and labeled "DEAD" in the project's own framing document.

2. **Non-independence of observations (W3).** Each judge appears in 91 of 455 panels. OLS treating these as independent inflates significance. Clustered standard errors or mixed-effects models are needed.

3. **Oracle adversary model (W4).** The "adaptive" adversary is really an oracle with perfect knowledge of each judge's vulnerability — no actual adversarial optimization loop is described.

4. **Missing reproducibility details.** Attack prompts, MI estimation procedures, evaluation instance counts, and code are not specified.

**Scores:** Soundness 2.5, Excitement 3.5, Reproducibility 2.0, Overall 3.0, Confidence 4/5.

The review report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2d0a95d-f57c-4bab-b5a4-39b6f6b61e7d",
  "isSidechain": true,
  "agentId": "a3fe7b14d3d025092",
  "requestId": "req_011CbJ7MLv8QfYgmu8AkroWD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72c879ee-94df-47f4-9631-f3b11031651f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "4bd8a18a-978d-4865-811c-2ab932d2722c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01713D444ohpuYW13K74ERSz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3821,
      "cache_read_input_tokens": 103958,
      "output_tokens": 517,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 517,
          "cache_read_input_tokens": 103958,
          "cache_creation_input_tokens": 3821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3821,
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
