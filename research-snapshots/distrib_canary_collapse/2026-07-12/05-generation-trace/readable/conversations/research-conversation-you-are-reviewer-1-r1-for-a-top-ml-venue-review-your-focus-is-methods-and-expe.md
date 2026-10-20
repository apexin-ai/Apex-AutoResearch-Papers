# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the following paper

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9e37490c50c6f87d.jsonl`
- **Structured JSON:** [`5a6bd1fd04156bf8c895.json`](../../sessions/5a/5a6bd1fd04156bf8c895.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

49 recorded events

### User

_source line 1 · 2026-05-14T19:21:31.725Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the following paper thoroughly and produce a structured review.

**Paper**: "Mapping the Predictability Boundary of Model Collapse: Calibration Canaries and Regime-Dependent Early Warning in Iterative Synthetic Data Training"

**Paper content summary** (7 pages):

The paper studies iterative self-consuming (SC) training where models train on their own synthetic outputs across generations, leading to "model collapse." The core contribution is a systematic framework using Toda-Yamamoto (TY) panel temporal precedence analysis to identify which metrics ("canaries") predict collapse and under what contamination regimes.

**Key claims:**
1. ECE and token entropy reliably lead diversity collapse by 1–2 generations (p < 0.005, effect size r > 0.88)
2. Predictability is regime-dependent: canary→perplexity lead exists only at α=0.25, vanishes at higher contamination
3. TY overturns 20% of naive correlation-based associations
4. A proof-of-concept CRS intervention preserves 42% of diversity at α=0.75

**Experimental setup:**
- Pythia-410M (primary) and Pythia-1.4B (scale check)
- WikiText-103 and C4 datasets
- α ∈ {0.25, 0.50, 0.75, 1.0} contamination ratios
- 3-4 random seeds, 10-20 generations
- Four canary families: ECE, token entropy, effective rank, self-BLEU
- Targets: distinct-1/2 (diversity), perplexity

**Tables in the paper:**
- Table 1: MVP lead-lag (α=1.0, max_lag=7) — ECE→distinct_1: lead=1, p=0.001, 4/4 seeds, r=0.94; token_entropy→distinct_1: lead=2, p=0.003, 3/4 seeds, r=0.91; both→perplexity: lead=0, not significant; effective_rank and self_BLEU: not significant
- Table 2: α-sweep results — canary→diversity lead decreases from 2 gen (α=0.25) to 1 gen (α≥0.50), always significant; canary→perplexity lead=1 only at α=0.25 (marginal p≈0.04, 2/3 seeds), lead=0 elsewhere
- Table 3: Method comparison — Naive Pearson: 71/96 significant (74%), TY overturns 19 (20%); Differenced XCorr: 52/96; Threshold 2σ: 58/96; TY: 54/96
- Table 4: Overturned associations — effective_rank and self_BLEU pairs, plus ECE/token_entropy→perplexity at α=0.50
- Table 5: C4 vs WikiText at α=0.50 — canary ranking preserved, lead=1, effect_r=0.88 vs 0.90
- Table 6: Scale comparison 410M vs 1.4B at α=0.50 — lead preserved at 1 gen, effect_r drops to 0.85, seeds_sig=2/3
- Table 7: Extended run 20 gen at α=1.0 — canary→diversity lead=2 at max_lag=10, canary→perplexity stays 0
- Table 8: CRS intervention at α=0.75 — no-intervention distinct_1=0.083, CRS=0.118 (42.2% preserved), oracle α=0.50=0.108
- Table 9: Accumulate vs Replace at α=0.50 — accumulate slows collapse 40%, canary lead preserved at 1 gen, effect_r=0.82

**Experiment design reference (from review_context.yaml):**
The paper was expected to cover 8 experiments (plan_001 through plan_008). All 8 are represented in the paper:
- plan_001: α-sweep (Section 4.2, Table 2) ✓
- plan_002: Naive vs TY ablation (Section 4.3, Tables 3-4) ✓
- plan_003: MVP formalization max_lag=7 (Section 4.1, Table 1) ✓
- plan_004: C4 cross-domain (Section 4.4, Table 5) ✓
- plan_005: Pythia-1.4B scale check (Section 4.5, Table 6) ✓
- plan_006: Extended 20 gen run (Section 4.6, Table 7) ✓
- plan_007: CRS intervention (Section 4.7, Table 8) ✓
- plan_008: Accumulate vs Replace ablation (Section 4.8, Table 9) ✓

**Your review should cover:**

1. **Methodological soundness**: Is the TY approach well-justified? Are there issues with the statistical methodology? Consider: sample sizes (only 10-20 time points per series), degrees of freedom with max_lag=7 or 10 on 10-point series, multiple comparisons correction, the "≥2/3 seeds" threshold.

2. **Experimental rigor**: Seed counts (3-4), generation counts (10-20), model scale coverage, dataset coverage. Are the experiments sufficient to support the claims?

3. **Results interpretation**: Are claims appropriately calibrated to evidence strength? Any overclaims or underclaims?

4. **Reproducibility**: Is enough detail provided? Any missing hyperparameters or procedural details?

5. **Weaknesses and missing experiments**: What's missing that would strengthen the paper?

**Output format** (use exactly this structure):

```
## R1: Methods & Experiments

### Summary
[2-3 sentences]

### Strengths
- S1: ...
- S2: ...
- S3: ...

### Weaknesses
- W1: ...
- W2: ...
- W3: ...
- W4: ...

### Questions for Authors
- Q1: ...
- Q2: ...
- Q3: ...

### Missing Experiments / Suggestions
- ...

### Soundness Score: [1-4] (1=poor, 4=excellent)
### Presentation Score: [1-4]
### Overall Score: [1-6] (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)
### Confidence: [1-5]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "01aa1cdb-8b3a-426e-9176-386e787e2713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T19:21:31.729Z_

```json
{
  "parentUuid": "01aa1cdb-8b3a-426e-9176-386e787e2713",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
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
  "uuid": "b960ded0-e75f-4dd7-af5f-db47a1c50d1a",
  "timestamp": "2026-05-14T19:21:31.729Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T19:21:34.919Z_



I'll start by reading the actual paper and any supporting files to ground my review in the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b960ded0-e75f-4dd7-af5f-db47a1c50d1a",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DDUg4FTLFDg5JMREq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a20f52bb-f8b1-4948-a2b5-ecfc955df810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01144CuRvgSkpL6SWoExZ9wB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15701,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15701,
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

_source line 4 · 2026-05-14T19:21:36.196Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EXRiKX8Q4aY8yUUk3XZMdZ`</summary>

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
  "parentUuid": "a20f52bb-f8b1-4948-a2b5-ecfc955df810",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DDUg4FTLFDg5JMREq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0862356-cbbd-43ab-96ab-4b67ccfbf07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01144CuRvgSkpL6SWoExZ9wB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15701,
      "cache_read_input_tokens": 0,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15701
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 127,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15701,
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

_source line 5 · 2026-05-14T19:21:36.200Z_

<details><summary>↩ Tool result · `toolu_01EXRiKX8Q4aY8yUUk3XZMdZ`</summary>

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
  "parentUuid": "d0862356-cbbd-43ab-96ab-4b67ccfbf07b",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "ae64cc16-ce74-409b-8c29-f4c6bc8a1f6c",
  "sourceToolAssistantUUID": "d0862356-cbbd-43ab-96ab-4b67ccfbf07b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T19:21:38.909Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01YLbYnNibB4DkUJAuF15noY`</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae64cc16-ce74-409b-8c29-f4c6bc8a1f6c",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DYrzJRWyTkayyjfVF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "021f178c-f34e-4992-ac80-55229cfbfb3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gs6aGnZ41eSqc1qUZQy1Fo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 7 · 2026-05-14T19:21:38.954Z_

<details><summary>↩ Tool result · `toolu_01YLbYnNibB4DkUJAuF15noY`</summary>

```text
{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (14 个)\n\n- **mvp_v4_rep44**: DONE (success) — \n- **alpha_sweep_a025_s42**: PREPARING — \n- **alpha_sweep_a000_s42**: PREPARING — \n- **mvp_rep44**: PREPARING — \n- **mvp_v4_rep45**: DONE (success) — \n- **mvp_v4_rep43**: DONE (success) — \n- **mvp_v4_rep42**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_v2_rep44**: PREPARING — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- mvp_v2_rep44（准备中）\n- mvp_rep44（准备中）\n\n## 近期结论\n- **mvp_v4_rep45** (success): —\n- **mvp_v4_rep44** (failed): —\n- **mvp_v4_rep43** (success): —\n\n## 趋势\n成功 3 / 负向 0 / 失败 3 / 共 10\n累计 GPU: 4.2h\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-19828: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_rep42: 已被终止 — unknown\n- mvp_rep43: 已被终止 — unknown\n- mvp_v2_rep42: 已被终止 — unknown\n- mvp_v2_rep43: 已被终止 — unknown\n- mvp_v3_rep42: 训练失败 — unknown\n- mvp_v3_rep43: 训练失败 — unknown\n- mvp_v4_rep44: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "021f178c-f34e-4992-ac80-55229cfbfb3c",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "19d29b53-6bc6-4319-832d-229e6aa3d486",
  "sourceToolAssistantUUID": "021f178c-f34e-4992-ac80-55229cfbfb3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T19:21:39.600Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EpX3EqBJS9g1JAwcT6HX3A`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19d29b53-6bc6-4319-832d-229e6aa3d486",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DYrzJRWyTkayyjfVF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52cd957d-b310-42d9-9b7b-b1f20845118e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gs6aGnZ41eSqc1qUZQy1Fo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15701,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 15701,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1449,
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

_source line 9 · 2026-05-14T19:21:39.607Z_

<details><summary>↩ Tool result · `toolu_01EpX3EqBJS9g1JAwcT6HX3A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- mvp_v2_rep44（准备中）\\n- mvp_rep44（准备中）\\n\\n## 近期结论\\n- **mvp_v4_rep45** (success): —\\n- **mvp_v4_rep44** (failed): —\\n- **mvp_v4_rep43** (success): —\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 3 / 共 10\\n累计 GPU: 4.2h\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19828: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_rep42: 已被终止 — unknown\\n- mvp_rep43: 已被终止 — unknown\\n- mvp_v2_rep42: 已被终止 — unknown\\n- mvp_v2_rep43: 已被终止 — unknown\\n- mvp_v3_rep42: 训练失败 — unknown\\n- mvp_v3_rep43: 训练失败 — unknown\\n- mvp_v4_rep44: 训练失败 — unknown\\n\", \"total_chars\": 560, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52cd957d-b310-42d9-9b7b-b1f20845118e",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "041753af-3108-4532-ab8c-db2e0bd7e266",
  "sourceToolAssistantUUID": "52cd957d-b310-42d9-9b7b-b1f20845118e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T19:21:42.497Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FHm1LwAzVuhudNWQHkEHv9`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "041753af-3108-4532-ab8c-db2e0bd7e266",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DoLt3shMvxhUQmZTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2b6f1ab-2857-402f-895b-c6f22b9e50f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQbLxinkb68qyhCZ6uHk6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 11 · 2026-05-14T19:21:42.504Z_

<details><summary>↩ Tool result · `toolu_01FHm1LwAzVuhudNWQHkEHv9`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'distrib_canary_collapse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2b6f1ab-2857-402f-895b-c6f22b9e50f3",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "3cf3b95a-4317-4e29-8d60-45d673839b64",
  "sourceToolAssistantUUID": "d2b6f1ab-2857-402f-895b-c6f22b9e50f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T19:21:43.010Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TXhTzF3D8t6rgUcC7uM2Xb`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cf3b95a-4317-4e29-8d60-45d673839b64",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DoLt3shMvxhUQmZTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e0a0b5f-6343-47b4-96fe-b9d2280e189e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQbLxinkb68qyhCZ6uHk6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 13 · 2026-05-14T19:21:43.017Z_

<details><summary>↩ Tool result · `toolu_01TXhTzF3D8t6rgUcC7uM2Xb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'distrib_canary_collapse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e0a0b5f-6343-47b4-96fe-b9d2280e189e",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "cb103b0e-1a7b-4f00-a428-856c152d543d",
  "sourceToolAssistantUUID": "7e0a0b5f-6343-47b4-96fe-b9d2280e189e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T19:21:44.084Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019KAELouH1cJMX58rzpUDVW`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb103b0e-1a7b-4f00-a428-856c152d543d",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DoLt3shMvxhUQmZTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52e26325-8d6e-404b-820c-b05d67c84d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQbLxinkb68qyhCZ6uHk6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 15 · 2026-05-14T19:21:44.095Z_

<details><summary>↩ Tool result · `toolu_019KAELouH1cJMX58rzpUDVW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/decisions.yaml\", \"content\": \"_next_id: 11\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 设计: Pythia-410M × WikiText-103 × 100% SC × 10 gen × 3 reps，验证 canary\\n    时序领先性'\\n  rationale: 100% SC 是最激进的 collapse 条件（理论预测必然退化），如果在此条件下没有任何 canary 指标领先 downstream，项目前提不成立。3\\n    reps × 10 gen 给出足够时间点做 cross-correlation。计算量 ~9 H100-hours，极低风险。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:26 UTC\\n  summary: MVP ECE 用 next-token calibration，SC 协议用 full replacement，effective rank\\n    用模型自身 embedding\\n  rationale: 'Reviewer warning 要求澄清 3 个操作化定义。ECE: next-token calibration 是 LM 原生度量、零额外成本，与\\n    Du et al. 的对比留到全量阶段加 downstream task ECE。SC: full replacement 是最大 feedback amplification\\n    (Truong & Truong Class 1)，collapse 信号最强，适合 MVP 压力测试。Effective rank: 模型自身 embedding\\n    与 SIGMA 一致，零额外依赖。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:27 UTC\\n  summary: 首选 AAAI 2027 (~Aug 2026)，May 25 ARR 不可行，后续 ARR cycle 备选\\n  rationale: 项目 2026-05-14 立项，无服务器无代码，11 天内无法完成 MVP + 全量实验 + 论文。AAAI 2027 给 ~2.5 个月，充分覆盖\\n    500-600 H100-hours 的实验量和论文写作。后续 ARR cycle (Jul/Aug) 也在射程内。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-14 05:36 UTC\\n  summary: 'MVP 参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000 (4 epochs/gen)'\\n  rationale: Reviewer 发现原配置下 40 epochs/gen 在 1000 samples 上严重过拟合，模型可能 1-2 代即骤然击穿，所有指标同时崩溃，无法观察\\n    lead-lag 时序结构。修改后 4 epochs/gen 接近文献实践，collapse 逐渐发展，给 cross-correlation 分析留出足够时间点。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D005\\n  date: 2026-05-14 08:39 UTC\\n  summary: MVP 中期决策：不重启实验，MAUVE demote 为 supplementary，等完整 10-gen 数据再判断 collapse 速度和\\n    lead-lag\\n  rationale: MAUVE 基线 0.034 触发 evaluation criteria §4 floor effect 规则。Gen 0→1 跳变大是\\\"未训练→首次训练\\\"的固有落差，后续\\n    gen 的增量变化才是分析目标。100% SC 如果确认无 lead-lag，null result 符合 Truong & Truong 一阶相变理论——是有意义的发现，不是实验失败。重启只会浪费更多\\n    GPU 时间。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 17:37 UTC\\n  summary: 论文 framing 采用 \\\"delineating predictability boundaries\\\" 而非 \\\"universal canary\\\"\\n  rationale: 2-seed 预分析显示 canary 仅 lead diversity (distinct_n) 不 lead perplexity。ECE→perplexity\\n    甚至反向 (lag=+5)。\\\"predictability boundary\\\" framing 将 null result 转化为 evidence：100%\\n    SC 是同步崩溃 regime（不可预测），较低 α 可能出现渐进退化（可预测）。此 framing 对 null result 天然鲁棒，与 Truong\\n    & Truong 相变理论自然对接，reviewer 攻击面最小。Reviewer 独立预审认同此方向为最强 framing。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: canary→distinct_n SIGNIFICANT, canary→perplexity NO LEAD\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: same pattern confirmed\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-14 17:37 UTC\\n  summary: Post-MVP 实验优先级：α-sweep >> 方法 ablation > C4 数据集 > 规模验证\\n  rationale: α-sweep (25/50/75%) 是唯一能回答\\\"canary 在温和 regime 下是否 lead perplexity\\\"的实验，决定论文从\\n    diversity-only predictor 到 regime-dependent general predictor 的 claim 升级。方法 ablation\\n    零 GPU 成本、高 ROI（回答 reviewer 方法论质疑）。C4 堵 domain-specific 攻击。规模验证优先级最低（Pythia 家族共享架构，只测一个维度）。Reviewer\\n    预审排序一致。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-14 17:37 UTC\\n  summary: distinct_3 lead-lag 结果待 4-seed 确认，如 lag 仍双峰则降级 inconclusive，主文只报 distinct_1/distinct_2\\n  rationale: distinct_3 的 lag 估计跨 seed 不稳定（lag=-5 vs lag=-1，lag_std=2.0）。lag=-5 触及\\n    max_lag 边界，N=11 下只剩 6 点做相关，统计意义极弱，可能是边界效应伪信号。distinct_1/distinct_2 的 lag 跨 seed\\n    完全一致（lag_std=0），足以支撑核心 claim。Reviewer 建议 distinct_3 放 supplementary 并注明不稳定性。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: distinct_3 lag=-5\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: distinct_3 lag=-1\\n  depends_on:\\n  - D006\\n- id: D009\\n  date: 2026-05-14 18:59 UTC\\n  summary: MVP 4-seed STRONG PASS，进入 Research 阶段全面实验\\n  rationale: 4/4 seed 一致确认 token_entropy 和 ECE 领先 diversity 指标 1-2 代（p<0.004）。核心发现：canary\\n    只领先 diversity collapse 不领先 perplexity degradation，这定义了 narrative 方向。plan_006 升级\\n    P0 以解决 max_lag 截断疑虑。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep44\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep45\\n    role: evidence\\n    result: success\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 19:10 UTC\\n  summary: plan_003 重分析修正 perplexity 通道叙述：WEAK LEAD 非断裂，ECE 反向因果，维持 D008 distinct_3\\n    降级\\n  rationale: max_lag=7 重分析三个关键发现：(1) token_entropy→perplexity lag=-5 是真实峰值非截断伪影，但\\n    p=0.058-0.12 在 N=11 下不显著——\\\"通道断裂\\\"改为\\\"弱信号、效力不足\\\"；(2) ECE→perplexity 呈反向因果(lag=+4/+5,\\n    p<0.01)，两个 canary 家族在 perplexity 通道方向相反，论文必须讨论；(3) distinct_3 虽升 SIGNIFICANT 但\\n    lag_std>1.5（双峰），维持 D008 降级。plan_006(20-gen, N=21) 成为 framing 关键判定实验。\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: evidence\\n    result: max_lag=7 重分析完成，核心 lead 稳固，perplexity 通道发现新细节\\n  depends_on:\\n  - D008\\n  - D009\\n\", \"total_chars\": 4841, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52e26325-8d6e-404b-820c-b05d67c84d2b",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "13abfaa5-8291-4f32-8795-8601da4877e9",
  "sourceToolAssistantUUID": "52e26325-8d6e-404b-820c-b05d67c84d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T19:21:44.425Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BsNyf49nRU5ptUYFkDuLiw`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13abfaa5-8291-4f32-8795-8601da4877e9",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DoLt3shMvxhUQmZTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dfc3920-36a3-4026-a0a8-5be765c1b20e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQbLxinkb68qyhCZ6uHk6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 17 · 2026-05-14T19:21:44.435Z_

<details><summary>↩ Tool result · `toolu_01BsNyf49nRU5ptUYFkDuLiw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md\", \"content\": \"# Paper Framing — distrib_canary_collapse\\n\\n## Target Venue\\n- Primary: AAAI 2027 (expected deadline ~August 2026)\\n- Fallback: EMNLP 2026 Findings (ARR October cycle if AAAI timeline tight)\\n- Note: EMNLP 2026 Main ARR May deadline已过；AAAI 2027 给出充足实验时间\\n\\n## Core Claims (3 条)\\n\\n1. **Canary→Diversity Lead**: 在迭代合成数据训练中，ECE 和 token entropy 作为廉价 canary 指标，稳定领先 diversity 退化（distinct_1/2）1-2 代——提供可量化的早期预警窗口。\\n2. **Regime-Dependent Predictability**: 可预测性取决于 contamination regime——100% SC 下 token_entropy→perplexity 存在一致的 lag=-5 弱信号（4/4 seed, p=0.058-0.12）但 N=11 统计效力不足，ECE→perplexity 则呈反向因果（perplexity 领先 ECE）。低 α 条件下 canary lead time 有望扩展。Predictability phase diagram 划定可预测/不可预测边界。\\n3. **Methodological Rigor**: 朴素相关分析在非平稳训练指标上产生伪回归；Toda-Yamamoto panel temporal precedence 提供统计严谨的 lead-lag 量化，方法论 ablation 量化伪显著关联被推翻的比例。\\n\\n## Story Spine\\n\\n- **Problem**: Model collapse 的在线监控工具已存在（SIGMA 谱监控、DCES 反应式干预），但没有工作系统性回答\\\"哪些指标最早预测崩溃、领先多久、在什么 regime 下有效\\\"。Du et al. 非正式观察到 ECE 领先 accuracy，但仅限单指标对、1-3 代、无统计检验。\\n\\n- **Existing approaches & their gaps**: SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足（无正式 time-series 检验、无多家族对比）；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效——但仅限特定 regime 和特定指标族。\\n\\n- **Our framing**: 我们不是提出\\\"通用 canary\\\"，而是**系统性映射可预测性的边界**——哪些 collapse 维度可预测（diversity）、哪些不可预测（perplexity in extreme regime）、在什么 contamination 条件下、用什么统计方法。Null results（canary 不 lead perplexity）不是失败，而是 phase diagram 中的一个 boundary data point。\\n\\n- **Headline result template**: \\\"ECE and token entropy predict diversity collapse 1-2 generations ahead (|r|>0.99, p<0.001, 4/4 seeds) in iterative synthetic data training, while a predictability phase diagram reveals regime-dependent boundaries where canary signals exist vs. where synchronous collapse precludes early warning.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n| Concern | Response Strategy | Required Experiment |\\n|---------|-------------------|---------------------|\\n| \\\"Canary 不预测 perplexity，实用价值有限\\\" | Framing 为 regime-dependent：100% SC 下 token_entropy 有 lag=-5 弱信号（plan_006 20-gen 验证）；α-sweep 展示低 α 下是否变显著 | α-sweep (P0) + plan_006 (P0) |\\n| \\\"ECE 和 token_entropy 对 perplexity 方向相反？\\\" | 诚实报告不对称性：token_entropy 捕捉分布收窄前驱信号（lead），ECE 作为 calibration 指标反映后期适应效应（lag）。两者覆盖 collapse 不同阶段 | 已有 MVP+plan_003 数据 |\\n| \\\"只在 Pythia-410M 上验证，scale 泛化？\\\" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |\\n| \\\"WikiText-103 单一数据集\\\" | C4 cross-domain validation | domain-transfer (P1) |\\n| \\\"为什么不用简单相关分析？\\\" | 方法 ablation：naive corr vs Toda-Yamamoto，量化伪显著比例 | method-ablation (P0, 零 GPU) |\\n| \\\"4 个 canary 中 2 个失败，选择偏差？\\\" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |\\n| \\\"Intervention 实验缺失\\\" | CRS-triggered vs reactive vs no-intervention 对比 | intervention (P2) |\\n\\n## Venue Fit\\n\\nAAAI 2027 优势：\\n- ML 方法论 track 接受 empirical analysis + 统计方法论贡献\\n- 不要求 SOTA，接受 systematic study with novel methodology\\n- Phase diagram / regime boundary 概念在 AAAI 偏理论的审稿人中有吸引力\\n\\n风险：\\n- 如果被认为\\\"只是 empirical study 没有算法贡献\\\"→ 补 CRS + intervention 提升 method 贡献\\n- 模型规模偏小（Pythia-410M/1.4B）→ 诚实标注 limitation + scaling trend\\n\\n## Key Narrative Constraints (from MVP + plan_003)\\n\\n1. **不能 claim \\\"canary predicts model collapse\\\"** — 只能 claim \\\"canary predicts diversity collapse\\\"。token_entropy→perplexity 在 100% SC 下存在一致的 lag=-5 弱信号（4/4 seed, p=0.058-0.12），但 N=11 统计效力不足——用\\\"统计不显著的弱信号\\\"而非\\\"通道断裂\\\"。plan_006（20-gen, N=21）是判定实验\\n2. **ECE→perplexity 呈反向因果** — perplexity 领先 ECE 4-5 代（lag=+4/+5, p<0.01）。与 token_entropy→perplexity（canary 领先）方向相反。论文必须讨论两个 canary 家族在 perplexity 通道上的不对称性\\n3. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果\\n4. **distinct_3 的 lead time 不如 distinct_1/2 可靠** — max_lag=7 下升为 SIGNIFICANT 但 lag_std>1.5（双峰：seed 42 总是 -5，其余 -1/-2），维持 D008 降级策略，主文聚焦 distinct_1/2\\n5. **max_lag=7 确认核心 lead 无截断** — token_entropy→distinct_1 lag=-1（std=0.0）、ECE→distinct_2 lag=-1（std=0.0）在 max_lag=5/7 下完全一致。token_entropy→perplexity lag=-5 是真实峰值非截断伪影\\n\", \"total_chars\": 3872, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dfc3920-36a3-4026-a0a8-5be765c1b20e",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "0e6d5249-9791-4ced-b5d2-639ab406acab",
  "sourceToolAssistantUUID": "2dfc3920-36a3-4026-a0a8-5be765c1b20e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T19:21:45.134Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0186NZgiTz14ADzymHpYqBup`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e6d5249-9791-4ced-b5d2-639ab406acab",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31DoLt3shMvxhUQmZTg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "600519d0-b9e9-4277-8512-46b97274a9ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQbLxinkb68qyhCZ6uHk6p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17150,
      "output_tokens": 482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1454
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 482,
          "cache_read_input_tokens": 17150,
          "cache_creation_input_tokens": 1454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1454,
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

_source line 19 · 2026-05-14T19:21:45.146Z_

<details><summary>↩ Tool result · `toolu_0186NZgiTz14ADzymHpYqBup`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ROADMAP.md\", \"content\": \"# distrib_canary_collapse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 19:09 UTC | 更新原因: plan_003 重分析结论：修正 perplexity 通道叙述（WEAK LEAD + ECE 反向因果），plan_006 升为 framing 判定实验\\n\\n## 核心方向\\n系统性映射迭代合成数据训练中 canary 指标的**可预测性边界**——哪些 collapse 维度可预测、用什么 canary、在什么 contamination regime 下。详见 paper_framing.md。\\n\\n**Refined narrative (D009→D010)**: Canary 指标（ECE/token_entropy）预测的是 diversity collapse（distinct_n 退化）。Perplexity 通道更复杂：token_entropy 对 perplexity 有一致的 lag=-5 弱信号（4/4 seed, p>0.05, N=11 效力不足），ECE 对 perplexity 呈反向因果（perplexity 领先 ECE）。plan_006（20-gen）是判定 token_entropy→perplexity 是否真实的关键实验。\\n\\n## 当前进展\\n- **阶段**: Research（MVP STRONG PASS + plan_003 max_lag=7 重分析完成）\\n- **MVP 核心发现**: ECE/token_entropy 领先 distinct_1/2 达 1-2 代（|r|>0.99, p<0.004, lag std=0.0）\\n- **plan_003 新发现**: token_entropy→perplexity lag=-5 是真实峰值（非截断），但 WEAK LEAD；ECE→perplexity 反向因果（lag=+4/+5）\\n- **排除指标**: self_bleu（方向不一致）、effective_rank（non-monotonic）、MAUVE（floor effect）\\n- **Framing**: \\\"Delineating Predictability Boundaries\\\"（D006），perplexity 通道叙述已修正（D010）\\n- **Target**: AAAI 2027（~Aug 2026 deadline）\\n- **Dream**: dream_20260514T184925 pending（full review mode）\\n- **代码部署**: ✅ α-sweep + accumulate + exit-code + 子采样 fix 已部署\\n- **累计 GPU**: 4.2h\\n\\n## 近期任务\\n- [ ] 启动 plan_001 α-sweep (P0): α∈{0.0, 0.25, 0.50, 0.75} × 3 seeds × 10 gen\\n- [ ] 启动 plan_006 extended 20-gen (P0): α=1.0 × 2 seeds × max_lag=10（**framing 判定实验**：token_entropy→perplexity 是否在 N=21 下变显著）\\n- [ ] 等 Dream 回调，按结果调整 framing/plan\\n- [ ] plan_002: 方法论 ablation（零 GPU，依赖 plan_001 数据）\\n\\n## GPU 预算\\n- **分配**: 2× RTX PRO 6000 Blackwell 96GB (westd-19828, cuda:0/cuda:1)\\n- **P0 估算**: ~48h（α-sweep 40h + extended run 8h）\\n- **P1 估算**: ~34h（C4 验证 10h + 1.4B spot-check 24h）\\n- **P2 估算**: ~20h（intervention 10h + accumulate ablation 10h）\\n- **总计**: ~102h，双卡 ~51h/卡（~2.1 天连续跑）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D010 | 2026-05-14 | plan_003 重分析修正 perplexity 通道叙述：WEAK LEAD 非断裂，ECE 反 | plan_003 |\\n| D009 | 2026-05-14 | MVP 4-seed STRONG PASS，进入 Research 阶段全面实验 | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep44, mvp_v4_rep45 |\\n| D008 | 2026-05-14 | distinct_3 lead-lag 结果待 4-seed 确认，如 lag 仍双峰则降级 inc | mvp_v4_rep42, mvp_v4_rep43 |\\n| D007 | 2026-05-14 | Post-MVP 实验优先级：α-sweep >> 方法 ablation > C4 数据集 > 规 | — |\\n| D006 | 2026-05-14 | 论文 framing 采用 \\\"delineating predictability boundari | mvp_v4_rep42, mvp_v4_rep43 |\\n| D005 | 2026-05-14 | MVP 中期决策：不重启实验，MAUVE demote 为 supplementary，等完整 10 | — |\\n| D004 | 2026-05-14 | MVP 参数修复: n_prompts 1000→5000, steps_per_gen 10000 | — |\\n| D003 | 2026-05-14 | 首选 AAAI 2027 (~Aug 2026)，May 25 ARR 不可行，后续 ARR cyc | — |\\n| D002 | 2026-05-14 | MVP ECE 用 next-token calibration，SC 协议用 full repla | — |\\n| D001 | 2026-05-14 | MVP 设计: Pythia-410M × WikiText-103 × 100% SC × 10  | — |\\n\\n\", \"total_chars\": 2736, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "600519d0-b9e9-4277-8512-46b97274a9ec",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "4d6f1c21-53d4-437f-af9b-77413bec809c",
  "sourceToolAssistantUUID": "600519d0-b9e9-4277-8512-46b97274a9ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-14T19:21:53.496Z_

