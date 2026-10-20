# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review the following pape

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aaf84bf95d906bf61.jsonl`
- **Structured JSON:** [`6824f23c32bdc4679c86.json`](../../sessions/68/6824f23c32bdc4679c86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-14T19:21:55.675Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review the following paper thoroughly and produce a structured review.

**Paper**: "Mapping the Predictability Boundary of Model Collapse: Calibration Canaries and Regime-Dependent Early Warning in Iterative Synthetic Data Training"

**Paper content summary** (7 pages):

The paper studies iterative self-consuming (SC) training where models train on their own synthetic outputs across generations, leading to "model collapse." The core contribution is a systematic framework using Toda-Yamamoto (TY) panel temporal precedence analysis to identify which metrics ("canaries") predict collapse and under what contamination regimes.

**Four stated contributions:**
1. A TY panel analysis establishing ECE and token entropy as robust canaries for diversity collapse with 1–2 generation lead time across four seeds, two datasets, and two model scales.
2. A predictability phase diagram showing canary→perplexity lead is regime-dependent: detectable only at α=0.25, absent at α≥0.50.
3. A methodological ablation showing TY overturns 20% of naive correlation-based lead-lag claims.
4. A proof-of-concept CRS intervention preserving 42% of diversity.

**Related work section (Section 2) covers three areas:**
- Model Collapse: Shumailov et al., Fu et al. (accumulate vs replace convergence), Dohmatob et al. (scaling laws)
- Monitoring and Intervention: SIGMA (spectral monitoring, no temporal precedence), DCES (reactive intervention with 1-2 gen delay), Truong & Truong (early-warning failure under first-order phase transitions)
- Calibration as Early Signal: Du et al. (informal ECE observation, no formal test, no multi-family comparison, no regime characterization)

**Method (Section 3):**
- Iterative SC loop with Pythia-410M/1.4B on WikiText-103/C4
- Four canary families: ECE, token entropy, effective rank, self-BLEU
- Targets: distinct-1/2, perplexity
- Toda-Yamamoto procedure: augment VAR(k) with d_max extra lags, test via Wald χ² statistic
- Significance threshold: ≥2/3 seeds, median p-value reported

**Experimental results:**
- ECE and token entropy lead diversity by 1-2 generations across all α, with large effect sizes
- Canary→perplexity lead only at α=0.25 (marginal)
- TY overturns 20% of naive Pearson correlations (19/96 pairs)
- C4 cross-domain: canary ranking preserved
- Pythia-1.4B: directionally consistent but weaker signal (2/3 seeds)
- 20-gen extended run confirms genuine synchrony for canary→perplexity
- CRS intervention: 42.2% diversity preserved at α=0.75
- Accumulate vs Replace: canary framework robust to data strategy

**Limitations acknowledged:**
1. Scale limited to 410M/1.4B
2. 10-gen horizon may underestimate lead at low α
3. CRS is proof-of-concept with simple thresholds
4. Only autoregressive LMs studied

**Your review should cover:**

1. **Novelty assessment**: How novel is the contribution? Is applying TY to model collapse metrics genuinely new or incremental? How does the "predictability phase diagram" concept advance the field beyond existing knowledge?

2. **Related work completeness**: Are there missing references? Consider: other model collapse monitoring work, calibration drift literature outside model collapse, Granger causality applications in ML, synthetic data quality metrics.

3. **Positioning**: Does the paper fairly represent prior work? Is the gap vis-à-vis Du et al. real or overstated? Does the paper adequately distinguish from SIGMA and DCES?

4. **Significance and impact**: Would this paper advance the field meaningfully? Who benefits from these results? Is the 1-2 generation lead practically useful?

5. **Framing and narrative**: Is the "phase diagram" framing justified by the data (only 3-4 discrete α values)? Is "20% overturned" a meaningful contribution or a methodological footnote?

**Output format** (use exactly this structure):

```
## R2: Novelty & Related Work

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

### Missing References / Positioning Issues
- ...

### Novelty Score: [1-4] (1=trivial, 4=groundbreaking)
### Significance Score: [1-4]
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
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "75c4028e-574b-4ad1-bf61-2b69f674e651",
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

_source line 2 · 2026-05-14T19:21:55.677Z_

```json
{
  "parentUuid": "75c4028e-574b-4ad1-bf61-2b69f674e651",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
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
  "uuid": "1c0612b8-3b5e-4af9-8d00-cd954227cd46",
  "timestamp": "2026-05-14T19:21:55.677Z",
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

_source line 3 · 2026-05-14T19:21:58.180Z_



I'll start by reading the paper and any related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c0612b8-3b5e-4af9-8d00-cd954227cd46",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31Eyqgj8NVQcPu6jXMh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff976083-6af0-4454-b922-11e0d38c6b04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6YMnELHdyuhvcuTcjjnMW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7074,
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

_source line 4 · 2026-05-14T19:21:59.628Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MmyXdNungkHKcqkg83wfVT`</summary>

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
  "parentUuid": "ff976083-6af0-4454-b922-11e0d38c6b04",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31Eyqgj8NVQcPu6jXMh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e231a87-d2e4-4841-8fef-fe8f02c7df75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6YMnELHdyuhvcuTcjjnMW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 8251,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7074,
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

_source line 5 · 2026-05-14T19:21:59.634Z_

<details><summary>↩ Tool result · `toolu_01MmyXdNungkHKcqkg83wfVT`</summary>

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
  "parentUuid": "5e231a87-d2e4-4841-8fef-fe8f02c7df75",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "6ff534e6-b51a-493e-ac6f-fc3252605589",
  "sourceToolAssistantUUID": "5e231a87-d2e4-4841-8fef-fe8f02c7df75",
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

_source line 6 · 2026-05-14T19:22:01.939Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff534e6-b51a-493e-ac6f-fc3252605589",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31FGz4yPrptsVxw493s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "060f1bc5-95a9-4486-a239-5b9f00d30e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9vVJ2CGjxBryFry1QAUV9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15325,
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

