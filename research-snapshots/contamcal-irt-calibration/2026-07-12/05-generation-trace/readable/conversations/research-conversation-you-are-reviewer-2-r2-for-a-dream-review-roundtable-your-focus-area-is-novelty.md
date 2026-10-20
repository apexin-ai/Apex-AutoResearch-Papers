# Research conversation: You are Reviewer 2 (R2) for a DREAM review roundtable. Your focus area is **Novelty and Related Work**. ## Paper Details

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a1922f0e6b71081b3.jsonl`
- **Structured JSON:** [`4e0ec4190b720bda712f.json`](../../sessions/4e/4e0ec4190b720bda712f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-13T16:42:33.268Z_

You are Reviewer 2 (R2) for a DREAM review roundtable. Your focus area is **Novelty and Related Work**.

## Paper Details
Title: "Empirical Identifiability Boundaries for Contamination-Aware IRT Calibration of LLM Benchmarks"
Venue: AAAI 2027 (use AAAI-26 standards: 1–10 scale, ~17.6% acceptance rate)

## Paper Summary
The paper investigates when contamination-aware IRT calibration of LLM benchmarks is identifiable. It augments 4PL IRT with a contamination covariate γ, using 4 detection signals (Embedding Retrieval, Min-K%++, ConStat, Self-Critique) fused via RRF. Through controlled SFT injection experiments across Qwen2.5 models (0.5B–7B), 4 benchmarks (MMLU, GSM8K, ARC-C, HumanEval), and 5 dosage levels, it establishes:
1. Calibration is identifiable only when signal AUC ≥ 0.70 and N ≥ 80 (rarely met)
2. RL post-training degrades all signals below threshold (avg AUC drops from 0.72 to 0.56)
3. Identifiability degrades with model scale (larger models harder to calibrate)

Key reframing: the paper shifts from "calibration solves contamination" to "we map when calibration is solvable."

## Key Contributions Claimed
1. An empirical identifiability map (signal AUC × model count × model scale)
2. Signal survival analysis showing RL degrades all signals below threshold
3. Controlled SFT injection experiments validating simulation-predicted boundaries
4. Practical identifiability thresholds: AUC ≥ 0.70, N ≥ 80, CI width < 15pp

## Method Overview
- Stage 1: 4 detection signals → RRF fusion → exposure scores s_ij
- Stage 2: 4PL IRT augmented with γ covariate: P(Y=1|θ,γ) = c + (d-c)/(1+exp(-a(θ+γs-b)))
- Fitted via HMC in Stan with Bayesian posterior inference

## Related Work as Presented (12 references total)
- Contamination detection: Embedding retrieval [5], Min-K%++ [6], ConStat [7], Self-Critique [8]
- IRT for LLM: PS-NIRT [9], Growing Pains [10], ATLAS [11], HiBayES [12]
- Contamination mitigation: DCR [1], Emperor's New Clothes [2]
- Item compromise in educational testing: Eckerly [3], Sinharay [4]
- Three structural differences when adapting IRT item compromise to LLMs: (a) single model vs. independent examinees, (b) continuous vs. binary exposure, (c) regime-conditional ability

## Experimental Results Summary
- 4PL+γ does NOT significantly outperform linear regression (7.8 vs 7.2pp MAE, p=0.23)
- γ only identifiable at ≥50% dosage; 5-25% dosage γ CIs include zero
- γ-θ posterior correlation 0.52 (3B) to 0.58 (7B) showing ability-contamination confound
- RL-trained models: calibration HARMFUL (MAE 10.5 vs uncalibrated 9.8pp)
- 2-signal closed-weight mode: Kendall τ=0.48 (worse than random for ranking)
- Scale barrier: 72B AUC 0.60, MAE 11.2pp
- Prior sensitivity: 30% variation, indicating under-identification

## Your Task
Write a detailed review focused on:
1. Novelty assessment — Is the framing genuinely new? Are the contributions incremental or significant?
2. Related work completeness — Are key references missing? Is positioning accurate?
3. Significance and impact — Will this change how the community thinks about contamination calibration?
4. Conceptual clarity and narrative — Is the "identifiability boundary" story well-told?

Provide:
- 3-5 strengths (specific, with evidence)
- 3-5 weaknesses (specific, with evidence, constructive)
- Missing related work (specific papers/areas)
- Questions for authors
- Scores (1-10 AAAI scale): Novelty, Significance, Related Work, Clarity, Overall Assessment, Confidence (1-5)

Be rigorous but fair. Score honestly for an AAAI submission at 17.6% acceptance rate. The paper has 12 references total — assess whether this is sufficient.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "4c5725eb-293e-4713-b95f-cea34ac02063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T16:42:33.277Z_

```json
{
  "parentUuid": "4c5725eb-293e-4713-b95f-cea34ac02063",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
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
  "uuid": "932cdbd3-58e9-493d-b23e-72d6303f2138",
  "timestamp": "2026-05-13T16:42:33.277Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T16:42:36.675Z_



I'll start by loading the project overview and reading the key project files to ground my review in the actual paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "932cdbd3-58e9-493d-b23e-72d6303f2138",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHBWkry7vhx75YrMbu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5b74607-64ea-427f-bbd1-3eeebe9403b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvNTb43ZRJsVoyoWzpoxw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7008,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7008,
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

_source line 4 · 2026-05-13T16:42:38.352Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015ykmgavqguQsPeD4PZjNdK`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5b74607-64ea-427f-bbd1-3eeebe9403b2",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHBWkry7vhx75YrMbu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78366945-d2fe-4a87-a10c-733a648054b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvNTb43ZRJsVoyoWzpoxw2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7008,
      "cache_read_input_tokens": 8253,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 147,
          "cache_read_input_tokens": 8253,
          "cache_creation_input_tokens": 7008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7008,
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

_source line 5 · 2026-05-13T16:42:38.359Z_

<details><summary>↩ Tool result · `toolu_015ykmgavqguQsPeD4PZjNdK`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

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
  "parentUuid": "78366945-d2fe-4a87-a10c-733a648054b5",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "fe97601e-5718-4b5b-b540-8e5fdc7c573a",
  "sourceToolAssistantUUID": "78366945-d2fe-4a87-a10c-733a648054b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T16:42:41.742Z_



Let me read the project files to get full context for the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe97601e-5718-4b5b-b540-8e5fdc7c573a",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHZfmKPnMPZehQXyWU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09a80bb1-7fdd-4fe1-968e-16d724495b79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8gA37bUP9ZTcB2iYsFRsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 15261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2021,
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

_source line 7 · 2026-05-13T16:42:42.228Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_011iQ3GpnHoXj8oLmEmg1Mcd`</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a80bb1-7fdd-4fe1-968e-16d724495b79",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHZfmKPnMPZehQXyWU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "302c9c30-b072-499e-ad02-33c33324f19c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8gA37bUP9ZTcB2iYsFRsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 15261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2021,
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

_source line 8 · 2026-05-13T16:42:42.277Z_

<details><summary>↩ Tool result · `toolu_011iQ3GpnHoXj8oLmEmg1Mcd`</summary>

```text
{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (2 个)\n\n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_sim_confounding** (success): 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\n- **mvp_sim_4pl_gamma** (success): 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\n\n## 趋势\n成功 2 / 负向 0 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\n（无服务器配置）\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "302c9c30-b072-499e-ad02-33c33324f19c",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "e0d22e0f-e65e-4ece-8eb0-573939d6f5e0",
  "sourceToolAssistantUUID": "302c9c30-b072-499e-ad02-33c33324f19c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T16:42:43.237Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019sBzydpguANjLTuo7ZXXtq`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0d22e0f-e65e-4ece-8eb0-573939d6f5e0",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHZfmKPnMPZehQXyWU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1de973ba-15b2-422b-bc30-7aee6bdfee1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8gA37bUP9ZTcB2iYsFRsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 15261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2021,
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

_source line 10 · 2026-05-13T16:42:43.272Z_

<details><summary>↩ Tool result · `toolu_019sBzydpguANjLTuo7ZXXtq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_sim_confounding** (success): 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\\n- **mvp_sim_4pl_gamma** (success): 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 570, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1de973ba-15b2-422b-bc30-7aee6bdfee1f",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "74d52f06-c1bb-40d8-ac26-203f41e66752",
  "sourceToolAssistantUUID": "1de973ba-15b2-422b-bc30-7aee6bdfee1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T16:42:43.933Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01K7u6U5L3PaWzSVXbmAkq2u`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74d52f06-c1bb-40d8-ac26-203f41e66752",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHZfmKPnMPZehQXyWU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c38322c3-6d25-4aff-827a-ac8598fad867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8gA37bUP9ZTcB2iYsFRsz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 15261,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2021
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 278,
          "cache_read_input_tokens": 15261,
          "cache_creation_input_tokens": 2021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2021,
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

_source line 12 · 2026-05-13T16:42:43.970Z_

<details><summary>↩ Tool result · `toolu_01K7u6U5L3PaWzSVXbmAkq2u`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c38322c3-6d25-4aff-827a-ac8598fad867",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "9d7afc09-9bb0-43df-90f2-2977eba8dd04",
  "sourceToolAssistantUUID": "c38322c3-6d25-4aff-827a-ac8598fad867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T16:42:48.465Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YYDPaZrgPu7PtneHb5HaJd`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d7afc09-9bb0-43df-90f2-2977eba8dd04",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHyJpTpWiWY48KMWfK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7d11e50-cbb9-48e5-8d36-4afc3493ced8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012p7VMPeJ6noKrDvjxtSqxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 17282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1253,
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

_source line 14 · 2026-05-13T16:42:48.508Z_

<details><summary>↩ Tool result · `toolu_01YYDPaZrgPu7PtneHb5HaJd`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7d11e50-cbb9-48e5-8d36-4afc3493ced8",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "15b6f0e2-90c5-4f27-997e-15ee39f88e55",
  "sourceToolAssistantUUID": "a7d11e50-cbb9-48e5-8d36-4afc3493ced8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T16:42:48.774Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014SQgBJoyqjdYpaup3W3u8a`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15b6f0e2-90c5-4f27-997e-15ee39f88e55",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHyJpTpWiWY48KMWfK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b46eabb2-eee7-48fa-8f6c-e6fcc3ca2248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012p7VMPeJ6noKrDvjxtSqxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 17282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1253,
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

_source line 16 · 2026-05-13T16:42:48.813Z_

<details><summary>↩ Tool result · `toolu_014SQgBJoyqjdYpaup3W3u8a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)\\n- Secondary: ICLR 2027 (expected deadline: Sep 2026)\\n- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)\\n\\n## Core Insight\\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017), with 3 non-trivial adaptations for LLM evaluation.\\n\\n## Core Claims (3 条)\\n\\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model recovers true (uncontaminated) benchmark performance with low calibration error (MAE) and nominal credible interval coverage, validated on controlled SFT contamination injection experiments across 3+ model scales (0.5B-7B) and 4 benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval).\\n\\n2. **Signal Aggregation Claim**: Training-free RRF fusion of 4 complementary detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique) provides principled contamination exposure estimation without meta-circularity, outperforming any single signal and degrading gracefully under signal dropout — including a degraded 2-signal mode for closed-weight models.\\n\\n3. **Uncertainty Quantification Claim**: ContamCal explicitly propagates detection signal noise into calibration uncertainty — SFT-trained models receive tighter credible intervals (multiple reliable signals), RL-trained models receive appropriately wider intervals (primarily Self-Critique), and simulation-validated identifiability bounds establish minimum signal quality thresholds for reliable calibration.\\n\\n## Contributions (Hierarchical)\\n\\n### Core\\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT) producing calibrated scores with credible intervals\\n2. Dual-track validation: controlled SFT injection (internal validity) + ecological RL case study (external validity)\\n3. 5 baselines + 5 quantitative evaluation metrics for contamination-aware calibration\\n\\n### Supporting\\n4. Simulation-based identifiability study: systematic parameter sweep establishing minimum signal quality / model count thresholds\\n5. Signal survival analysis: systematic evaluation of which detection signals remain reliable after SFT vs. RL post-training (signal × regime AUC heatmap)\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration as the principled alternative.\\n- **Our framing**: ContamCal is a \\\"statistical safety net\\\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. This is grounded in educational measurement's item compromise IRT tradition, with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics), (b) binary leakage → continuous exposure scores (requires generalization), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware modeling).\\n- **Headline result template**: \\\"On {benchmark}, ContamCal recovers true model performance within {X}% MAE with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage. Even under noisy RL-regime detection (Self-Critique AUC ~0.65), calibrated scores with wider CIs improve model selection decisions by {R}% expected regret reduction.\\\"\\n\\n## Venue Fit Risks\\n- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.\\n- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing (\\\"wide CIs are the correct answer, not a limitation\\\").\\n- **Novelty ceiling**: Core method is synthesis of existing components (detection signals + IRT). Defense: cross-disciplinary transfer with 3 non-trivial adaptations + simulation-validated identifiability bounds as methodological contribution. Not \\\"engineering glue\\\" — each adaptation requires non-obvious modeling decisions.\\n- **RL \\\"so what\\\"**: RL models only get wide CIs. Defense: expected regret quantification shows even wide CIs improve model selection vs. naive scores.\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | MVP validated: γ rel_bias <8%, θ_residual_exp_corr=0.058 at corr=0.38 | exp-004 (sweep) |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated | exp-003 (ablation) |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity) | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d parameters necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (50)? | Few-examinee regime study + Growing Pains pre-estimation strategy | exp-011 |\\n| 7 | Noisy exposure scores | Noise propagation analysis: calibrated noise injection → CI widening quantified | exp-005 |\\n| 8 | No baselines | 7 baselines: Raw anchor, remove-rescore, single-signal 2PL+γ, vanilla 4PL, linear regression+CI, Emperor's mitigations, DCR (EMNLP 2025) | exp-006 |\\n\\n## Evaluation Protocol (5 Metrics)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n\\n## Benchmarks (4)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\\n3. **ARC-Challenge** — science reasoning multiple-choice\\n4. **HumanEval** — code generation with execution evaluation\\n- Day-8 contingency: reduce to MMLU + GSM8K\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\", \"total_chars\": 8347, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b46eabb2-eee7-48fa-8f6c-e6fcc3ca2248",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "7795fc8d-d1f9-47c9-917f-64c9f5211d5d",
  "sourceToolAssistantUUID": "b46eabb2-eee7-48fa-8f6c-e6fcc3ca2248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T16:42:49.687Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CpVU2nmPS7UzHZ3b7SELAq`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7795fc8d-d1f9-47c9-917f-64c9f5211d5d",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHyJpTpWiWY48KMWfK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fef5e3e3-789b-4d1c-a5fc-dd488ed63e61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012p7VMPeJ6noKrDvjxtSqxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 17282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1253,
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

_source line 18 · 2026-05-13T16:42:49.724Z_

<details><summary>↩ Tool result · `toolu_01CpVU2nmPS7UzHZ3b7SELAq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-13 15:51 UTC | 更新原因: MVP 完成，进入 Research 阶段，完成 paper_framing + experiment_plan + dream_simulate\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration for contamination-adjusted benchmark scores。两阶段：(1) RRF 融合 4 检测信号得到 per-item contamination exposure，(2) contamination-augmented 4PL IRT 输出校准分数 + credible intervals。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）\\n- **MVP 结论**: 4PL+γ IRT 在合成数据上成功分离 γ 和 θ（γ rel_bias <8%, θ_corr >0.94, confounding 分离后残差相关 0.058）\\n- **关键发现**: 4PL 必要（2PL 结构性劣势）；NUTS 唯一可用推断方法（ADVI 废弃）；N_items≥300 必要\\n- **Dream**: dream_20260513T155040 进行中（full review mode）\\n- **GPU**: 待分配，已向 Manager 申请\\n- **实验计划**: 13 个实验（6 P0 + 5 P1 + 2 P2），详见 experiment_plan.yaml\\n\\n## 近期任务\\n- [ ] 等待 Dream 完成 → 分析审稿反馈 → 调整 framing/plan\\n- [ ] GPU 分配到位后启动 exp-001 (controlled SFT injection)\\n- [ ] 并行启动 exp-004 (simulation sweep, CPU only)\\n- [ ] exp-004 完成后启动 exp-005 (noise propagation, CPU only)\\n\\n## GPU 预算\\n- P0: 72h | P1: 57h | P2: 20h | Buffer: 30h | Total: ~179h\\n- 需要 2-4× H100/A100-80G\\n- 预估 wall-clock: 2-4 周取决于 GPU 数量\\n\\n## 投稿目标\\n- Primary: AAAI 2027（Jul-Aug 2026 deadline）\\n- Secondary: ICLR 2027（Sep 2026 deadline）\\n\\n## Core Claims (paper_framing.md)\\n1. **Calibration**: 4PL+γ IRT recovers true scores with low MAE + nominal CI coverage\\n2. **Signal Aggregation**: RRF fusion of 4 signals, training-free, graceful degradation\\n3. **Uncertainty Quantification**: Noise propagation + regime-appropriate CI widths\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-13 | MVP 通过，进入 Research 阶段 | mvp_sim_4pl_gamma, mvp_sim_confounding |\\n| D003 | 2026-05-13 | Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMS | mvp_sim_4pl_gamma |\\n| D002 | 2026-05-13 | 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-e | — |\\n| D001 | 2026-05-13 | MVP 用 simulation identifiability test 验证 4PL+γ IRT | — |\\n\\n\\n\", \"total_chars\": 1898, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fef5e3e3-789b-4d1c-a5fc-dd488ed63e61",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "b2a60212-375a-479c-a89e-779b2e57a454",
  "sourceToolAssistantUUID": "fef5e3e3-789b-4d1c-a5fc-dd488ed63e61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T16:42:50.096Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ThbNnHd8W9VjTNbSiVMDsb`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2a60212-375a-479c-a89e-779b2e57a454",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuHyJpTpWiWY48KMWfK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32aa3887-efbd-403e-87b7-a69e3fb1c5b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012p7VMPeJ6noKrDvjxtSqxU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 17282,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1253
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 394,
          "cache_read_input_tokens": 17282,
          "cache_creation_input_tokens": 1253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1253,
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

_source line 20 · 2026-05-13T16:42:50.128Z_

<details><summary>↩ Tool result · `toolu_01ThbNnHd8W9VjTNbSiVMDsb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No memory.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32aa3887-efbd-403e-87b7-a69e3fb1c5b1",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "9367e2e2-8d35-4a9f-a012-2289877908ec",
  "sourceToolAssistantUUID": "32aa3887-efbd-403e-87b7-a69e3fb1c5b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T16:42:53.410Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HsZzMk1TT7W96d1s53iQ2d`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9367e2e2-8d35-4a9f-a012-2289877908ec",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuJReqqAQw1mqumoMRc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f583ebf9-66b4-4de4-841c-25234f99a3d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017N1DVKTUKVpg3u1CCSjmN5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4341,
      "cache_read_input_tokens": 18535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4341,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 22 · 2026-05-13T16:42:53.455Z_

<details><summary>↩ Tool result · `toolu_01HsZzMk1TT7W96d1s53iQ2d`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f583ebf9-66b4-4de4-841c-25234f99a3d6",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "0d334473-eb65-4792-8864-323356b31e94",
  "sourceToolAssistantUUID": "f583ebf9-66b4-4de4-841c-25234f99a3d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T16:42:53.699Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AY7yavyZFuM8JT3JxZgUXF`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d334473-eb65-4792-8864-323356b31e94",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuJReqqAQw1mqumoMRc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35ee30e3-eb49-41d7-ad3f-e5c1ea446805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017N1DVKTUKVpg3u1CCSjmN5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4341,
      "cache_read_input_tokens": 18535,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4341
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 18535,
          "cache_creation_input_tokens": 4341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4341,
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

_source line 24 · 2026-05-13T16:42:53.719Z_

<details><summary>↩ Tool result · `toolu_01AY7yavyZFuM8JT3JxZgUXF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\\n    role: P2 confounding robustness\\n    result: PASS with confound_corr=0.38\\n  depends_on:\\n  - D002\\n  - D003\\n\", \"total_chars\": 1844, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35ee30e3-eb49-41d7-ad3f-e5c1ea446805",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "f294f0f2-db75-40ed-a4c8-16a579db1ebf",
  "sourceToolAssistantUUID": "35ee30e3-eb49-41d7-ad3f-e5c1ea446805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T16:42:56.843Z_

Now let me look at the artifacts and any experiment results for deeper understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f294f0f2-db75-40ed-a4c8-16a579db1ebf",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuJh4HmtpZnmWWk2Nku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad4a7ddc-f100-43b9-8b20-2fcda0fe9af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015u6CZuNaMnUk5JsXEP6hA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 22876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1552,
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

_source line 26 · 2026-05-13T16:42:59.261Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015gL4fwELeJidg13fiwVmQ1`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad4a7ddc-f100-43b9-8b20-2fcda0fe9af6",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuJh4HmtpZnmWWk2Nku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52a887a1-4169-4f95-97db-ff66482fdeee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015u6CZuNaMnUk5JsXEP6hA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 22876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1552,
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

_source line 27 · 2026-05-13T16:42:59.484Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0167pvbLpuQXUWArPCjWCduh`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52a887a1-4169-4f95-97db-ff66482fdeee",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuJh4HmtpZnmWWk2Nku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc4c6094-8e82-4ed9-92cd-8dcc90cf542f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015u6CZuNaMnUk5JsXEP6hA9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 22876,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 22876,
          "cache_creation_input_tokens": 1552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1552,
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

_source line 28 · 2026-05-13T16:42:59.526Z_

<details><summary>↩ Tool result · `toolu_015gL4fwELeJidg13fiwVmQ1`</summary>

```text
artifacts/mvp_simulation/contam_irt_4pl.stan
artifacts/mvp_simulation/contam_irt_2pl.stan
artifacts/mvp_simulation/contam_irt_4pl
artifacts/mvp_simulation/contam_irt_2pl
artifacts/mvp_simulation/.venv/.gitignore
artifacts/mvp_simulation/.venv/pyvenv.cfg
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/METADATA
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/WHEEL
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/entry_points.txt
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/licenses/AUTHORS.txt
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/licenses/LICENSE.txt
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/top_level.txt
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/__main__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/__pip-runner__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/build_env.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cache.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/autocompletion.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/cmdoptions.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/main.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/main_parser.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/parser.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/progress_bars.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/cli/status_codes.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/cache.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/check.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/completion.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/debug.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/download.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/freeze.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/hash.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/help.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/index.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/inspect.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/install.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/list.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/lock.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/search.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/show.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/uninstall.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/commands/wheel.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/distributions/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/distributions/base.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/distributions/installed.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/distributions/sdist.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/distributions/wheel.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/exceptions.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/index/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/index/collector.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/index/package_finder.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/index/sources.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/locations/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/locations/_distutils.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/locations/_sysconfig.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/locations/base.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/main.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/metadata/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/metadata/_json.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/metadata/base.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_compat.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_dists.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_envs.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/metadata/pkg_resources.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/candidate.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/direct_url.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/format_control.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/index.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/installation_report.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/link.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/pylock.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/scheme.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/search_scope.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/selection_prefs.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/target_python.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/models/wheel.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/network/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/network/auth.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/network/cache.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/network/download.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/network/lazy_wheel.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/network/session.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/network/utils.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/network/xmlrpc.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/operations/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__init__.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/build_tracker.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata.py
artifacts/mvp_simulation/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_editable.py
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52a887a1-4169-4f95-97db-ff66482fdeee",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "a3730be8-8552-4c4b-992d-b5f876484205",
  "sourceToolAssistantUUID": "52a887a1-4169-4f95-97db-ff66482fdeee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T16:42:59.651Z_

<details><summary>↩ Tool result · `toolu_0167pvbLpuQXUWArPCjWCduh`</summary>

```text
decisions.yaml
artifacts/dream_reports/dream_20260513T155040/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T155040/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T155040/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260513T155040/best/review_context.yaml
registry.yaml
artifacts/dream_reports/dream_20260513T155040/median/review_context.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260513T155040/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc4c6094-8e82-4ed9-92cd-8dcc90cf542f",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "5bd07605-3e0c-44a9-9113-35d50d902d87",
  "sourceToolAssistantUUID": "cc4c6094-8e82-4ed9-92cd-8dcc90cf542f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-13T16:43:02.372Z_

Let me read the experiment plan and the dream review context for deeper understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bd07605-3e0c-44a9-9113-35d50d902d87",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuK8LpPWWjR1py2pdoH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bcc7c5d-2cd1-44f1-b315-0d23d4b88313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDqDs2vZVrQhS9jjwq9wa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3548,
      "cache_read_input_tokens": 24428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3548,
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

_source line 31 · 2026-05-13T16:43:04.532Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EHRcuz5FZiHNtndRS41wM8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bcc7c5d-2cd1-44f1-b315-0d23d4b88313",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuK8LpPWWjR1py2pdoH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "392a9634-1ec3-4c84-b5ad-6f32467e5cb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDqDs2vZVrQhS9jjwq9wa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3548,
      "cache_read_input_tokens": 24428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3548,
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

_source line 32 · 2026-05-13T16:43:04.545Z_

<details><summary>↩ Tool result · `toolu_01EHRcuz5FZiHNtndRS41wM8`</summary>

```text
1	# ContamCal Experiment Plan
2	# Each experiment maps to Core Claims in paper_framing.md
3	# Priority: P0 = must-run, P1 = important, P2 = bonus
4	
5	experiments:
6	  # ============================================================
7	  # P0: Core experiments — must complete for submission
8	  # ============================================================
9	
10	  - id: exp-001
11	    name: controlled_sft_injection
12	    claim: [1]
13	    description: >
14	      SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels
15	      (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data).
16	      Produces ground-truth contaminated/clean model pairs. 15 SFT runs total
17	      (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition
18	      for key metrics (mean ± std).
19	      Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or
20	      equivalent) with controlled semantic similarity — following methodology
21	      of "Rethinking Benchmark and Contamination" (arXiv 2023). Target:
22	      high semantic similarity (cosine >0.85) but low lexical overlap
23	      (BLEU <0.3) to evade n-gram decontamination while preserving
24	      contamination effect. Quality validation: automated similarity metrics
25	      + human spot-check on 50 random pairs per benchmark.
26	    priority: P0
27	    gpu_budget_hours: 50
28	    deps: []
29	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
30	    models: [Qwen2.5-0.5B, Qwen2.5-1.5B, Qwen2.5-3B]
31	    seeds: 3
32	
33	  - id: exp-002
34	    name: stage1_signal_pipeline
35	    claim: [2]
36	    description: >
37	      Compute 4 detection signals on all contaminated + clean models from exp-001:
38	      (a) embedding-based semantic retrieval (FAISS + sentence-transformers),
39	      (b) Min-K%++ membership inference,
40	      (c) ConStat performance gap (original vs paraphrased items),
41	      (d) Self-Critique entropy collapse.
42	      Output: per-model-item exposure scores for each signal.
43	    priority: P0
44	    gpu_budget_hours: 20
45	    deps: [exp-001]
46	
47	  - id: exp-003
48	    name: rrf_aggregation_ablation
49	    claim: [2]
50	    description: >
51	      RRF fusion of 4 signals into composite per-item exposure score.
52	      Ablations: (a) RRF vs equal-weight rank averaging, (b) single-signal only
53	      (×4), (c) calibration-based weighted RRF variant, (d) false positive
54	      injection robustness check (inject FP at rates matching Duan et al. 2024).
55	      Also test degraded 2-signal mode (ConStat + Self-Critique) for closed-weight.
56	    priority: P0
57	    gpu_budget_hours: 2
58	    deps: [exp-002]
59	
60	  - id: exp-004
61	    name: simulation_identifiability_sweep
62	    claim: [1, 3]
63	    description: >
64	      Systematic synthetic-data sweep (NEW, not MVP — MVP only covered 4-5 conditions):
65	      exposure signal AUC (0.55, 0.60, 0.65, 0.70, 0.80, 0.90) ×
66	      model count (20, 50, 100, 200) ×
67	      prior strength (N(0,0.5), N(0,1), N(0,2)) ×
68	      exposure type (binary, continuous).
69	      144 conditions, 10 seeds each. Reports: θ-γ recovery RMSE, posterior
70	      correlation, coverage (50%/80%/95%), prior sensitivity. Establishes
71	      minimum AUC threshold; if 95% CI width > 15pp at AUC=0.65, label as
72	      "cannot distinguish no contamination from moderate contamination."
73	      N_items=300 fixed (per MVP finding).
74	      Subsumes exp-010 (prior sensitivity) and exp-011 (few-examinee regime)
75	      — prior × N_models dimensions already in sweep grid. Growing Pains
76	      pre-estimation sub-experiment: at N_models=20/50, compare flat prior
77	      vs informative prior from pre-estimated item parameters.
78	    priority: P0
79	    gpu_budget_hours: 0
80	    deps: []
81	    note: CPU only. MVP (mvp_sim_4pl_gamma) was preliminary; this is the full sweep.
82	
83	  - id: exp-005
84	    name: noise_propagation_analysis
85	    claim: [3]
86	    description: >
87	      Calibrated noise injection into exposure scores:
88	      (a) estimate Self-Critique per-item FP/FN rates from exp-001 ground truth,
89	      (b) inject Gaussian noise at matched level + 1.5× + 2× into exposure scores,
90	      (c) re-fit IRT, measure CI widening for γ and calibrated θ.
91	      Optional: extend Bayesian model with measurement error
92	      (exposure_ij ~ N(τ_ij, σ_e²)) for automatic noise propagation.
93	    priority: P0
94	    gpu_budget_hours: 0
95	    deps: [exp-002, exp-004]
96	    note: CPU only
97	
98	  - id: exp-006
99	    name: irt_calibration_and_baselines
100	    claim: [1, 3]
101	    description: >
102	      Fit 4PL+γ IRT (Stan NUTS) on controlled models from exp-001/003.
103	      Compute calibrated scores via exposure=0 counterfactual with CIs.
104	      Compare against 7 baselines:
105	      (0) Raw — no adjustment (anchor),
106	      (1) remove-and-rescore (drop flagged items),
107	      (2) single-signal 2PL+γ (best signal only, simpler IRT),
108	      (3) vanilla 4PL without γ (standard IRT, no contamination modeling),
109	      (4) linear exposure regression + bootstrap CI (simplest post-hoc),
110	      (5) Emperor's mitigation: rephrasing + option shuffling,
111	      (6) DCR fuzzy inference (EMNLP 2025) — the only existing method
112	          producing adjusted accuracy; must include or reviewers will reject.
113	      Evaluate all 5 metrics: MAE, coverage (50%/80%/95%), sharpness,
114	      Kendall τ, dose-response monotonicity.
115	      Report mean ± std across 3 seeds (matched to exp-001 seeds).
116	    priority: P0
117	    gpu_budget_hours: 8
118	    deps: [exp-003]
119	    benchmarks: [MMLU, GSM8K, ARC-Challenge, HumanEval]
120	    seeds: 3
121	
122	  # ============================================================
123	  # P1: Important — run if time/GPU permit
124	  # ============================================================
125	
126	  - id: exp-007
127	    name: scale_bridging_7b
128	    claim: [1]
129	    description: >
130	      Qwen2.5-7B controlled SFT injection at 5 dosage levels.
131	      Validates calibration accuracy scales to larger models.
132	      Requires multi-GPU node (7B LoRA SFT ~4-8h per run on 1×H100).
133	    priority: P1
134	    gpu_budget_hours: 30
135	    deps: [exp-001]
136	
137	  - id: exp-008
138	    name: signal_survival_analysis
139	    claim: [2]
140	    description: >
141	      Systematic evaluation of detection signal reliability across training regimes.
142	      Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated,
143	      RL-post-trained}. Confirms Self-Critique compensates where Min-K%++/ConStat
144	      degrade post-RL (per fragility paper arXiv 2510.02386).
145	      Upgraded to Supporting Contribution 5 in paper.
146	    priority: P1
147	    gpu_budget_hours: 10
148	    deps: [exp-002]
149	
150	  - id: exp-009
151	    name: rl_observational_case_study
152	    claim: [2, 3]
153	    description: >
154	      Apply Self-Critique + available signals to existing RL-trained models:
155	      Qwen2.5-Instruct (0.5B/1.5B/3B/7B), DeepSeek-R1-Distill-1.5B/7B.
156	      Fit IRT with appropriately wider CIs. Expected regret quantification:
157	      compare uncalibrated vs calibrated vs remove-rescore for top-5 model
158	      selection. Framed as observational — directional external validity,
159	      not full quantitative validation. Near-zero γ check on known-clean
160	      benchmark (specificity test).
161	    priority: P1
162	    gpu_budget_hours: 15
163	    deps: [exp-006, exp-008]
164	
165	  # exp-010 (prior_sensitivity) and exp-011 (few_examinee_regime) merged into exp-004.
166	  # Prior × N_models dimensions already covered in the sweep grid.
167	
168	  # ============================================================
169	  # P2: Bonus — adds breadth if resources allow
170	  # ============================================================
171	
172	  - id: exp-012
173	    name: observational_72b
174	    claim: [1]
175	    description: >
176	      Qwen2.5-72B observational analysis (inference only, no SFT).
177	      Extends ecological validity to frontier model scale.
178	    priority: P2
179	    gpu_budget_hours: 15
180	    deps: [exp-006]
181	
182	  - id: exp-013
183	    name: closed_weight_2signal_mode
184	    claim: [2]
185	    description: >
186	      Degraded 2-signal mode (ConStat + Self-Critique, no logits/embeddings)
187	      for closed-weight models. Ablation quantifying 2-signal vs 4-signal
188	      calibration accuracy gap.
189	    priority: P2
190	    gpu_budget_hours: 5
191	    deps: [exp-003]
192	
193	# ============================================================
194	# GPU Budget Summary
195	# ============================================================
196	gpu_budget:
197	  P0_hours: 80
198	  P1_hours: 55
199	  P2_hours: 20
200	  buffer_hours: 30
201	  total_hours: 185
202	  note: >
203	    CPU-only experiments (exp-004, exp-005, exp-011) excluded.
204	    Buffer covers reruns, debugging, multi-seed overhead, and unexpected issues.
205	    Requires 2-4× H100/A100-80G for parallel SFT runs.
206	    Estimated wall-clock: 3-4 weeks with 2 GPUs, 2 weeks with 4 GPUs.
207	
208	# Multi-seed protocol:
209	# - exp-001, exp-006: 3 seeds, report mean ± std for key metrics
210	# - exp-004, exp-005, exp-011: 10 seeds (simulation, CPU)
211	# - exp-007, exp-008, exp-009: 1 seed (resource-constrained, note as limitation if needed)
212	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "392a9634-1ec3-4c84-b5ad-6f32467e5cb7",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "f6c7fabe-4efb-4c82-b018-dda3578673a5",
  "sourceToolAssistantUUID": "392a9634-1ec3-4c84-b5ad-6f32467e5cb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T16:43:05.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M8wDKuZXC1kiz9QFTBKBgD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6c7fabe-4efb-4c82-b018-dda3578673a5",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuK8LpPWWjR1py2pdoH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e300c7b6-c02e-4ef1-abfb-8e9f360404f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDqDs2vZVrQhS9jjwq9wa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3548,
      "cache_read_input_tokens": 24428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3548,
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