Now let me read the actual paper and experimental artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d6f1c21-53d4-437f-af9b-77413bec809c",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31ED1vB7n6nhgqLsmEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95c4eade-abaf-4a05-be21-284c070e50bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DisjSSzsfhkQvRByqksfE2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 18604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7588,
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

_source line 21 · 2026-05-14T19:21:55.447Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PRmNAQASpaqLGQyy8TgwEp`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95c4eade-abaf-4a05-be21-284c070e50bc",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31ED1vB7n6nhgqLsmEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9e042bb-e731-4ff1-a025-b9aef6c0ebf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DisjSSzsfhkQvRByqksfE2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 18604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7588,
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

_source line 22 · 2026-05-14T19:21:55.468Z_

<details><summary>↩ Tool result · `toolu_01PRmNAQASpaqLGQyy8TgwEp`</summary>

```text
artifacts/dream_reports/dream_20260514T184925/best/paper.tex
artifacts/dream_reports/dream_20260514T184925/median/paper.tex
artifacts/dream_reports/dream_20260514T184925/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9e042bb-e731-4ff1-a025-b9aef6c0ebf3",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "7715cceb-9f60-4d0b-b674-4d84c5667c5f",
  "sourceToolAssistantUUID": "a9e042bb-e731-4ff1-a025-b9aef6c0ebf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T19:21:55.998Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DohxtQFyBroUMY5J2aKjGN`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7715cceb-9f60-4d0b-b674-4d84c5667c5f",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31ED1vB7n6nhgqLsmEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d99c4743-982c-42f5-bde3-a70e8c7ed39f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DisjSSzsfhkQvRByqksfE2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 18604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7588,
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

_source line 24 · 2026-05-14T19:21:56.011Z_

<details><summary>↩ Tool result · `toolu_01DohxtQFyBroUMY5J2aKjGN`</summary>

```text
artifacts/dream_reports/dream_20260514T184925/best/paper.pdf
artifacts/dream_reports/dream_20260514T184925/median/paper.pdf
artifacts/dream_reports/dream_20260514T184925/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d99c4743-982c-42f5-bde3-a70e8c7ed39f",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "b6fcdd10-3bdf-4402-9268-79fe0aebe8d7",
  "sourceToolAssistantUUID": "d99c4743-982c-42f5-bde3-a70e8c7ed39f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T19:21:56.466Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013b28KLxdHWVjbeWkFw2ZtQ`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6fcdd10-3bdf-4402-9268-79fe0aebe8d7",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31ED1vB7n6nhgqLsmEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1518dcf-17fb-4607-a7b9-6814cf8cec4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DisjSSzsfhkQvRByqksfE2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 18604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7588,
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

_source line 26 · 2026-05-14T19:21:56.481Z_

<details><summary>↩ Tool result · `toolu_013b28KLxdHWVjbeWkFw2ZtQ`</summary>

```text
artifacts/_project/intermediate/iterative_train.py
artifacts/prepare_data.py
artifacts/metrics.py
artifacts/analyze_mvp.py
artifacts/iterative_train.py
artifacts/test_alpha_sweep.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1518dcf-17fb-4607-a7b9-6814cf8cec4b",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "dd931682-cc8e-4852-941a-a3709d111334",
  "sourceToolAssistantUUID": "f1518dcf-17fb-4607-a7b9-6814cf8cec4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T19:21:57.105Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NmGrFktQmqtLtHeixn9nDa`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd931682-cc8e-4852-941a-a3709d111334",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31ED1vB7n6nhgqLsmEZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf0b3aae-d9a6-4b53-8a20-1112b0afa5e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DisjSSzsfhkQvRByqksfE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 18604,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 357,
          "cache_read_input_tokens": 18604,
          "cache_creation_input_tokens": 7588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7588,
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

_source line 28 · 2026-05-14T19:21:57.114Z_

<details><summary>↩ Tool result · `toolu_01NmGrFktQmqtLtHeixn9nDa`</summary>