_source line 7 · 2026-05-14T19:22:02.419Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_0181EjaRaoHtG7abxttaCv6b`</summary>

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
  "parentUuid": "060f1bc5-95a9-4486-a239-5b9f00d30e24",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31FGz4yPrptsVxw493s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e7d775f-1c76-4574-b2d0-0721bbc121a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9vVJ2CGjxBryFry1QAUV9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15325,
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

_source line 8 · 2026-05-14T19:22:02.456Z_

<details><summary>↩ Tool result · `toolu_0181EjaRaoHtG7abxttaCv6b`</summary>

```text
{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (14 个)\n\n- **mvp_v4_rep44**: DONE (success) — \n- **alpha_sweep_a025_s42**: PREPARING — \n- **alpha_sweep_a000_s42**: PREPARING — \n- **mvp_rep44**: PREPARING — \n- **mvp_v4_rep45**: DONE (success) — \n- **mvp_v4_rep43**: DONE (success) — \n- **mvp_v4_rep42**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_v2_rep44**: PREPARING — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- mvp_v2_rep44（准备中）\n- mvp_rep44（准备中）\n\n## 近期结论\n- **mvp_v4_rep45** (success): —\n- **mvp_v4_rep44** (failed): —\n- **mvp_v4_rep43** (success): —\n\n## 趋势\n成功 3 / 负向 0 / 失败 3 / 共 10\n累计 GPU: 4.2h\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-19828: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_rep42: 已被终止 — unknown\n- mvp_rep43: 已被终止 — unknown\n- mvp_v2_rep42: 已被终止 — unknown\n- mvp_v2_rep43: 已被终止 — unknown\n- mvp_v3_rep42: 训练失败 — unknown\n- mvp_v3_rep43: 训练失败 — unknown\n- mvp_v4_rep44: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e7d775f-1c76-4574-b2d0-0721bbc121a6",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "ea5b8941-9a8f-46d0-900f-85923d8ddd88",
  "sourceToolAssistantUUID": "0e7d775f-1c76-4574-b2d0-0721bbc121a6",
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

_source line 9 · 2026-05-14T19:22:03.114Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SH1tiRgPzDrjHscZBCdG7x`</summary>

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
  "parentUuid": "ea5b8941-9a8f-46d0-900f-85923d8ddd88",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31FGz4yPrptsVxw493s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "846f091d-c352-4a95-a8f9-4054bdccd353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9vVJ2CGjxBryFry1QAUV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15325,
      "output_tokens": 180,
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
          "output_tokens": 180,
          "cache_read_input_tokens": 15325,
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

_source line 10 · 2026-05-14T19:22:03.126Z_

<details><summary>↩ Tool result · `toolu_01SH1tiRgPzDrjHscZBCdG7x`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- mvp_v2_rep44（准备中）\\n- mvp_rep44（准备中）\\n\\n## 近期结论\\n- **mvp_v4_rep45** (success): —\\n- **mvp_v4_rep44** (failed): —\\n- **mvp_v4_rep43** (success): —\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 3 / 共 10\\n累计 GPU: 4.2h\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19828: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_rep42: 已被终止 — unknown\\n- mvp_rep43: 已被终止 — unknown\\n- mvp_v2_rep42: 已被终止 — unknown\\n- mvp_v2_rep43: 已被终止 — unknown\\n- mvp_v3_rep42: 训练失败 — unknown\\n- mvp_v3_rep43: 训练失败 — unknown\\n- mvp_v4_rep44: 训练失败 — unknown\\n\", \"total_chars\": 560, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "846f091d-c352-4a95-a8f9-4054bdccd353",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "05b849d7-dbc3-4ba4-944b-94eeef4444d1",
  "sourceToolAssistantUUID": "846f091d-c352-4a95-a8f9-4054bdccd353",
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

_source line 11 · 2026-05-14T19:22:06.119Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PRVAooFqDa7MrWu9aM5tD6`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b849d7-dbc3-4ba4-944b-94eeef4444d1",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31FXtG1HFrHQddmokso",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e1361dd-df25-4fc6-b283-bac41f7cdd50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7jTrvgFCQondvD41ZbnZR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 16772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1471,
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

_source line 12 · 2026-05-14T19:22:06.127Z_

<details><summary>↩ Tool result · `toolu_01PRVAooFqDa7MrWu9aM5tD6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'distrib_canary_collapse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e1361dd-df25-4fc6-b283-bac41f7cdd50",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "c6b69d69-5e22-4bb2-ac69-90427a11ab8d",
  "sourceToolAssistantUUID": "9e1361dd-df25-4fc6-b283-bac41f7cdd50",
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

_source line 13 · 2026-05-14T19:22:06.642Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015thZjYwNthoCwy5jxbL6C9`</summary>

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
  "parentUuid": "c6b69d69-5e22-4bb2-ac69-90427a11ab8d",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31FXtG1HFrHQddmokso",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f46ddb4-9323-4c0d-bdbd-e73f592c9e7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7jTrvgFCQondvD41ZbnZR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 16772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1471,
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

_source line 14 · 2026-05-14T19:22:06.649Z_

<details><summary>↩ Tool result · `toolu_015thZjYwNthoCwy5jxbL6C9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ROADMAP.md\", \"content\": \"# distrib_canary_collapse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 19:09 UTC | 更新原因: plan_003 重分析结论：修正 perplexity 通道叙述（WEAK LEAD + ECE 反向因果），plan_006 升为 framing 判定实验\\n\\n## 核心方向\\n系统性映射迭代合成数据训练中 canary 指标的**可预测性边界**——哪些 collapse 维度可预测、用什么 canary、在什么 contamination regime 下。详见 paper_framing.md。\\n\\n**Refined narrative (D009→D010)**: Canary 指标（ECE/token_entropy）预测的是 diversity collapse（distinct_n 退化）。Perplexity 通道更复杂：token_entropy 对 perplexity 有一致的 lag=-5 弱信号（4/4 seed, p>0.05, N=11 效力不足），ECE 对 perplexity 呈反向因果（perplexity 领先 ECE）。plan_006（20-gen）是判定 token_entropy→perplexity 是否真实的关键实验。\\n\\n## 当前进展\\n- **阶段**: Research（MVP STRONG PASS + plan_003 max_lag=7 重分析完成）\\n- **MVP 核心发现**: ECE/token_entropy 领先 distinct_1/2 达 1-2 代（|r|>0.99, p<0.004, lag std=0.0）\\n- **plan_003 新发现**: token_entropy→perplexity lag=-5 是真实峰值（非截断），但 WEAK LEAD；ECE→perplexity 反向因果（lag=+4/+5）\\n- **排除指标**: self_bleu（方向不一致）、effective_rank（non-monotonic）、MAUVE（floor effect）\\n- **Framing**: \\\"Delineating Predictability Boundaries\\\"（D006），perplexity 通道叙述已修正（D010）\\n- **Target**: AAAI 2027（~Aug 2026 deadline）\\n- **Dream**: dream_20260514T184925 pending（full review mode）\\n- **代码部署**: ✅ α-sweep + accumulate + exit-code + 子采样 fix 已部署\\n- **累计 GPU**: 4.2h\\n\\n## 近期任务\\n- [ ] 启动 plan_001 α-sweep (P0): α∈{0.0, 0.25, 0.50, 0.75} × 3 seeds × 10 gen\\n- [ ] 启动 plan_006 extended 20-gen (P0): α=1.0 × 2 seeds × max_lag=10（**framing 判定实验**：token_entropy→perplexity 是否在 N=21 下变显著）\\n- [ ] 等 Dream 回调，按结果调整 framing/plan\\n- [ ] plan_002: 方法论 ablation（零 GPU，依赖 plan_001 数据）\\n\\n## GPU 预算\\n- **分配**: 2× RTX PRO 6000 Blackwell 96GB (westd-19828, cuda:0/cuda:1)\\n- **P0 估算**: ~48h（α-sweep 40h + extended run 8h）\\n- **P1 估算**: ~34h（C4 验证 10h + 1.4B spot-check 24h）\\n- **P2 估算**: ~20h（intervention 10h + accumulate ablation 10h）\\n- **总计**: ~102h，双卡 ~51h/卡（~2.1 天连续跑）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D010 | 2026-05-14 | plan_003 重分析修正 perplexity 通道叙述：WEAK LEAD 非断裂，ECE 反 | plan_003 |\\n| D009 | 2026-05-14 | MVP 4-seed STRONG PASS，进入 Research 阶段全面实验 | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep44, mvp_v4_rep45 |\\n| D008 | 2026-05-14 | distinct_3 lead-lag 结果待 4-seed 确认，如 lag 仍双峰则降级 inc | mvp_v4_rep42, mvp_v4_rep43 |\\n| D007 | 2026-05-14 | Post-MVP 实验优先级：α-sweep >> 方法 ablation > C4 数据集 > 规 | — |\\n| D006 | 2026-05-14 | 论文 framing 采用 \\\"delineating predictability boundari | mvp_v4_rep42, mvp_v4_rep43 |\\n| D005 | 2026-05-14 | MVP 中期决策：不重启实验，MAUVE demote 为 supplementary，等完整 10 | — |\\n| D004 | 2026-05-14 | MVP 参数修复: n_prompts 1000→5000, steps_per_gen 10000 | — |\\n| D003 | 2026-05-14 | 首选 AAAI 2027 (~Aug 2026)，May 25 ARR 不可行，后续 ARR cyc | — |\\n| D002 | 2026-05-14 | MVP ECE 用 next-token calibration，SC 协议用 full repla | — |\\n| D001 | 2026-05-14 | MVP 设计: Pythia-410M × WikiText-103 × 100% SC × 10  | — |\\n\\n\", \"total_chars\": 2736, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f46ddb4-9323-4c0d-bdbd-e73f592c9e7b",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "835bda87-8fd5-449e-9b23-41b93014e34e",
  "sourceToolAssistantUUID": "9f46ddb4-9323-4c0d-bdbd-e73f592c9e7b",
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

_source line 15 · 2026-05-14T19:22:07.603Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L6Qq56pXj5bTrZikmJnLeB`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "835bda87-8fd5-449e-9b23-41b93014e34e",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31FXtG1HFrHQddmokso",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f6a4d79-dee5-4748-9e81-bb38a6cf5cbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7jTrvgFCQondvD41ZbnZR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 16772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1471,
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

_source line 16 · 2026-05-14T19:22:07.611Z_

<details><summary>↩ Tool result · `toolu_01L6Qq56pXj5bTrZikmJnLeB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-14 — MVP 代码设计决策\\n\\n- **训练方式**: 用 HF Trainer，每代独立训练 steps_per_gen 步（非 epoch-based），避免数据量波动导致训练量不一致\\n- **Generation 0 = baseline**: 不训练，只计算初始指标，作为后续 degradation 的参照\\n- **synthetic_ratio 控制混合**: 1.0 = 纯合成（MVP 压力测试），以 synthetic 为基准，ratio<1 时按比例补 real\\n- **Self-BLEU 采样**: 随机抽 500 pairs 而非全组合（O(n²) 太贵），固定 seed=0 保证可复现\\n- **Effective rank**: 用 mean-pooled last hidden states 的协方差矩阵，exp(entropy of normalized eigenvalues)\\n- **MAUVE**: 依赖 mauve-text 包，用 eval_dataset（真实）vs gen_dataset（合成）对比\\n- **ECE**: next-token calibration，10 bins，softmax max prob vs correctness\\n- **Cross-correlation 分析**: normalize 后翻转符号使 \\\"collapse direction\\\" 一致为正，peak lag 的符号决定 lead/lag\\n- **Metrics JSON 每代独立保存 + 汇总**: gen_N/metrics.json 做细粒度追溯，all_metrics.json 做分析输入\\n\\n## 2026-05-14 — AutoDL 服务器经验\\n\\n- **HF 下载不要用 network_turbo 代理**（会卡死），改用 `HF_ENDPOINT=https://hf-mirror.com` 直连国内镜像\\n- **pip install 可以用 network_turbo**\\n- **服务器默认没有 tmux**，需手动 apt 安装\\n- 环境：conda base, Python 3.12.3, PyTorch 2.10.0+cu128, 2× RTX PRO 6000 Blackwell 96GB\\n- **服务器名**: `westd-19828`（非 autodl-rtx6000），submit_training_job 必须用此名\\n\\n## 2026-05-14 — 参数修复 (D004)\\n\\n- 原始参数：n_prompts=1000, steps_per_gen=10000 → 40 epochs/gen，过拟合导致指标骤然击穿\\n- 修正参数：n_prompts=5000, steps_per_gen=5000 → 4 epochs/gen，合理 fine-tuning 量\\n- WikiText-103 test split 仅 ~1500 条 ≥64 words 段落，不够 5000 prompts，改为从 train split 取 prompt 前缀（prompts 仅做生成种子，不参与 loss）\\n- 新数据放 data/wikitext103_5k/ 避免影响正在跑的实验\\n\\n## 2026-05-14 — 文献调研核心发现\\n\\n- 最直接竞争者：chen2025scales (arXiv 2510.05133) 报告 \\\"calibration degradation precedes accuracy loss\\\"——ECE 在 iter 1 + 30% synthetic 时上升 75%，accuracy 未显著变化。但**未做 lead-lag 因果分析**，也没多指标 panel\\n- 8 个文献空白中最关键的 3 个：(1) 无人做 canary Granger causality / lead-lag 量化 (2) ECE 在 collapse 场景下几乎未被系统研究 (3) 多指标 panel 框架完全缺失\\n- Novelty 风险：如果 chen2025scales 团队扩展工作，会侵蚀 ECE-as-canary 的 novelty。需在方法论（Granger causality 框架）上尽快建立壁垒\\n- 共收录 31 篇论文（含补全的 6 篇）\\n- SIGMA (arXiv 2601.03385): Gram matrix 谱双轨监控，我们的 effective rank 是其简化版\\n- Truong & Truong: Class 1 凸反馈 entropy collapse 是一阶相变，canary 在此 regime 可能失效\\n- Fu et al. (ICLR 2025): 恒定 real data 比例保证 STL 收敛，α-sweep 理论基础\\n\\n## 2026-05-14 — 运维教训\\n\\n- **kill_job 只杀 tmux session，不杀子进程**。旧进程 (v1) 存活导致 v2 写同一输出目录死锁。后续 kill 后必须用 `ps aux | grep iterative_train` 确认子进程全部死亡，必要时 `kill -9 $(pgrep -f iterative_train)`\\n- **提交新实验前必须确认输出目录干净**，或使用不同的输出路径\\n- **analyze_mvp.py dry-run 验证通过**：cross-correlation 逻辑正确，token_entropy 和 effective_rank 在信噪比充足时检测准确\\n- **pgrep -a iterative_train 匹配不到训练进程**：因为进程名是 `python`，不是脚本名。用 `nvidia-smi` 或 `ps aux | grep python` 检查\\n- **nohup 启动的实验不写 EXIT_CODE 哨兵**，cron 检测到进程退出后无法判断成功/失败，误判为 failed（rep44 事故）。已在 iterative_train.py 添加 EXIT_CODE 哨兵机制\\n\\n## 2026-05-14 — MVP 4-Seed 正式分析（FINAL VERDICT）\\n\\n- **Overall: STRONG PASS** — 2 个 canary 家族 (token_entropy, ECE) 各自对 ≥1 个 diversity 指标有 SIGNIFICANT LEAD\\n- **最强结果 (4/4 seed 完全一致, std=0)**:\\n  - token_entropy → distinct_1: lag=-1, |r|=0.993–0.998, p=0.0006–0.0036\\n  - ece → distinct_2: lag=-1, |r|=0.995–0.997, p=0.0001–0.0023\\n- **Demoted**: MAUVE (floor effect), effective_rank (non-monotonic, 2+/2- across seeds)\\n- **Eliminated**: self_bleu (方向不一致), ece→perplexity (ECE 反而滞后 perplexity)\\n\\n## 2026-05-14 — ⚠️ Narrative 约束（4-seed 确认 + max_lag=7 验证）\\n\\n- **Canary 仅能 lead diversity metrics (distinct_n)，不能 lead quality metric (perplexity)**\\n  - token_entropy→perplexity: lag=-5，4/4 seed 一致，但 p borderline（seed42 p=0.12）\\n  - **max_lag=7 重分析确认 lag=-5 不是截断伪影**——扩展搜索窗口后 lag 值完全不变（2026-05-14 验证）\\n  - 问题在统计功效不足（仅 10 代数据点），不在截断\\n  - ECE→perplexity: lag=+4.75（ECE 滞后 perplexity！完全反向）\\n  - 这限制论文 claim：只能声称 \\\"canary predicts diversity collapse\\\"，不能声称 \\\"canary predicts general model degradation\\\"\\n- **Narrative 方向建议**: \\\"distributional canaries predict diversity collapse, which is a necessary precursor to quality degradation\\\"——diversity 丧失先于 perplexity 退化\\n- **plan_006 (extended 20-gen) 可能突破此限制**：如果 max_lag 从 5 扩到 10，token_entropy→perplexity 的 lead 可能变显著\\n- **α-sweep (plan_001) 是关键实验**：100% SC 下 collapse 太剧烈（37x ppl↑），canary 和 perplexity 几乎同步恶化。温和条件（α=0.25-0.75）下 collapse 更渐进，canary 的 lead time 对 perplexity 可能有效\\n\\n## 2026-05-14 — mix_datasets bug 修复\\n\\n- **原逻辑**: 保全 synthetic，subsample real → 低 α 下 real 不足时比例静默偏移（α=0.25 变成实际 α=0.50）\\n- **修复后**: 双向 subsample（低 α: 保全 real + subsample syn; 高 α: 保全 syn + subsample real）\\n- 14/14 测试通过，全 α 范围误差 <0.05\\n\", \"total_chars\": 4245, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f6a4d79-dee5-4748-9e81-bb38a6cf5cbf",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "4cc81e3c-a698-436c-995b-63a4ebbb573c",
  "sourceToolAssistantUUID": "0f6a4d79-dee5-4748-9e81-bb38a6cf5cbf",
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

_source line 17 · 2026-05-14T19:22:08.022Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018LUWR1k8yrNs7qRNedFmwW`</summary>

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
  "parentUuid": "4cc81e3c-a698-436c-995b-63a4ebbb573c",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31FXtG1HFrHQddmokso",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78c33ea4-5e8a-4b5e-9c32-1ad6cbfbfde2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7jTrvgFCQondvD41ZbnZR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 16772,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1471
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 385,
          "cache_read_input_tokens": 16772,
          "cache_creation_input_tokens": 1471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1471,
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

_source line 18 · 2026-05-14T19:22:08.038Z_

<details><summary>↩ Tool result · `toolu_018LUWR1k8yrNs7qRNedFmwW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml\", \"content\": \"papers:\\n  # ============================================================\\n  # CORE MODEL COLLAPSE\\n  # ============================================================\\n  - id: \\\"shumailov2024curse\\\"\\n    title: \\\"The Curse of Recursion: Training on Generated Data Makes Models Forget\\\"\\n    authors: \\\"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\\\"\\n    venue: \\\"Nature\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2305.17493\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\\\"\\n      - \\\"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\\\"\\n      - \\\"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\\\"\\n      - \\\"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\\\"\\n    relevance_to_us: \\\"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\\\"\\n    metrics_studied: [\\\"perplexity\\\", \\\"distributional tail mass\\\"]\\n\\n  - id: \\\"alemohammad2024mad\\\"\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2307.01850\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"提出 Model Autophagy Disorder (MAD) 概念\\\"\\n      - \\\"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\\\"\\n      - \\\"在图像生成领域验证 self-consuming loop 的退化效应\\\"\\n    relevance_to_us: \\\"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\\\"\\n    metrics_studied: [\\\"FID\\\", \\\"precision\\\", \\\"recall\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"dohmatob2024tale\\\"\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2402.07043\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\\\"\\n      - \\\"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\\\"\\n      - \\\"混入少量干净数据可缓解 collapse 并引发 grokking 现象\\\"\\n      - \\\"在 transformer 算术任务和 Llama2 文本生成上验证\\\"\\n    relevance_to_us: \\\"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"scaling exponents\\\"]\\n\\n  - id: \\\"dohmatob2025strong\\\"\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\\\"\\n    venue: \\\"ICLR 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.04840\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"即使合成数据占比极小（1/1000），仍可导致 model collapse\\\"\\n      - \\\"更大的训练集并不能避免 collapse\\\"\\n      - \\\"更大的模型（random projection 近似下）反而可能放大 collapse\\\"\\n      - \\\"存在 interpolation threshold 的 double-descent 现象\\\"\\n    relevance_to_us: \\\"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\\\"\\n    metrics_studied: [\\\"test loss\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"guo2024linguistic\\\"\\n    title: \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\"\\n    authors: \\\"Yanzhu Guo, Guokan Shang, et al.\\\"\\n    venue: \\\"NAACL 2024 Findings\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.09807\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"evaluation\\\"\\n    key_findings:\\n      - \\\"递归微调中，linguistic diversity 在连续迭代中持续下降\\\"\\n      - \\\"创造性任务中 diversity 下降最显著\\\"\\n      - \\\"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\\\"\\n    relevance_to_us: \\\"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\\\"\\n    metrics_studied: [\\\"distinct-n\\\", \\\"type-token ratio\\\", \\\"syntactic diversity\\\", \\\"semantic diversity\\\"]\\n\\n  - id: \\\"briesch2024selfconsuming\\\"\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: \\\"Martin Briesch, Dominik Sobania, Franz Rothlauf\\\"\\n    venue: \\\"arXiv (2311.16822)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2311.16822\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"首次系统研究 LLM 的 self-consuming training loop\\\"\\n      - \\\"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\\\"\\n      - \\\"expanding data cycle（累积）在 50 代内保持 diversity\\\"\\n    relevance_to_us: \\\"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\\\"\\n    metrics_studied: [\\\"diversity\\\", \\\"quality\\\"]\\n\\n  - id: \\\"truong2025entropy\\\"\\n    title: \\\"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\\\"\\n    authors: \\\"Truong Xuan Khanh, Truong Quynh Hoa\\\"\\n    venue: \\\"arXiv (2512.12381)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2512.12381\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\\\"\\n      - \\\"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\\\"\\n      - \\\"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\\\"\\n    relevance_to_us: \\\"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\\\"\\n    gaps: \\\"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"autocorrelation\\\", \\\"variance\\\"]\\n\\n  - id: \\\"wang2026contaminated\\\"\\n    title: \\\"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\\\"\\n    authors: \\\"Kevin Wang, Hongqian Niu, Didong Li\\\"\\n    venue: \\\"arXiv (2602.16065)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.16065\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\\\"\\n      - \\\"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\\\"\\n      - \\\"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\\\"\\n    relevance_to_us: \\\"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\\\"\\n    gaps: \\\"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\\\"\\n    metrics_studied: [\\\"convergence rate\\\", \\\"population risk\\\"]\\n\\n  # ============================================================\\n  # CANARY / EARLY WARNING METRICS\\n  # ============================================================\\n  - id: \\\"chen2025scales\\\"\\n    title: \\\"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"arXiv (2510.05133)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.05133\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\\\"\\n      - \\\"20% synthetic data 以下性能稳定，30% 以上退化加速\\\"\\n      - \\\"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\\\"\\n      - \\\"推理任务比检索任务更易退化\\\"\\n      - \\\"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\\\"\\n    relevance_to_us: \\\"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\", \\\"perplexity\\\"]\\n\\n  - id: \\\"gambetta2024surplexity\\\"\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: \\\"Daniele Gambetta et al.\\\"\\n    venue: \\\"arXiv (2410.12341)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\\\"\\n      - \\\"用 semantic networks 分析文本重复性和语义多样性\\\"\\n      - \\\"用 next-token probability 定量衡量 diversity loss\\\"\\n      - \\\"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\\\"\\n      - \\\"不需要区分 human vs AI-generated data\\\"\\n    relevance_to_us: \\\"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\\\"\\n    metrics_studied: [\\\"surplexity\\\", \\\"semantic network metrics\\\", \\\"next-token probability\\\"]\\n\\n  - id: \\\"qiu2025spectral\\\"\\n    title: \\\"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\\\"\\n    authors: \\\"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\\\"\\n    venue: \\\"arXiv (2510.04202)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04202\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\\\"\\n      - \\\"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\\\"\\n      - \\\"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\\\"\\n      - \\\"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\\\"\\n    relevance_to_us: \\\"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\\\"\\n    metrics_studied: [\\\"spectral alignment\\\", \\\"weight norm\\\", \\\"gradient norm\\\"]\\n\\n  - id: \\\"he2025closer\\\"\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shiliang He et al.\\\"\\n    venue: \\\"NeurIPS 2025 (Spotlight)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"识别 diffusion model collapse 中的 generalization → memorization 转变\\\"\\n      - \\\"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\\\"\\n      - \\\"提出基于 entropy 的数据选择策略，有效缓解 collapse\\\"\\n    relevance_to_us: \\\"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\\\"\\n    metrics_studied: [\\\"entropy\\\", \\\"FID\\\", \\\"diversity\\\"]\\n\\n  - id: \\\"ba2024fill\\\"\\n    title: \\\"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\\\"\\n    authors: \\\"Yang Ba, Michelle V Mancenido, Rong Pan\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.10864\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\\\"\\n      - \\\"推导了基于 PAC 框架的 ECE bound\\\"\\n      - \\\"合成数据可改善 calibration 但需精心设计生成策略\\\"\\n    relevance_to_us: \\\"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"accuracy\\\"]\\n\\n  - id: \\\"sigma2026spectral\\\"\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: \\\"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\\\"\\n    venue: \\\"arXiv (2601.03385)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2601.03385\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"direct-competitor\\\"\\n    key_findings:\\n      - \\\"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\\\"\\n      - \\\"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\\\"\\n      - \\\"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\\\"\\n    relevance_to_us: \\\"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\\\"\\n    gaps: \\\"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\\\"\\n    metrics_studied: [\\\"Gram matrix eigenspectrum\\\", \\\"spectral norm bounds\\\"]\\n\\n  - id: \\\"kalinowski2026topology\\\"\\n    title: \\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\"\\n    authors: \\\"Alexander Kalinowski\\\"\\n    venue: \\\"arXiv (2604.26984)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2604.26984\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\\\"\\n      - \\\"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\\\"\\n      - \\\"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\\\"\\n    relevance_to_us: \\\"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\\\"\\n    gaps: \\\"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\\\"\\n    metrics_studied: [\\\"Collapse Index\\\", \\\"persistent homology features\\\"]\\n\\n  # ============================================================\\n  # DIVERSITY METRICS (BACKGROUND)\\n  # ============================================================\\n  - id: \\\"zhu2018texygen\\\"\\n    title: \\\"Texygen: A Benchmarking Platform for Text Generation Models\\\"\\n    authors: \\\"Yaoming Zhu et al.\\\"\\n    venue: \\\"SIGIR 2018\\\"\\n    year: 2018\\n    url: \\\"https://arxiv.org/abs/1802.01886\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\\\"\\n      - \\\"成为文本生成多样性评估的标准基准之一\\\"\\n    relevance_to_us: \\\"Self-BLEU 是我们 diversity canary 的经典候选\\\"\\n    metrics_studied: [\\\"Self-BLEU\\\", \\\"BLEU\\\"]\\n\\n  - id: \\\"li2016diversity\\\"\\n    title: \\\"A Diversity-Promoting Objective Function for Neural Conversation Models\\\"\\n    authors: \\\"Jiwei Li et al.\\\"\\n    venue: \\\"NAACL 2016\\\"\\n    year: 2016\\n    url: \\\"https://arxiv.org/abs/1510.03055\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\\\"\\n      - \\\"计算 unique n-gram 数占总 n-gram 数的比例\\\"\\n    relevance_to_us: \\\"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\\\"\\n    metrics_studied: [\\\"distinct-1\\\", \\\"distinct-2\\\"]\\n\\n  # ============================================================\\n  # REPRESENTATION / SPECTRAL COLLAPSE\\n  # ============================================================\\n  - id: \\\"jing2022understanding\\\"\\n    title: \\\"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\\\"\\n    authors: \\\"Li Jing et al.\\\"\\n    venue: \\\"ICLR 2022\\\"\\n    year: 2022\\n    url: \\\"https://openreview.net/forum?id=YevsQ05DEN7\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"定义 dimensional collapse：embedding 向量只跨越低维子空间\\\"\\n      - \\\"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\\\"\\n      - \\\"strong augmentation 和 implicit regularization 驱动低秩解\\\"\\n    relevance_to_us: \\\"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\\\"\\n    metrics_studied: [\\\"effective rank\\\", \\\"singular value spectrum\\\"]\\n\\n  - id: \\\"noci2024mind\\\"\\n    title: \\\"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\\\"\\n    authors: \\\"Lorenzo Noci et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2410.07799\\\"\\n    category: \\\"canary-metrics\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 Random Matrix Theory 分析 attention 层的 rank collapse\\\"\\n      - \\\"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\\\"\\n      - \\\"rank collapse in depth: 所有 token 沿层收敛到单一表示\\\"\\n    relevance_to_us: \\\"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\\\"\\n    metrics_studied: [\\\"spectral gap\\\", \\\"singular values\\\", \\\"effective rank\\\"]\\n\\n  # ============================================================\\n  # DATA MIXING & ACCUMULATION\\n  # ============================================================\\n  - id: \\\"kazdan2025collapse\\\"\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"系统对比 replace vs accumulate 场景\\\"\\n      - \\\"replace → collapse；accumulate → 可避免 collapse\\\"\\n      - \\\"发现 real data 和 synthetic data 之间存在非平凡的交互效应\\\"\\n      - \\\"synthetic data 的价值取决于 real data 的绝对数量\\\"\\n    relevance_to_us: \\\"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"dey2024breaking\\\"\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: \\\"Apratim Dey, David Donoho, et al.\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.01413\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"foundation\\\"\\n    key_findings:\\n      - \\\"替换数据 → 发散 population risk；累积数据 → 避免发散\\\"\\n      - \\\"证明累积策略在多种模型（GMM, HMM, LLM）上有效\\\"\\n    relevance_to_us: \\\"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\\\"\\n    metrics_studied: [\\\"population risk\\\"]\\n\\n  - id: \\\"epstein2024howbad\\\"\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: \\\"Mohamed El Amine Epstein et al.\\\"\\n    venue: \\\"arXiv (2404.05090)\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.05090\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"纯合成数据训练不可避免 collapse\\\"\\n      - \\\"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\\\"\\n      - \\\"递归训练使原始分布尾部消失\\\"\\n    relevance_to_us: \\\"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\\\"\\n    metrics_studied: [\\\"perplexity\\\"]\\n\\n  - id: \\\"fu2025selfconsuming\\\"\\n    title: \\\"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\\\"\\n    authors: \\\"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\\\"\\n    venue: \\\"ICLR 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2502.18865\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\\\"\\n      - \\\"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\\\"\\n      - \\\"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\\\"\\n    relevance_to_us: \\\"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\\\"\\n    gaps: \\\"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\\\"\\n    metrics_studied: [\\\"generalization bound\\\", \\\"population risk\\\"]\\n\\n  - id: \\\"bakshi2026improvement\\\"\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: \\\"Soham Bakshi, Sunrit Chakraborty\\\"\\n    venue: \\\"arXiv (2602.10531)\\\"\\n    year: 2026\\n    url: \\\"https://arxiv.org/abs/2602.10531\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"theoretical-foundation\\\"\\n    key_findings:\\n      - \\\"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\\\"\\n      - \\\"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\\\"\\n      - \\\"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\\\"\\n      - \\\"在 next-token prediction 语言模型上分析完整迭代演化动态\\\"\\n    relevance_to_us: \\\"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\\\"\\n    gaps: \\\"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\\\"\\n    metrics_studied: [\\\"population risk\\\", \\\"total variation distance\\\"]\\n\\n  # ============================================================\\n  # MITIGATION & VERIFICATION\\n  # ============================================================\\n  - id: \\\"feng2025escaping\\\"\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification\\\"\\n    authors: \\\"Yunzhen Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.16657\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"通过外部 verifier（human 或 better model）注入信息可避免 collapse\\\"\\n      - \\\"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\\\"\\n      - \\\"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\\\"\\n    relevance_to_us: \\\"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\\\"\\n    metrics_studied: [\\\"test loss\\\"]\\n\\n  - id: \\\"barzilai2025consistency\\\"\\n    title: \\\"When Models Don't Collapse: On the Consistency of Iterative MLE\\\"\\n    authors: \\\"Daniel Barzilai, Ohad Shamir\\\"\\n    venue: \\\"ICML 2025\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2505.19046\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\\\"\\n      - \\\"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\\\"\\n    relevance_to_us: \\\"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"dces2026counter\\\"\\n    title: \\\"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\\\"\\n    authors: \\\"Anonymous\\\"\\n    venue: \\\"MDPI Electronics (2026)\\\"\\n    year: 2026\\n    url: \\\"https://www.mdpi.com/2079-9292/15/4/869\\\"\\n    category: \\\"data-mixing\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"提出 DCES（dynamic center-edge sampling）数据选择框架\\\"\\n      - \\\"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\\\"\\n    relevance_to_us: \\\"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\\\"\\n    metrics_studied: [\\\"ECE\\\", \\\"entropy\\\"]\\n\\n  # ============================================================\\n  # POSITION / SURVEY / EPISTEMICS\\n  # ============================================================\\n  - id: \\\"schaeffer2025position\\\"\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\\\"\\n    venue: \\\"arXiv (2503.03150)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\\\"\\n      - \\\"许多 collapse 预测依赖于与现实不符的假设\\\"\\n      - \\\"多种 collapse 场景是可以轻易避免的\\\"\\n    relevance_to_us: \\\"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"wang2025epistemic\\\"\\n    title: \\\"Epistemic Diversity and Knowledge Collapse in Large Language Models\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv (2510.04226)\\\"\\n    year: 2025\\n    url: \\\"https://arxiv.org/abs/2510.04226\\\"\\n    category: \\\"core-collapse\\\"\\n    role: \\\"background\\\"\\n    key_findings:\\n      - \\\"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\\\"\\n      - \\\"所有模型的 epistemic diversity 低于基本 web 搜索\\\"\\n      - \\\"模型越大 epistemic diversity 反而越低；RAG 有正面效果\\\"\\n    relevance_to_us: \\\"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\\\"\\n    metrics_studied: [\\\"epistemic diversity\\\"]\\n\\n  # ============================================================\\n  # METHODOLOGY (GRANGER / LEAD-LAG)\\n  # ============================================================\\n  - id: \\\"shojaie2022granger\\\"\\n    title: \\\"Granger Causality: A Review and Recent Advances\\\"\\n    authors: \\\"Ali Shojaie, Emily B. Fox\\\"\\n    venue: \\\"Annual Review of Statistics and Its Application\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2105.02675\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"Granger causality 综述：从经典线性到非线性/neural 方法\\\"\\n      - \\\"Panel data 场景的 Granger causality 扩展\\\"\\n      - \\\"VAR 和 neural Granger causality 的对比\\\"\\n    relevance_to_us: \\\"为我们的 panel Granger causality 分析提供方法论基础\\\"\\n    metrics_studied: []\\n\\n  - id: \\\"marcinkevics2022neural\\\"\\n    title: \\\"Granger Causality Using Neural Networks\\\"\\n    authors: \\\"Raphael Marcinkevics, Julia Vogt\\\"\\n    venue: \\\"arXiv (2208.03703)\\\"\\n    year: 2022\\n    url: \\\"https://arxiv.org/abs/2208.03703\\\"\\n    category: \\\"methodology\\\"\\n    role: \\\"method-component\\\"\\n    key_findings:\\n      - \\\"用 neural network 估计 Granger causality，突破线性假设\\\"\\n      - \\\"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\\\"\\n    relevance_to_us: \\\"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\\\"\\n    metrics_studied: []\\n\\ngaps:\\n  - \\\"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\\\"\\n  - \\\"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\\\"\\n  - \\\"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\\\"\\n  - \\\"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\\\"\\n  - \\\"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\\\"\\n  - \\\"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\\\"\\n  - \\\"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\\\"\\n  - \\\"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\\\"\\n\\nnovelty_assessment: |\\n  我们项目的核心 novelty 在于：\\n\\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\\n     但没有人做过系统的 lead-lag 量化分析。\\n\\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\\n     现有工作都是单一指标或最多两三个指标的孤立分析。\\n\\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\\n     但没人研究 canary 在不同 alpha 下的行为。\\n\\n  4. **与已有工作的差异**：\\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\\n       我们将类似思路迁移到 iterative collapse 场景\\n\\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\\n\", \"total_chars\": 24089, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78c33ea4-5e8a-4b5e-9c32-1ad6cbfbfde2",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "61acfe94-b1cb-481a-8030-ff21260816f6",
  "sourceToolAssistantUUID": "78c33ea4-5e8a-4b5e-9c32-1ad6cbfbfde2",
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

_source line 19 · 2026-05-14T19:22:13.130Z_

Now let me read the paper framing and any actual paper/artifact files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61acfe94-b1cb-481a-8030-ff21260816f6",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31Fu1zpeW3fZZ7ZuKf7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "663646b2-550a-491e-ba38-2a430159f4d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6MWMxirhA2d8aEKeSkJBU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17371,
      "cache_read_input_tokens": 18243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17371,
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

_source line 20 · 2026-05-14T19:22:14.082Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ryxq4du9pu554vma9ayZQS`</summary>

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
  "parentUuid": "663646b2-550a-491e-ba38-2a430159f4d4",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31Fu1zpeW3fZZ7ZuKf7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ebb25ae-d0b9-4d40-9476-2da2fcfe5dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6MWMxirhA2d8aEKeSkJBU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17371,
      "cache_read_input_tokens": 18243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17371,
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

_source line 21 · 2026-05-14T19:22:14.089Z_

<details><summary>↩ Tool result · `toolu_01Ryxq4du9pu554vma9ayZQS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_framing.md\", \"content\": \"# Paper Framing — distrib_canary_collapse\\n\\n## Target Venue\\n- Primary: AAAI 2027 (expected deadline ~August 2026)\\n- Fallback: EMNLP 2026 Findings (ARR October cycle if AAAI timeline tight)\\n- Note: EMNLP 2026 Main ARR May deadline已过；AAAI 2027 给出充足实验时间\\n\\n## Core Claims (3 条)\\n\\n1. **Canary→Diversity Lead**: 在迭代合成数据训练中，ECE 和 token entropy 作为廉价 canary 指标，稳定领先 diversity 退化（distinct_1/2）1-2 代——提供可量化的早期预警窗口。\\n2. **Regime-Dependent Predictability**: 可预测性取决于 contamination regime——100% SC 下 token_entropy→perplexity 存在一致的 lag=-5 弱信号（4/4 seed, p=0.058-0.12）但 N=11 统计效力不足，ECE→perplexity 则呈反向因果（perplexity 领先 ECE）。低 α 条件下 canary lead time 有望扩展。Predictability phase diagram 划定可预测/不可预测边界。\\n3. **Methodological Rigor**: 朴素相关分析在非平稳训练指标上产生伪回归；Toda-Yamamoto panel temporal precedence 提供统计严谨的 lead-lag 量化，方法论 ablation 量化伪显著关联被推翻的比例。\\n\\n## Story Spine\\n\\n- **Problem**: Model collapse 的在线监控工具已存在（SIGMA 谱监控、DCES 反应式干预），但没有工作系统性回答\\\"哪些指标最早预测崩溃、领先多久、在什么 regime 下有效\\\"。Du et al. 非正式观察到 ECE 领先 accuracy，但仅限单指标对、1-3 代、无统计检验。\\n\\n- **Existing approaches & their gaps**: SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足（无正式 time-series 检验、无多家族对比）；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效——但仅限特定 regime 和特定指标族。\\n\\n- **Our framing**: 我们不是提出\\\"通用 canary\\\"，而是**系统性映射可预测性的边界**——哪些 collapse 维度可预测（diversity）、哪些不可预测（perplexity in extreme regime）、在什么 contamination 条件下、用什么统计方法。Null results（canary 不 lead perplexity）不是失败，而是 phase diagram 中的一个 boundary data point。\\n\\n- **Headline result template**: \\\"ECE and token entropy predict diversity collapse 1-2 generations ahead (|r|>0.99, p<0.001, 4/4 seeds) in iterative synthetic data training, while a predictability phase diagram reveals regime-dependent boundaries where canary signals exist vs. where synchronous collapse precludes early warning.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n| Concern | Response Strategy | Required Experiment |\\n|---------|-------------------|---------------------|\\n| \\\"Canary 不预测 perplexity，实用价值有限\\\" | Framing 为 regime-dependent：100% SC 下 token_entropy 有 lag=-5 弱信号（plan_006 20-gen 验证）；α-sweep 展示低 α 下是否变显著 | α-sweep (P0) + plan_006 (P0) |\\n| \\\"ECE 和 token_entropy 对 perplexity 方向相反？\\\" | 诚实报告不对称性：token_entropy 捕捉分布收窄前驱信号（lead），ECE 作为 calibration 指标反映后期适应效应（lag）。两者覆盖 collapse 不同阶段 | 已有 MVP+plan_003 数据 |\\n| \\\"只在 Pythia-410M 上验证，scale 泛化？\\\" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |\\n| \\\"WikiText-103 单一数据集\\\" | C4 cross-domain validation | domain-transfer (P1) |\\n| \\\"为什么不用简单相关分析？\\\" | 方法 ablation：naive corr vs Toda-Yamamoto，量化伪显著比例 | method-ablation (P0, 零 GPU) |\\n| \\\"4 个 canary 中 2 个失败，选择偏差？\\\" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |\\n| \\\"Intervention 实验缺失\\\" | CRS-triggered vs reactive vs no-intervention 对比 | intervention (P2) |\\n\\n## Venue Fit\\n\\nAAAI 2027 优势：\\n- ML 方法论 track 接受 empirical analysis + 统计方法论贡献\\n- 不要求 SOTA，接受 systematic study with novel methodology\\n- Phase diagram / regime boundary 概念在 AAAI 偏理论的审稿人中有吸引力\\n\\n风险：\\n- 如果被认为\\\"只是 empirical study 没有算法贡献\\\"→ 补 CRS + intervention 提升 method 贡献\\n- 模型规模偏小（Pythia-410M/1.4B）→ 诚实标注 limitation + scaling trend\\n\\n## Key Narrative Constraints (from MVP + plan_003)\\n\\n1. **不能 claim \\\"canary predicts model collapse\\\"** — 只能 claim \\\"canary predicts diversity collapse\\\"。token_entropy→perplexity 在 100% SC 下存在一致的 lag=-5 弱信号（4/4 seed, p=0.058-0.12），但 N=11 统计效力不足——用\\\"统计不显著的弱信号\\\"而非\\\"通道断裂\\\"。plan_006（20-gen, N=21）是判定实验\\n2. **ECE→perplexity 呈反向因果** — perplexity 领先 ECE 4-5 代（lag=+4/+5, p<0.01）。与 token_entropy→perplexity（canary 领先）方向相反。论文必须讨论两个 canary 家族在 perplexity 通道上的不对称性\\n3. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果\\n4. **distinct_3 的 lead time 不如 distinct_1/2 可靠** — max_lag=7 下升为 SIGNIFICANT 但 lag_std>1.5（双峰：seed 42 总是 -5，其余 -1/-2），维持 D008 降级策略，主文聚焦 distinct_1/2\\n5. **max_lag=7 确认核心 lead 无截断** — token_entropy→distinct_1 lag=-1（std=0.0）、ECE→distinct_2 lag=-1（std=0.0）在 max_lag=5/7 下完全一致。token_entropy→perplexity lag=-5 是真实峰值非截断伪影\\n\", \"total_chars\": 3872, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ebb25ae-d0b9-4d40-9476-2da2fcfe5dcf",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "3ccde6a1-f915-4ec4-9aae-41ec1ec242a0",
  "sourceToolAssistantUUID": "9ebb25ae-d0b9-4d40-9476-2da2fcfe5dcf",
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

_source line 22 · 2026-05-14T19:22:14.483Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YTxXUDtNYFwoKBd9PUN62V`</summary>

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
  "parentUuid": "3ccde6a1-f915-4ec4-9aae-41ec1ec242a0",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31Fu1zpeW3fZZ7ZuKf7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "948c60e1-43ea-4ca2-92e7-25e6eeaf21f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6MWMxirhA2d8aEKeSkJBU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17371,
      "cache_read_input_tokens": 18243,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17371
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 18243,
          "cache_creation_input_tokens": 17371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17371,
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

_source line 23 · 2026-05-14T19:22:14.490Z_

<details><summary>↩ Tool result · `toolu_01YTxXUDtNYFwoKBd9PUN62V`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/decisions.yaml\", \"content\": \"_next_id: 11\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 设计: Pythia-410M × WikiText-103 × 100% SC × 10 gen × 3 reps，验证 canary\\n    时序领先性'\\n  rationale: 100% SC 是最激进的 collapse 条件（理论预测必然退化），如果在此条件下没有任何 canary 指标领先 downstream，项目前提不成立。3\\n    reps × 10 gen 给出足够时间点做 cross-correlation。计算量 ~9 H100-hours，极低风险。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:26 UTC\\n  summary: MVP ECE 用 next-token calibration，SC 协议用 full replacement，effective rank\\n    用模型自身 embedding\\n  rationale: 'Reviewer warning 要求澄清 3 个操作化定义。ECE: next-token calibration 是 LM 原生度量、零额外成本，与\\n    Du et al. 的对比留到全量阶段加 downstream task ECE。SC: full replacement 是最大 feedback amplification\\n    (Truong & Truong Class 1)，collapse 信号最强，适合 MVP 压力测试。Effective rank: 模型自身 embedding\\n    与 SIGMA 一致，零额外依赖。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:27 UTC\\n  summary: 首选 AAAI 2027 (~Aug 2026)，May 25 ARR 不可行，后续 ARR cycle 备选\\n  rationale: 项目 2026-05-14 立项，无服务器无代码，11 天内无法完成 MVP + 全量实验 + 论文。AAAI 2027 给 ~2.5 个月，充分覆盖\\n    500-600 H100-hours 的实验量和论文写作。后续 ARR cycle (Jul/Aug) 也在射程内。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-14 05:36 UTC\\n  summary: 'MVP 参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000 (4 epochs/gen)'\\n  rationale: Reviewer 发现原配置下 40 epochs/gen 在 1000 samples 上严重过拟合，模型可能 1-2 代即骤然击穿，所有指标同时崩溃，无法观察\\n    lead-lag 时序结构。修改后 4 epochs/gen 接近文献实践，collapse 逐渐发展，给 cross-correlation 分析留出足够时间点。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D005\\n  date: 2026-05-14 08:39 UTC\\n  summary: MVP 中期决策：不重启实验，MAUVE demote 为 supplementary，等完整 10-gen 数据再判断 collapse 速度和\\n    lead-lag\\n  rationale: MAUVE 基线 0.034 触发 evaluation criteria §4 floor effect 规则。Gen 0→1 跳变大是\\\"未训练→首次训练\\\"的固有落差，后续\\n    gen 的增量变化才是分析目标。100% SC 如果确认无 lead-lag，null result 符合 Truong & Truong 一阶相变理论——是有意义的发现，不是实验失败。重启只会浪费更多\\n    GPU 时间。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 17:37 UTC\\n  summary: 论文 framing 采用 \\\"delineating predictability boundaries\\\" 而非 \\\"universal canary\\\"\\n  rationale: 2-seed 预分析显示 canary 仅 lead diversity (distinct_n) 不 lead perplexity。ECE→perplexity\\n    甚至反向 (lag=+5)。\\\"predictability boundary\\\" framing 将 null result 转化为 evidence：100%\\n    SC 是同步崩溃 regime（不可预测），较低 α 可能出现渐进退化（可预测）。此 framing 对 null result 天然鲁棒，与 Truong\\n    & Truong 相变理论自然对接，reviewer 攻击面最小。Reviewer 独立预审认同此方向为最强 framing。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: canary→distinct_n SIGNIFICANT, canary→perplexity NO LEAD\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: same pattern confirmed\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-14 17:37 UTC\\n  summary: Post-MVP 实验优先级：α-sweep >> 方法 ablation > C4 数据集 > 规模验证\\n  rationale: α-sweep (25/50/75%) 是唯一能回答\\\"canary 在温和 regime 下是否 lead perplexity\\\"的实验，决定论文从\\n    diversity-only predictor 到 regime-dependent general predictor 的 claim 升级。方法 ablation\\n    零 GPU 成本、高 ROI（回答 reviewer 方法论质疑）。C4 堵 domain-specific 攻击。规模验证优先级最低（Pythia 家族共享架构，只测一个维度）。Reviewer\\n    预审排序一致。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-14 17:37 UTC\\n  summary: distinct_3 lead-lag 结果待 4-seed 确认，如 lag 仍双峰则降级 inconclusive，主文只报 distinct_1/distinct_2\\n  rationale: distinct_3 的 lag 估计跨 seed 不稳定（lag=-5 vs lag=-1，lag_std=2.0）。lag=-5 触及\\n    max_lag 边界，N=11 下只剩 6 点做相关，统计意义极弱，可能是边界效应伪信号。distinct_1/distinct_2 的 lag 跨 seed\\n    完全一致（lag_std=0），足以支撑核心 claim。Reviewer 建议 distinct_3 放 supplementary 并注明不稳定性。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: distinct_3 lag=-5\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: distinct_3 lag=-1\\n  depends_on:\\n  - D006\\n- id: D009\\n  date: 2026-05-14 18:59 UTC\\n  summary: MVP 4-seed STRONG PASS，进入 Research 阶段全面实验\\n  rationale: 4/4 seed 一致确认 token_entropy 和 ECE 领先 diversity 指标 1-2 代（p<0.004）。核心发现：canary\\n    只领先 diversity collapse 不领先 perplexity degradation，这定义了 narrative 方向。plan_006 升级\\n    P0 以解决 max_lag 截断疑虑。\\n  related_experiments:\\n  - exp_id: mvp_v4_rep42\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep43\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep44\\n    role: evidence\\n    result: success\\n  - exp_id: mvp_v4_rep45\\n    role: evidence\\n    result: success\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 19:10 UTC\\n  summary: plan_003 重分析修正 perplexity 通道叙述：WEAK LEAD 非断裂，ECE 反向因果，维持 D008 distinct_3\\n    降级\\n  rationale: max_lag=7 重分析三个关键发现：(1) token_entropy→perplexity lag=-5 是真实峰值非截断伪影，但\\n    p=0.058-0.12 在 N=11 下不显著——\\\"通道断裂\\\"改为\\\"弱信号、效力不足\\\"；(2) ECE→perplexity 呈反向因果(lag=+4/+5,\\n    p<0.01)，两个 canary 家族在 perplexity 通道方向相反，论文必须讨论；(3) distinct_3 虽升 SIGNIFICANT 但\\n    lag_std>1.5（双峰），维持 D008 降级。plan_006(20-gen, N=21) 成为 framing 关键判定实验。\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: evidence\\n    result: max_lag=7 重分析完成，核心 lead 稳固，perplexity 通道发现新细节\\n  depends_on:\\n  - D008\\n  - D009\\n\", \"total_chars\": 4841, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "948c60e1-43ea-4ca2-92e7-25e6eeaf21f7",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "878cc795-8537-442a-89a0-14283ad3a0bd",
  "sourceToolAssistantUUID": "948c60e1-43ea-4ca2-92e7-25e6eeaf21f7",
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

_source line 24 · 2026-05-14T19:22:17.298Z_

Now let me look at the artifacts directory for any paper drafts or experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "878cc795-8537-442a-89a0-14283ad3a0bd",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31GNVysBUtEHYwR4hTE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d37fd9d-048a-4814-a0ee-f77a386cfb94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTNrhZTF4HhUo3iLRqKTWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5398,
      "cache_read_input_tokens": 35614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5398,
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

_source line 25 · 2026-05-14T19:22:19.714Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Ht8avXrKX8nJrQfGb67x5H`</summary>

```json
{
  "pattern": "**/*.{tex,pdf,py}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d37fd9d-048a-4814-a0ee-f77a386cfb94",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31GNVysBUtEHYwR4hTE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86647cce-2301-4222-96b3-530a34354541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTNrhZTF4HhUo3iLRqKTWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5398,
      "cache_read_input_tokens": 35614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5398,
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

_source line 26 · 2026-05-14T19:22:19.727Z_

<details><summary>↩ Tool result · `toolu_01Ht8avXrKX8nJrQfGb67x5H`</summary>

```text
artifacts/_project/intermediate/iterative_train.py
artifacts/prepare_data.py
artifacts/metrics.py
artifacts/analyze_mvp.py
artifacts/iterative_train.py
artifacts/test_alpha_sweep.py
artifacts/dream_reports/dream_20260514T184925/best/paper.tex
artifacts/dream_reports/dream_20260514T184925/best/paper.pdf
artifacts/dream_reports/dream_20260514T184925/median/paper.tex
artifacts/dream_reports/dream_20260514T184925/median/paper.pdf
artifacts/dream_reports/dream_20260514T184925/worst/paper.tex
artifacts/dream_reports/dream_20260514T184925/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86647cce-2301-4222-96b3-530a34354541",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "da76849c-a064-43e9-b5cb-5e2af8ff5ae0",
  "sourceToolAssistantUUID": "86647cce-2301-4222-96b3-530a34354541",
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

_source line 27 · 2026-05-14T19:22:19.927Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017hq5WcammpfS66KvVTQn6P`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da76849c-a064-43e9-b5cb-5e2af8ff5ae0",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31GNVysBUtEHYwR4hTE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc248054-6325-4e9e-8946-983e17f059ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTNrhZTF4HhUo3iLRqKTWa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5398,
      "cache_read_input_tokens": 35614,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5398
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 35614,
          "cache_creation_input_tokens": 5398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5398,
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

_source line 28 · 2026-05-14T19:22:19.936Z_

<details><summary>↩ Tool result · `toolu_017hq5WcammpfS66KvVTQn6P`</summary>

```text
artifacts/_project/intermediate/iterative_train.py
artifacts/run_mvp.sh
artifacts/literature_map.yaml
artifacts/prepare_data.py
artifacts/metrics.py
artifacts/_project/intermediate/check_progress.sh
artifacts/check_progress.sh
artifacts/mvp_evaluation_criteria.md
artifacts/analyze_mvp.py
artifacts/literature_scan_20260514.md
artifacts/_project/report/mvp_4seed_verdict.md
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260514T184925/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T184925/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T184925/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T184925/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T184925/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T184925/best/experiment_data.json
artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md
artifacts/ccf_maxlag7_report.md
artifacts/iterative_train.py
artifacts/test_alpha_sweep.py
artifacts/dream_reports/dream_20260514T184925/best/paper.tex
artifacts/dream_reports/dream_20260514T184925/best/paper.aux
artifacts/dream_reports/dream_20260514T184925/best/paper.out
artifacts/dream_reports/dream_20260514T184925/best/paper.pdf
artifacts/dream_reports/dream_20260514T184925/best/paper.log
artifacts/dream_reports/dream_20260514T184925/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T184925/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T184925/median/experiment_data.json
artifacts/dream_reports/dream_20260514T184925/median/paper_framing.md
artifacts/dream_reports/dream_20260514T184925/median/paper.tex
artifacts/dream_reports/dream_20260514T184925/median/paper.aux
artifacts/dream_reports/dream_20260514T184925/median/paper.out
artifacts/dream_reports/dream_20260514T184925/median/paper.pdf
artifacts/dream_reports/dream_20260514T184925/median/paper.log
artifacts/dream_reports/dream_20260514T184925/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T184925/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T184925/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T184925/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T184925/worst/paper.tex
artifacts/dream_reports/dream_20260514T184925/worst/paper.aux
artifacts/dream_reports/dream_20260514T184925/worst/paper.out
artifacts/dream_reports/dream_20260514T184925/worst/paper.pdf
artifacts/dream_reports/dream_20260514T184925/worst/paper.log
artifacts/dream_reports/dream_20260514T184925/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T184925/best/review_context.yaml
artifacts/dream_reports/dream_20260514T184925/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T184925/best/review_report.md
artifacts/dream_reports/dream_20260514T184925/logs/review_best.log
artifacts/dream_reports/dream_20260514T184925/median/review_context.yaml
artifacts/dream_reports/dream_20260514T184925/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc248054-6325-4e9e-8946-983e17f059ee",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "a2bd3614-cc01-4a52-ba7c-cfa0b4ec7d51",
  "sourceToolAssistantUUID": "bc248054-6325-4e9e-8946-983e17f059ee",
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

_source line 29 · 2026-05-14T19:22:30.001Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Uy7XvbVLYQbvmSJGWVig2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2bd3614-cc01-4a52-ba7c-cfa0b4ec7d51",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31GmpBs6pUb5H726cng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cca48aa-6138-420b-ae39-ea10e11a9e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159aMajW6CwGFfCBQp864Kj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1441,
      "cache_read_input_tokens": 41012,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1441
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 41012,
          "cache_creation_input_tokens": 1441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1441,
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

_source line 30 · 2026-05-14T19:22:30.011Z_

<details><summary>↩ Tool result · `toolu_012Uy7XvbVLYQbvmSJGWVig2`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cca48aa-6138-420b-ae39-ea10e11a9e2c",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "88b68873-8917-4763-97a4-29a41bc2468d",
  "sourceToolAssistantUUID": "5cca48aa-6138-420b-ae39-ea10e11a9e2c",
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

_source line 31 · 2026-05-14T19:22:34.508Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DB9sbu8iHDQY9hRxfwdmGe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper.tex",
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88b68873-8917-4763-97a4-29a41bc2468d",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31HWqp5Jemp54yKiEgV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f4698f9-e52e-4a9d-a517-9d64b979918e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTDyXQoMjXbSPqmRmViPor",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7890,
      "cache_read_input_tokens": 42453,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7890
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 42453,
          "cache_creation_input_tokens": 7890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7890,
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

_source line 32 · 2026-05-14T19:22:34.517Z_

<details><summary>↩ Tool result · `toolu_01DB9sbu8iHDQY9hRxfwdmGe`</summary>

```text
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
  "parentUuid": "8f4698f9-e52e-4a9d-a517-9d64b979918e",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "60a2a0e1-f3ec-4154-881e-b9e8b1021931",
  "sourceToolAssistantUUID": "8f4698f9-e52e-4a9d-a517-9d64b979918e",
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

_source line 33 · 2026-05-14T19:22:39.400Z_

Now let me also read the review report that was already generated to see the existing review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60a2a0e1-f3ec-4154-881e-b9e8b1021931",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31Hr6CGyx2uyocEb3Ms",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51843fdc-b344-46b6-8270-35b7d19291cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeGuMnyDfAs7s8teSRpWae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2416,
      "cache_read_input_tokens": 50343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2416,
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

_source line 34 · 2026-05-14T19:22:43.638Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EmW4qt6U1YKDUPGLZKqa33`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51843fdc-b344-46b6-8270-35b7d19291cc",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31Hr6CGyx2uyocEb3Ms",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "caa93efd-d865-4bdc-b27a-8ebb322a2e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeGuMnyDfAs7s8teSRpWae",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2416,
      "cache_read_input_tokens": 50343,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2416
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 50343,
          "cache_creation_input_tokens": 2416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2416,
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

_source line 35 · 2026-05-14T19:22:43.651Z_

<details><summary>↩ Tool result · `toolu_01EmW4qt6U1YKDUPGLZKqa33`</summary>

```text
1	---
2	dream_id: dream_20260514T184925
3	tier: best
4	overall_score: weak reject
5	timestamp: 2026-05-14T19:20:17.780806+00:00
6	---
7	
8	
9	# Dream Review Report: Distributional Canary Collapse
10	
11	**Paper:** Distributional Canary Collapse: Predictability Phase Diagrams for Early Warning in Iterative Synthetic Data Training
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	**Date:** 2026-05-14
14	
15	---
16	
17	## Reviewer Assignments
18	- **R1:** Methods and Experiments
19	- **R2:** Novelty and Related Work
20	
21	---
22	
23	## R1 Review: Methods and Experiments
24	
25	### Summary
26	The paper applies Toda-Yamamoto temporal precedence testing to characterize which metrics lead model collapse in iterative self-consuming training, sweeping the synthetic mixing ratio α. Experimental coverage is comprehensive (8 experiments), but critical statistical concerns around short time series, sparse phase boundary estimation, and absent multiple-testing corrections weaken confidence in the quantitative claims.
27	
28	### Strengths
29	- **S1:** Correct identification that non-stationarity invalidates naive Pearson correlation; TY is an appropriate methodological choice.
30	- **S2:** Comprehensive experiment suite — all 8 planned experiments are present (α-sweep, cross-domain, cross-scale, extended runs, intervention, data strategy ablation, methodological ablation).
31	- **S3:** Reporting of null results (effective_rank, self_bleu fail as canaries) adds credibility and avoids cherry-picking.
32	- **S4:** The CRS intervention translates the diagnostic finding into actionable mitigation.
33	- **S5:** Extended 20-gen run and max_lag=7 robustness checks proactively address truncation-artifact concerns.
34	
35	### Weaknesses
36	- **W1 (Critical): Severely short time series for VAR fitting.** With T=10 and max_lag=7, a bivariate VAR(8) has ~34 parameters estimated from 10 observations. Effective degrees of freedom are near zero. Simulation studies typically recommend T≥50 for reliable TY inference. The paper does not discuss this fundamental limitation.
37	- **W2 (Major): No multiple comparison correction.** 104 canary→target pairs are tested at p<0.05. With ~62 truly null pairs, ~3 false positives are expected. Key marginal results (ECE→ppl at α=0.50, p=0.032; entropy→ppl at α=0.50, p=0.041) might not survive Bonferroni or BH correction.
38	- **W3 (Major): Phase boundary α\*≈0.60 from 4 data points.** The boundary is interpolated between α=0.50 (significant) and α=0.75 (not significant), yielding a range [0.50, 0.75], not a precise value. No uncertainty interval or confidence region is provided.
39	- **W4 (Moderate): 3 seeds is marginal.** "3/3 seeds consistent" sounds robust but carries limited statistical weight (n=3 gives only 87.5% power to detect a 95%-true positive rate).
40	- **W5 (Moderate): 2σ onset definition is fragile.** std(m_0) estimated from 3 initializations is highly noisy. No sensitivity analysis on threshold choice (1.5σ, 3σ) is provided.
41	- **W6 (Major): No figures.** The design planned 8+ figures including the actual phase diagram, trajectory panels, and scatter plots. A paper centered on a "phase diagram" that lacks the diagram is critically incomplete.
42	- **W7 (Minor): 1-epoch fine-tuning confound.** The degree of optimization per generation affects drift rate. Sensitivity to training duration is not explored.
43	- **W8 (Minor): 50k tokens per generation.** No analysis of metric estimation variance from sampling noise.
44	
45	### Detailed Scores
46	| Aspect | Score |
47	|--------|-------|
48	| Methodological Soundness | 3/6 |
49	| Experimental Rigor | 4/6 |
50	| Statistical Validity | 2/6 |
51	| Reproducibility | 4/6 |
52	| Experiment Coverage | 5/6 |
53	| Presentation Quality | 2/6 |
54	
55	### Questions for Authors
56	1. With T=10 and max_lag=7, the bivariate VAR(8) has more parameters than observations. Can you provide simulation evidence that TY testing has adequate size and power at this sample size?
57	2. Why is no multiple comparison correction applied? Would canary→perplexity results at α=0.50 (p=0.032, 0.041) survive Holm-Bonferroni correction?
58	3. How sensitive is the 2σ onset to threshold choice? How stable is it with std estimated from only 3 seeds?
59	4. Why are no figures included? The phase diagram is the paper's central concept.
60	5. Have you tested whether the panel fixed-effects assumption (common lag structure across seeds) holds?
61	
62	### R1 Overall Score: 3/6
63	### R1 Confidence: 4/5
64	
65	---
66	
67	## R2 Review: Novelty and Related Work
68	
69	### Summary
70	The paper extends Du et al.'s informal observation that ECE leads accuracy degradation into a systematic, statistically grounded study across contamination regimes. The contributions are solid but primarily incremental — formalizing and extending a known observation rather than revealing a fundamentally new phenomenon. Important related work from complex systems theory is missing.
71	
72	### Strengths
73	- **S1:** Clean problem formulation — "which metrics, how far ahead, under what conditions" — that structures a space previous work left informal.
74	- **S2:** The phase-boundary concept (predictable vs. unpredictable regimes) is a useful conceptual framework.
75	- **S3:** The 41% FP rate finding for naive correlation is independently valuable for the community.
76	- **S4:** Honest negative results (failed canaries) add depth.
77	- **S5:** The accumulate-extends-lead-time finding is a genuinely novel minor observation connecting data strategy to early-warning window.
78	
79	### Weaknesses
80	- **W1 (Major): Incremental over Du et al.** The core finding — ECE leads downstream degradation — was already observed by Du et al. This paper formalizes it with TY testing, adds token entropy, and maps regime dependence. Valuable but primarily quantitative refinement of a known qualitative observation.
81	- **W2 (Major): "Phase diagram" framing is overstatement.** In physics, phase diagrams map continuous parameter spaces with well-characterized transitions (finite-size scaling, order parameters, universality). Four α values on a single axis with a transition inferred between two points is an α-sweep with a threshold observation, not a phase diagram.
82	- **W3 (Moderate): TY is off-the-shelf, not methodological innovation.** The contribution is appropriate application, not method development. The paper should be more explicit about this.
83	- **W4 (Major): Missing critical related work.** The critical slowing down / early-warning indicators literature (Scheffer et al. 2009, 2012) from ecology and climate science is the intellectual ancestor of this work — it established frameworks for which indicators lead tipping points. Also missing: recent theoretical model collapse analyses (Seddik et al. 2024, Gerstgrasser et al. 2024, Dey et al. 2024).
84	- **W5 (Minor): CRS intervention is too simplistic** to constitute a meaningful contribution (threshold trigger → reduce α is the obvious response).
85	- **W6 (Moderate): Incomplete bibliography.** Multiple "?" citation placeholders on page 1 suggest broken references.
86	- **W7 (Moderate): Limited validation breadth.** Two models from the same family (Pythia), two English text datasets, autoregressive LMs only — insufficient for the generality claimed. The "model-intrinsic" claim (Section 5.4) is supported by one cross-domain check at a single α value.
87	
88	### Detailed Scores
89	| Aspect | Score |
90	|--------|-------|
91	| Novelty | 3/6 |
92	| Related Work Coverage | 3/6 |
93	| Positioning and Framing | 3/6 |
94	| Significance and Impact | 4/6 |
95	| Breadth of Validation | 3/6 |
96	
97	### Questions for Authors
98	1. How does this relate to the critical slowing down / early-warning indicators literature (Scheffer et al.)? Rising autocorrelation and variance as tipping-point warnings is well-established in other fields.
99	2. Would you consider renaming from "phase diagram" to "predictability sweep" or "regime analysis" to match the evidence?
100	3. Can you provide a theoretical argument for why α*≈0.60 should generalize beyond Pythia + WikiText?
101	4. What is the incremental actionable insight over Du et al.'s recommendation to monitor ECE?
102	5. Please fix the broken references ("?") on page 1.
103	
104	### Missing References
105	- Scheffer et al. (2009, 2012) — Early-warning signals for critical transitions
106	- Seddik et al. (2024) — Theoretical model collapse in Gaussian mixtures
107	- Gerstgrasser et al. (2024) — Model collapse analysis with drift characterization
108	- Dey et al. (2024) — Curse of recursion and model collapse
109	- Broader Granger causality application literature
110	
111	### R2 Overall Score: 3/6
112	### R2 Confidence: 4/5
113	
114	---
115	
116	## Roundtable Discussion
117	
118	### Step 2: Cross-Sharing
119	- **R1→R2:** R1's central concern is that TY testing on T=10 is severely underpowered (parameters ≈ observations), undermining the statistical foundation. No multiple comparison correction is applied. No figures are present.
120	- **R2→R1:** R2's central concern is incrementality over Du et al. and overstatement via the "phase diagram" framing. Important related work from complex systems theory is absent.
121	
122	### Step 3: Convergence
123	
124	**Points of Agreement:**
125	1. The research question is well-motivated and the TY methodology is appropriate in principle.
126	2. The "phase diagram" label overstates the evidence (4 α values, no uncertainty quantification).
127	3. Experimental breadth (8 experiments) is a genuine strength.
128	4. Both reviewers converge on 3/6 (Weak Reject).
129	5. Broken references and absent figures are quality concerns.
130	
131	**Synthesis of Concerns:**
132	R1 emphasizes statistical validity as the paper-killing weakness; R2 emphasizes limited novelty. After cross-sharing, both agree these compound: if the statistical evidence were unimpeachable, incremental novelty could be sufficient for a top venue. If the novelty were groundbreaking, marginal statistics could be tolerated. But weak statistics + incremental novelty together fall clearly below threshold.
133	
134	**Key Issue:** The paper's central value proposition is rigorous quantification of a qualitatively known phenomenon (ECE leads collapse). If the quantification itself is unreliable (T=10 for TY, no multiple testing correction, 3 seeds), the paper's raison d'être is undermined.
135	
136	---
137	
138	## Consolidated Assessment
139	
140	### Overall Score: 3/6 (Weak Reject)
141	
142	### Score Justification
143	The paper addresses a relevant question — predicting model collapse onset — with an appropriate statistical framework (Toda-Yamamoto) and commendable experimental breadth (8 experiments covering α, domain, scale, horizon, intervention, data strategy, methodology). The three claimed contributions (canary→diversity lead, regime-dependent perplexity predictability, naive-correlation failure) are clearly structured and mostly supported directionally.
144	
145	However, critical weaknesses prevent acceptance at a top ML venue:
146	
147	1. **Statistical foundation is unreliable.** TY testing on T=10 time series is severely underpowered — the VAR model has roughly as many parameters as observations. No multiple comparison correction is applied despite 104 hypothesis tests. The "phase boundary" α*≈0.60 is interpolated from 4 points without uncertainty quantification. These are not minor gaps; they undermine the quantitative claims that are the paper's core contribution.
148	
149	2. **Novelty is incremental.** The core observation (ECE leads downstream degradation) was already made by Du et al. The paper's added value is formalization, regime mapping, and TY methodology — valuable but primarily quantitative refinement. The "phase diagram" framing borrows prestige from statistical physics without the underlying rigor (only 4 α values, no universality analysis, no finite-size scaling analogue).
150	
151	3. **Presentation is incomplete.** No figures in a paper centered on a "phase diagram." Broken references ("?") on page 1. These suggest the paper was submitted in a draft state.
152	
153	4. **Related work has significant gaps.** The critical slowing down / tipping-point literature (Scheffer et al.) is the natural intellectual context for this work and is entirely absent. Recent theoretical model collapse analyses are also missing.
154	
155	### Actionable Recommendations for Revision
156	1. **Address statistical power:** Run simulations showing TY has adequate size/power at T=10 with your specific VAR structure, or increase to T≥20 generations for the core α-sweep (the 20-gen extension shows this is feasible).
157	2. **Apply multiple comparison correction:** At minimum BH correction within each α; report adjusted p-values.
158	3. **Finer α resolution for phase boundary:** Add α∈{0.40, 0.55, 0.60, 0.65, 0.70} to characterize α* with an uncertainty interval.
159	4. **Add figures:** The phase diagram (Fig 1 from design), trajectory panels (Fig 2), and lead-time vs α plot (Fig 3) are essential.
160	5. **Cite critical slowing down literature:** Scheffer et al. provides the intellectual framework; position this work as applying tipping-point early-warning theory to model collapse.
161	6. **Moderate the "phase diagram" framing:** Call it a "predictability regime map" or "α-dependent predictability analysis" until finer resolution justifies the phase diagram label.
162	7. **Fix broken references** and add missing citations.
163	8. **Broaden validation:** At minimum, one non-Pythia architecture (e.g., LLaMA, GPT-2) and one non-English dataset.
164	
165	### Verdict
166	The paper identifies a real phenomenon and makes useful contributions to how model collapse should be monitored and analyzed. With major revisions — particularly stronger statistical evidence, finer α resolution, proper multiple testing correction, and complete figures — this could become a solid contribution. In its current form, it falls below the acceptance threshold for a top ML venue.
167	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caa93efd-d865-4bdc-b27a-8ebb322a2e1e",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "1438cb5c-bd86-4393-b3a3-8e936e5e809b",
  "sourceToolAssistantUUID": "caa93efd-d865-4bdc-b27a-8ebb322a2e1e",
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

_source line 36 · 2026-05-14T19:22:43.730Z_

<details open><summary>🔧 Tool call — Read · `toolu_014igyCfe3p1xLbdZ8kjtvfM`</summary>

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
  "parentUuid": "1438cb5c-bd86-4393-b3a3-8e936e5e809b",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31Hr6CGyx2uyocEb3Ms",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d98f8770-0219-447b-afca-f403d4a35f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeGuMnyDfAs7s8teSRpWae",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2416,
      "cache_read_input_tokens": 50343,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2416
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 50343,
          "cache_creation_input_tokens": 2416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2416,
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

_source line 37 · 2026-05-14T19:22:43.738Z_

<details><summary>↩ Tool result · `toolu_014igyCfe3p1xLbdZ8kjtvfM`</summary>

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
  "parentUuid": "d98f8770-0219-447b-afca-f403d4a35f40",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "2ec28809-11b3-4fe5-b219-2127aba5db16",
  "sourceToolAssistantUUID": "d98f8770-0219-447b-afca-f403d4a35f40",
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

_source line 38 · 2026-05-14T19:22:48.788Z_

I now have a thorough understanding of the paper, its experimental design, results, literature positioning, and even the existing review. Let me also check the paper framing document mentioned as Du et al. -- this is referred to as `chen2025scales` in the literature map. Let me now produce my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ec28809-11b3-4fe5-b219-2127aba5db16",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31JXN61uMLgdSamFpub",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84ac56dd-7c05-4381-9b36-7178220682d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zmvoy67QajSzP9yqFk4fv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16348,
      "cache_read_input_tokens": 52759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16348,
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

_source line 39 · 2026-05-14T19:22:49.903Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SsLHwwsk3ADHr754TsYoHR`</summary>

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
  "parentUuid": "84ac56dd-7c05-4381-9b36-7178220682d8",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31JXN61uMLgdSamFpub",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55cda47c-2915-41db-b6d5-6d2ba1d98490",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zmvoy67QajSzP9yqFk4fv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16348,
      "cache_read_input_tokens": 52759,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16348
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 52759,
          "cache_creation_input_tokens": 16348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16348,
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

_source line 40 · 2026-05-14T19:22:49.905Z_

<details><summary>↩ Tool result · `toolu_01SsLHwwsk3ADHr754TsYoHR`</summary>

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
  "parentUuid": "55cda47c-2915-41db-b6d5-6d2ba1d98490",
  "isSidechain": true,
  "promptId": "8d57f6c0-5c37-40ab-b2ce-81fb97ce786d",
  "agentId": "aaf84bf95d906bf61",
  "type": "user",
  "uuid": "ff357520-7afe-408d-b302-7bb6bb8cc351",
  "sourceToolAssistantUUID": "55cda47c-2915-41db-b6d5-6d2ba1d98490",
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

_source line 41 · 2026-05-14T19:24:10.026Z_



Now I have thoroughly reviewed the paper content, the full LaTeX draft, the literature map, the project memory, the decisions log, the paper framing, and the existing R1+R2 review. Let me produce my R2 review focused on novelty and related work.

## R2: Novelty & Related Work

### Summary
The paper systematically studies which metrics can serve as early-warning "canaries" for model collapse in iterative self-consuming training, applying Toda-Yamamoto temporal precedence testing to establish lead-lag relationships across contamination regimes. The core finding -- ECE and token entropy lead diversity collapse by 1-3 generations, with a regime-dependent boundary around alpha=0.60 separating predictable from unpredictable perplexity collapse -- extends Du et al.'s (chen2025scales) informal ECE observation into a structured, multi-metric, multi-regime framework. The contribution is methodologically sound in conception but primarily incremental in novelty, formalizing and quantifying a qualitatively known phenomenon rather than uncovering a fundamentally new one.

### Strengths
- S1: **Well-structured research question.** The three-part question -- "which metrics, how far ahead, under what conditions" -- imposes a clean organizational framework on a space that prior work left informal. This decomposition is itself a conceptual contribution that future work can build on.
- S2: **The 41% false-positive finding is independently valuable.** Demonstrating that naive Pearson correlation produces ~41% spurious significant associations on non-stationary training trajectories is a broadly useful methodological warning for the ML monitoring community, independent of the specific canary results. The breakdown into three failure modes (shared trends, synchronous collapse, reverse direction) is instructive.
- S3: **Honest reporting of negative results.** Full reporting of effective rank and self-BLEU failures as canaries, and the ECE-perplexity reverse-causality finding, adds substantial credibility. Many papers in this space would cherry-pick the positive results.
- S4: **Accumulate-extends-lead-time is a genuinely novel minor finding.** The observation that data accumulation strategy not only slows collapse (known from Fu et al.) but also widens the canary lead window is new and practically relevant, connecting data engineering decisions to monitoring effectiveness.
- S5: **Regime-dependent framing turns null results into evidence.** The "predictability boundary" framing is intellectually honest -- the failure of canaries to lead perplexity at high alpha is presented as a mapped boundary rather than hidden. This is a mature scientific approach.

### Weaknesses
- W1: **(Major) Incremental over Du et al. (chen2025scales).** The headline finding -- ECE leads downstream degradation in iterative synthetic training -- was already reported by Du et al., who observed ECE rising 75% at iteration 1 with 30% synthetic data while accuracy remained stable. This paper adds: (a) formal TY testing instead of informal observation, (b) token entropy as a second canary family, (c) regime dependence across alpha values, and (d) multi-metric panel comparison. These are valuable extensions, but they quantitatively refine a known qualitative observation rather than reveal a new phenomenon. The paper's framing of the gap vis-a-vis Du et al. -- "no formal test, no multi-family comparison, no regime characterization" -- is accurate but the distance between "informal observation" and "formal TY test on the same phenomenon" is narrower than the paper implies.
- W2: **(Major) "Phase diagram" framing is a significant overstatement.** In condensed matter physics, a phase diagram maps continuous parameter spaces with rigorously characterized transitions involving order parameters, critical exponents, universality classes, and finite-size scaling. This paper has 4 discrete alpha values on a single axis, with a "boundary" interpolated between alpha=0.50 (significant) and alpha=0.75 (not significant). This is an alpha-sweep with a threshold observation, not a phase diagram. The precision claim of "alpha* approximately 0.60" is unjustified -- the data supports only "somewhere in [0.50, 0.75]" with no uncertainty quantification. The term borrows prestige from statistical physics without the underlying rigor. "Predictability regime map" or "regime-dependent analysis" would be honest descriptors.
- W3: **(Major) Critical missing related work: tipping-point early-warning theory.** The intellectual ancestor of this work is the critical slowing down / early-warning indicators literature from ecology and complex systems (Scheffer et al., "Early-warning signals for critical transitions," Nature 2009; Scheffer et al., "Anticipating Critical Transitions," Science 2012). That body of work established decades ago that rising autocorrelation and variance precede tipping points, and mapped conditions under which such early warnings succeed or fail. The paper's central question -- "under what conditions do early-warning indicators work?" -- is precisely the question Scheffer et al. addressed for ecological and climate systems. Not citing this literature is a major gap that makes the paper appear less aware of its intellectual context than it should be.
- W4: **(Moderate) Toda-Yamamoto is off-the-shelf application, not methodological innovation.** The paper lists the TY procedure as a "methodological contribution" (Contribution 3). TY is a well-established econometric technique from 1995. Applying it appropriately to a new domain is good practice, but calling it a contribution overstates the case. The real contribution is the empirical finding that naive methods fail 41% of the time in this setting, not the method itself. The paper should be explicit that the contribution is appropriate application and empirical validation, not method development.
- W5: **(Moderate) Narrow validation undermines generality claims.** Two models from the same family (Pythia-410M and 1.4B share architecture, tokenizer, and pretraining data distribution), two English text datasets, autoregressive LMs only. The claim that the canary mechanism is "model-intrinsic rather than data-specific" (Section 5.4) is supported by exactly one cross-domain check at a single alpha value. This is thin evidence for such a strong claim. At minimum, one architecturally distinct model (e.g., GPT-2, LLaMA) would be needed.
- W6: **(Moderate) Several missing references beyond Scheffer.** (a) Seddik et al. (2024) on theoretical model collapse in Gaussian mixtures provides relevant theoretical context for why phase boundaries might exist. (b) Gerstgrasser et al. (2024) on model collapse with accumulation strategies directly relates to the accumulate/replace ablation. (c) The Granger causality in ML literature (Tank et al., "Neural Granger Causality," IEEE TPAMI 2022; Nauta et al., "Causal Discovery with Attention-Based Convolutional Neural Networks," 2019) should be cited to position the choice of linear TY over neural alternatives. (d) Calibration drift literature outside model collapse (e.g., Ovadia et al., "Can You Trust Your Model's Uncertainty?", NeurIPS 2019) provides context for why ECE might be an early indicator.
- W7: **(Minor) CRS intervention is trivially obvious and does not constitute a meaningful contribution.** The intervention is: monitor ECE, when it crosses a threshold, reduce alpha. This is the most obvious possible response to detecting a problem. Including it as a "proof-of-concept" is fine, but the paper gives it disproportionate prominence (its own subsection, a table, a figure description, and prominence in the abstract's "77% diversity recovery" claim). The 77%/42% diversity preservation numbers are largely artifacts of the intervention mechanically shifting the training regime to a lower-alpha condition whose outcome is already known from the alpha-sweep.

### Questions for Authors
- Q1: How does the predictability boundary concept relate to the critical slowing down literature (Scheffer et al. 2009, 2012)? Those works established general conditions under which early-warning indicators succeed or fail for tipping points. Is your alpha* boundary an instance of their framework, or does it reflect a different mechanism? Positioning your work within that tradition would substantially strengthen the paper.
- Q2: What is the incremental actionable insight beyond Du et al.'s recommendation to monitor ECE? A practitioner who read Du et al. would already monitor ECE. Your paper adds the knowledge that (a) this works for diversity but not perplexity at high contamination, (b) token entropy is also useful, and (c) naive correlation is unreliable. Is the combined weight of (a)+(b)+(c) sufficient for a top-venue contribution, given that the core recommendation (monitor ECE) is unchanged?
- Q3: Can you provide any theoretical argument -- even heuristic -- for why the phase boundary should generalize beyond Pythia + WikiText? Without such an argument, the specific value alpha*=0.60 is a single-configuration empirical observation, and readers cannot judge whether it would hold for different architectures, scales, or data distributions.
- Q4: Why was TY chosen over neural Granger causality methods (Tank et al. 2022), given that the metric trajectories may exhibit nonlinear dynamics? At minimum, could you test whether a nonlinear alternative changes any conclusions?
- Q5: The paper reports "Spearman rho = 0.94" for cross-domain canary ranking agreement. How many items are in this ranking? If it is over 4-6 metric pairs, rho=0.94 with small N may not be statistically significant. Please report the p-value and N.

### Missing References / Positioning Issues
- **Scheffer et al. (2009, 2012)** -- "Early-warning signals for critical transitions" (Nature/Science). The foundational work on when early-warning indicators succeed or fail for tipping points. This is the most important missing reference; the paper's central question is a domain-specific instance of this general framework.
- **Seddik et al. (2024)** -- Theoretical model collapse analysis in Gaussian mixtures. Relevant to understanding why phase boundaries in collapse behavior might exist.
- **Gerstgrasser et al. (2024)** -- Model collapse analysis with accumulation. Directly relevant to the accumulate vs. replace ablation.
- **Ovadia et al. (2019)** -- "Can You Trust Your Model's Uncertainty?" (NeurIPS). Establishes that calibration degrades under distribution shift, providing mechanistic context for why ECE serves as an early indicator.
- **Tank et al. (2022)** -- Neural Granger Causality. Should be cited to justify the choice of linear TY over neural alternatives.
- **Dey et al. (2024)** -- "Is Model Collapse Inevitable?" Should be cited alongside Fu et al. for the accumulate vs. replace theoretical framework.
- The gap vis-a-vis Du et al. is real but overstated. The paper correctly identifies three limitations of Du et al. (no formal test, single metric pair, no regime exploration), but the first two are incremental gaps -- adding formal testing and one more metric family to a known observation. The regime exploration is the most novel aspect and should be foregrounded more strongly as the primary differentiator.
- The distinction from SIGMA is fair: SIGMA provides monitoring but no temporal lead quantification. The distinction from DCES is also fair: DCES is reactive. These are accurately represented.

### Novelty Score: 2 (incremental -- formalizes and extends a known observation with appropriate but off-the-shelf methodology)
### Significance Score: 3 (useful framework and findings for the model collapse monitoring community, though practical impact is limited by the 1-2 generation lead window and small model scale)
### Overall Score: 3 (Weak Reject)
### Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff357520-7afe-408d-b302-7bb6bb8cc351",
  "isSidechain": true,
  "agentId": "aaf84bf95d906bf61",
  "requestId": "req_011Cb31JyvG3YsLGfxnEpzQ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18e28058-885a-4f47-a6bb-47aec426fa73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "8b658381-150c-4d7a-982d-1cebf7ec2b62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4hTeb7LbYUcy4zFqvQsqi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 69107,
      "output_tokens": 2759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 733
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2759,
          "cache_read_input_tokens": 69107,
          "cache_creation_input_tokens": 733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 733,
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
