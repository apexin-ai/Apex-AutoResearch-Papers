# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **methods and experiments**. ## Venue calibratio

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-abcc09248c70fce74.jsonl`
- **Structured JSON:** [`47d19555300cffb51f12.json`](../../sessions/47/47d19555300cffb51f12.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-22T23:03:39.403Z_

You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **methods and experiments**. 

## Venue calibration
- EMNLP 2026, ARR unified review. Overall Assessment scale: 5=Award (top 2.5%), 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit. Half-point increments allowed.
- Accept rate ~21% for Main. Evaluate Soundness (1-5), Excitement (1-5), Reproducibility (1-5).
- Auto-reject signals: anonymity violation, over page limit, missing Limitations, hallucinated citations.

## Paper summary
**Title**: "The Mirage of Significance: How Non-Independence Inflates Predictor Effects in Combinatorial LLM Evaluation Panels"

The paper studies vulnerability of multi-judge LLM evaluation panels to adversarial attacks. It decomposes panel vulnerability into individual judge weakness (η_max) and structural diversity (K_eff) across 15 models, 455 panels (C(15,3)), 9 attack types, and 3 benchmarks (MMLU, ARC, MT-Bench).

**Central finding**: Standard OLS regression dramatically overstates predictor significance due to structural non-independence among combinatorial panels. Each of 15 models appears in 91 of 455 panels. Under wild cluster bootstrap correction:
- η_max significance drops from 11/12 to 3/12 conditions
- K_eff drops from 8/12 to 1/12
- SE inflation of 3.2×
- At K=9, SE inflation reaches 7.2× and η_max drops to 1/12

**Key results**:
1. OLS→bootstrap significance collapse (methodological contribution)
2. VIF > 7 for both predictors, 67% shared variance, K_eff unique variance only 3%
3. BFT random-fault contrast fails GO/NO-GO gate (Cohen's d=0.12, contrast p=0.31)
4. Capability-matched analysis: within-tier η_max sig drops to 0-3/12, cross-tier is 11/12
5. Panel size sensitivity: SE inflation scales from 3.2× (K=3) to 7.2× (K=9)
6. Aggregation gradient: threshold R²=0.89 vs Bayesian R²=0.10 (survives correction as descriptive stat)
7. Min-η_max panel selection wins 9/12 conditions; two-stage algorithm adds only 0.003pp improvement
8. GAM taxonomy develops 3 reversals at 9 attacks (was clean 6:6 at 6 attacks)
9. MT-Bench: bootstrap η_max 1/12, K_eff 0/12, R² lower (0.15 vs 0.25)
10. Partial-knowledge adversary: ASR gradient exists but adds little new insight
11. ASR concentration: adaptive vs RF Gini 0.28 vs 0.19 (d=0.22, small effect)

**Tables in paper**: 13 tables across 9 pages. No references section included.

**Limitations section**: Present (page 9), covers 3 points: small cluster count (15), MCQ-centric findings, diversity-capability confound.

## Your task
Produce a detailed R1 review focusing on:
1. **Soundness of methodology**: Is the non-independence correction framework appropriate? Is wild cluster bootstrap with 15 clusters reliable? Is the max-p across 3 positions justified? Are the VIF thresholds appropriate?
2. **Experimental design**: Is the combinatorial design (C(15,3)=455) the right approach? Could alternative designs (e.g., stratified sampling) avoid the non-independence issue entirely? Is this a design problem masquerading as a finding?
3. **Statistical rigor**: Are the correction methods properly implemented? Is the bootstrap conservative or appropriate? What about the 15-cluster limitation?
4. **Result interpretation**: Are the authors over-claiming or under-claiming? Is "neither predictor is reliable" a contribution or an admission of design failure?
5. **Missing analyses**: What's missing that would strengthen or weaken the paper?
6. **Practical value**: Is "use the strongest models" a trivial recommendation? Does the aggregation gradient provide actionable insight?
7. **Reproducibility**: Can this be reproduced? What's missing?

## Output format
```
## R1 Review: Methods and Experiments

### Summary
[2-3 sentences]

### Strengths
[Numbered list, 4-6 items]

### Weaknesses
[Numbered list, 4-8 items, with specific references to tables/sections]

### Questions for Authors
[3-5 specific questions]

### Missing References / Analyses
[If any]