```text
artifacts/literature_map.yaml
literature_map.yaml
artifacts/manifest.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260514T184925/best/imagined_experiments.yaml
registry.yaml
artifacts/dream_reports/dream_20260514T184925/median/imagined_experiments.yaml
decisions.yaml
artifacts/dream_reports/dream_20260514T184925/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260514T184925/best/review_context.yaml
artifacts/dream_reports/dream_20260514T184925/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf0b3aae-d9a6-4b53-8a20-1112b0afa5e4",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "6655ada4-2a6e-49d0-b7c5-78dc2af0aba5",
  "sourceToolAssistantUUID": "bf0b3aae-d9a6-4b53-8a20-1112b0afa5e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T19:21:59.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_015r5NndWnPtzFNiidYwz5kj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6655ada4-2a6e-49d0-b7c5-78dc2af0aba5",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31F66EBxCzeqRznyNsD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "447089b0-ebf3-4fcb-a501-086cea0579e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyrNQMfyrwiB1rjCE6ymFz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 26192,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 26192,
          "cache_creation_input_tokens": 801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 801,
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

_source line 30 · 2026-05-14T19:22:00.263Z_

<details><summary>↩ Tool result · `toolu_015r5NndWnPtzFNiidYwz5kj`</summary>

```text
1	\documentclass[letterpaper,11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{natbib}
11	
12	\setcounter{secnumdepth}{2}
13	
14	\title{Distributional Canary Collapse: Predictability Phase Diagrams\\for Early Warning in Iterative Synthetic Data Training}
15	
16	\author{
17	Anonymous Authors
18	}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	Iterative training on self-generated synthetic data leads to model collapse---progressive degradation of output quality and diversity.
25	While prior work has identified monitoring signals and reactive interventions, no systematic study has answered \emph{which} metrics earliest predict collapse, \emph{how far} ahead they lead, and \emph{under what contamination regime} such predictions hold.
26	We introduce a \textbf{predictability phase diagram} that maps the boundary between predictable and unpredictable collapse as a function of the synthetic data mixing ratio~$\alpha$.
27	Through Toda--Yamamoto panel temporal precedence testing on Pythia-410M and Pythia-1.4B across WikiText-103 and C4, we establish three results:
28	(1)~ECE and token entropy serve as \emph{canary} metrics that lead diversity collapse (distinct-$n$) by 1--3 generations across all tested regimes ($p<0.005$, all seeds);
29	(2)~a phase boundary at $\alpha^*\!\approx\!0.60$ separates regimes where canaries also lead perplexity ($\alpha \le 0.50$, $p<0.05$) from regimes where perplexity collapses synchronously with canaries ($\alpha \ge 0.75$, $p>0.18$);
30	(3)~naive Pearson lag-correlation produces ${\sim}41\%$ spurious significant associations on these non-stationary series, which the Toda--Yamamoto test correctly overturns.
31	Cross-domain (C4) and scale (1.4B) spot-checks preserve canary ranking (Spearman $\rho = 0.94$), and a canary-triggered intervention recovers 77\% of lost diversity at $\alpha = 0.75$.
32	\end{abstract}
33	
34	%----------------------------------------------------------------------
35	\section{Introduction}
36	%----------------------------------------------------------------------
37	
38	Training language models on their own outputs across successive generations---\emph{iterative self-consuming training}---causes \emph{model collapse}: a progressive narrowing of the output distribution that manifests as reduced lexical diversity, rising perplexity on held-out data, and deteriorating calibration \cite{shumailov2024ai}.
39	As synthetic data becomes increasingly prevalent in training pipelines, understanding and mitigating collapse is a pressing concern.
40	
41	Several monitoring tools exist. Spectral methods such as SIGMA track representation-level drift \cite{dohmatob2024model}; reactive interventions like DCES inject corrective signals after degradation is detected. Du et al.\ informally observed that expected calibration error (ECE) rises before accuracy degrades, but their study was limited to a single metric pair, 1--3 generations, and lacked formal time-series testing.
42	
43	A fundamental question remains unanswered: \emph{which metrics earliest predict collapse, how far ahead, and under what conditions?}
44	Answering this requires (i) a systematic comparison across metric families, (ii) a statistically rigorous lead--lag quantification method suited to non-stationary series, and (iii) exploration of the contamination regime.
45	
46	\paragraph{Contributions.}
47	We present a \textbf{predictability phase diagram} for iterative synthetic data training that maps the boundary between predictable and unpredictable collapse:
48	\begin{enumerate}
49	    \item \textbf{Canary$\to$Diversity Lead.} ECE and token entropy reliably lead diversity metrics (distinct-1/2) by 1--3 generations across all tested contamination ratios~$\alpha$, verified by Toda--Yamamoto (TY) panel temporal precedence ($p<0.005$, 3/3 seeds).
50	    \item \textbf{Regime-Dependent Predictability.} At $\alpha^*\!\approx\!0.60$, a phase transition separates regimes where canaries also lead perplexity from regimes where synchronous collapse precludes early warning.
51	    \item \textbf{Methodological Rigor.} We show that naive Pearson correlation on these non-stationary training trajectories yields ${\sim}41\%$ spurious significant associations, which the TY test correctly rejects. This methodological contribution stands independently of the specific canary findings.
52	\end{enumerate}
53	
54	We validate across domains (WikiText-103, C4), scales (410M, 1.4B parameters), data strategies (replace, accumulate), and demonstrate a canary-triggered intervention that recovers 77\% of diversity loss.
55	
56	%----------------------------------------------------------------------
57	\section{Related Work}
58	%----------------------------------------------------------------------
59	
60	\paragraph{Model collapse in iterative training.}
61	Shumailov et al.\ established that iterative training on self-generated data leads to progressive distribution narrowing. Subsequent theoretical analysis by Dohmatob et al.\ characterized spectral signatures of collapse, while Alemohammad et al.\ showed that mixing real data at ratio $1-\alpha$ can stabilize training under certain conditions. Fu et al.\ proved that accumulating historical generations bounds distributional drift, whereas replacing data each generation may diverge.
62	
63	\paragraph{Early warning and monitoring.}
64	SIGMA provides spectral monitoring of representation collapse but does not quantify temporal lead over downstream quality metrics. DCES operates reactively rather than predictively. Du et al.\ observed ECE rising before accuracy degradation, the closest antecedent to our work, but did not employ formal temporal precedence testing, examined only one metric pair, and did not explore regime dependence. Truong and Truong showed that standard early-warning indicators can fail under first-order phase transitions---our phase diagram explicitly maps where canary signals succeed and where they break down.
65	
66	\paragraph{Time-series causality in non-stationary settings.}
67	Granger causality testing requires stationarity, which training metric trajectories violate. The Toda--Yamamoto (TY) procedure augments the VAR lag order to accommodate integrated processes without pre-testing for unit roots, providing valid inference regardless of integration order. We adopt TY as our primary lead--lag quantification tool.
68	
69	%----------------------------------------------------------------------
70	\section{Method}
71	%----------------------------------------------------------------------
72	
73	\subsection{Iterative Self-Consuming Training Protocol}
74	
75	We train a language model $M_0$ on real data $D_0$ for one epoch, then iterate: at generation $t$, we sample synthetic data $S_t$ from $M_{t-1}$, form the training set $D_t = (1-\alpha)\,D_0 + \alpha\,S_t$ under the \textbf{replace} strategy (or $D_t = D_0 \cup \bigcup_{i=1}^{t} S_i$ under \textbf{accumulate}), and train $M_t$ on $D_t$.
76	We sweep $\alpha \in \{0.25, 0.50, 0.75, 1.00\}$ with 3 random seeds per condition.
77	
78	\subsection{Metric Families}
79	
80	We compute six metrics at each generation, grouped into three families:
81	
82	\paragraph{Canary candidates.} (i)~\textbf{ECE} (expected calibration error): measures miscalibration via binned confidence--accuracy gap. (ii)~\textbf{Token entropy}: Shannon entropy of the unigram token distribution in generated text. (iii)~\textbf{Effective rank}: the exponential of the entropy of the normalized singular values of the last-layer representations. (iv)~\textbf{Self-BLEU}: average pairwise BLEU among generated samples.
83	
84	\paragraph{Diversity targets.} (v)~\textbf{Distinct-$n$} ($n=1,2,3$): ratio of unique $n$-grams to total $n$-grams in generated text.
85	
86	\paragraph{Quality target.} (vi)~\textbf{Perplexity}: held-out perplexity on the original test split.
87	
88	\subsection{Toda--Yamamoto Panel Temporal Precedence}
89	
90	For each canary--target pair $(X,Y)$, we fit a bivariate VAR($k+d_{\max}$) where $k$ is selected by AIC and $d_{\max}$ is the maximal integration order (set to 1). We test the null $H_0$: lagged $X$ does not Granger-cause $Y$ by a Wald test on the first $k$ lag coefficients of $X$ in the $Y$ equation, following the Toda--Yamamoto procedure.
91	We report the optimal lag (negative = $X$ leads $Y$) and the $p$-value.
92	We pool across seeds using a panel specification with fixed effects.
93	
94	\subsection{Lead Time Quantification}
95	
96	We define the \textbf{$2\sigma$ onset} of metric $m$ as the earliest generation $t$ where $|m_t - m_0| > 2\,\text{std}(m_0)$, estimated from 3 independent initializations.
97	The \textbf{canary$\to$target lead} is the difference in onset generations.
98	This complements the TY test: TY provides a $p$-value for temporal precedence, while onset lead gives an interpretable time window.
99	
100	\subsection{Canary-Responsive Strategy (CRS)}
101	
102	As a proof-of-concept intervention, CRS monitors ECE at each generation. When a $2\sigma$ onset is detected, it reduces $\alpha$ by increasing the real data proportion (effective $\alpha$ post-trigger $\approx$ 0.52 from an initial 0.75).
103	
104	%----------------------------------------------------------------------
105	\section{Experimental Setup}
106	%----------------------------------------------------------------------
107	
108	\paragraph{Models.} Pythia-410M (primary) and Pythia-1.4B (scale check), both pretrained checkpoints from EleutherAI.
109	
110	\paragraph{Data.} WikiText-103 (primary) and C4 (cross-domain). We generate 50k tokens per generation for synthetic data, matching the original training set size.
111	
112	\paragraph{Training.} Each generation is fine-tuned for 1 epoch with AdamW (lr=$5\!\times\!10^{-5}$, batch size 16). 10 generations per run (20 for extended validation).
113	
114	\paragraph{Reproducibility.} 3 seeds per condition (4 seeds for the original MVP at $\alpha=1.0$). All TY tests use max\_lag $\geq 7$ unless otherwise noted.
115	
116	%----------------------------------------------------------------------
117	\section{Experiments and Results}
118	%----------------------------------------------------------------------
119	
120	\subsection{$\alpha$-Sweep: The Predictability Phase Diagram}
121	\label{sec:alpha_sweep}
122	
123	The core experiment sweeps $\alpha \in \{0.25, 0.50, 0.75, 1.00\}$ on Pythia-410M $\times$ WikiText-103 $\times$ 3 seeds $\times$ 10 generations. Table~\ref{tab:alpha_sweep} reports end-state metrics and canary lead times; Table~\ref{tab:ty_panel} reports the full TY panel results.
124	
125	\begin{table*}[t]
126	\centering
127	\caption{$\alpha$-sweep summary statistics (mean $\pm$ std across 3 seeds, except $\alpha\!=\!1.0$: 4 seeds). ``Canary$\to$d1 lead'' and ``canary$\to$ppl lead'' are $2\sigma$ onset differences in generations.}
128	\label{tab:alpha_sweep}
129	\small
130	\begin{tabular}{@{}lcccccccc@{}}
131	\toprule
132	$\alpha$ & gen10 ppl & gen10 entropy & gen10 ECE & gen10 d1 & gen10 d2 & canary$\to$d1 lead & canary$\to$ppl lead & TY $p$ (ECE$\to$ppl) \\
133	\midrule
134	0.25 & 68.4$\pm$4.1   & 2.41$\pm$0.05 & 0.138$\pm$0.009 & 0.312$\pm$0.018 & 0.681$\pm$0.022 & 2.7$\pm$0.3 & 2.0$\pm$0.4 & 0.018 \\
135	0.50 & 189.3$\pm$12.6  & 1.94$\pm$0.07 & 0.247$\pm$0.015 & 0.198$\pm$0.014 & 0.512$\pm$0.019 & 2.0$\pm$0.2 & 1.3$\pm$0.3 & 0.032 \\
136	0.75 & 512.7$\pm$31.4  & 1.52$\pm$0.09 & 0.361$\pm$0.021 & 0.112$\pm$0.011 & 0.402$\pm$0.025 & 1.7$\pm$0.2 & 0.3$\pm$0.5 & 0.214 \\
137	1.00 & 1024.7$\pm$16.8 & 1.27$\pm$0.06 & 0.420$\pm$0.012 & 0.075$\pm$0.008 & 0.365$\pm$0.015 & 1.5$\pm$0.3 & 0.0$\pm$0.2 & 0.487 \\
138	\bottomrule
139	\end{tabular}
140	\end{table*}
141	
142	\begin{table*}[t]
143	\centering
144	\caption{Toda--Yamamoto panel results for all canary$\to$target pairs. Each cell shows (optimal lag, $p$-value); negative lag indicates the canary leads the target. Bold entries are significant at $p<0.05$.}
145	\label{tab:ty_panel}
146	\small
147	\begin{tabular}{@{}llcccc@{}}
148	\toprule
149	Canary & Target & $\alpha=0.25$ & $\alpha=0.50$ & $\alpha=0.75$ & $\alpha=1.0$ \\
150	\midrule
151	ECE          & distinct\_1 & \textbf{($-$3, $<$0.001)} & \textbf{($-$2, $<$0.001)} & \textbf{($-$2, 0.003)} & \textbf{($-$2, $<$0.001)} \\
152	ECE          & distinct\_2 & \textbf{($-$3, 0.002)}    & \textbf{($-$2, 0.002)}    & \textbf{($-$2, 0.006)} & \textbf{($-$1, 0.004)} \\
153	token\_ent   & distinct\_1 & \textbf{($-$2, 0.003)}    & \textbf{($-$2, 0.004)}    & \textbf{($-$1, 0.012)} & \textbf{($-$1, 0.003)} \\
154	token\_ent   & distinct\_2 & \textbf{($-$3, 0.004)}    & \textbf{($-$2, 0.006)}    & \textbf{($-$2, 0.018)} & \textbf{($-$1, 0.009)} \\
155	\midrule
156	ECE          & perplexity  & \textbf{($-$2, 0.015)}    & \textbf{($-$1, 0.032)}    & (0, 0.187)             & (0, 0.412) \\
157	token\_ent   & perplexity  & \textbf{($-$2, 0.021)}    & \textbf{($-$1, 0.041)}    & (0, 0.238)             & ($-$5*, 0.063) \\
158	\midrule
159	eff\_rank    & distinct\_1 & (0, 0.342) & (0, 0.287) & (0, 0.415) & (0, 0.523) \\
160	self\_bleu   & distinct\_1 & (0, 0.178) & (0, 0.221) & ($-$1, 0.089) & (0, 0.156) \\
161	\bottomrule
162	\end{tabular}
163	\end{table*}
164	
165	\paragraph{Key findings.}
166	Three patterns emerge from Tables~\ref{tab:alpha_sweep}--\ref{tab:ty_panel}:
167	
168	\textit{(i) Canary$\to$diversity is universally predictable.}
169	ECE and token entropy significantly lead distinct-1 and distinct-2 at all $\alpha$ values ($p < 0.02$), with lead times of 1.5--2.7 generations. Cross-seed consistency is 3/3 at every $\alpha$.
170	
171	\textit{(ii) Canary$\to$perplexity is regime-dependent.}
172	At $\alpha \le 0.50$, ECE leads perplexity by 1--2 generations ($p < 0.05$). At $\alpha = 0.75$, the lead vanishes ($p = 0.187$--$0.238$). The phase boundary $\alpha^* \approx 0.60$ marks the transition. This occurs because lower~$\alpha$ slows distributional drift, allowing the sensitivity gap between canary metrics (which detect small KL-divergence shifts) and perplexity (which requires structural loss-landscape changes) to manifest as a temporal lead.
173	
174	\textit{(iii) Failed canaries.}
175	Effective rank and self-BLEU show no significant lead over any target at any~$\alpha$ ($p > 0.08$). We report these null results in full: the canary phenomenon is specific to calibration and token-distribution metrics, not a universal property of all collapse indicators.
176	
177	\subsection{Methodological Ablation: Naive vs.\ Robust Testing}
178	\label{sec:method_ablation}
179	
180	We compare four lead--lag quantification methods on the pooled MVP (4 seeds, $\alpha=1.0$) and $\alpha$-sweep (9 runs) data: naive Pearson lag-correlation, differenced cross-correlation, threshold-based onset lead, and TY panel temporal precedence. Table~\ref{tab:method_comparison} reports significant pair counts; Table~\ref{tab:false_positives} breaks down the false positives.
181	
182	\begin{table}[t]
183	\centering
184	\caption{Method comparison: significant pair counts out of 104 total canary$\to$target pairs tested. ``False positive vs TY'' counts pairs significant under the method but not under TY.}
185	\label{tab:method_comparison}
186	\small
187	\begin{tabular}{@{}lcccc@{}}
188	\toprule
189	Method & Sig.\ pairs & Agrees & FP vs TY & FN vs TY \\
190	\midrule
191	Naive Pearson     & 71/104 & 42 & 29 (40.8\%) & 0 \\
192	Differenced XCorr & 48/104 & 36 & 12 (16.9\%) & 6 \\
193	Threshold Onset   & 39/104 & 37 &  2 (2.8\%)  & 5 \\
194	Toda--Yamamoto    & 42/104 & --- & ---         & --- \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\begin{table}[t]
200	\centering
201	\caption{Breakdown of 29 naive Pearson false positives overturned by TY.}
202	\label{tab:false_positives}
203	\small
204	\begin{tabular}{@{}lcp{3.5cm}@{}}
205	\toprule
206	Category & Count & Example \\
207	\midrule
208	Failed canary $\to$ any target & 20 & eff\_rank$\to$d1, $\alpha\!=\!0.50$ \\
209	canary$\to$ppl at $\alpha\!\ge\!0.75$ & 6 & ECE$\to$ppl, $\alpha\!=\!0.75$ \\
210	Reverse direction & 3 & d1$\to$ECE, $\alpha\!=\!1.0$ \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	Naive Pearson correlation declares 71 out of 104 pairs significant---a 40.8\% false-positive rate relative to TY. The spurious associations arise from three sources: (1)~all-declining metrics producing high $|r|$ via shared trends (effective rank and self-BLEU pairs: 20 cases); (2)~synchronous collapse at high $\alpha$ being misclassified as directional lead (6 cases); and (3)~bidirectional correlation conflating target$\to$canary with canary$\to$target direction (3 cases).
216	
217	The threshold-onset method agrees with TY in 88\% of cases, but TY provides $p$-values and directional testing, yielding stronger statistical evidence for or against temporal precedence.
218	
219	\subsection{MVP Formalization ($\alpha = 1.0$, max\_lag = 7)}
220	\label{sec:mvp}
221	
222	We re-run TY testing on the original 4-seed MVP data with max\_lag increased from 5 to 7 to verify whether the marginal entropy$\to$perplexity signal at lag~$= -5$ is a truncation artifact. Results appear in Table~\ref{tab:mvp_maxlag}.
223	
224	\begin{table}[t]
225	\centering
226	\caption{MVP ($\alpha\!=\!1.0$) TY results: max\_lag$\,=\,$5 vs.\ 7.}
227	\label{tab:mvp_maxlag}
228	\small
229	\begin{tabular}{@{}lccc@{}}
230	\toprule
231	Pair & lag=5 & lag=7 & Conclusion \\
232	\midrule
233	ECE$\to$d1       & ($-$2, $<$0.001) & ($-$2, 0.0004) & Stable lead \\
234	ECE$\to$d2       & ($-$1, 0.003) & ($-$1, 0.004) & Stable \\
235	ent$\to$d1       & ($-$1, 0.002) & ($-$1, 0.0018) & Stable \\
236	ent$\to$ppl      & ($-$5, 0.052) & ($-$5, 0.071) & Not significant \\
237	ECE$\to$ppl      & (0, 0.38) & (0, 0.412)    & Not significant \\
238	\bottomrule
239	\end{tabular}
240	\end{table}
241	
242	The canary$\to$diversity leads are stable under increased max\_lag ($p < 0.005$). The entropy$\to$perplexity lag$\,= -5$ signal weakens from $p = 0.052$ to $p = 0.071$---confirming it as statistical noise rather than a truncation artifact. At $\alpha = 1.0$, $2\sigma$ onsets for ECE (gen~2.1$\pm$0.3), entropy (gen~2.4$\pm$0.4), and perplexity (gen~2.3$\pm$0.3) are nearly synchronous, leaving insufficient temporal separation for canary$\to$perplexity lead.
243	
244	\subsection{Cross-Domain Validation: C4}
245	\label{sec:c4}
246	
247	To test domain invariance, we replicate the $\alpha = 0.50$ condition on C4 (web crawl data) with Pythia-410M $\times$ 3 seeds $\times$ 10 generations. Table~\ref{tab:cross_domain} compares results with WikiText-103.
248	
249	\begin{table}[t]
250	\centering
251	\caption{Cross-domain comparison at $\alpha\!=\!0.50$. All lags and $p$-values from TY panel tests.}
252	\label{tab:cross_domain}
253	\small
254	\begin{tabular}{@{}lccc@{}}
255	\toprule
256	Metric pair & WikiText-103 & C4 & $\Delta$lag \\
257	\midrule
258	ECE$\to$d1       & ($-$2, $<$0.001) & ($-$2, 0.003) & 0 \\
259	ent$\to$d1       & ($-$2, 0.004) & ($-$2, 0.006)    & 0 \\
260	ECE$\to$ppl      & ($-$1, 0.032) & ($-$1, 0.044)    & 0 \\
261	ent$\to$ppl      & ($-$1, 0.041) & ($-$1, 0.058)    & 0 \\
262	eff\_rank$\to$d1 & (0, 0.287) & (0, 0.334)          & 0 \\
263	\bottomrule
264	\end{tabular}
265	\end{table}
266	
267	Canary ranking is preserved across domains with Spearman rank correlation $\rho = 0.94$ between WikiText-103 and C4 lag structures. All significant pairs on WikiText-103 remain significant on C4; all non-significant pairs remain non-significant. Absolute metric values differ (C4 gen-10 perplexity 211.8 vs.\ WikiText 189.3, reflecting noisier web text), but the temporal precedence structure is invariant. This supports the interpretation that the canary mechanism is model-intrinsic rather than data-specific.
268	
269	\subsection{Scale Spot-Check: Pythia-1.4B}
270	\label{sec:scale}
271	
272	We run Pythia-1.4B (3.4$\times$ parameters) at $\alpha = 0.50$ on WikiText-103 to test scale robustness. Table~\ref{tab:scale} compares with the 410M baseline.
273	
274	\begin{table}[t]
275	\centering
276	\caption{Scale comparison at $\alpha\!=\!0.50$, WikiText-103.}
277	\label{tab:scale}
278	\small
279	\begin{tabular}{@{}lccccc@{}}
280	\toprule
281	Model & gen10 ppl & c$\to$d1 lead & c$\to$ppl lead & TY $p$ (ECE$\to$d1) & TY $p$ (ECE$\to$ppl) \\
282	\midrule
283	Pythia-410M & 189.3 & 2.0 gen & 1.3 gen & $<$0.005 & 0.032 \\
284	Pythia-1.4B & 142.5 & 2.3 gen & 1.5 gen & 0.002 & 0.028 \\
285	\bottomrule
286	\end{tabular}
287	\end{table}
288	
289	Canary ranking is preserved at the larger scale. Lead times are slightly longer (2.3 vs.\ 2.0~gen for diversity; 1.5 vs.\ 1.3~gen for perplexity), consistent with the hypothesis that larger models collapse more gradually per generation, allowing the metric sensitivity gap to accumulate over more generations. The 1.4B model achieves lower gen-10 perplexity (142.5 vs.\ 189.3), indicating higher capacity provides partial resilience.
290	
291	\subsection{Extended Run: 20 Generations ($\alpha = 1.0$)}
292	\label{sec:extended}
293	
294	We extend the $\alpha = 1.0$ condition to 20 generations (2 seeds, max\_lag = 10) to rule out sequence-length artifacts. Table~\ref{tab:extended} compares 10-gen and 20-gen TY results.
295	
296	\begin{table}[t]
297	\centering
298	\caption{Extended run ($\alpha\!=\!1.0$) TY results with max\_lag$\,=\,$10.}
299	\label{tab:extended}
300	\small
301	\begin{tabular}{@{}lccc@{}}
302	\toprule
303	Pair & 10-gen & 20-gen & Conclusion \\
304	\midrule
305	ent$\to$ppl  & ($-$5, 0.071) & (0, 0.523) & No lead---confirmed \\
306	ECE$\to$d1   & ($-$2, 0.0004) & ($-$2, 0.0002) & Stable lead \\
307	ECE$\to$ppl  & (0, 0.412) & (0, 0.487)       & No lead---confirmed \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	With 20 generations and max\_lag $= 10$, the entropy$\to$perplexity ``signal'' vanishes entirely (lag~$= 0$, $p = 0.523$), confirming its absence is genuine. The canary$\to$diversity lead strengthens ($p = 0.0002$). Collapse saturates around generation~12 (gen-20 perplexity: 4287.3; gen-20 distinct-1: 0.024), consistent with the model output becoming near-deterministic.
313	
314	\subsection{Canary-Responsive Intervention}
315	\label{sec:intervention}
316	
317	We evaluate CRS at $\alpha = 0.75$ (the regime where canary$\to$perplexity lead is absent but canary$\to$diversity lead persists). When ECE triggers $2\sigma$ onset (gen~3.2$\pm$0.4), CRS reduces $\alpha$ from 0.75 to an effective $\sim$0.52. Table~\ref{tab:intervention} compares three conditions.
318	
319	\begin{table}[t]
320	\centering
321	\caption{Intervention results at $\alpha\!=\!0.75$ (mean $\pm$ std, 3 seeds). Oracle uses $\alpha\!=\!0.50$ throughout.}
322	\label{tab:intervention}
323	\small
324	\begin{tabular}{@{}lcccc@{}}
325	\toprule
326	Condition & gen10 d1 & gen10 d2 & gen10 ppl & gen10 ECE \\
327	\midrule
328	No intervention       & .112$\pm$.011 & .402$\pm$.025 & 512.7$\pm$31.4 & .361$\pm$.021 \\
329	CRS (ECE trigger)     & .198$\pm$.015 & .524$\pm$.020 & 341.2$\pm$22.7 & .253$\pm$.018 \\
330	Oracle ($\alpha\!=\!.50$) & .198$\pm$.014 & .512$\pm$.019 & 189.3$\pm$12.6 & .247$\pm$.015 \\
331	\bottomrule
332	\end{tabular}
333	\end{table}
334	
335	CRS recovers 76.8\% of the diversity gap between the no-intervention and $\alpha = 0.25$ baselines (computed as $(0.198 - 0.112)/(0.312 - 0.112) = 0.43$, relative to the full $\alpha$-sweep range). It matches the oracle on gen-10 distinct-1 ($0.198$ vs.\ $0.198$) and reduces perplexity by 33.4\% ($512.7 \to 341.2$). The perplexity gap relative to oracle ($341.2$ vs.\ $189.3$) reflects irreversible calibration drift accumulated during the first 3 generations at high~$\alpha$.
336	
337	\subsection{Data Strategy Ablation: Accumulate vs.\ Replace}
338	\label{sec:data_strategy}
339	
340	At $\alpha = 0.50$, we compare the standard replace strategy (each generation trains on fresh synthetic data) with accumulate (all historical synthetic data is retained). Table~\ref{tab:data_strategy} reports results.
341	
342	\begin{table}[t]
343	\centering
344	\caption{Data strategy comparison at $\alpha\!=\!0.50$ (mean, 3 seeds).}
345	\label{tab:data_strategy}
346	\small
347	\begin{tabular}{@{}lcccc@{}}
348	\toprule
349	Strategy & gen10 d1 & gen10 ppl & c$\to$d1 lead & c$\to$ppl lead \\
350	\midrule
351	Replace     & 0.198$\pm$0.014 & 189.3$\pm$12.6 & 2.0 gen & 1.3 gen \\
352	Accumulate  & 0.267$\pm$0.016 & 124.8$\pm$9.3  & 2.5 gen & 1.8 gen \\
353	\bottomrule
354	\end{tabular}
355	\end{table}
356	
357	Accumulate reduces gen-10 perplexity by 34.2\% and improves diversity (distinct-1: 0.267 vs.\ 0.198), confirming theoretical predictions that retaining historical data bounds distributional drift. A novel finding: accumulate also extends canary lead times (diversity lead: 2.5 vs.\ 2.0~gen; perplexity lead: 1.8 vs.\ 1.3~gen). More gradual collapse gives the metric sensitivity gap additional generations to manifest, widening the early-warning window.
358	
359	%----------------------------------------------------------------------
360	\section{Discussion}
361	%----------------------------------------------------------------------
362	
363	\paragraph{The predictability phase diagram.}
364	Our results unify three observations into a single framework parameterized by the contamination ratio~$\alpha$. At low~$\alpha$, real data anchors the distribution, collapse is gradual, and both diversity and perplexity are predictable from canary metrics. As $\alpha$ increases, drift rate rises, compressing the temporal gap between metric onsets. At $\alpha^* \approx 0.60$, the perplexity channel crosses from predictable to unpredictable. The diversity channel remains predictable across all tested regimes because diversity metrics (distinct-$n$) require vocabulary contraction that inherently lags the calibration and token-distribution shifts captured by ECE and entropy.
365	
366	\paragraph{Why some canaries fail.}
367	Effective rank operates on representation-space singular values, which can remain stable even as the output distribution narrows (the model maps diverse inputs to similar outputs without losing representational rank). Self-BLEU measures pairwise similarity at the sequence level, which is noisy with small sample sizes and confounded by sequence length.
368	
369	\paragraph{Practical implications.}
370	In realistic deployment scenarios ($\alpha \ll 1$, data accumulation), canary lead times of 2--3 generations provide actionable early warning. The CRS proof-of-concept shows that even a simple trigger-based intervention can recover most of the diversity loss. More sophisticated adaptive $\alpha$-scheduling strategies could further improve outcomes.
371	
372	\paragraph{Limitations.}
373	Scale validation reaches only 1.4B parameters; whether lead times continue to increase at 7B+ is unknown.
374	All experiments use autoregressive language models; applicability to diffusion models or other generative architectures is untested.
375	The phase boundary $\alpha^* \approx 0.60$ is estimated from four $\alpha$ values and should be refined with finer sweeps.
376	TY testing on 10-generation series has limited statistical power; longer training horizons would strengthen conclusions.
377	
378	%----------------------------------------------------------------------
379	\section{Conclusion}
380	%----------------------------------------------------------------------
381	
382	We have presented a predictability phase diagram for model collapse in iterative synthetic data training. ECE and token entropy serve as reliable canary metrics that lead diversity degradation by 1--3 generations across all tested contamination regimes, model scales, and data domains. A phase boundary at $\alpha^* \approx 0.60$ separates regimes where canaries also predict perplexity degradation from those where synchronous collapse precludes early warning. Our methodological contribution---demonstrating that naive correlation yields ${\sim}41\%$ spurious associations on these non-stationary trajectories---underscores the necessity of formal temporal precedence testing. A canary-triggered intervention recovers 77\% of diversity loss, translating predictive power into actionable mitigation.
383	
384	\bibliographystyle{plainnat}
385	
386	\appendix
387	
388	\section{Supplementary Tables}
389	
390	Tables~\ref{tab:mvp_maxlag} and~\ref{tab:extended} appear in the main text as they address specific robustness checks. Additional per-seed breakdowns and distinct-3 results are available in the supplementary material.
391	
392	\end{document}
393	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "447089b0-ebf3-4fcb-a501-086cea0579e2",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "900056cf-4d98-434c-87b4-1fa65bd57bdd",
  "sourceToolAssistantUUID": "447089b0-ebf3-4fcb-a501-086cea0579e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T19:22:02.833Z_

Now let me also read the review context and experimental plan files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "900056cf-4d98-434c-87b4-1fa65bd57bdd",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31FKYbrAW9SESYGH9NP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7152dd17-4b01-4aad-b59e-f57cf750b1cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzBarw8RmnhQCka4UN2KmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 26993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10154,
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

_source line 32 · 2026-05-14T19:22:05.173Z_

<details open><summary>🔧 Tool call — Read · `toolu_014fu5c3dYzurm7yWgyb4HFQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7152dd17-4b01-4aad-b59e-f57cf750b1cd",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31FKYbrAW9SESYGH9NP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "117ede09-664b-4803-96a5-935058448e31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzBarw8RmnhQCka4UN2KmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 26993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10154,
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

_source line 33 · 2026-05-14T19:22:05.178Z_

<details><summary>↩ Tool result · `toolu_014fu5c3dYzurm7yWgyb4HFQ`</summary>

```text
1	narrative_guidance: '原始 framing 三条 claims 全部成立。α-sweep 揭示清晰的 predictability phase
2	  transition： α≤0.50 下 canary→perplexity lead 出现（1-2 gen），α*≈0.60 划定可预测/不可预测边界。 方法论贡献独立成立——naive
3	  correlation 在非平稳序列上产生 ~40% 伪显著关联被 TY 推翻。 Cross-domain 和 scale spot-check 均保持 canary
4	  ranking。Headline 无需修改，直投 AAAI full paper。
5	
6	  '
7	imagined_experiments:
8	- name: α-sweep (α∈{0.25, 0.50, 0.75})
9	  plan_id: plan_001
10	  description: 'Pythia-410M × WikiText-103 × α∈{0.25, 0.50, 0.75} × 3 seeds × 10 gen
11	    iterative training。 每代计算 ECE、token_entropy、effective_rank、self_bleu、distinct_1/2/3、perplexity。
12	    Toda-Yamamoto panel temporal precedence 检验所有 canary→target 对。
13	
14	    '
15	  expected_results:
16	    alpha_0.25_gen10_perplexity: 68.4
17	    alpha_0.25_gen10_token_entropy: 2.41
18	    alpha_0.25_gen10_ece: 0.138
19	    alpha_0.25_gen10_distinct_1: 0.312
20	    alpha_0.25_gen10_distinct_2: 0.681
21	    alpha_0.25_canary_diversity_lead_gen: 2.7
22	    alpha_0.25_canary_perplexity_lead_gen: 2.0
23	    alpha_0.25_TY_canary_to_diversity_p: 0.002
24	    alpha_0.25_TY_canary_to_perplexity_p: 0.018
25	    alpha_0.25_effect_size_r_ece_distinct1: 0.97
26	    alpha_0.50_gen10_perplexity: 189.3
27	    alpha_0.50_gen10_token_entropy: 1.94
28	    alpha_0.50_gen10_ece: 0.247
29	    alpha_0.50_gen10_distinct_1: 0.198
30	    alpha_0.50_gen10_distinct_2: 0.512
31	    alpha_0.50_canary_diversity_lead_gen: 2.0
32	    alpha_0.50_canary_perplexity_lead_gen: 1.3
33	    alpha_0.50_TY_canary_to_diversity_p: 0.001
34	    alpha_0.50_TY_canary_to_perplexity_p: 0.032
35	    alpha_0.50_effect_size_r_ece_distinct1: 0.96
36	    alpha_0.75_gen10_perplexity: 512.7
37	    alpha_0.75_gen10_token_entropy: 1.52
38	    alpha_0.75_gen10_ece: 0.361
39	    alpha_0.75_gen10_distinct_1: 0.112
40	    alpha_0.75_gen10_distinct_2: 0.402
41	    alpha_0.75_canary_diversity_lead_gen: 1.7
42	    alpha_0.75_canary_perplexity_lead_gen: 0.3
43	    alpha_0.75_TY_canary_to_diversity_p: 0.003
44	    alpha_0.75_TY_canary_to_perplexity_p: 0.214
45	    alpha_0.75_effect_size_r_ece_distinct1: 0.96
46	    phase_boundary_alpha_star: 0.6
47	    cross_seed_consistency_diversity_lead: 3/3 seeds at all α
48	    cross_seed_consistency_perplexity_lead: 3/3 seeds at α≤0.50; 1/3 at α=0.75
49	  result_rationale: 'α 控制每代训练数据中合成数据的比例。低 α 下真实数据作为 anchor 减缓 distribution drift，
50	    collapse 从 catastrophic（α=1.0 时 gen10 ppl>1000）变为 gradual（α=0.25 时 gen10 ppl~68）。
51	    渐进退化使不同 metric family 的 onset timing 解耦——calibration（ECE）和 token distribution
52	    （entropy）对微小 distribution shift 最敏感（单代内 KL divergence 变化即可触发 2σ onset）， 而 diversity（distinct_n）需要
53	    vocabulary 实质收缩才反映，perplexity 则需 loss landscape 发生结构性改变。在 α=1.0（MVP）下三者近乎同步崩溃（1-2
54	    gen window），因为 drift 速度 压倒了 sensitivity 差异。降低 α 拉长 collapse timeline，sensitivity
55	    差异被放大： ECE onset 出现在 gen 2-3 而 distinct_1 onset 在 gen 5-6（α=0.25），产生 ~2.7 gen
56	    lead。 Perplexity 的可预测性取决于 drift 是否足够慢让 canary signal 积累足够 lead——α=0.25/0.50 下
57	    drift rate 允许 1-2 gen canary→perplexity lead，但 α=0.75 时 drift 过快， perplexity 几乎与
58	    canary 同步变化，TY 检验不再显著（p=0.214）。 Phase boundary α*≈0.60 是 perplexity lead 从统计显著跌落到不显著的转折点——
59	    这是 drift rate 与 metric sensitivity gap 的临界平衡点。
60	
61	    '
62	  tables:
63	  - name: 'Table 1: α-sweep Summary Statistics (mean ± std across seeds)'
64	    columns:
65	    - α
66	    - gen10_ppl
67	    - gen10_entropy
68	    - gen10_ece
69	    - gen10_d1
70	    - gen10_d2
71	    - canary→d1 lead (gen)
72	    - canary→ppl lead (gen)
73	    - TY p (canary→d1)
74	    - TY p (canary→ppl)
75	    rows:
76	    - - '0.25'
77	      - 68.4±4.1
78	      - 2.41±0.05
79	      - 0.138±0.009
80	      - 0.312±0.018
81	      - 0.681±0.022
82	      - 2.7±0.3
83	      - 2.0±0.4
84	      - <0.005
85	      - '0.018'
86	    - - '0.50'
87	      - 189.3±12.6
88	      - 1.94±0.07
89	      - 0.247±0.015
90	      - 0.198±0.014
91	      - 0.512±0.019
92	      - 2.0±0.2
93	      - 1.3±0.3
94	      - <0.005
95	      - '0.032'
96	    - - '0.75'
97	      - 512.7±31.4
98	      - 1.52±0.09
99	      - 0.361±0.021
100	      - 0.112±0.011
101	      - 0.402±0.025
102	      - 1.7±0.2
103	      - 0.3±0.5
104	      - <0.005
105	      - '0.214'
106	    - - 1.00 (MVP)
107	      - 1024.7±16.8
108	      - 1.27±0.06
109	      - 0.420±0.012
110	      - 0.075±0.008
111	      - 0.365±0.015
112	      - 1.5±0.3
113	      - 0.0±0.2
114	      - <0.001
115	      - '0.487'
116	  - name: 'Table 2: Toda-Yamamoto Panel Results — All Canary→Target Pairs'
117	    columns:
118	    - canary
119	    - target
120	    - α=0.25 (lag, p)
121	    - α=0.50 (lag, p)
122	    - α=0.75 (lag, p)
123	    - α=1.0 (lag, p)
124	    rows:
125	    - - ECE
126	      - distinct_1
127	      - (-3, <0.001)
128	      - (-2, <0.001)
129	      - (-2, 0.003)
130	      - (-2, <0.001)
131	    - - ECE
132	      - distinct_2
133	      - (-3, 0.002)
134	      - (-2, 0.002)
135	      - (-2, 0.006)
136	      - (-1, 0.004)
137	    - - token_entropy
138	      - distinct_1
139	      - (-2, 0.003)
140	      - (-2, 0.004)
141	      - (-1, 0.012)
142	      - (-1, 0.003)
143	    - - token_entropy
144	      - distinct_2
145	      - (-3, 0.004)
146	      - (-2, 0.006)
147	      - (-2, 0.018)
148	      - (-1, 0.009)
149	    - - ECE
150	      - perplexity
151	      - (-2, 0.015)
152	      - (-1, 0.032)
153	      - (0, 0.187)
154	      - (0, 0.412)
155	    - - token_entropy
156	      - perplexity
157	      - (-2, 0.021)
158	      - (-1, 0.041)
159	      - (0, 0.238)
160	      - (-5*, 0.063)
161	    - - effective_rank
162	      - distinct_1
163	      - (0, 0.342)
164	      - (0, 0.287)
165	      - (0, 0.415)
166	      - (0, 0.523)
167	    - - self_bleu
168	      - distinct_1
169	      - (0, 0.178)
170	      - (0, 0.221)
171	      - (-1, 0.089)
172	      - (0, 0.156)
173	  figures_description:
174	  - 'Fig 1: Predictability Phase Diagram — x-axis α∈[0,1], y-axis target metric (distinct_1,
175	    distinct_2, perplexity)。每个 cell 色标 = TY-estimated lead time (gen)，灰色 = not significant。清晰可见
176	    α*≈0.60 处 perplexity 行从有色变灰的 boundary。diversity 行全程有色。'
177	  - 'Fig 2: 四面板 collapse trajectory — 每面板一个 α，x-axis generation, y-axis 标准化 metric
178	    (z-score)。ECE 和 entropy 曲线领先 distinct_1/2，低 α 下 gap 明显加宽。Perplexity 曲线在 α≤0.50
179	    面板中可见延迟，在 α≥0.75 中与 canary 同步。'
180	  - 'Fig 3: Canary lead time vs α — x-axis α, y-axis TY-estimated lead (gen)。canary→diversity
181	    线近乎单调递增（随 α 降低 lead 增加），canary→perplexity 线在 α*≈0.60 处 drop to zero。误差带 = seed
182	    std。'
183	  analysis: 'α-sweep 是全文核心实验。Phase diagram 将三条 claims 统一为一张图： diversity 通道全 regime
184	    可预测（Claim 1），perplexity 通道 regime-dependent（Claim 2）， α* boundary 明确。effective_rank
185	    和 self_bleu 在所有 α 下均不显著—— 与 MVP 结论一致，排除选择偏差质疑。3 seeds 在所有 α 下 diversity lead 一致性
186	    3/3， perplexity lead 在 α≤0.50 下 3/3，α=0.75 下仅 1/3（边界行为，符合 phase transition 预期）。
187	
188	    '
189	- name: '方法论 ablation: Naive vs Robust 检验'
190	  plan_id: plan_002
191	  description: '在 MVP 4-seed 数据 + α-sweep 9 runs 数据上，对比四种 lead-lag 量化方法： (i) naive
192	    Pearson lag-correlation (ii) 差分后 cross-correlation (iii) threshold-based onset
193	    lead (iv) Toda-Yamamoto panel temporal precedence。 统计所有方法对所有 canary→target pair
194	    的显著性判定，量化伪显著被推翻比例。
195	
196	    '
197	  expected_results:
198	    total_pairs_tested: 104
199	    naive_pearson_significant_count: 71
200	    differenced_xcorr_significant_count: 48
201	    threshold_onset_significant_count: 39
202	    TY_significant_count: 42
203	    naive_overturned_by_TY_pct: 40.8
204	    naive_overturned_by_TY_count: 29
205	    false_positive_category_breakdown:
206	      effective_rank_pairs: 12
207	      self_bleu_pairs: 8
208	      canary_to_ppl_high_alpha: 6
209	      spurious_reverse_direction: 3
210	    TY_unique_significant_not_in_naive: 0
211	    method_agreement_TY_vs_threshold: 0.88
212	  result_rationale: '非平稳时间序列（所有 metric 在 iterative training 中趋势性退化）的 Pearson correlation
213	    产生 spurious regression——两个独立但都有趋势的序列可以 |r|>0.9。naive 方法对所有 "都在下降"的 metric pair
214	    报告显著，包括 effective_rank→diversity（实际无 lead-lag 关系， 只是共享下降趋势）和 canary→perplexity
215	    at α≥0.75（同步崩溃无因果方向）。 差分后去趋势消除部分伪关联但对短序列（10 gen）power 不足，false negative 较多。 TY
216	    方法在 VAR 框架中检验 Granger non-causality，自动处理非平稳性（通过 augmented lag），对真正的 lead-lag 关系（canary→diversity）保持高
217	    power（p<0.005）， 对无方向性的同步崩溃正确报告不显著（p>0.05）。~41% 的 naive 显著关联被推翻， 主要来自三类：(1) 失败
218	    canary 族的伪关联（effective_rank、self_bleu 与任何 target）， (2) 高 α 下 canary→perplexity
219	    的同步崩溃被误判为 lead， (3) 少数反向因果（target→canary）被 naive 双向 correlation 报告为显著。
220	
221	    '
222	  tables:
223	  - name: 'Table 3: Method Comparison — Significant Pair Counts'
224	    columns:
225	    - Method
226	    - Significant pairs
227	    - Agrees w/ TY
228	    - Disagrees w/ TY
229	    - False positive vs TY
230	    - False negative vs TY
231	    rows:
232	    - - Naive Pearson
233	      - 71/104
234	      - '42'
235	      - '29'
236	      - 29 (40.8%)
237	      - '0'
238	    - - Differenced XCorr
239	      - 48/104
240	      - '36'
241	      - '12'
242	      - 12 (16.9%)
243	      - '6'
244	    - - Threshold Onset
245	      - 39/104
246	      - '37'
247	      - '2'
248	      - 2 (2.8%)
249	      - '5'
250	    - - Toda-Yamamoto
251	      - 42/104
252	      - —
253	      - —
254	      - —
255	      - —
256	  - name: 'Table 4: Breakdown of Naive False Positives Overturned by TY'
257	    columns:
258	    - Category
259	    - Count
260	    - Example pair
261	    rows:
262	    - - Failed canary (eff_rank/self_bleu) → any target
263	      - '20'
264	      - effective_rank→distinct_1 at α=0.50
265	    - - canary→perplexity at α≥0.75
266	      - '6'
267	      - ECE→ppl at α=0.75
268	    - - Reverse direction (target→canary)
269	      - '3'
270	      - distinct_1→ECE at α=1.0
271	  figures_description:
272	  - 'Fig 4: Agreement matrix heatmap — 4 methods × 104 pairs，binary significant/not。visual
273	    clustering 显示 naive 方法在右上角大片''显著''区域被其他三种方法一致判定为不显著。'
274	  - 'Fig 5: Naive |r| vs TY p-value scatter — 每个 pair 一点，color = truly significant
275	    (TY) vs overturned。右上区域（高 |r| 但 TY p>0.05）包含所有 spurious regression 案例。'
276	  analysis: '~41% 伪显著率远超 30% 阈值，方法论贡献独立成立。这直接回应 reviewer concern "为什么不用简单相关"——答案是简单方法在这个
277	    setting 下系统性高估 canary 预测能力， 尤其是对失败 canary 和高 α regime。Threshold onset 与 TY 一致性高（88%），
278	    但 TY 提供 p-value 和方向性检验，统计论证更强。
279	
280	    '
281	- name: MVP 结果 formalization (max_lag=7)
282	  plan_id: plan_003
283	  description: '在 MVP 4-seed (α=1.0) 数据上重跑 TY 检验，max_lag 从 5 增大到 7， 验证 token_entropy→perplexity
284	    的 lag=-5 是否为截断伪影。 统一 2σ onset 定义，输出 paper-ready 数值。
285	
286	    '
287	  expected_results:
288	    max_lag_7_ece_to_distinct1_lag: -2
289	    max_lag_7_ece_to_distinct1_p: 0.0004
290	    max_lag_7_entropy_to_distinct1_lag: -1
291	    max_lag_7_entropy_to_distinct1_p: 0.0018
292	    max_lag_7_entropy_to_ppl_lag: -5
293	    max_lag_7_entropy_to_ppl_p: 0.071
294	    max_lag_7_ece_to_ppl_lag: 0
295	    max_lag_7_ece_to_ppl_p: 0.412
296	    onset_2sigma_ece: gen 2.1±0.3
297	    onset_2sigma_entropy: gen 2.4±0.4
298	    onset_2sigma_distinct1: gen 3.8±0.5
299	    onset_2sigma_distinct2: gen 4.2±0.4
300	    onset_2sigma_ppl: gen 2.3±0.3
301	    cross_seed_consistency: 4/4 seeds for canary→diversity
302	  result_rationale: '在 α=1.0 (100% self-consuming) 下 collapse 极快，perplexity onset（gen
303	    ~2.3） 与 canary onset（gen ~2.1-2.4）几乎同步——drift rate 太快，metric sensitivity 差异 不足以产生可检测的
304	    lead。max_lag=7 不改变 canary→diversity 的结论（lag=-2/-1 稳定）， 因为 diversity onset 确实延后到
305	    gen 3.8-4.2。token_entropy→ppl 的 lag=-5 在 max_lag=7 下保持但 p 值从边界上升到 0.071——这不是截断伪影而是统计
306	    noise， 因为 100% SC 下两者实际同步崩溃（onset 差 <0.3 gen），VAR 模型在短序列上 拟合出的 lag=-5 缺乏统计支撑。这进一步支持
307	    Claim 2 的 regime-dependent 叙事。
308	
309	    '
310	  tables:
311	  - name: 'Table S1: MVP (α=1.0) TY Results — max_lag=5 vs max_lag=7'
312	    columns:
313	    - Pair
314	    - max_lag=5 (lag, p)
315	    - max_lag=7 (lag, p)
316	    - Conclusion
317	    rows:
318	    - - ECE→distinct_1
319	      - (-2, <0.001)
320	      - (-2, 0.0004)
321	      - Stable — genuine lead
322	    - - ECE→distinct_2
323	      - (-1, 0.003)
324	      - (-1, 0.004)
325	      - Stable
326	    - - entropy→distinct_1
327	      - (-1, 0.002)
328	      - (-1, 0.0018)
329	      - Stable
330	    - - entropy→ppl
331	      - (-5, 0.052)
332	      - (-5, 0.071)
333	      - Not significant — noise
334	    - - ECE→ppl
335	      - (0, 0.38)
336	      - (0, 0.412)
337	      - Not significant — synchronous
338	  figures_description:
339	  - 'Fig S1: MVP 4-seed collapse trajectories — standardized z-score，带 2σ onset 标记线。可视化
340	    ECE/entropy onset 领先 distinct_1/2 但与 perplexity 同步。'
341	  analysis: 'max_lag=7 确认 MVP 核心结论不变。entropy→ppl lag=-5 是噪声非截断—— 在 α=1.0 下 canary
342	    不 lead perplexity 的结论更加稳固， 为 α-sweep 中低 α 下 lead 出现提供对比 baseline。
343	
344	    '
345	- name: C4 Cross-domain Validation
346	  plan_id: plan_004
347	  description: 'Pythia-410M × C4 × α=0.50 × 3 seeds × 10 gen。验证 WikiText-103 上 确认的
348	    canary ranking 和 lead time 是否在不同 domain 数据上保持。
349	
350	    '
351	  expected_results:
352	    c4_alpha050_gen10_perplexity: 211.8
353	    c4_alpha050_gen10_token_entropy: 1.88
354	    c4_alpha050_gen10_ece: 0.261
355	    c4_alpha050_gen10_distinct_1: 0.183
356	    c4_alpha050_gen10_distinct_2: 0.494
357	    c4_alpha050_canary_diversity_lead_gen: 1.8
358	    c4_alpha050_canary_perplexity_lead_gen: 1.0
359	    c4_alpha050_TY_ece_to_d1_p: 0.003
360	    c4_alpha050_TY_entropy_to_d1_p: 0.006
361	    c4_alpha050_TY_ece_to_ppl_p: 0.044
362	    canary_ranking_preserved: true
363	    rank_correlation_wiki_vs_c4: 0.94
364	  result_rationale: 'Canary metric 的 lead 机制是 distribution-level 的——ECE 检测 calibration
365	    drift， token entropy 检测 vocabulary concentration——这两个现象在任何 iterative self-consuming
366	    训练中都会发生，不依赖于 domain-specific 的 token 分布。C4 是 web crawl 数据， vocabulary 更多样、初始 distinct_n
367	    更高，但 iterative training 仍然驱动 mode collapse（vocabulary 收缩到高频 pattern）。绝对指标值会因 domain
368	    差异 而不同（C4 初始 perplexity 稍高、entropy 稍低因为 web text 噪声更大）， 但相对 ranking（ECE 和 entropy
369	    领先 diversity，diversity 领先 perplexity） 和 lead time 量级（~1.8 gen for diversity, ~1.0
370	    gen for perplexity at α=0.50） 应保持，因为底层的 distributional drift dynamics 是 model-intrinsic
371	    而非 data-specific。 Rank correlation 0.94 反映个别 pair 的精确 lag 可能差 ±0.5 gen 但排序一致。
372	
373	    '
374	  tables:
375	  - name: 'Table 5: Cross-domain Comparison (α=0.50)'
376	    columns:
377	    - Metric pair
378	    - WikiText-103 (lag, p)
379	    - C4 (lag, p)
380	    - Δlag
381	    rows:
382	    - - ECE→distinct_1
383	      - (-2, <0.001)
384	      - (-2, 0.003)
385	      - '0'
386	    - - entropy→distinct_1
387	      - (-2, 0.004)
388	      - (-2, 0.006)
389	      - '0'
390	    - - ECE→ppl
391	      - (-1, 0.032)
392	      - (-1, 0.044)
393	      - '0'
394	    - - entropy→ppl
395	      - (-1, 0.041)
396	      - (-1, 0.058)
397	      - '0'
398	    - - eff_rank→distinct_1
399	      - (0, 0.287)
400	      - (0, 0.334)
401	      - '0'
402	  figures_description:
403	  - 'Fig 6: Side-by-side collapse trajectories — WikiText-103 vs C4 at α=0.50。形态相似，绝对值不同，onset
404	    timing 保持。'
405	  analysis: 'C4 验证 canary ranking 的 domain-invariance。ECE 和 entropy 在两个 domain 上 对
406	    diversity 的 lead 一致（lag=-2），对 perplexity 的 lead 也一致（lag=-1）。 effective_rank 在两个
407	    domain 均失败，排除其作为 canary 的可能。 这支持 canary 机制是 model-intrinsic 的论断。
408	
409	    '
410	- name: Pythia-1.4B Scale Spot-check
411	  plan_id: plan_005
412	  description: 'Pythia-1.4B × WikiText-103 × α=0.50 × 3 seeds × 10 gen。 验证 canary
413	    lead 是否在 3.4× 参数量下保持。
414	
415	    '
416	  expected_results:
417	    scale_1.4b_gen10_perplexity: 142.5
418	    scale_1.4b_gen10_token_entropy: 2.12
419	    scale_1.4b_gen10_ece: 0.198
420	    scale_1.4b_gen10_distinct_1: 0.241
421	    scale_1.4b_gen10_distinct_2: 0.589
422	    scale_1.4b_canary_diversity_lead_gen: 2.3
423	    scale_1.4b_canary_perplexity_lead_gen: 1.5
424	    scale_1.4b_TY_ece_to_d1_p: 0.002
425	    scale_1.4b_TY_entropy_to_d1_p: 0.004
426	    scale_1.4b_TY_ece_to_ppl_p: 0.028
427	    canary_ranking_preserved: true
428	    lead_time_scaling_trend: slightly longer at larger scale
429	  result_rationale: '更大模型有更高的初始 capacity 和更好的 calibration（gen0 ECE 更低）， collapse 在每代的
430	    marginal degradation 更小（模型能更好地 fit 混合数据）， 但 cumulative drift 仍然驱动最终退化。关键推断：如果每代
431	    drift 更小， 不同 metric family 的 sensitivity gap 有更多代数来积累差异—— ECE 可能在 gen 2 就 onset
432	    而 distinct_1 在 gen 4.5， 比 410M 的 gen 2.5/4.0 差距更大，lead time 从 2.0 增加到 ~2.3 gen。
433	    Perplexity 也更渐进（gen10 ppl 142 vs 410M 的 189）， canary→ppl lead 从 1.3 增加到 ~1.5 gen。这个
434	    scaling trend（更大模型→更长 lead time） 如果成立将是一个有吸引力的 finding——意味着 canary 在实际部署的大模型上
435	    预警窗口更宽，实用价值更高。3/3 seed consistency 因为更大模型的 variance 更低。
436	
437	    '
438	  tables:
439	  - name: 'Table 6: Scale Comparison at α=0.50'
440	    columns:
441	    - Model
442	    - gen10_ppl
443	    - canary→d1 lead
444	    - canary→ppl lead
445	    - TY p (ECE→d1)
446	    - TY p (ECE→ppl)
447	    rows:
448	    - - Pythia-410M
449	      - '189.3'
450	      - 2.0 gen
451	      - 1.3 gen
452	      - <0.005
453	      - '0.032'
454	    - - Pythia-1.4B
455	      - '142.5'
456	      - 2.3 gen
457	      - 1.5 gen
458	      - '0.002'
459	      - '0.028'
460	  figures_description:
461	  - 'Fig 7: 410M vs 1.4B collapse trajectory overlay — 1.4B 曲线更平缓但形态一致，onset 标记显示
462	    1.4B 的 canary-target gap 更宽。'
463	  analysis: 'Scale spot-check 确认 canary lead 跨规模保持，且有 lead time 随 scale 增加的趋势。 虽然单点验证不能
464	    claim scaling law，但方向性结论支持实用价值论述。 Limitation 中需注明：仅验证到 1.4B，更大规模（7B+）是 future
465	    work。
466	
467	    '
468	- name: Extended Run 20 gen (α=1.0, max_lag=10)
469	  plan_id: plan_006
470	  description: 'Pythia-410M × WikiText-103 × α=1.0 × 20 gen × 2 seeds。 验证 entropy→ppl
471	    lag=-5 是否为 max_lag 截断伪影。
472	
473	    '
474	  expected_results:
475	    gen20_perplexity: 4287.3
476	    gen20_token_entropy: 0.68
477	    gen20_ece: 0.512
478	    gen20_distinct_1: 0.024
479	    gen20_distinct_2: 0.108
480	    extended_TY_entropy_to_ppl_lag: 0
481	    extended_TY_entropy_to_ppl_p: 0.523
482	    extended_TY_ece_to_d1_lag: -2
483	    extended_TY_ece_to_d1_p: 0.0002
484	    canary_diversity_lead_gen_20gen: 1.8
485	    collapse_saturation_gen: 12
486	  result_rationale: '延长到 20 gen 提供两个信息：(1) max_lag=10 下 entropy→ppl 仍无显著 lead（lag=0,
487	    p=0.52）， 确认 α=1.0 下 canary 不 lead perplexity 是 genuine 结论非截断伪影—— 因为 100% SC 的
488	    drift rate 太快，所有 metrics 在 gen 1-5 内同步急剧退化； (2) gen 12 后 collapse 趋于饱和（perplexity
489	    增长率下降，因为模型输出已近乎 deterministic），这个 saturation 行为为 phase diagram 增加了一个维度—— 不仅 α
490	    影响可预测性，generation depth 也有影响（但 best tier 下这是 supplementary observation，不是 main
491	    claim）。canary→diversity lead 在 20 gen 下保持（~1.8 gen）， 确认 diversity 通道的可预测性在极端 regime
492	    和长 horizon 下稳健。
493	
494	    '
495	  tables:
496	  - name: 'Table S2: Extended Run TY Results (max_lag=10)'
497	    columns:
498	    - Pair
499	    - 10-gen (lag, p)
500	    - 20-gen (lag, p)
501	    - Conclusion
502	    rows:
503	    - - entropy→ppl
504	      - (-5, 0.071)
505	      - (0, 0.523)
506	      - No lead — confirmed
507	    - - ECE→distinct_1
508	      - (-2, 0.0004)
509	      - (-2, 0.0002)
510	      - Stable lead — confirmed
511	    - - ECE→ppl
512	      - (0, 0.412)
513	      - (0, 0.487)
514	      - No lead — confirmed
515	  figures_description:
516	  - 'Fig S2: 20-gen collapse trajectory — 所有 metrics 在 gen 12 后进入饱和平台，canary→diversity
517	    lead 在前 10 gen 内建立并保持。'
518	  analysis: 'Extended run 排除截断伪影质疑。α=1.0 下 canary→ppl 的 absence 是 robust 结论， 不受 max_lag
519	    或 sequence length 影响。结果放 supplementary 即可。
520	
521	    '
522	- name: CRS Intervention 实验
523	  plan_id: plan_007
524	  description: 'CRS-predictive intervention vs no-intervention baseline。 Pythia-410M
525	    × α=0.75 × 3 seeds × 10 gen。 当 ECE 2σ onset 触发时自动增加 real data ratio。
526	
527	    '
528	  expected_results:
529	    no_intervention_gen10_distinct1: 0.112
530	    crs_intervention_gen10_distinct1: 0.198
531	    diversity_preservation_pct: 76.8
532	    intervention_trigger_gen: gen 3.2±0.4
533	    post_intervention_alpha_effective: 0.52
534	    gen10_perplexity_no_intervention: 512.7
535	    gen10_perplexity_crs: 341.2
536	    perplexity_reduction_pct: 33.4
537	  result_rationale: 'CRS 在 ECE onset（~gen 3）时将 α 从 0.75 降到 ~0.52（增加 real data 比例），
538	    等效于将训练轨迹从 α=0.75 regime "切换"到 α≈0.50 regime。 从 α-sweep 数据我们知道 α=0.50 的 gen10 distinct_1
539	    ≈ 0.198 vs α=0.75 的 0.112， 所以 intervention 后的 gen10 diversity 应接近 α=0.50 的水平。
540	    Perplexity 也相应改善（从 ~513 降到 ~341，接近 α=0.50 和 α=0.75 的中间值， 因为前 3 代仍在 α=0.75 下训练积累了部分
541	    drift）。 76.8% diversity preservation = (0.198 - 0.112) / (0.312 - 0.112) × 100%，
542	    即恢复了从 α=0.75 到 α=0.25 baseline 之间 ~77% 的 diversity gap。 这不是 perfect recovery 因为前几代的
543	    drift 不可逆，但足以证明 predictive intervention 的实用价值——canary 提供的 1-2 gen 预警窗口转化为可操作的
544	    diversity 保护。
545	
546	    '
547	  tables:
548	  - name: 'Table 7: Intervention Results (α=0.75, mean across 3 seeds)'
549	    columns:
550	    - Condition
551	    - gen10_d1
552	    - gen10_d2
553	    - gen10_ppl
554	    - gen10_ece
555	    rows:
556	    - - No intervention (α=0.75)
557	      - 0.112±0.011
558	      - 0.402±0.025
559	      - 512.7±31.4
560	      - 0.361±0.021
561	    - - CRS-predictive (trigger @ ECE onset)
562	      - 0.198±0.015
563	      - 0.524±0.020
564	      - 341.2±22.7
565	      - 0.253±0.018
566	    - - Oracle (α=0.50 throughout)
567	      - 0.198±0.014
568	      - 0.512±0.019
569	      - 189.3±12.6
570	      - 0.247±0.015
571	  figures_description:
572	  - 'Fig 8: Intervention trajectory — no-intervention vs CRS vs oracle (α=0.50)。vertical
573	    dashed line at intervention trigger gen。CRS 轨迹在 trigger 后弯向 oracle 轨迹但不完全重合（前几代
574	    drift 残留）。'
575	  analysis: 'Intervention 实验将 canary 的预测能力转化为可操作的 collapse mitigation。 CRS 的 diversity
576	    preservation 接近 oracle level 说明 ECE onset 的 timing 足够早。 Perplexity 恢复不如 oracle
577	    因为前 3 代在高 α 下的 calibration drift 不可逆。 P2 优先级——如果时间紧可砍，但如果包含将显著提升 practical contribution。
578	
579	    '
580	- name: Accumulate vs Replace 数据策略 Ablation
581	  plan_id: plan_008
582	  description: 'α=0.50 下 accumulate（保留所有历史生成数据）vs replace（每代仅用最新生成数据） 对比 × 3 seeds
583	    × 10 gen。
584	
585	    '
586	  expected_results:
587	    replace_gen10_distinct1: 0.198
588	    accumulate_gen10_distinct1: 0.267
589	    replace_gen10_ppl: 189.3
590	    accumulate_gen10_ppl: 124.8
591	    accumulate_canary_diversity_lead: 2.5
592	    replace_canary_diversity_lead: 2.0
593	    accumulate_canary_ppl_lead: 1.8
594	    replace_canary_ppl_lead: 1.3
595	    accumulate_collapse_rate_reduction_pct: 34.2
596	  result_rationale: 'Accumulate 模式保留所有历史生成数据，训练集 diversity 衰减更慢—— 每代新增的合成数据只占总数据的
597	    1/(gen+1) 而非 replace 模式下的 α 比例， effective contamination ratio 随代数递减。Fu et al.
598	    理论预测 accumulate 在 足够代数后收敛（distribution drift bounded），而 replace 可能发散。 在 10 gen
599	    内，accumulate 的 gen10 metrics 显著优于 replace（distinct_1 0.267 vs 0.198）， collapse
600	    更渐进意味着 metric sensitivity gap 有更多代数积累—— canary→diversity lead 从 2.0 增加到 2.5 gen，canary→ppl
601	    lead 从 1.3 增加到 1.8 gen。 这对 practical implication 有意义：accumulate 策略不仅减缓 collapse，
602	    还扩大了 canary 预警窗口。
603	
604	    '
605	  tables:
606	  - name: 'Table 8: Data Strategy Comparison (α=0.50)'
607	    columns:
608	    - Strategy
609	    - gen10_d1
610	    - gen10_ppl
611	    - canary→d1 lead
612	    - canary→ppl lead
613	    rows:
614	    - - Replace
615	      - 0.198±0.014
616	      - 189.3±12.6
617	      - 2.0 gen
618	      - 1.3 gen
619	    - - Accumulate
620	      - 0.267±0.016
621	      - 124.8±9.3
622	      - 2.5 gen
623	      - 1.8 gen
624	  figures_description:
625	  - 'Fig S3: Accumulate vs Replace trajectories — accumulate 曲线更平缓，onset delay 更大，canary-target
626	    gap 可视化更宽。'
627	  analysis: Accumulate ablation 验证 Fu et al. 理论预测的同时发现一个新 finding： 数据策略不仅影响 collapse
628	    severity，还影响 canary lead time—— 更渐进的 collapse 给予更长的预警窗口。P2 优先级但如果包含增加 paper depth。
629	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "117ede09-664b-4803-96a5-935058448e31",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "42665016-fceb-4c1a-9cd9-cae70a6f2887",
  "sourceToolAssistantUUID": "117ede09-664b-4803-96a5-935058448e31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T19:22:05.849Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DXLCrvy8fYnpwAdMTbDtM2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42665016-fceb-4c1a-9cd9-cae70a6f2887",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31FKYbrAW9SESYGH9NP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8420dc6-1b1f-4259-9b27-0163f4c1bd21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzBarw8RmnhQCka4UN2KmX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 26993,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 26993,
          "cache_creation_input_tokens": 10154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10154,
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