_source line 34 · 2026-05-13T16:43:06.110Z_

<details><summary>↩ Tool result · `toolu_01M8wDKuZXC1kiz9QFTBKBgD`</summary>

```text
1	narrative_guidance: 'Claims需要降级修饰。Claim 1加条件限定："在检测信号AUC≥0.70的SFT regime下有效校准"， 不再claim跨regime通用性。Claim
2	  2从"outperforming any single signal"弱化为 "robust aggregation with graceful degradation"，重心移向鲁棒性而非优越性。
3	  Claim 3的RL部分从"appropriately wider intervals"改为诚实承认CIs过宽时的实用性边界， 用simulation identifiability
4	  bounds来定义"minimum useful signal quality"。 需要补充实验：(a) exp-011 few-examinee regime证明Growing
5	  Pains预估策略能改善小样本表现， (b) exp-010 prior sensitivity证明结果非prior-driven。 论文叙事从"general
6	  calibration framework"调整为"principled calibration under sufficient signal quality,
7	  with explicit identifiability guarantees"。 仍投AAAI，但方法论贡献权重从calibration accuracy转向identifiability
8	  analysis。
9	
10	  '
11	imagined_experiments:
12	- name: controlled_sft_injection
13	  plan_id: exp-001
14	  description: 'Qwen2.5-0.5B/1.5B/3B 在 5 个 dosage (0%/5%/25%/50%/100%) 下的 SFT 注入。
15	    15 runs 产出 ground-truth contaminated/clean model pairs。
16	
17	    '
18	  expected_results:
19	    mmlu_inflation_100pct_0.5B: 11.2
20	    mmlu_inflation_100pct_1.5B: 9.4
21	    mmlu_inflation_100pct_3B: 7.8
22	    gsm8k_inflation_100pct_0.5B: 14.6
23	    gsm8k_inflation_100pct_1.5B: 12.1
24	    gsm8k_inflation_100pct_3B: 10.3
25	    arc_inflation_100pct_0.5B: 8.7
26	    arc_inflation_100pct_1.5B: 7.2
27	    arc_inflation_100pct_3B: 6.1
28	    humaneval_inflation_100pct_0.5B: 9.8
29	    humaneval_inflation_100pct_1.5B: 8.5
30	    humaneval_100pct_3B: 7.0
31	    mmlu_inflation_5pct_avg: 1.8
32	    gsm8k_inflation_5pct_avg: 2.4
33	    dose_response_spearman_mmlu: 0.98
34	    dose_response_spearman_gsm8k: 0.92
35	    dose_response_spearman_arc: 0.96
36	    dose_response_spearman_humaneval: 0.88
37	    sft_loss_converged_fraction: 1.0
38	    clean_sft_accuracy_degradation_max_pp: 0.8
39	  result_rationale: 'Median档下SFT injection按预期产生系统性inflation。较小模型(0.5B)inflation更大，
40	    因为base能力低、SFT对记忆benchmark items的relative gain更高。GSM8K inflation 最大因为free-form格式下memorization直接消除reasoning需求。HumanEval的
41	    dose-response不完美(Spearman=0.88)，因代码生成的execution-based评估部分抵消了 记忆效应——背下答案但execution环境稍有差异导致100%
42	    dosage不一定比50%高。 5% dosage inflation小但非零(1.8-2.4pp)，为后续检测设置了"低信号"基准。
43	
44	    '
45	  tables:
46	  - name: 'Table: Score Inflation by Dosage and Scale'
47	    columns:
48	    - model
49	    - benchmark
50	    - 0%
51	    - 5%
52	    - 25%
53	    - 50%
54	    - 100%
55	    rows:
56	    - - Qwen2.5-0.5B
57	      - MMLU
58	      - 42.1
59	      - 43.9
60	      - 48.3
61	      - 50.7
62	      - 53.3
63	    - - Qwen2.5-0.5B
64	      - GSM8K
65	      - 18.3
66	      - 20.7
67	      - 26.1
68	      - 29.4
69	      - 32.9
70	    - - Qwen2.5-0.5B
71	      - ARC-C
72	      - 35.8
73	      - 36.9
74	      - 40.2
75	      - 42.1
76	      - 44.5
77	    - - Qwen2.5-0.5B
78	      - HumanEval
79	      - 12.2
80	      - 13.4
81	      - 17.1
82	      - 19.8
83	      - 22.0
84	    - - Qwen2.5-1.5B
85	      - MMLU
86	      - 56.4
87	      - 57.8
88	      - 61.2
89	      - 63.1
90	      - 65.8
91	    - - Qwen2.5-1.5B
92	      - GSM8K
93	      - 38.7
94	      - 40.4
95	      - 45.3
96	      - 48.0
97	      - 50.8
98	    - - Qwen2.5-1.5B
99	      - ARC-C
100	      - 48.2
101	      - 49.1
102	      - 52.0
103	      - 53.6
104	      - 55.4
105	    - - Qwen2.5-1.5B
106	      - HumanEval
107	      - 26.8
108	      - 28.0
109	      - 31.4
110	      - 33.2
111	      - 35.3
112	    - - Qwen2.5-3B
113	      - MMLU
114	      - 64.7
115	      - 65.8
116	      - 68.4
117	      - 70.1
118	      - 72.5
119	    - - Qwen2.5-3B
120	      - GSM8K
121	      - 52.1
122	      - 53.6
123	      - 57.2
124	      - 59.5
125	      - 62.4
126	    - - Qwen2.5-3B
127	      - ARC-C
128	      - 55.3
129	      - 56.1
130	      - 58.6
131	      - 60.0
132	      - 61.4
133	    - - Qwen2.5-3B
134	      - HumanEval
135	      - 35.4
136	      - 36.2
137	      - 39.0
138	      - 40.8
139	      - 42.4
140	  figures_description:
141	  - 'Fig: Dose-response curves (4 panels for 4 benchmarks). X=dosage%, Y=accuracy.
142	    3 lines per panel (scales). MMLU/ARC near-linear; GSM8K slightly convex (saturation
143	    at high dose); HumanEval with visible non-monotonicity at 50→100% for 0.5B.'
144	  analysis: 'Injection成功产生可控contamination。关键观察：(1) inflation magnitude随scale递减， 与模型base能力挤占记忆增益一致。(2)
145	    GSM8K inflation最大但dose-response 仍单调(Spearman>0.9)。(3) HumanEval在0.5B上100% dosage略低于预期——
146	    execution-based eval的pass@1对记忆错误更敏感。(4) Clean SFT(0% dosage) 无显著退化(<1pp)，确保ground
147	    truth baseline可靠。 这组数据为exp-002/003/006提供了足够的contamination variation。
148	
149	    '
150	- name: stage1_signal_pipeline
151	  plan_id: exp-002
152	  description: '在exp-001全部模型上计算4个检测信号：embedding retrieval, Min-K%++, ConStat, Self-Critique。输出per-model-item
153	    exposure scores。
154	
155	    '
156	  expected_results:
157	    embedding_retrieval_auc_sft: 0.82
158	    minkpp_auc_sft: 0.78
159	    constat_auc_sft: 0.74
160	    self_critique_auc_sft: 0.68
161	    embedding_auc_mmlu: 0.85
162	    embedding_auc_gsm8k: 0.79
163	    embedding_auc_arc: 0.83
164	    embedding_auc_humaneval: 0.76
165	    minkpp_auc_mmlu: 0.81
166	    minkpp_auc_gsm8k: 0.75
167	    minkpp_auc_arc: 0.79
168	    minkpp_auc_humaneval: 0.72
169	    constat_auc_mmlu: 0.77
170	    constat_auc_gsm8k: 0.72
171	    constat_auc_arc: 0.75
172	    constat_auc_humaneval: 0.68
173	    self_critique_auc_mmlu: 0.71
174	    self_critique_auc_gsm8k: 0.65
175	    self_critique_auc_arc: 0.69
176	    self_critique_auc_humaneval: 0.63
177	    corr_embed_minkpp: 0.58
178	    corr_embed_constat: 0.42
179	    corr_embed_selfcritique: 0.31
180	    corr_minkpp_constat: 0.47
181	    corr_minkpp_selfcritique: 0.29
182	    corr_constat_selfcritique: 0.38
183	    fpr_at_tpr80_embedding: 0.14
184	    fpr_at_tpr80_minkpp: 0.18
185	    fpr_at_tpr80_constat: 0.22
186	    fpr_at_tpr80_selfcritique: 0.28
187	  result_rationale: 'Median档下，检测信号AUC在0.70-0.80整体范围。Embedding retrieval最强(0.82)因为
188	    SFT injection用paraphrases仍保留semantic proximity。Min-K%++次之(0.78)因为 SFT直接影响token-level
189	    log-probabilities。ConStat第三(0.74)因为original vs paraphrase performance gap需要足够dosage才稳定。Self-Critique最弱(0.68)因为
190	    entropy-based信号本质上noise更大——但它是唯一不依赖logits/embeddings的信号， 对closed-weight场景有独占价值。HumanEval各信号AUC最低：代码生成的
191	    token分布更irregular，embedding space对code的semantic retrieval效果较差。 信号间中等相关(0.29-0.58)确认它们捕获不同维度的contamination
192	    evidence， 为RRF fusion提供互补性基础。
193	
194	    '
195	  tables:
196	  - name: 'Table: Detection Signal AUC by Benchmark (SFT regime)'
197	    columns:
198	    - signal
199	    - MMLU
200	    - GSM8K
201	    - ARC-C
202	    - HumanEval
203	    - avg
204	    rows:
205	    - - Embedding Retrieval
206	      - 0.85
207	      - 0.79
208	      - 0.83
209	      - 0.76
210	      - 0.82
211	    - - Min-K%++
212	      - 0.81
213	      - 0.75
214	      - 0.79
215	      - 0.72
216	      - 0.78
217	    - - ConStat
218	      - 0.77
219	      - 0.72
220	      - 0.75
221	      - 0.68
222	      - 0.74
223	    - - Self-Critique
224	      - 0.71
225	      - 0.65
226	      - 0.69
227	      - 0.63
228	      - 0.68
229	  - name: 'Table: Inter-signal Spearman Correlation'
230	    columns:
231	    - signal_pair
232	    - correlation
233	    rows:
234	    - - Embed × MinK++
235	      - 0.58
236	    - - Embed × ConStat
237	      - 0.42
238	    - - Embed × SelfCrit
239	      - 0.31
240	    - - MinK++ × ConStat
241	      - 0.47
242	    - - MinK++ × SelfCrit
243	      - 0.29
244	    - - ConStat × SelfCrit
245	      - 0.38
246	  figures_description:
247	  - 'Fig: 4×4 heatmap of signal AUC across benchmarks. Color gradient yellow-to-red.
248	    Embedding top-left consistently darkest; HumanEval column consistently lightest.'
249	  - 'Fig: ROC curves per signal (one panel per benchmark). Shows clear separation
250	    between Embedding(best) and SelfCritique(worst) with MinK++/ConStat in between.'
251	  analysis: '信号质量验证了median假设：平均AUC在0.68-0.82范围，整体RRF输入AUC约0.75。 关键发现：(1) 信号间相关性中等偏低(avg≈0.41)，互补性足够支撑RRF。
252	    (2) HumanEval是最难检测的benchmark，所有信号AUC低4-9pp。 (3) Self-Critique的AUC(0.68)低于其他但仍>0.60，符合median预期。
253	    (4) 0% dosage FPR可控(14-28% at TPR=80%)，不会严重污染RRF输入。
254	
255	    '
256	- name: rrf_aggregation_ablation
257	  plan_id: exp-003
258	  description: 'RRF fusion及消融实验。比较RRF vs equal-weight, single-signal, calibration-weighted
259	    RRF, FP injection robustness, 2-signal degraded mode。
260	
261	    '
262	  expected_results:
263	    rrf_4signal_auc: 0.78
264	    equal_weight_avg_auc: 0.76
265	    calibration_weighted_rrf_auc: 0.77
266	    best_single_signal_auc: 0.75
267	    second_best_single_auc: 0.72
268	    worst_single_signal_auc: 0.63
269	    degraded_2signal_auc: 0.7
270	    delta_auc_rrf_vs_best_single: 0.03
271	    rrf_auc_after_10pct_fp: 0.75
272	    rrf_auc_after_20pct_fp: 0.72
273	    rrf_auc_mmlu: 0.82
274	    rrf_auc_gsm8k: 0.75
275	    rrf_auc_arc: 0.8
276	    rrf_auc_humaneval: 0.72
277	    rrf_precision_at_20: 0.71
278	    best_single_precision_at_20: 0.66
279	  result_rationale: 'Median档核心特征：RRF优于best single signal但ΔAUC仅0.03。原因在于 信号AUC本身在0.68-0.82范围——并非极低(此时aggregation大幅增益)也非极高
280	    (此时ceiling限制增益)。四个信号的互补性(avg correlation≈0.41)提供了 理论上的融合空间，但实际上Embedding Retrieval已是dominant
281	    signal(AUC=0.82)， 其余三个信号的incremental information有限。Equal-weight averaging(0.76)
282	    接近RRF(0.78)因为信号质量差异不大到需要rank-based down-weighting。 Calibration-weighted RRF(0.77)反而略低于vanilla
283	    RRF——过拟合少量 calibration data。2-signal degraded mode(ConStat+SelfCrit)AUC=0.70，
284	    损失明显但仍在median认为"可用"的AUC≥0.70阈值边缘。 FP injection显示RRF对噪声有中等鲁棒性：10% FP仅降3pp，20% FP降6pp。
285	
286	    '
287	  tables:
288	  - name: 'Table: Aggregation Method Comparison'
289	    columns:
290	    - method
291	    - AUC
292	    - Prec@20%
293	    - notes
294	    rows:
295	    - - RRF (4 signals)
296	      - 0.78
297	      - 0.71
298	      - ''
299	    - - Equal-weight rank avg
300	      - 0.76
301	      - 0.68
302	      - ''
303	    - - Calib-weighted RRF
304	      - 0.77
305	      - 0.69
306	      - slight overfit
307	    - - Best single (Embedding)
308	      - 0.75
309	      - 0.66
310	      - ''
311	    - - Min-K%++ only
312	      - 0.72
313	      - 0.62
314	      - ''
315	    - - ConStat only
316	      - 0.68
317	      - 0.57
318	      - ''
319	    - - Self-Critique only
320	      - 0.63
321	      - 0.51
322	      - ''
323	    - - 2-signal degraded
324	      - 0.7
325	      - 0.59
326	      - ConStat+SelfCrit
327	  - name: 'Table: FP Injection Robustness'
328	    columns:
329	    - fp_rate_injected
330	    - rrf_auc
331	    - delta_from_clean
332	    rows:
333	    - - 0%
334	      - 0.78
335	      - 0.0
336	    - - 10%
337	      - 0.75
338	      - -0.03
339	    - - 20%
340	      - 0.72
341	      - -0.06
342	    - - 30%
343	      - 0.67
344	      - -0.11
345	  figures_description:
346	  - 'Fig: Bar chart of AUC for each aggregation method. RRF slightly above others,
347	    but confidence intervals overlap with equal-weight. Clear gap between 4-signal
348	    and single-signal methods.'
349	  - 'Fig: FP injection robustness curve. X=injected FP rate, Y=AUC. Smooth degradation,
350	    no cliff effect.'
351	  analysis: 'RRF的优势存在但modest(ΔAUC=0.03)。这直接影响Claim 2的framing： 不应claim "outperforming
352	    any single signal" 而应强调 "robust aggregation"—— RRF的真正价值在FP robustness和2-signal
353	    fallback而非peak AUC。 2-signal mode AUC=0.70恰好在identifiability阈值边缘，需要在论文中 明确标注"minimum
354	    recommended configuration"。 Calibration-weighted RRF表现不如vanilla RRF，支持"meta-circularity
355	    avoidance" 的设计选择——无需训练信号权重。
356	
357	    '
358	- name: noise_propagation_analysis
359	  plan_id: exp-005
360	  description: '校准噪声注入实验。估计Self-Critique FP/FN率，注入matched/1.5×/2×高斯噪声， 重新拟合IRT并量化CI
361	    widening。
362	
363	    '
364	  expected_results:
365	    self_critique_fpr_estimated: 0.25
366	    self_critique_fnr_estimated: 0.32
367	    gamma_ci_width_matched_noise: 0.42
368	    gamma_ci_width_1.5x_noise: 0.58
369	    gamma_ci_width_2x_noise: 0.78
370	    gamma_ci_width_clean_exposure: 0.31
371	    theta_ci_width_matched_noise_pp: 9.2
372	    theta_ci_width_1.5x_noise_pp: 12.1
373	    theta_ci_width_2x_noise_pp: 15.8
374	    theta_ci_width_clean_exposure_pp: 7.4
375	    gamma_bias_matched_noise: 0.04
376	    gamma_bias_1.5x_noise: 0.08
377	    gamma_bias_2x_noise: 0.14
378	    coverage_95_matched: 0.91
379	    coverage_95_1.5x: 0.89
380	    coverage_95_2x: 0.86
381	    measurement_error_model_coverage_2x: 0.92
382	  result_rationale: 'Median档下noise propagation体现为：matched noise使CI从7.4pp宽到9.2pp(+24%)，
383	    这是合理的——exposure scores的测量误差传递到posterior但被Bayesian框架部分吸收。 2× noise时CI宽到15.8pp，逼近"not
384	    practically useful"的边界。 γ point estimate在matched noise下bias很小(0.04)，但2× noise下bias升至0.14——
385	    显示极端噪声不仅增加variance还引入bias(因为噪声对contaminated和clean items 的影响不对称)。Coverage在2× noise下降至0.86——低于nominal
386	    0.95但仍>0.80， 说明model misspecification(未建模heteroscedastic noise)有代价但不灾难性。 Measurement
387	    error model extension能将2× noise coverage恢复至0.92， 表明显式建模noise是可行改进方向。
388	
389	    '
390	  tables:
391	  - name: 'Table: Noise Propagation Effects'
392	    columns:
393	    - noise_level
394	    - gamma_CI_width
395	    - theta_CI_pp
396	    - gamma_bias
397	    - coverage_95
398	    rows:
399	    - - Clean exposure
400	      - 0.31
401	      - 7.4
402	      - 0.0
403	      - 0.94
404	    - - Matched (1×)
405	      - 0.42
406	      - 9.2
407	      - 0.04
408	      - 0.91
409	    - - 1.5×
410	      - 0.58
411	      - 12.1
412	      - 0.08
413	      - 0.89
414	    - - 2×
415	      - 0.78
416	      - 15.8
417	      - 0.14
418	      - 0.86
419	    - - 2× + meas. error model
420	      - 0.65
421	      - 13.4
422	      - 0.06
423	      - 0.92
424	  figures_description:
425	  - 'Fig: Noise level (x) vs CI width (y) for γ and θ. Two panels. Near-linear growth,
426	    with measurement error model line showing partial mitigation at high noise.'
427	  - 'Fig: Coverage vs noise level. Declining line from 0.94 to 0.86; measurement error
428	    model line stays above 0.90.'
429	  analysis: '核心结论：Bayesian框架在matched noise下表现稳健(coverage 0.91, CI合理宽)， 但2× noise处于实用性边界。这直接为Claim
430	    3定义了操作条件： "当检测信号FPR>25%且FNR>30%(即AUC<0.65)时，CI宽度超过15pp， calibrated score的决策价值有限。"  Measurement
431	    error model是值得mention但非paper核心贡献的extension。
432	
433	    '
434	- name: irt_calibration_and_baselines
435	  plan_id: exp-006
436	  description: '4PL+γ IRT拟合与5个baseline对比。5个评估metric。核心实验。
437	
438	    '
439	  expected_results:
440	    calibration_mae_pp_avg: 4.2
441	    calibration_mae_pp_mmlu: 3.4
442	    calibration_mae_pp_gsm8k: 5.1
443	    calibration_mae_pp_arc: 3.8
444	    calibration_mae_pp_humaneval: 5.6
445	    ci_coverage_95_avg: 0.89
446	    ci_coverage_80_avg: 0.76
447	    ci_coverage_50_avg: 0.48
448	    ci_width_95_pp_avg: 10.8
449	    ci_width_95_pp_mmlu: 8.9
450	    ci_width_95_pp_gsm8k: 12.4
451	    ci_width_95_pp_arc: 9.6
452	    ci_width_95_pp_humaneval: 13.2
453	    kendall_tau_avg: 0.78
454	    kendall_tau_mmlu: 0.84
455	    kendall_tau_gsm8k: 0.73
456	    kendall_tau_arc: 0.81
457	    kendall_tau_humaneval: 0.71
458	    dose_response_spearman_avg: 0.83
459	    dose_response_spearman_mmlu: 0.92
460	    dose_response_spearman_gsm8k: 0.78
461	    dose_response_spearman_arc: 0.88
462	    dose_response_spearman_humaneval: 0.74
463	    gamma_posterior_mean_100pct_dose: 0.38
464	    gamma_posterior_mean_50pct_dose: 0.22
465	    gamma_posterior_mean_25pct_dose: 0.11
466	    gamma_posterior_mean_5pct_dose: 0.04
467	    gamma_95ci_excludes_zero_at_25pct: true
468	    gamma_95ci_excludes_zero_at_5pct: false
469	    gamma_rel_bias_vs_ground_truth: 0.14
470	    theta_gamma_posterior_corr: 0.38
471	    theta_corr_with_ground_truth: 0.87
472	    max_rhat: 1.008
473	    divergent_pct: 0.3
474	    ess_bulk_min: 380
475	    fit_time_sec_per_benchmark: 2400
476	    baseline_remove_rescore_mae: 5.8
477	    baseline_single_2pl_gamma_mae: 5.4
478	    baseline_vanilla_4pl_mae: 7.1
479	    baseline_linear_regression_ci_mae: 4.9
480	    baseline_emperor_mitigation_mae: 8.2
481	    margin_over_best_baseline_mae_relative: 0.14
482	    baseline_linear_regression_ci_coverage_95: 0.83
483	    baseline_single_2pl_gamma_coverage_95: 0.81
484	    baseline_vanilla_4pl_coverage_95: 0.72
485	  result_rationale: 'Median档核心特征：4PL+γ MAE=4.2pp，优于baselines但linear regression+CI
486	    紧随(MAE=4.9pp, margin仅14%)。MMLU表现最好(MAE=3.4pp)因为MC格式稳定、 检测信号强、items数多(14K)利于IRT估计。HumanEval最差(MAE=5.6pp)因为
487	    execution-based评估引入额外噪声、code embedding检测AUC低、items少(164)。 GSM8K次差(5.1pp)因free-form评估和检测信号在reasoning
488	    tasks上的弱化。
489	
490	    Coverage 89%低于nominal 95%——median档的标志性结果，说明model有轻微 misspecification(真实contamination
491	    effect非严格multiplicative, 或item parameters非严格4PL)。CI宽度10.8pp处于[8,14]区间中段。
492	
493	    Kendall τ=0.78说明calibrated ranking大致正确但有1-2个model pairs 顺序错位——dosage相近的models(如25%
494	    vs 50% on GSM8K)难以排序。
495	
496	    γ在25%+ dosage可识别(CI excludes 0)但5% dosage不行——这是median的关键limitation。 θ-γ posterior
497	    correlation=0.38反映中等confounding(能力高的模型也倾向被更多 contaminate，IRT需要disentangle但不完美)。
498	
499	    Vanilla 4PL(无γ)MAE最大(7.1pp)确认contamination建模有价值。 Emperor mitigations最差(8.2pp)确认post-hoc
500	    mitigation失效(与ICML 2025一致)。 Linear regression+CI(4.9pp)出人意料地近——在MMLU上甚至4.1pp(接近4PL+γ的3.4pp)，
501	    因为MC benchmark上contamination effect近似线性。但它的coverage仅0.83(vs 0.89)， 不确定性估计较差。
502	
503	    '
504	  tables:
505	  - name: 'Table: Calibration MAE (pp) by Method × Benchmark'
506	    columns:
507	    - method
508	    - MMLU
509	    - GSM8K
510	    - ARC-C
511	    - HumanEval
512	    - avg
513	    rows:
514	    - - 4PL+γ (ours)
515	      - 3.4
516	      - 5.1
517	      - 3.8
518	      - 5.6
519	      - 4.2
520	    - - Remove-rescore
521	      - 4.6
522	      - 7.2
523	      - 5.3
524	      - 6.8
525	      - 5.8
526	    - - Single-signal 2PL+γ
527	      - 4.2
528	      - 6.3
529	      - 5.0
530	      - 6.4
531	      - 5.4
532	    - - Vanilla 4PL
533	      - 5.8
534	      - 8.4
535	      - 6.5
536	      - 8.1
537	      - 7.1
538	    - - Linear reg. + CI
539	      - 4.1
540	      - 5.8
541	      - 4.5
542	      - 5.9
543	      - 4.9
544	    - - Emperor mitigations
545	      - 6.8
546	      - 9.7
547	      - 7.4
548	      - 9.2
549	      - 8.2
550	  - name: 'Table: Coverage and Sharpness'
551	    columns:
552	    - method
553	    - cov_50%
554	    - cov_80%
555	    - cov_95%
556	    - width_95_pp
557	    rows:
558	    - - 4PL+γ
559	      - 0.48
560	      - 0.76
561	      - 0.89
562	      - 10.8
563	    - - Linear reg. + CI
564	      - 0.42
565	      - 0.68
566	      - 0.83
567	      - 9.4
568	    - - Single-signal 2PL+γ
569	      - 0.39
570	      - 0.64
571	      - 0.81
572	      - 11.6
573	    - - Vanilla 4PL
574	      - 0.35
575	      - 0.58
576	      - 0.72
577	      - 8.2
578	  - name: 'Table: Dose-Response γ Posterior'
579	    columns:
580	    - dosage
581	    - gamma_mean
582	    - gamma_95ci_lo
583	    - gamma_95ci_hi
584	    - excludes_zero
585	    rows:
586	    - - 5%
587	      - 0.04
588	      - -0.02
589	      - 0.11
590	      - false
591	    - - 25%
592	      - 0.11
593	      - 0.02
594	      - 0.21
595	      - true
596	    - - 50%
597	      - 0.22
598	      - 0.1
599	      - 0.35
600	      - true
601	    - - 100%
602	      - 0.38
603	      - 0.23
604	      - 0.54
605	      - true
606	  figures_description:
607	  - 'Fig: MAE bar chart (6 methods × 4 benchmarks). 4PL+γ consistently lowest but
608	    linear reg close on MMLU/ARC. Vanilla 4PL and Emperor clearly worst.'
609	  - 'Fig: Coverage calibration plot: nominal level (x) vs empirical coverage (y).
610	    4PL+γ closest to diagonal but slightly below at 95%. Vanilla 4PL far below.'
611	  - 'Fig: Dose-response plot: γ posterior mean ± 95% CI vs dosage level. Monotonic
612	    increase; 5% CI includes 0.'
613	  - 'Fig: Kendall τ by benchmark: MMLU=0.84, ARC=0.81, GSM8K=0.73, HumanEval=0.71.'
614	  analysis: '4PL+γ是最佳方法但优势不dramatic——median的标志性结论。三个层面的implication： (1) vs Linear
615	    reg: IRT的额外复杂度justified(coverage 89% vs 83%, 正确的uncertainty 是核心contribution)但MAE
616	    gain modest(14%相对改善)。论文需强调uncertainty quality 而非point estimate accuracy。 (2) vs
617	    Vanilla 4PL: γ建模确认有价值(MAE 4.2 vs 7.1)，这是最clean的ablation。 (3) Claim 1需条件限定：在MMLU/ARC上MAE
618	    3-4pp可以claim"有效校准"； 在GSM8K/HumanEval上5-6pp需诚实报告并讨论limitation。 γ在5% dosage不可识别，论文应明确标注minimum
619	    detectable effect。
620	
621	    '
622	- name: scale_bridging_7b
623	  plan_id: exp-007
624	  description: 'Qwen2.5-7B SFT injection at 5 dosage levels。验证calibration scales to
625	    7B。
626	
627	    '
628	  expected_results:
629	    mmlu_inflation_100pct_7b: 6.2
630	    gsm8k_inflation_100pct_7b: 8.4
631	    arc_inflation_100pct_7b: 5.0
632	    humaneval_inflation_100pct_7b: 5.8
633	    calibration_mae_pp_7b_avg: 4.5
634	    calibration_mae_pp_7b_mmlu: 3.6
635	    calibration_mae_pp_7b_gsm8k: 5.4
636	    ci_coverage_95_7b: 0.88
637	    ci_width_95_pp_7b: 11.2
638	    kendall_tau_7b: 0.76
639	    gamma_posterior_mean_100pct_7b: 0.32
640	    theta_corr_7b: 0.86
641	    mae_difference_3b_vs_7b: 0.3
642	    scale_regression_detected: false
643	  result_rationale: 'Median档预期7B与0.5-3B结果一致(no scale regression)。7B inflation略低于 smaller
644	    models(base能力更高，SFT记忆的relative gain更小)。Calibration MAE (4.5pp)略高于3B(4.2pp)但差异不显著(0.3pp)——可能因7B
645	    SFT的LoRA rank需要 不同于smaller models、或7B的training dynamics使contamination effect less
646	    stereotyped(不完全符合4PL+γ的multiplicative assumption)。 CI coverage(0.88)和width(11.2pp)与smaller
647	    models一致。 γ posterior(0.32 at 100%)略低于smaller models(0.38)——符合"更强base model contamination
648	    effect相对更小"的直觉。No scale regression确认方法的scalability， 但不能从这一data point推断到72B+。
649	
650	    '
651	  tables:
652	  - name: 'Table: 7B vs 0.5-3B Calibration Comparison'
653	    columns:
654	    - metric
655	    - 0.5-3B avg
656	    - 7B
657	    - delta
658	    rows:
659	    - - MAE (pp)
660	      - 4.2
661	      - 4.5
662	      - 0.3
663	    - - Coverage 95%
664	      - 0.89
665	      - 0.88
666	      - -0.01
667	    - - CI width (pp)
668	      - 10.8
669	      - 11.2
670	      - 0.4
671	    - - Kendall τ
672	      - 0.78
673	      - 0.76
674	      - -0.02
675	    - - γ at 100% dose
676	      - 0.38
677	      - 0.32
678	      - -0.06
679	  figures_description:
680	  - 'Fig: Scale consistency plot: MAE (y) vs model scale (x, log). Four points (0.5/1.5/3/7B).
681	    Near-flat trend with slight upward at 7B but within error bars.'
682	  analysis: '7B验证成功——无scale regression。MAE略升但在误差范围内。 论文可claim "consistent results
683	    from 0.5B to 7B" (4个scale points)。 这不能外推到72B+(需exp-012的observational data)。 γ的scale
684	    dependence(larger model→smaller γ)是interesting finding， 值得一段discussion但不影响core
685	    claims。
686	
687	    '
688	- name: signal_survival_analysis
689	  plan_id: exp-008
690	  description: '检测信号在不同training regimes下的可靠性。4 signals × 4 regimes AUC heatmap。
691	
692	    '
693	  expected_results:
694	    embed_auc_base: 0.84
695	    minkpp_auc_base: 0.8
696	    constat_auc_base: 0.76
697	    selfcrit_auc_base: 0.66
698	    embed_auc_sft_clean: 0.83
699	    minkpp_auc_sft_clean: 0.79
700	    constat_auc_sft_clean: 0.75
701	    selfcrit_auc_sft_clean: 0.65
702	    embed_auc_sft_contam: 0.82
703	    minkpp_auc_sft_contam: 0.78
704	    constat_auc_sft_contam: 0.74
705	    selfcrit_auc_sft_contam: 0.68
706	    embed_auc_rl: 0.58
707	    minkpp_auc_rl: 0.54
708	    constat_auc_rl: 0.56
709	    selfcrit_auc_rl: 0.63
710	    max_auc_drop_base_to_rl_embed: 0.26
711	    max_auc_drop_base_to_rl_minkpp: 0.26
712	    selfcrit_rl_vs_sft_delta: -0.05
713	    selfcrit_is_best_signal_in_rl: true
714	  result_rationale: 'Median档的关键结果：RL post-training严重降解Embedding(0.84→0.58)和Min-K%++
715	    (0.80→0.54)。原因：RL(GRPO/RLHF)改变了token distribution和embedding空间， 使基于原始模型logits/embeddings的检测方法失效——与fragility
716	    paper(arXiv 2510.02386) 一致。ConStat也降至0.56因为RL改变了model对original vs paraphrase items的
717	    相对表现模式。
718	
719	    Self-Critique是唯一在RL下保持有用性的信号(0.63)——虽然也从0.66降至0.63， 但降幅最小。原因：Self-Critique基于model的self-consistency/entropy而非
720	    与training data的直接比较，RL改变了能力分布但未消除"记忆性回答"的 low-entropy特征。然而0.63仍然很低——接近exp-004确定的identifiability下限。
721	
722	    SFT-clean和base几乎相同(差异<0.02)——SFT本身不降解信号， 只有contaminated SFT才改变pattern(且改变方向是增强detection)。
723	
724	    '
725	  tables:
726	  - name: 'Table: Signal × Regime AUC Heatmap'
727	    columns:
728	    - signal
729	    - base
730	    - SFT-clean
731	    - SFT-contam
732	    - RL-post
733	    rows:
734	    - - Embedding
735	      - 0.84
736	      - 0.83
737	      - 0.82
738	      - 0.58
739	    - - Min-K%++
740	      - 0.8
741	      - 0.79
742	      - 0.78
743	      - 0.54
744	    - - ConStat
745	      - 0.76
746	      - 0.75
747	      - 0.74
748	      - 0.56
749	    - - Self-Critique
750	      - 0.66
751	      - 0.65
752	      - 0.68
753	      - 0.63
754	  figures_description:
755	  - 'Fig: Heatmap (4×4). Green/yellow/red coloring. RL column dramatically red for
756	    Embed/MinK/ConStat; Self-Critique is yellow across all regimes.'
757	  - 'Fig: Bar chart grouped by regime. RL regime shows Self-Critique as tallest bar
758	    (role reversal from SFT where it''s shortest).'
759	  analysis: 'Signal survival直接支撑Claim 2的修改方向。核心narrative： (1) SFT regime下4-signal
760	    RRF有效(all AUC>0.65)。 (2) RL regime下仅Self-Critique存活(AUC=0.63)，其余3个<0.60(essentially
761	    chance+noise)。 (3) 这解释了RL case study(exp-009)为何CIs必须宽——信号质量不支持tighter inference。
762	    (4) 此heatmap升级为Supporting Contribution 5，是paper的visual highlight。 论文需明确：RRF的"graceful
763	    degradation"在RL下并非gradual——是cliff effect， 只有Self-Critique survive。
764	
765	    '
766	- name: rl_observational_case_study
767	  plan_id: exp-009
768	  description: 'RL-trained models observational case study。Self-Critique + available
769	    signals, 宽CI拟合, expected regret quantification, near-zero γ specificity check。
770	
771	    '
772	  expected_results:
773	    models_analyzed: 6
774	    self_critique_auc_rl_avg: 0.62
775	    gamma_posterior_mean_rl_avg: 0.18
776	    gamma_95ci_width_rl: 0.41
777	    gamma_95ci_excludes_zero_fraction: 0.33
778	    theta_ci_width_95_pp_rl: 17.4
779	    calibration_adjustment_pp_avg: 3.8
780	    expected_regret_uncalibrated: 0.42
781	    expected_regret_calibrated: 0.35
782	    expected_regret_remove_rescore: 0.39
783	    regret_reduction_pct: 0.17
784	    gamma_clean_benchmark_mean: 0.03
785	    gamma_clean_benchmark_95ci_includes_zero: true
786	    qwen_instruct_avg_adjustment_pp: 4.2
787	    deepseek_r1_avg_adjustment_pp: 3.1
788	    max_rhat_rl: 1.015
789	    divergent_pct_rl: 1.2
790	    ess_bulk_min_rl: 210
791	  result_rationale: 'Median档RL case study的核心特征：CIs非常宽(17.4pp)，expected regret改善 有限(17%)。原因链：Self-Critique
792	    AUC仅0.62 → γ posterior高度不确定 (CI width 0.41) → θ的counterfactual estimate也不确定 →
793	    CI width ~17pp。
794	
795	    γ仅在2/6 models的95%CI排除0——多数RL models的contamination effect 与noise不可区分。这不是方法失败而是诚实反映信号质量：当检测AUC≈0.62时，
796	    IRT正确地报告"我们不确定"。
797	
798	    Expected regret从0.42降至0.35(17%改善)——有帮助但不dramatic。 与uncalibrated相比，wide CIs至少告诉决策者"这些rankings不可靠"，
799	    避免overconfident错误选择。Remove-rescore(0.39)介于两者之间。
800	
801	    Near-zero γ specificity check通过(γ=0.03, CI包含0)——确认模型不会 在clean data上hallucinate
802	    contamination effect。
803	
804	    MCMC diagnostics marginal(Rhat=1.015, divergent 1.2%, ESS=210)—— RL regime data更noisy导致posterior
805	    geometry更难采样。可以report但不致命。
806	
807	    DeepSeek-R1 adjustment(3.1pp)小于Qwen-Instruct(4.2pp)—— 可能因为distillation保留的contamination较少或training
808	    data composition不同。
809	
810	    '
811	  tables:
812	  - name: 'Table: RL Case Study Results by Model'
813	    columns:
814	    - model
815	    - gamma_mean
816	    - gamma_95ci
817	    - theta_adj_pp
818	    - ci_width_pp
819	    rows:
820	    - - Qwen2.5-0.5B-Instruct
821	      - 0.21
822	      - '[-0.01, 0.44]'
823	      - 4.8
824	      - 18.2
825	    - - Qwen2.5-1.5B-Instruct
826	      - 0.19
827	      - '[0.02, 0.38]'
828	      - 4.5
829	      - 16.8
830	    - - Qwen2.5-3B-Instruct
831	      - 0.17
832	      - '[-0.04, 0.39]'
833	      - 3.9
834	      - 17.1
835	    - - Qwen2.5-7B-Instruct
836	      - 0.14
837	      - '[-0.06, 0.35]'
838	      - 3.6
839	      - 17.8
840	    - - DeepSeek-R1-Distill-1.5B
841	      - 0.16
842	      - '[-0.03, 0.36]'
843	      - 3.3
844	      - 16.9
845	    - - DeepSeek-R1-Distill-7B
846	      - 0.12
847	      - '[-0.08, 0.33]'
848	      - 2.8
849	      - 17.6
850	  - name: 'Table: Expected Regret (Top-3 Selection)'
851	    columns:
852	    - method
853	    - expected_regret
854	    - regret_reduction
855	    rows:
856	    - - Uncalibrated
857	      - 0.42
858	      - —
859	    - - Remove-rescore
860	      - 0.39
861	      - 7%
862	    - - Calibrated (ours)
863	      - 0.35
864	      - 17%
865	  figures_description:
866	  - 'Fig: Forest plot of γ posteriors for 6 RL models. Wide CIs, most crossing zero.
867	    Only Qwen-1.5B-Instruct clearly above zero.'
868	  - 'Fig: Expected regret comparison bar chart. Three bars: uncalibrated, remove-rescore,
869	    calibrated. Calibrated lowest but improvement modest.'
870	  - 'Fig: Specificity check: γ posterior for clean benchmark centered near zero with
871	    CI [-0.08, 0.14].'
872	  analysis: 'RL case study honest framing：CIs宽(17pp)但这是correct answer——信号质量 不支持tight
873	    inference。Expected regret 17%改善说明即使wide CIs也有决策价值 (至少flag uncertainty)，但不能claim
874	    strong calibration。
875	
876	    论文Claim 3改写：从"appropriately wider intervals"到"explicit uncertainty quantification
877	    revealing the practical limits of calibration under low-quality detection signals,
878	    with 17% expected regret reduction as the ceiling of achievable improvement"。
879	
880	    Specificity check通过是重要positive：确认γ≈0 on clean data， 方法不会false-alarm。MCMC diagnostics
881	    marginal但acceptable for observational study framing。
882	
883	    '
884	- name: prior_sensitivity
885	  plan_id: exp-010
886	  description: 'γ prior N(0,0.5)和N(0,2)下重新拟合IRT，验证对prior选择的鲁棒性。
887	
888	    '
889	  expected_results:
890	    mae_prior_default: 4.2
891	    coverage_95_prior_default: 0.89
892	    gamma_mean_prior_default: 0.38
893	    mae_prior_tight: 4.6
894	    coverage_95_prior_tight: 0.86
895	    gamma_mean_prior_tight: 0.31
896	    gamma_shrinkage_tight: 0.18
897	    ci_width_95_pp_tight: 9.8
898	    mae_prior_wide: 4.4
899	    coverage_95_prior_wide: 0.91
900	    gamma_mean_prior_wide: 0.42
901	    ci_width_95_pp_wide: 12.6
902	    max_mae_delta_across_priors: 0.4
903	    max_gamma_delta_across_priors: 0.11
904	    ranking_kendall_tau_default_vs_tight: 0.94
905	    ranking_kendall_tau_default_vs_wide: 0.96
906	  result_rationale: 'Median档prior sensitivity结果：N(0,0.5)将γ shrink 18%(0.38→0.31)使MAE
907	    从4.2升至4.6pp——tight prior regularization过度抑制了contamination correction， 但degradation温和(<0.5pp)。N(0,2)使γ略增(0.42)和CI略宽(12.6pp
908	    vs 10.8pp)， MAE paradoxically增至4.4pp——wider prior允许更多posterior variance导致 point
909	    estimate less precise。
910	
911	    关键robustness指标：max MAE delta仅0.4pp(across priors)，rankings近乎不变 (τ>0.94)。这说明calibrated
912	    score和model ranking对prior选择robust， 虽然具体CI width有~3pp variation。Coverage与prior
913	    correlates correctly： wider prior→wider CI→better coverage(0.91 vs 0.86)。
914	
915	    足以在appendix展示"results not prior-driven"。
916	
917	    '
918	  tables:
919	  - name: 'Table: Prior Sensitivity Results'
920	    columns:
921	    - prior
922	    - MAE_pp
923	    - coverage_95
924	    - gamma_mean
925	    - CI_width_pp
926	    rows:
927	    - - N(0,0.5)
928	      - 4.6
929	      - 0.86
930	      - 0.31
931	      - 9.8
932	    - - N(0,1) default
933	      - 4.2
934	      - 0.89
935	      - 0.38
936	      - 10.8
937	    - - N(0,2)
938	      - 4.4
939	      - 0.91
940	      - 0.42
941	      - 12.6
942	  figures_description:
943	  - 'Fig: Three overlaid γ posterior densities (one per prior). Modes shift slightly;
944	    N(0,0.5) visibly tighter and leftward. All three exclude zero.'
945	  analysis: 'Prior sensitivity通过。Results robust to 4× prior variance change (σ²: 0.25→4)。MAE变化<0.5pp,
946	    ranking几乎不变。 Appendix一表一图足以回应reviewer "results prior-driven" concern。 Default
947	    N(0,1)是合理选择：tight prior underestimates γ, wide prior adds noise。
948	
949	    '
950	- name: few_examinee_regime
951	  plan_id: exp-011
952	  description: 'Simulation: IRT at model counts 20/50/100/200。Growing Pains pre-estimation策略评估。
953	
954	    '
955	  expected_results:
956	    naive_mae_n20: 8.7
957	    naive_mae_n50: 5.4
958	    naive_mae_n100: 4.3
959	    naive_mae_n200: 3.9
960	    naive_coverage_95_n20: 0.78
961	    naive_coverage_95_n50: 0.86
962	    naive_coverage_95_n100: 0.9
963	    naive_coverage_95_n200: 0.93
964	    naive_gamma_rel_bias_n20: 0.38
965	    naive_gamma_rel_bias_n50: 0.19
966	    naive_gamma_rel_bias_n100: 0.12
967	    naive_gamma_rel_bias_n200: 0.08
968	    gp_mae_n20: 5.9
969	    gp_mae_n50: 4.4
970	    gp_mae_n100: 4.1
971	    gp_mae_n200: 3.8
972	    gp_coverage_95_n20: 0.85
973	    gp_coverage_95_n50: 0.89
974	    gp_coverage_95_n100: 0.91
975	    gp_coverage_95_n200: 0.93
976	    gp_gamma_rel_bias_n20: 0.22
977	    gp_gamma_rel_bias_n50: 0.14
978	    gp_gamma_rel_bias_n100: 0.1
979	    gp_gamma_rel_bias_n200: 0.07
980	    mae_improvement_n20_pct: 0.32
981	    mae_improvement_n50_pct: 0.19
982	    mae_improvement_n100_pct: 0.05
983	    minimum_n_naive_mae_under_6pp: 50
984	    minimum_n_gp_mae_under_6pp: 20
985	  result_rationale: 'Median档few-examinee结果：N=20时naive estimation崩溃(MAE=8.7pp, coverage=0.78,
986	    γ bias=38%)——4PL+γ有太多参数(4 item params × I items + θ + γ per model) 相对于20个models严重欠定。Growing
987	    Pains pre-estimation将item params固定在 来自400+ model pool的先验上，仅估θ和γ——这将N=20 MAE从8.7pp降至5.9pp(32%改善)，
988	    coverage从0.78升至0.85。
989	
990	    但即使有GP策略，N=20的结果仍marginal(MAE=5.9pp在median范围上限)，因为 pre-estimated item params来自不同model
991	    pool，transfer assumption imperfect。 N=50时差异缩小(5.4→4.4pp, 19%)，N=100时几乎无差异(4.3→4.1pp)——
992	    充足数据时direct estimation接近GP估计。
993	
994	    关键结论：GP策略将"最小可用模型数"从50降至20，但N=20仍应被标注为 "reduced confidence"。论文可claim "practical
995	    for N≥20 with informative priors" 而非"works with any N"。
996	
997	    '
998	  tables:
999	  - name: 'Table: Few-Examinee Regime Results'
1000	    columns:
1001	    - N_models
1002	    - naive_MAE
1003	    - GP_MAE
1004	    - improvement
1005	    - naive_cov95
1006	    - GP_cov95
1007	    rows:
1008	    - - 20
1009	      - 8.7
1010	      - 5.9
1011	      - 32%
1012	      - 0.78
1013	      - 0.85
1014	    - - 50
1015	      - 5.4
1016	      - 4.4
1017	      - 19%
1018	      - 0.86
1019	      - 0.89
1020	    - - 100
1021	      - 4.3
1022	      - 4.1
1023	      - 5%
1024	      - 0.9
1025	      - 0.91
1026	    - - 200
1027	      - 3.9
1028	      - 3.8
1029	      - 3%
1030	      - 0.93
1031	      - 0.93
1032	  figures_description:
1033	  - 'Fig: MAE vs N (log scale). Two curves: naive (steep decline) and GP (flatter,
1034	    starting lower). Converge around N=100-200. Dashed line at MAE=6pp marking usability
1035	    threshold.'
1036	  - 'Fig: γ relative bias vs N. Same two-curve pattern. GP consistently lower bias.'
1037	  analysis: 'GP策略is a genuine contribution for median tier——它将practical applicability
1038	    扩展到小样本场景。N=20 GP MAE=5.9pp刚好在median acceptable range， 回应reviewer concern "too
1039	    few models"。 论文framing：Section 4.x "Practical Considerations: Few-Examinee Regime"，
1040	    展示GP as recommended practice when N<50。 但需诚实：N=20仍比N=100差(5.9 vs 4.1pp)，GP不是magic
1041	    bullet。
1042	
1043	    '
1044	- name: observational_72b
1045	  plan_id: exp-012
1046	  description: 'Qwen2.5-72B observational analysis (inference only)。Frontier scale
1047	    ecological validity。
1048	
1049	    '
1050	  expected_results:
1051	    self_critique_auc_72b_estimated: 0.61
1052	    constat_auc_72b_estimated: 0.55
1053	    gamma_posterior_mean_72b: 0.1
1054	    gamma_95ci: '[-0.09, 0.30]'
1055	    gamma_95ci_excludes_zero: false
1056	    theta_ci_width_95_pp: 14.8
1057	    calibration_adjustment_pp: 2.1
1058	    gamma_72b_vs_7b_instruct_difference: -0.04
1059	    ranking_consistency_with_smaller: true
1060	  result_rationale: 'Median档下72B observational是最弱的data point。原因：(1) 仅有Self-Critique和
1061	    ConStat可用(closed-weight限制embed/MinK)，AUC约0.55-0.61——接近chance。 (2) 单一模型(N=1 for
1062	    this scale)使IRT估计极度依赖item-level variation。 (3) γ posterior CI包含0——无法conclude contamination
1063	    effect。
1064	
1065	    但γ point estimate(0.10)较低且calibration adjustment小(2.1pp)—— 与72B模型更大training corpus下contamination"稀释"一致。
1066	    排名与smaller models一致(no scale-specific anomaly)。
1067	
1068	    论文定位：一段discussion + appendix table。不能support quantitative claims， 仅提供"no evidence
1069	    of scale regression"的directional observation。
1070	
1071	    '
1072	  tables:
1073	  - name: 'Table: 72B Observational Results'
1074	    columns:
1075	    - metric
1076	    - value
1077	    rows:
1078	    - - Self-Critique AUC (est.)
1079	      - 0.61
1080	    - - γ posterior mean
1081	      - 0.1
1082	    - - γ 95% CI
1083	      - '[-0.09, 0.30]'
1084	    - - Calibration adj. (pp)
1085	      - 2.1
1086	    - - θ CI width (pp)
1087	      - 14.8
1088	  figures_description:
1089	  - 'Fig: γ posterior for 72B added to forest plot from exp-009. Widest CI among all
1090	    models, centered near zero.'
1091	  analysis: '72B data point is weak but not harmful。γ CI包含0，无法claim或refute contamination。论文可以说"extending
1092	    to 72B, we observe no evidence of scale-specific artifacts, though signal quality
1093	    at this scale limits definitive conclusions"。P2 priority justified——nice to have,
1094	    not essential。
1095	
1096	    '
1097	- name: closed_weight_2signal_mode
1098	  plan_id: exp-013
1099	  description: '2-signal degraded mode (ConStat + Self-Critique)。量化vs 4-signal calibration
1100	    gap。
1101	
1102	    '
1103	  expected_results:
1104	    two_signal_rrf_auc: 0.7
1105	    mae_2signal_avg: 5.4
1106	    mae_2signal_mmlu: 4.3
1107	    mae_2signal_gsm8k: 6.5
1108	    mae_2signal_arc: 4.9
1109	    mae_2signal_humaneval: 6.8
1110	    ci_coverage_95_2signal: 0.85
1111	    ci_width_95_pp_2signal: 13.8
1112	    kendall_tau_2signal: 0.68
1113	    mae_increase_relative: 0.29
1114	    coverage_decrease: 0.04
1115	    ci_width_increase_pp: 3.0
1116	    tau_decrease: 0.1
1117	    degradation_worst_benchmark: HumanEval
1118	    degradation_worst_mae_increase: 1.2
1119	  result_rationale: 'Median档2-signal degradation约29%相对MAE增加，在[0.15, 0.35]范围中段。 Composite
1120	    AUC从0.78降至0.70——恰好在identifiability threshold边缘。 MAE从4.2升至5.4pp——仍然functional但不impressive。
1121	
1122	    降级对HumanEval打击最大(5.6→6.8pp)因为code benchmarks的两个surviving signals 都最弱(ConStat和Self-Critique在HumanEval
1123	    AUC最低)。MMLU降级最小(3.4→4.3pp) 因为即使只用两个信号MMLU的MC格式仍提供较好的ConStat performance gap。
1124	
1125	    Coverage从0.89降至0.85——低于nominal但仍>0.80。CI从10.8宽到13.8pp—— 接近"不太有用"的boundary(15pp)但还没到。
1126	
1127	    Kendall τ降至0.68——model ranking reliability受影响，3-4个model pairs可能错序。 这限制了2-signal
1128	    mode在competitive benchmarking(排名靠前的模型精确排序) 中的应用，但对"flagging severely contaminated
1129	    models"仍有价值。
1130	
1131	    '
1132	  tables:
1133	  - name: 'Table: 2-Signal vs 4-Signal Calibration'
1134	    columns:
1135	    - metric
1136	    - 4-signal
1137	    - 2-signal
1138	    - degradation
1139	    rows:
1140	    - - RRF AUC
1141	      - 0.78
1142	      - 0.7
1143	      - '-0.08'
1144	    - - MAE avg (pp)
1145	      - 4.2
1146	      - 5.4
1147	      - +1.2 (29%)
1148	    - - Coverage 95%
1149	      - 0.89
1150	      - 0.85
1151	      - '-0.04'
1152	    - - CI width (pp)
1153	      - 10.8
1154	      - 13.8
1155	      - '+3.0'
1156	    - - Kendall τ
1157	      - 0.78
1158	      - 0.68
1159	      - '-0.10'
1160	  - name: 'Table: 2-Signal MAE by Benchmark'
1161	    columns:
1162	    - benchmark
1163	    - 4-signal MAE
1164	    - 2-signal MAE
1165	    - delta
1166	    rows:
1167	    - - MMLU
1168	      - 3.4
1169	      - 4.3
1170	      - 0.9
1171	    - - GSM8K
1172	      - 5.1
1173	      - 6.5
1174	      - 1.4
1175	    - - ARC-C
1176	      - 3.8
1177	      - 4.9
1178	      - 1.1
1179	    - - HumanEval
1180	      - 5.6
1181	      - 6.8
1182	      - 1.2
1183	  figures_description:
1184	  - 'Fig: Paired bar chart showing 4-signal vs 2-signal MAE across benchmarks. Gap
1185	    visible but not catastrophic.'
1186	  - 'Fig: CI width comparison violin plot. 2-signal distribution shifted right with
1187	    longer upper tail.'
1188	  analysis: 2-signal mode functional但clearly inferior。29% MAE degradation是 "graceful
1189	    degradation"的上限——再去掉一个信号(1-signal)会cross usability boundary。论文framing：2-signal
1190	    mode作为"accessible fallback for closed-weight evaluation, with explicit performance
1191	    penalty disclosure"。 不应claim 2-signal mode等效于4-signal。 建议在paper中加warning box："2-signal
1192	    mode is recommended only when model internals are unavailable. Users should expect
1193	    ~30% higher calibration error and wider confidence intervals."
1194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e300c7b6-c02e-4ef1-abfb-8e9f360404f9",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "27039fd5-b7d1-44bf-9ca3-408743df1c6e",
  "sourceToolAssistantUUID": "e300c7b6-c02e-4ef1-abfb-8e9f360404f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T16:43:06.263Z_

<details open><summary>🔧 Tool call — Read · `toolu_011F8ynUoZVvEmcK8idgd5wE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27039fd5-b7d1-44bf-9ca3-408743df1c6e",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuK8LpPWWjR1py2pdoH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb6accf4-e5ac-4b04-a625-19482b8a4612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDqDs2vZVrQhS9jjwq9wa1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3548,
      "cache_read_input_tokens": 24428,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 24428,
          "cache_creation_input_tokens": 3548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3548,
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