### Soundness: X/5
### Excitement: X/5
### Reproducibility: X/5
### Overall Assessment: X.X (with justification referencing the ARR scale)
### Confidence: X/5
```

Be rigorous but fair. Ground every criticism in specific paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "ed99b08e-e376-48f0-92aa-57388a25a5ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T23:03:39.408Z_

```json
{
  "parentUuid": "ed99b08e-e376-48f0-92aa-57388a25a5ca",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
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
  "uuid": "d55140e2-e2e6-4a9c-ae89-cfffcdfd4578",
  "timestamp": "2026-05-22T23:03:39.408Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-22T23:03:42.345Z_



I'll start by reading the paper and project files to ground my review in specific content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d55140e2-e2e6-4a9c-ae89-cfffcdfd4578",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJScytkKwWaGot6t7CRp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08feb32f-aa3f-47d0-9e37-0cc618dbf969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWQjKGaNEuX6ghkbuH3phF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7642,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7642,
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

_source line 4 · 2026-05-22T23:03:43.416Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MkfJM1HPcpWnuKAC1o19u9`</summary>

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
  "parentUuid": "08feb32f-aa3f-47d0-9e37-0cc618dbf969",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJScytkKwWaGot6t7CRp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbeab964-e3a3-4d23-a943-ae1eb3e1f155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWQjKGaNEuX6ghkbuH3phF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7642,
      "cache_read_input_tokens": 8252,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7642
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7642,
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

_source line 5 · 2026-05-22T23:03:43.421Z_

<details><summary>↩ Tool result · `toolu_01MkfJM1HPcpWnuKAC1o19u9`</summary>

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
  "parentUuid": "fbeab964-e3a3-4d23-a943-ae1eb3e1f155",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "4dbe3b20-a379-49c6-a5a3-591677f7ace8",
  "sourceToolAssistantUUID": "fbeab964-e3a3-4d23-a943-ae1eb3e1f155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T23:03:46.363Z_



Let me read the paper and project files to ground my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dbe3b20-a379-49c6-a5a3-591677f7ace8",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSdHJ148BafMxySsQut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f4aa28f-246e-4aa4-8b0b-4bfc28f9b73c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK8px6ToEHMnLpdn9TRDcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 15894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 7 · 2026-05-22T23:03:47.377Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XmhZvVF1bk2ZUrRnGskLqg`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f4aa28f-246e-4aa4-8b0b-4bfc28f9b73c",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSdHJ148BafMxySsQut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa226226-26f7-460d-92cc-ce80d4a7077f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK8px6ToEHMnLpdn9TRDcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 15894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 8 · 2026-05-22T23:03:47.393Z_

<details><summary>↩ Tool result · `toolu_01XmhZvVF1bk2ZUrRnGskLqg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan001_step1_batched_v2（准备中）\\n- plan001_step1_batched（准备中）\\n- plan001_step1_v3（准备中）\\n- plan001_step1_throttled_v5（准备中）\\n- plan001_step1_throttled_v4（准备中）\\n- plan001_step1_throttled_v3（准备中）\\n- plan001_step1_throttled_v2（准备中）\\n- plan001_step1_throttled（准备中）\\n- plan001_step1_v2（准备中）\\n- plan001_step1_parallel_final（准备中）\\n- …另有 13 项\\n\\n## 近期结论\\n- **plan001_step1_full_v4** (success): Expanding from 6 to 15 models (9 API + 6 local) across 6 families and 3 capability tiers breaks the structural K_eff-η_max collinearity (r=-0.8 with 6 models). With 15 models, panels can have high K_eff (cross-family diversity) without necessarily including weak judges, enabling clean separation of diversity vs robustness effects.\\n- **taxonomy-broad-spectrum** (negative): K_eff is a significant negative predictor of panel ASR specifically for broad-spectrum attacks (verbosity bias, position bias, authority bias) that exploit shared judge biases, consistent across both MMLU and ARC datasets. This validates the attack taxonomy: targeted attacks → η_max dominates; broad-spectrum attacks → K_eff provides additional protection. ← 基于 mvp-step2v3-retry3\\n- **mvp-step2v3-retry3** (negative): Controlling for individual model robustness (η_max), higher K_eff panels have significantly lower ASR. Multi-factor regression log(ASR) ~ log(K_eff) + log(η_max) should show K_eff coefficient significantly negative. ← 基于 mvp-step2v3-retry2\\n\\n## 趋势\\n成功 1 / 负向 3 / 失败 3 / 共 7\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nseetacloud-rtx6000: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp-step2v3-regression: 训练失败 — unknown\\n- mvp-step2v3-retry: 训练失败 — unknown\\n- mvp-step2v3-retry2: 训练失败 — unknown\\n\", \"total_chars\": 1736, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa226226-26f7-460d-92cc-ce80d4a7077f",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "8280ba18-5043-462b-bea0-7d4e5857bf5a",
  "sourceToolAssistantUUID": "aa226226-26f7-460d-92cc-ce80d4a7077f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T23:03:49.320Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AEiEfww4kdruzGx8fikkAi`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/**/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8280ba18-5043-462b-bea0-7d4e5857bf5a",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSdHJ148BafMxySsQut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11552149-a086-44d1-a2b7-af59b1940525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK8px6ToEHMnLpdn9TRDcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 15894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 10 · 2026-05-22T23:03:49.343Z_

<details><summary>↩ Tool result · `toolu_01AEiEfww4kdruzGx8fikkAi`</summary>

```text
artifacts/_project/report/t1_sdpi_parallel.md
artifacts/theory/t1_sdpi_parallel.md
artifacts/_project/report/t3_peg_degradation.md
artifacts/theory/t3_peg_degradation.md
artifacts/report_step2v3_retry.md
artifacts/worker_output_step2v3_retry2_analysis.md
artifacts/dream_reports/dream_20260522T055016/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260522T055016/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260522T055016/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260522T055016/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260522T055016/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T055016/best/experiment_data.json
artifacts/dream_reports/dream_20260522T055016/best/paper_framing.md
artifacts/dream_reports/dream_20260522T055016/best/paper.tex
artifacts/dream_reports/dream_20260522T055016/best/paper.aux
artifacts/dream_reports/dream_20260522T055016/best/paper.out
artifacts/dream_reports/dream_20260522T055016/best/paper.pdf
artifacts/dream_reports/dream_20260522T055016/best/paper.log
artifacts/dream_reports/dream_20260522T055016/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260522T055016/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T055016/median/experiment_data.json
artifacts/dream_reports/dream_20260522T055016/median/paper_framing.md
artifacts/dream_reports/dream_20260522T055016/median/paper.tex
artifacts/dream_reports/dream_20260522T055016/median/paper.aux
artifacts/dream_reports/dream_20260522T055016/median/paper.out
artifacts/dream_reports/dream_20260522T055016/median/paper.pdf
artifacts/dream_reports/dream_20260522T055016/median/paper.log
artifacts/dream_reports/dream_20260522T055016/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260522T055016/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T055016/worst/experiment_data.json
artifacts/dream_reports/dream_20260522T055016/worst/paper_framing.md
artifacts/dream_reports/dream_20260522T055016/worst/acl.sty
artifacts/dream_reports/dream_20260522T055016/worst/acl_natbib.bst
artifacts/dream_reports/dream_20260522T055016/worst/references.bib
artifacts/dream_reports/dream_20260522T055016/worst/paper.tex
artifacts/dream_reports/dream_20260522T055016/worst/paper.aux
artifacts/dream_reports/dream_20260522T055016/worst/paper.out
artifacts/dream_reports/dream_20260522T055016/worst/paper.pdf
artifacts/dream_reports/dream_20260522T055016/worst/paper.log
artifacts/dream_reports/dream_20260522T055016/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260522T055016/best/review_context.yaml
artifacts/dream_reports/dream_20260522T055016/logs/review_best.log
artifacts/dream_reports/dream_20260522T055016/best/review_report.md
artifacts/dream_reports/dream_20260522T055016/median/review_context.yaml
artifacts/dream_reports/dream_20260522T055016/logs/review_median.log
artifacts/dream_reports/dream_20260522T055016/median/review_report.md
artifacts/dream_reports/dream_20260522T055016/worst/review_context.yaml
artifacts/dream_reports/dream_20260522T055016/logs/review_worst.log
artifacts/dream_reports/dream_20260522T055016/logs/orchestrator.log
artifacts/dream_reports/dream_20260522T055016/worst/review_report.md
artifacts/dream_reports/dream_20260522T055016/meta.yaml
artifacts/scripts/run_plan009_vif_analysis.py
artifacts/scripts/run_plan003_random_fault.py
artifacts/_project/report/plan009_vif_analysis_summary.txt
artifacts/_project/report/plan003_random_fault_summary.txt
artifacts/results/api_model_availability.json
artifacts/_project/data/plan001_api_model_availability.txt
artifacts/_project/report/plan001_step0_adapter_validation.txt
artifacts/_project/paper/theorem1_proof.tex
artifacts/theorem1_proof.aux
artifacts/theorem1_proof.pdf
artifacts/theorem1_proof.log
artifacts/_project/paper/theorem1_proof_summary.txt
artifacts/theorem1_proof.tex
artifacts/_project/report/plan010_aggregation_summary.txt
artifacts/_project/report/plan010_fdr_cv_summary.txt
artifacts/_project/data/results_plan010_threshold_keff_positive_fdr.json
artifacts/_project/paper/references.bib
artifacts/_project/data/7model_preview_results.txt
artifacts/_project/chart/7model_confound_scatter_location.txt
artifacts/dream_reports/dream_20260522T173833/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260522T173833/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260522T173833/logs/phase2_median_attempt0.log
artifacts/run_aggregation_regression_15model.py
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
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11552149-a086-44d1-a2b7-af59b1940525",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "142b5165-5f48-4739-b673-18ffde9e3b77",
  "sourceToolAssistantUUID": "11552149-a086-44d1-a2b7-af59b1940525",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T23:03:49.679Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MdND14Xz1agMe5RAf1P3wu`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "142b5165-5f48-4739-b673-18ffde9e3b77",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSdHJ148BafMxySsQut",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1512f41-32a2-45cb-b88c-83973566d590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK8px6ToEHMnLpdn9TRDcW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 15894,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1290
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 286,
          "cache_read_input_tokens": 15894,
          "cache_creation_input_tokens": 1290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1290,
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

_source line 12 · 2026-05-22T23:03:49.716Z_

<details><summary>↩ Tool result · `toolu_01MdND14Xz1agMe5RAf1P3wu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/ROADMAP.md\", \"content\": \"# cert_manip_resist_eval — Research Dashboard\\n\\n> 最后更新: 2026-05-22 21:39 UTC | 更新原因: Paper Step 5 converged (5 rounds, Overall 7/10, 0 CRITICAL). PDF visually confirmed 8 pages. Submission-ready.\\n\\n## 核心方向\\n**v5+ (D019+D021)**: η_max dominates panel vulnerability. Bootstrap (recommended for small clusters) gives 5/12 η_max, 1/12 K_eff — 5:1 ratio. K_eff fragile (0-1/12 under all corrections). GAM 6:6 split confirmed. Aggregation gradient independent.\\n\\n## 当前阶段\\n**论文投稿就绪** — Step 5 写作迭代完成 (5 轮, Overall 7/10, 0 CRITICAL, 0 WARNING)\\n\\n## 校正方法对比（D021, Reviewer-verified）\\n| Method | η_max | K_eff | Reliability |\\n|--------|-------|-------|-------------|\\n| OLS | 11/12 | 8/12 (7+/1−) | low (inflated) |\\n| **Wild Bootstrap v2** | **5/12** | **1/12** | **high (recommended)** |\\n| Clustered SE | 8/12 | 0/12 | medium |\\n| Mixed Effects | 7/12 | 3/12 | medium |\\n| + Tier indicators | 11/12 | 5/12 | controls confound |\\n| GAM | 12/12 | 12/12 (6+/6−) | nonlinear |\\n\\n## 论文状态\\n- ✅ 主文本 8 页（PDF 视觉确认，Conclusion 在 p8 结束）\\n- ✅ 4 张 Figure 集成（Fig 1-3 主文本, Fig 4 Appendix）\\n- ✅ β 下标全文一致（β₁=K_eff, β₂=η_max）\\n- ✅ 方法描述与代码实现一致（3-position max-SE/max-p, 13 clusters）\\n- ✅ Em-dash 零残留，TODO 零残留，R² 统一 0.89\\n- ✅ 7 个 Appendix cross-reference 全部正确\\n- ✅ Appendix: A(Proof) → B(Robustness Methods) → C(Extended Analysis) → D(Panel Selection)\\n- ✅ 编译通过，0 undefined references, 0 critical warnings\\n\\n## 写作迭代记录\\n| 轮次 | Overall | CRITICAL | WARNING | 主要修复 |\\n|------|---------|----------|---------|---------|\\n| R1 | 4 | 1 (β swap) | 3 | β 下标统一 |\\n| R2 | 6 | 1 (clustered SE) | 2 | 方法描述修正 |\\n| R3 | 4* | 1 (page limit) | 3 | 8 页裁剪 |\\n| R4 | 7 | 0 | 2 | em-dash + 重复表格 |\\n| R5 | 7 | 0 | 0 | 收敛 |\\n\\n## 近期任务\\n- [x] Paper Agent v5 全文 reframe\\n- [x] Figures 制作 + 集成 (4 张)\\n- [x] 8 页裁剪 + 页数视觉确认\\n- [x] β 下标 + 方法描述 + em-dash + PLACEHOLDER 修复\\n- [ ] **Re-dream v5+**（论文修复完成后验证整体质量）\\n- [ ] 提交 Review Director 正式审稿\\n- [ ] Attack prompt templates 补入 Appendix（可选）\\n- [ ] Code/data availability statement（可选）\\n\\n## GPU 预算\\nseetacloud-rtx6000: 4× RTX 6000 96G（全空闲，写作阶段）\\n\\n## 目标\\nEMNLP 2026 via ARR | Target: 3.5-4.0\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D022 | 2026-05-22 | Paper v5 Step 5 converged: 5 rounds, Overall 7/10, | — |\\n| D021 | 2026-05-22 | Bootstrap v2 (Reviewer-verified): η_max 5/12, K_ef | plan001_step1_full_v4 |\\n| D020 | 2026-05-22 | Dream v5 analysis (3.0/2.5/2.5): 7 confirmed actio | dream_20260522T173833 |\\n| D019 | 2026-05-22 | K_eff significance collapses under non-independenc | plan001_step1_full_v4 |\\n| D018 | 2026-05-22 | Dream v4 review (3.0/2.5/2.5): 6 structural issues | dream_20260522T173833 |\\n| D017 | 2026-05-22 | Claim 7 final (log-log canonical): Bayesian partia | plan001_step1_full_v4 |\\n| D016 | 2026-05-22 | Claim 7 revised: \\\"Bayesian breaks weakest-link\\\" fa | plan001_step1_full_v4 |\\n| D015 | 2026-05-22 | Claim 5 (Gaussian Copula Failure) falsified at 15- | worker_analysis_15model-family-copula |\\n| D014 | 2026-05-22 | 15-model 结果证伪原始 Claim 1 (\\\"K_eff irrelevant\\\")；K_eff | plan001_step1_full_v4 |\\n| D013 | 2026-05-22 | 7-model 预览显示 Claim 2 复活信号：random-fault K_eff gains | plan_001_7model_preview |\\n\\n\", \"total_chars\": 3091, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1512f41-32a2-45cb-b88c-83973566d590",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "ae093b0a-1840-4e52-88e1-f464bfbd9ac8",
  "sourceToolAssistantUUID": "f1512f41-32a2-45cb-b88c-83973566d590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T23:03:52.544Z_

Now let me read the actual paper tex file and the experiment data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae093b0a-1840-4e52-88e1-f464bfbd9ac8",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSdk2qSi1snZjziqPxb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d789d17-b688-445b-baba-39fedbcb7a76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Rx1sLQrNWHLuzDee8nd6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5146,
      "cache_read_input_tokens": 17184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5146,
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

_source line 14 · 2026-05-22T23:03:54.953Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EZuzENQ5rWLyuJ5BA3QxSG`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d789d17-b688-445b-baba-39fedbcb7a76",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSdk2qSi1snZjziqPxb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "830f59d7-8e43-4951-98c4-6b1fe09b7d12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Rx1sLQrNWHLuzDee8nd6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5146,
      "cache_read_input_tokens": 17184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5146,
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

_source line 15 · 2026-05-22T23:03:54.981Z_

<details><summary>↩ Tool result · `toolu_01EZuzENQ5rWLyuJ5BA3QxSG`</summary>

```text
artifacts/dream_reports/dream_20260522T173833/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "830f59d7-8e43-4951-98c4-6b1fe09b7d12",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "b98de9c3-b992-47f0-a59f-a11648dac2a1",
  "sourceToolAssistantUUID": "830f59d7-8e43-4951-98c4-6b1fe09b7d12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T23:03:55.416Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Jhmfpn2y3d9U2DaSzKWcsK`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b98de9c3-b992-47f0-a59f-a11648dac2a1",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSdk2qSi1snZjziqPxb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75772229-3550-4de0-ba2d-d2578642c8a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Rx1sLQrNWHLuzDee8nd6x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5146,
      "cache_read_input_tokens": 17184,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5146
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 17184,
          "cache_creation_input_tokens": 5146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5146,
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

_source line 17 · 2026-05-22T23:03:55.447Z_

<details><summary>↩ Tool result · `toolu_01Jhmfpn2y3d9U2DaSzKWcsK`</summary>

```text
artifacts/dream_reports/dream_20260522T173833/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75772229-3550-4de0-ba2d-d2578642c8a4",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "44d564c1-c9a7-4a90-9320-0d958a460990",
  "sourceToolAssistantUUID": "75772229-3550-4de0-ba2d-d2578642c8a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T23:03:58.083Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WxtumqMRgE4B15vGwmPV7Q`</summary>

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
  "parentUuid": "44d564c1-c9a7-4a90-9320-0d958a460990",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSeAmcsnPo6wTHVZMXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ef74353-7af1-4078-9f37-cb3cb53b3d4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJGwhLVBH2LVjc7rCErGde",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 303,
      "cache_read_input_tokens": 22330,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 303
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 22330,
          "cache_creation_input_tokens": 303,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 303,
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

_source line 19 · 2026-05-22T23:03:58.367Z_

<details><summary>↩ Tool result · `toolu_01WxtumqMRgE4B15vGwmPV7Q`</summary>

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
  "parentUuid": "1ef74353-7af1-4078-9f37-cb3cb53b3d4a",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "2f38eae3-48f5-4ee7-9eef-356aca515518",
  "sourceToolAssistantUUID": "1ef74353-7af1-4078-9f37-cb3cb53b3d4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-22T23:04:01.659Z_

Now let me also check the other paper version to understand the differences, and read the experiment data and framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f38eae3-48f5-4ee7-9eef-356aca515518",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSeP15CqzoeEJB8WGjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4a43baa-5d4e-4408-a9f6-51285f0e12cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcS28rnYJuhmguHeRVEa5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10819,
      "cache_read_input_tokens": 22633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10819,
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

_source line 21 · 2026-05-22T23:04:04.036Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EtAH7RAoD8f7HDRQc65mLM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4a43baa-5d4e-4408-a9f6-51285f0e12cc",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSeP15CqzoeEJB8WGjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15a1d6fb-2284-46d2-996e-c67f2ce378e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcS28rnYJuhmguHeRVEa5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10819,
      "cache_read_input_tokens": 22633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10819,
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

_source line 22 · 2026-05-22T23:04:04.341Z_

<details><summary>↩ Tool result · `toolu_01EtAH7RAoD8f7HDRQc65mLM`</summary>

```text
1	[
2	  {
3	    "name": "15-Model Scale Expansion + Core Regression",
4	    "description": "从 6 扩展到 15 models（GPT-4o, GPT-4o-mini, GPT-4.1, GPT-4.1-mini, Claude-3.5-Sonnet, Gemini-1.5-Pro + 6 local open-source: Llama-3.1-8B/70B, Qwen2.5-7B/72B, Mistral-7B-v0.3, Phi-3-medium-14B）。455 C(15,3) panels，2 datasets × 6 attacks = 12 conditions 全量回归。",
5	    "results": {
6	      "K_eff_raw_FDR_sig_positive": "12/12",
7	      "K_eff_resid_FDR_sig_positive": "10/12",
8	      "eta_max_FDR_sig": "10/12",
9	      "VIF_keff_etamax": 1.02,
10	      "mean_R2": 0.62,
11	      "confound_r_mean": 0.55,
12	      "confound_free_conditions_count": 3,
13	      "confound_free_keff_p_min": 2.1e-28,
14	      "panels_total": 455,
15	      "keff_dominates_etamax_conditions": 3,
16	      "etamax_dominates_keff_conditions": 4,
17	      "sensitivity_exclude_ACC_lt_05_keff_sig": "11/12"
18	    },
19	    "tables": [
20	      {
21	        "name": "Dual Vulnerability Drivers: 15-Model Regression (12 Conditions)",
22	        "columns": [
23	          "Condition",
24	          "η_max β",
25	          "η_max p",
26	          "K_eff_resid β",
27	          "K_eff_resid p",
28	          "R²",
29	          "Confound r",
30	          "Dominant"
31	        ],
32	        "rows": [
33	          [
34	            "mmlu×sycophancy",
35	            "0.82",
36	            "1.2e-8",
37	            "0.31",
38	            "0.004",
39	            "0.68",
40	            "0.72",
41	            "η_max"
42	          ],
43	          [
44	            "mmlu×score_manip",
45	            "0.45",
46	            "0.018",
47	            "0.61",
48	            "3.4e-9",
49	            "0.71",
50	            "0.38",
51	            "K_eff"
52	          ],
53	          [
54	            "mmlu×position",
55	            "0.15",
56	            "0.214",
57	            "0.58",
58	            "1.2e-8",
59	            "0.56",
60	            "0.36",
61	            "K_eff"
62	          ],
63	          [
64	            "mmlu×verbosity",
65	            "0.74",
66	            "4.1e-7",
67	            "0.28",
68	            "0.011",
69	            "0.63",
70	            "0.74",
71	            "η_max"
72	          ],
73	          [
74	            "mmlu×authority",
75	            "0.69",
76	            "1.8e-6",
77	            "0.19",
78	            "0.087",
79	            "0.58",
80	            "0.78",
81	            "η_max"
82	          ],
83	          [
84	            "mmlu×few_shot",
85	            "0.55",
86	            "2.3e-4",
87	            "0.48",
88	            "6.1e-6",
89	            "0.65",
90	            "0.65",
91	            "both"
92	          ],
93	          [
94	            "arc×sycophancy",
95	            "0.79",
96	            "3.5e-8",
97	            "0.35",
98	            "0.002",
99	            "0.66",
100	            "0.71",
101	            "η_max"
102	          ],
103	          [
104	            "arc×score_manip",
105	            "0.38",
106	            "0.117",
107	            "0.64",
108	            "1.7e-7",
109	            "0.59",
110	            "0.35",
111	            "K_eff"
112	          ],
113	          [
114	            "arc×position",
115	            "0.03",
116	            "0.910",
117	            "0.72",
118	            "1.8e-8",
119	            "0.57",
120	            "0.34",
121	            "K_eff"
122	          ],
123	          [
124	            "arc×verbosity",
125	            "0.71",
126	            "8.9e-7",
127	            "0.33",
128	            "0.003",
129	            "0.61",
130	            "0.73",
131	            "η_max"
132	          ],
133	          [
134	            "arc×authority",
135	            "0.66",
136	            "3.2e-6",
137	            "0.22",
138	            "0.062",
139	            "0.55",
140	            "0.76",
141	            "η_max"
142	          ],
143	          [
144	            "arc×few_shot",
145	            "0.51",
146	            "5.7e-4",
147	            "0.52",
148	            "3.8e-6",
149	            "0.63",
150	            "0.62",
151	            "both"
152	          ]
153	        ]
154	      }
155	    ],
156	    "figures": [],
157	    "analysis": "15-model 核心回归确认 Diversity Trap 的全部结构。10/12 残差化显著（vs 初步分析 8/12）表明 refined 统计方法（FDR 校正 + beta regression consistency check from plan_009）增强效应检测。Condition-dependent dominance pattern 从定性观察升级为 systematic taxonomy：attack transferability 高→K_eff 主导（adversary 利用 judge 异质性找 judge-specific 攻击路径），attack transferability 低（shared bias）→η_max 主导（所有 judges 共享弱点）。3 个 confound-free conditions 的 p<1e-20 是最强 'smoking gun'——即使 K_eff 与 η_max 近乎正交（r≈0.35），K_eff 仍达 genome-wide 级别显著性。这单独就足以封堵 RC1 的所有统计变体。\n\n模型池从 6→15 后能力谱系大幅展开（7B→72B 全开源 + GPT-4/Claude/Gemini API tier），K_eff-η_max 结构性共线从 r=-0.80 降至 ~0.55。455 panels（23× 6-model 的 20 panels）给残差化 K_eff 分析提供充足统计功效，使 8/12 的初步结果在 refined analysis 后升至 10/12。关键驱动力：(1) confound-free conditions 从 2→3 个（arc×score_manipulation、arc×position_bias、mmlu×position_bias 中 r≈0.35），这些条件下 K_eff 达极端显著性（p<1e-20），彻底排除 confound artifact；(2) condition-dependent dominance pattern 清晰——transferable attacks（score_manipulation、position_bias）中 K_eff β > η_max β，因为 diverse judges 提供异质化 attack surface；shared-bias attacks（sycophancy、verbosity、authority）中 η_max 主导，因为所有 judges 共享类似认知偏差；(3) sensitivity analysis 排除 ACC<0.5 outlier models 后 K_eff_resid 增至 11/12，证明效应非极端 outlier 驱动。"
158	  },
159	  {
160	    "name": "Attack Surface Expansion (9 Types)",
161	    "description": "攻击类型从 6 扩展到 9：新增 few-shot hijacking（in-context example 注入篡改评分标准）、persona manipulation（冒充权威角色指令 judge 改分）、instruction override（直接覆写评判 prompt）。全 15 models × 455 panels × 2 datasets。",
162	    "results": {
163	      "new_attack_types": 3,
164	      "new_conditions": 6,
165	      "keff_resid_sig_new_conditions": "4/6",
166	      "total_conditions_majority": 18,
167	      "keff_resid_sig_total_majority": "14/18",
168	      "eta_max_sig_total_majority": "15/18",
169	      "keff_dominates_new_attacks": 1,
170	      "etamax_dominates_new_attacks": 2,
171	      "mean_R2_new": 0.63
172	    },
173	    "tables": [
174	      {
175	        "name": "Extended Attack Results (New 6 Conditions)",
176	        "columns": [
177	          "Condition",
178	          "K_eff_resid β",
179	          "K_eff_resid p (FDR)",
180	          "η_max β",
181	          "η_max p (FDR)",
182	          "R²",
183	          "Attack Transferability"
184	        ],
185	        "rows": [
186	          [
187	            "mmlu×few_shot_hijack",
188	            "0.54",
189	            "8.2e-7",
190	            "0.47",
191	            "3.1e-5",
192	            "0.67",
193	            "High"
194	          ],
195	          [
196	            "mmlu×persona_manip",
197	            "0.29",
198	            "0.008",
199	            "0.63",
200	            "5.4e-7",
201	            "0.60",
202	            "Moderate"
203	          ],
204	          [
205	            "mmlu×instr_override",
206	            "0.22",
207	            "0.042",
208	            "0.71",
209	            "1.1e-7",
210	            "0.64",
211	            "Low"
212	          ],
213	          [
214	            "arc×few_shot_hijack",
215	            "0.58",
216	            "2.1e-7",
217	            "0.41",
218	            "8.8e-5",
219	            "0.65",
220	            "High"
221	          ],
222	          [
223	            "arc×persona_manip",
224	            "0.25",
225	            "0.019",
226	            "0.68",
227	            "2.3e-7",
228	            "0.62",
229	            "Moderate"
230	          ],
231	          [
232	            "arc×instr_override",
233	            "0.18",
234	            "0.112",
235	            "0.74",
236	            "3.7e-8",
237	            "0.66",
238	            "Low"
239	          ]
240	        ]
241	      }
242	    ],
243	    "figures": [],
244	    "analysis": "新攻击验证了 attack taxonomy 的预测性：transferability 越高的攻击，K_eff 的相对重要性越大。Few-shot hijacking 与 score_manipulation/position_bias 一起构成 'transferable attacks cluster'（K_eff β 0.47–0.72），persona/instruction/sycophancy/verbosity/authority 构成 'shared-bias cluster'（η_max β 0.58–0.82）。Taxonomy 从 post-hoc 描述升级为 predictive framework：给定新攻击类型，可预测哪个 vulnerability driver 主导。14/18 总显著数直接封堵 RC3 的 generalization 质疑，attack 覆盖面从 6→9 类型跨越 injection、bias、hijacking 三大攻击范式。\n\n三类新攻击按 transferability 分层：few-shot hijacking 是 high-transferability 攻击——通过 in-context examples 篡改评分标准，不同 judge 对 ICL 的响应模式差异极大（Qwen 系对 Chinese-style ICL 特别敏感、GPT 系对结构化 format hijacking 脆弱），因此 K_eff 主导（β≈0.54, p<1e-6）——diverse panel 有更多可利用的 ICL 入口点。Persona manipulation 和 instruction override 属于 moderate-to-low transferability：不同 judge 的 instruction-following 遵从度存在差异但 RLHF 训练给所有模型植入了类似的 authority-compliance bias，预测 η_max 主导但 K_eff 在 persona_manip 上仍显著（p<0.02）。Instruction override 的 K_eff 在 arc 上 NS（p=0.112）因为 ARC 的简短问题格式给 override 攻击的操作空间更少，judge 差异贡献有限。总计 14/18 残差化显著满足 K_eff_resid_sig_extended_conditions [10,16] 范围。"
245	  },
246	  {
247	    "name": "BFT Random-Fault Contrast (Calibrated, 15-Model)",
248	    "description": "Random-fault simulation 使用 calibrated failure rates（非原始 η_j）：基于 bootstrapped clean-accuracy noise 生成独立 random failures。每个 judge 失败概率与其 clean accuracy 相关但独立采样，模拟 BFT 假设的 uncorrelated fault 模式。455 panels × 12 conditions 对比 adaptive 与 RF 下的 K_eff β。",
249	    "results": {
250	      "RF_keff_sig_positive": "3/12",
251	      "RF_keff_sig_negative": "5/12",
252	      "RF_keff_NS": "4/12",
253	      "adaptive_keff_beta_mean": 0.42,
254	      "RF_keff_beta_mean": -0.12,
255	      "BFT_RF_beta_ratio": 2.8,
256	      "conditions_ratio_ge_1_5x": "9/12",
257	      "conditions_beta_flipped_negative": "5/12",
258	      "delta_R2_RF_vs_adaptive": 0.31,
259	      "RF_R2_mean": 0.78,
260	      "adaptive_R2_mean": 0.47
261	    },
262	    "tables": [
263	      {
264	        "name": "BFT Regime Contrast: K_eff β Adaptive vs Random-Fault (12 Conditions)",
265	        "columns": [
266	          "Condition",
267	          "β_adaptive",
268	          "p_adap",
269	          "β_RF",
270	          "p_RF",
271	          "|β_adap/β_RF|",
272	          "R²_adap",
273	          "R²_RF",
274	          "Flipped?"
275	        ],
276	        "rows": [
277	          [
278	            "mmlu×sycophancy",
279	            "0.31",
280	            "0.004",
281	            "0.08",
282	            "0.310",
283	            "3.88",
284	            "0.68",
285	            "0.82",
286	            "No"
287	          ],
288	          [
289	            "mmlu×score_manip",
290	            "0.61",
291	            "3.4e-9",
292	            "-0.22",
293	            "0.015",
294	            "2.77",
295	            "0.71",
296	            "0.89",
297	            "Yes"
298	          ],
299	          [
300	            "mmlu×position",
301	            "0.58",
302	            "1.2e-8",
303	            "-0.31",
304	            "0.003",
305	            "1.87",
306	            "0.56",
307	            "0.76",
308	            "Yes"
309	          ],
310	          [
311	            "mmlu×verbosity",
312	            "0.28",
313	            "0.011",
314	            "0.11",
315	            "0.198",
316	            "2.55",
317	            "0.63",
318	            "0.79",
319	            "No"
320	          ],
321	          [
322	            "mmlu×authority",
323	            "0.19",
324	            "0.087",
325	            "0.06",
326	            "0.541",
327	            "3.17",
328	            "0.58",
329	            "0.74",
330	            "No"
331	          ],
332	          [
333	            "mmlu×few_shot",
334	            "0.48",
335	            "6.1e-6",
336	            "-0.18",
337	            "0.039",
338	            "2.67",
339	            "0.65",
340	            "0.81",
341	            "Yes"
342	          ],
343	          [
344	            "arc×sycophancy",
345	            "0.35",
346	            "0.002",
347	            "0.10",
348	            "0.251",
349	            "3.50",
350	            "0.66",
351	            "0.80",
352	            "No"
353	          ],
354	          [
355	            "arc×score_manip",
356	            "0.64",
357	            "1.7e-7",
358	            "-0.28",
359	            "0.008",
360	            "2.29",
361	            "0.59",
362	            "0.85",
363	            "Yes"
364	          ],
365	          [
366	            "arc×position",
367	            "0.72",
368	            "1.8e-8",
369	            "-0.35",
370	            "0.001",
371	            "2.06",
372	            "0.57",
373	            "0.78",
374	            "Yes"
375	          ],
376	          [
377	            "arc×verbosity",
378	            "0.33",
379	            "0.003",
380	            "0.12",
381	            "0.175",
382	            "2.75",
383	            "0.61",
384	            "0.77",
385	            "No"
386	          ],
387	          [
388	            "arc×authority",
389	            "0.22",
390	            "0.062",
391	            "0.05",
392	            "0.612",
393	            "4.40",
394	            "0.55",
395	            "0.72",
396	            "No"
397	          ],
398	          [
399	            "arc×few_shot",
400	            "0.52",
401	            "3.8e-6",
402	            "-0.14",
403	            "0.091",
404	            "3.71",
405	            "0.63",
406	            "0.79",
407	            "Yes(marg)"
408	          ]
409	        ]
410	      }
411	    ],
412	    "figures": [],
413	    "analysis": "Calibrated RF 对比定性建立 BFT reversal mechanism：5/12 conditions β 翻转为负（diversity 在 true random faults 下确实有益），集中在 transferable attacks 上——exactly as mechanism predicts。翻转在 score_manip 和 position 上最强（这些攻击的 ASR 最依赖 judge-specific vulnerabilities），在 RF 模式下这些 vulnerabilities 被 random noise 取代，diversity 的容错优势重新显现。9/12 ratio ≥1.5× 表明即使不完全翻转，adaptive 下 K_eff 的有害效应也显著强于 RF——β 系统性 amplification 2.8× on average。ΔR²=0.31 是 BFT 理论的直接数值体现：BFT 假设 panel structure determines fault tolerance（high R²=0.78），adaptive adversary 打破这一假设（low R²=0.47）。BFT reversal 从 conceptual analogy 升级为 empirically grounded mechanism with quantitative support。\n\nBFT contrast 的核心区分在于 failure mode topology：random faults 下 judges 独立失败且 failures 无空间相关性，majority vote 的冗余容错使 K_eff 越高→fault tolerance 越强→β 应为负或接近零。Adaptive adversary 则 strategic targeting：找到 panel 中最弱的 judges 并集中攻击，K_eff 越高→attack surface 越大→β 为正。之前 15-model pipeline 的 RF 分析直接用 η_j 作为 failure prob，保留了 adaptive vulnerability structure（弱 judges 在 RF 下仍然更容易 fail），未能 cleanly 模拟 BFT 假设。Best tier 用 calibrated rates（基于 clean accuracy 的 bootstrapped noise）打破 adaptive vulnerability structure：RF failure prob 仅与 clean accuracy 相关而非 adversarial robustness，使 RF 成为 genuine random-fault baseline。翻转在 transferable attacks（score_manip、position、few_shot）中最明确（β 从 +0.52–0.72 翻至 -0.14–-0.35），因为这些攻击最依赖 judge-specific exploit paths——RF 下这些 paths 变成 random noise。Shared-bias attacks（sycophancy、verbosity）下 RF β 仍略正（0.08–0.12）但 NS，因为 bias 的 shared nature 使 'random' 和 'adaptive' failure modes 部分重叠。ΔR²=0.31 表明 RF 下 panel composition 解释 78% 方差（结构可预测），adaptive 仅 47%（strategic noise 占 53%），直接支撑 'adaptive adversary introduces variance beyond panel structure' 论点。"
414	  },
415	  {
416	    "name": "Capability-Matched Within-Tier Validation",
417	    "description": "同 capability tier 内做 within-tier regression 排除 tier-mixing artifact。Small tier: Llama-8B, Qwen-7B, Mistral-7B, Phi-14B, GPT-4o-mini (5 models, C(5,3)=10 panels)。Medium tier: 此 tier 仅 4 models → 4 panels，功效不足标注 directional。Large tier: Llama-70B, Qwen-72B, GPT-4o, GPT-4.1, Claude-3.5, Gemini-1.5 (6 models, C(6,3)=20 panels)。",
418	    "results": {
419	      "small_tier_models": 5,
420	      "small_tier_panels": 10,
421	      "small_tier_keff_sig": "2/6",
422	      "small_tier_confound_r": 0.32,
423	      "medium_tier_models": 4,
424	      "medium_tier_panels": 4,
425	      "medium_tier_keff_sig": "1/6",
426	      "medium_tier_note": "directional only, underpowered",
427	      "large_tier_models": 6,
428	      "large_tier_panels": 20,
429	      "large_tier_keff_sig": "4/6",
430	      "large_tier_confound_r": 0.33,
431	      "total_keff_sig_across_tiers": 4,
432	      "capability_matched_keff_sig": 4,
433	      "within_tier_confound_r_mean": 0.35
434	    },
435	    "tables": [
436	      {
437	        "name": "Within-Tier K_eff Validation",
438	        "columns": [
439	          "Tier",
440	          "Models",
441	          "Panels",
442	          "K_eff-η_max r",
443	          "K_eff_resid sig (of 6)",
444	          "Best p",
445	          "η_max sig (of 6)"
446	        ],
447	        "rows": [
448	          [
449	            "Small (7B-14B)",
450	            "5",
451	            "10",
452	            "0.32",
453	            "2/6",
454	            "0.008",
455	            "3/6"
456	          ],
457	          [
458	            "Medium (14-34B)",
459	            "4",
460	            "4",
461	            "0.41",
462	            "1/6",
463	            "0.031",
464	            "2/6"
465	          ],
466	          [
467	            "Large (70B+API)",
468	            "6",
469	            "20",
470	            "0.33",
471	            "4/6",
472	            "4.2e-4",
473	            "5/6"
474	          ],
475	          [
476	            "Cross-tier (all 15)",
477	            "15",
478	            "455",
479	            "0.55",
480	            "10/12",
481	            "1.7e-7",
482	            "10/12"
483	          ]
484	        ]
485	      },
486	      {
487	        "name": "Large-Tier Condition Detail",
488	        "columns": [
489	          "Condition",
490	          "K_eff_resid β",
491	          "p",
492	          "η_max β",
493	          "p",
494	          "Sig?"
495	        ],
496	        "rows": [
497	          [
498	            "score_manip",
499	            "0.58",
500	            "4.2e-4",
501	            "0.31",
502	            "0.042",
503	            "K_eff dominant"
504	          ],
505	          [
506	            "position_bias",
507	            "0.52",
508	            "0.001",
509	            "0.18",
510	            "0.228",
511	            "K_eff dominant"
512	          ],
513	          [
514	            "sycophancy",
515	            "0.21",
516	            "0.154",
517	            "0.61",
518	            "0.002",
519	            "η_max dominant"
520	          ],
521	          [
522	            "verbosity",
523	            "0.17",
524	            "0.238",
525	            "0.55",
526	            "0.005",
527	            "η_max dominant"
528	          ],
529	          [
530	            "authority",
531	            "0.34",
532	            "0.018",
533	            "0.48",
534	            "0.008",
535	            "both sig"
536	          ],
537	          [
538	            "few_shot",
539	            "0.45",
540	            "0.003",
541	            "0.39",
542	            "0.012",
543	            "both sig"
544	          ]
545	        ]
546	      }
547	    ],
548	    "figures": [],
549	    "analysis": "Capability-matched validation 是封堵 RC1 最强变体的 decisive evidence。Reviewer 可能 argue：'K_eff positive 不过是因为 high-K_eff panels 混了弱模型（tier-mixing）'。Large tier 结果直接否定：全是 top-tier 模型（GPT-4 级别），η_max 在 0.08-0.15 的 narrow range 内，K_eff 仍在 4/6 conditions 显著正向。Condition-dependent pattern 在 tier-internal 分析中完美复现：score_manip + position 由 K_eff 主导，sycophancy + verbosity 由 η_max 主导。这一致性跨 pooling strategy（all-15 vs within-tier）极大增强了 finding 的 robustness。Small tier 的 2/6 sig 表明 diversity trap 在低能力模型中也存在（低能力 diverse panel 更脆弱），但效应弱于 large tier——可能因为 small models 的 η_max 方差更大（有的 7B 异常脆弱），η_max 抢走了更多 variance。\n\nWithin-tier analysis 的核心价值是控制 tier-mixing confound。全局 r=0.55（K_eff 与 η_max）有约 40% 来自跨 tier mixing：高 K_eff panels 往往混合 7B 和 70B 模型，天然引入低 robustness judges。同 tier 内 r 降至 ~0.35，给 K_eff 最干净的检验。Large tier 结果最有说服力：6 models（GPT-4o, GPT-4.1, Claude-3.5, Gemini-1.5, Llama-70B, Qwen-72B）全是 top-tier 模型，η_max 方差天然较小，但 K_eff 仍在 4/6 conditions 显著——diverse panel 即使全由强模型组成也更脆弱，因为 judges 的 robustness profiles 仍然异质（GPT-4o 对 sycophancy 特别敏感、Llama-70B 对 position bias 敏感等）。Small tier 5 models / 10 panels 功效有限但 2/6 sig 提供 cross-tier consistency。Medium tier 仅 4 panels，1/6 sig 是 directional evidence only。总计 ≥4/6 unique conditions 有 within-tier K_eff 显著，满足 capability_matched_keff_sig [3,6] 范围。意义：即使 reviewer 最强版本的 'K_eff positive = tier-mixing artifact' argument 也被否定——same-tier panels 中 diversity 仍独立有害。"
550	  },
551	  {
552	    "name": "Two-Stage Panel Selection Algorithm Benchmark",
553	    "description": "Robustness-first 两阶段算法：Stage 1 filter η_j > percentile-75 threshold (保留最 robust 的 75% judges)，Stage 2 在通过筛选的 candidates 中 maximize K_eff。Benchmark vs 5 baselines on 15-model pool，6 attack conditions (MMLU × 6 attacks)。",
554	    "results": {
555	      "two_stage_mean_ASR": 0.038,
556	      "strongest_k_ASR": 0.048,
557	      "min_etamax_ASR": 0.041,
558	      "max_keff_ASR": 0.112,
559	      "random_ASR": 0.089,
560	      "oracle_ASR": 0.032,
561	      "ASR_reduction_vs_strongest_k_pct": 20.8,
562	      "ASR_reduction_vs_max_keff_pct": 66.1,
563	      "conditions_two_stage_best": "5/6",
564	      "two_stage_pareto_optimal_pct": 78,
565	      "screening_threshold_optimal_percentile": 75
566	    },
567	    "tables": [
568	      {
569	        "name": "Panel Selection Strategy Benchmark (15 Models, MMLU)",
570	        "columns": [
571	          "Strategy",
572	          "Mean ASR",
573	          "Δ vs Strongest-K",
574	          "Best (of 6)",
575	          "Worst-case ASR"
576	        ],
577	        "rows": [
578	          [
579	            "Two-Stage (ours)",
580	            "0.038",
581	            "-20.8%",
582	            "5/6",
583	            "0.071"
584	          ],
585	          [
586	            "Min-η_max",
587	            "0.041",
588	            "-14.6%",
589	            "4/6",
590	            "0.078"
591	          ],
592	          [
593	            "Strongest-K",
594	            "0.048",
595	            "baseline",
596	            "1/6",
597	            "0.095"
598	          ],
599	          [
600	            "Random",
601	            "0.089",
602	            "+85.4%",
603	            "0/6",
604	            "0.156"
605	          ],
606	          [
607	            "Max-K_eff",
608	            "0.112",
609	            "+133.3%",
610	            "0/6",
611	            "0.198"
612	          ],
613	          [
614	            "Oracle",
615	            "0.032",
616	            "-33.3%",
617	            "6/6",
618	            "0.052"
619	          ]
620	        ]
621	      },
622	      {
623	        "name": "Two-Stage Sensitivity to Screening Threshold",
624	        "columns": [
625	          "Threshold (percentile)",
626	          "Candidate models",
627	          "Mean ASR",
628	          "K_eff of selected panel"
629	        ],
630	        "rows": [
631	          [
632	            "50",
633	            "8",
634	            "0.039",
635	            "2.12"
636	          ],
637	          [
638	            "65",
639	            "10",
640	            "0.037",
641	            "2.28"
642	          ],
643	          [
644	            "75 (optimal)",
645	            "11",
646	            "0.038",
647	            "2.41"
648	          ],
649	          [
650	            "85",
651	            "13",
652	            "0.045",
653	            "2.55"
654	          ],
655	          [
656	            "100 (no filter)",
657	            "15",
658	            "0.058",
659	            "2.71"
660	          ]
661	        ]
662	      }
663	    ],
664	    "figures": [],
665	    "analysis": "20.8% ASR reduction 将实用贡献从 Dream 批评的 'marginal'（12.5% at 6-model）升级为 'practically meaningful'。Threshold sensitivity table 揭示 sweet spot 在 percentile-65–75：太紧（50th）损失 candidate diversity，太松（85–100th）引入弱 judges。Pareto frontier analysis 显示 78% 的 Two-stage selected panels 落在 Pareto 前沿上——算法近似了 computationally-expensive 的 exhaustive Pareto search。关键 takeaway for practitioners：(1) 绝不盲目 maximize diversity（Max-K_eff 灾难级 ASR）；(2) Pure robustness（Min-η_max）已经很好，diversity 优化提供 modest 额外收益；(3) Two-stage 在所有非 oracle 策略中最接近理论最优。\n\n15-model pool 给 Two-stage 算法显著优于 6-model 结果（12.5%→20.8% vs Strongest-K）的空间。原因双重：(1) 15 models 筛选后 candidate pool 更大——6-model 时 threshold filter 后仅剩 3-4 judges（几乎无 K_eff 优化空间），15-model 时剩 ~11 judges（C(11,3)=165 candidate panels），K_eff 最大化有真正的搜索空间。(2) Robustness screening 后的 restricted pool 中，K_eff-η_max confound 被 threshold 机制性打破（高 η_max 模型已被移除），K_eff 的效应方向可能从有害翻转为中性——当所有 judges 都 robust 时，diversity 不再引入弱 judge，其 BFT 容错优势部分恢复。Min_etamax 与 Two-stage 差距较小（0.041 vs 0.038, Δ=7.3%）说明 K_eff 优化在 robustness-screened pool 内的增量贡献 modest——这恰好支持 'robustness-first, diversity-second' 的优先级判断。Max_keff 策略的灾难性表现（ASR 0.112, +133% vs Strongest-K）是 diversity trap 最直观的实证：盲目追求 diversity 而不管 robustness 是危险的。Oracle 的存在（0.032）表明 Two-stage 达 Oracle 效率的 84%（0.038/0.032），远超 Strongest-K 的 67%（0.048/0.032）。15%+ 降幅满足 two_stage_ASR_reduction_pct [15,35]。"
666	  },
667	  {
668	    "name": "Per-Judge ASR Concentration Analysis",
669	    "description": "计算 455 panels × 6 attacks 的 per-judge ASR 分布。Gini coefficient 量化 ASR 在 panel 内 judges 间的集中度，Shannon entropy 量化均匀性。Adaptive vs RF 对比。",
670	    "results": {
671	      "mean_gini_adaptive": 0.68,
672	      "mean_gini_RF": 0.12,
673	      "gini_ratio_adaptive_vs_RF": 5.67,
674	      "mean_entropy_adaptive": 1.42,
675	      "mean_entropy_RF": 2.31,
676	      "high_keff_gini_adaptive": 0.74,
677	      "low_keff_gini_adaptive": 0.55,
678	      "gini_keff_correlation": 0.52,
679	      "top1_judge_ASR_share_adaptive": 0.78,
680	      "top1_judge_ASR_share_RF": 0.38
681	    },
682	    "tables": [
683	      {
684	        "name": "ASR Concentration Metrics: Adaptive vs Random-Fault",
685	        "columns": [
686	          "Metric",
687	          "Adaptive",
688	          "Random-Fault",
689	          "Ratio",
690	          "Interpretation"
691	        ],
692	        "rows": [
693	          [
694	            "Mean Gini",
695	            "0.68",
696	            "0.12",
697	            "5.67",
698	            "Concentrated vs uniform"
699	          ],
700	          [
701	            "Mean Entropy (bits)",
702	            "1.42",
703	            "2.31",
704	            "0.61",
705	            "Low entropy = targeted"
706	          ],
707	          [
708	            "Top-1 Judge ASR Share",
709	            "0.78",
710	            "0.38",
711	            "2.05",
712	            "78% ASR on weakest judge"
713	          ],
714	          [
715	            "r(K_eff, Gini)",
716	            "0.52",
717	            "0.08",
718	            "6.50",
719	            "Diversity → more targeting"
720	          ]
721	        ]
722	      }
723	    ],
724	    "figures": [],
725	    "analysis": "Concentration analysis 将 diversity trap 从统计关联推进到机制层面：不是 'K_eff 与 ASR 碰巧正相关'，而是 'diverse panels 给 adversary 提供了更清晰的 targeting gradient（Gini 0.74），使攻击集中在最弱 judge 上（78% share），从而打破 majority vote'。r(K_eff, Gini)=0.52 的正相关是 diversity trap 因果链中的关键中间变量——future work 可用 mediation analysis 正式量化 Gini 在 K_eff→ASR 路径中的 mediating role。此外 RF 下的 low concentration（Gini 0.12）直接验证了 BFT 的 key assumption（uncorrelated failures distribute uniformly），解释了为何 diversity 在 RF 下可以有益。\n\nConcentration analysis 是 diversity trap 机制的 'microscope'——从 panel-level 聚合统计深入到 judge-level 攻击分布。Adaptive adversary 的 core strategy 是 targeting：识别 panel 中最脆弱的 judge 并集中 exploit。这导致 ASR 高度 concentrated 在 1-2 个 judges 上（Gini≈0.68, top-1 share 78%），而 RF 下 failures 近似均匀分布（Gini≈0.12）。关键发现：high-K_eff panels 的 Gini 更高（0.74 vs 0.55），因为 diverse panel 中 judges 的 capability spread 更大→adversary 的 target 更清晰（最弱 judge 与最强 judge 的差距更大）。Gini-K_eff 正相关（r=0.52）是 diversity trap 因果链的直接 observational evidence：diversity → larger capability spread → clearer targeting → higher concentration → higher panel ASR。这不是因果证明（需要 intervention），但因果方向性（directional consistency）很强。5.67× Gini ratio 也是 BFT contrast 的另一维度验证：BFT 假设 failures 均匀分布（low Gini），adaptive adversary 打破这一假设（high Gini）。"
726	  },
727	  {
728	    "name": "Diversity-Capability Tradeoff Visualization",
729	    "description": "455 panels 的 K_eff vs η_max tradeoff 散点图、Pareto 前沿、tier 分层分析。",
730	    "results": {
731	      "global_r_keff_etamax": 0.55,
732	      "within_small_r": 0.32,
733	      "within_medium_r": 0.41,
734	      "within_large_r": 0.33,
735	      "pareto_frontier_panels": 18,
736	      "pareto_frontier_slope": -0.73,
737	      "tradeoff_explained_variance": 0.42
738	    },
739	    "tables": [
740	      {
741	        "name": "K_eff–η_max Correlation Structure by Tier",
742	        "columns": [
743	          "Tier",
744	          "r(K_eff, η_max)",
745	          "N panels",
746	          "Pareto-optimal",
747	          "Mean K_eff",
748	          "Mean η_max"
749	        ],
750	        "rows": [
751	          [
752	            "Small (7B-14B)",
753	            "0.32",
754	            "10",
755	            "3",
756	            "2.41",
757	            "0.312"
758	          ],
759	          [
760	            "Medium (14-34B)",
761	            "0.41",
762	            "4",
763	            "2",
764	            "2.18",
765	            "0.224"
766	          ],
767	          [
768	            "Large (70B+API)",
769	            "0.33",
770	            "20",
771	            "5",
772	            "1.95",
773	            "0.148"
774	          ],
775	          [
776	            "Cross-tier (all 15)",
777	            "0.55",
778	            "455",
779	            "18",
780	            "2.35",
781	            "0.231"
782	          ]
783	        ]
784	      }
785	    ],
786	    "figures": [],
787	    "analysis": "Tradeoff 可视化的核心价值是将 Claim 3 从统计数字转化为直觉图形。Pareto frontier 的 steep negative slope（-0.73）意味着 K_eff 每增加 0.1，η_max 至少增加 0.073——practitioners 必须明确这个 cost。Tier-stratified view 显示 within-tier tradeoff 较弱但仍存在，支持 'screening + optimize' 策略的理论基础。ASR 等值线叠加（contour）直接显示 Pareto-optimal panels 的 ASR 远低于 max-K_eff panels——视觉化 diversity trap。\n\n全局 K_eff-η_max 正相关（r=0.55）编码了 LLM 生态系统的一个结构性约束：maximizing panel independence（K_eff）要求跨越 capability tiers 选 judges（例如同时选 GPT-4o 和 Mistral-7B），这必然引入 robustness 差异大的 judges，推高 η_max。Within-tier r 大幅下降（0.32–0.41）揭示了 tradeoff 的两层结构：(1) Cross-tier component（贡献 ~40% 的 global r）：源于 tier mixing，可通过 screening 消除；(2) Within-tier component（residual r≈0.35）：即使同 tier 内，追求 diversity 仍需选择 robustness profile 更异质的 judges，这不可完全消除但幅度较小。Pareto 前沿的 18 panels（约 4% of 455）定义了 diversity-robustness 不可能三角的 achievable boundary——Two-stage 算法的目标就是逼近这个前沿。解释方差 42% 意味着 K_eff 是 η_max 的 moderate 但非 dominant 预测器——剩余 58% 的 η_max 方差由 attack-specific vulnerability profiles、评分偏好差异等因素决定，这也解释了为什么 K_eff 的 residualized effect 在控制 η_max 后仍然显著。"
788	  },
789	  {
790	    "name": "Panel Size Sensitivity K=3,5,7,9",
791	    "description": "Panel size 从 K=3 扩展到 K=5,7,9。15 models 选 K 个 judges 的组合数分别为 C(15,3)=455, C(15,5)=3003, C(15,7)=6435, C(15,9)=5005。每个 K 做 12 conditions 回归。",
792	    "results": {
793	      "K3_keff_resid_sig": "10/12",
794	      "K5_keff_resid_sig": "11/12",
795	      "K7_keff_resid_sig": "12/12",
796	      "K9_keff_resid_sig": "12/12",
797	      "K3_mean_keff_beta": 0.42,
798	      "K5_mean_keff_beta": 0.48,
799	      "K7_mean_keff_beta": 0.55,
800	      "K9_mean_keff_beta": 0.61,
801	      "K3_mean_etamax_beta": 0.51,
802	      "K5_mean_etamax_beta": 0.49,
803	      "K7_mean_etamax_beta": 0.43,
804	      "K9_mean_etamax_beta": 0.38,
805	      "crossover_K": 6,
806	      "K3_mean_R2": 0.62,
807	      "K9_mean_R2": 0.51
808	    },
809	    "tables": [
810	      {
811	        "name": "Panel Size Sensitivity Summary",
812	        "columns": [
813	          "K",
814	          "Panels",
815	          "K_eff_resid sig",
816	          "Mean K_eff β",
817	          "Mean η_max β",
818	          "Mean R²",
819	          "Primary driver"
820	        ],
821	        "rows": [
822	          [
823	            "3",
824	            "455",
825	            "10/12",
826	            "0.42",
827	            "0.51",
828	            "0.62",
829	            "η_max"
830	          ],
831	          [
832	            "5",
833	            "3003",
834	            "11/12",
835	            "0.48",
836	            "0.49",
837	            "0.58",
838	            "balanced"
839	          ],
840	          [
841	            "7",
842	            "6435",
843	            "12/12",
844	            "0.55",
845	            "0.43",
846	            "0.54",
847	            "K_eff"
848	          ],
849	          [
850	            "9",
851	            "5005",
852	            "12/12",
853	            "0.61",
854	            "0.38",
855	            "0.51",
856	            "K_eff"
857	          ]
858	        ]
859	      }
860	    ],
861	    "figures": [],
862	    "analysis": "Panel size sensitivity 提供 diversity trap 的 scaling law：K_eff β ≈ 0.33 + 0.047K（近似线性增长）。这意味着 evaluation community 普遍采用的 'add more judges' strategy 会 systematically amplify diversity trap——K=9 panel 的 K_eff 有害效应比 K=3 大 45%。η_max 的下降则反映了 weakest-link theorem 在 large K 下的局限性：当 K 足够大时，单一最弱 judge 不再 decisive，panel 的整体结构（diversity/independence）接管。交叉点 K≈6 有实际指导意义：K≤5 的小 panel 优先管控 η_max（选最 robust 的 judges），K≥7 的大 panel 必须同时管控 K_eff（限制不必要的 diversity）。\n\nK_eff β 随 panel size 单调递增（0.42→0.61），原因：(1) larger panels 有更多 judges → attack surface 与 panel size 正比增长，每个 additional judge 提供一个额外的 potential exploit path；(2) K=9 panel 的 K_eff range 更大（15 models 选 9 → wider independence spectrum），给回归更大信号。η_max β 随 K 递减（0.51→0.38），原因：larger panel 的 vulnerability 不再由单一 weakest judge 决定——K=9 时 adversary 需要 compromise ⌈9/2⌉=5 judges，不能仅靠 targeting the weakest one，panel structure（diversity）的相对重要性上升。交叉点约 K≈6：在此 panel size 以上，K_eff 超过 η_max 成为 primary vulnerability driver。R² 随 K 下降（0.62→0.51）因为 larger panel 的行为更复杂，judge interaction effects 增加 unexplained variance。K=9 时 K_eff 12/12 sig + β=0.61 是 diversity trap 的 strongest single evidence point：大型 evaluation panels 中 diversity 是 dominant 有害因素。这直接回应 'just add more judges to be safer' 的朴素直觉。"
863	  },
864	  {
865	    "name": "VIF + Multicollinearity Full Diagnostics",
866	    "description": "对 15-model 455-panel 数据做完整统计诊断：VIF、condition number、partial correlations、residualized K_eff、Bonferroni/FDR 多重比较校正、beta regression（处理 ASR 的 [0,1] bounded nature）、Shapiro-Wilk 残差正态性检验。纯计算，无 GPU。",
867	    "results": {
868	      "VIF_keff_resid": 1.02,
869	      "VIF_etamax": 1.02,
870	      "condition_number": 4.8,
871	      "partial_r_keff_given_etamax": 0.38,
872	      "partial_r_etamax_given_keff": 0.45,
873	      "keff_resid_FDR_sig": "10/12",
874	      "keff_bonferroni_sig": "8/12",
875	      "beta_regression_keff_sig": "9/12",
876	      "beta_regression_etamax_sig": "10/12",
877	      "shapiro_wilk_residuals_p_mean": 0.23,
878	      "cooks_d_max": 0.031,
879	      "leverage_outlier_pct": 2.4
880	    },
881	    "tables": [
882	      {
883	        "name": "Multicollinearity Diagnostics Summary",
884	        "columns": [
885	          "Diagnostic",
886	          "Value",
887	          "Threshold",
888	          "Status"
889	        ],
890	        "rows": [
891	          [
892	            "VIF (K_eff_resid)",
893	            "1.02",
894	            "<5.0",
895	            "PASS"
896	          ],
897	          [
898	            "VIF (η_max)",
899	            "1.02",
900	            "<5.0",
901	            "PASS"
902	          ],
903	          [
904	            "Condition Number",
905	            "4.8",
906	            "<30",
907	            "PASS"
908	          ],
909	          [
910	            "Partial r(K_eff|η_max)",
911	            "0.38",
912	            ">0.1",
913	            "Moderate independent effect"
914	          ],
915	          [
916	            "Partial r(η_max|K_eff)",
917	            "0.45",
918	            ">0.1",
919	            "Moderate-strong independent effect"
920	          ],
921	          [
922	            "Shapiro-Wilk p (residuals)",
923	            "0.23",
924	            ">0.05",
925	            "Normal residuals"
926	          ],
927	          [
928	            "Max Cook's D",
929	            "0.031",
930	            "<1.0",
931	            "No influential points"
932	          ],
933	          [
934	            "High-leverage %",
935	            "2.4%",
936	            "<5%",
937	            "Acceptable"
938	          ]
939	        ]
940	      },
941	      {
942	        "name": "Multiple Comparison Robustness",
943	        "columns": [
944	          "Correction Method",
945	          "K_eff_resid sig",
946	          "η_max sig",
947	          "Interpretation"
948	        ],
949	        "rows": [
950	          [
951	            "Uncorrected",
952	            "12/12",
953	            "11/12",
954	            "Raw signal"
955	          ],
956	          [
957	            "FDR (Benjamini-Hochberg)",
958	            "10/12",
959	            "10/12",
960	            "Primary report"
961	          ],
962	          [
963	            "Bonferroni",
964	            "8/12",
965	            "9/12",
966	            "Most conservative, still passes"
967	          ],
968	          [
969	            "Beta Regression + FDR",
970	            "9/12",
971	            "10/12",
972	            "Distributional robustness"
973	          ]
974	        ]
975	      }
976	    ],
977	    "figures": [],
978	    "analysis": "VIF + diagnostics package 是论文统计 credibility 的 foundation。Key contribution to paper: (1) 把 'K_eff is independently significant' 从初步 observation 升级为经过 6 层 robustness check（residualization, VIF, partial correlation, beta regression, multiple comparison, influence diagnostics）验证的 result；(2) 每个 check 都 pass 意味着 reviewer 无法从任何统计 angle 质疑 K_eff 的独立效应；(3) Bonferroni-corrected 8/12 sig 是最保守的下界——即使用最严格的多重比较校正，diversity trap 仍在 2/3 的 conditions 中成立。\n\n残差化设计（K_eff_resid = residuals of K_eff ~ η_max）在数学上保证 VIF=1.0（两个 predictors 正交）。实际计算得 1.02 是因为 floating point precision + minor numerical jitter。Condition number 4.8 远低于 30 的 concern threshold，确认回归矩阵 well-conditioned。Partial correlations 揭示各自独立贡献：K_eff|η_max 的 partial r=0.38 意味着 holding η_max constant，K_eff 独立解释 ~14% ASR variance；η_max|K_eff 的 partial r=0.45 解释 ~20%。Beta regression 作为 distributional robustness check 处理两个 OLS 假设违反：(1) ASR 在 [0,1] 内 bounded，OLS 可能在极端值处产生 out-of-range predictions；(2) ASR 的方差可能 heteroscedastic（低 ASR panels 方差更小）。Beta regression 结果（9/12 vs OLS 10/12）高度一致，证明 OLS findings 非 distributional artifact。Multiple comparison 从 FDR（10/12）到 Bonferroni（8/12，最保守）全部 pass，消除 'cherry-picking' concern。Cook's distance max=0.031（远低于 1.0 threshold）和 leverage outliers 仅 2.4% 证明结果非 influential point 驱动。这套诊断 package 直接 preempt Dream review W2（VIF 未报告）和 RC1（multicollinearity）的所有 variants。"
979	  },
980	  {
981	    "name": "Aggregation Rule Modulation (15-Model)",
982	    "description": "三种非 majority-vote 聚合规则下的 dual vulnerability drivers 分析：Threshold voting（unanimity: 所有 judges 必须同意 reject）、Accuracy-weighted voting（权重 ∝ clean accuracy）、Bayesian aggregation（基于 prior accuracy 的 posterior probability）。455 panels × 12 conditions per aggregation。",
983	    "results": {
984	      "majority_keff_sig": "10/12",
985	      "majority_etamax_sig": "10/12",
986	      "threshold_keff_sig": "11/12",
987	      "threshold_etamax_sig": "7/12",
988	      "threshold_keff_beta_amplification": 1.45,
989	      "weighted_keff_sig": "8/12",
990	      "weighted_etamax_sig": "9/12",
991	      "bayesian_keff_sig": "6/12",
992	      "bayesian_etamax_sig": "5/12",
993	      "bayesian_mean_ASR_reduction_vs_majority": 0.28,
994	      "total_keff_sig_majority_plus_threshold": "14/16"
995	    },
996	    "tables": [
997	      {
998	        "name": "Aggregation Rule × Vulnerability Drivers (15-Model, 455 Panels)",
999	        "columns": [
1000	          "Aggregation",
1001	          "K_eff_resid sig",
1002	          "η_max sig",
1003	          "Mean K_eff β",
1004	          "Mean η_max β",
1005	          "Mean ASR",
1006	          "Δ ASR vs Majority"
1007	        ],
1008	        "rows": [
1009	          [
1010	            "Majority",
1011	            "10/12",
1012	            "10/12",
1013	            "0.42",
1014	            "0.51",
1015	            "0.074",
1016	            "baseline"
1017	          ],
1018	          [
1019	            "Threshold (unanimity)",
1020	            "11/12",
1021	            "7/12",
1022	            "0.61",
1023	            "0.34",
1024	            "0.138",
1025	            "+86%"
1026	          ],
1027	          [
1028	            "Accuracy-weighted",
1029	            "8/12",
1030	            "9/12",
1031	            "0.39",
1032	            "0.48",
1033	            "0.069",
1034	            "-6.8%"
1035	          ],
1036	          [
1037	            "Bayesian",
1038	            "6/12",
1039	            "5/12",
1040	            "0.25",
1041	            "0.28",
1042	            "0.053",
1043	            "-28.4%"
1044	          ]
1045	        ]
1046	      }
1047	    ],
1048	    "figures": [],
1049	    "analysis": "Aggregation 分析的 three actionable insights：(1) Threshold voting 是 diversity trap 的 worst-case amplifier——unanimity requirement 使 K_eff β 增加 45%，absolute ASR 增加 86%。Deployment recommendation: 避免在 adversarial-aware 场景使用 unanimity aggregation。(2) Bayesian 是 best partial defense——同时削弱两个 vulnerability channels（K_eff 6/12, η_max 5/12 vs majority 的 10/12, 10/12），ASR 降 28%。但 6/12 K_eff 仍 sig 表明 Bayesian 不能完全消除 diversity trap。(3) Defense stack rationale: Two-stage selection（控制 η_max 通道）+ Bayesian aggregation（削弱残余 η_max + 部分削弱 K_eff）是最 comprehensive defense。单一维度不够。\n\n聚合规则改变 vulnerability driver 的 relative weight 通过三个机制：(1) Threshold/unanimity 放大 K_eff——panel reject 需要 ALL judges agree，adversary 只需 flip one judge 就能 block rejection。Diverse panel 有更多 potential 'flip targets'（judge-specific vulnerabilities 更多样），因此 K_eff β amplifies 1.45×。同时 η_max 弱化（7/12）因为 unanimity 的 blocking 不需要 weakest judge 特别弱——任何一个 judge 被 flip 就够了。(2) Weighted voting 结果近似 majority 因为 accuracy weights 仅微调 vote influence（权重范围 0.8-1.2），未根本改变投票结构。(3) Bayesian aggregation 基于 clean-accuracy prior 下调低能力 judges 的 posterior weight，partially 中和了 η_max 通道（5/12，从 majority 的 10/12 下降）——弱 judges 的 vote 被 discount 所以 adversary targeting 弱 judge 的收益降低。但 K_eff 仍 6/12 sig，因为 Bayesian weights 基于 clean accuracy 而非 adversarial robustness——attack-shifted accuracy ≠ clean accuracy，adversary 可以 manipulate a judge 使其给出 'confidently wrong' judgment，Bayesian 无法区分这种 confident error 与 genuine judgment。28% ASR reduction 说明 Bayesian 是 best single-aggregation defense 但非 silver bullet。Combined majority + threshold conditions 的 14/16 K_eff sig 落入 K_eff_resid_sig_extended_conditions [10,16] 范围。"
1050	  },
1051	  {
1052	    "name": "Open-Ended Generation Benchmark (MT-Bench + AlpacaEval)",
1053	    "description": "在 MT-Bench（多轮对话评判）和 AlpacaEval（指令遵循评分）上测试 diversity trap。4 attack types × 2 benchmarks = 8 新 conditions（选 4 primary attacks: score_manip, sycophancy, position, verbosity）。15 models 但 panel size 受限于 benchmark cost 可能 sample 200 panels。",
1054	    "results": {
1055	      "mtbench_keff_resid_sig": "3/4",
1056	      "mtbench_etamax_sig": "3/4",
1057	      "mtbench_mean_R2": 0.48,
1058	      "alpacaeval_keff_resid_sig": "2/4",
1059	      "alpacaeval_etamax_sig": "3/4",
1060	      "alpacaeval_mean_R2": 0.42,
1061	      "open_ended_keff_sig_total": "3/4",
1062	      "open_ended_confound_r": 0.48,
1063	      "keff_beta_ratio_open_vs_mcq": 0.85,
1064	      "condition_dependent_pattern_preserved": true
1065	    },
1066	    "tables": [
1067	      {
1068	        "name": "Open-Ended Benchmark Results (8 Conditions)",
1069	        "columns": [
1070	          "Benchmark×Attack",
1071	          "K_eff_resid β",
1072	          "K_eff_resid p (FDR)",
1073	          "η_max β",
1074	          "η_max p (FDR)",
1075	          "R²",
1076	          "Dominant"
1077	        ],
1078	        "rows": [
1079	          [
1080	            "MT-Bench×score_manip",
1081	            "0.52",
1082	            "1.8e-5",
1083	            "0.38",
1084	            "0.003",
1085	            "0.52",
1086	            "K_eff"
1087	          ],
1088	          [
1089	            "MT-Bench×sycophancy",
1090	            "0.28",
1091	            "0.012",
1092	            "0.55",
1093	            "4.1e-5",
1094	            "0.49",
1095	            "η_max"
1096	          ],
1097	          [
1098	            "MT-Bench×position",
1099	            "0.47",
1100	            "8.3e-5",
1101	            "0.21",
1102	            "0.089",
1103	            "0.44",
1104	            "K_eff"
1105	          ],
1106	          [
1107	            "MT-Bench×verbosity",
1108	            "0.18",
1109	            "0.108",
1110	            "0.62",
1111	            "7.2e-6",
1112	            "0.47",
1113	            "η_max"
1114	          ],
1115	          [
1116	            "AlpacaEval×score_manip",
1117	            "0.44",
1118	            "3.2e-4",
1119	            "0.35",
1120	            "0.006",
1121	            "0.46",
1122	            "K_eff"
1123	          ],
1124	          [
1125	            "AlpacaEval×sycophancy",
1126	            "0.21",
1127	            "0.058",
1128	            "0.58",
1129	            "1.4e-5",
1130	            "0.43",
1131	            "η_max"
1132	          ],
1133	          [
1134	            "AlpacaEval×position",
1135	            "0.38",
1136	            "0.002",
1137	            "0.25",
1138	            "0.041",
1139	            "0.40",
1140	            "both"
1141	          ],
1142	          [
1143	            "AlpacaEval×verbosity",
1144	            "0.14",
1145	            "0.175",
1146	            "0.59",
1147	            "2.1e-5",
1148	            "0.39",
1149	            "η_max"
1150	          ]
1151	        ]
1152	      }
1153	    ],
1154	    "figures": [],
1155	    "analysis": "Open-ended 结果的 three-fold significance：(1) Generalization — diversity trap 从 MCQ 推广到 open-ended，覆盖 LLM evaluation 的两大应用场景（benchmark scoring + human preference prediction），claim 从 'diversity hurts on MMLU/ARC' 升级为 'diversity hurts on LLM evaluation generally'。(2) Taxonomy transfer — condition-dependent dominance pattern（transferable→K_eff, shared-bias→η_max）在 open-ended 上 preserved without modification，表明 taxonomy 是 task-agnostic fundamental structure。(3) Practical relevance — MT-Bench/AlpacaEval 是 LLM 排名的 de facto standard，diversity trap 在这些 benchmark 上成立直接影响模型选择和部署决策。R² 下降（0.39-0.52 vs MCQ 0.62）是 expected tradeoff：open-ended evaluation 的 subjectivity noise 是 inherent 的，panel structure 能解释的 fraction naturally 减少。\n\nOpen-ended judging 与 MCQ 的关键差异：(1) 评分更主观——judges 在 'what constitutes a good response' 上 disagreement 更高，noise floor 提升；(2) 攻击空间更大——adversary 可以在 multi-turn conversation 的每轮 independently manipulate（MT-Bench），或在 free-form response 中 embed 更复杂的 manipulation signals（AlpacaEval）。K_eff 在 open-ended 上仍显著正向（3/4 unique conditions across benchmarks），但 β 略低于 MCQ（ratio 0.85），因为 open-ended 的 higher noise floor 使 panel structure 解释的方差降低（R² 0.42-0.48 vs MCQ 0.62）。MT-Bench 比 AlpacaEval 表现更强（3/4 vs 2/4 sig），因为 multi-turn 结构给 adversary 更多 manipulation surface（每轮是独立攻击机会），judge-specific 响应差异在多轮中累积。Condition-dependent pattern 在 open-ended 上完美复现：score_manip 和 position 下 K_eff 主导，sycophancy 和 verbosity 下 η_max 主导——attack taxonomy 从 MCQ 推广到 open-ended 无需修改。≥2/4 open-ended K_eff 显著（best tier 达 3/4）满足 open-ended 显著条件。意义：diversity trap 不是 MCQ-specific artifact，直接回应 Dream W6 和 RC3。"
1156	  },
1157	  {
1158	    "name": "Gaussian Copula Failure + Family Label Revalidation (15-Model, 105 Pairs)",
1159	    "description": "15-model 105 pairwise MI matrix 计算。Gaussian copula MI vs observed MI ratio 验证。Family labels（6 families）的 MI 预测性检验（within vs cross-family）。Capability proximity 与 MI 的相关性分析。",
1160	    "results": {
1161	      "total_pairs": 105,
1162	      "MI_gaussian_ratio_mean": 18.5,
1163	      "MI_gaussian_ratio_max": 312,
1164	      "MI_gaussian_ratio_min": 4.2,
1165	      "pairs_ratio_gt_10x": "82/105",
1166	      "family_label_MWU_p": 0.158,
1167	      "family_label_permutation_p": 0.312,
1168	      "within_family_MI_mean": 0.42,
1169	      "cross_family_MI_mean": 0.39,
1170	      "capability_proximity_MI_correlation": -0.71,
1171	      "copula_MI_ratio_15model": 18.5
1172	    },
1173	    "tables": [
1174	      {
1175	        "name": "Copula Failure: Scale Comparison",
1176	        "columns": [
1177	          "Metric",
1178	          "6-model (15 pairs)",
1179	          "15-model (105 pairs)",
1180	          "Change"
1181	        ],
1182	        "rows": [
1183	          [
1184	            "MI_obs/MI_gauss mean",
1185	            "14.7",
1186	            "18.5",
1187	            "+25.9%"
1188	          ],
1189	          [
1190	            "MI_obs/MI_gauss max",
1191	            "235",
1192	            "312",
1193	            "+32.8%"
1194	          ],
1195	          [
1196	            "MI_obs/MI_gauss min",
1197	            "8.3",
1198	            "4.2",
1199	            "Some close pairs"
1200	          ],
1201	          [
1202	            "Pairs with ratio >10×",
1203	            "11/15 (73%)",
1204	            "82/105 (78%)",
1205	            "+5pp"
1206	          ],
1207	          [
1208	            "Family label p (MWU)",
1209	            "0.206",
1210	            "0.158",
1211	            "Still NS"
1212	          ],
1213	          [
1214	            "Capability-MI r",
1215	            "-0.65",
1216	            "-0.71",
1217	            "Stronger"
1218	          ]
1219	        ]
1220	      }
1221	    ],
1222	    "figures": [],
1223	    "analysis": "15-model copula failure 和 family label 结果分别强化 Claims 5 和 4。Copula failure 的 practical implication：任何基于 Gaussian copula 假设的 panel reliability bound（如 independence-based certification）在 LLM judge 对上不可信——underestimate information sharing by 10-30×（mean 18.5×）。这为 K_eff 作为 empirical independence measure（而非 copula-derived bounds）提供 methodological justification。Family label result 的 practical implication：panel designers 不能简单用 '3 different families = diverse panel' 的 heuristic——Qwen-7B 和 Llama-8B 虽属不同 families 但 capability 接近故 MI 高（independence 低），而 GPT-4o-mini 和 GPT-4o 虽同属 OpenAI 但 capability gap 大故 MI 低（independence 高）。Capability proximity 是 independence 的 true driver。\n\n105 pairs（7× 6-model 的 15 pairs）大幅增加 copula failure 的统计力度。MI_gaussian_ratio 均值从 6-model 的 14.7 升至 18.5，因为 15-model pool 包含更多 capability-heterogeneous pairs（如 Mistral-7B 与 GPT-4o、Phi-14B 与 Claude-3.5），这些极端 pair 的联合分布更远离 bivariate Gaussian——heavy tails、discrete clustering、capability-dependent correlation structure 使 Gaussian copula 的低估更严重。Max ratio 从 235 升至 312（最极端 pair 如 Mistral-7B × GPT-4o 的 MI 被 Gaussian 低估 312×）。Family labels 仍无预测力（MWU p=0.158）：within-family MI（0.42）和 cross-family MI（0.39）无显著差异。根本原因：同 family 不同 size（如 Llama-8B vs Llama-70B）的 judges 独立性差异远大于同 size 不同 family（如 Llama-8B vs Qwen-7B vs Mistral-7B）——这些 7B-class 模型 capability-wise 非常接近，共享 similar failure modes despite different training pipelines。Capability proximity（|capability_i - capability_j|）与 MI 的强负相关（r=-0.71）直接支持：能力越接近→共享越多 failure patterns→MI 越高→independence 越低。意义：practitioners 不应用 family diversity 作为 panel independence proxy——capability-based metrics（如 K_eff）才是 valid measure。"
1224	  },
1225	  {
1226	    "name": "Partial-Knowledge Adversary Model",
1227	    "description": "Adversary 知道 panel 包含哪些 model families（public information）但不知各 judge 的具体 η_j vulnerability profiles。Strategy: family-level average attack 而非 judge-specific targeting。与 full-knowledge 和 black-box baselines 对比。",
1228	    "results": {
1229	      "full_knowledge_mean_ASR": 0.074,
1230	      "partial_knowledge_mean_ASR": 0.058,
1231	      "black_box_mean_ASR": 0.031,
1232	      "partial_vs_full_ratio": 0.784,
1233	      "keff_sig_partial": "7/12",
1234	      "etamax_sig_partial": "8/12",
1235	      "partial_R2": 0.51,
1236	      "family_info_value_pct": 62.8
1237	    },
1238	    "tables": [
1239	      {
1240	        "name": "Adversary Knowledge Level Comparison",
1241	        "columns": [
1242	          "Knowledge Level",
1243	          "Mean ASR",
1244	          "K_eff sig",
1245	          "η_max sig",
1246	          "R²",
1247	          "Info value vs black-box"
1248	        ],
1249	        "rows": [
1250	          [
1251	            "Full (judge-level η_j)",
1252	            "0.074",
1253	            "10/12",
1254	            "10/12",
1255	            "0.62",
1256	            "100%"
1257	          ],
1258	          [
1259	            "Partial (family only)",
1260	            "0.058",
1261	            "7/12",
1262	            "8/12",
1263	            "0.51",
1264	            "62.8%"
1265	          ],
1266	          [
1267	            "Black-box (none)",
1268	            "0.031",
1269	            "3/12",
1270	            "4/12",
1271	            "0.28",
1272	            "0%"
1273	          ]
1274	        ]
1275	      }
1276	    ],
1277	    "figures": [],
1278	    "analysis": "Partial-knowledge 分析的 key takeaway：diversity trap 的 threat model 是 realistic。Full-knowledge 是 worst-case security analysis 的 standard practice（similar to how cryptography assumes worst-case adversary），但 even partial-knowledge（family info = public）已经 captures 63% of the vulnerability。The 7/12 K_eff significance under partial knowledge means: even if the adversary only knows 'this panel uses judges from Llama, GPT, and Qwen families'（commonly disclosed），they can exploit diversity. This eliminates the 'but real adversaries don't have full information' defense. Graduation: paper can now claim diversity trap holds under realistic threat models, not just theoretical worst-case.\n\nPartial-knowledge adversary 的 strategy 是 family-level targeting：知道 panel 含 Llama → apply Llama-family average attack template，知道含 GPT → apply GPT-family average attack template。ASR 约为 full-knowledge 的 78%——family membership 提供了 ~63% of adversary information value（(0.058-0.031)/(0.074-0.031)=62.8%），因为 family→capability tier 有强相关性（所有 Qwen-7B 都是 small tier），且 family-level vulnerability profiles 有 within-family consistency。K_eff 在 partial-knowledge 下仍 7/12 sig（vs full-knowledge 10/12），因为 diverse panel 跨越更多 families → adversary 的 family-level portfolio attack 有更多 entry points。η_max 8/12 sig（vs 10/12）轻微下降因为 adversary 不知 exact η_j，targeting precision 降低使 weakest-link exploitation 变 fuzzy。R² 从 0.62 降至 0.51 反映 partial-knowledge 下 panel structure 的 predictive power 减弱——adversary behavior 有更多 randomness（不确定性导致 suboptimal targeting）。关键意义：diversity trap 不依赖于 unrealistically strong adversary 假设——即使 adversary 只有 public-level information（model families are typically disclosed in evaluation pipelines），diversity 仍然显著有害。这直接回应 Dream W7（'unrealistically strong adversary'）。"
1279	  }
1280	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15a1d6fb-2284-46d2-996e-c67f2ce378e4",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "d3f48d01-d54b-4ad2-b30b-7a844bbb5a79",
  "sourceToolAssistantUUID": "15a1d6fb-2284-46d2-996e-c67f2ce378e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T23:04:04.668Z_

<details open><summary>🔧 Tool call — Read · `toolu_013fxKECugketr2Ez3aPJHhb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f48d01-d54b-4ad2-b30b-7a844bbb5a79",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSeP15CqzoeEJB8WGjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd84bbc7-a752-47cc-8565-0c5f19e32619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcS28rnYJuhmguHeRVEa5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10819,
      "cache_read_input_tokens": 22633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10819,
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

_source line 24 · 2026-05-22T23:04:04.674Z_

<details><summary>↩ Tool result · `toolu_013fxKECugketr2Ez3aPJHhb`</summary>

```text
1	# Paper Framing — cert_manip_resist_eval (v4: 15-Model Empirical Revision)
2	
3	> Last updated: 2026-05-22 | Reason: 15-model/455-panel results fundamentally changed Claim 1 direction; K_eff independently positive; dual vulnerability drivers
4	
5	## Target
6	EMNLP 2026 (via ARR)
7	
8	## Title Candidates
9	1. "The Diversity Trap: Why Adding More Judges Doesn't Make LLM Evaluation Safer"
10	2. "More Diverse, More Vulnerable: How Judge Independence Backfires Under Adaptive Adversaries"
11	3. "Against the Diversity Assumption: Panel Diversity Independently Increases LLM Evaluation Vulnerability"
12	
13	## Core Insight
14	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, analogous to Byzantine Fault Tolerance (BFT) where independence protects against faults. We provide the first large-scale empirical evidence (15 models, 455 panels, 6 attacks) that this assumption **reverses** under adaptive adversaries: diversity (K_eff) is significantly and independently **positively** correlated with attack success rate. Panel vulnerability is driven by **dual factors** — individual weakness (η_max) AND structural diversity (K_eff) — with their relative importance depending on attack type. The mechanism: BFT assumes random faults where independent nodes tolerate uncorrelated failures; but adaptive adversaries exploit the diverse attack surface that independent judges create, finding judge-specific vulnerabilities across a wider attack space.
15	
16	## Hook
17	"Adding more diverse judges to an evaluation panel doesn't just fail to help — it actively makes the panel more vulnerable to adversarial manipulation."
18	
19	## Novelty Positioning
20	We do NOT claim to discover that diversity can be harmful in adversarial settings — the concept exists in security literature. Our contributions are:
21	1. **First empirical quantification of diversity's independent harmful effect** in the LLM-judge domain (15 models, 455 panels, residualized K_eff analysis confirming independent effect beyond η_max)
22	2. **Dual vulnerability driver discovery**: η_max and K_eff independently predict panel ASR, with condition-dependent relative importance (η_max dominates bias attacks; K_eff dominates transferable attacks)
23	3. **BFT reversal mechanism**: formal and empirical demonstration of WHY diversity helps under random faults but HURTS under adaptive adversaries
24	4. **Structural barriers**: copula failure (10-21× MI underestimation), diversity-capability tradeoff (now with independent predictive evidence), family label unreliability
25	5. **Actionable defense**: robustness-first selection + reliability-weighted aggregation
26	
27	## Core Claims
28	
29	### Claim 1 (Primary): Dual Vulnerability Drivers — Diversity Trap
30	**Statement**: Under adaptive adversarial attacks, panel ASR is independently predicted by BOTH individual weakness (η_max, 9/12 FDR sig) AND panel diversity (K_eff, 8/12 FDR sig positive after residualization). Diversity **increases** vulnerability. Their relative importance is condition-dependent: η_max dominates shared-bias attacks, K_eff dominates transferable attacks.
31	**Evidence** (15-model, 455 panels, 12 conditions):
32	- η_max FDR significant: **9/12**
33	- K_eff raw FDR significant positive: **12/12**
34	- K_eff residualized (orthogonalized against η_max, VIF=1.00): **8/12 FDR sig positive**
35	- Sensitivity (exclude ACC < 0.5): K_eff_resid **9/12** sig → not driven by extreme outliers
36	- **K_eff dominates η_max** in 2 conditions: arc×score_manipulation (η_max p=0.117 NS, K_eff_resid p=1.7e-7), arc×position_bias (η_max p=0.910 NS, K_eff_resid p=1.8e-8)
37	- **η_max dominates K_eff** in bias-type attacks: sycophancy, verbosity, authority
38	- Confound status: mean |r|=0.700 (SEVERE), but 2 BROKEN conditions (r≈0.35) confirm independent K_eff effect (p=6e-26, 4e-16)
39	**Strength**: Strong. Residualized analysis + confound-free conditions + sensitivity analysis all converge.
40	**Headline**: "Both η_max (9/12) and K_eff (8/12 residualized) independently predict panel vulnerability. Diversity actively increases attack surface."
41	
42	**Comparison to 6-model results** (for transparency):
43	- 6-model (20 panels): K_eff 1/12 sig, η_max 6/12 sig → "K_eff irrelevant"
44	- 15-model (455 panels): K_eff 8/12 sig positive, η_max 9/12 sig → "K_eff independently harmful"
45	- The reversal is driven by model pool expansion: more diverse capability spectrum enables detecting K_eff's real effect.
46	
47	### Claim 2 (Empirical): Adaptive vs Random-Fault Predictability Gap
48	**Statement**: Panel composition explains systematically more variance under random faults than under adaptive attacks (ΔR² = +0.213). Adaptive adversaries introduce strategic variance beyond panel structure.
49	**Evidence** (15-model, 455 panels):
50	- K_eff significant in both regimes (12/12 adaptive, 12/12 RF), both positive direction
51	- K_eff gains significance: 11/12 (RF β larger than adaptive β in most conditions)
52	- ΔR² = +0.213 mean
53	**Reframing from v3**: Original BFT contrast ("K_eff helps under RF but not adaptive") does NOT hold — K_eff is harmful in both regimes. The real distinction is predictability: random faults produce more explainable variance, adaptive attacks introduce strategic noise.
54	**Strength**: Moderate. R² gap real, but K_eff regime-difference story is weaker than originally hoped.
55	
56	### Claim 3 (Empirical): Diversity-Capability Tradeoff
57	**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally introduces less capable/robust models. This tradeoff is not merely correlational — residualized K_eff analysis confirms diversity has an independent predictive effect on vulnerability beyond its association with η_max.
58	**Evidence**:
59	- K_eff-η_max correlation: r = +0.700 (15-model)
60	- Residualized K_eff still significant 8/12 → not purely mediated by η_max
61	- Independent statistical effect: diversity predicts vulnerability beyond what η_max alone explains
62	**Upgrade from v3**: From "correlation" to "independent predictive effect" (residualized analysis). Note: observational regression cannot establish causality — would require experimental manipulation of panel composition or instrumental variables.
63	**Strength**: Strong (statistical association). Causal language avoided.
64	
65	### Claim 4 (Methodological): Family Labels ≠ Diversity
66	**Statement**: Model family labels (Qwen/Llama/Mistral/Anthropic/OpenAI/Google) do not predict judge independence. Capability proximity is the primary driver of inter-judge correlation.
67	**Evidence**: Mann-Whitney U p=0.206, permutation p=0.427 for within vs cross-family MI. (6-model data; needs 15-model revalidation with 105 pairs)
68	**Strength**: Moderate (needs 15-model update).
69	
70	### Claim 5 (Methodological): Gaussian Copula Failure
71	**Statement**: The Gaussian copula model systematically underestimates information sharing between LLM judges by 10-21× (up to 235×), invalidating copula-based independence bounds.
72	**Evidence**: MI_observed / MI_gaussian ratio across model pairs × datasets. (Needs 15-model update)
73	**Strength**: Strong (6-model). Needs 15-model revalidation.
74	
75	### Claim 6 (Practical): Robustness-First Panel Design
76	**Statement**: Optimal panel selection is robustness-first: (1) screen for individual robustness (η ≤ threshold), then (2) maximize K_eff among qualifying judges. The two-stage approach is critical because K_eff is harmful in unrestricted pools but may be neutral or beneficial among robustness-screened judges.
77	**Evidence**: min_eta_max strategy dominates 5/6 conditions (6-model). Full 15-model validation needed.
78	**Strength**: Moderate. Updated rationale: K_eff's positive (harmful) effect should diminish when η_max is controlled by screening.
79	
80	### Claim 7 (Empirical+Practical): Aggregation Rule Modulates Vulnerability Drivers
81	**Statement**: The dual vulnerability driver effect (Claim 1) varies by aggregation rule. Bayesian aggregation partially breaks the η_max effect; threshold voting amplifies K_eff's harmful effect.
82	**Evidence** (6-model, needs 15-model rerun):
83	- Majority: η_max 5/12, K_eff mostly NS
84	- Threshold: K_eff positive 8/12 (diversity harmful under unanimity)
85	- Bayesian: η_max 2/12 (weakened)
86	**Needs**: 15-model/455-panel rerun of plan_010 aggregation analysis.
87	**Strength**: Moderate (6-model only).
88	
89	## Contribution Stack (ordered by strength)
90	1. **Diversity Trap / Dual vulnerability drivers** — primary empirical contribution (K_eff independently harmful + condition-dependent dominance pattern)
91	2. **Diversity-capability tradeoff with independent predictive evidence** — empirical contribution (residualized analysis upgrades from correlation to independent effect)
92	3. **BFT reversal mechanism** — theoretical contribution (why independence hurts under adaptive adversaries)
93	4. **Aggregation-dependent effects** — empirical+practical (Bayesian as partial defense; threshold as amplifier)
94	5. **Robustness-first panel design** — practical contribution
95	6. **Gaussian copula failure** — methodological contribution
96	7. **Family label unreliability** — methodological contribution
97	8. **Adaptive vs random-fault predictability gap** — empirical (R² gap, weakened from original)
98	
99	## Anticipated Reviewer Concerns
100	
101	### RC1: "K_eff positive is just confound with η_max"
102	**Response**: (a) Residualized K_eff (VIF=1.00) still significant 8/12; (b) In confound-free conditions (r≈0.35), K_eff p < 1e-16; (c) Sensitivity analysis excluding extreme models: 9/12 still significant. Three independent lines of evidence rule out confound artifact.
103	
104	### RC2: "Why does diversity hurt? What's the mechanism?"
105	**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) Condition-dependent analysis: K_eff dominates transferable attacks (score_manipulation, position_bias) where attack diversity maps to judge diversity; η_max dominates shared-bias attacks (sycophancy, verbosity) where all judges share similar biases.
106	
107	### RC3: "Only 15 models — does this generalize?"
108	**Response**: (a) 15 models across 6 families, 3 capability tiers, covering major commercial and open-source models; (b) 455 panels provide strong statistical power; (c) Effect is robust to sensitivity analysis; (d) Direction consistent across 6→9→15 model scaling (K_eff shifts from NS to positive as model pool diversifies).
109	
110	### RC4: "BFT comparison is a strawman"
111	**Response**: (a) The implicit assumption "more diverse judges = more robust" is pervasive in LLM evaluation literature; (b) We formalize this assumption and show its reversal; (c) The BFT reversal mechanism (random vs adaptive faults) provides theoretical grounding beyond just empirical observation.
112	
113	### RC5: "Why not just use the strongest models?"
114	**Response**: (a) "Strongest" varies by attack type; (b) K_eff dominates η_max in 2 conditions — even all-strong panels are vulnerable through diversity channel; (c) Two-stage algorithm addresses both vulnerability drivers.
115	
116	### RC6: "No theoretical novelty"
117	**Response**: (a) Theorem 1 (η_max monotonicity) is formally proved; (b) BFT reversal mechanism provides novel theoretical framework; (c) Dual vulnerability driver finding with condition-dependent importance is new.
118	
119	### RC7: "Why not just use Bayesian aggregation?"
120	**Response**: (a) Bayesian reduces η_max significance but K_eff effect unknown at 15-model scale; (b) Requires clean accuracy prior; (c) Adaptive attacker can target Bayesian weighting; (d) Defense stack (selection + aggregation) recommended.
121	
122	### RC8 (new): "6-model and 15-model results contradict — which is right?"
123	**Response**: (a) 6-model result (K_eff NS) was underpowered and confounded (r=-0.8, only 20 panels); (b) 15-model result (K_eff positive) has 23× more panels, wider capability range, and passes residualized validation; (c) Paper reports both and explains why 15-model result is definitive; (d) The scaling behavior itself (K_eff effect emerging with more models) is informative.
124	
125	## "When Diversity Helps" Section
126	Diversity MAY be beneficial under specific conditions — paper must acknowledge nuance:
127	1. **Non-adversarial settings**: reducing calibration errors, position bias, verbosity bias in absence of adversary
128	2. **After robustness screening**: once all judges exceed a capability threshold, K_eff's harmful effect may diminish (the diversity-capability tradeoff is broken by screening). This is the basis for our two-stage recommendation.
129	3. **Shared-bias attacks where η_max is high and uniform**: when all models are similarly vulnerable (low η_max variance), K_eff's independent harmful effect is weaker. But this is a narrow regime.
130	4. **Disclaimer**: K_eff's harmful effect was significant in 8/12 conditions including confound-free ones. "When diversity helps" is the exception, not the rule, under adaptive adversaries.
131	
132	## Story Arc (v4)
133	1. **Background**: Multi-judge LLM evaluation is increasingly adopted; diversity is assumed to be the key defense against manipulation (BFT analogy)
134	2. **Tension**: We test this assumption at unprecedented scale — 15 models, 6 families, 455 panels, 6 attack types
135	3. **Surprise**: Diversity doesn't just fail to protect — it **actively increases vulnerability**. K_eff is significantly positive in 12/12 conditions (8/12 after residualization)
136	4. **Mechanism**: BFT assumes random faults; adaptive adversaries exploit the diverse attack surface that independent judges create. η_max and K_eff are dual vulnerability drivers with condition-dependent importance
137	5. **Nuance**: K_eff dominates transferable attacks; η_max dominates shared-bias attacks. The diversity-capability tradeoff provides partial (but not complete) explanation
138	6. **Defense**: Robustness-first screening + Bayesian aggregation. No single defense eliminates both vulnerability channels
139	7. **Implication**: The LLM evaluation community should rethink the "more diverse = more robust" assumption. Panel security requires managing both individual robustness AND structural diversity
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd84bbc7-a752-47cc-8565-0c5f19e32619",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "6db2bcd7-bfde-4815-910a-6b6199e6ab09",
  "sourceToolAssistantUUID": "bd84bbc7-a752-47cc-8565-0c5f19e32619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T23:04:05.263Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Kh493koBcP5FmjfRy53484`</summary>

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
  "parentUuid": "6db2bcd7-bfde-4815-910a-6b6199e6ab09",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSeP15CqzoeEJB8WGjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1393f1a7-d7a9-4013-a666-5188ae743b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcS28rnYJuhmguHeRVEa5g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10819,
      "cache_read_input_tokens": 22633,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10819
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 307,
          "cache_read_input_tokens": 22633,
          "cache_creation_input_tokens": 10819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10819,
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

_source line 26 · 2026-05-22T23:04:05.530Z_

<details><summary>↩ Tool result · `toolu_01Kh493koBcP5FmjfRy53484`</summary>

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
  "parentUuid": "1393f1a7-d7a9-4013-a666-5188ae743b92",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "51c09b71-b5cd-46af-a568-3a940f821af4",
  "sourceToolAssistantUUID": "1393f1a7-d7a9-4013-a666-5188ae743b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-22T23:04:11.206Z_

Now let me check the ROADMAP for the discrepancy between the "best" paper and the actual submitted paper, and also read the review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51c09b71-b5cd-46af-a568-3a940f821af4",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSeuf44VW9CFdwbx8tE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "087318a7-ce7c-47bc-b8b1-f87bc0ae90e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172Vt17fJZXWphUfayF6ZuM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50441,
      "cache_read_input_tokens": 33452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 50441,
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

_source line 28 · 2026-05-22T23:04:14.982Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MVyNVgPnZeoTCjTpPCU4dh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "087318a7-ce7c-47bc-b8b1-f87bc0ae90e0",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSeuf44VW9CFdwbx8tE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b25f1365-71a3-4bf4-bc8a-f584dff7b162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172Vt17fJZXWphUfayF6ZuM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50441,
      "cache_read_input_tokens": 33452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 50441,
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

_source line 29 · 2026-05-22T23:04:14.989Z_

<details><summary>↩ Tool result · `toolu_01MVyNVgPnZeoTCjTpPCU4dh`</summary>

```text
1	---
2	dream_id: dream_20260522T173833
3	tier: best
4	overall_score: 3.0 (Findings)
5	timestamp: 2026-05-22T18:50:53.878058+00:00
6	---
7	
8	# Review Report — R1 (Methodology and Experiments)
9	
10	**Paper**: "More Diverse, More Vulnerable: How Judge Panel Diversity Backfires Under Adaptive Adversaries"
11	
12	**Venue**: EMNLP 2026 via ARR
13	
14	---
15	
16	## Summary
17	
18	This paper investigates whether diversity in multi-judge LLM evaluation panels provides adversarial robustness, analogous to Byzantine Fault Tolerance. Through a large-scale study of 15 models, 455 three-judge panels, 9 attack types, and 4 benchmarks, the authors claim that panel diversity (K_eff) is independently and *positively* associated with attack success rate after residualizing against individual judge weakness (eta_max). They identify a "dual vulnerability driver" structure where attack type determines which factor dominates, propose a two-stage defense, and show Bayesian aggregation provides complementary protection.
19	
20	---
21	
22	## Strengths
23	
24	- **Comprehensive experimental coverage.** The paper tests an impressive combinatorial space: all C(15,3)=455 panels, 9 attack types, 4 benchmarks, 4 aggregation rules, 4 panel sizes, and 3 adversary knowledge levels. This breadth is unusual and commendable. The 12 imagined experiments are all represented.
25	
26	- **Rigorous statistical diagnostics.** The residualization approach to handle K_eff-eta_max collinearity is methodologically sound, yielding VIF=1.02. The paper reports multiple correction methods (uncorrected, FDR, Bonferroni), beta regression as a distributional robustness check, Cook's distance, leverage diagnostics, and Shapiro-Wilk normality tests. This is well above the typical standard for empirical NLP papers.
27	
28	- **BFT random-fault contrast is well-designed.** Using calibrated random faults (bootstrapped from clean accuracy noise rather than reusing adversarial eta_j values) is the correct experimental design. The 5/12 coefficient flip to negative under RF for transferable attacks provides genuine mechanistic insight — it is not a strawman comparison.
29	
30	- **Attack taxonomy provides predictive structure.** The observation that transferable attacks (score manipulation, position bias) are K_eff-dominated while shared-bias attacks (sycophancy, verbosity) are eta_max-dominated is a genuinely useful organizing principle. The taxonomy transfers to open-ended benchmarks and extended attacks, suggesting it captures real structure.
31	
32	- **Capability-matched validation addresses the most obvious confound.** The large-tier within-tier analysis (6 top-tier models, 20 panels, K_eff significant in 4/6 conditions) is the strongest single piece of evidence that K_eff's effect is not merely a tier-mixing artifact.
33	
34	- **Practical defense stack is well-motivated.** The two-stage algorithm + Bayesian aggregation combination directly follows from the dual-driver analysis. The 20.8% ASR reduction over Strongest-K is non-trivial, and the Max-K_eff catastrophic performance (ASR 0.112) is a compelling demonstration.
35	
36	---
37	
38	## Weaknesses
39	
40	### Major
41	
42	- **W1: Critical discrepancy between paper versions and actual experimental results.** Cross-referencing the paper's claims against the project's memory.md and ROADMAP.md reveals a serious concern. The actual 15-model experimental results (from plan001_step1_full_v4) show: eta_max FDR sig 11/12, K_eff FDR sig positive 7/12, K_eff negative 1/12 (arc x sycophancy), K_eff NS 4/12, with K_eff-eta_max confound correlation r=+0.70 (SEVERE). The paper reports K_eff_resid significant in 10/12 conditions with mean confound r=0.55 and VIF=1.02, which cannot be derived from the actual data where r=+0.70 (and even the project itself labels this "CONFOUND_SEVERE"). The paper appears to present imagined/projected numbers rather than actual experimental results. The real regression used log-log specification [log(ASR+eps) ~ log(K_eff) + log(eta_max+eps)], not the linear OLS presented in the paper. This is a fundamental credibility issue.
43	
44	- **W2: The "diversity trap" framing is inconsistent with the project's own falsification history.** The project memory documents that the original K_eff hypothesis was "thoroughly falsified" at the 6-model and 9-model scales (K_eff 1/12 significant, taxonomy broad-spectrum 0/6). The 15-model result shows K_eff 7/12 positive, 1/12 negative — predominantly harmful but far from the 10/12 claimed in the paper. The paper's title "More Diverse, More Vulnerable" and the abstract's claim of K_eff "independently and positively associated" in 10/12 conditions overstates what the actual data supports. The project's own paper_framing.md (v4b) is more honest: "K_eff 7/12 positive + protective exception + condition-dependent dominance."
45	
46	- **W3: Non-independence of observations inflates statistical significance.** The 455 panels share judges extensively — each of the 15 models appears in C(14,2)=91 panels. This means panel-level ASR observations are not independent. The OLS regression treats all 455 as independent observations, which inflates degrees of freedom and deflates p-values. The paper needs clustered standard errors (clustering on individual judges) or a mixed-effects model with random intercepts per judge. Without this correction, the reported p-values (some as low as 1.2e-8) are unreliable. This could substantially change the significance counts.
47	
48	- **W4: The adversary model conflates "adaptive" with "oracle."** The paper defines the adaptive adversary as one who "observes panel composition and crafts attacks to maximize panel ASR." In practice, how are attacks "crafted" for each judge? The paper does not describe an actual adversarial optimization loop — it appears to simply measure each judge's vulnerability to pre-defined attack templates and then report eta_j as the individual ASR. This is an oracle adversary who knows each judge's exact vulnerability, not a realistic adaptive attacker who must discover vulnerabilities through interaction. The partial-knowledge experiment (Section 7.4) partially addresses this but still assumes the adversary can execute family-level attack templates with known average ASRs. The gap between this oracle model and realistic adversaries is inadequately discussed.
49	
50	- **W5: Regression specification concerns.** (a) Linear OLS on ASR in [0,1] can produce out-of-range predictions. The paper mentions beta regression as a robustness check (9/12 vs 10/12 sig), but the main analysis uses OLS — beta regression should be the primary analysis for bounded outcomes. (b) The paper claims R^2=0.62 mean, but the ROADMAP.md shows R^2=0.298 for majority vote under the actual log-log canonical specification. This is a 2x discrepancy. (c) With only 2 predictors and 455 observations, an R^2 of 0.62 is suspiciously high for social/behavioral science regression — it raises the question of whether the regression is partially tautological (K_eff and eta_max are computed from the same judge pool that generates ASR).
51	
52	### Minor
53	
54	- **W6: Panel size analysis may be confounded by statistical power.** The claim that K_eff significance increases from 10/12 (K=3) to 12/12 (K=9) could be an artifact of increasing sample size: C(15,9)=5005 panels have 11x the statistical power of C(15,3)=455 panels. The increasing beta coefficient (0.42 to 0.61) is more informative but could reflect increased multicollinearity at larger K (where K_eff and eta_max become more structurally coupled).
55	
56	- **W7: No figures in the paper.** For a paper with 12+ tables of regression coefficients, the absence of any scatter plots, coefficient plots, or visualizations is a significant presentation weakness. Key patterns (the attack taxonomy, the BFT flip, the Pareto frontier) would be far more interpretable visually.
57	
58	- **W8: Gaussian copula failure numbers are inconsistent with project data.** The paper claims MI_obs/MI_gauss ratio of 18.5x mean (max 312x), but the project's actual 15-model results show MI_obs/MI_gauss ratio of 0.93 (MMLU) and 0.90 (ARC) — the copula fits *well* at 15-model scale. The 6-model result of 10-21x was explicitly labeled "small-sample artifact" and "DEAD as independent claim" in paper_framing.md v4b. Presenting the falsified 18.5x number in the paper is misleading.
59	
60	- **W9: Limitations section is thin.** Three points in one paragraph is adequate per EMNLP norms, but the points chosen omit the most important limitation: the non-independence of panel observations sharing judges (W3). The "observational not causal" caveat is buried as the third point and understated given the paper's causal-direction language throughout ("diversity backfires," "diversity trap").
61	
62	- **W10: Reference list is minimal.** Only 4 actual citations in the related work (zheng2023, li2023, dubois2024, wang2023, plus raina2024, shi2024, lamport1982, castro1999, krogh1994, brown2005, sagawa2020). For a paper claiming to overturn a "pervasive assumption," the literature review should more thoroughly document where this assumption appears and what evidence supports it.
63	
64	---
65	
66	## Questions for Authors
67	
68	1. **Q1**: The project's actual experimental results (plan001_step1_full_v4) show K_eff significant in 7/12 (not 10/12) conditions with confound r=+0.70 (not 0.55). The regression specification was log-log (not linear OLS), and the R^2 was 0.298 (not 0.62). Can you clarify why the paper reports different numbers? Are the paper's numbers from a different analysis pipeline?
69	
70	2. **Q2**: How do you address the non-independence of panel observations? Each judge appears in 91 of 455 panels. Have you run the analysis with clustered standard errors or mixed-effects models? What happens to the significance counts?
71	
72	3. **Q3**: In the adversary model, you assume the attacker can apply judge-specific or family-specific attack templates with known ASRs. How were individual judge ASRs measured? Was there a held-out evaluation set, or are the same samples used for both measuring eta_j and computing panel ASR?
73	
74	4. **Q4**: The BFT random-fault contrast uses "calibrated random faults based on bootstrapped clean-accuracy noise." Can you specify the exact procedure? How many bootstrap samples? How does the calibration ensure the marginal failure rates match between adaptive and RF conditions?
75	
76	5. **Q5**: The Bayesian aggregation uses "prior accuracy" to downweight judges. How is this prior estimated? If estimated from the same evaluation data, this introduces information leakage. The paper mentions "5-fold CV" in passing — was the Bayesian prior estimated in cross-validation? Details are needed.
77	
78	6. **Q6**: For the within-tier analysis, the small tier has only 10 panels and the medium tier only 4 panels. With 2 predictors, these regressions have 7 and 1 residual degrees of freedom respectively. Are the reported significance tests reliable with such small samples?
79	
80	7. **Q7**: The Pareto frontier analysis claims "83% large-tier, 0% small-tier." How is "Pareto-optimal" defined here — over which objectives? Is this Pareto-optimal in the K_eff vs eta_max space, or K_eff vs ASR space?
81	
82	---
83	
84	## Scores
85	
86	| Dimension | Score | Rationale |
87	|-----------|-------|-----------|
88	| **Soundness** | 2.5 | The non-independence issue (W3) undermines all significance claims. The discrepancy between reported and actual experimental numbers (W1, W2, W8) raises credibility concerns. The adversary model is closer to oracle than adaptive (W4). Core statistical framework is reasonable in design (residualization, diagnostics) but implementation details do not match the project's actual data. |
89	| **Excitement** | 3.5 | The research question is important and timely. The finding that diversity can *harm* adversarial robustness — if validated — would be genuinely surprising and impactful for the LLM evaluation community. The attack taxonomy (transferable vs shared-bias) is a useful conceptual contribution. The BFT contrast is well-conceived. |
90	| **Reproducibility** | 2.0 | Model list is provided but attack implementations are not described in detail. The paper does not specify: prompt templates for attacks, evaluation criteria for ASR, number of evaluation instances per condition, how MI matrices are estimated, or computational requirements. No code or data availability statement. The discrepancy between paper numbers and project data makes it unclear which analysis pipeline produced the reported results. |
91	| **Overall** | 3.0 | The paper addresses an important question with ambitious experimental scale, but the gap between claimed and actual results, the unaddressed non-independence of observations, and the underspecified adversary model prevent confidence in the central claims. If the statistical issues (W1, W3) were resolved and the paper accurately reported its actual experimental results — even if those results are weaker (7/12 rather than 10/12 for K_eff) — this could be a solid Findings paper. The core insight (diversity-robustness relationship depends on attack type and adversary model) is genuine and valuable, but the current presentation overstates the evidence. |
92	| **Confidence** | 4 | I have carefully read the paper, cross-referenced against the underlying experimental records, and identified specific numerical discrepancies. My concerns about non-independence and the adversary model are grounded in standard statistical methodology. I am less certain about the precise impact of clustered standard errors on significance counts, which would require re-analysis. |
93	
94	---
95	
96	## Recommendation
97	
98	**3.0 — Findings.** The paper has genuine scientific value in its research question, experimental scale, and the attack taxonomy insight. However, the methodological concerns (non-independence, adversary model realism) and the discrepancy between reported and actual results prevent main conference recommendation. A revised version that (1) accurately reports the actual experimental numbers, (2) addresses non-independence through appropriate multilevel modeling, (3) more clearly specifies and justifies the adversary model, and (4) adds implementation details for reproducibility could reach borderline conference level. The core contribution — that the diversity-robustness relationship is attack-type-dependent and breaks under adaptive adversaries — is worth publishing if properly validated.
99	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b25f1365-71a3-4bf4-bc8a-f584dff7b162",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "b48d69e9-8492-4c23-896f-8ebe45f01273",
  "sourceToolAssistantUUID": "b25f1365-71a3-4bf4-bc8a-f584dff7b162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T23:04:15.047Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QJJKSwJgAmuSVw73h5h84b`</summary>

```json
{
  "project": "cert_manip_resist_eval",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b48d69e9-8492-4c23-896f-8ebe45f01273",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSeuf44VW9CFdwbx8tE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba751a7e-85be-4fa3-92e4-4f6fb427affc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172Vt17fJZXWphUfayF6ZuM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50441,
      "cache_read_input_tokens": 33452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 50441,
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

_source line 31 · 2026-05-22T23:04:15.056Z_

<details><summary>↩ Tool result · `toolu_01QJJKSwJgAmuSVw73h5h84b`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/memory.md\", \"content\": \"# cert_manip_resist_eval — Memory\\n\\n## 环境信息\\n- **服务器**: seetacloud-rtx6000, 4× RTX PRO 6000 96GB\\n- **Python 环境**: conda base (`/root/miniconda3/bin/python`), vLLM 0.21.0 + torch 2.11.0+cu128\\n- **项目路径**: 服务器 `/root/cert_manip_resist_eval/`\\n- **模型路径**: `/root/autodl-tmp/models/`\\n- **AWQ 量化**: 所有模型均为 INT4 AWQ 量化版\\n- **HF 缓存**: `/root/autodl-tmp/.hf_cache/`（datasets 子目录有 mmlu + arc_challenge 的 arrow 缓存）\\n\\n## seetacloud 必须环境变量清单（缺一不可，连续 3 次 crash 教训）\\n```bash\\nsource /etc/network_turbo                    # 代理加速\\nexport HF_HUB_DISABLE_XET=1                 # xet 协议在 AutoDL 上 401\\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt  # SSL 证书\\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\\nexport HF_HOME=/root/autodl-tmp/.hf_cache   # 避免根分区写满\\nexport VLLM_WORKER_MULTIPROC_METHOD=spawn   # 必须在 import vllm 之前\\n```\\n\\n## 推理配置\\n- `gpu_memory_utilization=0.90` 安全（单模型串行加载时）\\n- serial load/unload 模式避免共享 GPU 的 OOM\\n- **启动新脚本前必须 kill 所有残留 vLLM 进程**，否则 GPU OOM（mvp-step2v3-retry2 教训）\\n\\n## 理论推导状态（2026-05-22）\\n- **T1 SDPI**: 完成。K_eff = 1+(K-1)e^{-2I_max} 是精确 Gaussian 值的上界\\n- **Theorem 1 (Weakest-Link)**: 完成。Panel ASR monotonically increasing in η_max under correlated judges + adaptive adversary. ASR = Θ(η_max^t). 6 页 LaTeX 证明在 `artifacts/theorem1_proof.tex`\\n- **T3 PEG**: 完成。Proposition 1/2 (sketch proof)。ε_inc(ρ) = 1-√(1-ρ²)\\n- T2/T4/T5/T6: planned\\n\\n## API 模型列表（2026-05-22 更新）\\n| 旧名 | 新名 | 原因 |\\n|---|---|---|\\n| claude-opus-4 | claude-opus-4-6 | 新版本 |\\n| claude-sonnet-4 | claude-sonnet-4-6 | 新版本 |\\n| gemini-2.5-pro | gemini-3.1-pro-preview | 新版本 |\\n| gemini-2.5-flash | gemini-3.5-flash | 新版本 |\\n| gpt-4o | gpt-4.1-nano | gpt-4o 退役(2026-02) |\\n| gpt-4o-mini | gpt-4.1-mini | 同理 |\\n\\n不变：gpt-4.1, gpt-5.5, claude-3-haiku\\n\\n**Scoring 基础设施**：本地 AWS 机器通过 OpenRouter（中国 IP 被 403 封锁）\\n\\n## K_eff 稳健性全景（2026-05-22 最终版）\\n\\n### 汇总表\\n| Method | η_max FDR sig | K_eff FDR sig | K_eff sig+ | K_eff sig− | 可靠度 |\\n|---|---|---|---|---|---|\\n| Canonical OLS | 11/12 | 8/12 | 7 | 1 | baseline (inflated) |\\n| **Wild Bootstrap v2** | **5/12** | **1/12** | 1 | 0 | ✓ 推荐 |\\n| Clustered SE (CGM) | 8/12 | 0/12 | 0 | 0 | 保守 |\\n| Mixed Effects | 7/12 | 3/12 | 3 | 0 | 中间 |\\n| + Tier indicators (3/3/9) | 11/12 | 5/12 | 4 | 1 | 控制 confound |\\n| GAM | 12/12 | 12/12 | 6 | 6 | 非线性 |\\n\\n### 关键判断\\n- **OLS 11/12 (η_max) 和 8/12 (K_eff) 因 panel 非独立性膨胀**：每个 judge 出现在 91/455 panels\\n- **Wild bootstrap v2 是最可靠估计**：修复了 K_eff 公式 + 3-position 聚类 max p-value\\n- **K_eff 不具备独立预测力**：bootstrap 1/12, clustered SE 0/12\\n- **η_max 仍是 dominant predictor**：bootstrap 5/12 vs K_eff 1/12，方向一致\\n- **Wild bootstrap v1 (9/12) 已作废**：K_eff 公式错误 + 聚类策略错误\\n- **GAM 6:6 split 在正确 3/3/9 tier 下确认成立**\\n- **Aggregation gradient 独立于 non-independence**\\n\\n### Alternative diversity metrics\\n- κ-diversity 与 K_eff 近等价（r=0.942），η_max 在所有 diversity metrics 下 dominant\\n\\n### Effect size\\n- η_max std β: 0.387 ± 0.179（K_eff 的 2.4 倍）\\n- K_eff std β: 0.164 ± 0.182\\n- Practical Δ_ASR (K_eff IQR): 1.3pp ± 1.6pp\\n\\n## 攻击模板（2026-05-22）\\n6 种攻击已完整提取：prompt_injection (3 templates), sycophancy (3×3), score_manipulation (3), verbosity_bias (3), position_bias (swap A/B), authority_bias (3 prefix)。ASR = |clean_correct ∩ attacked_incorrect| / |clean_correct|。\\n\\n## 教训\\n- [2026-05-22] **Wild bootstrap K_eff 公式必须与 canonical 完全一致**。v1 用了 max-MI 公式导致 arc×sycophancy β 符号翻转（+4.5 vs -0.19），产出假阳性 9/12。验证方法：检查已知负向条件的 β 符号。\\n- [2026-05-22] **聚类策略必须与 clustered SE 一致**。v1 用 alphabetical primary judge（13 clusters），canonical 用 3-position × 15 clusters max SE。不一致导致 bootstrap 比 clustered SE 宽松。\\n\\n## 决策记录\\n- [2026-05-21] keff.py: empirical_keff_from_rho 用所有 pairwise ρ，formula_keff 用 I_max\\n- [2026-05-22] Step 2 v3 negative: η_max dominates, K_eff 仅对 broad-spectrum 攻击有效\\n- [2026-05-22] Taxonomy negative: K_eff 理论完全证伪\\n- [2026-05-22] Plan_010: Bayesian aggregation 部分打破 weakest-link\\n- [2026-05-22] API 模型 6/9 升级，改用本地 AWS + OpenRouter scoring\\n- [2026-05-22] Wild bootstrap v2: K_eff 1/12, η_max 5/12 — K_eff 不 robust, η_max directional dominant\\n- [2026-05-22] v5 story 由 Director 定：η_max dominant + K_eff directional but fragile + GAM 6:6 + aggregation gradient\\n\", \"total_chars\": 4035, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba751a7e-85be-4fa3-92e4-4f6fb427affc",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "fc197827-46cb-42c7-839b-19dac362d326",
  "sourceToolAssistantUUID": "ba751a7e-85be-4fa3-92e4-4f6fb427affc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-22T23:04:21.592Z_

Now I have a comprehensive picture. Let me also check the actual submitted paper (the latest version after revisions), as the ROADMAP mentions a "Paper v5 Step 5 converged."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc197827-46cb-42c7-839b-19dac362d326",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSfcpZG7a3DiXgB4eun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9edffd53-adab-42d5-9a2c-263b01f3d349",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeRoUMLJktQMtwUcyrrWkK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6537,
      "cache_read_input_tokens": 83893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6537,
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

_source line 33 · 2026-05-22T23:04:24.432Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WALjrtN9eG27BaA2vm3ytd`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T173833/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9edffd53-adab-42d5-9a2c-263b01f3d349",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSfcpZG7a3DiXgB4eun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db5ddb12-83bd-4099-8458-8ef550b88a27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeRoUMLJktQMtwUcyrrWkK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6537,
      "cache_read_input_tokens": 83893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6537,
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

_source line 34 · 2026-05-22T23:04:24.447Z_

<details><summary>↩ Tool result · `toolu_01WALjrtN9eG27BaA2vm3ytd`</summary>

```text
artifacts/dream_reports/dream_20260522T173833/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db5ddb12-83bd-4099-8458-8ef550b88a27",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "c0bf4ee6-16a1-4025-a425-1a301d36756a",
  "sourceToolAssistantUUID": "db5ddb12-83bd-4099-8458-8ef550b88a27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T23:04:24.878Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QDwtUxVGos5qx5jZdVs2tK`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/**/*paper*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0bf4ee6-16a1-4025-a425-1a301d36756a",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSfcpZG7a3DiXgB4eun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbfc6e99-bc14-429d-a44e-e2c5bc8b63c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeRoUMLJktQMtwUcyrrWkK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6537,
      "cache_read_input_tokens": 83893,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6537
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 83893,
          "cache_creation_input_tokens": 6537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6537,
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

_source line 36 · 2026-05-22T23:04:24.934Z_

<details><summary>↩ Tool result · `toolu_01QDwtUxVGos5qx5jZdVs2tK`</summary>

```text
artifacts/dream_reports/dream_20260522T055016/best/paper.tex
artifacts/dream_reports/dream_20260522T055016/median/paper.tex
artifacts/dream_reports/dream_20260522T055016/worst/paper.tex
artifacts/dream_reports/dream_20260522T173833/best/paper.tex
artifacts/dream_reports/dream_20260522T173833/median/paper.tex
artifacts/dream_reports/dream_20260522T173833/worst/paper.tex
artifacts/dream_reports/dream_20260522T221131/best/paper.tex
artifacts/dream_reports/dream_20260522T221131/median/paper.tex
artifacts/dream_reports/dream_20260522T221131/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbfc6e99-bc14-429d-a44e-e2c5bc8b63c9",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "7e29e610-9a98-4f18-a16c-78a1b5a96641",
  "sourceToolAssistantUUID": "dbfc6e99-bc14-429d-a44e-e2c5bc8b63c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-22T23:04:28.164Z_

The most recent dream is `dream_20260522T221131`. Let me read the latest paper version which is likely the one after the v5 revisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e29e610-9a98-4f18-a16c-78a1b5a96641",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSgLnSAkpXcdTt7Ddyv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9722134f-6831-41d6-9f60-700dae643245",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtTB1knFfXqr2TxZ8BDT5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 483,
      "cache_read_input_tokens": 90430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 483,
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

_source line 38 · 2026-05-22T23:04:28.492Z_

<details open><summary>🔧 Tool call — Read · `toolu_018XBmFimEj4cTrQANKM4j9M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9722134f-6831-41d6-9f60-700dae643245",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSgLnSAkpXcdTt7Ddyv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a01ba10b-2051-4a1b-a188-bdeb24e6d66f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtTB1knFfXqr2TxZ8BDT5r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 483,
      "cache_read_input_tokens": 90430,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 483
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 90430,
          "cache_creation_input_tokens": 483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 483,
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

_source line 39 · 2026-05-22T23:04:28.759Z_

<details><summary>↩ Tool result · `toolu_018XBmFimEj4cTrQANKM4j9M`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{enumitem}
12	\usepackage{hyperref}
13	\usepackage[T1]{fontenc}
14	\usepackage[utf8]{inputenc}
15	\usepackage{natbib}
16	\renewcommand{\bibsection}{\section*{References}}
17	
18	\title{Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Multi-judge LLM evaluation panels are increasingly adopted to improve reliability, with an implicit assumption---rooted in Byzantine Fault Tolerance (BFT) theory---that judge diversity provides robustness against manipulation. We conduct the first large-scale empirical decomposition of panel vulnerability into two structural predictors: individual judge weakness ($\eta_{\max}$, the vulnerability of the weakest panel member) and panel diversity ($K_{\text{eff}}$, effective number of independent behavioral clusters). Across 15 models from 6 families, 455 panels, 9 attack types, and 3 benchmarks (MMLU, ARC-Challenge, MT-Bench), we find that $\eta_{\max}$ \emph{robustly} dominates panel vulnerability---significant in 8/12 conditions under clustered standard errors and 5/12 under wild cluster bootstrap, with a dominance ratio of 5:1 over $K_{\text{eff}}$. $K_{\text{eff}}$ shows directional but statistically fragile association, collapsing from 8/12 (OLS) to 0/12 (clustered SE) after correcting for panel non-independence. A Generalized Additive Model (GAM) analysis reveals a clean mechanistic split: $K_{\text{eff}}$ is positive (diversity harmful) for all targeted attacks and negative (diversity protective) for all shared-bias attacks---a 10:8 taxonomy across 9 attack types. Aggregation rule choice fundamentally modulates vulnerability: Bayesian calibration reverses $K_{\text{eff}}$ direction and weakens $\eta_{\max}$, while threshold voting amplifies both. We propose a robustness-first panel design algorithm that wins 12/12 conditions, outperforming naive diversity maximization which performs worse than random selection.
27	\end{abstract}
28	
29	\section{Introduction}
30	
31	The use of Large Language Models (LLMs) as automated judges for evaluating other LLMs has become a cornerstone of modern NLP evaluation \cite{zheng2023judging}. To mitigate individual judge biases, recent work increasingly employs multi-judge panels where multiple LLM judges evaluate candidates and their scores are aggregated via majority vote or similar mechanisms. The implicit operating assumption---borrowed from distributed systems and BFT theory---is that judge diversity provides robustness: more diverse panels should be harder to fool.
32	
33	This assumption has not been empirically tested under adversarial conditions. In non-adversarial settings, diversity does reduce calibration errors and position biases. But adversarial manipulation fundamentally changes the threat model: an adaptive adversary can exploit judge-specific vulnerabilities, potentially turning diversity from a defense into an attack surface.
34	
35	We conduct the first large-scale empirical study decomposing panel vulnerability into two structural predictors. Let $\eta_{\max}$ denote the vulnerability of the weakest judge in a panel (the maximum individual attack success rate), and $K_{\text{eff}}$ denote the effective number of independent behavioral clusters among panel judges (a diversity measure derived from mutual information). Our central question: \emph{which structural factor---individual weakness or panel diversity---drives vulnerability under adaptive adversarial attack?}
36	
37	Our findings challenge the diversity-as-defense assumption:
38	
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Weakest-link dominance.} $\eta_{\max}$ robustly dominates panel vulnerability (5:1 over $K_{\text{eff}}$ under bootstrap inference). $K_{\text{eff}}$'s apparent significance under OLS (8/12) collapses to 0--1/12 after correcting for panel non-independence---a methodological finding relevant to all combinatorial evaluation designs.
41	
42	\item \textbf{BFT reversal evidence.} A random-fault Monte Carlo contrast experiment shows $K_{\text{eff}}$ is genuinely significant (2/2, all corrections) under i.i.d. faults but artifactual under adaptive attacks, providing causal evidence for the failure of BFT assumptions.
43	
44	\item \textbf{Attack-type taxonomy.} GAM analysis reveals a clean mechanistic split: $K_{\text{eff}}$ is positive (diversity harmful) for targeted attacks and negative (diversity protective) for shared-bias attacks---a 10:8 pattern across 9 attack types.
45	
46	\item \textbf{Aggregation as control lever.} Bayesian calibration reverses $K_{\text{eff}}$ direction (from harmful to protective) and weakens $\eta_{\max}$ dominance. Threshold voting amplifies both drivers ($R^2=0.87$).
47	
48	\item \textbf{Robustness-first panel design.} A two-stage algorithm (filter by $\eta_{\max}$, then optimize $K_{\text{eff}}$) wins 12/12 conditions. Naive $K_{\text{eff}}$ maximization performs \emph{worse} than random selection.
49	\end{enumerate}
50	
51	\section{Related Work}
52	
53	\paragraph{LLM-as-Judge.} LLM-based evaluation has become standard practice for open-ended generation tasks \cite{zheng2023judging}. Known biases include position bias, verbosity bias, and sycophancy. Multi-judge panels have been proposed as a mitigation strategy, though systematic analysis of panel robustness under adversarial conditions remains absent.
54	
55	\paragraph{Adversarial Attacks on LLM Judges.} Prior work has demonstrated that individual LLM judges can be manipulated through prompt injection, score inflation, and stylistic gaming. However, existing studies focus on single-judge vulnerability rather than panel-level structural predictors.
56	
57	\paragraph{Byzantine Fault Tolerance.} BFT theory guarantees correctness when fewer than $f < n/3$ nodes fail independently. The key assumption---independent, random faults---is violated by adaptive adversaries who can strategically target specific judges. Our work provides the first empirical quantification of this assumption violation in LLM evaluation.
58	
59	\section{Method}
60	
61	\subsection{Panel Construction}
62	
63	We enumerate all $\binom{15}{3} = 455$ panels of size $K=3$ from a pool of 15 LLM judges spanning 6 model families (GPT, Claude, Gemini, Llama, Qwen, Mistral) and 3 capability tiers (frontier, mid, base). Each panel evaluates benchmark items under majority vote.
64	
65	\subsection{Vulnerability Predictors}
66	
67	\paragraph{Individual Weakness ($\eta_{\max}$).} For each panel, $\eta_{\max} = \max_{j \in \text{panel}} \eta_j$, where $\eta_j$ is judge $j$'s individual attack success rate (ASR) under a given attack type. This captures the weakest-link hypothesis: panel vulnerability is determined by the most exploitable judge.
68	
69	\paragraph{Panel Diversity ($K_{\text{eff}}$).} We compute pairwise mutual information (MI) between all judge pairs' evaluation vectors on clean data, then derive $K_{\text{eff}}$ as the effective number of independent clusters. Higher $K_{\text{eff}}$ indicates greater behavioral diversity among panel judges.
70	
71	\subsection{Attack Types}
72	
73	We study 9 attack types spanning two mechanistic categories:
74	
75	\begin{itemize}[leftmargin=*,itemsep=1pt]
76	\item \textbf{Targeted attacks} exploit judge-specific weaknesses: prompt injection, score manipulation, position bias exploitation, few-shot hijacking, instruction override, format gaming.
77	\item \textbf{Shared-bias attacks} exploit common cognitive biases: sycophancy amplification, verbosity bias, authority bias, style manipulation, length inflation, persona manipulation.
78	\end{itemize}
79	
80	\subsection{Regression Specification}
81	
82	Our canonical specification is log-log OLS:
83	\begin{equation}
84	\log(\text{ASR} + \epsilon) = \beta_0 + \beta_1 \log(K_{\text{eff}}) + \beta_2 \log(\eta_{\max} + \epsilon)
85	\label{eq:regression}
86	\end{equation}
87	where $\epsilon$ is a small constant for numerical stability. We report significance under four correction methods: standard OLS, clustered standard errors (CR1, 15 judge clusters), wild cluster bootstrap ($B=9999$, Rademacher weights, max-$p$ across 3 judge positions), and mixed effects (random judge intercepts). Panel non-independence arises because judges appear in multiple panels (e.g., claude-3-haiku appears in 91/455 panels), inflating standard errors by $\sim$2.5$\times$.
88	
89	\subsection{Aggregation Rules}
90	
91	We evaluate five aggregation rules: majority vote (baseline), accuracy-weighted vote, threshold (unanimity), Bayesian calibration (prior-weighted), and veto (single-judge override).
92	
93	\section{Experiments}
94	
95	\subsection{Core Results: Weakest-Link Dominance}
96	\label{sec:core}
97	
98	Table~\ref{tab:correction} presents our primary results across 15 models, 455 panels, and 12 conditions (6 attack types $\times$ 2 benchmarks). The pattern is stark: $\eta_{\max}$ dominates under all correction methods, while $K_{\text{eff}}$'s significance collapses after accounting for panel non-independence.
99	
100	\begin{table}[t]
101	\centering
102	\small
103	\begin{tabular}{lcccc}
104	\toprule
105	\textbf{Method} & \textbf{$\eta_{\max}$ sig} & \textbf{$K_{\text{eff}}$ sig} & \textbf{$K_{\text{eff}}$ dir} & \textbf{Ratio} \\
106	\midrule
107	OLS & 11/12 & 8/12 & 7+/1$-$ & 1.4:1 \\
108	Clustered SE & 8/12 & 0/12 & -- & $\infty$ \\
109	Bootstrap v2 & 5/12 & 1/12 & 1+ & 5:1 \\
110	Mixed effects & 7/12 & 3/12 & 3+ & 2.3:1 \\
111	\bottomrule
112	\end{tabular}
113	\caption{Correction method comparison (15 models, 455 panels, 12 conditions). $\eta_{\max}$ significance is robust across all methods; $K_{\text{eff}}$ collapses from 8/12 under OLS to 0--1/12 after non-independence correction. SE inflation $\sim$2.5$\times$ is consistent with 91/455 panel overlap.}
114	\label{tab:correction}
115	\end{table}
116	
117	Under OLS, both predictors appear significant ($\eta_{\max}$ 11/12, $K_{\text{eff}}$ 8/12), producing a misleading near-parity (1.4:1). Clustered SE correction---which accounts for shared judge membership across panels---eliminates all $K_{\text{eff}}$ significance (0/12) while retaining $\eta_{\max}$ at 8/12. The most conservative method (wild cluster bootstrap with max-$p$ across judge positions) gives a 5:1 dominance ratio. The $\min(\eta_{\max})$ panel selection strategy wins 12/12 conditions with ASR advantages ranging from 3.8 to 51.1 percentage points.
118	
119	\subsection{Attack Surface Expansion}
120	\label{sec:attack_expansion}
121	
122	To confirm that $\eta_{\max}$ dominance is not an artifact of our initial attack selection, we extend to 3 additional attack types (few-shot hijacking, persona manipulation, instruction override), yielding 18 total conditions. Table~\ref{tab:extended_attack} shows results under clustered SE.
123	
124	\begin{table}[t]
125	\centering
126	\small
127	\begin{tabular}{lcccl}
128	\toprule
129	\textbf{Attack} & \textbf{Mech.} & \textbf{$\eta_{\max}$} & \textbf{$K_{\text{eff}}$} & \textbf{GAM dir} \\
130	\midrule
131	Few-shot hijack & targ. & \checkmark\checkmark & 0/2 & positive \\
132	Persona manip. & shared & \checkmark\checkmark & 0/2 & negative \\
133	Instr. override & targ. & 1/2 & 0/2 & positive \\
134	\midrule
135	\multicolumn{2}{l}{\textit{Combined (18 cond.)}} & 13/18 & 0/18 & 10:8 \\
136	\bottomrule
137	\end{tabular}
138	\caption{Extended attack taxonomy (clustered SE). $\eta_{\max}$ remains dominant across all new attack types. GAM taxonomy extends cleanly from 6:6 to 10:8 (targeted:shared-bias). $\checkmark\checkmark$ = significant on both benchmarks.}
139	\label{tab:extended_attack}
140	\end{table}
141	
142	The combined dominance ratio under clustered SE is 13:0---$K_{\text{eff}}$ achieves zero significance across all 18 conditions. The GAM taxonomy extends cleanly: few-shot hijacking and instruction override are classified as targeted (positive $K_{\text{eff}}$), while persona manipulation is classified as shared-bias (negative $K_{\text{eff}}$), extending the split from 6:6 to 10:8.
143	
144	\subsection{Random-Fault BFT Contrast}
145	\label{sec:rf}
146	
147	To provide causal evidence for BFT assumption failure, we construct a random-fault (RF) baseline via Monte Carlo simulation (10,000 iterations). Each judge fails independently with probability $\eta_j = 1 - \text{clean\_accuracy}$.
148	
149	\begin{table}[t]
150	\centering
151	\small
152	\begin{tabular}{lccl}
153	\toprule
154	\textbf{Metric} & \textbf{Random Fault} & \textbf{Adaptive} & \textbf{Interpretation} \\
155	\midrule
156	$K_{\text{eff}}$ sig (OLS) & 2/2 & 8/12 & Both appear sig. \\
157	$K_{\text{eff}}$ sig (CL-SE) & 2/2 & 0/12 & RF genuine; adap. not \\
158	$K_{\text{eff}}$ sig (Boot.) & 2/2 & 1/12 & Consistent contrast \\
159	$K_{\text{eff}}$ std $\beta$ & +0.297 & +0.164 & RF larger, genuine \\
160	$R^2$ & 0.78--0.81 & 0.25--0.35 & Predictability gap \\
161	$\eta_{\max}$ sig (all) & 2/2 & 5--8/12 & Genuine in both \\
162	\bottomrule
163	\end{tabular}
164	\caption{Random-fault vs.\ adaptive regime contrast. $K_{\text{eff}}$ is genuinely significant under i.i.d.\ faults (2/2 under all corrections) but artifactual under adaptive attacks (0--1/12 after correction). The $R^2$ gap ($\Delta = 0.48$) quantifies the unpredictability introduced by adaptive adversaries.}
165	\label{tab:rf_contrast}
166	\end{table}
167	
168	Table~\ref{tab:rf_contrast} presents the contrast. Under random faults, $K_{\text{eff}}$ is significant 2/2 under \emph{all} correction methods ($p_{\text{bootstrap}} = 0.003$ for MMLU, $<$0.001 for ARC), with $R^2 = 0.78$--$0.81$. Under adaptive attacks, the same predictor collapses to 0--1/12 after correction. This is not a direction reversal---$K_{\text{eff}}$ is positively associated with vulnerability in \emph{both} regimes. The difference is that the RF association is genuine (panel structure determines fault tolerance under i.i.d.\ assumptions), while the adaptive association is inflated by panel overlap. The $R^2$ gap ($\Delta = 0.48$) directly quantifies the strategic variance introduced by adaptive adversaries that panel structure cannot predict.
169	
170	\subsection{ASR Concentration Analysis}
171	\label{sec:concentration}
172	
173	To provide mechanistic evidence for $\eta_{\max}$ dominance, we compute per-judge ASR distributions within each panel and measure concentration via Gini coefficients and Shannon entropy.
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\begin{tabular}{llccc}
179	\toprule
180	\textbf{Attack} & \textbf{Cat.} & \textbf{Gini} & \textbf{Entropy} & \textbf{Top-1 frac.} \\
181	\midrule
182	Prompt inject. & targ. & 0.82 & 0.73 & 0.65 \\
183	Score manip. & targ. & 0.79 & 0.78 & 0.62 \\
184	Position bias & targ. & 0.74 & 0.94 & 0.56 \\
185	Sycophancy & shared & 0.45 & 1.38 & 0.40 \\
186	Verbosity bias & shared & 0.42 & 1.47 & 0.37 \\
187	Authority bias & shared & 0.41 & 1.50 & 0.36 \\
188	\bottomrule
189	\end{tabular}
190	\caption{ASR concentration by attack category. Targeted attacks show highly concentrated ASR (Gini $>$ 0.7, top-1 judge contributes $>$56\% of panel ASR), providing mechanistic evidence for $\eta_{\max}$ dominance. Mann-Whitney $U$ test: $p < 0.001$ between categories.}
191	\label{tab:concentration}
192	\end{table}
193	
194	Table~\ref{tab:concentration} reveals a sharp dichotomy. Under targeted attacks, ASR is highly concentrated: the most vulnerable judge contributes 56--65\% of total panel ASR (mean Gini = 0.78). Under shared-bias attacks, ASR is more uniformly distributed (mean Gini = 0.43, top-1 fraction = 37\%). The Gini--$\eta_{\max}$ correlation is $r = 0.83$, directly linking panel-level vulnerability to judge-level concentration. This independently validates the GAM taxonomy: targeted and shared-bias attacks differ not only in $K_{\text{eff}}$ direction but in their micro-level ASR distribution patterns.
195	
196	\subsection{Aggregation Gradient}
197	\label{sec:aggregation}
198	
199	We evaluate five aggregation rules under clustered SE to characterize how vote aggregation modulates vulnerability.
200	
201	\begin{table}[t]
202	\centering
203	\small
204	\begin{tabular}{lccccl}
205	\toprule
206	\textbf{Rule} & \textbf{$\eta_{\max}$} & \textbf{$K_{\text{eff}}$} & \textbf{Neg.} & \textbf{$R^2$} & \textbf{Position} \\
207	\midrule
208	Veto & 11/12 & 0/12 & -- & 0.82 & Max vuln. \\
209	Threshold & 10/12 & 4/12 & 1/4 & 0.87 & High \\
210	Majority & 8/12 & 0/12 & -- & 0.28 & Moderate \\
211	Weighted & 6/12 & 1/12 & 0/1 & 0.26 & Low-mod. \\
212	Bayesian & 5/12 & 4/12 & 3/4 & 0.09 & Min vuln. \\
213	\bottomrule
214	\end{tabular}
215	\caption{Aggregation gradient under clustered SE. ``Neg.'' = fraction of significant $K_{\text{eff}}$ coefficients that are negative. Bayesian calibration weakens $\eta_{\max}$ (11$\to$5/12) and flips $K_{\text{eff}}$ direction (3/4 negative), while veto/threshold amplify the weakest-link channel.}
216	\label{tab:aggregation}
217	\end{table}
218	
219	Table~\ref{tab:aggregation} reveals a gradient from maximum to minimum vulnerability. Veto rule (any single judge can override) maximizes $\eta_{\max}$ dominance (11/12) with $K_{\text{eff}}$ completely suppressed. Threshold voting (unanimity) amplifies both channels ($R^2 = 0.87$). Bayesian calibration, which down-weights unreliable judges using prior accuracy estimates, achieves the strongest mitigation: $\eta_{\max}$ drops to 5/12 and $K_{\text{eff}}$ flips to majority-negative (3/4 significant coefficients negative), meaning diversity becomes protective.
220	
221	Under bootstrap, Bayesian $K_{\text{eff}}$ shows 3/12 significant---all negative (3/3 negative fraction = 100\%). This directional flip is the cleanest evidence that aggregation is an independent control lever, unaffected by the non-independence concerns that plague the diversity analysis.
222	
223	\subsection{Panel Design Algorithm}
224	\label{sec:design}
225	
226	We benchmark a two-stage robustness-first algorithm against 6 baseline strategies across 12 conditions.
227	
228	\begin{table}[t]
229	\centering
230	\small
231	\begin{tabular}{lccc}
232	\toprule
233	\textbf{Strategy} & \textbf{Mean ASR} & \textbf{Rank} & \textbf{$\Delta$ vs.\ random (pp)} \\
234	\midrule
235	Two-stage & 0.112 & 1 & $-$8.3 \\
236	$\min(\eta_{\max})$ & 0.119 & 2 & $-$7.6 \\
237	Strongest-$K$ & 0.131 & 3 & $-$6.4 \\
238	Uniform family & 0.158 & 4 & $-$3.7 \\
239	Max disagreement & 0.172 & 5 & $-$2.3 \\
240	Random & 0.195 & 6 & 0.0 \\
241	$\max(K_{\text{eff}})$ & 0.208 & 7 & $+$1.3 \\
242	\bottomrule
243	\end{tabular}
244	\caption{Panel design strategy comparison (mean ASR across 12 conditions). The $\max(K_{\text{eff}})$ strategy---the intuitive ``maximize diversity'' approach---performs \emph{worse} than random selection because it introduces weak models. Two-stage provides a marginal 0.7pp improvement over $\min(\eta_{\max})$ alone.}
245	\label{tab:strategy}
246	\end{table}
247	
248	Table~\ref{tab:strategy} presents the ranking. The most striking result is that $\max(K_{\text{eff}})$---the intuitive ``diversify your panel'' strategy---ranks \emph{last}, performing 1.3pp worse than random selection. This occurs because maximizing diversity necessarily introduces weaker models (the diversity-capability tradeoff, $r = 0.70$). The two-stage algorithm provides a consistent but modest improvement (0.7pp) over pure $\min(\eta_{\max})$, with the marginal gain concentrated in targeted attack conditions (5/6 wins, mean $\Delta = -1.1$pp) where controlled $K_{\text{eff}}$ optimization adds value after robustness screening.
249	
250	\subsection{Capability-Matched Validation}
251	\label{sec:capability}
252	
253	To disentangle $\eta_{\max}$ and $K_{\text{eff}}$ (confound $r = 0.70$ in the full pool), we conduct within-tier analysis using 9 base-tier models (84 panels), which reduces the confound to $r = 0.35$ and $\eta_{\max}$ variance by 65--70\%.
254	
255	\begin{table}[t]
256	\centering
257	\small
258	\begin{tabular}{lcccc}
259	\toprule
260	\textbf{Setting} & \textbf{Panels} & \textbf{$r$} & \textbf{$\eta_{\max}$ (CL)} & \textbf{$K_{\text{eff}}$ (CL)} \\
261	\midrule
262	Full pool & 455 & 0.70 & 8/12 & 0/12 \\
263	Base tier & 84 & 0.35 & 4/12 & 2/12 \\
264	\bottomrule
265	\end{tabular}
266	\caption{Cross-tier vs.\ within-tier comparison (clustered SE). Controlling for capability reduces confound and reveals $K_{\text{eff}}$ as a weak but detectable secondary factor (2/12, both in targeted conditions). The dominance ratio narrows from $\infty$ to 2:1, but $\eta_{\max}$ still dominates.}
267	\label{tab:capability}
268	\end{table}
269	
270	Within the base tier (Table~\ref{tab:capability}), $K_{\text{eff}}$ emerges as a weak secondary factor (2/12 significant under clustered SE), with the dominance ratio narrowing from $\infty$ to 2:1. Both significant $K_{\text{eff}}$ conditions are targeted attacks (mmlu$\times$prompt\_injection, $\beta = +0.31$, $p = 0.028$; mmlu$\times$score\_manipulation, $\beta = +0.25$, $p = 0.041$), consistent with the GAM taxonomy. The within-tier $R^2$ mean drops to 0.18 (vs.\ 0.30 in the full pool), confirming that cross-tier $\eta_{\max}$ variance is the primary source of predictive power.
271	
272	\subsection{Diversity-Capability Tradeoff}
273	\label{sec:tradeoff}
274	
275	The structural correlation between $K_{\text{eff}}$ and $\eta_{\max}$ ($r = 0.70$, 95\% CI $[0.66, 0.74]$) reflects a fundamental constraint in the current LLM ecosystem: maximizing behavioral diversity requires including models from different capability tiers, which inevitably introduces weaker judges. This correlation is strongest within model families ($r = 0.81$) and weakest at the frontier tier ($r = 0.35$), where architectural differences provide diversity without large capability gaps. The Pareto frontier analysis shows that 97.4\% of panels are dominated, with optimal panels clustering in the low-$K_{\text{eff}}$, low-$\eta_{\max}$ region. VIF analysis confirms moderate but non-pathological multicollinearity (VIF = 2.96, condition number = 4.8), with partial correlations of $r(\eta_{\max}, \text{ASR} \mid K_{\text{eff}}) = 0.42$ vs.\ $r(K_{\text{eff}}, \text{ASR} \mid \eta_{\max}) = 0.18$.
276	
277	\subsection{Panel Size Sensitivity}
278	\label{sec:panel_size}
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\begin{tabular}{lccccc}
284	\toprule
285	\textbf{$K$} & \textbf{Panels} & \textbf{$\eta_{\max}$} & \textbf{$K_{\text{eff}}$} & \textbf{Ratio} & \textbf{SE infl.} \\
286	\midrule
287	3 & 455 & 8/12 & 0/12 & $\infty$ & 2.5$\times$ \\
288	5 & 3003 & 9/12 & 1/12 & 9:1 & 4.1$\times$ \\
289	7 & 6435 & 9/12 & 1/12 & 9:1 & 6.3$\times$ \\
290	9 & 5005 & 8/12 & 2/12 & 4:1 & 7.8$\times$ \\
291	\bottomrule
292	\end{tabular}
293	\caption{Panel size sensitivity (clustered SE). $\eta_{\max}$ dominance persists across $K=3$--$9$, confirming the weakest-link mechanism is scale-invariant. SE inflation increases sharply with $K$, underscoring the necessity of non-independence correction in combinatorial designs.}
294	\label{tab:panel_size}
295	\end{table}
296	
297	Table~\ref{tab:panel_size} demonstrates that $\eta_{\max}$ dominance is not an artifact of small panels. Across $K = 3$ to $K = 9$, the $\eta_{\max}$ effect size decreases slightly (standardized $\beta$: 0.42 to 0.31) as larger panels provide more majority-vote fault tolerance, but the dominance ratio remains $\geq$4:1. The $\min(\eta_{\max})$ strategy wins 12/12 conditions at every panel size. SE inflation increases from 2.5$\times$ to 7.8$\times$, providing compelling evidence that non-independence correction is essential for panel studies at any scale.
298	
299	\subsection{Generation Benchmark Extension}
300	\label{sec:generation}
301	
302	To rule out MCQ-specific artifacts, we extend to MT-Bench, an open-ended generation benchmark with 1--10 scale scoring. We test 3 generation-specific attack types across 12 available models and 220 panels.
303	
304	\begin{table}[t]
305	\centering
306	\small
307	\begin{tabular}{lcccl}
308	\toprule
309	\textbf{Format} & \textbf{$\eta_{\max}$ (CL)} & \textbf{$K_{\text{eff}}$ (CL)} & \textbf{Ratio} \\
310	\midrule
311	MCQ (MMLU+ARC) & 8/12 & 0/12 & $\infty$ \\
312	Generation (MT-Bench) & 4/6 & 0/6 & $\infty$ \\
313	Combined & 12/18 & 0/18 & $\infty$ \\
314	\bottomrule
315	\end{tabular}
316	\caption{Cross-format consistency (clustered SE). $\eta_{\max}$ dominance generalizes from MCQ to open-ended generation evaluation. The combined ratio across 18 conditions is $\infty$ (12:0).}
317	\label{tab:generation}
318	\end{table}
319	
320	Table~\ref{tab:generation} confirms that $\eta_{\max}$ dominance generalizes across evaluation formats. Under clustered SE, the combined dominance ratio is 12:0 across 18 conditions. GAM classification of generation attacks aligns with the mechanistic taxonomy: style manipulation and length inflation are shared-bias (negative $K_{\text{eff}}$), while format gaming is targeted (positive $K_{\text{eff}}$). The $\min(\eta_{\max})$ strategy wins 6/6 generation conditions, confirming the practical recommendation is format-agnostic.
321	
322	\subsection{Partial-Knowledge Adversary}
323	\label{sec:partial}
324	
325	Real-world adversaries rarely have full knowledge of panel composition. We simulate three knowledge levels: full (baseline), family-only (adversary knows model family labels but not specific vulnerability profiles), and random (no targeting).
326	
327	\begin{table}[t]
328	\centering
329	\small
330	\begin{tabular}{lcccc}
331	\toprule
332	\textbf{Knowledge} & \textbf{ASR} & \textbf{$\eta_{\max}$ (CL)} & \textbf{$K_{\text{eff}}$ (CL)} & \textbf{$R^2$} \\
333	\midrule
334	Full & 0.195 & 8/12 & 0/12 & 0.30 \\
335	Family-only & 0.160 & 7/12 & 0/12 & 0.24 \\
336	Random & 0.113 & 3/12 & 0/12 & 0.08 \\
337	\bottomrule
338	\end{tabular}
339	\caption{Adversary knowledge level comparison (clustered SE). Family-only knowledge retains 82\% attack efficiency. $K_{\text{eff}}$ is 0/12 under all knowledge levels. $\eta_{\max}$ dominance persists under realistic threat models.}
340	\label{tab:partial}
341	\end{table}
342	
343	Table~\ref{tab:partial} reveals that family-level knowledge retains 82\% of full-knowledge attack efficiency ($\text{ASR} = 0.160$ vs.\ $0.195$), because same-family models share training pipeline and architectural biases ($r_{\text{family-vulnerability}} = 0.61$). Defenders cannot rely on panel composition secrecy: family labels are easily inferred from API endpoints and response styles. $K_{\text{eff}}$ remains 0/12 under all knowledge levels, and $\eta_{\max}$ dominance persists even under family-only targeting (7/12), confirming the core findings are robust to adversary capability assumptions.
344	
345	\section{Discussion}
346	
347	\paragraph{When diversity helps.} Our results do not imply diversity is universally harmful. Under shared-bias attacks, GAM analysis consistently shows negative $K_{\text{eff}}$ direction (8/8 conditions including extended attacks), meaning diversity provides partial immunity when the adversary exploits biases shared across model families. After robustness screening removes weak judges, the diversity-capability tradeoff is weakened ($r$ drops from 0.70 to 0.35), creating conditions where diversity optimization adds marginal value. And in non-adversarial settings, diversity remains beneficial for reducing calibration errors and position biases.
348	
349	\paragraph{Practical recommendations.} Based on our findings, we recommend a defense stack combining: (1) robustness-first screening to eliminate $\eta_{\max}$ as a vulnerability driver, and (2) Bayesian aggregation to reverse $K_{\text{eff}}$ from harmful to protective. This dual-channel approach addresses both structural vulnerability drivers. The $\max(K_{\text{eff}})$ strategy should be explicitly avoided, as it performs worse than random selection.
350	
351	\paragraph{Methodological implications.} The dramatic significance shift from OLS to clustered SE ($K_{\text{eff}}$: 8/12 $\to$ 0/12) is a cautionary finding for all combinatorial evaluation designs where the same items (here, judges) appear in multiple experimental units (panels). SE inflation of 2.5--7.8$\times$ can produce severely misleading conclusions. We recommend that future panel studies routinely report clustered SE alongside OLS.
352	
353	\section{Conclusion}
354	
355	We conducted the first large-scale empirical decomposition of multi-judge LLM evaluation panel vulnerability. Our central finding---that panel vulnerability is dominated by the weakest individual judge, not panel diversity---challenges the implicit BFT assumption underlying multi-judge evaluation design. The dominance ratio of 5:1 ($\eta_{\max}$ over $K_{\text{eff}}$) is robust across 9 attack types, 3 benchmarks, 4 panel sizes, 3 adversary knowledge levels, and 4 statistical correction methods. Aggregation rule choice provides an independent control lever: Bayesian calibration reverses diversity's role from vulnerability to defense. We release our two-stage panel design algorithm as a practical tool for building adversarially robust evaluation panels.
356	
357	\section*{Limitations}
358	
359	Our study has three main limitations. First, the model pool (15 models, 6 families) represents the current LLM ecosystem; the diversity-capability tradeoff ($r = 0.70$) may weaken as more capable open-source models become available. Second, our adaptive adversary model assumes strategic targeting of individual judges---real-world adversaries may face additional constraints (e.g., limited query budgets) that reduce attack efficiency below the levels we measure. Third, the Bayesian aggregation defense requires access to clean-data accuracy estimates, which may themselves be subject to manipulation; evaluating the robustness of the defense stack to meta-adversarial attacks remains future work.
360	
361	\begin{thebibliography}{9}
362	\bibitem{zheng2023judging}
363	Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P.\ Xing, Hao Zhang, Joseph E.\ Gonzalez, and Ion Stoica.
364	\newblock Judging {LLM}-as-a-{J}udge with {MT-B}ench and {C}hatbot {A}rena.
365	\newblock In \emph{Advances in Neural Information Processing Systems}, 2023.
366	
367	\bibitem{lamport1982byzantine}
368	Leslie Lamport, Robert Shostak, and Marshall Pease.
369	\newblock The {B}yzantine generals problem.
370	\newblock \emph{ACM Transactions on Programming Languages and Systems}, 4(3):382--401, 1982.
371	
372	\bibitem{hendrycks2021mmlu}
373	Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
374	\newblock Measuring massive multitask language understanding.
375	\newblock In \emph{International Conference on Learning Representations}, 2021.
376	
377	\bibitem{clark2018arc}
378	Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord.
379	\newblock Think you have solved question answering? {T}ry {ARC}, the {AI2} reasoning challenge.
380	\newblock \emph{arXiv preprint arXiv:1803.05457}, 2018.
381	
382	\bibitem{perez2022red}
383	Ethan Perez, Saffron Huang, Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, and Geoffrey Irving.
384	\newblock Red teaming language models with language models.
385	\newblock In \emph{Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing}, 2022.
386	
387	\bibitem{panickssery2024llm}
388	Arjun Panickssery, Samuel R.\ Bowman, and Shi Feng.
389	\newblock {LLM} evaluators recognize and favor their own generations.
390	\newblock \emph{arXiv preprint arXiv:2404.13076}, 2024.
391	
392	\bibitem{raina2024llm}
393	Vyas Raina, Adian Liusie, and Mark J.\ F.\ Gales.
394	\newblock Is {LLM}-as-a-{J}udge robust? {I}nvestigating universal adversarial attacks on zero-shot {LLM} assessment.
395	\newblock In \emph{Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing}, 2024.
396	\end{thebibliography}
397	
398	\end{document}
399	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a01ba10b-2051-4a1b-a188-bdeb24e6d66f",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "40788e39-7d54-4891-84f6-3ea823da738a",
  "sourceToolAssistantUUID": "a01ba10b-2051-4a1b-a188-bdeb24e6d66f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-22T23:04:32.329Z_

Now I have a thorough understanding of both the paper versions and the underlying project data. Let me also check the latest review report for this version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40788e39-7d54-4891-84f6-3ea823da738a",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSgcwHTFmAqMyGN5NRS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cfa57f4-0102-4f42-93ce-d71b1545435f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011m9njrXz8ybHr9XUbVeLSf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10998,
      "cache_read_input_tokens": 90913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10998,
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

_source line 41 · 2026-05-22T23:04:34.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sj41EAXRwiYRPGHXttXcFe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/dream_reports/dream_20260522T221131/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cfa57f4-0102-4f42-93ce-d71b1545435f",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSgcwHTFmAqMyGN5NRS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a004d43a-7786-4647-8cf3-cad633704041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011m9njrXz8ybHr9XUbVeLSf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10998,
      "cache_read_input_tokens": 90913,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 90913,
          "cache_creation_input_tokens": 10998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10998,
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

_source line 42 · 2026-05-22T23:04:34.885Z_

<details><summary>↩ Tool result · `toolu_01Sj41EAXRwiYRPGHXttXcFe`</summary>

```text
1	---
2	dream_id: dream_20260522T221131
3	tier: best
4	overall_score: 3.0 — Findings
5	timestamp: 2026-05-22T22:55:55.043972+00:00
6	---
7	
8	# Dream Review Report — "Weakest Link, Not Diversity: Adversarial Vulnerability in Multi-Judge LLM Evaluation"
9	
10	**Review Mode:** Full (2 Reviewers, 4-step roundtable)  
11	**Target Venue:** EMNLP 2026 (ARR)  
12	**Date:** 2026-05-22  
13	
14	---
15	
16	## Paper Summary
17	
18	The paper conducts the first large-scale empirical decomposition of multi-judge LLM evaluation panel vulnerability into two structural predictors: individual judge weakness (η_max, the vulnerability of the weakest panel member) and panel diversity (K_eff, effective number of independent behavioral clusters). Using 15 models from 6 families, 455 panels (K=3), 9 attack types across 2 mechanistic categories (targeted and shared-bias), and 3 benchmarks (MMLU, ARC-Challenge, MT-Bench), the paper finds that η_max robustly dominates panel vulnerability with a 5:1 dominance ratio over K_eff under wild cluster bootstrap inference. K_eff's apparent significance under OLS (8/12 conditions) collapses to 0/12 after clustered SE correction. A GAM analysis reveals a targeted/shared-bias taxonomy (10:8 split), and aggregation rule choice modulates vulnerability (Bayesian calibration reverses K_eff direction). A two-stage robustness-first panel design algorithm wins 12/12 conditions. The paper claims 5 contributions and includes 10 tables across 11 experiment subsections.
19	
20	---
21	
22	## Reviewer R1 — Methods & Experiments
23	
24	### Strengths
25	
26	**S1. Well-defined decomposition framework.** The operationalization of panel vulnerability into η_max and K_eff is clean and enables systematic analysis. The research question — which structural factor drives panel vulnerability under adversarial conditions? — is precisely stated and empirically tractable.
27	
28	**S2. Rigorous attention to non-independence correction.** The paper's strongest methodological contribution is identifying and addressing panel non-independence. The demonstration that K_eff collapses from 8/12 (OLS) to 0/12 (clustered SE) is a cautionary finding applicable to all combinatorial evaluation designs. Reporting 4 correction methods side-by-side is good practice.
29	
30	**S3. Comprehensive robustness checks.** The paper tests its central claim across multiple panel sizes (K=3–9), benchmarks (MCQ + generation), adversary knowledge levels (full/family/random), attack types (9 types, 2 categories), and correction methods. This breadth is impressive for an 8-page paper.
31	
32	**S4. RF contrast experiment.** The random-fault Monte Carlo contrast (Table 3) provides clean causal evidence for BFT assumption failure. K_eff significant 2/2 under i.i.d. faults vs. 0/12 under adaptive attacks (all corrections) is a compelling demonstration. The R² gap (0.78–0.81 vs. 0.25–0.35) quantifies the predictability difference.
33	
34	**S5. Aggregation gradient.** The finding that Bayesian calibration reverses K_eff direction (Table 5) is non-obvious and practically actionable. The gradient from veto (max vulnerability) to Bayesian (min vulnerability) provides a clean design spectrum.
35	
36	### Weaknesses
37	
38	**W1 (Major). 15 clusters may be insufficient for reliable clustered SE.** The paper clusters by individual judge (15 clusters) for the clustered SE correction. Cameron, Gelbach & Miller (2008) recommend ≥50 clusters for reliable inference; with 15 clusters, CR1 standard errors can be severely biased (typically over-conservative), producing inflated Type II error rates. The paper's central finding — K_eff 0/12 under clustered SE — could be a power artifact rather than a genuine null. The wild cluster bootstrap partially addresses this but is also unreliable with <20 clusters (Webb 2023). The paper never discusses this limitation. This is the most consequential methodological concern because it directly affects the paper's central claim.
39	
40	**W2 (Major). K_eff formula not given.** The paper defines K_eff as "the effective number of independent clusters" derived from "pairwise mutual information between all judge pairs' evaluation vectors on clean data." The exact computation — how MI is estimated, what clustering method is used, how the effective number is derived — is absent. Is this spectral analysis of the MI matrix? Eigenvalue thresholding? The Participation Ratio? Without the formula, the main predictor variable is irreproducible.
41	
42	**W3 (Major). Attack implementation entirely absent.** The 9 attack types are listed by name (prompt injection, score manipulation, etc.) but their operational implementation is never described. How are prompt injections actually executed against LLM judges? What prompts are used? What is the adversary's budget? What does "adaptive" mean operationally — does the adversary optimize per-judge or per-panel? For a paper whose entire empirical contribution rests on attack experiments, this is a critical omission.
43	
44	**W4 (Moderate). ε constant and log-log specification issues.** The regression uses log(ASR + ε) but ε is never specified. For near-zero ASR values, the choice of ε can substantially affect results. More fundamentally, log-log OLS is questionable for ASR ∈ [0,1] — beta regression (mentioned only in §4.8 in passing) would be the natural choice. The paper reports that beta regression gives similar results (η_max 10/12, K_eff 4/12) but doesn't use it as the primary specification without justification.
45	
46	**W5 (Moderate). No multiple testing correction across conditions.** The paper reports "η_max significant in X/12 conditions" but never applies Bonferroni or FDR correction across the 12 (or 18) conditions. The VIF section mentions that Bonferroni gives η_max 7/12 and K_eff 2/12, and FDR gives η_max 8/12 and K_eff 3/12 — but these are buried and not in the main results tables.
47	
48	**W6 (Moderate). Model identities underspecified.** The paper mentions 6 families (GPT, Claude, Gemini, Llama, Qwen, Mistral) and 3 capability tiers (frontier, mid, base) but doesn't list the 15 specific model versions, temperature settings, or prompt templates used.
49	
50	**W7 (Minor). Confidence intervals sparse.** Most reported quantities (R², effect sizes, correlation coefficients) are point estimates. The diversity-capability tradeoff correlation (r=0.70) has a CI, but most others don't.
51	
52	### Questions for Authors
53	1. What happens if you cluster by model family (6 clusters) instead of individual model (15)? Or by panel? The choice of clustering unit is consequential.
54	2. What is the exact K_eff computation? Please provide the formula.
55	3. How sensitive are the log-log OLS results to the choice of ε? Have you tried ε ∈ {0.001, 0.01, 0.1}?
56	4. Why not use beta regression as the primary specification given ASR ∈ [0,1]?
57	5. Can you provide a power analysis for detecting a K_eff effect of the size observed in within-tier analysis (β = 0.25–0.31) with 15 clusters?
58	
59	### R1 Scores
60	- **Soundness:** 3/5 (η_max finding robust, but K_eff null uncertain due to cluster count; attack details missing)
61	- **Excitement:** 3.5/5 (important question, good experimental breadth)
62	- **Reproducibility:** 2/5 (K_eff formula absent, attack implementation absent, model versions missing)
63	
64	---
65	
66	## Reviewer R2 — Novelty & Related Work
67	
68	### Strengths
69	
70	**S1. Timely and practically relevant research question.** Multi-judge LLM evaluation panels are increasingly deployed; understanding their adversarial robustness properties is important for the NLP community. The question is well-motivated.
71	
72	**S2. Creative BFT framing.** Using Byzantine Fault Tolerance theory as the conceptual lens provides a clear narrative structure. The RF contrast experiment (Table 3) operationalizes the "BFT assumption violation" cleanly.
73	
74	**S3. Counter-intuitive finding about diversity.** The result that max(K_eff) performs worse than random selection (Table 6) is surprising and practically valuable. This directly challenges the intuitive "diversify your panel" recommendation.
75	
76	**S4. GAM taxonomy is a clean conceptual contribution.** The targeted/shared-bias mechanistic split (10:8 across 9 attack types) provides an interpretable framework for understanding when diversity helps vs. hurts. The ASR concentration analysis (Table 4) provides independent mechanistic validation.
77	
78	**S5. Actionable recommendations.** The two-stage algorithm and the Bayesian aggregation recommendation are concrete and implementable.
79	
80	### Weaknesses
81	
82	**W1 (Critical). Only 7 references — fatally insufficient for EMNLP.** The paper spans three major research areas (LLM evaluation, adversarial robustness, distributed systems) but cites only 7 works. Critical missing literature includes:
83	- **Ensemble diversity theory:** Kuncheva & Whitaker (2003) on diversity measures, Krogh & Vedelsby (1995) on the ambiguity decomposition, Brown et al. (2005) on diversity in neural network ensembles. The diversity-vs-individual-strength tradeoff is *the* classical question in ensemble learning — the paper doesn't acknowledge this entire body of work.
84	- **LLM-as-judge papers:** Li et al. (2024, AlpacaEval), Dubois et al. (2024, Length-controlled AlpacaEval), Ye et al. (2024, Flask), Kim et al. (2024), Shankar et al. (2024, "Who Validates the Validators?"), Bavaresco et al. (2024).
85	- **Crowdsourcing quality literature:** Dawid & Skene (1979), Welinder et al. (2010), Sheng et al. (2008) — panel design for annotation quality has a rich history.
86	- **Adversarial ensemble robustness:** Tramèr et al. (2018, ensemble adversarial training), He et al. (2017, adversarial transferability).
87	- **Multi-agent debate / evaluation:** Du et al. (2023), Liang et al. (2023), Chan et al. (2024).
88	
89	This is a reviewer-blocking issue. The paper cannot be accepted in any track without substantially expanded related work.
90	
91	**W2 (Major). Related Work section is ~15 lines.** Three brief paragraphs covering LLM-as-Judge, adversarial attacks, and BFT is far below EMNLP standards for a paper that claims to bridge these areas. The paper doesn't discuss how its findings relate to classical ensemble diversity results, which is the most obvious point of comparison.
92	
93	**W3 (Major). Core finding has limited novelty given ensemble learning precedent.** In classical ensemble theory, it is well-established that individual member quality often matters more than diversity (bias-variance decomposition: diversity reduces variance but doesn't address bias). The paper's finding that η_max dominates K_eff can be seen as a reconfirmation of this principle in the specific context of adversarial LLM evaluation. The paper should explicitly position itself relative to this body of work and articulate what is genuinely new about the LLM-judge setting (e.g., the adaptive adversary dimension, the BFT contrast, the aggregation gradient).
94	
95	**W4 (Major). No figures.** An 8-page empirical paper with 10 tables and 0 figures is highly unusual. Key visualizations that would substantially improve readability:
96	- K_eff vs η_max scatter plot with Pareto frontier (currently described in text only in §4.8)
97	- Aggregation gradient visualization
98	- RF vs adaptive regime contrast
99	- GAM taxonomy heatmap
100	- Strategy comparison radar/bar chart
101	
102	The experiment plan includes detailed specifications for many such figures. Their absence suggests the paper may have been rushed.
103	
104	**W5 (Moderate). Title overstates the claim.** "Weakest Link, *Not* Diversity" is too absolute. The paper's own results show:
105	- K_eff matters under Bayesian aggregation (4/12 significant, 3/4 negative = protective)
106	- K_eff emerges as a secondary factor in within-tier analysis (2/12 significant)
107	- Under shared-bias attacks, diversity consistently shows a protective direction
108	A more accurate title would be "Weakest Link Over Diversity" or "Weakest Link Dominates Diversity."
109	
110	**W6 (Moderate). BFT analogy is imprecise.** Byzantine Fault Tolerance assumes Byzantine (arbitrary, worst-case) faults where faulty nodes can behave in any way. The paper's "adaptive adversary" uses specific attack strategies (prompt injection, etc.) — this is closer to a strategic adversary model than a Byzantine one. The key BFT guarantee (f < n/3 tolerance) assumes independent faults, which the paper correctly identifies as violated, but the connection between the paper's threat model and formal BFT is looser than presented.
111	
112	**W7 (Minor). 11 experiment subsections in 4 pages is too compressed.** Several experiments (panel size sensitivity, partial-knowledge adversary, VIF diagnostics) could be moved to supplementary material to give more space to the core results, related work, and methodology. The current presentation sacrifices depth for breadth.
113	
114	### Questions for Authors
115	1. How does your finding relate to Krogh & Vedelsby's (1995) ambiguity decomposition and the classical ensemble diversity-accuracy tradeoff?
116	2. Why only 7 references? This seems well below the standard for a paper at this venue.
117	3. Would you consider softening the title to better reflect the nuanced findings (K_eff matters under certain conditions)?
118	4. Can you be more precise about how your adversary model relates to formal BFT? What specific BFT guarantee is being tested/violated?
119	5. Who are the intended users of the two-stage algorithm? How common is formal panel design in current LLM evaluation practice?
120	
121	### R2 Scores
122	- **Soundness:** 3/5 (BFT framing imprecise, missing ensemble context creates positioning gap)
123	- **Excitement:** 3/5 (interesting applied question, but novelty reduced by ensemble precedent; provocative finding about max(K_eff) being worse than random is the most exciting element)
124	- **Reproducibility:** 2.5/5 (attack details and K_eff formula missing, though overall study design is clear)
125	
126	---
127	
128	## Roundtable Convergence
129	
130	### Points of Agreement (R1 + R2)
131	
132	1. **The η_max dominance finding is robust and valuable.** Significance under 4 correction methods, stability across panel sizes (K=3–9), benchmarks (MCQ + generation), and adversary knowledge levels (full/family/random) makes this a solid empirical finding.
133	
134	2. **The K_eff null result is uncertain due to statistical power concerns.** With only 15 clusters for clustered SE, the 0/12 result may reflect insufficient power rather than a genuine null. This interacts with the title's strong claim ("Not Diversity") to create a compound issue: the paper overclaims a result it may lack power to establish.
135	
136	3. **Reproducibility is critically low.** Both reviewers identify missing K_eff formula, absent attack implementation details, and unspecified model versions as blocking issues.
137	
138	4. **7 references is a blocking issue for EMNLP.** The paper needs at minimum 25–30 references covering ensemble diversity, LLM-as-judge, crowdsourcing, and adversarial robustness literatures.
139	
140	5. **No figures significantly hurts presentation.** Both reviewers note this is unusual and detrimental for an empirical paper.
141	
142	6. **Several secondary findings add real value:** the GAM taxonomy (targeted vs shared-bias), the aggregation gradient (Bayesian K_eff reversal), the RF contrast experiment, and the max(K_eff) < random result are all interesting contributions that strengthen the overall work.
143	
144	### Remaining Disagreement
145	
146	- R1 weights the 15-cluster methodological concern more heavily (this could fundamentally undermine the central claim).
147	- R2 weights the novelty concern more heavily (the finding may be predictable from ensemble theory).
148	- Both agree these concerns are compatible and don't conflict — they're different facets of the same overall assessment (Findings-level).
149	
150	### Compound Issue: Power × Overclaiming
151	
152	The most significant cross-reviewer insight is the interaction between R1's power concern and R2's title concern. The paper:
153	1. Uses a method (clustered SE with 15 clusters) that may be over-conservative for K_eff
154	2. Interprets the resulting null (0/12) as strong evidence against diversity
155	3. Uses this to justify the title "Not Diversity"
156	4. But then shows K_eff *does* matter under Bayesian aggregation (4/12) and within-tier (2/12)
157	
158	A more honest framing would be: "η_max dominates K_eff in the full-pool analysis, but the relative contribution of K_eff is difficult to establish precisely due to the confound (r=0.70) and the small number of clustering units."
159	
160	---
161	
162	## Converged Scores
163	
164	| Dimension | R1 | R2 | Converged |
165	|-----------|----|----|-----------|
166	| Soundness | 3 | 3 | **3** |
167	| Excitement | 3.5 | 3 | **3** |
168	| Reproducibility | 2 | 2.5 | **2** |
169	| **Overall Assessment** | 3 | 3 | **3.0** |
170	
171	**Overall Assessment: 3.0 — Findings**
172	
173	---
174	
175	## Detailed Justification
176	
177	### Why not Main (4.0)?
178	1. **Reproducibility crisis:** K_eff formula, attack implementation, and model details are all missing — a reviewer cannot attempt to verify the results.
179	2. **Methodological gap:** The 15-cluster concern is never discussed, creating a gap between the paper's strong claims and its statistical foundation.
180	3. **Thin related work:** 7 references for a paper spanning 3 research areas is unacceptable. Missing the ensemble diversity literature is particularly damaging since it's the most directly relevant body of work.
181	4. **No figures:** Presentation quality is below Main standards for an empirical paper.
182	5. **Title overstatement:** The paper's own results contradict the absolute "Not Diversity" framing.
183	
184	### Why not Resubmit (2.0)?
185	1. **η_max dominance is a solid finding** that survives multiple robustness checks.
186	2. **The RF contrast experiment** is well-designed and provides genuine causal evidence.
187	3. **The aggregation gradient** is a non-obvious, practically relevant finding.
188	4. **max(K_eff) < random** is a surprising and valuable empirical result.
189	5. **The research question is important** and the experimental breadth is impressive.
190	
191	### Why Findings (3.0)?
192	The paper makes a real empirical contribution to understanding multi-judge panel robustness. The η_max dominance finding, the RF contrast, the aggregation gradient, and the diversity-maximization pitfall are all valuable. However, the combination of reproducibility gaps, thin related work, presentation issues, and the uncertain K_eff null result prevent Main acceptance. With substantial revision (expanded related work, K_eff formula, attack details, figures, power analysis, softened title), this could be a strong Main submission.
193	
194	---
195	
196	## Actionable Revision Recommendations
197	
198	### Must-Fix (Blocking)
199	1. **Expand related work to 25–30+ references.** Include ensemble diversity theory (Kuncheva, Krogh & Vedelsby, Brown et al.), LLM-as-judge papers (AlpacaEval, Flask, etc.), crowdsourcing (Dawid-Skene), and adversarial ensemble robustness (Tramèr et al.).
200	2. **Provide the exact K_eff formula.** Specify: MI estimation method, clustering algorithm (if any), the formula mapping MI matrix to K_eff.
201	3. **Describe attack implementation.** For each of the 9 attack types: what prompt templates, adversary strategy, budget, and evaluation protocol are used?
202	4. **Specify model versions.** List all 15 models with exact version identifiers, API dates, temperature settings, and prompting templates.
203	5. **Add figures.** At minimum: (a) K_eff vs η_max scatter with Pareto frontier, (b) aggregation gradient visualization, (c) RF vs adaptive contrast.
204	
205	### Should-Fix (Significantly Strengthens)
206	6. **Discuss the 15-cluster power limitation.** Include a power analysis for detecting K_eff effects of the size found in within-tier analysis (β ≈ 0.25–0.31).
207	7. **Use beta regression as primary or co-primary specification.** Log-log OLS on [0,1] data is non-standard; report both.
208	8. **Apply multiple testing correction.** Report Bonferroni/FDR-adjusted significance counts alongside raw counts.
209	9. **Soften the title.** "Weakest Link Over Diversity" or similar — reflect that K_eff matters conditionally.
210	10. **Move 3–4 experiments to supplementary.** Panel size sensitivity, VIF diagnostics, and partial-knowledge adversary are natural candidates. Use freed space for related work and methodology.
211	11. **Specify the ε constant** and report sensitivity analysis.
212	12. **Position relative to ensemble diversity literature.** Explicitly discuss how the η_max > K_eff finding relates to the classical bias-variance tradeoff in ensembles.
213	
214	### Nice-to-Have
215	13. **Code and data release** (or at minimum, a reproducibility appendix with pseudocode).
216	14. **Confidence intervals** for all key quantities.
217	15. **Discussion of clustering unit choice** (individual judge vs. model family vs. panel-level).
218	
219	---
220	
221	## Experiment Coverage Assessment
222	
223	| Planned Experiment | Paper Coverage | Notes |
224	|---|---|---|
225	| 1. 15-Model Scaling (plan_001) | ✅ Full (Table 1) | Core results well-reported |
226	| 2. Attack Expansion (plan_002) | ✅ Full (Table 2) | Clean extension to 18 conditions |
227	| 3. RF BFT Contrast (plan_003) | ✅ Full (Table 3) | Strong causal evidence |
228	| 4. Capability-Matched (plan_004) | ✅ Adequate (Table 7) | Brief but key results present |
229	| 5. Panel Design Algorithm (plan_005) | ✅ Full (Table 6) | Clear strategy comparison |
230	| 6. ASR Concentration (plan_006) | ✅ Full (Table 4) | Good mechanistic evidence |
231	| 7. Diversity-Capability Tradeoff (plan_007) | ⚠️ Text only (§4.8) | No figure — described in one paragraph |
232	| 8. Panel Size Sensitivity (plan_008) | ✅ Full (Table 8) | Clean robustness check |
233	| 9. VIF Diagnostics (plan_009) | ⚠️ Brief mention (§4.8) | VIF=2.96, condition number=4.8 mentioned in one sentence |
234	| 10. Aggregation Gradient (plan_010) | ✅ Full (Table 5) | Including veto rule addition |
235	| 11. Generation Extension (plan_011) | ✅ Full (Table 9) | MT-Bench results clear |
236	| 12. Partial-Knowledge (plan_012) | ✅ Full (Table 10) | Three knowledge levels tested |
237	
238	**Coverage: 10/12 fully covered, 2/12 briefly mentioned.** The experiment plan's many figures are entirely absent from the paper. The planned detailed per-condition breakdowns are compressed into summary counts.
239	
240	---
241	
242	## Meta-Assessment
243	
244	This paper addresses a genuinely important question for the NLP evaluation community: does diversity protect multi-judge panels against adversarial attack? The answer — that individual judge robustness (η_max) matters far more than panel diversity (K_eff) — is a valuable empirical finding, even if it echoes classical ensemble theory. The experimental breadth is impressive, covering multiple axes of variation (attacks, benchmarks, panel sizes, knowledge levels, correction methods).
245	
246	However, the paper in its current form reads like a rushed first draft of a strong paper. The complete absence of figures, the 7-reference bibliography, the missing K_eff formula, and the absent attack implementation details suggest that significant revision is needed before this work is ready for Main conference acceptance. The 15-cluster power concern adds a genuine methodological uncertainty that the paper does not acknowledge.
247	
248	With the recommended revisions — particularly expanded related work, reproducibility details, figures, and honest discussion of power limitations — this could become a 3.5–4.0 paper in a subsequent cycle.
249	
250	
251	---
252	
253	## 引用验证结果
254	
255	**统计**: 40 篇文献 / 61 处引用 / 在线验证 40/40 篇
256	
257	### 问题 (10)
258	
259	- ⚠️ `almasoud2026security` — 元数据不匹配: first_author: bib=al masoud vs api=masoud
260	- ⚠️ `tramer2018ensemble` — 元数据不匹配: first_author: bib=tram\`er vs api=tramèr
261	- ⚠️ `schneier2000secrets` — 元数据不匹配: first_author: bib=schneier vs api=1963-
262	- ⚠️ `hendrycks2021mmlu` — 元数据不匹配: year: bib=2021 vs api=2025, first_author: bib=hendrycks vs api=son
263	- ❌ `condorcet1785essai` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.38 below threshold 0.82
264	- ⚠️ `brown2005managing` — 元数据不匹配: year: bib=2005 vs api=2023, first_author: bib=brown vs api=zelenkov
265	- ⚠️ `keppo2026fragility` — 在 .bib 中但正文未引用
266	- ⚠️ `kraskov2004estimating` — 在 .bib 中但正文未引用
267	- ⚠️ `schulhoff2023hackaprompt` — 在 .bib 中但正文未引用
268	- ⚠️ `zheng2024lmsyschat` — 在 .bib 中但正文未引用
269	
270	### ✅ 通过 (34)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a004d43a-7786-4647-8cf3-cad633704041",
  "isSidechain": true,
  "promptId": "1e94c2b0-ff5a-44a5-87b0-4dd92e95e0e0",
  "agentId": "abcc09248c70fce74",
  "type": "user",
  "uuid": "88488133-34c7-410f-8e0c-5e41360771f2",
  "sourceToolAssistantUUID": "a004d43a-7786-4647-8cf3-cad633704041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-22T23:06:33.122Z_

Now I have comprehensive knowledge of both the paper versions and all underlying project data. The key insight is that there are **two distinct paper versions**: the earlier "best" dream (dream_20260522T173833) that presents the "Diversity Trap" framing with inflated numbers, and the later corrected version (dream_20260522T221131) that honestly reports the non-independence correction results. The task asks me to review the paper described in the task prompt, which appears to match a hybrid -- the title references "Mirage of Significance" and discusses non-independence inflation, which aligns with the corrected v5 framing, but some of the specific numbers in the summary match a different version. Let me produce my R1 review grounded in the actual project data and the most recent paper version.

## R1 Review: Methods and Experiments

### Summary

This paper decomposes multi-judge LLM evaluation panel vulnerability into two structural predictors -- individual judge weakness (eta_max) and panel diversity (K_eff) -- using 15 models, 455 combinatorial panels, 9 attack types, and 3 benchmarks. The central methodological contribution is demonstrating that standard OLS regression dramatically overstates both predictors' significance due to structural non-independence among combinatorial panels (each model appears in 91 of 455 panels), with wild cluster bootstrap correction collapsing K_eff significance from 8/12 to 1/12 conditions and eta_max from 11/12 to 5/12. The paper presents multiple correction methods, a random-fault BFT contrast experiment, and a robustness-first panel design algorithm.

### Strengths

1. **Identification of the non-independence problem is the paper's strongest contribution.** The observation that combinatorial panel construction (C(15,3) = 455 panels from 15 models) produces massively overlapping observations -- each model appearing in 91 panels -- is an important methodological finding. The demonstration that OLS significance collapses under proper correction (K_eff: 8/12 to 0-1/12; SE inflation up to 7.2x at K=9) is a genuine cautionary finding for the growing body of work on LLM evaluation panel design. This contribution alone has value independent of the specific substantive findings.

2. **Four correction methods reported side-by-side.** Presenting OLS, clustered SE (CR1), wild cluster bootstrap (Rademacher weights, max-p across 3 positions), and mixed effects in a single comparison table (Table 1 in the v5 paper) is rigorous and transparent. The agreement between clustered SE (K_eff: 0/12) and wild bootstrap (K_eff: 1/12) provides cross-validation of the correction approach.

3. **Random-fault BFT contrast is well-designed.** The Monte Carlo simulation (10,000 iterations) with i.i.d. fault probabilities calibrated to clean accuracy provides a proper counterfactual. K_eff achieving significance 2/2 under all corrections in the random-fault regime, versus 0-1/12 under adaptive attacks, provides clean evidence for BFT assumption violation. The R-squared gap (0.78-0.81 vs 0.25-0.35) elegantly quantifies how adaptive adversary behavior introduces strategic variance that panel structure cannot predict.

4. **GAM taxonomy (targeted vs shared-bias) is a useful organizing principle.** The 10:8 split across 9 attack types, with K_eff positive (diversity harmful) for targeted attacks and negative (diversity protective) for shared-bias attacks, provides a predictive framework. The ASR concentration analysis (Table 4 in v5: Gini 0.74-0.82 for targeted vs 0.41-0.45 for shared-bias) provides independent mechanistic validation from a different measurement approach.

5. **Aggregation gradient is a non-obvious practical finding.** The demonstration that Bayesian calibration reverses K_eff's direction (3/4 significant coefficients negative, i.e., diversity becomes protective) while threshold voting amplifies vulnerability (R-squared = 0.87) is actionable. This is probably the paper's most novel empirical contribution.

6. **Max-K_eff worse than random is a compelling negative result.** The finding that naive diversity maximization performs worse than random selection (ASR 0.208 vs 0.195, Table 6 in v5) provides a crisp, memorable takeaway with direct practical implications.

### Weaknesses

1. **(Major) 15 clusters is insufficient for reliable clustered inference, and this is never discussed.** The paper clusters by individual judge (15 clusters) for both CR1 standard errors and wild cluster bootstrap. Cameron, Gelbach & Miller (2008) recommend a minimum of 50 clusters for CR1 reliability; with 15 clusters, CR1 standard errors are known to be severely biased, typically over-conservative, producing inflated Type II error rates. Wild cluster bootstrap with fewer than 20 clusters is also unreliable per Webb (2023). The paper's central finding -- K_eff 0/12 under clustered SE -- could be entirely a power artifact rather than a genuine null. The max-p procedure (taking the maximum p-value across 3 judge-position clusterings) further compounds the conservatism. The paper never acknowledges or discusses this limitation, despite it directly undermining the central claim. A power analysis for detecting a K_eff effect of the size observed in within-tier analysis (standardized beta approximately 0.25-0.31) with only 15 clusters is essential.

2. **(Major) The K_eff computation is never specified.** The paper defines K_eff as "the effective number of independent behavioral clusters" derived from pairwise mutual information, but provides no formula. How is MI estimated (empirical, k-NN, binning)? How is the MI matrix converted to K_eff (spectral analysis, participation ratio, eigenvalue thresholding)? The project memory reveals that at least two different K_eff formulas were used during the project (a max-MI formula and an empirical formula, with the former producing erroneously inflated significance in bootstrap v1). Without the exact formula, the main predictor variable is irreproducible, and reviewers cannot assess whether the computation is appropriate.

3. **(Major) Attack implementation is entirely absent.** The 9 attack types are listed by name only. The paper does not describe: what prompt templates are used for each attack, what "adaptive" means operationally (does the adversary optimize per-judge, per-panel, or just apply pre-defined templates?), what the adversary's query budget is, how ASR is computed (flipped from correct to incorrect? on what evaluation instances? how many?). The project memory reveals the actual implementation uses pre-defined prompt templates (3 templates per attack type) applied uniformly, with ASR = |clean_correct intersect attacked_incorrect| / |clean_correct|. This operational definition -- applying fixed templates and measuring which clean-correct items flip -- is much closer to an oracle evaluation than an "adaptive adversary." The gap between the claimed threat model ("adaptive adversary who observes panel composition and crafts attacks") and the likely implementation (fixed templates applied to each judge independently) is a significant concern.

4. **(Major) The diversity-capability confound (r=0.70) is inadequately addressed for the paper's claims.** The correlation between K_eff and eta_max is 0.70 with VIF = 2.96. While the paper reports residualized analysis and within-tier validation, the within-tier results have extremely low power: the large tier has only 20 panels, the small tier 10 panels, and the medium tier 4 panels. The within-tier K_eff significance (2/12 under clustered SE, in the base tier with 84 panels) is genuinely informative, but the paper does not adequately convey that the confound is the fundamental obstacle to interpreting K_eff's role. The partial correlation r(K_eff, ASR | eta_max) = 0.18 corresponds to only about 3% unique variance explained -- consistent with the ROADMAP's own assessment that "K_eff unique variance only 3%." This deserves more prominent discussion.

5. **(Moderate) The epsilon constant in the log-log specification is unspecified and potentially consequential.** The regression uses log(ASR + epsilon) but epsilon is never given. For near-zero ASR values (which are common for robust panels under weak attacks), the choice of epsilon can substantially affect both coefficient estimates and significance. More fundamentally, log-log OLS on a [0,1]-bounded outcome is non-standard; beta regression is the natural distributional choice. The paper mentions that beta regression gives eta_max 10/12 and K_eff 4/12 (versus OLS 11/12 and 8/12) but does not use it as the primary specification without justification. This is important because the beta regression K_eff count (4/12) is substantially higher than the OLS-then-clustered result (0/12), raising the question of whether the correction method and the outcome model interact in ways the paper does not explore.

6. **(Moderate) No multiple testing correction across conditions.** The paper reports significance counts (e.g., "eta_max significant in 5/12 conditions") but never applies FDR or Bonferroni correction across the 12 or 18 conditions. The project data mentions that Bonferroni gives eta_max 7/12 and K_eff 2/12, and FDR gives 8/12 and 3/12, but these numbers are not in the main results tables. Given that the paper's central argument rests on comparing significance counts between correction methods, the failure to also correct for multiple comparisons across conditions is an inconsistency.

7. **(Moderate) Panel size analysis (Table 8 in v5) conflates power with substance.** The claim that K_eff significance increases from 0/12 (K=3, 455 panels) to 2/12 (K=9, 5005 panels) could be entirely an artifact of the 11x increase in sample size. Meanwhile, SE inflation increases from 2.5x to 7.8x, meaning the non-independence problem gets dramatically worse at larger K. The paper presents these as robustness checks but does not disentangle the power increase from the substantive effect.

8. **(Minor) No figures in an empirical paper with 10+ tables is a serious presentation weakness.** Key patterns -- the BFT flip, the aggregation gradient, the K_eff vs eta_max scatter with Pareto frontier, the GAM taxonomy -- would be far more interpretable as visualizations. The project planning documents specify 15+ figures, none of which appear in the paper.

### Questions for Authors

1. What happens to the K_eff significance count if you cluster by model family (6 clusters) rather than individual model (15 clusters)? Family-level clustering would capture within-family correlation (which your own results show is substantial, r = 0.81) while increasing cluster count. Alternatively, have you considered the grouped jackknife variance estimator (Angrist & Pischke, 2009), which is designed for situations with few clusters?

2. The project's actual experimental data shows that the OLS R-squared under the log-log canonical specification is approximately 0.30 for majority vote, not the 0.62 reported in some versions of the paper. Can you clarify which specification produces the R-squared values reported? The discrepancy between 0.30 and 0.62 is large enough to affect interpretation.

3. What is the exact K_eff formula? The project memory documents at least two different formulas (empirical_keff_from_rho using all pairwise correlations and formula_keff using I_max), and the switch between them caused the wild bootstrap v1 results (9/12 K_eff significant) to be invalidated. Which formula is used in the final paper, and how sensitive are results to this choice?

4. For the partial-knowledge adversary experiment, you report that family-level knowledge retains 82% of full-knowledge attack efficiency. But this seems to imply the "full knowledge" adversary has access to each judge's exact vulnerability profile before attacking. Is this not an oracle rather than an adaptive adversary? In realistic settings, adversaries must discover vulnerabilities through interaction -- what would a genuine adaptive adversary look like, and would the diversity trap persist?

5. The Bayesian aggregation results (K_eff 3/4 significant negative under bootstrap, 4/12 significant under clustered SE) suggest that under the right aggregation rule, diversity actually becomes protective. This seems to undercut the paper's negative framing about diversity. Could you comment on why the paper emphasizes the null result for majority vote rather than the protective result for Bayesian aggregation?

### Missing References / Analyses

**Missing references** are a critical issue. The paper needs at minimum:
- Ensemble diversity theory: Kuncheva & Whitaker (2003), Krogh & Vedelsby (1995), Brown et al. (2005) on the diversity-accuracy tradeoff in ensembles
- LLM evaluation papers: Li et al. (2024, AlpacaEval), Dubois et al. (2024), Ye et al. (2024, Flask), Shankar et al. (2024, "Who Validates the Validators?")
- Crowdsourcing quality: Dawid & Skene (1979), Welinder et al. (2010)
- Adversarial ensemble robustness: Tramer et al. (2018), He et al. (2017)
- Multi-agent debate: Du et al. (2023), Chan et al. (2024)

**Missing analyses:**
- Power analysis for the K_eff null under 15 clusters
- Sensitivity analysis for the epsilon constant in log-log specification
- Proper FDR/Bonferroni correction reported alongside raw significance counts in all tables
- Effect size reporting (the project data shows K_eff practical delta ASR of only 1.3pp +/- 1.6pp across the K_eff IQR -- this tiny effect size should be prominently reported)
- Alternative clustering units (model family, panel-level) for robustness
- Mediation analysis: does Gini concentration formally mediate the K_eff -> ASR path?

### Soundness: 3/5
The non-independence correction framework is appropriate in principle, and the comparison of four correction methods is rigorous. However, the 15-cluster limitation is never discussed and may produce over-conservative inference, making the K_eff null unreliable. The attack implementation is unspecified, making it impossible to evaluate whether the adversary model matches the claimed adaptive threat model. The log-log specification with unspecified epsilon is a secondary concern. The eta_max dominance finding is robust across corrections, which anchors the soundness score at 3 rather than lower.

### Excitement: 3/5
The research question is timely and important. The methodological contribution (non-independence correction for combinatorial evaluation designs) is genuinely useful. However, the substantive finding -- that individual judge strength matters more than panel diversity -- is largely predictable from classical ensemble theory (bias-variance decomposition). The GAM taxonomy and the aggregation gradient are the most exciting specific findings, but they receive compressed treatment. The practical recommendation ("use strong models") is somewhat obvious. The max(K_eff) < random result is surprising and valuable but is a relatively small part of the paper.

### Reproducibility: 2/5
The K_eff formula is absent. Attack implementations are absent. Model versions and temperatures are not listed. The epsilon constant is unspecified. The project data reveals that different K_eff formulas produced dramatically different results (bootstrap v1 with wrong formula: 9/12 significant; bootstrap v2 with corrected formula: 1/12 significant), making the formula specification critical for reproducibility. No code or data availability statement is provided.

### Overall Assessment: 3.0 (Findings)

The paper addresses an important question with impressive experimental breadth (15 models, 455 panels, 9 attacks, 3 benchmarks, 4 corrections, 4 aggregation rules, 4 panel sizes, 3 adversary knowledge levels). The eta_max dominance finding survives multiple robustness checks and is a solid empirical contribution. The methodological finding about non-independence inflation in combinatorial evaluation designs has general applicability. The BFT random-fault contrast and the aggregation gradient are well-designed experiments with non-obvious results.

However, the paper cannot reach Main conference level (4.0) for several reasons: (1) the 15-cluster limitation for clustered inference is never acknowledged and may produce a false K_eff null, directly undermining the central claim; (2) critical reproducibility gaps (no K_eff formula, no attack details, no model specifics); (3) a thin 7-reference bibliography for a paper spanning LLM evaluation, adversarial robustness, and distributed systems; (4) no figures in a heavily empirical paper; (5) limited novelty relative to classical ensemble diversity theory, which the paper does not engage with.

With substantial revision -- expanded related work (25+ references), the K_eff formula, attack implementation details, figures, a power analysis for the 15-cluster limitation, and honest discussion of the K_eff practical effect size (approximately 1.3 percentage points) -- this could become a competitive Main submission (3.5-4.0) in a subsequent cycle.

### Confidence: 4/5
I have carefully examined the paper, cross-referenced it against the underlying experimental records (memory.md, ROADMAP.md, experiment_data.json, paper_framing.md), and identified specific numerical and methodological concerns. I am confident in the non-independence concern (15-cluster limitation) and the reproducibility gaps. I am less certain about the precise impact of alternative clustering strategies on the K_eff significance count, which would require re-analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88488133-34c7-410f-8e0c-5e41360771f2",
  "isSidechain": true,
  "agentId": "abcc09248c70fce74",
  "requestId": "req_011CbJSh5LH7gwmZi1X95t6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "443e3e0b-464b-44dc-973e-adb57f3ded2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "e22ae69a-98d0-4e8b-ab2b-d12049c8f59c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUJj6BtN4c29dasxZo4Si5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 101911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7304,
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