_source line 35 · 2026-05-14T19:22:05.853Z_

<details><summary>↩ Tool result · `toolu_01DXLCrvy8fYnpwAdMTbDtM2`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 三条 claims 全部成立。α-sweep 揭示清晰的 predictability phase
3	  transition： α≤0.50 下 canary→perplexity lead 出现（1-2 gen），α*≈0.60 划定可预测/不可预测边界。 方法论贡献独立成立——naive
4	  correlation 在非平稳序列上产生 ~40% 伪显著关联被 TY 推翻。 Cross-domain 和 scale spot-check 均保持 canary
5	  ranking。Headline 无需修改，直投 AAAI full paper。
6	
7	  '
8	imagined_experiments:
9	- name: α-sweep (α∈{0.25, 0.50, 0.75})
10	  plan_id: plan_001
11	  description: 'Pythia-410M × WikiText-103 × α∈{0.25, 0.50, 0.75} × 3 seeds × 10 gen
12	    iterative training。 每代计算 ECE、token_entropy、effective_rank、self_bleu、distinct_1/2/3、perplexity。
13	    Toda-Yamamoto panel temporal precedence 检验所有 canary→target 对。
14	
15	    '
16	  expected_results:
17	    alpha_0.25_gen10_perplexity: 68.4
18	    alpha_0.25_gen10_token_entropy: 2.41
19	    alpha_0.25_gen10_ece: 0.138
20	    alpha_0.25_gen10_distinct_1: 0.312
21	    alpha_0.25_gen10_distinct_2: 0.681
22	    alpha_0.25_canary_diversity_lead_gen: 2.7
23	    alpha_0.25_canary_perplexity_lead_gen: 2.0
24	    alpha_0.25_TY_canary_to_diversity_p: 0.002
25	    alpha_0.25_TY_canary_to_perplexity_p: 0.018
26	    alpha_0.25_effect_size_r_ece_distinct1: 0.97
27	    alpha_0.50_gen10_perplexity: 189.3
28	    alpha_0.50_gen10_token_entropy: 1.94
29	    alpha_0.50_gen10_ece: 0.247
30	    alpha_0.50_gen10_distinct_1: 0.198
31	    alpha_0.50_gen10_distinct_2: 0.512
32	    alpha_0.50_canary_diversity_lead_gen: 2.0
33	    alpha_0.50_canary_perplexity_lead_gen: 1.3
34	    alpha_0.50_TY_canary_to_diversity_p: 0.001
35	    alpha_0.50_TY_canary_to_perplexity_p: 0.032
36	    alpha_0.50_effect_size_r_ece_distinct1: 0.96
37	    alpha_0.75_gen10_perplexity: 512.7
38	    alpha_0.75_gen10_token_entropy: 1.52
39	    alpha_0.75_gen10_ece: 0.361
40	    alpha_0.75_gen10_distinct_1: 0.112
41	    alpha_0.75_gen10_distinct_2: 0.402
42	    alpha_0.75_canary_diversity_lead_gen: 1.7
43	    alpha_0.75_canary_perplexity_lead_gen: 0.3
44	    alpha_0.75_TY_canary_to_diversity_p: 0.003
45	    alpha_0.75_TY_canary_to_perplexity_p: 0.214
46	    alpha_0.75_effect_size_r_ece_distinct1: 0.96
47	    phase_boundary_alpha_star: 0.6
48	    cross_seed_consistency_diversity_lead: 3/3 seeds at all α
49	    cross_seed_consistency_perplexity_lead: 3/3 seeds at α≤0.50; 1/3 at α=0.75
50	  result_rationale: 'α 控制每代训练数据中合成数据的比例。低 α 下真实数据作为 anchor 减缓 distribution drift，
51	    collapse 从 catastrophic（α=1.0 时 gen10 ppl>1000）变为 gradual（α=0.25 时 gen10 ppl~68）。
52	    渐进退化使不同 metric family 的 onset timing 解耦——calibration（ECE）和 token distribution
53	    （entropy）对微小 distribution shift 最敏感（单代内 KL divergence 变化即可触发 2σ onset）， 而 diversity（distinct_n）需要
54	    vocabulary 实质收缩才反映，perplexity 则需 loss landscape 发生结构性改变。在 α=1.0（MVP）下三者近乎同步崩溃（1-2
55	    gen window），因为 drift 速度 压倒了 sensitivity 差异。降低 α 拉长 collapse timeline，sensitivity
56	    差异被放大： ECE onset 出现在 gen 2-3 而 distinct_1 onset 在 gen 5-6（α=0.25），产生 ~2.7 gen
57	    lead。 Perplexity 的可预测性取决于 drift 是否足够慢让 canary signal 积累足够 lead——α=0.25/0.50 下
58	    drift rate 允许 1-2 gen canary→perplexity lead，但 α=0.75 时 drift 过快， perplexity 几乎与
59	    canary 同步变化，TY 检验不再显著（p=0.214）。 Phase boundary α*≈0.60 是 perplexity lead 从统计显著跌落到不显著的转折点——
60	    这是 drift rate 与 metric sensitivity gap 的临界平衡点。
61	
62	    '
63	  tables:
64	  - name: 'Table 1: α-sweep Summary Statistics (mean ± std across seeds)'
65	    columns:
66	    - α
67	    - gen10_ppl
68	    - gen10_entropy
69	    - gen10_ece
70	    - gen10_d1
71	    - gen10_d2
72	    - canary→d1 lead (gen)
73	    - canary→ppl lead (gen)
74	    - TY p (canary→d1)
75	    - TY p (canary→ppl)
76	    rows:
77	    - - '0.25'
78	      - 68.4±4.1
79	      - 2.41±0.05
80	      - 0.138±0.009
81	      - 0.312±0.018
82	      - 0.681±0.022
83	      - 2.7±0.3
84	      - 2.0±0.4
85	      - <0.005
86	      - '0.018'
87	    - - '0.50'
88	      - 189.3±12.6
89	      - 1.94±0.07
90	      - 0.247±0.015
91	      - 0.198±0.014
92	      - 0.512±0.019
93	      - 2.0±0.2
94	      - 1.3±0.3
95	      - <0.005
96	      - '0.032'
97	    - - '0.75'
98	      - 512.7±31.4
99	      - 1.52±0.09
100	      - 0.361±0.021
101	      - 0.112±0.011
102	      - 0.402±0.025
103	      - 1.7±0.2
104	      - 0.3±0.5
105	      - <0.005
106	      - '0.214'
107	    - - 1.00 (MVP)
108	      - 1024.7±16.8
109	      - 1.27±0.06
110	      - 0.420±0.012
111	      - 0.075±0.008
112	      - 0.365±0.015
113	      - 1.5±0.3
114	      - 0.0±0.2
115	      - <0.001
116	      - '0.487'
117	  - name: 'Table 2: Toda-Yamamoto Panel Results — All Canary→Target Pairs'
118	    columns:
119	    - canary
120	    - target
121	    - α=0.25 (lag, p)
122	    - α=0.50 (lag, p)
123	    - α=0.75 (lag, p)
124	    - α=1.0 (lag, p)
125	    rows:
126	    - - ECE
127	      - distinct_1
128	      - (-3, <0.001)
129	      - (-2, <0.001)
130	      - (-2, 0.003)
131	      - (-2, <0.001)
132	    - - ECE
133	      - distinct_2
134	      - (-3, 0.002)
135	      - (-2, 0.002)
136	      - (-2, 0.006)
137	      - (-1, 0.004)
138	    - - token_entropy
139	      - distinct_1
140	      - (-2, 0.003)
141	      - (-2, 0.004)
142	      - (-1, 0.012)
143	      - (-1, 0.003)
144	    - - token_entropy
145	      - distinct_2
146	      - (-3, 0.004)
147	      - (-2, 0.006)
148	      - (-2, 0.018)
149	      - (-1, 0.009)
150	    - - ECE
151	      - perplexity
152	      - (-2, 0.015)
153	      - (-1, 0.032)
154	      - (0, 0.187)
155	      - (0, 0.412)
156	    - - token_entropy
157	      - perplexity
158	      - (-2, 0.021)
159	      - (-1, 0.041)
160	      - (0, 0.238)
161	      - (-5*, 0.063)
162	    - - effective_rank
163	      - distinct_1
164	      - (0, 0.342)
165	      - (0, 0.287)
166	      - (0, 0.415)
167	      - (0, 0.523)
168	    - - self_bleu
169	      - distinct_1
170	      - (0, 0.178)
171	      - (0, 0.221)
172	      - (-1, 0.089)
173	      - (0, 0.156)
174	  figures_description:
175	  - 'Fig 1: Predictability Phase Diagram — x-axis α∈[0,1], y-axis target metric (distinct_1,
176	    distinct_2, perplexity)。每个 cell 色标 = TY-estimated lead time (gen)，灰色 = not significant。清晰可见
177	    α*≈0.60 处 perplexity 行从有色变灰的 boundary。diversity 行全程有色。'
178	  - 'Fig 2: 四面板 collapse trajectory — 每面板一个 α，x-axis generation, y-axis 标准化 metric
179	    (z-score)。ECE 和 entropy 曲线领先 distinct_1/2，低 α 下 gap 明显加宽。Perplexity 曲线在 α≤0.50
180	    面板中可见延迟，在 α≥0.75 中与 canary 同步。'
181	  - 'Fig 3: Canary lead time vs α — x-axis α, y-axis TY-estimated lead (gen)。canary→diversity
182	    线近乎单调递增（随 α 降低 lead 增加），canary→perplexity 线在 α*≈0.60 处 drop to zero。误差带 = seed
183	    std。'
184	  analysis: 'α-sweep 是全文核心实验。Phase diagram 将三条 claims 统一为一张图： diversity 通道全 regime
185	    可预测（Claim 1），perplexity 通道 regime-dependent（Claim 2）， α* boundary 明确。effective_rank
186	    和 self_bleu 在所有 α 下均不显著—— 与 MVP 结论一致，排除选择偏差质疑。3 seeds 在所有 α 下 diversity lead 一致性
187	    3/3， perplexity lead 在 α≤0.50 下 3/3，α=0.75 下仅 1/3（边界行为，符合 phase transition 预期）。
188	
189	    '
190	- name: '方法论 ablation: Naive vs Robust 检验'
191	  plan_id: plan_002
192	  description: '在 MVP 4-seed 数据 + α-sweep 9 runs 数据上，对比四种 lead-lag 量化方法： (i) naive
193	    Pearson lag-correlation (ii) 差分后 cross-correlation (iii) threshold-based onset
194	    lead (iv) Toda-Yamamoto panel temporal precedence。 统计所有方法对所有 canary→target pair
195	    的显著性判定，量化伪显著被推翻比例。
196	
197	    '
198	  expected_results:
199	    total_pairs_tested: 104
200	    naive_pearson_significant_count: 71
201	    differenced_xcorr_significant_count: 48
202	    threshold_onset_significant_count: 39
203	    TY_significant_count: 42
204	    naive_overturned_by_TY_pct: 40.8
205	    naive_overturned_by_TY_count: 29
206	    false_positive_category_breakdown:
207	      effective_rank_pairs: 12
208	      self_bleu_pairs: 8
209	      canary_to_ppl_high_alpha: 6
210	      spurious_reverse_direction: 3
211	    TY_unique_significant_not_in_naive: 0
212	    method_agreement_TY_vs_threshold: 0.88
213	  result_rationale: '非平稳时间序列（所有 metric 在 iterative training 中趋势性退化）的 Pearson correlation
214	    产生 spurious regression——两个独立但都有趋势的序列可以 |r|>0.9。naive 方法对所有 "都在下降"的 metric pair
215	    报告显著，包括 effective_rank→diversity（实际无 lead-lag 关系， 只是共享下降趋势）和 canary→perplexity
216	    at α≥0.75（同步崩溃无因果方向）。 差分后去趋势消除部分伪关联但对短序列（10 gen）power 不足，false negative 较多。 TY
217	    方法在 VAR 框架中检验 Granger non-causality，自动处理非平稳性（通过 augmented lag），对真正的 lead-lag 关系（canary→diversity）保持高
218	    power（p<0.005）， 对无方向性的同步崩溃正确报告不显著（p>0.05）。~41% 的 naive 显著关联被推翻， 主要来自三类：(1) 失败
219	    canary 族的伪关联（effective_rank、self_bleu 与任何 target）， (2) 高 α 下 canary→perplexity
220	    的同步崩溃被误判为 lead， (3) 少数反向因果（target→canary）被 naive 双向 correlation 报告为显著。
221	
222	    '
223	  tables:
224	  - name: 'Table 3: Method Comparison — Significant Pair Counts'
225	    columns:
226	    - Method
227	    - Significant pairs
228	    - Agrees w/ TY
229	    - Disagrees w/ TY
230	    - False positive vs TY
231	    - False negative vs TY
232	    rows:
233	    - - Naive Pearson
234	      - 71/104
235	      - '42'
236	      - '29'
237	      - 29 (40.8%)
238	      - '0'
239	    - - Differenced XCorr
240	      - 48/104
241	      - '36'
242	      - '12'
243	      - 12 (16.9%)
244	      - '6'
245	    - - Threshold Onset
246	      - 39/104
247	      - '37'
248	      - '2'
249	      - 2 (2.8%)
250	      - '5'
251	    - - Toda-Yamamoto
252	      - 42/104
253	      - —
254	      - —
255	      - —
256	      - —
257	  - name: 'Table 4: Breakdown of Naive False Positives Overturned by TY'
258	    columns:
259	    - Category
260	    - Count
261	    - Example pair
262	    rows:
263	    - - Failed canary (eff_rank/self_bleu) → any target
264	      - '20'
265	      - effective_rank→distinct_1 at α=0.50
266	    - - canary→perplexity at α≥0.75
267	      - '6'
268	      - ECE→ppl at α=0.75
269	    - - Reverse direction (target→canary)
270	      - '3'
271	      - distinct_1→ECE at α=1.0
272	  figures_description:
273	  - 'Fig 4: Agreement matrix heatmap — 4 methods × 104 pairs，binary significant/not。visual
274	    clustering 显示 naive 方法在右上角大片''显著''区域被其他三种方法一致判定为不显著。'
275	  - 'Fig 5: Naive |r| vs TY p-value scatter — 每个 pair 一点，color = truly significant
276	    (TY) vs overturned。右上区域（高 |r| 但 TY p>0.05）包含所有 spurious regression 案例。'
277	  analysis: '~41% 伪显著率远超 30% 阈值，方法论贡献独立成立。这直接回应 reviewer concern "为什么不用简单相关"——答案是简单方法在这个
278	    setting 下系统性高估 canary 预测能力， 尤其是对失败 canary 和高 α regime。Threshold onset 与 TY 一致性高（88%），
279	    但 TY 提供 p-value 和方向性检验，统计论证更强。
280	
281	    '
282	- name: MVP 结果 formalization (max_lag=7)
283	  plan_id: plan_003
284	  description: '在 MVP 4-seed (α=1.0) 数据上重跑 TY 检验，max_lag 从 5 增大到 7， 验证 token_entropy→perplexity
285	    的 lag=-5 是否为截断伪影。 统一 2σ onset 定义，输出 paper-ready 数值。
286	
287	    '
288	  expected_results:
289	    max_lag_7_ece_to_distinct1_lag: -2
290	    max_lag_7_ece_to_distinct1_p: 0.0004
291	    max_lag_7_entropy_to_distinct1_lag: -1
292	    max_lag_7_entropy_to_distinct1_p: 0.0018
293	    max_lag_7_entropy_to_ppl_lag: -5
294	    max_lag_7_entropy_to_ppl_p: 0.071
295	    max_lag_7_ece_to_ppl_lag: 0
296	    max_lag_7_ece_to_ppl_p: 0.412
297	    onset_2sigma_ece: gen 2.1±0.3
298	    onset_2sigma_entropy: gen 2.4±0.4
299	    onset_2sigma_distinct1: gen 3.8±0.5
300	    onset_2sigma_distinct2: gen 4.2±0.4
301	    onset_2sigma_ppl: gen 2.3±0.3
302	    cross_seed_consistency: 4/4 seeds for canary→diversity
303	  result_rationale: '在 α=1.0 (100% self-consuming) 下 collapse 极快，perplexity onset（gen
304	    ~2.3） 与 canary onset（gen ~2.1-2.4）几乎同步——drift rate 太快，metric sensitivity 差异 不足以产生可检测的
305	    lead。max_lag=7 不改变 canary→diversity 的结论（lag=-2/-1 稳定）， 因为 diversity onset 确实延后到
306	    gen 3.8-4.2。token_entropy→ppl 的 lag=-5 在 max_lag=7 下保持但 p 值从边界上升到 0.071——这不是截断伪影而是统计
307	    noise， 因为 100% SC 下两者实际同步崩溃（onset 差 <0.3 gen），VAR 模型在短序列上 拟合出的 lag=-5 缺乏统计支撑。这进一步支持
308	    Claim 2 的 regime-dependent 叙事。
309	
310	    '
311	  tables:
312	  - name: 'Table S1: MVP (α=1.0) TY Results — max_lag=5 vs max_lag=7'
313	    columns:
314	    - Pair
315	    - max_lag=5 (lag, p)
316	    - max_lag=7 (lag, p)
317	    - Conclusion
318	    rows:
319	    - - ECE→distinct_1
320	      - (-2, <0.001)
321	      - (-2, 0.0004)
322	      - Stable — genuine lead
323	    - - ECE→distinct_2
324	      - (-1, 0.003)
325	      - (-1, 0.004)
326	      - Stable
327	    - - entropy→distinct_1
328	      - (-1, 0.002)
329	      - (-1, 0.0018)
330	      - Stable
331	    - - entropy→ppl
332	      - (-5, 0.052)
333	      - (-5, 0.071)
334	      - Not significant — noise
335	    - - ECE→ppl
336	      - (0, 0.38)
337	      - (0, 0.412)
338	      - Not significant — synchronous
339	  figures_description:
340	  - 'Fig S1: MVP 4-seed collapse trajectories — standardized z-score，带 2σ onset 标记线。可视化
341	    ECE/entropy onset 领先 distinct_1/2 但与 perplexity 同步。'
342	  analysis: 'max_lag=7 确认 MVP 核心结论不变。entropy→ppl lag=-5 是噪声非截断—— 在 α=1.0 下 canary
343	    不 lead perplexity 的结论更加稳固， 为 α-sweep 中低 α 下 lead 出现提供对比 baseline。
344	
345	    '
346	- name: C4 Cross-domain Validation
347	  plan_id: plan_004
348	  description: 'Pythia-410M × C4 × α=0.50 × 3 seeds × 10 gen。验证 WikiText-103 上 确认的
349	    canary ranking 和 lead time 是否在不同 domain 数据上保持。
350	
351	    '
352	  expected_results:
353	    c4_alpha050_gen10_perplexity: 211.8
354	    c4_alpha050_gen10_token_entropy: 1.88
355	    c4_alpha050_gen10_ece: 0.261
356	    c4_alpha050_gen10_distinct_1: 0.183
357	    c4_alpha050_gen10_distinct_2: 0.494
358	    c4_alpha050_canary_diversity_lead_gen: 1.8
359	    c4_alpha050_canary_perplexity_lead_gen: 1.0
360	    c4_alpha050_TY_ece_to_d1_p: 0.003
361	    c4_alpha050_TY_entropy_to_d1_p: 0.006
362	    c4_alpha050_TY_ece_to_ppl_p: 0.044
363	    canary_ranking_preserved: true
364	    rank_correlation_wiki_vs_c4: 0.94
365	  result_rationale: 'Canary metric 的 lead 机制是 distribution-level 的——ECE 检测 calibration
366	    drift， token entropy 检测 vocabulary concentration——这两个现象在任何 iterative self-consuming
367	    训练中都会发生，不依赖于 domain-specific 的 token 分布。C4 是 web crawl 数据， vocabulary 更多样、初始 distinct_n
368	    更高，但 iterative training 仍然驱动 mode collapse（vocabulary 收缩到高频 pattern）。绝对指标值会因 domain
369	    差异 而不同（C4 初始 perplexity 稍高、entropy 稍低因为 web text 噪声更大）， 但相对 ranking（ECE 和 entropy
370	    领先 diversity，diversity 领先 perplexity） 和 lead time 量级（~1.8 gen for diversity, ~1.0
371	    gen for perplexity at α=0.50） 应保持，因为底层的 distributional drift dynamics 是 model-intrinsic
372	    而非 data-specific。 Rank correlation 0.94 反映个别 pair 的精确 lag 可能差 ±0.5 gen 但排序一致。
373	
374	    '
375	  tables:
376	  - name: 'Table 5: Cross-domain Comparison (α=0.50)'
377	    columns:
378	    - Metric pair
379	    - WikiText-103 (lag, p)
380	    - C4 (lag, p)
381	    - Δlag
382	    rows:
383	    - - ECE→distinct_1
384	      - (-2, <0.001)
385	      - (-2, 0.003)
386	      - '0'
387	    - - entropy→distinct_1
388	      - (-2, 0.004)
389	      - (-2, 0.006)
390	      - '0'
391	    - - ECE→ppl
392	      - (-1, 0.032)
393	      - (-1, 0.044)
394	      - '0'
395	    - - entropy→ppl
396	      - (-1, 0.041)
397	      - (-1, 0.058)
398	      - '0'
399	    - - eff_rank→distinct_1
400	      - (0, 0.287)
401	      - (0, 0.334)
402	      - '0'
403	  figures_description:
404	  - 'Fig 6: Side-by-side collapse trajectories — WikiText-103 vs C4 at α=0.50。形态相似，绝对值不同，onset
405	    timing 保持。'
406	  analysis: 'C4 验证 canary ranking 的 domain-invariance。ECE 和 entropy 在两个 domain 上 对
407	    diversity 的 lead 一致（lag=-2），对 perplexity 的 lead 也一致（lag=-1）。 effective_rank 在两个
408	    domain 均失败，排除其作为 canary 的可能。 这支持 canary 机制是 model-intrinsic 的论断。
409	
410	    '
411	- name: Pythia-1.4B Scale Spot-check
412	  plan_id: plan_005
413	  description: 'Pythia-1.4B × WikiText-103 × α=0.50 × 3 seeds × 10 gen。 验证 canary
414	    lead 是否在 3.4× 参数量下保持。
415	
416	    '
417	  expected_results:
418	    scale_1.4b_gen10_perplexity: 142.5
419	    scale_1.4b_gen10_token_entropy: 2.12
420	    scale_1.4b_gen10_ece: 0.198
421	    scale_1.4b_gen10_distinct_1: 0.241
422	    scale_1.4b_gen10_distinct_2: 0.589
423	    scale_1.4b_canary_diversity_lead_gen: 2.3
424	    scale_1.4b_canary_perplexity_lead_gen: 1.5
425	    scale_1.4b_TY_ece_to_d1_p: 0.002
426	    scale_1.4b_TY_entropy_to_d1_p: 0.004
427	    scale_1.4b_TY_ece_to_ppl_p: 0.028
428	    canary_ranking_preserved: true
429	    lead_time_scaling_trend: slightly longer at larger scale
430	  result_rationale: '更大模型有更高的初始 capacity 和更好的 calibration（gen0 ECE 更低）， collapse 在每代的
431	    marginal degradation 更小（模型能更好地 fit 混合数据）， 但 cumulative drift 仍然驱动最终退化。关键推断：如果每代
432	    drift 更小， 不同 metric family 的 sensitivity gap 有更多代数来积累差异—— ECE 可能在 gen 2 就 onset
433	    而 distinct_1 在 gen 4.5， 比 410M 的 gen 2.5/4.0 差距更大，lead time 从 2.0 增加到 ~2.3 gen。
434	    Perplexity 也更渐进（gen10 ppl 142 vs 410M 的 189）， canary→ppl lead 从 1.3 增加到 ~1.5 gen。这个
435	    scaling trend（更大模型→更长 lead time） 如果成立将是一个有吸引力的 finding——意味着 canary 在实际部署的大模型上
436	    预警窗口更宽，实用价值更高。3/3 seed consistency 因为更大模型的 variance 更低。
437	
438	    '
439	  tables:
440	  - name: 'Table 6: Scale Comparison at α=0.50'
441	    columns:
442	    - Model
443	    - gen10_ppl
444	    - canary→d1 lead
445	    - canary→ppl lead
446	    - TY p (ECE→d1)
447	    - TY p (ECE→ppl)
448	    rows:
449	    - - Pythia-410M
450	      - '189.3'
451	      - 2.0 gen
452	      - 1.3 gen
453	      - <0.005
454	      - '0.032'
455	    - - Pythia-1.4B
456	      - '142.5'
457	      - 2.3 gen
458	      - 1.5 gen
459	      - '0.002'
460	      - '0.028'
461	  figures_description:
462	  - 'Fig 7: 410M vs 1.4B collapse trajectory overlay — 1.4B 曲线更平缓但形态一致，onset 标记显示
463	    1.4B 的 canary-target gap 更宽。'
464	  analysis: 'Scale spot-check 确认 canary lead 跨规模保持，且有 lead time 随 scale 增加的趋势。 虽然单点验证不能
465	    claim scaling law，但方向性结论支持实用价值论述。 Limitation 中需注明：仅验证到 1.4B，更大规模（7B+）是 future
466	    work。
467	
468	    '
469	- name: Extended Run 20 gen (α=1.0, max_lag=10)
470	  plan_id: plan_006
471	  description: 'Pythia-410M × WikiText-103 × α=1.0 × 20 gen × 2 seeds。 验证 entropy→ppl
472	    lag=-5 是否为 max_lag 截断伪影。
473	
474	    '
475	  expected_results:
476	    gen20_perplexity: 4287.3
477	    gen20_token_entropy: 0.68
478	    gen20_ece: 0.512
479	    gen20_distinct_1: 0.024
480	    gen20_distinct_2: 0.108
481	    extended_TY_entropy_to_ppl_lag: 0
482	    extended_TY_entropy_to_ppl_p: 0.523
483	    extended_TY_ece_to_d1_lag: -2
484	    extended_TY_ece_to_d1_p: 0.0002
485	    canary_diversity_lead_gen_20gen: 1.8
486	    collapse_saturation_gen: 12
487	  result_rationale: '延长到 20 gen 提供两个信息：(1) max_lag=10 下 entropy→ppl 仍无显著 lead（lag=0,
488	    p=0.52）， 确认 α=1.0 下 canary 不 lead perplexity 是 genuine 结论非截断伪影—— 因为 100% SC 的
489	    drift rate 太快，所有 metrics 在 gen 1-5 内同步急剧退化； (2) gen 12 后 collapse 趋于饱和（perplexity
490	    增长率下降，因为模型输出已近乎 deterministic），这个 saturation 行为为 phase diagram 增加了一个维度—— 不仅 α
491	    影响可预测性，generation depth 也有影响（但 best tier 下这是 supplementary observation，不是 main
492	    claim）。canary→diversity lead 在 20 gen 下保持（~1.8 gen）， 确认 diversity 通道的可预测性在极端 regime
493	    和长 horizon 下稳健。
494	
495	    '
496	  tables:
497	  - name: 'Table S2: Extended Run TY Results (max_lag=10)'
498	    columns:
499	    - Pair
500	    - 10-gen (lag, p)
501	    - 20-gen (lag, p)
502	    - Conclusion
503	    rows:
504	    - - entropy→ppl
505	      - (-5, 0.071)
506	      - (0, 0.523)
507	      - No lead — confirmed
508	    - - ECE→distinct_1
509	      - (-2, 0.0004)
510	      - (-2, 0.0002)
511	      - Stable lead — confirmed
512	    - - ECE→ppl
513	      - (0, 0.412)
514	      - (0, 0.487)
515	      - No lead — confirmed
516	  figures_description:
517	  - 'Fig S2: 20-gen collapse trajectory — 所有 metrics 在 gen 12 后进入饱和平台，canary→diversity
518	    lead 在前 10 gen 内建立并保持。'
519	  analysis: 'Extended run 排除截断伪影质疑。α=1.0 下 canary→ppl 的 absence 是 robust 结论， 不受 max_lag
520	    或 sequence length 影响。结果放 supplementary 即可。
521	
522	    '
523	- name: CRS Intervention 实验
524	  plan_id: plan_007
525	  description: 'CRS-predictive intervention vs no-intervention baseline。 Pythia-410M
526	    × α=0.75 × 3 seeds × 10 gen。 当 ECE 2σ onset 触发时自动增加 real data ratio。
527	
528	    '
529	  expected_results:
530	    no_intervention_gen10_distinct1: 0.112
531	    crs_intervention_gen10_distinct1: 0.198
532	    diversity_preservation_pct: 76.8
533	    intervention_trigger_gen: gen 3.2±0.4
534	    post_intervention_alpha_effective: 0.52
535	    gen10_perplexity_no_intervention: 512.7
536	    gen10_perplexity_crs: 341.2
537	    perplexity_reduction_pct: 33.4
538	  result_rationale: 'CRS 在 ECE onset（~gen 3）时将 α 从 0.75 降到 ~0.52（增加 real data 比例），
539	    等效于将训练轨迹从 α=0.75 regime "切换"到 α≈0.50 regime。 从 α-sweep 数据我们知道 α=0.50 的 gen10 distinct_1
540	    ≈ 0.198 vs α=0.75 的 0.112， 所以 intervention 后的 gen10 diversity 应接近 α=0.50 的水平。
541	    Perplexity 也相应改善（从 ~513 降到 ~341，接近 α=0.50 和 α=0.75 的中间值， 因为前 3 代仍在 α=0.75 下训练积累了部分
542	    drift）。 76.8% diversity preservation = (0.198 - 0.112) / (0.312 - 0.112) × 100%，
543	    即恢复了从 α=0.75 到 α=0.25 baseline 之间 ~77% 的 diversity gap。 这不是 perfect recovery 因为前几代的
544	    drift 不可逆，但足以证明 predictive intervention 的实用价值——canary 提供的 1-2 gen 预警窗口转化为可操作的
545	    diversity 保护。
546	
547	    '
548	  tables:
549	  - name: 'Table 7: Intervention Results (α=0.75, mean across 3 seeds)'
550	    columns:
551	    - Condition
552	    - gen10_d1
553	    - gen10_d2
554	    - gen10_ppl
555	    - gen10_ece
556	    rows:
557	    - - No intervention (α=0.75)
558	      - 0.112±0.011
559	      - 0.402±0.025
560	      - 512.7±31.4
561	      - 0.361±0.021
562	    - - CRS-predictive (trigger @ ECE onset)
563	      - 0.198±0.015
564	      - 0.524±0.020
565	      - 341.2±22.7
566	      - 0.253±0.018
567	    - - Oracle (α=0.50 throughout)
568	      - 0.198±0.014
569	      - 0.512±0.019
570	      - 189.3±12.6
571	      - 0.247±0.015
572	  figures_description:
573	  - 'Fig 8: Intervention trajectory — no-intervention vs CRS vs oracle (α=0.50)。vertical
574	    dashed line at intervention trigger gen。CRS 轨迹在 trigger 后弯向 oracle 轨迹但不完全重合（前几代
575	    drift 残留）。'
576	  analysis: 'Intervention 实验将 canary 的预测能力转化为可操作的 collapse mitigation。 CRS 的 diversity
577	    preservation 接近 oracle level 说明 ECE onset 的 timing 足够早。 Perplexity 恢复不如 oracle
578	    因为前 3 代在高 α 下的 calibration drift 不可逆。 P2 优先级——如果时间紧可砍，但如果包含将显著提升 practical contribution。
579	
580	    '
581	- name: Accumulate vs Replace 数据策略 Ablation
582	  plan_id: plan_008
583	  description: 'α=0.50 下 accumulate（保留所有历史生成数据）vs replace（每代仅用最新生成数据） 对比 × 3 seeds
584	    × 10 gen。
585	
586	    '
587	  expected_results:
588	    replace_gen10_distinct1: 0.198
589	    accumulate_gen10_distinct1: 0.267
590	    replace_gen10_ppl: 189.3
591	    accumulate_gen10_ppl: 124.8
592	    accumulate_canary_diversity_lead: 2.5
593	    replace_canary_diversity_lead: 2.0
594	    accumulate_canary_ppl_lead: 1.8
595	    replace_canary_ppl_lead: 1.3
596	    accumulate_collapse_rate_reduction_pct: 34.2
597	  result_rationale: 'Accumulate 模式保留所有历史生成数据，训练集 diversity 衰减更慢—— 每代新增的合成数据只占总数据的
598	    1/(gen+1) 而非 replace 模式下的 α 比例， effective contamination ratio 随代数递减。Fu et al.
599	    理论预测 accumulate 在 足够代数后收敛（distribution drift bounded），而 replace 可能发散。 在 10 gen
600	    内，accumulate 的 gen10 metrics 显著优于 replace（distinct_1 0.267 vs 0.198）， collapse
601	    更渐进意味着 metric sensitivity gap 有更多代数积累—— canary→diversity lead 从 2.0 增加到 2.5 gen，canary→ppl
602	    lead 从 1.3 增加到 1.8 gen。 这对 practical implication 有意义：accumulate 策略不仅减缓 collapse，
603	    还扩大了 canary 预警窗口。
604	
605	    '
606	  tables:
607	  - name: 'Table 8: Data Strategy Comparison (α=0.50)'
608	    columns:
609	    - Strategy
610	    - gen10_d1
611	    - gen10_ppl
612	    - canary→d1 lead
613	    - canary→ppl lead
614	    rows:
615	    - - Replace
616	      - 0.198±0.014
617	      - 189.3±12.6
618	      - 2.0 gen
619	      - 1.3 gen
620	    - - Accumulate
621	      - 0.267±0.016
622	      - 124.8±9.3
623	      - 2.5 gen
624	      - 1.8 gen
625	  figures_description:
626	  - 'Fig S3: Accumulate vs Replace trajectories — accumulate 曲线更平缓，onset delay 更大，canary-target
627	    gap 可视化更宽。'
628	  analysis: Accumulate ablation 验证 Fu et al. 理论预测的同时发现一个新 finding： 数据策略不仅影响 collapse
629	    severity，还影响 canary lead time—— 更渐进的 collapse 给予更长的预警窗口。P2 优先级但如果包含增加 paper depth。
630	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8420dc6-1b1f-4259-9b27-0163f4c1bd21",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "fc6baa02-743d-46e2-bfab-89cc5d10fcd6",
  "sourceToolAssistantUUID": "d8420dc6-1b1f-4259-9b27-0163f4c1bd21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-14T19:22:10.436Z_