_source line 36 · 2026-05-13T16:43:06.690Z_

<details><summary>↩ Tool result · `toolu_011F8ynUoZVvEmcK8idgd5wE`</summary>

```text
1	tier: median
2	narrative_guidance: 'Claims需要降级修饰。Claim 1加条件限定："在检测信号AUC≥0.70的SFT regime下有效校准"， 不再claim跨regime通用性。Claim
3	  2从"outperforming any single signal"弱化为 "robust aggregation with graceful degradation"，重心移向鲁棒性而非优越性。
4	  Claim 3的RL部分从"appropriately wider intervals"改为诚实承认CIs过宽时的实用性边界， 用simulation identifiability
5	  bounds来定义"minimum useful signal quality"。 需要补充实验：(a) exp-011 few-examinee regime证明Growing
6	  Pains预估策略能改善小样本表现， (b) exp-010 prior sensitivity证明结果非prior-driven。 论文叙事从"general
7	  calibration framework"调整为"principled calibration under sufficient signal quality,
8	  with explicit identifiability guarantees"。 仍投AAAI，但方法论贡献权重从calibration accuracy转向identifiability
9	  analysis。
10	
11	  '
12	imagined_experiments:
13	- name: controlled_sft_injection
14	  plan_id: exp-001
15	  description: 'Qwen2.5-0.5B/1.5B/3B 在 5 个 dosage (0%/5%/25%/50%/100%) 下的 SFT 注入。
16	    15 runs 产出 ground-truth contaminated/clean model pairs。
17	
18	    '
19	  expected_results:
20	    mmlu_inflation_100pct_0.5B: 11.2
21	    mmlu_inflation_100pct_1.5B: 9.4
22	    mmlu_inflation_100pct_3B: 7.8
23	    gsm8k_inflation_100pct_0.5B: 14.6
24	    gsm8k_inflation_100pct_1.5B: 12.1
25	    gsm8k_inflation_100pct_3B: 10.3
26	    arc_inflation_100pct_0.5B: 8.7
27	    arc_inflation_100pct_1.5B: 7.2
28	    arc_inflation_100pct_3B: 6.1
29	    humaneval_inflation_100pct_0.5B: 9.8
30	    humaneval_inflation_100pct_1.5B: 8.5
31	    humaneval_100pct_3B: 7.0
32	    mmlu_inflation_5pct_avg: 1.8
33	    gsm8k_inflation_5pct_avg: 2.4
34	    dose_response_spearman_mmlu: 0.98
35	    dose_response_spearman_gsm8k: 0.92
36	    dose_response_spearman_arc: 0.96
37	    dose_response_spearman_humaneval: 0.88
38	    sft_loss_converged_fraction: 1.0
39	    clean_sft_accuracy_degradation_max_pp: 0.8
40	  result_rationale: 'Median档下SFT injection按预期产生系统性inflation。较小模型(0.5B)inflation更大，
41	    因为base能力低、SFT对记忆benchmark items的relative gain更高。GSM8K inflation 最大因为free-form格式下memorization直接消除reasoning需求。HumanEval的
42	    dose-response不完美(Spearman=0.88)，因代码生成的execution-based评估部分抵消了 记忆效应——背下答案但execution环境稍有差异导致100%
43	    dosage不一定比50%高。 5% dosage inflation小但非零(1.8-2.4pp)，为后续检测设置了"低信号"基准。
44	
45	    '
46	  tables:
47	  - name: 'Table: Score Inflation by Dosage and Scale'
48	    columns:
49	    - model
50	    - benchmark
51	    - 0%
52	    - 5%
53	    - 25%
54	    - 50%
55	    - 100%
56	    rows:
57	    - - Qwen2.5-0.5B
58	      - MMLU
59	      - 42.1
60	      - 43.9
61	      - 48.3
62	      - 50.7
63	      - 53.3
64	    - - Qwen2.5-0.5B
65	      - GSM8K
66	      - 18.3
67	      - 20.7
68	      - 26.1
69	      - 29.4
70	      - 32.9
71	    - - Qwen2.5-0.5B
72	      - ARC-C
73	      - 35.8
74	      - 36.9
75	      - 40.2
76	      - 42.1
77	      - 44.5
78	    - - Qwen2.5-0.5B
79	      - HumanEval
80	      - 12.2
81	      - 13.4
82	      - 17.1
83	      - 19.8
84	      - 22.0
85	    - - Qwen2.5-1.5B
86	      - MMLU
87	      - 56.4
88	      - 57.8
89	      - 61.2
90	      - 63.1
91	      - 65.8
92	    - - Qwen2.5-1.5B
93	      - GSM8K
94	      - 38.7
95	      - 40.4
96	      - 45.3
97	      - 48.0
98	      - 50.8
99	    - - Qwen2.5-1.5B
100	      - ARC-C
101	      - 48.2
102	      - 49.1
103	      - 52.0
104	      - 53.6
105	      - 55.4
106	    - - Qwen2.5-1.5B
107	      - HumanEval
108	      - 26.8
109	      - 28.0
110	      - 31.4
111	      - 33.2
112	      - 35.3
113	    - - Qwen2.5-3B
114	      - MMLU
115	      - 64.7
116	      - 65.8
117	      - 68.4
118	      - 70.1
119	      - 72.5
120	    - - Qwen2.5-3B
121	      - GSM8K
122	      - 52.1
123	      - 53.6
124	      - 57.2
125	      - 59.5
126	      - 62.4
127	    - - Qwen2.5-3B
128	      - ARC-C
129	      - 55.3
130	      - 56.1
131	      - 58.6
132	      - 60.0
133	      - 61.4
134	    - - Qwen2.5-3B
135	      - HumanEval
136	      - 35.4
137	      - 36.2
138	      - 39.0
139	      - 40.8
140	      - 42.4
141	  figures_description:
142	  - 'Fig: Dose-response curves (4 panels for 4 benchmarks). X=dosage%, Y=accuracy.
143	    3 lines per panel (scales). MMLU/ARC near-linear; GSM8K slightly convex (saturation
144	    at high dose); HumanEval with visible non-monotonicity at 50→100% for 0.5B.'
145	  analysis: 'Injection成功产生可控contamination。关键观察：(1) inflation magnitude随scale递减， 与模型base能力挤占记忆增益一致。(2)
146	    GSM8K inflation最大但dose-response 仍单调(Spearman>0.9)。(3) HumanEval在0.5B上100% dosage略低于预期——
147	    execution-based eval的pass@1对记忆错误更敏感。(4) Clean SFT(0% dosage) 无显著退化(<1pp)，确保ground
148	    truth baseline可靠。 这组数据为exp-002/003/006提供了足够的contamination variation。
149	
150	    '
151	- name: stage1_signal_pipeline
152	  plan_id: exp-002
153	  description: '在exp-001全部模型上计算4个检测信号：embedding retrieval, Min-K%++, ConStat, Self-Critique。输出per-model-item
154	    exposure scores。
155	
156	    '
157	  expected_results:
158	    embedding_retrieval_auc_sft: 0.82
159	    minkpp_auc_sft: 0.78
160	    constat_auc_sft: 0.74
161	    self_critique_auc_sft: 0.68
162	    embedding_auc_mmlu: 0.85
163	    embedding_auc_gsm8k: 0.79
164	    embedding_auc_arc: 0.83
165	    embedding_auc_humaneval: 0.76
166	    minkpp_auc_mmlu: 0.81
167	    minkpp_auc_gsm8k: 0.75
168	    minkpp_auc_arc: 0.79
169	    minkpp_auc_humaneval: 0.72
170	    constat_auc_mmlu: 0.77
171	    constat_auc_gsm8k: 0.72
172	    constat_auc_arc: 0.75
173	    constat_auc_humaneval: 0.68
174	    self_critique_auc_mmlu: 0.71
175	    self_critique_auc_gsm8k: 0.65
176	    self_critique_auc_arc: 0.69
177	    self_critique_auc_humaneval: 0.63
178	    corr_embed_minkpp: 0.58
179	    corr_embed_constat: 0.42
180	    corr_embed_selfcritique: 0.31
181	    corr_minkpp_constat: 0.47
182	    corr_minkpp_selfcritique: 0.29
183	    corr_constat_selfcritique: 0.38
184	    fpr_at_tpr80_embedding: 0.14
185	    fpr_at_tpr80_minkpp: 0.18
186	    fpr_at_tpr80_constat: 0.22
187	    fpr_at_tpr80_selfcritique: 0.28
188	  result_rationale: 'Median档下，检测信号AUC在0.70-0.80整体范围。Embedding retrieval最强(0.82)因为
189	    SFT injection用paraphrases仍保留semantic proximity。Min-K%++次之(0.78)因为 SFT直接影响token-level
190	    log-probabilities。ConStat第三(0.74)因为original vs paraphrase performance gap需要足够dosage才稳定。Self-Critique最弱(0.68)因为
191	    entropy-based信号本质上noise更大——但它是唯一不依赖logits/embeddings的信号， 对closed-weight场景有独占价值。HumanEval各信号AUC最低：代码生成的
192	    token分布更irregular，embedding space对code的semantic retrieval效果较差。 信号间中等相关(0.29-0.58)确认它们捕获不同维度的contamination
193	    evidence， 为RRF fusion提供互补性基础。
194	
195	    '
196	  tables:
197	  - name: 'Table: Detection Signal AUC by Benchmark (SFT regime)'
198	    columns:
199	    - signal
200	    - MMLU
201	    - GSM8K
202	    - ARC-C
203	    - HumanEval
204	    - avg
205	    rows:
206	    - - Embedding Retrieval
207	      - 0.85
208	      - 0.79
209	      - 0.83
210	      - 0.76
211	      - 0.82
212	    - - Min-K%++
213	      - 0.81
214	      - 0.75
215	      - 0.79
216	      - 0.72
217	      - 0.78
218	    - - ConStat
219	      - 0.77
220	      - 0.72
221	      - 0.75
222	      - 0.68
223	      - 0.74
224	    - - Self-Critique
225	      - 0.71
226	      - 0.65
227	      - 0.69
228	      - 0.63
229	      - 0.68
230	  - name: 'Table: Inter-signal Spearman Correlation'
231	    columns:
232	    - signal_pair
233	    - correlation
234	    rows:
235	    - - Embed × MinK++
236	      - 0.58
237	    - - Embed × ConStat
238	      - 0.42
239	    - - Embed × SelfCrit
240	      - 0.31
241	    - - MinK++ × ConStat
242	      - 0.47
243	    - - MinK++ × SelfCrit
244	      - 0.29
245	    - - ConStat × SelfCrit
246	      - 0.38
247	  figures_description:
248	  - 'Fig: 4×4 heatmap of signal AUC across benchmarks. Color gradient yellow-to-red.
249	    Embedding top-left consistently darkest; HumanEval column consistently lightest.'
250	  - 'Fig: ROC curves per signal (one panel per benchmark). Shows clear separation
251	    between Embedding(best) and SelfCritique(worst) with MinK++/ConStat in between.'
252	  analysis: '信号质量验证了median假设：平均AUC在0.68-0.82范围，整体RRF输入AUC约0.75。 关键发现：(1) 信号间相关性中等偏低(avg≈0.41)，互补性足够支撑RRF。
253	    (2) HumanEval是最难检测的benchmark，所有信号AUC低4-9pp。 (3) Self-Critique的AUC(0.68)低于其他但仍>0.60，符合median预期。
254	    (4) 0% dosage FPR可控(14-28% at TPR=80%)，不会严重污染RRF输入。
255	
256	    '
257	- name: rrf_aggregation_ablation
258	  plan_id: exp-003
259	  description: 'RRF fusion及消融实验。比较RRF vs equal-weight, single-signal, calibration-weighted
260	    RRF, FP injection robustness, 2-signal degraded mode。
261	
262	    '
263	  expected_results:
264	    rrf_4signal_auc: 0.78
265	    equal_weight_avg_auc: 0.76
266	    calibration_weighted_rrf_auc: 0.77
267	    best_single_signal_auc: 0.75
268	    second_best_single_auc: 0.72
269	    worst_single_signal_auc: 0.63
270	    degraded_2signal_auc: 0.7
271	    delta_auc_rrf_vs_best_single: 0.03
272	    rrf_auc_after_10pct_fp: 0.75
273	    rrf_auc_after_20pct_fp: 0.72
274	    rrf_auc_mmlu: 0.82
275	    rrf_auc_gsm8k: 0.75
276	    rrf_auc_arc: 0.8
277	    rrf_auc_humaneval: 0.72
278	    rrf_precision_at_20: 0.71
279	    best_single_precision_at_20: 0.66
280	  result_rationale: 'Median档核心特征：RRF优于best single signal但ΔAUC仅0.03。原因在于 信号AUC本身在0.68-0.82范围——并非极低(此时aggregation大幅增益)也非极高
281	    (此时ceiling限制增益)。四个信号的互补性(avg correlation≈0.41)提供了 理论上的融合空间，但实际上Embedding Retrieval已是dominant
282	    signal(AUC=0.82)， 其余三个信号的incremental information有限。Equal-weight averaging(0.76)
283	    接近RRF(0.78)因为信号质量差异不大到需要rank-based down-weighting。 Calibration-weighted RRF(0.77)反而略低于vanilla
284	    RRF——过拟合少量 calibration data。2-signal degraded mode(ConStat+SelfCrit)AUC=0.70，
285	    损失明显但仍在median认为"可用"的AUC≥0.70阈值边缘。 FP injection显示RRF对噪声有中等鲁棒性：10% FP仅降3pp，20% FP降6pp。
286	
287	    '
288	  tables:
289	  - name: 'Table: Aggregation Method Comparison'
290	    columns:
291	    - method
292	    - AUC
293	    - Prec@20%
294	    - notes
295	    rows:
296	    - - RRF (4 signals)
297	      - 0.78
298	      - 0.71
299	      - ''
300	    - - Equal-weight rank avg
301	      - 0.76
302	      - 0.68
303	      - ''
304	    - - Calib-weighted RRF
305	      - 0.77
306	      - 0.69
307	      - slight overfit
308	    - - Best single (Embedding)
309	      - 0.75
310	      - 0.66
311	      - ''
312	    - - Min-K%++ only
313	      - 0.72
314	      - 0.62
315	      - ''
316	    - - ConStat only
317	      - 0.68
318	      - 0.57
319	      - ''
320	    - - Self-Critique only
321	      - 0.63
322	      - 0.51
323	      - ''
324	    - - 2-signal degraded
325	      - 0.7
326	      - 0.59
327	      - ConStat+SelfCrit
328	  - name: 'Table: FP Injection Robustness'
329	    columns:
330	    - fp_rate_injected
331	    - rrf_auc
332	    - delta_from_clean
333	    rows:
334	    - - 0%
335	      - 0.78
336	      - 0.0
337	    - - 10%
338	      - 0.75
339	      - -0.03
340	    - - 20%
341	      - 0.72
342	      - -0.06
343	    - - 30%
344	      - 0.67
345	      - -0.11
346	  figures_description:
347	  - 'Fig: Bar chart of AUC for each aggregation method. RRF slightly above others,
348	    but confidence intervals overlap with equal-weight. Clear gap between 4-signal
349	    and single-signal methods.'
350	  - 'Fig: FP injection robustness curve. X=injected FP rate, Y=AUC. Smooth degradation,
351	    no cliff effect.'
352	  analysis: 'RRF的优势存在但modest(ΔAUC=0.03)。这直接影响Claim 2的framing： 不应claim "outperforming
353	    any single signal" 而应强调 "robust aggregation"—— RRF的真正价值在FP robustness和2-signal
354	    fallback而非peak AUC。 2-signal mode AUC=0.70恰好在identifiability阈值边缘，需要在论文中 明确标注"minimum
355	    recommended configuration"。 Calibration-weighted RRF表现不如vanilla RRF，支持"meta-circularity
356	    avoidance" 的设计选择——无需训练信号权重。
357	
358	    '
359	- name: noise_propagation_analysis
360	  plan_id: exp-005
361	  description: '校准噪声注入实验。估计Self-Critique FP/FN率，注入matched/1.5×/2×高斯噪声， 重新拟合IRT并量化CI
362	    widening。
363	
364	    '
365	  expected_results:
366	    self_critique_fpr_estimated: 0.25
367	    self_critique_fnr_estimated: 0.32
368	    gamma_ci_width_matched_noise: 0.42
369	    gamma_ci_width_1.5x_noise: 0.58
370	    gamma_ci_width_2x_noise: 0.78
371	    gamma_ci_width_clean_exposure: 0.31
372	    theta_ci_width_matched_noise_pp: 9.2
373	    theta_ci_width_1.5x_noise_pp: 12.1
374	    theta_ci_width_2x_noise_pp: 15.8
375	    theta_ci_width_clean_exposure_pp: 7.4
376	    gamma_bias_matched_noise: 0.04
377	    gamma_bias_1.5x_noise: 0.08
378	    gamma_bias_2x_noise: 0.14
379	    coverage_95_matched: 0.91
380	    coverage_95_1.5x: 0.89
381	    coverage_95_2x: 0.86
382	    measurement_error_model_coverage_2x: 0.92
383	  result_rationale: 'Median档下noise propagation体现为：matched noise使CI从7.4pp宽到9.2pp(+24%)，
384	    这是合理的——exposure scores的测量误差传递到posterior但被Bayesian框架部分吸收。 2× noise时CI宽到15.8pp，逼近"not
385	    practically useful"的边界。 γ point estimate在matched noise下bias很小(0.04)，但2× noise下bias升至0.14——
386	    显示极端噪声不仅增加variance还引入bias(因为噪声对contaminated和clean items 的影响不对称)。Coverage在2× noise下降至0.86——低于nominal
387	    0.95但仍>0.80， 说明model misspecification(未建模heteroscedastic noise)有代价但不灾难性。 Measurement
388	    error model extension能将2× noise coverage恢复至0.92， 表明显式建模noise是可行改进方向。
389	
390	    '
391	  tables:
392	  - name: 'Table: Noise Propagation Effects'
393	    columns:
394	    - noise_level
395	    - gamma_CI_width
396	    - theta_CI_pp
397	    - gamma_bias
398	    - coverage_95
399	    rows:
400	    - - Clean exposure
401	      - 0.31
402	      - 7.4
403	      - 0.0
404	      - 0.94
405	    - - Matched (1×)
406	      - 0.42
407	      - 9.2
408	      - 0.04
409	      - 0.91
410	    - - 1.5×
411	      - 0.58
412	      - 12.1
413	      - 0.08
414	      - 0.89
415	    - - 2×
416	      - 0.78
417	      - 15.8
418	      - 0.14
419	      - 0.86
420	    - - 2× + meas. error model
421	      - 0.65
422	      - 13.4
423	      - 0.06
424	      - 0.92
425	  figures_description:
426	  - 'Fig: Noise level (x) vs CI width (y) for γ and θ. Two panels. Near-linear growth,
427	    with measurement error model line showing partial mitigation at high noise.'
428	  - 'Fig: Coverage vs noise level. Declining line from 0.94 to 0.86; measurement error
429	    model line stays above 0.90.'
430	  analysis: '核心结论：Bayesian框架在matched noise下表现稳健(coverage 0.91, CI合理宽)， 但2× noise处于实用性边界。这直接为Claim
431	    3定义了操作条件： "当检测信号FPR>25%且FNR>30%(即AUC<0.65)时，CI宽度超过15pp， calibrated score的决策价值有限。"  Measurement
432	    error model是值得mention但非paper核心贡献的extension。
433	
434	    '
435	- name: irt_calibration_and_baselines
436	  plan_id: exp-006
437	  description: '4PL+γ IRT拟合与5个baseline对比。5个评估metric。核心实验。
438	
439	    '
440	  expected_results:
441	    calibration_mae_pp_avg: 4.2
442	    calibration_mae_pp_mmlu: 3.4
443	    calibration_mae_pp_gsm8k: 5.1
444	    calibration_mae_pp_arc: 3.8
445	    calibration_mae_pp_humaneval: 5.6
446	    ci_coverage_95_avg: 0.89
447	    ci_coverage_80_avg: 0.76
448	    ci_coverage_50_avg: 0.48
449	    ci_width_95_pp_avg: 10.8
450	    ci_width_95_pp_mmlu: 8.9
451	    ci_width_95_pp_gsm8k: 12.4
452	    ci_width_95_pp_arc: 9.6
453	    ci_width_95_pp_humaneval: 13.2
454	    kendall_tau_avg: 0.78
455	    kendall_tau_mmlu: 0.84
456	    kendall_tau_gsm8k: 0.73
457	    kendall_tau_arc: 0.81
458	    kendall_tau_humaneval: 0.71
459	    dose_response_spearman_avg: 0.83
460	    dose_response_spearman_mmlu: 0.92
461	    dose_response_spearman_gsm8k: 0.78
462	    dose_response_spearman_arc: 0.88
463	    dose_response_spearman_humaneval: 0.74
464	    gamma_posterior_mean_100pct_dose: 0.38
465	    gamma_posterior_mean_50pct_dose: 0.22
466	    gamma_posterior_mean_25pct_dose: 0.11
467	    gamma_posterior_mean_5pct_dose: 0.04
468	    gamma_95ci_excludes_zero_at_25pct: true
469	    gamma_95ci_excludes_zero_at_5pct: false
470	    gamma_rel_bias_vs_ground_truth: 0.14
471	    theta_gamma_posterior_corr: 0.38
472	    theta_corr_with_ground_truth: 0.87
473	    max_rhat: 1.008
474	    divergent_pct: 0.3
475	    ess_bulk_min: 380
476	    fit_time_sec_per_benchmark: 2400
477	    baseline_remove_rescore_mae: 5.8
478	    baseline_single_2pl_gamma_mae: 5.4
479	    baseline_vanilla_4pl_mae: 7.1
480	    baseline_linear_regression_ci_mae: 4.9
481	    baseline_emperor_mitigation_mae: 8.2
482	    margin_over_best_baseline_mae_relative: 0.14
483	    baseline_linear_regression_ci_coverage_95: 0.83
484	    baseline_single_2pl_gamma_coverage_95: 0.81
485	    baseline_vanilla_4pl_coverage_95: 0.72
486	  result_rationale: 'Median档核心特征：4PL+γ MAE=4.2pp，优于baselines但linear regression+CI
487	    紧随(MAE=4.9pp, margin仅14%)。MMLU表现最好(MAE=3.4pp)因为MC格式稳定、 检测信号强、items数多(14K)利于IRT估计。HumanEval最差(MAE=5.6pp)因为
488	    execution-based评估引入额外噪声、code embedding检测AUC低、items少(164)。 GSM8K次差(5.1pp)因free-form评估和检测信号在reasoning
489	    tasks上的弱化。
490	
491	    Coverage 89%低于nominal 95%——median档的标志性结果，说明model有轻微 misspecification(真实contamination
492	    effect非严格multiplicative, 或item parameters非严格4PL)。CI宽度10.8pp处于[8,14]区间中段。
493	
494	    Kendall τ=0.78说明calibrated ranking大致正确但有1-2个model pairs 顺序错位——dosage相近的models(如25%
495	    vs 50% on GSM8K)难以排序。
496	
497	    γ在25%+ dosage可识别(CI excludes 0)但5% dosage不行——这是median的关键limitation。 θ-γ posterior
498	    correlation=0.38反映中等confounding(能力高的模型也倾向被更多 contaminate，IRT需要disentangle但不完美)。
499	
500	    Vanilla 4PL(无γ)MAE最大(7.1pp)确认contamination建模有价值。 Emperor mitigations最差(8.2pp)确认post-hoc
501	    mitigation失效(与ICML 2025一致)。 Linear regression+CI(4.9pp)出人意料地近——在MMLU上甚至4.1pp(接近4PL+γ的3.4pp)，
502	    因为MC benchmark上contamination effect近似线性。但它的coverage仅0.83(vs 0.89)， 不确定性估计较差。
503	
504	    '
505	  tables:
506	  - name: 'Table: Calibration MAE (pp) by Method × Benchmark'
507	    columns:
508	    - method
509	    - MMLU
510	    - GSM8K
511	    - ARC-C
512	    - HumanEval
513	    - avg
514	    rows:
515	    - - 4PL+γ (ours)
516	      - 3.4
517	      - 5.1
518	      - 3.8
519	      - 5.6
520	      - 4.2
521	    - - Remove-rescore
522	      - 4.6
523	      - 7.2
524	      - 5.3
525	      - 6.8
526	      - 5.8
527	    - - Single-signal 2PL+γ
528	      - 4.2
529	      - 6.3
530	      - 5.0
531	      - 6.4
532	      - 5.4
533	    - - Vanilla 4PL
534	      - 5.8
535	      - 8.4
536	      - 6.5
537	      - 8.1
538	      - 7.1
539	    - - Linear reg. + CI
540	      - 4.1
541	      - 5.8
542	      - 4.5
543	      - 5.9
544	      - 4.9
545	    - - Emperor mitigations
546	      - 6.8
547	      - 9.7
548	      - 7.4
549	      - 9.2
550	      - 8.2
551	  - name: 'Table: Coverage and Sharpness'
552	    columns:
553	    - method
554	    - cov_50%
555	    - cov_80%
556	    - cov_95%
557	    - width_95_pp
558	    rows:
559	    - - 4PL+γ
560	      - 0.48
561	      - 0.76
562	      - 0.89
563	      - 10.8
564	    - - Linear reg. + CI
565	      - 0.42
566	      - 0.68
567	      - 0.83
568	      - 9.4
569	    - - Single-signal 2PL+γ
570	      - 0.39
571	      - 0.64
572	      - 0.81
573	      - 11.6
574	    - - Vanilla 4PL
575	      - 0.35
576	      - 0.58
577	      - 0.72
578	      - 8.2
579	  - name: 'Table: Dose-Response γ Posterior'
580	    columns:
581	    - dosage
582	    - gamma_mean
583	    - gamma_95ci_lo
584	    - gamma_95ci_hi
585	    - excludes_zero
586	    rows:
587	    - - 5%
588	      - 0.04
589	      - -0.02
590	      - 0.11
591	      - false
592	    - - 25%
593	      - 0.11
594	      - 0.02
595	      - 0.21
596	      - true
597	    - - 50%
598	      - 0.22
599	      - 0.1
600	      - 0.35
601	      - true
602	    - - 100%
603	      - 0.38
604	      - 0.23
605	      - 0.54
606	      - true
607	  figures_description:
608	  - 'Fig: MAE bar chart (6 methods × 4 benchmarks). 4PL+γ consistently lowest but
609	    linear reg close on MMLU/ARC. Vanilla 4PL and Emperor clearly worst.'
610	  - 'Fig: Coverage calibration plot: nominal level (x) vs empirical coverage (y).
611	    4PL+γ closest to diagonal but slightly below at 95%. Vanilla 4PL far below.'
612	  - 'Fig: Dose-response plot: γ posterior mean ± 95% CI vs dosage level. Monotonic
613	    increase; 5% CI includes 0.'
614	  - 'Fig: Kendall τ by benchmark: MMLU=0.84, ARC=0.81, GSM8K=0.73, HumanEval=0.71.'
615	  analysis: '4PL+γ是最佳方法但优势不dramatic——median的标志性结论。三个层面的implication： (1) vs Linear
616	    reg: IRT的额外复杂度justified(coverage 89% vs 83%, 正确的uncertainty 是核心contribution)但MAE
617	    gain modest(14%相对改善)。论文需强调uncertainty quality 而非point estimate accuracy。 (2) vs
618	    Vanilla 4PL: γ建模确认有价值(MAE 4.2 vs 7.1)，这是最clean的ablation。 (3) Claim 1需条件限定：在MMLU/ARC上MAE
619	    3-4pp可以claim"有效校准"； 在GSM8K/HumanEval上5-6pp需诚实报告并讨论limitation。 γ在5% dosage不可识别，论文应明确标注minimum
620	    detectable effect。
621	
622	    '
623	- name: scale_bridging_7b
624	  plan_id: exp-007
625	  description: 'Qwen2.5-7B SFT injection at 5 dosage levels。验证calibration scales to
626	    7B。
627	
628	    '
629	  expected_results:
630	    mmlu_inflation_100pct_7b: 6.2
631	    gsm8k_inflation_100pct_7b: 8.4
632	    arc_inflation_100pct_7b: 5.0
633	    humaneval_inflation_100pct_7b: 5.8
634	    calibration_mae_pp_7b_avg: 4.5
635	    calibration_mae_pp_7b_mmlu: 3.6
636	    calibration_mae_pp_7b_gsm8k: 5.4
637	    ci_coverage_95_7b: 0.88
638	    ci_width_95_pp_7b: 11.2
639	    kendall_tau_7b: 0.76
640	    gamma_posterior_mean_100pct_7b: 0.32
641	    theta_corr_7b: 0.86
642	    mae_difference_3b_vs_7b: 0.3
643	    scale_regression_detected: false
644	  result_rationale: 'Median档预期7B与0.5-3B结果一致(no scale regression)。7B inflation略低于 smaller
645	    models(base能力更高，SFT记忆的relative gain更小)。Calibration MAE (4.5pp)略高于3B(4.2pp)但差异不显著(0.3pp)——可能因7B
646	    SFT的LoRA rank需要 不同于smaller models、或7B的training dynamics使contamination effect less
647	    stereotyped(不完全符合4PL+γ的multiplicative assumption)。 CI coverage(0.88)和width(11.2pp)与smaller
648	    models一致。 γ posterior(0.32 at 100%)略低于smaller models(0.38)——符合"更强base model contamination
649	    effect相对更小"的直觉。No scale regression确认方法的scalability， 但不能从这一data point推断到72B+。
650	
651	    '
652	  tables:
653	  - name: 'Table: 7B vs 0.5-3B Calibration Comparison'
654	    columns:
655	    - metric
656	    - 0.5-3B avg
657	    - 7B
658	    - delta
659	    rows:
660	    - - MAE (pp)
661	      - 4.2
662	      - 4.5
663	      - 0.3
664	    - - Coverage 95%
665	      - 0.89
666	      - 0.88
667	      - -0.01
668	    - - CI width (pp)
669	      - 10.8
670	      - 11.2
671	      - 0.4
672	    - - Kendall τ
673	      - 0.78
674	      - 0.76
675	      - -0.02
676	    - - γ at 100% dose
677	      - 0.38
678	      - 0.32
679	      - -0.06
680	  figures_description:
681	  - 'Fig: Scale consistency plot: MAE (y) vs model scale (x, log). Four points (0.5/1.5/3/7B).
682	    Near-flat trend with slight upward at 7B but within error bars.'
683	  analysis: '7B验证成功——无scale regression。MAE略升但在误差范围内。 论文可claim "consistent results
684	    from 0.5B to 7B" (4个scale points)。 这不能外推到72B+(需exp-012的observational data)。 γ的scale
685	    dependence(larger model→smaller γ)是interesting finding， 值得一段discussion但不影响core
686	    claims。
687	
688	    '
689	- name: signal_survival_analysis
690	  plan_id: exp-008
691	  description: '检测信号在不同training regimes下的可靠性。4 signals × 4 regimes AUC heatmap。
692	
693	    '
694	  expected_results:
695	    embed_auc_base: 0.84
696	    minkpp_auc_base: 0.8
697	    constat_auc_base: 0.76
698	    selfcrit_auc_base: 0.66
699	    embed_auc_sft_clean: 0.83
700	    minkpp_auc_sft_clean: 0.79
701	    constat_auc_sft_clean: 0.75
702	    selfcrit_auc_sft_clean: 0.65
703	    embed_auc_sft_contam: 0.82
704	    minkpp_auc_sft_contam: 0.78
705	    constat_auc_sft_contam: 0.74
706	    selfcrit_auc_sft_contam: 0.68
707	    embed_auc_rl: 0.58
708	    minkpp_auc_rl: 0.54
709	    constat_auc_rl: 0.56
710	    selfcrit_auc_rl: 0.63
711	    max_auc_drop_base_to_rl_embed: 0.26
712	    max_auc_drop_base_to_rl_minkpp: 0.26
713	    selfcrit_rl_vs_sft_delta: -0.05
714	    selfcrit_is_best_signal_in_rl: true
715	  result_rationale: 'Median档的关键结果：RL post-training严重降解Embedding(0.84→0.58)和Min-K%++
716	    (0.80→0.54)。原因：RL(GRPO/RLHF)改变了token distribution和embedding空间， 使基于原始模型logits/embeddings的检测方法失效——与fragility
717	    paper(arXiv 2510.02386) 一致。ConStat也降至0.56因为RL改变了model对original vs paraphrase items的
718	    相对表现模式。
719	
720	    Self-Critique是唯一在RL下保持有用性的信号(0.63)——虽然也从0.66降至0.63， 但降幅最小。原因：Self-Critique基于model的self-consistency/entropy而非
721	    与training data的直接比较，RL改变了能力分布但未消除"记忆性回答"的 low-entropy特征。然而0.63仍然很低——接近exp-004确定的identifiability下限。
722	
723	    SFT-clean和base几乎相同(差异<0.02)——SFT本身不降解信号， 只有contaminated SFT才改变pattern(且改变方向是增强detection)。
724	
725	    '
726	  tables:
727	  - name: 'Table: Signal × Regime AUC Heatmap'
728	    columns:
729	    - signal
730	    - base
731	    - SFT-clean
732	    - SFT-contam
733	    - RL-post
734	    rows:
735	    - - Embedding
736	      - 0.84
737	      - 0.83
738	      - 0.82
739	      - 0.58
740	    - - Min-K%++
741	      - 0.8
742	      - 0.79
743	      - 0.78
744	      - 0.54
745	    - - ConStat
746	      - 0.76
747	      - 0.75
748	      - 0.74
749	      - 0.56
750	    - - Self-Critique
751	      - 0.66
752	      - 0.65
753	      - 0.68
754	      - 0.63
755	  figures_description:
756	  - 'Fig: Heatmap (4×4). Green/yellow/red coloring. RL column dramatically red for
757	    Embed/MinK/ConStat; Self-Critique is yellow across all regimes.'
758	  - 'Fig: Bar chart grouped by regime. RL regime shows Self-Critique as tallest bar
759	    (role reversal from SFT where it''s shortest).'
760	  analysis: 'Signal survival直接支撑Claim 2的修改方向。核心narrative： (1) SFT regime下4-signal
761	    RRF有效(all AUC>0.65)。 (2) RL regime下仅Self-Critique存活(AUC=0.63)，其余3个<0.60(essentially
762	    chance+noise)。 (3) 这解释了RL case study(exp-009)为何CIs必须宽——信号质量不支持tighter inference。
763	    (4) 此heatmap升级为Supporting Contribution 5，是paper的visual highlight。 论文需明确：RRF的"graceful
764	    degradation"在RL下并非gradual——是cliff effect， 只有Self-Critique survive。
765	
766	    '
767	- name: rl_observational_case_study
768	  plan_id: exp-009
769	  description: 'RL-trained models observational case study。Self-Critique + available
770	    signals, 宽CI拟合, expected regret quantification, near-zero γ specificity check。
771	
772	    '
773	  expected_results:
774	    models_analyzed: 6
775	    self_critique_auc_rl_avg: 0.62
776	    gamma_posterior_mean_rl_avg: 0.18
777	    gamma_95ci_width_rl: 0.41
778	    gamma_95ci_excludes_zero_fraction: 0.33
779	    theta_ci_width_95_pp_rl: 17.4
780	    calibration_adjustment_pp_avg: 3.8
781	    expected_regret_uncalibrated: 0.42
782	    expected_regret_calibrated: 0.35
783	    expected_regret_remove_rescore: 0.39
784	    regret_reduction_pct: 0.17
785	    gamma_clean_benchmark_mean: 0.03
786	    gamma_clean_benchmark_95ci_includes_zero: true
787	    qwen_instruct_avg_adjustment_pp: 4.2
788	    deepseek_r1_avg_adjustment_pp: 3.1
789	    max_rhat_rl: 1.015
790	    divergent_pct_rl: 1.2
791	    ess_bulk_min_rl: 210
792	  result_rationale: 'Median档RL case study的核心特征：CIs非常宽(17.4pp)，expected regret改善 有限(17%)。原因链：Self-Critique
793	    AUC仅0.62 → γ posterior高度不确定 (CI width 0.41) → θ的counterfactual estimate也不确定 →
794	    CI width ~17pp。
795	
796	    γ仅在2/6 models的95%CI排除0——多数RL models的contamination effect 与noise不可区分。这不是方法失败而是诚实反映信号质量：当检测AUC≈0.62时，
797	    IRT正确地报告"我们不确定"。
798	
799	    Expected regret从0.42降至0.35(17%改善)——有帮助但不dramatic。 与uncalibrated相比，wide CIs至少告诉决策者"这些rankings不可靠"，
800	    避免overconfident错误选择。Remove-rescore(0.39)介于两者之间。
801	
802	    Near-zero γ specificity check通过(γ=0.03, CI包含0)——确认模型不会 在clean data上hallucinate
803	    contamination effect。
804	
805	    MCMC diagnostics marginal(Rhat=1.015, divergent 1.2%, ESS=210)—— RL regime data更noisy导致posterior
806	    geometry更难采样。可以report但不致命。
807	
808	    DeepSeek-R1 adjustment(3.1pp)小于Qwen-Instruct(4.2pp)—— 可能因为distillation保留的contamination较少或training
809	    data composition不同。
810	
811	    '
812	  tables:
813	  - name: 'Table: RL Case Study Results by Model'
814	    columns:
815	    - model
816	    - gamma_mean
817	    - gamma_95ci
818	    - theta_adj_pp
819	    - ci_width_pp
820	    rows:
821	    - - Qwen2.5-0.5B-Instruct
822	      - 0.21
823	      - '[-0.01, 0.44]'
824	      - 4.8
825	      - 18.2
826	    - - Qwen2.5-1.5B-Instruct
827	      - 0.19
828	      - '[0.02, 0.38]'
829	      - 4.5
830	      - 16.8
831	    - - Qwen2.5-3B-Instruct
832	      - 0.17
833	      - '[-0.04, 0.39]'
834	      - 3.9
835	      - 17.1
836	    - - Qwen2.5-7B-Instruct
837	      - 0.14
838	      - '[-0.06, 0.35]'
839	      - 3.6
840	      - 17.8
841	    - - DeepSeek-R1-Distill-1.5B
842	      - 0.16
843	      - '[-0.03, 0.36]'
844	      - 3.3
845	      - 16.9
846	    - - DeepSeek-R1-Distill-7B
847	      - 0.12
848	      - '[-0.08, 0.33]'
849	      - 2.8
850	      - 17.6
851	  - name: 'Table: Expected Regret (Top-3 Selection)'
852	    columns:
853	    - method
854	    - expected_regret
855	    - regret_reduction
856	    rows:
857	    - - Uncalibrated
858	      - 0.42
859	      - —
860	    - - Remove-rescore
861	      - 0.39
862	      - 7%
863	    - - Calibrated (ours)
864	      - 0.35
865	      - 17%
866	  figures_description:
867	  - 'Fig: Forest plot of γ posteriors for 6 RL models. Wide CIs, most crossing zero.
868	    Only Qwen-1.5B-Instruct clearly above zero.'
869	  - 'Fig: Expected regret comparison bar chart. Three bars: uncalibrated, remove-rescore,
870	    calibrated. Calibrated lowest but improvement modest.'
871	  - 'Fig: Specificity check: γ posterior for clean benchmark centered near zero with
872	    CI [-0.08, 0.14].'
873	  analysis: 'RL case study honest framing：CIs宽(17pp)但这是correct answer——信号质量 不支持tight
874	    inference。Expected regret 17%改善说明即使wide CIs也有决策价值 (至少flag uncertainty)，但不能claim
875	    strong calibration。
876	
877	    论文Claim 3改写：从"appropriately wider intervals"到"explicit uncertainty quantification
878	    revealing the practical limits of calibration under low-quality detection signals,
879	    with 17% expected regret reduction as the ceiling of achievable improvement"。
880	
881	    Specificity check通过是重要positive：确认γ≈0 on clean data， 方法不会false-alarm。MCMC diagnostics
882	    marginal但acceptable for observational study framing。
883	
884	    '
885	- name: prior_sensitivity
886	  plan_id: exp-010
887	  description: 'γ prior N(0,0.5)和N(0,2)下重新拟合IRT，验证对prior选择的鲁棒性。
888	
889	    '
890	  expected_results:
891	    mae_prior_default: 4.2
892	    coverage_95_prior_default: 0.89
893	    gamma_mean_prior_default: 0.38
894	    mae_prior_tight: 4.6
895	    coverage_95_prior_tight: 0.86
896	    gamma_mean_prior_tight: 0.31
897	    gamma_shrinkage_tight: 0.18
898	    ci_width_95_pp_tight: 9.8
899	    mae_prior_wide: 4.4
900	    coverage_95_prior_wide: 0.91
901	    gamma_mean_prior_wide: 0.42
902	    ci_width_95_pp_wide: 12.6
903	    max_mae_delta_across_priors: 0.4
904	    max_gamma_delta_across_priors: 0.11
905	    ranking_kendall_tau_default_vs_tight: 0.94
906	    ranking_kendall_tau_default_vs_wide: 0.96
907	  result_rationale: 'Median档prior sensitivity结果：N(0,0.5)将γ shrink 18%(0.38→0.31)使MAE
908	    从4.2升至4.6pp——tight prior regularization过度抑制了contamination correction， 但degradation温和(<0.5pp)。N(0,2)使γ略增(0.42)和CI略宽(12.6pp
909	    vs 10.8pp)， MAE paradoxically增至4.4pp——wider prior允许更多posterior variance导致 point
910	    estimate less precise。
911	
912	    关键robustness指标：max MAE delta仅0.4pp(across priors)，rankings近乎不变 (τ>0.94)。这说明calibrated
913	    score和model ranking对prior选择robust， 虽然具体CI width有~3pp variation。Coverage与prior
914	    correlates correctly： wider prior→wider CI→better coverage(0.91 vs 0.86)。
915	
916	    足以在appendix展示"results not prior-driven"。
917	
918	    '
919	  tables:
920	  - name: 'Table: Prior Sensitivity Results'
921	    columns:
922	    - prior
923	    - MAE_pp
924	    - coverage_95
925	    - gamma_mean
926	    - CI_width_pp
927	    rows:
928	    - - N(0,0.5)
929	      - 4.6
930	      - 0.86
931	      - 0.31
932	      - 9.8
933	    - - N(0,1) default
934	      - 4.2
935	      - 0.89
936	      - 0.38
937	      - 10.8
938	    - - N(0,2)
939	      - 4.4
940	      - 0.91
941	      - 0.42
942	      - 12.6
943	  figures_description:
944	  - 'Fig: Three overlaid γ posterior densities (one per prior). Modes shift slightly;
945	    N(0,0.5) visibly tighter and leftward. All three exclude zero.'
946	  analysis: 'Prior sensitivity通过。Results robust to 4× prior variance change (σ²: 0.25→4)。MAE变化<0.5pp,
947	    ranking几乎不变。 Appendix一表一图足以回应reviewer "results prior-driven" concern。 Default
948	    N(0,1)是合理选择：tight prior underestimates γ, wide prior adds noise。
949	
950	    '
951	- name: few_examinee_regime
952	  plan_id: exp-011
953	  description: 'Simulation: IRT at model counts 20/50/100/200。Growing Pains pre-estimation策略评估。
954	
955	    '
956	  expected_results:
957	    naive_mae_n20: 8.7
958	    naive_mae_n50: 5.4
959	    naive_mae_n100: 4.3
960	    naive_mae_n200: 3.9
961	    naive_coverage_95_n20: 0.78
962	    naive_coverage_95_n50: 0.86
963	    naive_coverage_95_n100: 0.9
964	    naive_coverage_95_n200: 0.93
965	    naive_gamma_rel_bias_n20: 0.38
966	    naive_gamma_rel_bias_n50: 0.19
967	    naive_gamma_rel_bias_n100: 0.12
968	    naive_gamma_rel_bias_n200: 0.08
969	    gp_mae_n20: 5.9
970	    gp_mae_n50: 4.4
971	    gp_mae_n100: 4.1
972	    gp_mae_n200: 3.8
973	    gp_coverage_95_n20: 0.85
974	    gp_coverage_95_n50: 0.89
975	    gp_coverage_95_n100: 0.91
976	    gp_coverage_95_n200: 0.93
977	    gp_gamma_rel_bias_n20: 0.22
978	    gp_gamma_rel_bias_n50: 0.14
979	    gp_gamma_rel_bias_n100: 0.1
980	    gp_gamma_rel_bias_n200: 0.07
981	    mae_improvement_n20_pct: 0.32
982	    mae_improvement_n50_pct: 0.19
983	    mae_improvement_n100_pct: 0.05
984	    minimum_n_naive_mae_under_6pp: 50
985	    minimum_n_gp_mae_under_6pp: 20
986	  result_rationale: 'Median档few-examinee结果：N=20时naive estimation崩溃(MAE=8.7pp, coverage=0.78,
987	    γ bias=38%)——4PL+γ有太多参数(4 item params × I items + θ + γ per model) 相对于20个models严重欠定。Growing
988	    Pains pre-estimation将item params固定在 来自400+ model pool的先验上，仅估θ和γ——这将N=20 MAE从8.7pp降至5.9pp(32%改善)，
989	    coverage从0.78升至0.85。
990	
991	    但即使有GP策略，N=20的结果仍marginal(MAE=5.9pp在median范围上限)，因为 pre-estimated item params来自不同model
992	    pool，transfer assumption imperfect。 N=50时差异缩小(5.4→4.4pp, 19%)，N=100时几乎无差异(4.3→4.1pp)——
993	    充足数据时direct estimation接近GP估计。
994	
995	    关键结论：GP策略将"最小可用模型数"从50降至20，但N=20仍应被标注为 "reduced confidence"。论文可claim "practical
996	    for N≥20 with informative priors" 而非"works with any N"。
997	
998	    '
999	  tables:
1000	  - name: 'Table: Few-Examinee Regime Results'
1001	    columns:
1002	    - N_models
1003	    - naive_MAE
1004	    - GP_MAE
1005	    - improvement
1006	    - naive_cov95
1007	    - GP_cov95
1008	    rows:
1009	    - - 20
1010	      - 8.7
1011	      - 5.9
1012	      - 32%
1013	      - 0.78
1014	      - 0.85
1015	    - - 50
1016	      - 5.4
1017	      - 4.4
1018	      - 19%
1019	      - 0.86
1020	      - 0.89
1021	    - - 100
1022	      - 4.3
1023	      - 4.1
1024	      - 5%
1025	      - 0.9
1026	      - 0.91
1027	    - - 200
1028	      - 3.9
1029	      - 3.8
1030	      - 3%
1031	      - 0.93
1032	      - 0.93
1033	  figures_description:
1034	  - 'Fig: MAE vs N (log scale). Two curves: naive (steep decline) and GP (flatter,
1035	    starting lower). Converge around N=100-200. Dashed line at MAE=6pp marking usability
1036	    threshold.'
1037	  - 'Fig: γ relative bias vs N. Same two-curve pattern. GP consistently lower bias.'
1038	  analysis: 'GP策略is a genuine contribution for median tier——它将practical applicability
1039	    扩展到小样本场景。N=20 GP MAE=5.9pp刚好在median acceptable range， 回应reviewer concern "too
1040	    few models"。 论文framing：Section 4.x "Practical Considerations: Few-Examinee Regime"，
1041	    展示GP as recommended practice when N<50。 但需诚实：N=20仍比N=100差(5.9 vs 4.1pp)，GP不是magic
1042	    bullet。
1043	
1044	    '
1045	- name: observational_72b
1046	  plan_id: exp-012
1047	  description: 'Qwen2.5-72B observational analysis (inference only)。Frontier scale
1048	    ecological validity。
1049	
1050	    '
1051	  expected_results:
1052	    self_critique_auc_72b_estimated: 0.61
1053	    constat_auc_72b_estimated: 0.55
1054	    gamma_posterior_mean_72b: 0.1
1055	    gamma_95ci: '[-0.09, 0.30]'
1056	    gamma_95ci_excludes_zero: false
1057	    theta_ci_width_95_pp: 14.8
1058	    calibration_adjustment_pp: 2.1
1059	    gamma_72b_vs_7b_instruct_difference: -0.04
1060	    ranking_consistency_with_smaller: true
1061	  result_rationale: 'Median档下72B observational是最弱的data point。原因：(1) 仅有Self-Critique和
1062	    ConStat可用(closed-weight限制embed/MinK)，AUC约0.55-0.61——接近chance。 (2) 单一模型(N=1 for
1063	    this scale)使IRT估计极度依赖item-level variation。 (3) γ posterior CI包含0——无法conclude contamination
1064	    effect。
1065	
1066	    但γ point estimate(0.10)较低且calibration adjustment小(2.1pp)—— 与72B模型更大training corpus下contamination"稀释"一致。
1067	    排名与smaller models一致(no scale-specific anomaly)。
1068	
1069	    论文定位：一段discussion + appendix table。不能support quantitative claims， 仅提供"no evidence
1070	    of scale regression"的directional observation。
1071	
1072	    '
1073	  tables:
1074	  - name: 'Table: 72B Observational Results'
1075	    columns:
1076	    - metric
1077	    - value
1078	    rows:
1079	    - - Self-Critique AUC (est.)
1080	      - 0.61
1081	    - - γ posterior mean
1082	      - 0.1
1083	    - - γ 95% CI
1084	      - '[-0.09, 0.30]'
1085	    - - Calibration adj. (pp)
1086	      - 2.1
1087	    - - θ CI width (pp)
1088	      - 14.8
1089	  figures_description:
1090	  - 'Fig: γ posterior for 72B added to forest plot from exp-009. Widest CI among all
1091	    models, centered near zero.'
1092	  analysis: '72B data point is weak but not harmful。γ CI包含0，无法claim或refute contamination。论文可以说"extending
1093	    to 72B, we observe no evidence of scale-specific artifacts, though signal quality
1094	    at this scale limits definitive conclusions"。P2 priority justified——nice to have,
1095	    not essential。
1096	
1097	    '
1098	- name: closed_weight_2signal_mode
1099	  plan_id: exp-013
1100	  description: '2-signal degraded mode (ConStat + Self-Critique)。量化vs 4-signal calibration
1101	    gap。
1102	
1103	    '
1104	  expected_results:
1105	    two_signal_rrf_auc: 0.7
1106	    mae_2signal_avg: 5.4
1107	    mae_2signal_mmlu: 4.3
1108	    mae_2signal_gsm8k: 6.5
1109	    mae_2signal_arc: 4.9
1110	    mae_2signal_humaneval: 6.8
1111	    ci_coverage_95_2signal: 0.85
1112	    ci_width_95_pp_2signal: 13.8
1113	    kendall_tau_2signal: 0.68
1114	    mae_increase_relative: 0.29
1115	    coverage_decrease: 0.04
1116	    ci_width_increase_pp: 3.0
1117	    tau_decrease: 0.1
1118	    degradation_worst_benchmark: HumanEval
1119	    degradation_worst_mae_increase: 1.2
1120	  result_rationale: 'Median档2-signal degradation约29%相对MAE增加，在[0.15, 0.35]范围中段。 Composite
1121	    AUC从0.78降至0.70——恰好在identifiability threshold边缘。 MAE从4.2升至5.4pp——仍然functional但不impressive。
1122	
1123	    降级对HumanEval打击最大(5.6→6.8pp)因为code benchmarks的两个surviving signals 都最弱(ConStat和Self-Critique在HumanEval
1124	    AUC最低)。MMLU降级最小(3.4→4.3pp) 因为即使只用两个信号MMLU的MC格式仍提供较好的ConStat performance gap。
1125	
1126	    Coverage从0.89降至0.85——低于nominal但仍>0.80。CI从10.8宽到13.8pp—— 接近"不太有用"的boundary(15pp)但还没到。
1127	
1128	    Kendall τ降至0.68——model ranking reliability受影响，3-4个model pairs可能错序。 这限制了2-signal
1129	    mode在competitive benchmarking(排名靠前的模型精确排序) 中的应用，但对"flagging severely contaminated
1130	    models"仍有价值。
1131	
1132	    '
1133	  tables:
1134	  - name: 'Table: 2-Signal vs 4-Signal Calibration'
1135	    columns:
1136	    - metric
1137	    - 4-signal
1138	    - 2-signal
1139	    - degradation
1140	    rows:
1141	    - - RRF AUC
1142	      - 0.78
1143	      - 0.7
1144	      - '-0.08'
1145	    - - MAE avg (pp)
1146	      - 4.2
1147	      - 5.4
1148	      - +1.2 (29%)
1149	    - - Coverage 95%
1150	      - 0.89
1151	      - 0.85
1152	      - '-0.04'
1153	    - - CI width (pp)
1154	      - 10.8
1155	      - 13.8
1156	      - '+3.0'
1157	    - - Kendall τ
1158	      - 0.78
1159	      - 0.68
1160	      - '-0.10'
1161	  - name: 'Table: 2-Signal MAE by Benchmark'
1162	    columns:
1163	    - benchmark
1164	    - 4-signal MAE
1165	    - 2-signal MAE
1166	    - delta
1167	    rows:
1168	    - - MMLU
1169	      - 3.4
1170	      - 4.3
1171	      - 0.9
1172	    - - GSM8K
1173	      - 5.1
1174	      - 6.5
1175	      - 1.4
1176	    - - ARC-C
1177	      - 3.8
1178	      - 4.9
1179	      - 1.1
1180	    - - HumanEval
1181	      - 5.6
1182	      - 6.8
1183	      - 1.2
1184	  figures_description:
1185	  - 'Fig: Paired bar chart showing 4-signal vs 2-signal MAE across benchmarks. Gap
1186	    visible but not catastrophic.'
1187	  - 'Fig: CI width comparison violin plot. 2-signal distribution shifted right with
1188	    longer upper tail.'
1189	  analysis: 2-signal mode functional但clearly inferior。29% MAE degradation是 "graceful
1190	    degradation"的上限——再去掉一个信号(1-signal)会cross usability boundary。论文framing：2-signal
1191	    mode作为"accessible fallback for closed-weight evaluation, with explicit performance
1192	    penalty disclosure"。 不应claim 2-signal mode等效于4-signal。 建议在paper中加warning box："2-signal
1193	    mode is recommended only when model internals are unavailable. Users should expect
1194	    ~30% higher calibration error and wider confidence intervals."
1195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb6accf4-e5ac-4b04-a625-19482b8a4612",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "0179de73-83c3-4560-a325-07c11279149e",
  "sourceToolAssistantUUID": "bb6accf4-e5ac-4b04-a625-19482b8a4612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-13T16:43:10.805Z_

Now I have comprehensive context. Let me also check the best and worst tier review contexts to understand the full picture, and look for the Stan model code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0179de73-83c3-4560-a325-07c11279149e",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuKeQaHfeY6EKabauzc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c6c5d25-95d9-44f6-a3a0-e36ab80add2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBTZJWKf6wNWTNdyi2zcDt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42302,
      "cache_read_input_tokens": 27976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 42302,
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

_source line 38 · 2026-05-13T16:43:13.777Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gh4T2pCkeUb8YFq3aAmofD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/review_context.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c6c5d25-95d9-44f6-a3a0-e36ab80add2f",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuKeQaHfeY6EKabauzc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35e38804-3456-4d21-b631-599b2326bb60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBTZJWKf6wNWTNdyi2zcDt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42302,
      "cache_read_input_tokens": 27976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 42302,
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

_source line 39 · 2026-05-13T16:43:13.792Z_

<details><summary>↩ Tool result · `toolu_01Gh4T2pCkeUb8YFq3aAmofD`</summary>

```text
1	narrative_guidance: '原始framing完全成立：ContamCal是benchmark contamination的"statistical
2	  safety net"， 三条claims按原始强度表述。Headline: "ContamCal recovers true performance within
3	  2pp MAE with 93% CI coverage, while naive scores overestimate by 8-12pp." RL宽CI叙事自然成立——"wide
4	  CIs are the correct answer"用expected regret量化证明。投AAAI无需调整framing。
5	
6	  '
7	imagined_experiments:
8	- name: controlled_sft_injection
9	  plan_id: exp-001
10	  description: 'Qwen2.5-0.5B/1.5B/3B × 5 dosage levels (0%/5%/25%/50%/100%) SFT注入，
11	    生成15个contaminated/clean模型对作为ground truth。
12	
13	    '
14	  expected_results:
15	    sft_runs_completed: 15
16	    dosage_0pct_acc_delta_mmlu_pp: 0.0
17	    dosage_5pct_acc_inflation_mmlu_pp: 2.1
18	    dosage_25pct_acc_inflation_mmlu_pp: 5.8
19	    dosage_50pct_acc_inflation_mmlu_pp: 9.3
20	    dosage_100pct_acc_inflation_mmlu_pp: 12.6
21	    dosage_25pct_acc_inflation_gsm8k_pp: 4.2
22	    dosage_25pct_acc_inflation_arc_pp: 5.1
23	    dosage_25pct_acc_inflation_humaneval_pp: 7.5
24	    scale_0_5B_mean_inflation_50pct_pp: 10.8
25	    scale_1_5B_mean_inflation_50pct_pp: 9.1
26	    scale_3B_mean_inflation_50pct_pp: 8.2
27	    dose_response_spearman_across_all: 0.97
28	    convergence_failures: 0
29	  result_rationale: 'best档下SFT注入实验完全按预期工作。paraphrase-based injection在5%剂量时已产生可测量的2pp
30	    inflation， 100%剂量下MMLU膨胀达12.6pp，与Emperor''s New Clothes报告的8-15pp范围一致。 较小模型(0.5B)受contamination影响更大（memorization
31	    capacity占比更高）， 3B模型因能力更强、泛化更好而inflation略低。GSM8K因reasoning chain结构使得 memorization效果弱于纯knowledge
32	    recall的MMLU。HumanEval inflation最高因为 code solutions更容易被精确记忆。dose-response严格单调（spearman=0.97），
33	    为后续IRT建模提供理想的ground truth梯度。
34	
35	    '
36	  tables:
37	  - name: 'Table 1: Accuracy Inflation (pp) by Model Scale × Dosage × Benchmark'
38	    rows: 60
39	    columns:
40	    - model
41	    - benchmark
42	    - dosage
43	    - clean_acc
44	    - contaminated_acc
45	    - inflation_pp
46	  figures_description:
47	  - 'Fig 1: Dose-response curves (dosage vs inflation) for each model×benchmark combination,
48	    12 panels, showing strict monotonicity'
49	  analysis: '所有15个SFT run成功收敛。inflation幅度在MMLU上与文献一致。 关键观察：inflation并非线性——25%→50%的增量大于5%→25%，表明contamination效果存在加速区间，
50	    支持非线性4PL建模的必要性。跨benchmark一致性强，为Claim 1提供坚实的ground truth基础。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35e38804-3456-4d21-b631-599b2326bb60",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "18ad3edf-7018-4421-9f26-2c58b82d9dde",
  "sourceToolAssistantUUID": "35e38804-3456-4d21-b631-599b2326bb60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T16:43:14.541Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AnJGi2kDviHNVBSu37Pk17`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/contam_irt_4pl.stan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18ad3edf-7018-4421-9f26-2c58b82d9dde",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuKeQaHfeY6EKabauzc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3c69a79-af4a-491c-a4a6-d020d284e041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBTZJWKf6wNWTNdyi2zcDt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42302,
      "cache_read_input_tokens": 27976,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 42302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 27976,
          "cache_creation_input_tokens": 42302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 42302,
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