Now let me also check the literature map and the experiment plan for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc6baa02-743d-46e2-bfab-89cc5d10fcd6",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31FjYjmd2FccTo45s6t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a77f6b4-97fc-4a73-8b7c-85f634c43cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRMB1EVBcvbhBQPnbpSERn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24713,
      "cache_read_input_tokens": 37147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24713,
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

_source line 37 · 2026-05-14T19:22:11.215Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016kf6iUYGMgibaH9PE9o7ac`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a77f6b4-97fc-4a73-8b7c-85f634c43cb1",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31FjYjmd2FccTo45s6t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2644dff9-91d3-4450-9c2b-ee27bf1a1149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRMB1EVBcvbhBQPnbpSERn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24713,
      "cache_read_input_tokens": 37147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24713,
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

_source line 38 · 2026-05-14T19:22:11.228Z_

<details><summary>↩ Tool result · `toolu_016kf6iUYGMgibaH9PE9o7ac`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # CORE MODEL COLLAPSE\\n  # ============================================================\\n  - id: \\\"shumailov2024curse\\\"\\n    title: \\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\"\\n    authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\"\\n    venue: \\\"Nature\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2305.17493\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\"\\n      - \\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\"\\n      - \\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\"\\n      - \\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\"\\n    relevance_to_us: \\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\"\\n    metrics_studied: [\\\"perplexity\\\", \\\"distributional tail mass\\\"]\\n\\n  - id: \\\"alemohammad2024mad\\\"\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"提出 Model Autophagy Disorder (MAD) 概念\\\"\\n      - \\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\"\\n      - \\\"在图像生成领域验证 self-consuming loop 的退化效应\\\"\\n    relevance_to_us: \\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\"\\n    metrics_studied: [\\\"FID\\\", \\\"precision\\\", \\\"recall\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"dohmatob2024tale\\\"\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.07043\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\\\"\\n      - \\\"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\\\"\\n      - \\\"混入少量干净数据可缓解 collapse 并引发 grokking 现象\\\"\\n      - \\\"在 transformer 算术任务和 Llama2 文本生成上验证\\\"\\n    relevance_to_us: \\\"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"scaling exponents\\\"]\\n\\n  - id: \\\"dohmatob2025strong\\\"\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n    venue: \\\"ICLR 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"即使合成数据占比极小（1/1000），仍可导致 model collapse\\\"\\n      - \\\"更大的训练集并不能避免 collapse\\\"\\n      - \\\"更大的模型（random projection 近似下）反而可能放大 collapse\\\"\\n      - \\\"存在 interpolation threshold 的 double-descent 现象\\\"\\n    relevance_to_us: \\\"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"guo2024linguistic\\\"\\n    title: \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\"\\n    authors: \\\"Yanzhu Guo, Guokan Shang, et al.\\\"\\n    venue: \\\"NAACL 2024 Findings\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.09807\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"evaluation\\\"\\n    key_findings:\\n      - \\\"递归微调中，linguistic diversity 在连续迭代中持续下降\\\"\\n      - \\\"创造性任务中 diversity 下降最显著\\\"\\n      - \\\"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\\\"\\n    relevance_to_us: \\\"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\\\"\\n    metrics_studied: [\\\"distinct-n\\\", \\\"type-token ratio\\\", \\\"syntactic diversity\\\", \\\"semantic diversity\\\"]\\n\\n  - id: \\\"briesch2024selfconsuming\\\"\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: \\\"Martin Briesch, Dominik Sobania, Franz Rothlauf\\\"\\n    venue: \\\"arXiv (2311.16822)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.16822\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"首次系统研究 LLM 的 self-consuming training loop\\\"\\n      - \\\"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\\\"\\n      - \\\"expanding data cycle（累积）在 50 代内保持 diversity\\\"\\n    relevance_to_us: \\\"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\\\"\\n    metrics_studied: [\\\"diversity\\\", \\\"quality\\\"]\\n\\n  - id: \\\"truong2025entropy\\\"\\n    title: \\\"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\\\"\\n    authors: \\\"Truong Xuan Khanh, Truong Quynh Hoa\\\"\\n    venue: \\\"arXiv (2512.12381)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2512.12381\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\\\"\\n      - \\\"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\\\"\\n      - \\\"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\\\"\\n    relevance_to_us: \\\"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\\\"\\n    gaps: \\\"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"autocorrelation\\\", \\\"variance\\\"]\\n\\n  - id: \\\"wang2026contaminated\\\"\\n    title: \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\"\\n    authors: \\\"Kevin Wang, Hongqian Niu, Didong Li\\\"\\n    venue: \\\"arXiv (2602.16065)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.16065\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\\\"\\n      - \\\"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\\\"\\n      - \\\"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\\\"\\n    relevance_to_us: \\\"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\\\"\\n    gaps: \\\"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\\\"\\n    metrics_studied: [\\\"convergence rate\\\", \\\"population risk\\\"]\\n\\n  # ============================================================\\n  # CANARY / EARLY WARNING METRICS\\n  # ============================================================\\n  - id: \\\"chen2025scales\\\"\\n    title: \\\"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv (2510.05133)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.05133\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\\\"\\n      - \\\"20% synthetic data 以下性能稳定，30% 以上退化加速\\\"\\n      - \\\"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\\\"\\n      - \\\"推理任务比检索任务更易退化\\\"\\n      - \\\"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\\\"\\n    relevance_to_us: \\\"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\", \\\"perplexity\\\"]\\n\\n  - id: \\\"gambetta2024surplexity\\\"\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: \\\"Daniele Gambetta et al.\\\"\\n    venue: \\\"arXiv (2410.12341)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\\\"\\n      - \\\"用 semantic networks 分析文本重复性和语义多样性\\\"\\n      - \\\"用 next-token probability 定量衡量 diversity loss\\\"\\n      - \\\"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\\\"\\n      - \\\"不需要区分 human vs AI-generated data\\\"\\n    relevance_to_us: \\\"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\\\"\\n    metrics_studied: [\\\"surplexity\\\", \\\"semantic network metrics\\\", \\\"next-token probability\\\"]\\n\\n  - id: \\\"qiu2025spectral\\\"\\n    title: \\\"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\\\"\\n    authors: \\\"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\\\"\\n    venue: \\\"arXiv (2510.04202)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04202\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\\\"\\n      - \\\"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\\\"\\n      - \\\"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\\\"\\n      - \\\"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\\\"\\n    relevance_to_us: \\\"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\\\"\\n    metrics_studied: [\\\"spectral alignment\\\", \\\"weight norm\\\", \\\"gradient norm\\\"]\\n\\n  - id: \\\"he2025closer\\\"\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shiliang He et al.\\\"\\n    venue: \\\"NeurIPS 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"识别 diffusion model collapse 中的 generalization → memorization 转变\\\"\\n      - \\\"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\\\"\\n      - \\\"提出基于 entropy 的数据选择策略，有效缓解 collapse\\\"\\n    relevance_to_us: \\\"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"FID\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"ba2024fill\\\"\\n    title: \\\"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\\\"\\n    authors: \\\"Yang Ba, Michelle V Mancenido, Rong Pan\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.10864\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\\\"\\n      - \\\"推导了基于 PAC 框架的 ECE bound\\\"\\n      - \\\"合成数据可改善 calibration 但需精心设计生成策略\\\"\\n    relevance_to_us: \\\"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\"]\\n\\n  - id: \\\"sigma2026spectral\\\"\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: \\\"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\\\"\\n    venue: \\\"arXiv (2601.03385)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2601.03385\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\\\"\\n      - \\\"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\\\"\\n      - \\\"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\\\"\\n    relevance_to_us: \\\"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\\\"\\n    gaps: \\\"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\\\"\\n    metrics_studied: [\\\"Gram matrix eigenspectrum\\\", \\\"spectral norm bounds\\\"]\\n\\n  - id: \\\"kalinowski2026topology\\\"\\n    title: \\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\"\\n    authors: \\\"Alexander Kalinowski\\\"\\n    venue: \\\"arXiv (2604.26984)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.26984\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\\\"\\n      - \\\"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\\\"\\n      - \\\"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\\\"\\n    relevance_to_us: \\\"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\\\"\\n    gaps: \\\"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\\\"\\n    metrics_studied: [\\\"Collapse Index\\\", \\\"persistent homology features\\\"]\\n\\n  # ============================================================\\n  # DIVERSITY METRICS (BACKGROUND)\\n  # ============================================================\\n  - id: \\\"zhu2018texygen\\\"\\n    title: \\\"Texygen: A Benchmarking Platform for Text Generation Models\\\"\\n    authors: \\\"Yaoming Zhu et al.\\\"\\n    venue: \\\"SIGIR 2018\\\"\\n    year: 2018\\n    url: \\\"https://arxiv.org/abs/1802.01886\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\\\"\\n      - \\\"成为文本生成多样性评估的标准基准之一\\\"\\n    relevance_to_us: \\\"Self-BLEU 是我们 diversity canary 的经典候选\\\"\\n    metrics_studied: [\\\"Self-BLEU\\\", \\\"BLEU\\\"]\\n\\n  - id: \\\"li2016diversity\\\"\\n    title: \\\"A Diversity-Promoting Objective Function for Neural Conversation Models\\\"\\n    authors: \\\"Jiwei Li et al.\\\"\\n    venue: \\\"NAACL 2016\\\"\\n    year: 2016\\n    url: \\\"https://arxiv.org/abs/1510.03055\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\\\"\\n      - \\\"计算 unique n-gram 数占总 n-gram 数的比例\\\"\\n    relevance_to_us: \\\"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\\\"\\n    metrics_studied: [\\\"distinct-1\\\", \\\"distinct-2\\\"]\\n\\n  # ============================================================\\n  # REPRESENTATION / SPECTRAL COLLAPSE\\n  # ============================================================\\n  - id: \\\"jing2022understanding\\\"\\n    title: \\\"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\\\"\\n    authors: \\\"Li Jing et al.\\\"\\n    venue: \\\"ICLR 2022\\\"\\n    year: 2022\\n    url: \\\"https://openreview.net/forum?id=YevsQ05DEN7\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"定义 dimensional collapse：embedding 向量只跨越低维子空间\\\"\\n      - \\\"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\\\"\\n      - \\\"strong augmentation 和 implicit regularization 驱动低秩解\\\"\\n    relevance_to_us: \\\"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\\\"\\n    metrics_studied: [\\\"effective rank\\\", \\\"singular value spectrum\\\"]\\n\\n  - id: \\\"noci2024mind\\\"\\n    title: \\\"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\\\"\\n    authors: \\\"Lorenzo Noci et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.07799\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 Random Matrix Theory 分析 attention 层的 rank collapse\\\"\\n      - \\\"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\\\"\\n      - \\\"rank collapse in depth: 所有 token 沿层收敛到单一表示\\\"\\n    relevance_to_us: \\\"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\\\"\\n    metrics_studied: [\\\"spectral gap\\\", \\\"singular values\\\", \\\"effective rank\\\"]\\n\\n  # ============================================================\\n  # DATA MIXING & ACCUMULATION\\n  # ============================================================\\n  - id: \\\"kazdan2025collapse\\\"\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"系统对比 replace vs accumulate 场景\\\"\\n      - \\\"replace → collapse；accumulate → 可避免 collapse\\\"\\n      - \\\"发现 real data 和 synthetic data 之间存在非平凡的交互效应\\\"\\n      - \\\"synthetic data 的价值取决于 real data 的绝对数量\\\"\\n    relevance_to_us: \\\"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"dey2024breaking\\\"\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: \\\"Apratim Dey, David Donoho, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.01413\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"替换数据 → 发散 population risk；累积数据 → 避免发散\\\"\\n      - \\\"证明累积策略在多种模型（GMM, HMM, LLM）上有效\\\"\\n    relevance_to_us: \\\"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\\\"\\n    metrics_studied: [\\\"population risk\\\"]\\n\\n  - id: \\\"epstein2024howbad\\\"\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: \\\"Mohamed El Amine Epstein et al.\\\"\\n    venue: \\\"arXiv (2404.05090)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.05090\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"纯合成数据训练不可避免 collapse\\\"\\n      - \\\"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\\\"\\n      - \\\"递归训练使原始分布尾部消失\\\"\\n    relevance_to_us: \\\"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\\\"\\n    metrics_studied: [\\\"perplexity\\\"]\\n\\n  - id: \\\"fu2025selfconsuming\\\"\\n    title: \\\"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\\\"\\n    authors: \\\"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\\\"\\n    venue: \\\"ICLR 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2502.18865\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\\\"\\n      - \\\"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\\\"\\n      - \\\"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\\\"\\n    relevance_to_us: \\\"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\\\"\\n    gaps: \\\"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\\\"\\n    metrics_studied: [\\\"generalization bound\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"bakshi2026improvement\\\"\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: \\\"Soham Bakshi, Sunrit Chakraborty\\\"\\n    venue: \\\"arXiv (2602.10531)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.10531\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\\\"\\n      - \\\"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\\\"\\n      - \\\"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\\\"\\n      - \\\"在 next-token prediction 语言模型上分析完整迭代演化动态\\\"\\n    relevance_to_us: \\\"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\\\"\\n    gaps: \\\"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\\\"\\n    metrics_studied: [\\\"population risk\\\", \\\"total variation distance\\\"]\\n\\n  # ============================================================\\n  # MITIGATION & VERIFICATION\\n  # ============================================================\\n  - id: \\\"feng2025escaping\\\"\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification\\\"\\n    authors: \\\"Yunzhen Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.16657\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"通过外部 verifier（human 或 better model）注入信息可避免 collapse\\\"\\n      - \\\"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\\\"\\n      - \\\"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\\\"\\n    relevance_to_us: \\\"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"barzilai2025consistency\\\"\\n    title: \\\"When Models Don't Collapse: On the Consistency of Iterative MLE\\\"\\n    authors: \\\"Daniel Barzilai, Ohad Shamir\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2505.19046\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\\\"\\n      - \\\"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\\\"\\n    relevance_to_us: \\\"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"dces2026counter\\\"\\n    title: \\\"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"MDPI Electronics (2026)\\\"\\n    year: 2026\\n    url: \\\"https://www.mdpi.com/2079-9292/15/4/869\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 DCES（dynamic center-edge sampling）数据选择框架\\\"\\n      - \\\"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\\\"\\n    relevance_to_us: \\\"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"entropy\\\"]\\n\\n  # ============================================================\\n  # POSITION / SURVEY / EPISTEMICS\\n  # ============================================================\\n  - id: \\\"schaeffer2025position\\\"\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\\\"\\n    venue: \\\"arXiv (2503.03150)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\\\"\\n      - \\\"许多 collapse 预测依赖于与现实不符的假设\\\"\\n      - \\\"多种 collapse 场景是可以轻易避免的\\\"\\n    relevance_to_us: \\\"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"wang2025epistemic\\\"\\n    title: \\\"Epistemic Diversity and Knowledge Collapse in Large Language Models\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv (2510.04226)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04226\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\\\"\\n      - \\\"所有模型的 epistemic diversity 低于基本 web 搜索\\\"\\n      - \\\"模型越大 epistemic diversity 反而越低；RAG 有正面效果\\\"\\n    relevance_to_us: \\\"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\\\"\\n    metrics_studied: [\\\"epistemic diversity\\\"]\\n\\n  # ============================================================\\n  # METHODOLOGY (GRANGER / LEAD-LAG)\\n  # ============================================================\\n  - id: \\\"shojaie2022granger\\\"\\n    title: \\\"Granger Causality: A Review and Recent Advances\\\"\\n    authors: \\\"Ali Shojaie, Emily B. Fox\\\"\\n    venue: \\\"Annual Review of Statistics and Its Application\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2105.02675\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Granger causality 综述：从经典线性到非线性/neural 方法\\\"\\n      - \\\"Panel data 场景的 Granger causality 扩展\\\"\\n      - \\\"VAR 和 neural Granger causality 的对比\\\"\\n    relevance_to_us: \\\"为我们的 panel Granger causality 分析提供方法论基础\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"marcinkevics2022neural\\\"\\n    title: \\\"Granger Causality Using Neural Networks\\\"\\n    authors: \\\"Raphael Marcinkevics, Julia Vogt\\\"\\n    venue: \\\"arXiv (2208.03703)\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2208.03703\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 neural network 估计 Granger causality，突破线性假设\\\"\\n      - \\\"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\\\"\\n    relevance_to_us: \\\"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\\\"\\n    metrics_studied: []\\n\\ngaps:\\n  - \\\"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\\\"\\n  - \\\"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\\\"\\n  - \\\"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\\\"\\n  - \\\"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\\\"\\n  - \\\"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\\\"\\n  - \\\"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\\\"\\n  - \\\"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\\\"\\n  - \\\"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\\\"\\n\\nnovelty_assessment: |\\n  我们项目的核心 novelty 在于：\\n\\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\\n     但没有人做过系统的 lead-lag 量化分析。\\n\\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\\n     现有工作都是单一指标或最多两三个指标的孤立分析。\\n\\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\\n     但没人研究 canary 在不同 alpha 下的行为。\\n\\n  4. **与已有工作的差异**：\\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\\n       我们将类似思路迁移到 iterative collapse 场景\\n\\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\\n\", \"total_chars\": 24089, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2644dff9-91d3-4450-9c2b-ee27bf1a1149",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "321b6708-aa7d-49a2-83f7-91c9d579d97b",
  "sourceToolAssistantUUID": "2644dff9-91d3-4450-9c2b-ee27bf1a1149",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T19:22:12.260Z_

<details open><summary>🔧 Tool call — Read · `toolu_017eNnNDVg9Nr6nkf3Ddqcvu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "321b6708-aa7d-49a2-83f7-91c9d579d97b",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31FjYjmd2FccTo45s6t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a77c0a7c-9171-40ea-a891-8c5113f327d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRMB1EVBcvbhBQPnbpSERn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24713,
      "cache_read_input_tokens": 37147,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 37147,
          "cache_creation_input_tokens": 24713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24713,
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

_source line 40 · 2026-05-14T19:22:12.265Z_

<details><summary>↩ Tool result · `toolu_017eNnNDVg9Nr6nkf3Ddqcvu`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 2
4	  description: 'α-sweep: 在 α∈{0.0, 0.25, 0.50, 0.75} 四个 contamination ratio 下重复 iterative
5	    training (Pythia-410M, WikiText-103, 10 gen, 3 seeds)，验证 canary→perplexity 的 lead-lag
6	    是否在低 α 下出现，绘制 predictability phase diagram。α=0.0 为 null control（纯 real data 再训练，确认
7	    canary signal 源于合成污染而非 fine-tuning artifact）'
8	  priority: P0
9	  gpu_budget_hours: 40
10	  deps: []
11	  notes: 需先部署双向 mix_datasets 修复 + accumulate 模式到远程服务器
12	  registry_id: alpha_sweep_a025_s42
13	- id: plan_002
14	  claim: 3
15	  description: '方法论 ablation: 在 MVP 4-seed 数据 + α-sweep 数据上对比 (i) naive Pearson lag-corr
16	    (ii) 差分后 cross-corr (iii) threshold-based lead time (iv) Toda-Yamamoto panel temporal
17	    precedence，量化伪显著比例'
18	  priority: P0
19	  gpu_budget_hours: 0
20	  deps:
21	  - plan_001
22	  notes: 需安装 statsmodels；如果 >30% naive 显著关联被 robust 方法推翻，则方法论贡献强
23	- id: plan_003
24	  claim: 1
25	  description: 'MVP 结果 formalization: 将 4-seed 100% SC 结果按 paper 格式整理，确认 lead time
26	    精确量化（signal onset 2σ 定义），max_lag 增大到 7 重跑验证截断效应'
27	  priority: P0
28	  gpu_budget_hours: 0
29	  deps: []
30	  registry_id: mvp_v4_rep42,mvp_v4_rep43,mvp_v4_rep44,mvp_v4_rep45
31	- id: plan_004
32	  claim: 2
33	  description: 'Cross-domain validation: C4 数据集 × Pythia-410M × α=0.50 × 3 seeds ×
34	    10 gen，验证 canary ranking 是否跨域转移'
35	  priority: P1
36	  gpu_budget_hours: 10
37	  deps:
38	  - plan_001
39	  notes: 如果 α-sweep 确认 canary→perplexity lead 在 α=0.50 存在，C4 验证其跨域性
40	- id: plan_005
41	  claim: 1
42	  description: 'Scale spot-check: Pythia-1.4B × α=0.50 × 3 seeds × 10 gen，验证 canary
43	    lead 是否跨规模保持'
44	  priority: P1
45	  gpu_budget_hours: 24
46	  deps:
47	  - plan_001
48	  notes: 单点验证，不做完整 α-sweep。如果 lead 保持则报告 scaling trend
49	- id: plan_006
50	  claim: 2
51	  description: 'Extended run: Pythia-410M × α=1.0 × 20 gen × 2 seeds，验证 token_entropy→perplexity
52	    的 lag=-5 是否为截断伪影（增大到 max_lag=10）'
53	  priority: P1
54	  gpu_budget_hours: 8
55	  deps: []
56	  notes: 解决 Reviewer 关于 max_lag 截断的质疑
57	- id: plan_007
58	  claim: 2
59	  description: 'Intervention 实验: CRS-predictive vs no-intervention baseline × Pythia-410M
60	    × α=0.75 × 3 seeds × 10 gen，展示 predictive intervention 保住 diversity 的效果'
61	  priority: P2
62	  gpu_budget_hours: 10
63	  deps:
64	  - plan_001
65	  - plan_002
66	  notes: 需先有 CRS 权重（从 α-sweep 学习）。如果时间紧可砍
67	- id: plan_008
68	  claim: 1
69	  description: '数据策略 ablation: α=0.50 下 accumulate vs replace 对比 × 3 seeds × 10 gen，验证
70	    Fu et al. 理论（accumulate 保证收敛）的同时测 canary 行为差异'
71	  priority: P2
72	  gpu_budget_hours: 10
73	  deps:
74	  - plan_001
75	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a77c0a7c-9171-40ea-a891-8c5113f327d2",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "0ea79d5a-2514-4794-bb8a-de17638480eb",
  "sourceToolAssistantUUID": "a77c0a7c-9171-40ea-a891-8c5113f327d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T19:22:15.759Z_

Now let me check the actual analysis code to understand the statistical methodology implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ea79d5a-2514-4794-bb8a-de17638480eb",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31GCyFHYg8WwitPa1mi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32d730d0-f29b-4247-b4df-5d67092d6a60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dgagz8pjAARFktyN22MobG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14077,
      "cache_read_input_tokens": 61860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14077,
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

_source line 42 · 2026-05-14T19:22:17.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EeVoAu1XiemtMSGLi49id2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32d730d0-f29b-4247-b4df-5d67092d6a60",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31GCyFHYg8WwitPa1mi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "144cae4e-ecc1-471c-a2f8-ccb359903c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dgagz8pjAARFktyN22MobG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14077,
      "cache_read_input_tokens": 61860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14077,
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

_source line 43 · 2026-05-14T19:22:17.708Z_

<details><summary>↩ Tool result · `toolu_01EeVoAu1XiemtMSGLi49id2`</summary>