_source line 41 · 2026-05-13T16:43:14.558Z_

<details><summary>↩ Tool result · `toolu_01AnJGi2kDviHNVBSu37Pk17`</summary>

```text
1	// 4PL + gamma contamination-augmented IRT model
2	// P(y_ij = 1) = c_j + (d_j - c_j) * inv_logit(a_j * (theta_i - b_j) + gamma * exposure_ij)
3	
4	data {
5	  int&lt;lower=1> N_models;
6	  int&lt;lower=1> N_items;
7	  array[N_models, N_items] int&lt;lower=0, upper=1> y;
8	  matrix[N_models, N_items] exposure;
9	}
10	
11	parameters {
12	  vector[N_models] theta;
13	  vector&lt;lower=0>[N_items] a;
14	  vector[N_items] b;
15	  vector&lt;lower=0, upper=1>[N_items] c;
16	  vector&lt;lower=0, upper=1>[N_items] d;
17	  real gamma;
18	}
19	
20	model {
21	  // Priors
22	  theta ~ std_normal();
23	  a ~ lognormal(0, 0.5);
24	  b ~ std_normal();
25	  c ~ beta(5, 20);
26	  d ~ beta(20, 5);
27	  gamma ~ std_normal();
28	
29	  // Likelihood
30	  for (i in 1:N_models) {
31	    for (j in 1:N_items) {
32	      real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
33	      real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
34	      y[i, j] ~ bernoulli(p);
35	    }
36	  }
37	}
38	
39	generated quantities {
40	  vector[N_models * N_items] log_lik;
41	  {
42	    int idx = 0;
43	    for (i in 1:N_models) {
44	      for (j in 1:N_items) {
45	        idx += 1;
46	        real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
47	        real p = c[j] + (d[j] - c[j]) * inv_logit(eta);
48	        log_lik[idx] = bernoulli_lpmf(y[i, j] | p);
49	      }
50	    }
51	  }
52	}
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3c69a79-af4a-491c-a4a6-d020d284e041",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a1922f0e6b71081b3",
  "type": "user",
  "uuid": "980b71cc-03da-4488-9f94-a82eeea630e8",
  "sourceToolAssistantUUID": "c3c69a79-af4a-491c-a4a6-d020d284e041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-13T16:44:52.293Z_

I now have thorough context. Let me compose the R2 review focused on Novelty and Related Work.

---

## Reviewer 2 (R2) Review: Novelty and Related Work

**Paper:** "Empirical Identifiability Boundaries for Contamination-Aware IRT Calibration of LLM Benchmarks"
**Venue:** AAAI 2027

---

### Summary

The paper investigates the conditions under which contamination-aware IRT calibration of LLM benchmarks is identifiable. It augments 4PL IRT with a contamination covariate gamma, fed by RRF-fused detection signals, and uses controlled SFT injection experiments to map identifiability boundaries across signal quality, model count, and model scale. The central finding is predominantly negative: calibration is identifiable only under narrow conditions (AUC >= 0.70, N >= 80) that are rarely satisfied in practice, especially after RL post-training.

---

### Strengths

**S1. Valuable reframing of the research question.** The shift from "calibration solves contamination" to "when is calibration solvable?" is a genuinely useful contribution to the community discourse. Rather than proposing yet another method and claiming it works, the paper maps the failure modes. This is intellectually honest and fills a gap: the field has many proposed fixes but little understanding of their operating conditions. The analogy to identification conditions in causal inference is apt and well-motivated.

**S2. Systematic identifiability analysis with clear actionable thresholds.** The empirical identifiability map (signal AUC x model count x model scale) with concrete thresholds (AUC >= 0.70, N >= 80, CI width < 15pp) gives practitioners something they can actually check before deploying calibration. This is more useful than a method paper that reports average metrics without operating conditions. The simulation sweep (144 conditions, 10 seeds each in the planned exp-004) is appropriately comprehensive for establishing these boundaries.

**S3. The signal survival analysis under RL is a strong empirical finding.** Demonstrating that RL post-training degrades all 4 detection signals below the identifiability threshold (avg AUC drop from 0.72 to 0.56) -- and that this is a cliff effect rather than gradual degradation -- is an important negative result. This directly challenges the assumption underlying multiple prior works that detection signals remain reliable across training regimes. The 4x4 signal-regime AUC heatmap is a compact, informative visualization.

**S4. Principled connection to educational measurement literature.** The three structural differences identified when adapting item compromise IRT to LLMs -- (a) single model vs. independent examinees, (b) continuous vs. binary exposure, (c) regime-conditional ability -- are non-trivial and correctly identified. This cross-disciplinary transfer is substantive, not merely cosmetic. The Eckerly (2017) and Sinharay (2017) references ground the work in a well-established psychometric tradition.

**S5. Methodological transparency.** The paper honestly reports its own method's limitations: 4PL+gamma does NOT significantly outperform linear regression (7.8 vs 7.2pp MAE, p=0.23 in the summary), gamma is unidentifiable at low dosages (<= 25%), and calibration is HARMFUL for RL models. This level of candor is unusual and commendable. The prior sensitivity analysis showing 30% variation is honestly disclosed rather than buried.

---

### Weaknesses

**W1. The core methodological contribution is a synthesis of known components, and the paper does not adequately position this relative to the synthesis effort.**

The two-stage pipeline -- RRF fusion of existing detection signals, followed by 4PL IRT with an added covariate -- combines well-known building blocks. RRF is a standard rank fusion technique (Cormack et al., 2009). 4PL IRT is textbook psychometrics. Adding a covariate to IRT is standard practice in educational measurement (explanatory IRT; De Boeck & Wilson, 2004). The individual detection signals are all prior work.

The paper partially acknowledges this ("not engineering glue -- each adaptation requires non-obvious modeling decisions") but the three claimed adaptations are more incremental than portrayed:
- (a) "single model vs. independent examinees" -- this is effectively a fixed-effects IRT model, well-known in psychometrics (e.g., Mislevy, 1986)
- (b) "continuous vs. binary exposure" -- replacing a binary indicator with a continuous covariate in IRT is standard (e.g., latent regression IRT; Adams et al., 1997)
- (c) "regime-conditional ability" -- this is essentially interaction modeling, also standard

The novelty ceiling is real: the paper's primary value lies in the empirical identifiability analysis, not the method itself. The framing should reflect this more explicitly.

**W2. The reference list is strikingly thin (12 references) and misses significant related work.**

For an AAAI submission addressing contamination detection, IRT for LLMs, and Bayesian calibration, 12 references is inadequate. Several important gaps:

- *Explanatory IRT literature*: The paper uses contamination as a covariate in IRT but does not cite the explanatory IRT framework (De Boeck & Wilson, 2004; Wilson & De Boeck, 2004) or latent regression IRT (Adams, Wilson & Wu, 1997), which provide the theoretical foundation for what is being done.

- *Broader contamination detection*: Missing KDS (Knowledge Decontamination Score; Dong et al., 2024), Contamination Detection via Output Distribution (Oren et al., 2024), and the benchmark contamination survey by Balloccu et al. (2024). The paper uses 4 signals but does not justify why these 4 were selected over alternatives.

- *IRT identifiability theory*: The paper claims to study "identifiability" but does not cite the substantial psychometric literature on IRT model identifiability (e.g., San Martin et al., 2009; Maris & Bechger, 2009). These works provide formal conditions for parameter identifiability in IRT, which could ground the empirical thresholds more rigorously.

- *Concurrent work on IRT for LLMs*: The paper cites PSN-IRT, Growing Pains, ATLAS, and HiBayES but misses Polo et al. (2024, "TinyBenchmarks"), which also uses IRT for LLM evaluation with small item sets, and Gu et al. (2024, "STIRT"), which studies IRT stability across model updates.

- *Rank fusion*: RRF is used without citation. Cormack, Clarke & Buettcher (2009) should be cited.

- *Contamination-adjusted evaluation*: Li et al. (2024, "Task Contamination") and Jiang et al. (2024, "Investigating Data Contamination in Modern Benchmarks") provide contamination-aware evaluation approaches that should be discussed.

- *Bayesian model comparison and identifiability diagnostics*: The paper uses HMC in Stan but does not cite or discuss SBC (Simulation-Based Calibration; Talts et al., 2018), which is the gold standard for validating Bayesian workflow and could strengthen the identifiability analysis.

**W3. The "identifiability boundary" contribution is primarily empirical, lacking theoretical grounding.**

The paper establishes AUC >= 0.70 and N >= 80 as thresholds, but these are derived from simulation sweeps rather than theoretical analysis. Several concerns:

- Why is the threshold AUC >= 0.70 specifically? Is this an artifact of the specific 4PL parameterization, the prior choices, or something more fundamental? The 30% prior sensitivity suggests the threshold itself may be prior-dependent.

- The Fisher Information matrix provides closed-form expressions for the minimum information needed to identify parameters in IRT models. The paper could derive approximate analytical identifiability conditions rather than relying purely on simulation. This would make the contribution more generalizable.

- The gamma-theta posterior correlation (0.52 to 0.58 for larger models) suggests a fundamental confound that no amount of data resolves -- this is a structural identifiability issue, not just a finite-sample issue. The paper does not clearly distinguish structural vs. practical identifiability.

**W4. Limited ecological validity of the SFT injection paradigm.**

The controlled SFT injection (paraphrased benchmark items inserted into SFT training data) is a reasonable but limited proxy for real-world contamination:

- Real contamination often occurs through pre-training data, not SFT. The dynamics differ: pre-training exposure is diffuse (mixed with billions of tokens), while SFT exposure is concentrated. The paper does not discuss how pre-training contamination might differ in terms of signal quality and identifiability.

- The RL observational study is acknowledged as "directional" only, with CIs too wide to be informative (17.4pp). This is honest but means the paper has no validated evidence for the most practically relevant scenario (RL-post-trained production models).

- Using only Qwen2.5 models raises generalizability concerns. Other model families (Llama, Mistral, Gemma) may have different contamination response profiles. Single model family limits the external validity of the identifiability map.

**W5. The negative result, while honest, raises the question of constructive contribution.**

The paper's strongest finding is that calibration mostly does not work: it requires conditions rarely met, fails under RL, degrades with scale, and barely outperforms linear regression when it does work. While documenting failure modes is valuable, the paper could do more to chart a constructive path forward:

- Under what conditions *would* calibration become viable? What detection signal AUC would be needed for frontier models?
- Could the identifiability analysis guide the design of *better* detection signals specifically optimized for IRT identifiability rather than binary classification AUC?
- The measurement error model extension (mentioned in noise propagation analysis) recovered coverage from 0.86 to 0.92 at 2x noise -- this seems like a genuine methodological contribution that is under-developed.

---

### Missing Related Work (Specific)

1. **Explanatory IRT / Latent Regression IRT**: De Boeck & Wilson (2004), Adams et al. (1997) -- theoretical foundation for covariate-augmented IRT
2. **IRT identifiability theory**: San Martin et al. (2009), Maris & Bechger (2009) -- formal identifiability conditions
3. **RRF**: Cormack, Clarke & Buettcher (2009) -- the fusion method used without citation
4. **KDS**: Dong et al. (2024) -- prominent detection signal not included or discussed
5. **TinyBenchmarks**: Polo et al. (2024) -- IRT-based efficient LLM evaluation
6. **Contamination surveys**: Balloccu et al. (2024), "A Survey on Data Contamination"
7. **SBC**: Talts et al. (2018) -- Bayesian workflow validation
8. **LiveBench / dynamic benchmarks**: White et al. (2024) -- an alternative to post-hoc calibration that should be discussed as a competing paradigm
9. **Task Contamination**: Li et al. (2024) -- contamination-aware evaluation
10. **Explanatory item response models**: Wilson, De Boeck & Carstensen (2008) -- item covariates in IRT

---

### Questions for Authors

1. **On identifiability thresholds**: The AUC >= 0.70 threshold shows 30% prior sensitivity. Can you provide a Fisher Information-based derivation or at least a sensitivity analysis showing how this threshold changes across different 4PL parameterizations? Without this, how confident should practitioners be in applying this threshold to their specific setting?

2. **On the linear regression baseline**: The 4PL+gamma model's advantage over linear regression + bootstrap CI is marginal (7.8 vs 7.2pp MAE, p=0.23). Given the much greater computational cost of HMC fitting and the complexity of the 4PL model, under what circumstances would you recommend 4PL+gamma over simple linear regression? Is the IRT complexity justified?

3. **On pre-training contamination**: Your SFT injection paradigm assumes concentrated exposure. Have you considered or can you speculate about how your identifiability boundaries would shift for pre-training contamination, where the signal-to-noise ratio is fundamentally different?

4. **On structural identifiability**: The gamma-theta correlation of 0.52-0.58 for larger models appears to be a structural confound (more capable models may both score higher and have more training data overlap). Is this a fundamental limit of the additive gamma*s_ij formulation, or could alternative functional forms (e.g., multiplicative, threshold-based) reduce this confound?

5. **On signal selection**: Why these 4 detection signals specifically? The exclusion of KDS and other methods is not justified. Was there a principled selection criterion, or is this convenience sampling?

---

### Scores (AAAI 1-10 Scale)

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Novelty** | 5 | The "identifiability boundary" reframing is genuinely useful, but the method itself is a standard synthesis of known components. The three claimed adaptations from educational IRT are more incremental than presented. The primary novelty is in the empirical analysis, not the methodology. |
| **Significance** | 6 | The negative results (calibration rarely works, RL destroys signals, scale degrades identifiability) are important for the community to know. This could change how people think about post-hoc calibration. However, the limited constructive contribution reduces impact -- the paper tells us what does not work more than what to do about it. |
| **Related Work** | 3 | 12 references is far below the standard for a top venue. Missing the explanatory IRT literature that directly underpins the method, missing RRF citation, missing IRT identifiability theory, missing several relevant contamination detection and LLM evaluation works. This is a significant gap that undermines the paper's positioning claims. |
| **Clarity** | 7 | The "identifiability boundary" narrative is well-structured. The three-axis map (signal quality x model count x scale) is a clear organizing principle. The honest reporting of negative results is well-handled. The Stan model is clean. However, the paper would benefit from clearer distinction between structural and practical identifiability. |
| **Overall Assessment** | 5 | Below the acceptance threshold for AAAI. The reframing is valuable and the empirical analysis is thorough, but the thin related work section seriously undermines the paper's scholarly positioning. The methodological contribution is incremental (standard IRT + standard fusion), and the main finding is a well-documented negative result. With a substantially expanded related work section, theoretical grounding for the identifiability thresholds, and more constructive forward-looking analysis, this could become a solid contribution. In its current form, it reads as a thorough empirical study that does not quite reach the novelty bar for AAAI's 17.6% acceptance rate. |
| **Confidence** | 4 | I am familiar with both the IRT/psychometric literature and the LLM contamination literature, and have reviewed the experimental design in detail. My main uncertainty is whether the AAAI community would weight the "negative result" contribution more favorably than I have. |

---

### Recommendation

**Borderline Reject.** The paper addresses a timely question with an honest empirical analysis, but (1) the reference list is unacceptably thin for a top venue, (2) the methodological novelty is limited to synthesis of known techniques, and (3) the identifiability thresholds lack theoretical grounding. The strongest path to acceptance would be: expand related work to 30+ references with proper positioning against explanatory IRT and IRT identifiability theory; derive at least approximate analytical identifiability conditions via Fisher Information to complement the simulation sweep; and develop the constructive implications (signal design criteria, measurement error model extension) more fully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "980b71cc-03da-4488-9f94-a82eeea630e8",
  "isSidechain": true,
  "agentId": "a1922f0e6b71081b3",
  "requestId": "req_011CazuLEXfSjJAUk2EuyKcP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81258d2b-7a29-4665-92a5-45326ea74881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G5LpGP3xuXg838FV6M3dpS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2163,
      "cache_read_input_tokens": 70278,
      "output_tokens": 3833,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2163
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3833,
          "cache_read_input_tokens": 70278,
          "cache_creation_input_tokens": 2163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2163,
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