```text
1	"""Analyze MVP experiment: metric trends, cross-correlation, lead time.
2	
3	Reads all_metrics.json from each rep, produces:
4	  - metric_trends.png : canary + downstream metrics vs generation
5	  - cross_correlation.png : cross-correlation heatmap
6	  - lead_time_table.csv : lead time estimates per canary-downstream pair
7	  - analysis_summary.json : machine-readable summary with graded verdict
8	
9	Evaluation pipeline (per mvp_evaluation_criteria.md):
10	  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50
11	  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency
12	  3. Permutation test (§1) — per-triplet significance via 10k permutations
13	  4. Per-seed significance filtering (§2) — 3/3 consistency requirement
14	  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL
15	  6. Lag dispersion statistics — mean, std, min, max per consistent pair
16	
17	Usage:
18	    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44
19	    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000
20	"""
21	
22	import argparse
23	import json
24	import os
25	import sys
26	
27	import matplotlib.pyplot as plt
28	import numpy as np
29	import pandas as pd
30	
31	
32	CANARY_METRICS = ["token_entropy", "self_bleu", "ece", "effective_rank"]
33	DOWNSTREAM_METRICS = ["perplexity", "distinct_1", "distinct_2", "distinct_3", "mauve"]
34	
35	HIGHER_IS_WORSE = {"self_bleu", "ece", "perplexity"}
36	LOWER_IS_WORSE = {"token_entropy", "effective_rank", "distinct_1", "distinct_2",
37	                   "distinct_3", "mauve"}
38	
39	
40	def load_metrics(results_dir, seeds):
41	    """Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}."""
42	    data = {}
43	    for seed in seeds:
44	        path = os.path.join(results_dir, f"rep_{seed}", "all_metrics.json")
45	        with open(path) as f:
46	            data[seed] = json.load(f)
47	    return data
48	
49	
50	def metrics_to_df(data):
51	    """Convert {seed: [metrics_per_gen]} to a long-form DataFrame."""
52	    rows = []
53	    for seed, gens in data.items():
54	        for m in gens:
55	            m_copy = dict(m)
56	            m_copy["seed"] = seed
57	            rows.append(m_copy)
58	    return pd.DataFrame(rows)
59	
60	
61	def normalize_for_correlation(series, metric_name):
62	    """Flip sign so that 'getting worse' is always positive direction."""
63	    s = series.copy()
64	    if metric_name in LOWER_IS_WORSE:
65	        s = -s
66	    s = (s - s.mean()) / (s.std() + 1e-12)
67	    return s
68	
69	
70	def cross_correlate(x, y, max_lag=5):
71	    """Cross-correlation of x and y at lags -max_lag..+max_lag.
72	
73	    Positive lag k means y leads x by k steps.
74	    Negative lag k means x leads y by |k| steps.
75	    """
76	    x = (x - x.mean()) / (x.std() + 1e-12)
77	    y = (y - y.mean()) / (y.std() + 1e-12)
78	    n = len(x)
79	    correlations = {}
80	    for lag in range(-max_lag, max_lag + 1):
81	        if lag >= 0:
82	            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0
83	        else:
84	            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0
85	        correlations[lag] = c
86	    return correlations
87	
88	
89	def estimate_lead_time(canary_series, downstream_series, canary_name,
90	                       downstream_name, max_lag=5):
91	    """Estimate how many generations canary leads downstream.
92	
93	    Returns (peak_lag, peak_corr, corrs). Negative peak_lag = canary leads.
94	    """
95	    c_norm = normalize_for_correlation(canary_series, canary_name)
96	    d_norm = normalize_for_correlation(downstream_series, downstream_name)
97	    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)
98	    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))
99	    return peak_lag, corrs[peak_lag], corrs
100	
101	
102	def permutation_test(canary_series, downstream_series, canary_name,
103	                     downstream_name, max_lag=5, n_permutations=10000, seed=0):
104	    """Permutation test for cross-correlation significance.
105	
106	    Shuffles the downstream series to break temporal structure, recomputes
107	    max |r| across all lags for each permutation. p-value is the fraction
108	    of permutation max|r| >= observed peak|r|.
109	
110	    Returns (peak_lag, peak_corr, p_value).
111	    """
112	    c_norm = normalize_for_correlation(canary_series, canary_name)
113	    d_norm = normalize_for_correlation(downstream_series, downstream_name)
114	
115	    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)
116	    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))
117	    observed_peak_r = abs(corrs[peak_lag])
118	
119	    rng = np.random.RandomState(seed)
120	    count_ge = 0
121	    for _ in range(n_permutations):
122	        d_perm = rng.permutation(d_norm)
123	        perm_corrs = cross_correlate(c_norm, d_perm, max_lag=max_lag)
124	        perm_max_r = max(abs(v) for v in perm_corrs.values())
125	        if perm_max_r >= observed_peak_r:
126	            count_ge += 1
127	
128	    p_value = count_ge / n_permutations
129	    return peak_lag, corrs[peak_lag], p_value
130	
131	
132	def check_mauve_floor(df, seeds):
133	    """Check MAUVE floor effect: Gen 0 < 0.10 and CV < 0.50 across all seeds.
134	
135	    Returns (demoted: bool, reason: str or None).
136	    """
137	    for seed in seeds:
138	        seed_df = df[df["seed"] == seed].sort_values("generation")
139	        gen0_mauve = seed_df[seed_df["generation"] == 0]["mauve"].values
140	        if len(gen0_mauve) == 0:
141	            return False, None
142	        if gen0_mauve[0] >= 0.10:
143	            return False, None
144	        mauve_vals = seed_df["mauve"].values
145	        mean_m = np.mean(mauve_vals)
146	        std_m = np.std(mauve_vals)
147	        cv = std_m / (mean_m + 1e-12)
148	        if cv >= 0.50:
149	            return False, None
150	    return True, "floor_effect"
151	
152	
153	def check_effective_rank_monotonicity(df, seeds):
154	    """Check effective_rank Gen 4-9 slope consistency across seeds.
155	
156	    Returns (status: str, slopes: dict).
157	    status is one of: "decreasing", "increasing", "inconclusive".
158	    """
159	    slopes = {}
160	    for seed in seeds:
161	        seed_df = df[df["seed"] == seed].sort_values("generation")
162	        late = seed_df[seed_df["generation"] >= 4]
163	        if len(late) < 2:
164	            return "inconclusive", {}
165	        gens = late["generation"].values.astype(float)
166	        vals = late["effective_rank"].values.astype(float)
167	        coeffs = np.polyfit(gens, vals, 1)
168	        slopes[str(seed)] = float(coeffs[0])
169	
170	    slope_vals = list(slopes.values())
171	    if all(s < 0 for s in slope_vals):
172	        return "decreasing", slopes
173	    if all(s > 0 for s in slope_vals):
174	        return "increasing", slopes
175	    return "inconclusive", slopes
176	
177	
178	def classify_pair(per_seed_results):
179	    """Classify a (canary, downstream) pair based on per-seed results.
180	
181	    Returns one of: "SIGNIFICANT LEAD", "WEAK LEAD", "NO LEAD".
182	    """
183	    if not all(r["peak_lag"] < 0 for r in per_seed_results):
184	        return "NO LEAD"
185	    if all(r["p_value"] < 0.10 and abs(r["peak_corr"]) >= 0.60
186	           for r in per_seed_results):
187	        return "SIGNIFICANT LEAD"
188	    return "WEAK LEAD"
189	
190	
191	def check_near_miss(per_seed_results):
192	    """Check if a NO LEAD pair is a near miss (2/3 seeds lead, 1 at lag=0)."""
193	    lags = [r["peak_lag"] for r in per_seed_results]
194	    neg_seeds = [r for r in per_seed_results if r["peak_lag"] < 0]
195	    zero_seeds = [r for r in per_seed_results if r["peak_lag"] == 0]
196	    if len(neg_seeds) == 2 and len(zero_seeds) == 1:
197	        if all(r["peak_lag"] <= -2 and r["p_value"] < 0.05 for r in neg_seeds):
198	            return True
199	    return False
200	
201	
202	def compute_lag_dispersion(per_seed_results):
203	    """Compute lag dispersion statistics for a consistent pair."""
204	    lags = [r["peak_lag"] for r in per_seed_results]
205	    lag_std = float(np.std(lags))
206	    return {
207	        "mean_lag": float(np.mean(lags)),
208	        "lag_std": lag_std,
209	        "min_lag": int(min(lags)),
210	        "max_lag": int(max(lags)),
211	        "high_dispersion": lag_std > 2.0,
212	    }
213	
214	
215	def compute_verdict(per_pair_results, effective_rank_status):
216	    """Compute graded verdict from per-pair results.
217	
218	    Returns (verdict, reasoning, significant_pairs, weak_pairs).
219	    """
220	    significant_pairs = []
221	    weak_pairs = []
222	
223	    for pr in per_pair_results:
224	        if pr["canary"] == "effective_rank" and effective_rank_status == "inconclusive":
225	            continue
226	        if pr["pair_verdict"] == "SIGNIFICANT LEAD":
227	            significant_pairs.append(pr)
228	        elif pr["pair_verdict"] == "WEAK LEAD":
229	            weak_pairs.append(pr)
230	
231	    sig_families = set(p["canary"] for p in significant_pairs)
232	    weak_families = set(p["canary"] for p in weak_pairs)
233	
234	    if len(sig_families) >= 2:
235	        verdict = "STRONG PASS"
236	        reasoning = (f"{len(sig_families)} canary families ({', '.join(sorted(sig_families))}) "
237	                     f"each have >= 1 SIGNIFICANT LEAD pair.")
238	    elif len(sig_families) >= 1:
239	        verdict = "PASS"
240	        reasoning = (f"{len(sig_families)} canary family ({', '.join(sorted(sig_families))}) "
241	                     f"has >= 1 SIGNIFICANT LEAD pair.")
242	    elif len(weak_families) >= 1:
243	        verdict = "CONDITIONAL PASS"
244	        reasoning = (f"No SIGNIFICANT LEAD pairs, but {len(weak_families)} canary "
245	                     f"family ({', '.join(sorted(weak_families))}) has >= 1 WEAK LEAD pair.")
246	    else:
247	        verdict = "FAIL"
248	        reasoning = "No canary family achieves even WEAK LEAD consistency across seeds."
249	
250	    return verdict, reasoning, significant_pairs, weak_pairs
251	
252	
253	def plot_metric_trends(df, output_dir):
254	    """Plot metric-vs-generation with mean +/- std across seeds."""
255	    all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS
256	    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
257	    axes = axes.flatten()
258	
259	    for idx, metric in enumerate(all_metrics):
260	        if idx >= len(axes):
261	            break
262	        ax = axes[idx]
263	        grouped = df.groupby("generation")[metric]
264	        mean = grouped.mean()
265	        std = grouped.std()
266	
267	        ax.plot(mean.index, mean.values, "o-", linewidth=2)
268	        ax.fill_between(mean.index, mean.values - std.values,
269	                        mean.values + std.values, alpha=0.2)
270	        ax.set_title(metric, fontsize=11, fontweight="bold")
271	        ax.set_xlabel("Generation")
272	        ax.set_ylabel(metric)
273	        ax.grid(True, alpha=0.3)
274	
275	        is_canary = metric in CANARY_METRICS
276	        ax.set_facecolor("#fff8f0" if is_canary else "#f0f8ff")
277	
278	    for idx in range(len(all_metrics), len(axes)):
279	        axes[idx].set_visible(False)
280	
281	    fig.suptitle("Metric Trends over Generations (mean ± std, 3 reps)",
282	                 fontsize=14, fontweight="bold")
283	    plt.tight_layout()
284	    plt.savefig(os.path.join(output_dir, "metric_trends.png"), dpi=150,
285	                bbox_inches="tight")
286	    plt.close()
287	    print("Saved metric_trends.png")
288	
289	
290	def plot_cross_correlation_heatmap(lead_table, output_dir):
291	    """Heatmap of peak lag (canary leads = negative lag)."""
292	    pivot_lag = lead_table.pivot(index="canary", columns="downstream",
293	                                values="peak_lag")
294	    pivot_corr = lead_table.pivot(index="canary", columns="downstream",
295	                                  values="peak_corr")
296	
297	    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
298	
299	    im1 = ax1.imshow(pivot_lag.values, cmap="RdBu_r", aspect="auto",
300	                     vmin=-5, vmax=5)
301	    ax1.set_xticks(range(len(pivot_lag.columns)))
302	    ax1.set_xticklabels(pivot_lag.columns, rotation=45, ha="right")
303	    ax1.set_yticks(range(len(pivot_lag.index)))
304	    ax1.set_yticklabels(pivot_lag.index)
305	    ax1.set_title("Peak Lag (negative = canary leads)")
306	    for i in range(len(pivot_lag.index)):
307	        for j in range(len(pivot_lag.columns)):
308	            ax1.text(j, i, f"{pivot_lag.values[i, j]:.0f}",
309	                     ha="center", va="center", fontsize=10)
310	    plt.colorbar(im1, ax=ax1)
311	
312	    im2 = ax2.imshow(np.abs(pivot_corr.values), cmap="YlOrRd", aspect="auto",
313	                     vmin=0, vmax=1)
314	    ax2.set_xticks(range(len(pivot_corr.columns)))
315	    ax2.set_xticklabels(pivot_corr.columns, rotation=45, ha="right")
316	    ax2.set_yticks(range(len(pivot_corr.index)))
317	    ax2.set_yticklabels(pivot_corr.index)
318	    ax2.set_title("|Peak Correlation|")
319	    for i in range(len(pivot_corr.index)):
320	        for j in range(len(pivot_corr.columns)):
321	            ax2.text(j, i, f"{pivot_corr.values[i, j]:.2f}",
322	                     ha="center", va="center", fontsize=10)
323	    plt.colorbar(im2, ax=ax2)
324	
325	    fig.suptitle("Cross-Correlation: Canary → Downstream", fontsize=13,
326	                 fontweight="bold")
327	    plt.tight_layout()
328	    plt.savefig(os.path.join(output_dir, "cross_correlation.png"), dpi=150,
329	                bbox_inches="tight")
330	    plt.close()
331	    print("Saved cross_correlation.png")
332	
333	
334	def main():
335	    parser = argparse.ArgumentParser(
336	        description="Analyze MVP experiment with graded verdict system.")
337	    parser.add_argument("--results_dir", type=str, default="results/mvp")
338	    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 43, 44])
339	    parser.add_argument("--max_lag", type=int, default=5)
340	    parser.add_argument("--n_permutations", type=int, default=10000,
341	                        help="Number of permutations for significance test (default: 10000)")
342	    args = parser.parse_args()
343	
344	    output_dir = os.path.join(args.results_dir, "analysis")
345	    os.makedirs(output_dir, exist_ok=True)
346	
347	    print("Loading metrics ...")
348	    data = load_metrics(args.results_dir, args.seeds)
349	    df = metrics_to_df(data)
350	
351	    # --- Metric trend plots ---
352	    plot_metric_trends(df, output_dir)
353	
354	    # --- §4: MAUVE floor effect detection ---
355	    mauve_demoted, mauve_reason = check_mauve_floor(df, args.seeds)
356	    active_downstream = list(DOWNSTREAM_METRICS)
357	    if mauve_demoted:
358	        print(f"MAUVE demoted to supplementary (reason: {mauve_reason})")
359	
360	    # --- §3: effective_rank monotonicity check ---
361	    er_status, er_slopes = check_effective_rank_monotonicity(df, args.seeds)
362	    print(f"effective_rank status: {er_status} (slopes: {er_slopes})")
363	
364	    # --- Cross-correlation with permutation tests ---
365	    total_triplets = len(CANARY_METRICS) * len(DOWNSTREAM_METRICS) * len(args.seeds)
366	    triplet_idx = 0
367	
368	    per_pair_results = []
369	    lead_rows = []
370	    near_misses = []
371	
372	    for canary in CANARY_METRICS:
373	        for downstream in DOWNSTREAM_METRICS:
374	            per_seed = []
375	            all_lags = []
376	            all_corrs = []
377	
378	            for seed in args.seeds:
379	                triplet_idx += 1
380	                print(f"\r  Permutation test {triplet_idx}/{total_triplets}: "
381	                      f"{canary} vs {downstream} (seed {seed})", end="",
382	                      flush=True)
383	
384	                seed_df = df[df["seed"] == seed].sort_values("generation")
385	                c_series = seed_df[canary].values
386	                d_series = seed_df[downstream].values
387	
388	                peak_lag, peak_corr, p_value = permutation_test(
389	                    c_series, d_series, canary, downstream,
390	                    max_lag=args.max_lag,
391	                    n_permutations=args.n_permutations,
392	                    seed=seed)
393	
394	                per_seed.append({
395	                    "seed": seed,
396	                    "peak_lag": int(peak_lag),
397	                    "peak_corr": round(float(peak_corr), 4),
398	                    "p_value": round(float(p_value), 4),
399	                })
400	                all_lags.append(peak_lag)
401	                all_corrs.append(peak_corr)
402	
403	            pair_verdict = classify_pair(per_seed)
404	
405	            pair_result = {
406	                "canary": canary,
407	                "downstream": downstream,
408	                "pair_verdict": pair_verdict,
409	                "per_seed": per_seed,
410	            }
411	
412	            if pair_verdict in ("SIGNIFICANT LEAD", "WEAK LEAD"):
413	                disp = compute_lag_dispersion(per_seed)
414	                pair_result.update(disp)
415	            else:
416	                if check_near_miss(per_seed):
417	                    near_misses.append({"canary": canary, "downstream": downstream,
418	                                        "per_seed": per_seed})
419	
420	            per_pair_results.append(pair_result)
421	
422	            lead_rows.append({
423	                "canary": canary,
424	                "downstream": downstream,
425	                "peak_lag": np.mean(all_lags),
426	                "peak_corr": np.mean(all_corrs),
427	                "lag_std": np.std(all_lags),
428	                "corr_std": np.std(all_corrs),
429	                "consistent": all(l < 0 for l in all_lags),
430	            })
431	
432	    print()
433	
434	    lead_table = pd.DataFrame(lead_rows)
435	    lead_table.to_csv(os.path.join(output_dir, "lead_time_table.csv"),
436	                      index=False)
437	    print("Saved lead_time_table.csv")
438	
439	    plot_cross_correlation_heatmap(lead_table, output_dir)
440	
441	    # --- §5: Graded verdict ---
442	    verdict_pairs = per_pair_results
443	    if mauve_demoted:
444	        verdict_pairs = [p for p in per_pair_results if p["downstream"] != "mauve"]
445	
446	    verdict, reasoning, sig_pairs, weak_pairs = compute_verdict(
447	        verdict_pairs, er_status)
448	
449	    # --- Build summary ---
450	    summary = {
451	        "mauve_demoted": mauve_demoted,
452	        "mauve_demoted_reason": mauve_reason,
453	        "effective_rank_status": er_status,
454	        "effective_rank_slopes": er_slopes,
455	        "per_pair_results": per_pair_results,
456	        "verdict": verdict,
457	        "verdict_reasoning": reasoning,
458	        "significant_lead_pairs": [
459	            {"canary": p["canary"], "downstream": p["downstream"]}
460	            for p in sig_pairs
461	        ],
462	        "weak_lead_pairs": [
463	            {"canary": p["canary"], "downstream": p["downstream"]}
464	            for p in weak_pairs
465	        ],
466	        "near_misses": near_misses,
467	    }
468	
469	    with open(os.path.join(output_dir, "analysis_summary.json"), "w") as f:
470	        json.dump(summary, f, indent=2)
471	
472	    # --- Console report ---
473	    print("\n" + "=" * 60)
474	    print("MVP ANALYSIS SUMMARY")
475	    print("=" * 60)
476	
477	    if mauve_demoted:
478	        print(f"MAUVE: demoted to supplementary ({mauve_reason})")
479	    else:
480	        print("MAUVE: retained as primary downstream metric")
481	
482	    print(f"effective_rank: {er_status}")
483	    if er_slopes:
484	        slope_str = ", ".join(f"seed {k}: {v:.4f}" for k, v in er_slopes.items())
485	        print(f"  slopes: {slope_str}")
486	
487	    n_sig = len(sig_pairs)
488	    n_weak = len(weak_pairs)
489	    n_total = len(verdict_pairs)
490	    print(f"\nPair results ({n_total} pairs evaluated for verdict):")
491	    print(f"  SIGNIFICANT LEAD: {n_sig}")
492	    print(f"  WEAK LEAD: {n_weak}")
493	    print(f"  NO LEAD: {n_total - n_sig - n_weak}")
494	
495	    if near_misses:
496	        print(f"  Near misses: {len(near_misses)}")
497	        for nm in near_misses:
498	            print(f"    {nm['canary']} -> {nm['downstream']}")
499	
500	    verdict_icon = {"STRONG PASS": "STRONG PASS", "PASS": "PASS",
501	                    "CONDITIONAL PASS": "CONDITIONAL PASS", "FAIL": "FAIL"}
502	    print(f"\nVerdict: {verdict_icon[verdict]}")
503	    print(f"Reasoning: {reasoning}")
504	
505	    if sig_pairs:
506	        print("\nSignificant lead pairs:")
507	        for p in sig_pairs:
508	            disp_flag = " [high_dispersion]" if p.get("high_dispersion") else ""
509	            print(f"  {p['canary']} -> {p['downstream']}: "
510	                  f"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}")
511	            for s in p["per_seed"]:
512	                print(f"    seed {s['seed']}: lag={s['peak_lag']}, "
513	                      f"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}")
514	
515	    if weak_pairs:
516	        print("\nWeak lead pairs:")
517	        for p in weak_pairs:
518	            disp_flag = " [high_dispersion]" if p.get("high_dispersion") else ""
519	            print(f"  {p['canary']} -> {p['downstream']}: "
520	                  f"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}")
521	            for s in p["per_seed"]:
522	                print(f"    seed {s['seed']}: lag={s['peak_lag']}, "
523	                      f"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}")
524	
525	    print("\nFull lead time table:")
526	    print(lead_table.to_string(index=False))
527	    print(f"\nResults saved to {output_dir}/")
528	
529	
530	if __name__ == "__main__":
531	    main()
532	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "144cae4e-ecc1-471c-a2f8-ccb359903c29",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "a7ef65e7-d038-4300-b38d-a8dd57e9d31d",
  "sourceToolAssistantUUID": "144cae4e-ecc1-471c-a2f8-ccb359903c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T19:22:18.080Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VaZVinqZwLnWdQ5zBiBBoL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/metrics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7ef65e7-d038-4300-b38d-a8dd57e9d31d",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31GCyFHYg8WwitPa1mi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97764c42-2002-4e1c-9221-ad58a409b142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dgagz8pjAARFktyN22MobG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14077,
      "cache_read_input_tokens": 61860,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 61860,
          "cache_creation_input_tokens": 14077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14077,
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

_source line 45 · 2026-05-14T19:22:18.088Z_

<details><summary>↩ Tool result · `toolu_01VaZVinqZwLnWdQ5zBiBBoL`</summary>

```text
1	"""Canary and downstream metrics for model collapse detection.
2	
3	Computes per-generation metrics on held-out data and generated samples.
4	All compute_* functions share the signature:
5	    (model, tokenizer, eval_dataset, gen_dataset=None, **kwargs) -> float | dict
6	
7	Dependencies: torch, transformers, mauve-text, nltk
8	"""
9	
10	import math
11	from collections import Counter
12	from itertools import combinations
13	
14	import numpy as np
15	import torch
16	from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
17	
18	
19	# ---------------------------------------------------------------------------
20	# Text-surface metrics
21	# ---------------------------------------------------------------------------
22	
23	def compute_token_entropy(model, tokenizer, eval_dataset, gen_dataset=None,
24	                          max_samples=512, max_length=256, batch_size=8):
25	    """Mean next-token entropy of `model` on `eval_dataset` (held-out real text).
26	
27	    Lower entropy over generations signals the model is becoming overly
28	    confident / less diverse — a collapse canary.
29	    """
30	    model.eval()
31	    device = next(model.parameters()).device
32	    total_entropy = 0.0
33	    total_tokens = 0
34	
35	    texts = eval_dataset["text"][:max_samples]
36	    for i in range(0, len(texts), batch_size):
37	        batch_texts = texts[i:i + batch_size]
38	        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
39	                        max_length=max_length, padding=True)
40	        input_ids = enc["input_ids"].to(device)
41	        attention_mask = enc["attention_mask"].to(device)
42	
43	        with torch.no_grad():
44	            logits = model(input_ids=input_ids, attention_mask=attention_mask).logits
45	
46	        # shift: predict token t+1 from position t
47	        shift_logits = logits[:, :-1, :]
48	        shift_mask = attention_mask[:, 1:]
49	
50	        log_probs = torch.log_softmax(shift_logits, dim=-1)
51	        probs = torch.exp(log_probs)
52	        token_entropy = -(probs * log_probs).sum(dim=-1)  # (B, T-1)
53	
54	        masked_entropy = (token_entropy * shift_mask).sum()
55	        total_entropy += masked_entropy.item()
56	        total_tokens += shift_mask.sum().item()
57	
58	    return total_entropy / max(total_tokens, 1)
59	
60	
61	def compute_self_bleu(model, tokenizer, eval_dataset, gen_dataset=None,
62	                      max_samples=200, sample_pairs=500):
63	    """Self-BLEU among generated samples — higher means less diversity.
64	
65	    Uses `gen_dataset["text"]`. Falls back to `eval_dataset` if gen_dataset
66	    is None (useful for baseline measurement on real data).
67	    """
68	    src = gen_dataset if gen_dataset is not None else eval_dataset
69	    texts = src["text"][:max_samples]
70	    tokenized = [tokenizer.tokenize(t)[:128] for t in texts if len(t.strip()) > 0]
71	
72	    if len(tokenized) < 2:
73	        return 0.0
74	
75	    smoother = SmoothingFunction().method1
76	    n_pairs = min(sample_pairs, len(tokenized) * (len(tokenized) - 1) // 2)
77	
78	    rng = np.random.RandomState(0)
79	    indices = list(range(len(tokenized)))
80	    scores = []
81	    for _ in range(n_pairs):
82	        i, j = rng.choice(indices, size=2, replace=False)
83	        score = sentence_bleu([tokenized[i]], tokenized[j],
84	                              weights=(0.25, 0.25, 0.25, 0.25),
85	                              smoothing_function=smoother)
86	        scores.append(score)
87	
88	    return float(np.mean(scores))
89	
90	
91	def compute_distinct_n(model, tokenizer, eval_dataset, gen_dataset=None,
92	                       max_samples=500, ns=(1, 2, 3)):
93	    """Distinct-n: ratio of unique n-grams to total n-grams in generated text.
94	
95	    Returns dict {"distinct_1": ..., "distinct_2": ..., "distinct_3": ...}.
96	    """
97	    src = gen_dataset if gen_dataset is not None else eval_dataset
98	    texts = src["text"][:max_samples]
99	    all_tokens = []
100	    for t in texts:
101	        all_tokens.extend(tokenizer.tokenize(t)[:256])
102	
103	    result = {}
104	    for n in ns:
105	        ngrams = [tuple(all_tokens[i:i + n]) for i in range(len(all_tokens) - n + 1)]
106	        if len(ngrams) == 0:
107	            result[f"distinct_{n}"] = 0.0
108	        else:
109	            result[f"distinct_{n}"] = len(set(ngrams)) / len(ngrams)
110	    return result
111	
112	
113	# ---------------------------------------------------------------------------
114	# Calibration metrics
115	# ---------------------------------------------------------------------------
116	
117	def compute_ece(model, tokenizer, eval_dataset, gen_dataset=None,
118	                max_samples=512, max_length=256, n_bins=10, batch_size=8):
119	    """Expected Calibration Error on held-out eval_dataset.
120	
121	    Measures whether the model's confidence matches its accuracy at the
122	    token level. Rising ECE is a collapse canary (overconfidence).
123	    """
124	    model.eval()
125	    device = next(model.parameters()).device
126	
127	    confidences = []
128	    accuracies = []
129	
130	    texts = eval_dataset["text"][:max_samples]
131	    for i in range(0, len(texts), batch_size):
132	        batch_texts = texts[i:i + batch_size]
133	        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
134	                        max_length=max_length, padding=True)
135	        input_ids = enc["input_ids"].to(device)
136	        attention_mask = enc["attention_mask"].to(device)
137	
138	        with torch.no_grad():
139	            logits = model(input_ids=input_ids, attention_mask=attention_mask).logits
140	
141	        shift_logits = logits[:, :-1, :]
142	        shift_labels = input_ids[:, 1:]
143	        shift_mask = attention_mask[:, 1:]
144	
145	        probs = torch.softmax(shift_logits, dim=-1)
146	        max_probs, preds = probs.max(dim=-1)
147	
148	        mask_flat = shift_mask.bool().flatten()
149	        confidences.append(max_probs.flatten()[mask_flat].cpu())
150	        accuracies.append((preds == shift_labels).flatten()[mask_flat].cpu().float())
151	
152	    confidences = torch.cat(confidences)
153	    accuracies = torch.cat(accuracies)
154	
155	    bin_boundaries = torch.linspace(0, 1, n_bins + 1)
156	    ece = 0.0
157	    for b in range(n_bins):
158	        mask = (confidences > bin_boundaries[b]) & (confidences <= bin_boundaries[b + 1])
159	        if mask.sum() == 0:
160	            continue
161	        bin_acc = accuracies[mask].mean()
162	        bin_conf = confidences[mask].mean()
163	        ece += mask.sum().item() / len(confidences) * abs(bin_acc - bin_conf).item()
164	
165	    return ece
166	
167	
168	# ---------------------------------------------------------------------------
169	# Spectral metrics
170	# ---------------------------------------------------------------------------
171	
172	def compute_effective_rank(model, tokenizer, eval_dataset, gen_dataset=None,
173	                           max_samples=256, max_length=256, batch_size=8):
174	    """Effective rank of last-layer hidden state covariance matrix.
175	
176	    effective_rank = exp(entropy of normalized eigenvalues)
177	    Declining effective rank signals representation collapse.
178	    """
179	    model.eval()
180	    device = next(model.parameters()).device
181	    all_hidden = []
182	
183	    texts = eval_dataset["text"][:max_samples]
184	    for i in range(0, len(texts), batch_size):
185	        batch_texts = texts[i:i + batch_size]
186	        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
187	                        max_length=max_length, padding=True)
188	        input_ids = enc["input_ids"].to(device)
189	        attention_mask = enc["attention_mask"].to(device)
190	
191	        with torch.no_grad():
192	            outputs = model(input_ids=input_ids, attention_mask=attention_mask,
193	                            output_hidden_states=True)
194	        last_hidden = outputs.hidden_states[-1]  # (B, T, D)
195	
196	        # take mean-pooled representation per sample
197	        mask_expanded = attention_mask.unsqueeze(-1).float()
198	        pooled = (last_hidden * mask_expanded).sum(dim=1) / mask_expanded.sum(dim=1)
199	        all_hidden.append(pooled.cpu().float())
200	
201	    H = torch.cat(all_hidden, dim=0).numpy()  # (N, D)
202	    H = H - H.mean(axis=0, keepdims=True)
203	    cov = np.cov(H, rowvar=False)
204	    eigenvalues = np.linalg.eigvalsh(cov)
205	    eigenvalues = eigenvalues[eigenvalues > 1e-12]
206	
207	    # normalized eigenvalue distribution
208	    p = eigenvalues / eigenvalues.sum()
209	    entropy = -np.sum(p * np.log(p))
210	    return float(np.exp(entropy))
211	
212	
213	# ---------------------------------------------------------------------------
214	# Downstream metrics
215	# ---------------------------------------------------------------------------
216	
217	def compute_perplexity(model, tokenizer, eval_dataset, gen_dataset=None,
218	                       max_samples=512, max_length=256, batch_size=8):
219	    """Perplexity on held-out real data. The primary collapse indicator."""
220	    model.eval()
221	    device = next(model.parameters()).device
222	    total_loss = 0.0
223	    total_tokens = 0
224	
225	    texts = eval_dataset["text"][:max_samples]
226	    for i in range(0, len(texts), batch_size):
227	        batch_texts = texts[i:i + batch_size]
228	        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
229	                        max_length=max_length, padding=True)
230	        input_ids = enc["input_ids"].to(device)
231	        attention_mask = enc["attention_mask"].to(device)
232	
233	        labels = input_ids.clone()
234	        labels[attention_mask == 0] = -100
235	
236	        with torch.no_grad():
237	            outputs = model(input_ids=input_ids, attention_mask=attention_mask,
238	                            labels=labels)
239	
240	        shift_mask = attention_mask[:, 1:]
241	        n_tokens = shift_mask.sum().item()
242	
243	        # outputs.loss is mean over all non-ignored tokens
244	        total_loss += outputs.loss.item() * n_tokens
245	        total_tokens += n_tokens
246	
247	    return float(math.exp(total_loss / max(total_tokens, 1)))
248	
249	
250	def compute_mauve(model, tokenizer, eval_dataset, gen_dataset=None,
251	                  max_samples=2000, max_length=256):
252	    """MAUVE score between real (eval_dataset) and generated (gen_dataset) text.
253	
254	    MAUVE ∈ [0, 1]; higher = generated distribution closer to real.
255	    Declining MAUVE is a downstream collapse signal.
256	    """
257	    import mauve as mauve_pkg
258	
259	    real_texts = eval_dataset["text"][:max_samples]
260	    real_texts = [t[:max_length * 4] for t in real_texts if len(t.strip()) > 0]
261	
262	    if gen_dataset is None:
263	        return 1.0  # no generated data to compare
264	
265	    gen_texts = gen_dataset["text"][:max_samples]
266	    gen_texts = [t[:max_length * 4] for t in gen_texts if len(t.strip()) > 0]
267	
268	    if len(gen_texts) == 0:
269	        return 0.0
270	
271	    # use the same number of samples for fair comparison
272	    n = min(len(real_texts), len(gen_texts))
273	    result = mauve_pkg.compute_mauve(
274	        p_text=real_texts[:n],
275	        q_text=gen_texts[:n],
276	        device_id=torch.cuda.current_device() if torch.cuda.is_available() else -1,
277	        max_text_length=max_length,
278	        verbose=False,
279	    )
280	    return float(result.mauve)
281	
282	
283	# ---------------------------------------------------------------------------
284	# Convenience: compute all metrics at once
285	# ---------------------------------------------------------------------------
286	
287	def compute_all_metrics(model, tokenizer, eval_dataset, gen_dataset=None,
288	                        **kwargs):
289	    """Compute every metric and return a flat dict.
290	
291	    Args:
292	        model: HuggingFace causal LM.
293	        tokenizer: Corresponding tokenizer.
294	        eval_dataset: Held-out real data split (must have "text" column).
295	        gen_dataset: Generated/synthetic data (must have "text" column).
296	        **kwargs: Forwarded to individual metric functions.
297	
298	    Returns:
299	        dict with keys: token_entropy, self_bleu, distinct_1/2/3, ece,
300	        effective_rank, perplexity, mauve.
301	    """
302	    results = {}
303	
304	    results["token_entropy"] = compute_token_entropy(
305	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
306	
307	    results["self_bleu"] = compute_self_bleu(
308	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
309	
310	    distinct = compute_distinct_n(
311	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
312	    results.update(distinct)
313	
314	    results["ece"] = compute_ece(
315	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
316	
317	    results["effective_rank"] = compute_effective_rank(
318	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
319	
320	    results["perplexity"] = compute_perplexity(
321	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
322	
323	    results["mauve"] = compute_mauve(
324	        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
325	
326	    return results
327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97764c42-2002-4e1c-9221-ad58a409b142",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "fe550505-b771-43fa-9f0a-f0db4f31f92e",
  "sourceToolAssistantUUID": "97764c42-2002-4e1c-9221-ad58a409b142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-14T19:22:22.150Z_

Now I have a thorough understanding of the paper, its experimental infrastructure, the underlying data, and the framing decisions. Let me also check for discrepancies between the actual MVP data and what's reported in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe550505-b771-43fa-9f0a-f0db4f31f92e",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31Gdz9Km3ymQFjWykvT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d835d8f-965e-45e0-b161-ac70eee50030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012itx1inE4axVCNa73pD1AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12272,
      "cache_read_input_tokens": 75937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12272,
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

_source line 47 · 2026-05-14T19:22:24.765Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E2ZzbsZv8XBBxeSBfLuWVB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d835d8f-965e-45e0-b161-ac70eee50030",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31Gdz9Km3ymQFjWykvT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cedf667e-c3ed-4d93-b20e-ce3ffca02658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012itx1inE4axVCNa73pD1AB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12272,
      "cache_read_input_tokens": 75937,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 75937,
          "cache_creation_input_tokens": 12272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12272,
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

_source line 48 · 2026-05-14T19:22:24.781Z_

<details><summary>↩ Tool result · `toolu_01E2ZzbsZv8XBBxeSBfLuWVB`</summary>

```text
1	narrative_guidance: 'Claim 1 fully supported: canary→diversity lead 1-2 gen, robust
2	  across seeds. Claim 2 softened to regime-dependent gradient: canary→perplexity lead
3	  only at α=0.25, marginal, phase boundary is a gradual degradation zone around α∈[0.25,0.5]
4	  rather than a sharp transition. Claim 3 softened: TY overturns 15-29% naive associations
5	  — useful methodological contribution but not dramatic. Intervention (plan_007) needed
6	  to strengthen practical narrative. Target AAAI with honest framing; prepare EMNLP
7	  Findings fallback.
8	
9	  '
10	imagined_experiments:
11	- name: α-sweep predictability phase diagram
12	  plan_id: plan_001
13	  description: 'Pythia-410M × WikiText-103 × α∈{0.25, 0.50, 0.75} × 10 gen × 3 seeds.
14	    Run Toda-Yamamoto panel temporal precedence for all canary→target pairs at each
15	    α.
16	
17	    '
18	  expected_results:
19	    alpha_025_canary_diversity_lead_gen: 2.0
20	    alpha_025_canary_diversity_TY_pval_median: 0.003
21	    alpha_025_canary_diversity_seeds_significant: 3/3
22	    alpha_025_canary_perplexity_lead_gen: 1.0
23	    alpha_025_canary_perplexity_TY_pval_median: 0.042
24	    alpha_025_canary_perplexity_seeds_significant: 2/3
25	    alpha_025_gen10_perplexity: 78.5
26	    alpha_025_gen10_distinct_1: 0.142
27	    alpha_025_gen10_token_entropy: 2.61
28	    alpha_025_gen10_ece: 0.089
29	    alpha_050_canary_diversity_lead_gen: 1.0
30	    alpha_050_canary_diversity_TY_pval_median: 0.008
31	    alpha_050_canary_diversity_seeds_significant: 3/3
32	    alpha_050_canary_perplexity_lead_gen: 0.0
33	    alpha_050_canary_perplexity_TY_pval_median: 0.31
34	    alpha_050_canary_perplexity_seeds_significant: 0/3
35	    alpha_050_gen10_perplexity: 185.3
36	    alpha_050_gen10_distinct_1: 0.108
37	    alpha_050_gen10_token_entropy: 2.18
38	    alpha_050_gen10_ece: 0.167
39	    alpha_075_canary_diversity_lead_gen: 1.0
40	    alpha_075_canary_diversity_TY_pval_median: 0.017
41	    alpha_075_canary_diversity_seeds_significant: 3/3
42	    alpha_075_canary_perplexity_lead_gen: 0.0
43	    alpha_075_canary_perplexity_TY_pval_median: 0.58
44	    alpha_075_canary_perplexity_seeds_significant: 0/3
45	    alpha_075_gen10_perplexity: 512.7
46	    alpha_075_gen10_distinct_1: 0.083
47	    alpha_075_gen10_token_entropy: 1.68
48	    alpha_075_gen10_ece: 0.312
49	    effective_rank_lead_any_alpha: not significant
50	    self_bleu_lead_any_alpha: not significant
51	  result_rationale: 'α=0.25 保留 75% 真实数据，collapse 进程最慢。diversity 退化需要更多代数积累才显现， 给 canary（ECE/entropy
52	    对分布偏移更敏感）提供 2 gen 的领先窗口。perplexity 在此 regime 下也是渐进恶化而非突变，canary 有机会以 ~1 gen 领先，但效应弱——因为
53	    75% 真实数据的 锚定效应使 perplexity 变化幅度小，信噪比低，仅 2/3 seeds 达到显著。 α=0.50 是过渡区：collapse 加速，canary→diversity
54	    仍有 1 gen lead（diversity 指标的 累积性质使其滞后于 distributional shift），但 perplexity 开始与 canary
55	    近同步恶化， TY 无法分离 temporal precedence。 α=0.75 接近 full SC：collapse 动力学加速到 canary 和
56	    diversity 几乎同代恶化，仅因 diversity 的定义性滞后保留 1 gen lead；perplexity 与 canary 完全同步崩溃。
57	    effective_rank 和 self_bleu 在所有 α 下均无显著 lead——与 MVP 一致，这两个指标要么 噪声太大（self_bleu 的
58	    sampling variance），要么对 synthetic data drift 不够敏感 （effective_rank 在 embedding space
59	    退化前不变化）。
60	
61	    '
62	  tables:
63	  - name: 'Table 2: Toda-Yamamoto lead-lag results across α'
64	    columns:
65	    - α
66	    - canary_family
67	    - target
68	    - TY_lead_gen
69	    - TY_p_median
70	    - seeds_sig
71	    - effect_size_r
72	    rows:
73	    - - 0.25
74	      - ECE
75	      - distinct_1
76	      - 2
77	      - 0.002
78	      - 3/3
79	      - 0.93
80	    - - 0.25
81	      - token_entropy
82	      - distinct_1
83	      - 2
84	      - 0.004
85	      - 3/3
86	      - 0.91
87	    - - 0.25
88	      - ECE
89	      - perplexity
90	      - 1
91	      - 0.038
92	      - 2/3
93	      - 0.72
94	    - - 0.25
95	      - token_entropy
96	      - perplexity
97	      - 1
98	      - 0.047
99	      - 2/3
100	      - 0.68
101	    - - 0.5
102	      - ECE
103	      - distinct_1
104	      - 1
105	      - 0.006
106	      - 3/3
107	      - 0.9
108	    - - 0.5
109	      - token_entropy
110	      - distinct_1
111	      - 1
112	      - 0.01
113	      - 3/3
114	      - 0.88
115	    - - 0.5
116	      - ECE
117	      - perplexity
118	      - 0
119	      - 0.28
120	      - 0/3
121	      - 0.31
122	    - - 0.5
123	      - token_entropy
124	      - perplexity
125	      - 0
126	      - 0.35
127	      - 0/3
128	      - 0.25
129	    - - 0.75
130	      - ECE
131	      - distinct_1
132	      - 1
133	      - 0.014
134	      - 3/3
135	      - 0.89
136	    - - 0.75
137	      - token_entropy
138	      - distinct_1
139	      - 1
140	      - 0.019
141	      - 3/3
142	      - 0.88
143	    - - 0.75
144	      - ECE
145	      - perplexity
146	      - 0
147	      - 0.52
148	      - 0/3
149	      - 0.14
150	    - - 0.75
151	      - token_entropy
152	      - perplexity
153	      - 0
154	      - 0.63
155	      - 0/3
156	      - 0.09
157	  - name: 'Table S1: Failed canary families across α'
158	    columns:
159	    - α
160	    - canary_family
161	    - target
162	    - TY_p_median
163	    - failure_reason
164	    rows:
165	    - - 0.25
166	      - effective_rank
167	      - distinct_1
168	      - 0.41
169	      - rank plateau until gen 6-7
170	    - - 0.25
171	      - self_bleu
172	      - distinct_1
173	      - 0.55
174	      - high sampling variance
175	    - - 0.5
176	      - effective_rank
177	      - distinct_1
178	      - 0.38
179	      - rank plateau until gen 5
180	    - - 0.5
181	      - self_bleu
182	      - distinct_1
183	      - 0.62
184	      - high sampling variance
185	    - - 0.75
186	      - effective_rank
187	      - distinct_1
188	      - 0.29
189	      - noisy but borderline
190	    - - 0.75
191	      - self_bleu
192	      - distinct_1
193	      - 0.48
194	      - sampling variance + floor effect
195	  figures_description:
196	  - 'Fig 2: Predictability phase diagram. X-axis: α (0.25–1.0). Y-axis: TY-estimated
197	    lead (gen). 两条曲线: canary→diversity (从 2 gen 单调降至 ~1 gen) 和 canary→perplexity (从
198	    ~1 gen 降至 0). 灰色 shading 标注 ''predictable zone'' (α<0.5) vs ''synchronous collapse
199	    zone'' (α>0.5). Boundary 是渐变带而非 sharp line.'
200	  - 'Fig 3: Per-α metric trajectories. 3×2 panel (3 α × 2 targets). 每个 panel 叠加 ECE
201	    (red), token_entropy (blue), distinct_1 (black dashed). 可视化 lead 如何随 α 收缩.'
202	  - 'Fig S1: Per-seed scatter for α=0.25 canary→perplexity, showing 2/3 seeds significant,
203	    1 seed nonsignificant (p=0.11).'
204	  analysis: 'Phase diagram 的核心发现：canary→diversity lead 是 monotonically decreasing
205	    function of α, 从 α=0.25 的 2 gen 到 α=0.75/1.0 的 ~1 gen。这意味着 early warning window
206	    随 contamination ratio 缩短但不消失——即使在 α=0.75 仍有 1 gen lead for diversity。 canary→perplexity
207	    的 boundary 在 α≈0.25-0.50 之间：仅在 α=0.25 可检测到 marginal lead， 且 cross-seed consistency
208	    仅 2/3。这定义了 phase diagram 的 "partially predictable" 区域。 narrative: "we map the
209	    boundary of predictability" 而非 "we show canaries predict collapse"。
210	
211	    '
212	- name: '方法论 ablation: naive correlation vs Toda-Yamamoto'
213	  plan_id: plan_002
214	  description: '在 MVP 4-seed (α=1.0) + plan_001 α-sweep 数据上，对比四种方法: (i) naive Pearson
215	    lag-correlation, (ii) 差分后 cross-correlation, (iii) threshold-based lead time (2σ
216	    onset), (iv) Toda-Yamamoto panel temporal precedence. 量化各方法的 Type I error rate
217	    和伪显著比例。
218	
219	    '
220	  expected_results:
221	    total_pairwise_associations_tested: 96
222	    naive_pearson_significant_count: 71
223	    differenced_xcorr_significant_count: 52
224	    threshold_2sigma_significant_count: 58
225	    TY_significant_count: 54
226	    naive_overturned_by_TY_count: 19
227	    naive_overturned_by_TY_pct: 20.0
228	    naive_only_significant_examples: effective_rank→distinct_1 (α=0.75), self_bleu→perplexity
229	      (α=0.50), ECE→perplexity (α=0.50)
230	    TY_and_differenced_agree_pct: 85.0
231	    threshold_vs_TY_concordance_pct: 78.0
232	  result_rationale: 'Naive Pearson correlation 在非平稳时间序列上 inflate Type I error，因为两个共同趋势
233	    的序列（如都单调恶化的指标）即使无因果关系也会产生高相关。在 α=1.0 (MVP) 数据中， 所有指标都单调恶化，naive 方法会将几乎所有 pair
234	    标记为显著。在 α=0.50/0.75 中， 部分指标（如 effective_rank）前期平台后期骤降，与 diversity 的单调下降产生虚假的 lag
235	    correlation。 TY 通过在 VAR 中加入额外 lag 吸收非平稳性，只检测 Granger-causal temporal precedence。
236	    预计 ~20% 的 naive 显著关联被推翻——主要是 (1) failed canary families (effective_rank, self_bleu)
237	    的虚假显著, (2) canary→perplexity 在 α≥0.50 的虚假显著。 20% 而非更高，因为 canary→diversity 的 lead
238	    是 genuine 的（即使 naive 也能捕捉）， 所以大部分真阳性在两种方法下一致。差分法与 TY 85% 一致因为差分也处理了一阶非平稳， 但 TY
239	    对高阶整合更 robust。
240	
241	    '
242	  tables:
243	  - name: 'Table 3: Method comparison — significance rates'
244	    columns:
245	    - Method
246	    - Significant_pairs
247	    - Total_pairs
248	    - Rate
249	    - Overturned_by_TY
250	    rows:
251	    - - Naive Pearson
252	      - 71
253	      - 96
254	      - 74.0%
255	      - 19 (20%)
256	    - - Differenced XCorr
257	      - 52
258	      - 96
259	      - 54.2%
260	      - 3 (3%)
261	    - - Threshold (2σ)
262	      - 58
263	      - 96
264	      - 60.4%
265	      - 8 (8%)
266	    - - Toda-Yamamoto
267	      - 54
268	      - 96
269	      - 56.3%
270	      - —
271	  - name: 'Table 4: Overturned associations breakdown'
272	    columns:
273	    - canary_family
274	    - target
275	    - α
276	    - naive_p
277	    - TY_p
278	    - diagnosis
279	    rows:
280	    - - effective_rank
281	      - distinct_1
282	      - 0.75
283	      - 0.008
284	      - 0.29
285	      - 'spurious: co-trending'
286	    - - effective_rank
287	      - distinct_2
288	      - 0.5
289	      - 0.012
290	      - 0.38
291	      - 'spurious: co-trending'
292	    - - self_bleu
293	      - perplexity
294	      - 0.5
295	      - 0.015
296	      - 0.55
297	      - 'spurious: shared nonstationary trend'
298	    - - self_bleu
299	      - distinct_1
300	      - 0.75
301	      - 0.021
302	      - 0.48
303	      - 'spurious: variance-driven'
304	    - - ECE
305	      - perplexity
306	      - 0.5
307	      - 0.031
308	      - 0.28
309	      - 'spurious: co-trending without lead'
310	    - - token_entropy
311	      - perplexity
312	      - 0.5
313	      - 0.034
314	      - 0.35
315	      - 'spurious: co-trending without lead'
316	  figures_description:
317	  - 'Fig 4: Bar chart. 每个 method 的 significant pair 数量，colored by genuine (TY-confirmed)
318	    vs overturned. 直观展示 naive inflation.'
319	  - 'Fig S2: Heatmap. 4 methods × 24 canary-target-α combinations. Cell color = p-value.
320	    突出 naive 与 TY 不一致的 cells.'
321	  analysis: '20% overturned rate 证明 naive correlation 在非平稳训练指标上不可靠，但不是灾难性的。 方法论贡献的叙事：TY
322	    提供 "more conservative but reliable" 估计，特别在 failed canary families 上避免了误导性结论。如果直接用
323	    naive correlation 写论文，会错误声称 effective_rank 和 self_bleu 也是 viable canaries。这足以作为
324	    methodological contribution 但不应过分渲染。
325	
326	    '
327	- name: MVP 结果 formalization (max_lag=7)
328	  plan_id: plan_003
329	  description: '在 MVP 4-seed 100% SC 数据上，max_lag 从 5 增大到 7，重跑 TY 检验。 确认 ECE/token_entropy→diversity
330	    的 lead time 精确值。 用 2σ signal onset 定义交叉验证。
331	
332	    '
333	  expected_results:
334	    ECE_to_distinct1_lead_maxlag5: 1
335	    ECE_to_distinct1_lead_maxlag7: 1
336	    token_entropy_to_distinct1_lead_maxlag5: 1
337	    token_entropy_to_distinct1_lead_maxlag7: 2
338	    ECE_to_distinct2_lead_maxlag7: 1
339	    token_entropy_to_distinct2_lead_maxlag7: 1
340	    ECE_to_perplexity_lead_maxlag7: 0
341	    truncation_artifact_detected: partial — token_entropy→distinct_1 增加 1 gen at maxlag=7
342	    cross_seed_consistency_maxlag7: 4/4 for ECE→distinct_1; 3/4 for token_entropy→distinct_1
343	      at lag=2
344	    effect_size_r_ECE_distinct1: 0.94
345	    effect_size_r_token_entropy_distinct1: 0.91
346	    signal_onset_2sigma_ECE_gen: 2.0
347	    signal_onset_2sigma_distinct1_gen: 3.5
348	    signal_onset_2sigma_perplexity_gen: 2.0
349	  result_rationale: '在 α=1.0 (100% SC) 下，collapse 进程快速：10 gen 的 time series 很短，max_lag=5
350	    消耗大量自由度。增大到 max_lag=7 后，token_entropy→distinct_1 的 lead 从 1 增到 2 gen ——说明 max_lag=5
351	    确实存在 mild truncation。但 ECE→distinct_1 不变（lag=1），因为 ECE 的响应更即时（calibration error
352	    在 distribution shift 第一代就跳变）。 canary→perplexity 在 max_lag=7 下仍无显著 lead (lag=0)，确认
353	    100% SC 下 perplexity 与 canary 同步崩溃不是截断伪影而是 genuine 同步性。 2σ onset 分析显示 ECE 在 gen
354	    2 就超出 baseline 2σ，distinct_1 在 gen 3-4 才 显著偏离——视觉上也能看出 ~1.5 gen lead，与 TY 的 1-2
355	    gen 一致。
356	
357	    '
358	  tables:
359	  - name: 'Table 1: MVP lead-lag summary (max_lag=7)'
360	    columns:
361	    - canary
362	    - target
363	    - TY_lead_gen
364	    - p_value_median
365	    - seeds_sig
366	    - effect_r
367	    - truncation_vs_lag5
368	    rows:
369	    - - ECE
370	      - distinct_1
371	      - 1
372	      - 0.001
373	      - 4/4
374	      - 0.94
375	      - unchanged
376	    - - ECE
377	      - distinct_2
378	      - 1
379	      - 0.002
380	      - 4/4
381	      - 0.92
382	      - unchanged
383	    - - token_entropy
384	      - distinct_1
385	      - 2
386	      - 0.003
387	      - 3/4
388	      - 0.91
389	      - +1 gen (was 1)
390	    - - token_entropy
391	      - distinct_2
392	      - 1
393	      - 0.004
394	      - 4/4
395	      - 0.9
396	      - unchanged
397	    - - ECE
398	      - perplexity
399	      - 0
400	      - 0.48
401	      - 0/4
402	      - 0.12
403	      - unchanged
404	    - - token_entropy
405	      - perplexity
406	      - 0
407	      - 0.55
408	      - 0/4
409	      - 0.08
410	      - unchanged
411	    - - effective_rank
412	      - distinct_1
413	      - —
414	      - 0.37
415	      - 0/4
416	      - —
417	      - —
418	    - - self_bleu
419	      - distinct_1
420	      - —
421	      - 0.61
422	      - 0/4
423	      - —
424	      - —
425	  figures_description:
426	  - 'Fig 1: 4-seed overlay of ECE, token_entropy, distinct_1, distinct_2, perplexity
427	    over 10 gen (α=1.0). Error bands = ±1σ across seeds. Vertical dashed lines mark
428	    2σ onset for each metric. Visual lead ~1-2 gen for canary→diversity.'
429	  - 'Fig S3: max_lag sensitivity plot. X-axis: max_lag (3–7). Y-axis: TY-estimated
430	    lead. 每条线一个 canary-target pair. 展示 token_entropy→distinct_1 在 lag=5→7 时 lead 增加.'
431	  analysis: 'Truncation 效应存在但 mild：仅影响 token_entropy→distinct_1 一个 pair (+1 gen)。
432	    核心结论不变：ECE 和 token_entropy lead diversity 1-2 gen，不 lead perplexity。 建议主文报告 max_lag=7
433	    结果，附录给出 sensitivity analysis。
434	
435	    '
436	- name: C4 cross-domain validation
437	  plan_id: plan_004
438	  description: 'Pythia-410M × C4 × α=0.50 × 3 seeds × 10 gen. 验证 canary ranking (ECE
439	    > token_entropy > failed families) 是否跨域保持, 以及 lead time 是否缩短。
440	
441	    '
442	  expected_results:
443	    canary_ranking_preserved: true
444	    ECE_to_distinct1_lead_gen: 1.0
445	    token_entropy_to_distinct1_lead_gen: 1.0
446	    ECE_to_distinct1_TY_pval_median: 0.012
447	    seeds_significant_ECE_distinct1: 3/3
448	    ECE_to_perplexity_lead_gen: 0.0
449	    gen10_perplexity_C4: 210.5
450	    gen10_distinct_1_C4: 0.098
451	    collapse_speed_vs_wiki: slightly faster
452	    lead_time_vs_wiki_alpha050: same (1 gen) or shorter
453	    effect_size_r_ECE_distinct1: 0.88
454	  result_rationale: 'C4 比 WikiText-103 更多样（web crawl vs curated Wikipedia），但 Pythia
455	    在 the Pile 上预训练（包含部分 web text），所以 C4 并非完全 out-of-distribution。在 α=0.50 下， canary
456	    ranking 应保持因为 ECE 和 token_entropy 检测的是分布偏移的通用信号（calibration degradation 和 entropy
457	    collapse），不依赖特定数据集的词汇分布。 Lead time 可能缩短到 1 gen（WikiText 在 α=0.50 也是 1 gen），因为
458	    C4 的 higher initial diversity 意味着 diversity 指标的下降需要更大的分布偏移才开始——但同时 canary 也需要更大偏移才触发
459	    2σ，两个效应部分抵消。 Effect size 略低 (0.88 vs 0.90) 因为 C4 的 heterogeneity 增加噪声。 Collapse
460	    略快因为 C4 子集的 domain 多样性使得 mode collapse 更容易发生（模型 倾向 collapse 到高频 domain patterns）。
461	
462	    '
463	  tables:
464	  - name: 'Table 5: C4 vs WikiText-103 comparison (α=0.50)'
465	    columns:
466	    - metric
467	    - WikiText_gen10
468	    - C4_gen10
469	    - delta_pct
470	    rows:
471	    - - perplexity
472	      - 185.3
473	      - 210.5
474	      - +13.6%
475	    - - distinct_1
476	      - 0.108
477	      - 0.098
478	      - -9.3%
479	    - - ECE
480	      - 0.167
481	      - 0.178
482	      - +6.6%
483	    - - token_entropy
484	      - 2.18
485	      - 2.09
486	      - -4.1%
487	    - - ECE→distinct_1 lead (gen)
488	      - 1
489	      - 1
490	      - '0'
491	    - - ECE→distinct_1 TY p
492	      - 0.008
493	      - 0.012
494	      - —
495	    - - ECE→distinct_1 effect_r
496	      - 0.9
497	      - 0.88
498	      - '-0.02'
499	  figures_description:
500	  - 'Fig 5: Side-by-side trajectory comparison WikiText vs C4 at α=0.50. Same axes,
501	    same metrics. 视觉上确认 ranking 和 lead 保持.'
502	  analysis: 'C4 验证了 canary ranking 的 domain-independence：ECE 和 token_entropy 仍是最佳
503	    canary。 Lead time 在 α=0.50 下保持 1 gen（未缩短也未延长），effect size 略降但仍 >0.85。 这足以支撑 "canary
504	    ranking transfers across domains" 的 claim，但需诚实报告 effect size 的下降。不宜 over-claim
505	    "universal canary"。
506	
507	    '
508	- name: Pythia-1.4B scale spot-check
509	  plan_id: plan_005
510	  description: 'Pythia-1.4B × WikiText-103 × α=0.50 × 3 seeds × 10 gen. 验证 canary
511	    lead 是否跨规模保持。
512	
513	    '
514	  expected_results:
515	    canary_ranking_preserved: true
516	    ECE_to_distinct1_lead_gen: 1.0
517	    ECE_to_distinct1_TY_pval_median: 0.029
518	    seeds_significant_ECE_distinct1: 2/3
519	    token_entropy_to_distinct1_lead_gen: 1.0
520	    token_entropy_to_distinct1_TY_pval_median: 0.038
521	    seeds_significant_token_entropy_distinct1: 2/3
522	    ECE_to_perplexity_lead_gen: 0.0
523	    gen10_perplexity_1_4B: 142.8
524	    gen10_distinct_1_1_4B: 0.121
525	    gen10_ECE_1_4B: 0.131
526	    cross_seed_variance_vs_410M: higher
527	    effect_size_r_ECE_distinct1: 0.85
528	    collapse_speed_vs_410M: slower
529	  result_rationale: '1.4B 参数量是 410M 的 ~3.4 倍。更大模型在 iterative SC 下 collapse 更慢（更大的
530	    representation capacity 和更好的 initial calibration 提供 buffer）。这意味着： (1) 各指标的绝对变化幅度更小（gen10
531	    perplexity 142 vs 185），信噪比降低； (2) canary lead 保持（1 gen）因为 lead 源于指标类型的本质差异（分布指标
532	    vs 多样性 指标的响应速度），与模型规模无关； (3) cross-seed variance 更高因为 1.4B 训练的随机性更大（更大参数空间 + 相同数据量
533	    = 更多局部最优的变异），导致仅 2/3 seeds 达到显著。 Effect size 下降到 0.85 因为 slower collapse = 更平缓的趋势
534	    = 更弱的统计信号。 结果 "noisy but directionally consistent" —— 符合 median 档预期。
535	
536	    '
537	  tables:
538	  - name: 'Table 6: Scale comparison 410M vs 1.4B (α=0.50, WikiText)'
539	    columns:
540	    - metric
541	    - 410M_gen10
542	    - 1.4B_gen10
543	    - delta_pct
544	    rows:
545	    - - perplexity
546	      - 185.3
547	      - 142.8
548	      - -22.9%
549	    - - distinct_1
550	      - 0.108
551	      - 0.121
552	      - +12.0%
553	    - - ECE
554	      - 0.167
555	      - 0.131
556	      - -21.6%
557	    - - token_entropy
558	      - 2.18
559	      - 2.41
560	      - +10.6%
561	    - - ECE→distinct_1 lead
562	      - 1
563	      - 1
564	      - '0'
565	    - - ECE→distinct_1 TY p
566	      - 0.008
567	      - 0.029
568	      - '+0.021'
569	    - - ECE→distinct_1 effect_r
570	      - 0.9
571	      - 0.85
572	      - '-0.05'
573	    - - ECE→distinct_1 seeds_sig
574	      - 3/3
575	      - 2/3
576	      - '-1'
577	  figures_description:
578	  - 'Fig 6: 410M vs 1.4B trajectory overlay at α=0.50. Dual y-axis for perplexity
579	    (left) and distinct_1 (right). Shaded ±1σ bands. 1.4B bands visibly wider.'
580	  analysis: 'Scaling trend: canary ranking and lead direction preserved, but statistical
581	    power drops. 这是 expected tradeoff——更大模型 collapse 更慢 = 信号更弱 = 需要更多 gen 或更多 seeds。
582	    Paper 应报告为 "directionally consistent scaling trend" 并标注 limitation： 完整 scale validation
583	    需要更长训练和更多 seeds（留作 future work）。 不宜用 1.4B 结果 over-claim scaling law。
584	
585	    '
586	- name: Extended run 20 gen (max_lag truncation check)
587	  plan_id: plan_006
588	  description: 'Pythia-410M × WikiText-103 × α=1.0 × 20 gen × 2 seeds. 增大 max_lag
589	    到 10，检验 token_entropy→perplexity 的 lag=-5 是否为截断伪影。
590	
591	    '
592	  expected_results:
593	    token_entropy_to_perplexity_lead_maxlag5: 0
594	    token_entropy_to_perplexity_lead_maxlag10: 0
595	    ECE_to_distinct1_lead_maxlag10: 2
596	    token_entropy_to_distinct1_lead_maxlag10: 2
597	    gen20_perplexity: 4280.5
598	    gen20_distinct_1: 0.018
599	    gen20_token_entropy: 0.72
600	    gen20_ECE: 0.623
601	    collapse_saturation_gen: 14
602	    post_saturation_behavior: all metrics plateau at floor/ceiling after gen ~14
603	    seeds_consistent: 2/2
604	  result_rationale: '20 gen 在 α=1.0 下提供足够长的序列来排除 max_lag truncation。如果 token_entropy
605	    真的 lead perplexity，更长序列 + 更大 max_lag 应该能检测到。预计仍然 lead=0： 在 100% SC 下，perplexity
606	    和 canary 的恶化由同一个机制驱动（distribution collapse → simultaneous calibration loss + fluency
607	    loss），没有 temporal separation。 这不是检测力不足，而是 genuine 同步性。 新发现：gen ~14 后所有指标 saturate（distinct_1
608	    接近 0，entropy 接近 ln(1)=0， perplexity 增长放缓因为模型已完全 degenerate）。20 gen 提供了完整的 collapse
609	    trajectory 包括 saturation phase，对 paper 的 Fig 1 有展示价值。 canary→diversity lead 增大到
610	    2 gen (max_lag=10)，与 plan_003 的 max_lag=7 一致， 确认更大 max_lag 能检测到更长 lead。
611	
612	    '
613	  tables:
614	  - name: 'Table S2: Extended run lead-lag (max_lag=10)'
615	    columns:
616	    - canary
617	    - target
618	    - lead_lag5
619	    - lead_lag7
620	    - lead_lag10
621	    - conclusion
622	    rows:
623	    - - ECE
624	      - distinct_1
625	      - 1
626	      - 1
627	      - 2
628	      - mild truncation at lag≤7
629	    - - token_entropy
630	      - distinct_1
631	      - 1
632	      - 2
633	      - 2
634	      - truncation confirmed at lag=5
635	    - - ECE
636	      - perplexity
637	      - 0
638	      - 0
639	      - 0
640	      - genuine synchrony, not truncation
641	    - - token_entropy
642	      - perplexity
643	      - 0
644	      - 0
645	      - 0
646	      - genuine synchrony, not truncation
647	  figures_description:
648	  - 'Fig S4: 20-gen trajectory (α=1.0). Full collapse curve including saturation phase.
649	    Vertical line at gen ~14 marking saturation onset.'
650	  - 'Fig S5: TY lead estimate as function of max_lag (3–10). Shows canary→diversity
651	    lead stabilizing at 2 for max_lag≥7, canary→perplexity flat at 0.'
652	  analysis: 'Extended run 解决了 two questions: (1) max_lag truncation 对 canary→diversity
653	    有 mild 影响 (lead=1→2)，对 canary→perplexity 无影响 (stays 0); (2) 100% SC 的 complete
654	    collapse trajectory 包括 saturation at gen ~14。 建议主文报告 max_lag=7 或 10 的结果（避免已知截断的
655	    max_lag=5），附录给出 sensitivity。
656	
657	    '
658	- name: CRS intervention experiment
659	  plan_id: plan_007
660	  description: 'CRS-predictive intervention vs no-intervention baseline. Pythia-410M
661	    × WikiText-103 × α=0.75 × 3 seeds × 10 gen. CRS 在 ECE 超过 threshold 时 trigger re-weighting
662	    to increase real data ratio.
663	
664	    '
665	  expected_results:
666	    baseline_gen10_distinct_1: 0.083
667	    baseline_gen10_perplexity: 512.7
668	    baseline_gen10_ECE: 0.312
669	    intervention_gen10_distinct_1: 0.118
670	    intervention_gen10_perplexity: 324.6
671	    intervention_gen10_ECE: 0.195
672	    diversity_preserved_pct: 42.2
673	    perplexity_reduction_pct: 36.7
674	    intervention_trigger_gen_median: 3.0
675	    intervention_trigger_gen_range:
676	    - 2
677	    - 4
678	    false_trigger_rate: 0.0
679	    seeds_with_improvement: 3/3
680	  result_rationale: 'α=0.75 是一个有意义的测试点：collapse 足够严重以展示 intervention 效果，但不至于 像 α=1.0
681	    那样 catastrophic（无法挽救）。CRS 基于 ECE threshold 触发（ECE 在 gen 2-4 超过 2σ baseline）。触发后，CRS
682	    将有效 α 从 0.75 降到 ~0.50（增加真实 数据比例），从而减缓后续 collapse。 预计 diversity 保留 ~42%（不是完全挽救，因为
683	    (1) 触发前已有 2-3 gen 的损伤， (2) CRS 只调整比例不改变训练动态）。Perplexity 改善更大 (~37%) 因为 perplexity
684	    对数据质量比例的响应更直接。 所有 3 seeds 都有改善因为 ECE threshold 的 trigger 是 reliable 的（plan_001
685	    确认 ECE 在 α=0.75 下 3/3 seeds 显著 lead diversity）。 这个实验的价值不在于 CRS 本身的 novelty，而是证明
686	    "predictive monitoring enables actionable intervention"——将 canary lead 从学术发现转化为实用工具。
687	
688	    '
689	  tables:
690	  - name: 'Table 7: Intervention comparison at α=0.75'
691	    columns:
692	    - condition
693	    - gen10_distinct_1
694	    - gen10_ppl
695	    - gen10_ECE
696	    - diversity_preserved
697	    rows:
698	    - - no-intervention
699	      - 0.083
700	      - 512.7
701	      - 0.312
702	      - —
703	    - - CRS-predictive
704	      - 0.118
705	      - 324.6
706	      - 0.195
707	      - 42.2%
708	    - - oracle (α=0.50 from start)
709	      - 0.108
710	      - 185.3
711	      - 0.167
712	      - benchmark
713	  figures_description:
714	  - 'Fig 7: Intervention timeline. X-axis: gen. Two trajectory bundles (no-intervention
715	    red, CRS blue). Vertical line at trigger gen. Shows divergence after intervention.'
716	  - 'Fig S6: Per-seed trigger gen distribution and post-trigger trajectory variance.'
717	  analysis: 'Intervention 实验将 canary lead 的学术发现转化为 actionable tool。42% diversity preservation
718	    不是 dramatic 但 non-trivial。关键 insight：CRS 的效果上限受限于 trigger latency（ECE 需要 2-3 gen
719	    才触发）和干预力度（仅调整混合比例）。 Paper 应将此定位为 "proof of concept for predictive monitoring"
720	    而非 "complete solution to model collapse"。与 DCES (reactive) 的对比：CRS 在 trigger gen
721	    就 干预，DCES 需要等到 diversity 本身下降才反应（多 1-2 gen 延迟）。
722	
723	    '
724	- name: Accumulate vs Replace 数据策略 ablation
725	  plan_id: plan_008
726	  description: 'α=0.50 下 accumulate (保留所有历史生成数据) vs replace (每代只用最新生成数据) × Pythia-410M
727	    × WikiText-103 × 3 seeds × 10 gen. 验证 Fu et al. 理论（accumulate 保证收敛）并测 canary 行为差异。
728	
729	    '
730	  expected_results:
731	    replace_gen10_distinct_1: 0.108
732	    replace_gen10_perplexity: 185.3
733	    replace_ECE_to_distinct1_lead: 1
734	    accumulate_gen10_distinct_1: 0.135
735	    accumulate_gen10_perplexity: 112.4
736	    accumulate_ECE_to_distinct1_lead: 1
737	    accumulate_collapse_speed: ~40% slower
738	    accumulate_canary_ranking_preserved: true
739	    accumulate_canary_lead_preserved: true
740	    accumulate_effect_size_vs_replace: lower (0.82 vs 0.90)
741	  result_rationale: 'Accumulate 模式通过保留所有历史数据稀释了 synthetic contamination 的有效比例—— 到
742	    gen 10，累积数据中真实数据仍占相当比例（不像 replace 模式每代都是 α=0.50 fresh synthetic）。Fu et al. 的理论预测
743	    accumulate 最终收敛到 fixed point 而非 diverge，empirically 表现为 collapse 速度减慢 ~40%。 Canary
744	    ranking 和 lead 保持（1 gen）因为 lead 的机制（指标类型的响应速度差异） 不依赖 data strategy。但 effect size
745	    降低因为 slower collapse = 更平缓的趋势 = 更弱的 temporal precedence signal。 这个实验的主要价值是 (1)
746	    验证 Fu et al. 理论预测, (2) 证明 canary 行为对 data strategy robust, (3) 为 practitioner
747	    提供 actionable recommendation（accumulate 优于 replace）。
748	
749	    '
750	  tables:
751	  - name: 'Table 8: Accumulate vs Replace (α=0.50)'
752	    columns:
753	    - strategy
754	    - gen10_distinct_1
755	    - gen10_ppl
756	    - collapse_rate
757	    - ECE→d1_lead
758	    - effect_r
759	    rows:
760	    - - replace
761	      - 0.108
762	      - 185.3
763	      - 1.0x (baseline)
764	      - 1
765	      - 0.9
766	    - - accumulate
767	      - 0.135
768	      - 112.4
769	      - 0.6x
770	      - 1
771	      - 0.82
772	  figures_description:
773	  - 'Fig S7: Accumulate vs Replace trajectories. 4 metrics × 2 strategies. Accumulate
774	    curves visibly flatter.'
775	  analysis: Accumulate 减缓 collapse 但不消除——符合 Fu et al. 的收敛到 degraded fixed point 的预测。Canary
776	    lead 保持是 positive result，说明监控策略对 data pipeline 选择 robust。 Effect size 降低是 expected
777	    tradeoff。Paper 中定位为 supplementary ablation， 不作为主要贡献。
778	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cedf667e-c3ed-4d93-b20e-ce3ffca02658",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "a9e37490c50c6f87d",
  "type": "user",
  "uuid": "7a275d42-00ab-4ec8-be20-d972f4929c22",
  "sourceToolAssistantUUID": "cedf667e-c3ed-4d93-b20e-ce3ffca02658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-14T19:23:49.483Z_

I now have a comprehensive picture. I've reviewed the paper (best-tier dream report), the actual code implementing the analysis, the median-tier dream report for comparison, the decisions log, framing document, roadmap, literature map, and experiment plan. This gives me enough material for a thorough methods and experiments review.

## R1: Methods & Experiments

### Summary
The paper proposes a framework using Toda-Yamamoto (TY) panel temporal precedence testing to identify which metrics ("canaries") predict model collapse in iterative self-consuming training and under what contamination regimes. The experimental coverage is comprehensive across eight planned experiments. However, the core statistical methodology is applied to extremely short time series (10-20 data points), raising fundamental concerns about the validity of the VAR-based inference, and several numerical results shift notably between the paper's "best" and "median" outcome tiers in ways that suggest the reported numbers may be aspirational rather than observed.

### Strengths
- S1: **Systematic experimental design.** The paper executes all 8 planned experiments covering the alpha-sweep, methodological ablation, cross-domain validation, scale spot-check, extended run, intervention proof-of-concept, and data strategy ablation. The experimental matrix (4 canary families x 2+ targets x 4 alpha values x 3-4 seeds) is well-structured.
- S2: **Honest reporting of null results.** Two of four canary families (effective_rank, self_BLEU) fail across all conditions. The paper reports these in full rather than omitting them, and discusses plausible failure mechanisms (representational stability despite output narrowing; sampling noise in self-BLEU).
- S3: **Methodological ablation is independently valuable.** The comparison of naive Pearson correlation vs. TY on non-stationary training trajectories (Table 3) is a genuine contribution: demonstrating that naive correlation inflates significance by 41% on these data provides a clear cautionary result for future empirical model collapse studies.
- S4: **Phase diagram framing is well-motivated.** Rather than overclaiming universal canary behavior, the paper explicitly maps where canary signals work (diversity targets, all alpha) and where they fail (perplexity target at high alpha), which is a more intellectually honest and scientifically informative framing than "canaries predict collapse."
- S5: **Cross-domain and scale robustness checks.** Testing on C4 and Pythia-1.4B adds meaningful validation, and the paper appropriately limits claims from these spot-checks rather than generalizing to "universal" findings.

### Weaknesses
- W1: **Critical degrees-of-freedom issue with TY on 10-point series.** The Toda-Yamamoto procedure fits a bivariate VAR(k + d_max) model. With k selected by AIC and d_max = 1, a typical model order of k=2 means VAR(3). A bivariate VAR(3) has 2 x (2 x 3 + 1) = 14 parameters (including intercepts). With T = 10 observations (and effective sample size T - k - d_max = 6-7 data points for estimation), the model is severely over-parameterized. The Wald test's chi-squared approximation requires T >> number of parameters, which is not satisfied here. This fundamental concern applies to all main results in Tables 1-2 and undermines the p-values reported throughout. The 20-generation extended run (T=20) partially alleviates this but is run only at alpha=1.0 with 2 seeds.

- W2: **Discrepancy between "best" and "median" outcome tiers reveals results may be simulated.** Comparing the best-tier paper (which is the one reviewed) to the median-tier imagined experiments reveals systematic disagreements: (a) canary->perplexity lead at alpha=0.50 is significant (p=0.032) in "best" but completely non-significant (p=0.31, 0/3 seeds) in "median"; (b) the 41% false-positive rate drops to 20% in "median"; (c) CRS diversity preservation is 77% in "best" vs 42% in "median"; (d) distinct_1 at alpha=0.50 is 0.198 in "best" vs 0.108 in "median." The MVP experiments (plan_003) are the only ones that appear to have actually run (mvp_v4_rep42 through rep45 show DONE/success). All other experiments (plan_001 through plan_008 except plan_003) appear to be in PREPARING or have no registry entries with success status. This strongly suggests the alpha-sweep, C4, scale, intervention, and accumulate results are projections rather than observed data.

- W3: **Multiple comparisons not corrected.** Table 2 reports TY p-values for 8 canary-target pairs x 4 alpha levels = 32 tests. No Bonferroni, Holm, or FDR correction is applied. Several "significant" results (ECE->perplexity at alpha=0.25: p=0.015; token_entropy->perplexity at alpha=0.50: p=0.041) would lose significance after even mild correction. The paper's core claim about the phase boundary relies on precisely these marginal associations being significant at low alpha and non-significant at high alpha.

- W4: **The "2/3 seeds significant" threshold is ad hoc and lenient.** The paper declares a canary-target pair as "reliably leading" if >= 2 out of 3 seeds show significant results. With only 3 seeds, 2/3 is the minimum possible majority, and given that each per-seed test already has inflated Type I error (due to W1), the joint probability of 2/3 false positives is non-trivial. No formal panel testing or meta-analytic combination is used to aggregate across seeds.

- W5: **Intervention experiment (CRS) has a confounded baseline.** CRS triggers at gen ~3.2 and reduces alpha from 0.75 to ~0.52. But the "oracle" comparison is alpha=0.50 from start, not alpha=0.75-then-switched-to-0.50-at-gen-3. The CRS matching the oracle on distinct_1 (both 0.198) is suspicious given the CRS runs at alpha=0.75 for 3 generations first. More importantly, the CRS intervention is simply "reduce alpha when ECE rises," which does not require lead-time prediction -- a reactive threshold on ECE itself (checking current-generation ECE against a threshold) would achieve the same effect since the trigger and the canary are the same metric.

- W6: **Effect size "r" definition unclear.** The paper reports effect sizes r > 0.88-0.94 but never defines what "r" measures in this context. In the code (analyze_mvp.py), the "peak_corr" is the cross-correlation at the optimal lag, but cross-correlation between two co-declining non-stationary series will be high by construction. If "r" is the peak cross-correlation, it confounds the shared trend with the lead-lag structure and is not a meaningful effect size for the temporal precedence claim.

### Questions for Authors
- Q1: With T=10 observations and a bivariate VAR(k+1) model where k>=2, can you provide evidence that the Wald test's asymptotic chi-squared distribution is valid? Have you compared the TY p-values against bootstrap-based p-values or performed Monte Carlo simulations under the null to verify the test's calibration at this sample size?

- Q2: The paper claims ECE->perplexity lead exists at alpha<=0.50 (p=0.032) but not at alpha>=0.75. The median-tier analysis of your own project finds this lead is non-significant even at alpha=0.50 (p=0.31). Can you confirm which experiments have actually been run vs. projected, and provide raw per-seed metric trajectories for independent verification?

- Q3: What is the formal definition of the effect size "r" reported in Tables 1 and 6? Is it the cross-correlation at optimal lag, the TY Wald test statistic rescaled, or something else? If it is peak cross-correlation, how do you disentangle shared trend from genuine lead-lag structure in this effect size?

- Q4: The CRS intervention triggers based on ECE exceeding a 2-sigma threshold at the current generation. Why does this require lead-time prediction rather than simple reactive monitoring? A reactive system checking ECE at each generation and reducing alpha when ECE first rises would intervene at exactly the same time. What additional value does the TY temporal precedence framework provide for the intervention beyond what threshold monitoring achieves?

- Q5: The phase boundary alpha* ~ 0.60 is estimated from only 4 alpha values with a visually interpolated transition. What is the statistical basis for this estimate, and how sensitive is it to noise? Could the true boundary be anywhere in [0.25, 0.75] given the data?

### Missing Experiments / Suggestions
- **Bootstrap or permutation-based p-values for TY tests at T=10.** The asymptotic chi-squared approximation is unreliable at this sample size. A residual bootstrap or parametric bootstrap under the null should be used to calibrate the test.
- **Multiple comparisons correction.** Apply Benjamini-Hochberg FDR correction across the 32 TY tests in Table 2 and report adjusted p-values.
- **Finer alpha grid near the claimed boundary.** Alpha = {0.40, 0.50, 0.55, 0.60, 0.65, 0.70} with the same seed count would be needed to credibly establish a phase boundary rather than interpolating from 4 points.
- **Reactive intervention baseline.** Compare CRS against a simple reactive baseline that reduces alpha when ECE (or distinct_1 itself) exceeds a threshold, to isolate the value of temporal precedence prediction vs. simple monitoring.
- **Longer generation horizon as default.** Given the extreme DOF concerns at T=10, consider 20+ generations as the primary experimental setting rather than a supplementary check.
- **A model family outside Pythia** (e.g., LLaMA, GPT-2) to test whether the canary phenomenon is architecture-specific within the Pythia family's shared pretraining.

### Soundness Score: 2 (out of 4)
The core statistical methodology (TY on 10-point series) operates well outside its validity regime, multiple comparisons are uncorrected, and strong evidence suggests that most reported results (7 of 8 experiments) are projections rather than observed data. The MVP results (Table 5 in the original submission, corresponding to plan_003) are on firmer ground but alone do not support the full set of claims.

### Presentation Score: 3 (out of 4)
The paper is well-organized with clear tables, honest null-result reporting, and a well-motivated framing. The writing is concise. Deductions for the undefined effect size metric and the lack of transparency about which experiments were actually run.

### Overall Score: 3 (Weak Reject)
The research question is important and the systematic framework is promising, but the statistical foundation is insufficiently rigorous for the claims made. The TY procedure on 10-point series is fundamentally underpowered and likely miscalibrated; the phase boundary claim rests on marginal p-values that would not survive multiple comparisons correction; and strong circumstantial evidence suggests most results beyond the MVP are projected rather than observed. The MVP finding (ECE and token entropy lead diversity by 1-2 generations at alpha=1.0) is credible and interesting but insufficient alone for a full paper at this venue. A revision with longer generation horizons (20+ as default), bootstrap-calibrated p-values, FDR correction, and actual execution of the alpha-sweep experiments would substantially strengthen the contribution.

### Confidence: 4 (out of 5)
I am confident in the statistical concerns raised (DOF, multiple comparisons, asymptotic approximation validity). The observation about projected vs. observed results is based on cross-referencing the project registry, decision log, and the divergence between best/median tiers, which provides strong circumstantial evidence. The one point of uncertainty is whether the authors may have run experiments outside the tracked registry that I cannot see.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a275d42-00ab-4ec8-be20-d972f4929c22",
  "isSidechain": true,
  "agentId": "a9e37490c50c6f87d",
  "requestId": "req_011Cb31H8VtkT8zTmF5AzuJr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4503021-f363-483f-a610-102a688004b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMfi4sWiVM68wzG4qNjPUA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12948,
      "cache_read_input_tokens": 88209,
      "output_tokens": 2914,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12948
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2914,
          "cache_read_input_tokens": 88209,
          "cache_creation_input_tokens": 12948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12948,
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
