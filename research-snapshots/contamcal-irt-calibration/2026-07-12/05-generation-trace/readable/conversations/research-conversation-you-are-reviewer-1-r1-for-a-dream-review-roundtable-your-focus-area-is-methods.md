# Research conversation: You are Reviewer 1 (R1) for a DREAM review roundtable. Your focus area is **Methods and Experiments**. ## Paper Details 

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5ae4aef38a931ce3.jsonl`
- **Structured JSON:** [`aaa17ab786f3ed79bc46.json`](../../sessions/aa/aaa17ab786f3ed79bc46.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-13T16:42:14.688Z_

You are Reviewer 1 (R1) for a DREAM review roundtable. Your focus area is **Methods and Experiments**.

## Paper Details
Title: "Empirical Identifiability Boundaries for Contamination-Aware IRT Calibration of LLM Benchmarks"
Venue: AAAI 2027 (use AAAI-26 standards: 1–10 scale, ~17.6% acceptance rate)

## Paper Summary
The paper investigates when contamination-aware IRT calibration of LLM benchmarks is identifiable. It augments 4PL IRT with a contamination covariate γ, using 4 detection signals (Embedding Retrieval, Min-K%++, ConStat, Self-Critique) fused via RRF. Through controlled SFT injection experiments across Qwen2.5 models (0.5B–7B), 4 benchmarks (MMLU, GSM8K, ARC-C, HumanEval), and 5 dosage levels, it establishes:
1. Calibration is identifiable only when signal AUC ≥ 0.70 and N ≥ 80 (rarely met)
2. RL post-training degrades all signals below threshold (avg AUC drops from 0.72 to 0.56)
3. Identifiability degrades with model scale (larger models harder to calibrate)

## Key Experimental Results (from the paper)
- Table 1: Score inflation matrix — inflation inversely related to model scale (0.5B: +11.5pp, 3B: +5.2pp at 100% dosage). 5% dosage inflation <1pp, indistinguishable from noise.
- Table 2: Signal AUCs — Only Embedding Retrieval at 100% dosage reaches 0.70 threshold. At 5% dosage, all ≤0.54.
- Table 3: Signal AUC by scale — Larger models produce weaker signals (ER: 0.75→0.69 from 0.5B→3B).
- Tables 4-5: RRF fusion does NOT outperform best single signal. Pairwise correlation r=0.58 explains insufficient complementarity. 2-signal degraded mode (closed-weight): AUC 0.64.
- Table 6: 4PL+γ MAE 7.8pp vs Linear Regression 7.2pp (p=0.23). No significant difference between methods.
- Table 7: 4PL+γ achieves only 78% empirical coverage at nominal 95%. Linear reg provides better coverage (83%) and narrower CIs (16.2 vs 19.5pp).
- Table 8: Dose-response — γ CI includes zero at 5% and 25% dosage. Only identifiable at ≥50%.
- Table 9: Noise propagation — baseline γ CI width already 18pp. At matched noise, 78% conditions exceed 15pp threshold.
- Table 10: Prior sensitivity — MAE varies by 2.3pp (30% of estimate) across prior choices. Under-identification symptom.
- Table 11: Few-examinee — N=20 gives 55% γ relative bias, 68% coverage. N≥80 for significance, N≥150 for coverage.
- Tables 12-13: Signal survival — RL causes 27% AUC reduction. All signals below 0.70 under RL. Self-Critique "stable" at 0.57 (pyrrhic).
- Tables 14-15: Scale analysis — 7B: worse AUC (0.66), higher γ-θ corr (0.58), worse MAE (8.5pp). 72B: AUC 0.60, MAE 11.2pp.
- Tables 16-17: RL case study — 4PL+γ MAE 10.5pp WORSE than uncalibrated 9.8pp. Negative regret reduction (-0.03). 85% γ CIs include zero.
- Table 18: 2-signal degraded mode — 38% higher MAE, Kendall τ=0.48 (below 0.5).
- Table 19: Synthesized identifiability boundaries — 5 conditions, only 1 typically met.

## Experimental Design Reference (13 planned experiments)
All 13 experiments from the design appear covered:
- exp-001 → §4.1 (SFT injection)
- exp-002 → §4.2 (signal quality)
- exp-003 → §4.3 (RRF aggregation)
- exp-004 → referenced in §5 but NOT presented as standalone simulation (identifiability map synthesized across experiments)
- exp-005 → §4.5 (noise propagation)
- exp-006 → §4.4 (calibration + baselines)
- exp-007 → §4.9 (7B scale bridging)
- exp-008 → §4.8 (signal survival)
- exp-009 → §4.10 (RL observational)
- exp-010 → §4.6 (prior sensitivity)
- exp-011 → §4.7 (few-examinee regime)
- exp-012 → §4.9 (72B observational)
- exp-013 → §4.11 (closed-weight 2-signal)

## Your Task
Write a detailed review focused on:
1. Methodological soundness (4PL+γ model specification, Stan fitting, statistical testing)
2. Experimental design quality (controls, coverage, generalizability)
3. Reproducibility and rigor
4. Statistical analysis quality

Provide:
- 3-5 strengths (specific, with evidence)
- 3-5 weaknesses (specific, with evidence, constructive)
- Minor issues
- Questions for authors
- Scores (1-10 AAAI scale): Soundness, Experimental Quality, Clarity, Overall Assessment, Confidence (1-5)

Be rigorous but fair. Score honestly for an AAAI submission at 17.6% acceptance rate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "ab961caf-56be-4ab2-8918-98de99917772",
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

_source line 2 · 2026-05-13T16:42:14.703Z_

```json
{
  "parentUuid": "ab961caf-56be-4ab2-8918-98de99917772",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
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
  "uuid": "a28c1511-b99a-48e9-9857-0d3854113e79",
  "timestamp": "2026-05-13T16:42:14.703Z",
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

_source line 3 · 2026-05-13T16:42:17.393Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a28c1511-b99a-48e9-9857-0d3854113e79",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuFp5srHQ62KD64Jhaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa421f75-1cb1-495c-9ae9-6a9733dd5a85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198KU9Q6o11ff4YJnvdWoeE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15580,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15580,
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

_source line 4 · 2026-05-13T16:42:19.379Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B3MwNbL7TzW19tTkWFNRDs`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa421f75-1cb1-495c-9ae9-6a9733dd5a85",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuFp5srHQ62KD64Jhaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0d4526a-0210-486a-b060-b0e47013d897",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198KU9Q6o11ff4YJnvdWoeE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15580,
      "cache_read_input_tokens": 0,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15580
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15580,
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

_source line 5 · 2026-05-13T16:42:19.392Z_

<details><summary>↩ Tool result · `toolu_01B3MwNbL7TzW19tTkWFNRDs`</summary>

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
  "parentUuid": "b0d4526a-0210-486a-b060-b0e47013d897",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "54565895-eb90-446b-8a2a-e839b49df6a4",
  "sourceToolAssistantUUID": "b0d4526a-0210-486a-b060-b0e47013d897",
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

_source line 6 · 2026-05-13T16:42:22.844Z_



Let me read the paper and supporting materials to conduct a thorough methods and experiments review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54565895-eb90-446b-8a2a-e839b49df6a4",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGAAcoVKm7BfJZMMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a94748e7-e224-48e5-a1b6-b5026dac0a5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLLvrEMjRrZ8hL5a3P6BRC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
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

_source line 7 · 2026-05-13T16:42:24.436Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XYw34aHptFBCjztkzggxum`</summary>

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
  "parentUuid": "a94748e7-e224-48e5-a1b6-b5026dac0a5c",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGAAcoVKm7BfJZMMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00f3722e-8ec8-4c0c-96b1-6cf13ccbbeb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLLvrEMjRrZ8hL5a3P6BRC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
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

_source line 8 · 2026-05-13T16:42:24.512Z_

<details><summary>↩ Tool result · `toolu_01XYw34aHptFBCjztkzggxum`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_sim_confounding** (success): 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\\n- **mvp_sim_4pl_gamma** (success): 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 570, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00f3722e-8ec8-4c0c-96b1-6cf13ccbbeb5",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "4050736e-a2f7-479c-ab1e-d0445d300990",
  "sourceToolAssistantUUID": "00f3722e-8ec8-4c0c-96b1-6cf13ccbbeb5",
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

_source line 9 · 2026-05-13T16:42:24.557Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01C38yv5kJ5hJVWuLnrZb6AN`</summary>

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
  "parentUuid": "4050736e-a2f7-479c-ab1e-d0445d300990",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGAAcoVKm7BfJZMMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6a52623-bca8-458d-b14d-6352bff8286c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLLvrEMjRrZ8hL5a3P6BRC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15580,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2015
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 187,
          "cache_read_input_tokens": 15580,
          "cache_creation_input_tokens": 2015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2015,
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

_source line 10 · 2026-05-13T16:42:24.627Z_

<details><summary>↩ Tool result · `toolu_01C38yv5kJ5hJVWuLnrZb6AN`</summary>

```text
{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (2 个)\n\n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_sim_confounding** (success): 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\n- **mvp_sim_4pl_gamma** (success): 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\n\n## 趋势\n成功 2 / 负向 0 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\n（无服务器配置）\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6a52623-bca8-458d-b14d-6352bff8286c",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "a1b2867e-3c4b-42bc-b677-06e765200790",
  "sourceToolAssistantUUID": "f6a52623-bca8-458d-b14d-6352bff8286c",
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

_source line 11 · 2026-05-13T16:42:27.669Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018HrBRVnBfwHg3cq14y2fa5`</summary>

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
  "parentUuid": "a1b2867e-3c4b-42bc-b677-06e765200790",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGYU41k7YcHbYeVH3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f28a2473-0f2f-44ba-a07a-1f370cb88a71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cCyuRWXRHaYoymVPhLNgJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1077,
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

_source line 12 · 2026-05-13T16:42:27.707Z_

<details><summary>↩ Tool result · `toolu_018HrBRVnBfwHg3cq14y2fa5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)\\n- Secondary: ICLR 2027 (expected deadline: Sep 2026)\\n- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)\\n\\n## Core Insight\\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017), with 3 non-trivial adaptations for LLM evaluation.\\n\\n## Core Claims (3 条)\\n\\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model recovers true (uncontaminated) benchmark performance with low calibration error (MAE) and nominal credible interval coverage, validated on controlled SFT contamination injection experiments across 3+ model scales (0.5B-7B) and 4 benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval).\\n\\n2. **Signal Aggregation Claim**: Training-free RRF fusion of 4 complementary detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique) provides principled contamination exposure estimation without meta-circularity, outperforming any single signal and degrading gracefully under signal dropout — including a degraded 2-signal mode for closed-weight models.\\n\\n3. **Uncertainty Quantification Claim**: ContamCal explicitly propagates detection signal noise into calibration uncertainty — SFT-trained models receive tighter credible intervals (multiple reliable signals), RL-trained models receive appropriately wider intervals (primarily Self-Critique), and simulation-validated identifiability bounds establish minimum signal quality thresholds for reliable calibration.\\n\\n## Contributions (Hierarchical)\\n\\n### Core\\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT) producing calibrated scores with credible intervals\\n2. Dual-track validation: controlled SFT injection (internal validity) + ecological RL case study (external validity)\\n3. 5 baselines + 5 quantitative evaluation metrics for contamination-aware calibration\\n\\n### Supporting\\n4. Simulation-based identifiability study: systematic parameter sweep establishing minimum signal quality / model count thresholds\\n5. Signal survival analysis: systematic evaluation of which detection signals remain reliable after SFT vs. RL post-training (signal × regime AUC heatmap)\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration as the principled alternative.\\n- **Our framing**: ContamCal is a \\\"statistical safety net\\\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. This is grounded in educational measurement's item compromise IRT tradition, with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics), (b) binary leakage → continuous exposure scores (requires generalization), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware modeling).\\n- **Headline result template**: \\\"On {benchmark}, ContamCal recovers true model performance within {X}% MAE with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage. Even under noisy RL-regime detection (Self-Critique AUC ~0.65), calibrated scores with wider CIs improve model selection decisions by {R}% expected regret reduction.\\\"\\n\\n## Venue Fit Risks\\n- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.\\n- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing (\\\"wide CIs are the correct answer, not a limitation\\\").\\n- **Novelty ceiling**: Core method is synthesis of existing components (detection signals + IRT). Defense: cross-disciplinary transfer with 3 non-trivial adaptations + simulation-validated identifiability bounds as methodological contribution. Not \\\"engineering glue\\\" — each adaptation requires non-obvious modeling decisions.\\n- **RL \\\"so what\\\"**: RL models only get wide CIs. Defense: expected regret quantification shows even wide CIs improve model selection vs. naive scores.\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | MVP validated: γ rel_bias <8%, θ_residual_exp_corr=0.058 at corr=0.38 | exp-004 (sweep) |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated | exp-003 (ablation) |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity) | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d parameters necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (50)? | Few-examinee regime study + Growing Pains pre-estimation strategy | exp-011 |\\n| 7 | Noisy exposure scores | Noise propagation analysis: calibrated noise injection → CI widening quantified | exp-005 |\\n| 8 | No baselines | 7 baselines: Raw anchor, remove-rescore, single-signal 2PL+γ, vanilla 4PL, linear regression+CI, Emperor's mitigations, DCR (EMNLP 2025) | exp-006 |\\n\\n## Evaluation Protocol (5 Metrics)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n\\n## Benchmarks (4)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\\n3. **ARC-Challenge** — science reasoning multiple-choice\\n4. **HumanEval** — code generation with execution evaluation\\n- Day-8 contingency: reduce to MMLU + GSM8K\\n\\n## Baselines (7)\\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\\n\", \"total_chars\": 8347, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f28a2473-0f2f-44ba-a07a-1f370cb88a71",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "3d95af95-1600-4a09-9243-7bc65934dd47",
  "sourceToolAssistantUUID": "f28a2473-0f2f-44ba-a07a-1f370cb88a71",
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

_source line 13 · 2026-05-13T16:42:28.146Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DWq6G2LMZEgmc4Nyq5qBpN`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ARCHITECTURE.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d95af95-1600-4a09-9243-7bc65934dd47",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGYU41k7YcHbYeVH3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "110683c6-f593-43da-b82b-196514e41402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cCyuRWXRHaYoymVPhLNgJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1077,
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

_source line 14 · 2026-05-13T16:42:28.172Z_

<details><summary>↩ Tool result · `toolu_01DWq6G2LMZEgmc4Nyq5qBpN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "110683c6-f593-43da-b82b-196514e41402",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "4319a754-02e2-450e-8d69-a4d35fc766e6",
  "sourceToolAssistantUUID": "110683c6-f593-43da-b82b-196514e41402",
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

_source line 15 · 2026-05-13T16:42:28.667Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FNGpYinazTb42phX2v8W1F`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4319a754-02e2-450e-8d69-a4d35fc766e6",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGYU41k7YcHbYeVH3V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d2246b5-5314-4b60-bc93-a9af31287594",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cCyuRWXRHaYoymVPhLNgJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1077,
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

_source line 16 · 2026-05-13T16:42:28.697Z_

<details><summary>↩ Tool result · `toolu_01FNGpYinazTb42phX2v8W1F`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d2246b5-5314-4b60-bc93-a9af31287594",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "35c2324d-ae86-4024-a70e-72ac135b5552",
  "sourceToolAssistantUUID": "4d2246b5-5314-4b60-bc93-a9af31287594",
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

_source line 17 · 2026-05-13T16:42:32.030Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Nry2BuR3B2MAbw6Hin9J5H`</summary>

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
  "parentUuid": "35c2324d-ae86-4024-a70e-72ac135b5552",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGr2zB4ru3XwccNPs7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b3909c2-09d9-43aa-8d51-b6195e149c32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSpw2PRsw7PzdgNGHZq4tq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2985,
      "cache_read_input_tokens": 18672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2985,
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

_source line 18 · 2026-05-13T16:42:32.057Z_

<details><summary>↩ Tool result · `toolu_01Nry2BuR3B2MAbw6Hin9J5H`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b3909c2-09d9-43aa-8d51-b6195e149c32",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "52580982-eee7-464f-82d2-1026f62a684e",
  "sourceToolAssistantUUID": "0b3909c2-09d9-43aa-8d51-b6195e149c32",
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

_source line 19 · 2026-05-13T16:42:32.444Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CZ8rLjYPTWkfrXuZk5XU8t`</summary>

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
  "parentUuid": "52580982-eee7-464f-82d2-1026f62a684e",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGr2zB4ru3XwccNPs7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5b369ee-e843-4b1b-977d-ba60ed2bf439",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSpw2PRsw7PzdgNGHZq4tq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2985,
      "cache_read_input_tokens": 18672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2985,
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

_source line 20 · 2026-05-13T16:42:32.480Z_

<details><summary>↩ Tool result · `toolu_01CZ8rLjYPTWkfrXuZk5XU8t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\\n    role: P2 confounding robustness\\n    result: PASS with confound_corr=0.38\\n  depends_on:\\n  - D002\\n  - D003\\n\", \"total_chars\": 1844, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5b369ee-e843-4b1b-977d-ba60ed2bf439",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "ecaa3c7f-0347-4ac3-b865-1a078846ea66",
  "sourceToolAssistantUUID": "d5b369ee-e843-4b1b-977d-ba60ed2bf439",
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

_source line 21 · 2026-05-13T16:42:33.154Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011SURt5Srqivr9iPwstSMDr`</summary>

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
  "parentUuid": "ecaa3c7f-0347-4ac3-b865-1a078846ea66",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuGr2zB4ru3XwccNPs7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "796a8800-4fc9-4730-9f56-b052d6f141e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSpw2PRsw7PzdgNGHZq4tq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2985,
      "cache_read_input_tokens": 18672,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 18672,
          "cache_creation_input_tokens": 2985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2985,
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

_source line 22 · 2026-05-13T16:42:33.333Z_

<details><summary>↩ Tool result · `toolu_011SURt5Srqivr9iPwstSMDr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-13 15:51 UTC | 更新原因: MVP 完成，进入 Research 阶段，完成 paper_framing + experiment_plan + dream_simulate\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration for contamination-adjusted benchmark scores。两阶段：(1) RRF 融合 4 检测信号得到 per-item contamination exposure，(2) contamination-augmented 4PL IRT 输出校准分数 + credible intervals。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）\\n- **MVP 结论**: 4PL+γ IRT 在合成数据上成功分离 γ 和 θ（γ rel_bias <8%, θ_corr >0.94, confounding 分离后残差相关 0.058）\\n- **关键发现**: 4PL 必要（2PL 结构性劣势）；NUTS 唯一可用推断方法（ADVI 废弃）；N_items≥300 必要\\n- **Dream**: dream_20260513T155040 进行中（full review mode）\\n- **GPU**: 待分配，已向 Manager 申请\\n- **实验计划**: 13 个实验（6 P0 + 5 P1 + 2 P2），详见 experiment_plan.yaml\\n\\n## 近期任务\\n- [ ] 等待 Dream 完成 → 分析审稿反馈 → 调整 framing/plan\\n- [ ] GPU 分配到位后启动 exp-001 (controlled SFT injection)\\n- [ ] 并行启动 exp-004 (simulation sweep, CPU only)\\n- [ ] exp-004 完成后启动 exp-005 (noise propagation, CPU only)\\n\\n## GPU 预算\\n- P0: 72h | P1: 57h | P2: 20h | Buffer: 30h | Total: ~179h\\n- 需要 2-4× H100/A100-80G\\n- 预估 wall-clock: 2-4 周取决于 GPU 数量\\n\\n## 投稿目标\\n- Primary: AAAI 2027（Jul-Aug 2026 deadline）\\n- Secondary: ICLR 2027（Sep 2026 deadline）\\n\\n## Core Claims (paper_framing.md)\\n1. **Calibration**: 4PL+γ IRT recovers true scores with low MAE + nominal CI coverage\\n2. **Signal Aggregation**: RRF fusion of 4 signals, training-free, graceful degradation\\n3. **Uncertainty Quantification**: Noise propagation + regime-appropriate CI widths\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-13 | MVP 通过，进入 Research 阶段 | mvp_sim_4pl_gamma, mvp_sim_confounding |\\n| D003 | 2026-05-13 | Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMS | mvp_sim_4pl_gamma |\\n| D002 | 2026-05-13 | 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-e | — |\\n| D001 | 2026-05-13 | MVP 用 simulation identifiability test 验证 4PL+γ IRT | — |\\n\\n\\n\", \"total_chars\": 1898, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "796a8800-4fc9-4730-9f56-b052d6f141e9",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "b324c73f-a2f3-4b77-8a2d-4951cd883f26",
  "sourceToolAssistantUUID": "796a8800-4fc9-4730-9f56-b052d6f141e9",
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

_source line 23 · 2026-05-13T16:42:38.191Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01N5LNs5zm7uEJmjJPbrVYNu`</summary>

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
  "parentUuid": "b324c73f-a2f3-4b77-8a2d-4951cd883f26",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuHBk9kWEpbq28CjRp5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ff1ca81-eb1b-47d1-acd3-2ee6853f27ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHUKBMUii9QTNZSQUCV6EA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 21657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2906,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 24 · 2026-05-13T16:42:38.234Z_

<details><summary>↩ Tool result · `toolu_01N5LNs5zm7uEJmjJPbrVYNu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No memory.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ff1ca81-eb1b-47d1-acd3-2ee6853f27ee",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "0dfb1e7c-4495-48c9-9686-7ea74f0d0be9",
  "sourceToolAssistantUUID": "4ff1ca81-eb1b-47d1-acd3-2ee6853f27ee",
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

_source line 25 · 2026-05-13T16:42:38.723Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NAdRhKmnVEf6HX1jhzsDdr`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dfb1e7c-4495-48c9-9686-7ea74f0d0be9",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuHBk9kWEpbq28CjRp5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f496d924-fda6-4622-b86a-39fa3224bb1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHUKBMUii9QTNZSQUCV6EA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 21657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2906,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 26 · 2026-05-13T16:42:38.758Z_

<details><summary>↩ Tool result · `toolu_01NAdRhKmnVEf6HX1jhzsDdr`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f496d924-fda6-4622-b86a-39fa3224bb1f",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "f5d61a7a-23cf-46ea-8a7c-3d4b6cc39985",
  "sourceToolAssistantUUID": "f496d924-fda6-4622-b86a-39fa3224bb1f",
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

_source line 27 · 2026-05-13T16:42:39.389Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0186iJQ5vUBMHiwSZj9WUV31`</summary>

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
  "parentUuid": "f5d61a7a-23cf-46ea-8a7c-3d4b6cc39985",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuHBk9kWEpbq28CjRp5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f4d4473-3076-4b55-97d6-2b475512ad32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHUKBMUii9QTNZSQUCV6EA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 21657,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 21657,
          "cache_creation_input_tokens": 2906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2906,
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

_source line 28 · 2026-05-13T16:42:39.411Z_

<details><summary>↩ Tool result · `toolu_0186iJQ5vUBMHiwSZj9WUV31`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f4d4473-3076-4b55-97d6-2b475512ad32",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "093620db-eae5-4612-9226-2c93d3b6777a",
  "sourceToolAssistantUUID": "5f4d4473-3076-4b55-97d6-2b475512ad32",
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

_source line 29 · 2026-05-13T16:42:42.470Z_

Let me look for the experiment plan and any artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "093620db-eae5-4612-9226-2c93d3b6777a",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuHdwFA2gE8rsWxYqBS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d31ce11f-d758-42e8-9342-f5637abd1fa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015enSPsKV4KhcQiGkoFtgpx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 24563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 566,
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

_source line 30 · 2026-05-13T16:42:44.364Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JnSWg61UqYrJ3x4sL63TKD`</summary>

```json
{
  "pattern": "**/*experiment*plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d31ce11f-d758-42e8-9342-f5637abd1fa3",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuHdwFA2gE8rsWxYqBS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12ca355f-cf22-48e3-882b-24f1c37f54a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015enSPsKV4KhcQiGkoFtgpx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 24563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 566,
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

_source line 31 · 2026-05-13T16:42:44.534Z_

<details><summary>↩ Tool result · `toolu_01JnSWg61UqYrJ3x4sL63TKD`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12ca355f-cf22-48e3-882b-24f1c37f54a3",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "e649a115-8cd9-4726-848a-4a15d3bfcfaa",
  "sourceToolAssistantUUID": "12ca355f-cf22-48e3-882b-24f1c37f54a3",
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

_source line 32 · 2026-05-13T16:42:44.842Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UaVQ1PNAT5KD1xG9YQP2K8`</summary>

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
  "parentUuid": "e649a115-8cd9-4726-848a-4a15d3bfcfaa",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuHdwFA2gE8rsWxYqBS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11c40caf-71c1-4d70-b474-a4d5dced83a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015enSPsKV4KhcQiGkoFtgpx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 24563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 566,
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

_source line 33 · 2026-05-13T16:42:44.950Z_

<details><summary>↩ Tool result · `toolu_01UaVQ1PNAT5KD1xG9YQP2K8`</summary>

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
  "parentUuid": "11c40caf-71c1-4d70-b474-a4d5dced83a5",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "a86b306b-9c58-44d6-ae53-ddcfa862e510",
  "sourceToolAssistantUUID": "11c40caf-71c1-4d70-b474-a4d5dced83a5",
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

_source line 34 · 2026-05-13T16:42:45.338Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KySBjpr434xrRe1HWyF7yV`</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a86b306b-9c58-44d6-ae53-ddcfa862e510",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuHdwFA2gE8rsWxYqBS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f28c38d-977f-40d3-8ced-9354ef546339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015enSPsKV4KhcQiGkoFtgpx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 566,
      "cache_read_input_tokens": 24563,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 566
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 24563,
          "cache_creation_input_tokens": 566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 566,
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

_source line 35 · 2026-05-13T16:42:45.584Z_

<details><summary>↩ Tool result · `toolu_01KySBjpr434xrRe1HWyF7yV`</summary>

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
  "parentUuid": "6f28c38d-977f-40d3-8ced-9354ef546339",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "74998980-eec0-4d3c-80b8-e8398c4332a5",
  "sourceToolAssistantUUID": "6f28c38d-977f-40d3-8ced-9354ef546339",
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

_source line 36 · 2026-05-13T16:42:50.929Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DR9BvfE6aR2jyHT5NfZAKR`</summary>

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
  "parentUuid": "74998980-eec0-4d3c-80b8-e8398c4332a5",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuJ7Yv3kkBbjJ3NfdUm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61f8a32a-79f1-4e44-8b79-87b635cba4dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SxfdJbTCCDuye3LzxrZna",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3659,
      "cache_read_input_tokens": 25129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3659,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 37 · 2026-05-13T16:42:50.945Z_

<details><summary>↩ Tool result · `toolu_01DR9BvfE6aR2jyHT5NfZAKR`</summary>

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
  "parentUuid": "61f8a32a-79f1-4e44-8b79-87b635cba4dd",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "1b593dac-3076-463d-b20d-00fe39a0a488",
  "sourceToolAssistantUUID": "61f8a32a-79f1-4e44-8b79-87b635cba4dd",
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

_source line 38 · 2026-05-13T16:42:52.030Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RbRtB5ua8Yq58Ffts5VtqB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b593dac-3076-463d-b20d-00fe39a0a488",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuJ7Yv3kkBbjJ3NfdUm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "606d76d4-cb49-4d53-a9af-8a73c9bd76ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SxfdJbTCCDuye3LzxrZna",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3659,
      "cache_read_input_tokens": 25129,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3659
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 25129,
          "cache_creation_input_tokens": 3659,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3659,
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

_source line 39 · 2026-05-13T16:42:52.072Z_

<details><summary>↩ Tool result · `toolu_01RbRtB5ua8Yq58Ffts5VtqB`</summary>

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
51	
52	    '
53	- name: stage1_signal_pipeline
54	  plan_id: exp-002
55	  description: '在exp-001的所有模型上计算4种检测信号：embedding retrieval, Min-K%++, ConStat, Self-Critique。输出per-model-item
56	    exposure scores。
57	
58	    '
59	  expected_results:
60	    embedding_retrieval_auc_sft_mean: 0.88
61	    mink_pp_auc_sft_mean: 0.84
62	    constat_auc_sft_mean: 0.82
63	    self_critique_auc_sft_mean: 0.79
64	    embedding_retrieval_auc_at_5pct_dosage: 0.76
65	    mink_pp_auc_at_5pct_dosage: 0.71
66	    constat_auc_at_5pct_dosage: 0.68
67	    self_critique_auc_at_5pct_dosage: 0.66
68	    signal_pairwise_rank_corr_max: 0.52
69	    signal_pairwise_rank_corr_min: 0.28
70	    items_with_all4_signals_agree_contaminated_pct: 0.73
71	    items_with_disagreement_pct: 0.27
72	  result_rationale: 'best档下所有4个信号都有效但各有侧重。Embedding retrieval AUC最高(0.88)因为 paraphrase-based
73	    injection保留了语义相似性，FAISS能直接捕获。Min-K%++次之(0.84) 因为SFT后model perplexity在seen items上显著降低。ConStat(0.82)通过original
74	    vs paraphrase performance gap检测有效但受paraphrase质量影响。Self-Critique最低(0.79) 因为依赖模型自身判断，噪声更大，但仍远超chance。在低剂量(5%)时所有信号AUC下降约0.1，
75	    这是合理的——更少的contaminated items意味着更弱的统计信号。 信号间相关性适中(0.28-0.52)，说明它们捕获的是complementary
76	    information， 为RRF融合提供理想条件。
77	
78	    '
79	  tables:
80	  - name: 'Table 2: Per-Signal AUC by Model × Dosage'
81	    rows: 60
82	    columns:
83	    - model
84	    - dosage
85	    - embedding_auc
86	    - mink_auc
87	    - constat_auc
88	    - selfcritique_auc
89	  figures_description:
90	  - 'Fig 2: Signal AUC heatmap (signal × dosage), averaged across models and benchmarks'
91	  - 'Fig 3: Pairwise signal rank correlation matrix (4×4)'
92	  analysis: '信号质量全面达到best档预期。关键发现：信号间低-中等相关性(mean=0.38)证实 complementarity假设，为RRF融合奠定基础。HumanEval上embedding
93	    retrieval AUC 特别高(0.92)因为code的语义embedding更具区分性。
94	
95	    '
96	- name: rrf_aggregation_ablation
97	  plan_id: exp-003
98	  description: 'RRF融合4信号为composite exposure score。消融实验：RRF vs rank averaging, 单信号,
99	    calibration-weighted RRF, FP注入鲁棒性, 2-signal降级模式。
100	
101	    '
102	  expected_results:
103	    rrf_4signal_auc: 0.87
104	    rank_averaging_auc: 0.84
105	    best_single_signal_auc: 0.88
106	    calibration_weighted_rrf_auc: 0.86
107	    rrf_minus_best_single_delta_auc: -0.01
108	    rrf_auc_at_fp_rate_10pct: 0.84
109	    rrf_auc_at_fp_rate_20pct: 0.8
110	    degraded_2signal_auc: 0.78
111	    rrf_4signal_vs_2signal_delta: 0.09
112	    rrf_exposure_score_spearman_with_true_dosage: 0.91
113	    rank_stability_bootstrap_cv: 0.04
114	  result_rationale: 'best档下RRF融合AUC(0.87)接近最好的单信号(embedding 0.88)但关键优势在于鲁棒性： RRF在所有benchmark上都稳定达到0.85+，而单信号表现波动大（embedding在GSM8K上可能
115	    降到0.80，ConStat在HumanEval上可能降到0.75）。RRF比rank averaging高3pp因为 reciprocal rank weighting对高置信排名给予更大权重。Calibration-weighted
116	    RRF略低于 vanilla RRF因为权重估计引入了额外noise，且在best档的高信号质量下vanilla RRF已足够。 FP注入10%时AUC仅降3pp，20%时降7pp，证明graceful
117	    degradation。 2-signal模式(ConStat+Self-Critique)AUC=0.78，比4-signal低9pp但仍远超chance，
118	    满足closed-weight场景的可用性。exposure score与true dosage的spearman=0.91 证明RRF输出确实捕获了contamination程度的有序信息。
119	
120	    '
121	  tables:
122	  - name: 'Table 3: RRF Ablation Results'
123	    rows: 8
124	    columns:
125	    - method
126	    - auc_mmlu
127	    - auc_gsm8k
128	    - auc_arc
129	    - auc_humaneval
130	    - auc_mean
131	    - auc_std
132	  - name: 'Table 4: FP Injection Robustness'
133	    rows: 4
134	    columns:
135	    - fp_rate
136	    - rrf_auc
137	    - delta_from_clean
138	  figures_description:
139	  - 'Fig 4: Signal dropout ablation bar chart — AUC by combination (4-signal, each
140	    3-signal, each single, 2-signal degraded)'
141	  - 'Fig 5: RRF exposure score vs true dosage scatter plot with Spearman annotation'
142	  analysis: 'RRF fusion的核心价值不在于AUC绝对值（最好的单信号可能匹配），而在于跨benchmark、 跨模型的一致性和FP鲁棒性。这直接支持Claim
143	    2的"outperforming any single signal"—— 含义是worst-case performance更优，而非mean AUC更高。2-signal降级模式AUC=0.78
144	    为closed-weight实用性提供了有力支撑。
145	
146	    '
147	- name: noise_propagation_analysis
148	  plan_id: exp-005
149	  description: '校准noise注入到exposure scores中：估计per-item FP/FN率， 注入matched/1.5×/2×高斯噪声，重新拟合IRT，测量CI宽化。
150	
151	    '
152	  expected_results:
153	    selfcritique_estimated_fp_rate: 0.12
154	    selfcritique_estimated_fn_rate: 0.18
155	    matched_noise_ci_width_gamma_pp: 5.2
156	    noise_1_5x_ci_width_gamma_pp: 6.8
157	    noise_2x_ci_width_gamma_pp: 8.9
158	    matched_noise_ci_coverage_95: 0.94
159	    noise_1_5x_ci_coverage_95: 0.96
160	    noise_2x_ci_coverage_95: 0.97
161	    gamma_rel_bias_at_matched_noise: 0.06
162	    gamma_rel_bias_at_2x_noise: 0.09
163	    theta_corr_at_matched_noise: 0.94
164	    theta_corr_at_2x_noise: 0.89
165	    measurement_error_model_dic_improvement: 12.3
166	  result_rationale: 'best档下noise propagation表现理想：随着noise增加，CI合理宽化（5.2→8.9pp）而非崩溃，
167	    coverage从94%略升至97%（略过覆盖而非欠覆盖）。这说明Bayesian posterior正确地将 exposure score uncertainty吸收进了参数不确定性。gamma相对偏差从0.06增到0.09，
168	    表明点估计稳健性在2×noise下仍可接受。theta相关性从0.94降至0.89，下降幅度合理—— 更多noise意味着contamination信号更弱，ability估计回退向vanilla
169	    IRT。 Self-Critique的FP=12%/FN=18%在best档下是合理的——比embedding差但比random好得多。 measurement
170	    error扩展模型DIC改善12.3说明显式建模exposure noise有统计意义上的价值。
171	
172	    '
173	  tables:
174	  - name: 'Table 5: Noise Propagation Results'
175	    rows: 4
176	    columns:
177	    - noise_level
178	    - gamma_mean
179	    - gamma_rel_bias
180	    - ci_width_pp
181	    - ci_coverage_95
182	    - theta_corr
183	  figures_description:
184	  - 'Fig 6: CI width vs noise level line plot, with coverage annotated at each point'
185	  - 'Fig 7: θ recovery correlation scatterplots at 3 noise levels (1×, 1.5×, 2×)'
186	  analysis: '核心结论：4PL+γ的Bayesian formulation天然支持noise propagation——更noisy的exposure
187	    scores产生更宽的CI而不是更差的点估计。这直接支持Claim 3，也为RL regime下 Self-Critique-only信号的wider CIs提供了机制解释。
188	
189	    '
190	- name: irt_calibration_and_baselines
191	  plan_id: exp-006
192	  description: '在exp-001/003的controlled数据上拟合4PL+γ IRT (Stan NUTS)， 计算calibrated scores，与5个baselines比较，评估5个指标。
193	
194	    '
195	  expected_results:
196	    contam_cal_mae_pp_mmlu: 1.8
197	    contam_cal_mae_pp_gsm8k: 2.1
198	    contam_cal_mae_pp_arc: 1.6
199	    contam_cal_mae_pp_humaneval: 2.4
200	    contam_cal_mae_pp_mean: 1.97
201	    contam_cal_ci_coverage_95: 0.93
202	    contam_cal_ci_coverage_80: 0.84
203	    contam_cal_ci_coverage_50: 0.55
204	    contam_cal_ci_width_95_pp: 5.8
205	    contam_cal_kendall_tau: 0.91
206	    contam_cal_dose_response_spearman: 0.96
207	    baseline_remove_rescore_mae_pp: 4.2
208	    baseline_single_2plg_mae_pp: 3.8
209	    baseline_vanilla_4pl_mae_pp: 6.1
210	    baseline_linear_regression_mae_pp: 3.5
211	    baseline_emperor_mitigation_mae_pp: 5.7
212	    best_baseline_mae_pp: 3.5
213	    margin_over_best_baseline_mae_relative: 0.44
214	    naive_score_overestimation_50pct_dosage_pp: 9.3
215	    gamma_posterior_mean: 0.42
216	    gamma_posterior_sd: 0.08
217	    gamma_rel_bias_real_data: 0.06
218	    theta_corr_with_ground_truth: 0.95
219	    theta_gamma_posterior_corr: 0.31
220	    nuts_divergent_pct: 0.0
221	    nuts_max_rhat: 1.005
222	    nuts_ess_min: 800
223	  result_rationale: 'best档核心实验。4PL+γ MAE=1.97pp完全复现仿真表现——真实SFT数据上的contamination 结构与仿真假设匹配良好。MMLU
224	    MAE最低(1.8pp)因为item数量最多(14K)提供了最强的 统计功效；HumanEval最高(2.4pp)因为item少且code execution评分的binary
225	    nature 增加了noise。93% coverage接近nominal 95%，略低是因为real data的item heterogeneity 比仿真更大，但仍在可接受范围。CI宽度5.8pp在sharpness和coverage间取得了好的平衡。
226	
227	    Baselines方面：vanilla 4PL(无γ)MAE=6.1pp最差，因为完全忽略contamination， 证明contamination covariate是必要的。Emperor''s
228	    mitigation MAE=5.7pp次差， 与ICML 2025发现一致——mitigation strategies确实不够有效。Linear regression
229	    MAE=3.5pp 是最好的baseline，但仍比ContamCal差44%——IRT的优势在于non-linear item response 建模和proper
230	    uncertainty propagation。Remove-rescore MAE=4.2pp受限于binary flagging丢失了contamination程度信息。Single-signal
231	    2PL+γ MAE=3.8pp表明 signal fusion和4PL复杂度各贡献了一部分改善。
232	
233	    θ-γ posterior correlation=0.31 < 0.4阈值，证实identifiability。 gamma rel_bias=0.06与仿真的0.068几乎一致。NUTS诊断完美——无divergence，
234	    Rhat<1.01，ESS>800。
235	
236	    '
237	  tables:
238	  - name: 'Table 6 (Main Result): Calibration Performance — ContamCal vs 5 Baselines'
239	    rows: 6
240	    columns:
241	    - method
242	    - mae_mmlu
243	    - mae_gsm8k
244	    - mae_arc
245	    - mae_humaneval
246	    - mae_mean
247	    - ci_coverage_95
248	    - ci_width_95
249	    - kendall_tau
250	  - name: 'Table 7: Per-Benchmark Detailed Metrics'
251	    rows: 4
252	    columns:
253	    - benchmark
254	    - mae_pp
255	    - coverage_50
256	    - coverage_80
257	    - coverage_95
258	    - ci_width_95_pp
259	    - kendall_tau
260	    - dose_response_spearman
261	  - name: 'Table 8: MCMC Diagnostics'
262	    rows: 4
263	    columns:
264	    - benchmark
265	    - divergent_pct
266	    - max_rhat
267	    - min_ess
268	    - fit_time_sec
269	  figures_description:
270	  - 'Fig 8 (Main Figure): Calibrated vs true accuracy scatter plot, all benchmarks,
271	    with 95% CI error bars, diagonal reference line'
272	  - 'Fig 9: MAE bar chart — ContamCal vs 5 baselines, per benchmark'
273	  - 'Fig 10: Dose-response curves — γ effect size vs contamination dosage, 4 benchmark
274	    panels'
275	  - 'Fig 11: Coverage calibration plot — nominal vs empirical coverage at 50/80/95%
276	    levels'
277	  analysis: '这是论文的核心结果表。MAE 1.97pp vs best baseline 3.5pp (44% relative improvement)
278	    提供了Claim 1的强有力支撑。93% coverage证明CI可靠。headline result可直接写为 "ContamCal recovers true
279	    performance within 2pp MAE with 93% CI coverage, while naive scores overestimate
280	    by 8-12pp." Kendall τ=0.91证明model ranking 在calibration后基本保持正确——contamination改变的是绝对分数而非相对排名，
281	    但ContamCal在absolute calibration上的优势对于跨benchmark比较至关重要。
282	
283	    '
284	- name: scale_bridging_7b
285	  plan_id: exp-007
286	  description: 'Qwen2.5-7B在5个dosage水平下的controlled SFT注入，验证calibration在更大模型上的有效性。
287	
288	    '
289	  expected_results:
290	    dosage_25pct_acc_inflation_mmlu_pp: 4.8
291	    dosage_50pct_acc_inflation_mmlu_pp: 7.6
292	    dosage_100pct_acc_inflation_mmlu_pp: 10.2
293	    contam_cal_mae_pp_mean_7b: 2.2
294	    contam_cal_ci_coverage_95_7b: 0.92
295	    contam_cal_kendall_tau_7b: 0.89
296	    mae_increase_vs_3b_pp: 0.3
297	    gamma_mean_7b: 0.38
298	    dose_response_spearman_7b: 0.94
299	  result_rationale: 'best档下7B模型表现略弱于0.5-3B但仍在acceptable范围内。7B的inflation略低于小模型 (50%
300	    dosage: 7.6pp vs 9.3pp mean for smaller)因为7B的更强泛化能力意味着 contamination的relative
301	    contribution更小。MAE略增至2.2pp(+0.3pp vs 3B)因为 7B模型的item response pattern更复杂，但仍远优于baselines。gamma估计值0.38略低于
302	    小模型的0.42，反映了contamination对larger model的较小相对效应。 Coverage 92%和Kendall τ=0.89仍然强劲，证明ContamCal可扩展到7B规模。
303	
304	    '
305	  tables:
306	  - name: 'Table 9: 7B Scale Bridging Results'
307	    rows: 5
308	    columns:
309	    - dosage
310	    - inflation_pp
311	    - contam_cal_mae_pp
312	    - ci_coverage_95
313	    - kendall_tau
314	  figures_description:
315	  - 'Fig 12: MAE vs model scale line plot (0.5B, 1.5B, 3B, 7B) showing graceful degradation'
316	  analysis: '7B结果证明ContamCal从小模型到中等规模模型的可扩展性。MAE增加有限(+0.3pp) 且符合理论预期——更大的模型有更复杂的ability
317	    landscape但contamination的相对效应更小。
318	
319	    '
320	- name: signal_survival_analysis
321	  plan_id: exp-008
322	  description: '检测信号在不同训练regime下的可靠性系统评估。 Signal × regime AUC heatmap: 4 signals ×
323	    {base, SFT-clean, SFT-contaminated, RL-post-trained}。
324	
325	    '
326	  expected_results:
327	    embedding_auc_base: 0.9
328	    embedding_auc_sft_clean: 0.51
329	    embedding_auc_sft_contam: 0.88
330	    embedding_auc_rl: 0.55
331	    mink_auc_base: 0.86
332	    mink_auc_sft_clean: 0.53
333	    mink_auc_sft_contam: 0.84
334	    mink_auc_rl: 0.58
335	    constat_auc_base: 0.5
336	    constat_auc_sft_clean: 0.5
337	    constat_auc_sft_contam: 0.82
338	    constat_auc_rl: 0.67
339	    selfcritique_auc_base: 0.5
340	    selfcritique_auc_sft_clean: 0.5
341	    selfcritique_auc_sft_contam: 0.79
342	    selfcritique_auc_rl: 0.72
343	    signal_survival_rl_best: Self-Critique
344	    signal_survival_rl_second: ConStat
345	  result_rationale: 'best档下信号存活模式清晰：embedding和Min-K%++在SFT-contaminated上表现强劲 (0.88/0.84)但在RL后严重降级(0.55/0.58)——RL的policy
346	    gradient更新破坏了 token-level memorization pattern，使得perplexity-based信号失效。 ConStat在RL后保留AUC=0.67因为它测量的是performance
347	    gap(original vs paraphrase) 这一higher-level信号，不依赖model internals。Self-Critique在RL后最强(0.72)
348	    因为它利用模型的reasoning能力来自我评估，RL强化了这种元认知能力而非削弱。 base模型和SFT-clean模型上ConStat和Self-Critique接近chance(0.50)是正确的——
349	    没有contamination时不应有信号（specificity验证）。 这个heatmap直接支持RRF fusion的必要性：没有任何单一信号在所有regime下都最优。
350	
351	    '
352	  tables:
353	  - name: 'Table 10 (Supporting Contribution): Signal × Regime AUC Heatmap'
354	    rows: 4
355	    columns:
356	    - signal
357	    - base
358	    - sft_clean
359	    - sft_contam
360	    - rl_post_trained
361	  figures_description:
362	  - 'Fig 13: Signal survival heatmap (4×4 matrix, color-coded by AUC)'
363	  - 'Fig 14: Per-signal AUC degradation from SFT→RL, paired bar chart'
364	  analysis: '这是论文的Supporting Contribution 5。关键insight：RL post-training创造了一个 "signal
365	    desert"——只有Self-Critique和ConStat存活。这解释了为什么RL regime 需要更宽的CI（更少信号→更大不确定性），同时也为2-signal
366	    degraded mode提供了 empirical justification。
367	
368	    '
369	- name: rl_observational_case_study
370	  plan_id: exp-009
371	  description: '对现有RL-trained模型(Qwen2.5-Instruct系列, DeepSeek-R1-Distill系列) 应用Self-Critique
372	    + available signals，拟合IRT with wider CIs， expected regret量化。
373	
374	    '
375	  expected_results:
376	    selfcritique_auc_rl_models_mean: 0.71
377	    available_signals_rl_count: 2
378	    contam_cal_ci_width_95_rl_pp: 11.4
379	    contam_cal_ci_width_95_sft_comparison_pp: 5.8
380	    ci_width_ratio_rl_vs_sft: 1.97
381	    expected_regret_uncalibrated: 0.38
382	    expected_regret_calibrated_wide_ci: 0.22
383	    expected_regret_remove_rescore: 0.31
384	    regret_reduction_vs_uncalibrated: 0.42
385	    regret_reduction_vs_remove_rescore: 0.29
386	    near_zero_gamma_clean_benchmark_check: 0.03
387	    gamma_posterior_rl_mean: 0.28
388	    gamma_posterior_rl_sd: 0.14
389	    gamma_ci_includes_zero_rl: false
390	    num_models_rl_case: 8
391	    kendall_tau_rl_top5_selection: 0.8
392	  result_rationale: 'best档下RL observational case study展示了"wide CIs are the correct
393	    answer"的完整叙事。 Self-Critique AUC=0.71（略超0.70阈值）在RL模型上提供了可用但noisy的信号。 CI宽度11.4pp约为SFT的2倍——这不是方法失败，而是正确反映了RL
394	    regime下检测信号的 更大不确定性。gamma posterior mean=0.28 (sd=0.14)表明RL模型确实存在contamination
395	    效应但估计更不确定；CI不包含0证明信号是directionally informative的。
396	
397	    Expected regret量化是关键：uncalibrated选择top-5模型的expected regret=0.38， 使用wide-CI calibrated
398	    scores后降至0.22（42% reduction），优于remove-rescore的0.31。 机制：即使CI很宽，calibrated scores的point
399	    estimate仍然比naive scores更准确， 而wide CI让决策者知道应该对RL模型的排名更谨慎。
400	
401	    Near-zero gamma check在known-clean benchmark上γ=0.03(接近0)， 通过specificity检验——模型不会对uncontaminated
402	    data产生false alarm。
403	
404	    '
405	  tables:
406	  - name: 'Table 11: RL Case Study — Expected Regret Comparison'
407	    rows: 3
408	    columns:
409	    - method
410	    - expected_regret
411	    - regret_reduction_vs_naive
412	    - top5_kendall_tau
413	  - name: 'Table 12: RL vs SFT CI Width Comparison'
414	    rows: 2
415	    columns:
416	    - regime
417	    - mean_ci_width_95_pp
418	    - gamma_mean
419	    - gamma_sd
420	    - signal_count
421	  figures_description:
422	  - 'Fig 15: RL vs SFT credible interval width comparison (paired model bar chart)'
423	  - 'Fig 16: Expected regret cumulative plot — uncalibrated vs calibrated vs remove-rescore'
424	  - 'Fig 17: Near-zero gamma check — posterior density on clean benchmark showing
425	    mass near zero'
426	  analysis: 'RL case study的叙事完美支持Claim 3。核心message不是"ContamCal在RL上也很准" （那不诚实），而是"ContamCal在RL上给出了appropriately
427	    uncertain的答案， 这些uncertain answers仍然改善了决策"。42% regret reduction是一个compelling number。
428	    Near-zero gamma specificity check排除了"方法总是报告contamination"的担忧。
429	
430	    '
431	- name: prior_sensitivity
432	  plan_id: exp-010
433	  description: '使用γ prior N(0,0.5)和N(0,2)（默认N(0,1)）重新拟合IRT， 验证calibrated scores和CIs对prior选择的鲁棒性。
434	
435	    '
436	  expected_results:
437	    mae_prior_tight_n05: 2.1
438	    mae_prior_default_n10: 1.97
439	    mae_prior_wide_n20: 2.0
440	    coverage_95_prior_tight: 0.91
441	    coverage_95_prior_default: 0.93
442	    coverage_95_prior_wide: 0.95
443	    ci_width_prior_tight_pp: 4.9
444	    ci_width_prior_default_pp: 5.8
445	    ci_width_prior_wide_pp: 7.1
446	    gamma_mean_prior_tight: 0.39
447	    gamma_mean_prior_default: 0.42
448	    gamma_mean_prior_wide: 0.44
449	    max_mae_diff_across_priors_pp: 0.13
450	    kendall_tau_prior_tight: 0.9
451	    kendall_tau_prior_default: 0.91
452	    kendall_tau_prior_wide: 0.91
453	  result_rationale: 'best档下prior sensitivity表现理想：三种prior下MAE差异仅0.13pp，Kendall τ几乎
454	    不变(0.90-0.91)。tight prior N(0,0.5)略微shrink了gamma估计(0.39 vs 0.42) 导致MAE略高(2.1pp)，但差异很小。wide
455	    prior N(0,2)允许gamma更大(0.44)且CI更宽 (7.1pp vs 5.8pp)，coverage从93%升至95%但sharpness代价可接受。
456	    这种行为说明：(1)数据信息量足够大，prior的影响被likelihood dominated； (2)在best档的高信号质量下，任何reasonable
457	    prior都能得到好的结果。 这直接回应了"prior choice drives results"的潜在reviewer concern。
458	
459	    '
460	  tables:
461	  - name: 'Table 13: Prior Sensitivity Analysis'
462	    rows: 3
463	    columns:
464	    - prior
465	    - mae_pp
466	    - coverage_95
467	    - ci_width_pp
468	    - gamma_mean
469	    - kendall_tau
470	  figures_description:
471	  - 'Fig 18: Prior sensitivity — MAE and CI width across 3 prior choices, error bars'
472	  analysis: 'Prior sensitivity结果证明方法稳健。MAE变化<0.15pp且ranking完全稳定， 满足了Bayesian方法的基本robustness要求。default
473	    prior N(0,1)在 coverage/sharpness trade-off上最优。
474	
475	    '
476	- name: few_examinee_regime
477	  plan_id: exp-011
478	  description: '仿真研究：model count 20/50/100/200下的IRT性能。 两阶段估计策略：用Growing Pains 400+模型池预估item参数作为informative
479	    priors。
480	
481	    '
482	  expected_results:
483	    mae_pp_n20_no_preestimate: 4.8
484	    mae_pp_n20_with_preestimate: 2.9
485	    mae_pp_n50_no_preestimate: 2.8
486	    mae_pp_n50_with_preestimate: 2.1
487	    mae_pp_n100_no_preestimate: 2.0
488	    mae_pp_n100_with_preestimate: 1.9
489	    mae_pp_n200_no_preestimate: 1.7
490	    mae_pp_n200_with_preestimate: 1.7
491	    preestimate_benefit_n20_pp: 1.9
492	    preestimate_benefit_n50_pp: 0.7
493	    preestimate_benefit_n100_pp: 0.1
494	    coverage_95_n20_preestimate: 0.9
495	    coverage_95_n50_preestimate: 0.92
496	    coverage_95_n100_preestimate: 0.93
497	    gamma_rel_bias_n20_preestimate: 0.12
498	    gamma_rel_bias_n50_preestimate: 0.08
499	    min_viable_model_count: 50
500	  result_rationale: 'best档下few-examinee仿真展示了清晰的performance gradient和pre-estimation策略的价值。
501	    N=20裸跑MAE=4.8pp不可接受，但pre-estimation将其降至2.9pp——从Growing Pains的 400+模型池中借用item parameter
502	    estimates作为informative prior极大地稳定了估计。 N=50是一个sweet spot：裸跑MAE已降至2.8pp，pre-estimation进一步降至2.1pp。
503	    N=100+时pre-estimation的marginal benefit趋近于0（0.1pp），因为数据本身已足够。 min viable model
504	    count设为50（with pre-estimation），此时coverage 92%且 gamma rel_bias 8%都在可接受范围。这直接回应了reviewer
505	    concern #6 "too few models"。
506	
507	    '
508	  tables:
509	  - name: 'Table 14: Few-Examinee Regime Study'
510	    rows: 8
511	    columns:
512	    - n_models
513	    - preestimate
514	    - mae_pp
515	    - coverage_95
516	    - ci_width_pp
517	    - gamma_rel_bias
518	  figures_description:
519	  - 'Fig 19: MAE vs model count, with/without pre-estimation, two lines converging
520	    at N=100+'
521	  analysis: 'N=50 with pre-estimation是论文推荐的minimum viable configuration。 pre-estimation策略巧妙利用了existing
522	    model evaluation pools（如Growing Pains的 Open LLM Leaderboard数据），无需额外实验成本。
523	
524	    '
525	- name: observational_72b
526	  plan_id: exp-012
527	  description: 'Qwen2.5-72B观测分析（仅推理，无SFT）。将ecological validity扩展到frontier模型规模。
528	
529	    '
530	  expected_results:
531	    gamma_posterior_72b_mmlu: 0.18
532	    gamma_posterior_72b_gsm8k: 0.12
533	    gamma_ci_excludes_zero_72b_mmlu: true
534	    gamma_ci_excludes_zero_72b_gsm8k: false
535	    calibrated_score_shift_mmlu_pp: -3.2
536	    calibrated_score_shift_gsm8k_pp: -1.8
537	    ci_width_95_72b_pp: 8.5
538	    selfcritique_auc_72b_estimated: 0.68
539	    qualitative_consistency_with_7b: true
540	  result_rationale: 'best档下72B观测分析提供了重要的ecological validity但不能有ground truth验证。 gamma=0.18（MMLU）表明即使72B模型也存在可检测的contamination效应，但效应量小于
541	    小模型(0.42)——这合理因为72B的能力足够强使得contamination的relative contribution更小。 MMLU上gamma CI排除0说明信号存在；GSM8K上CI包含0说明reasoning
542	    benchmark对72B的 contamination效应可能在noise floor以下。calibrated score下调3.2pp（MMLU） 是一个substantive但不极端的correction。CI宽度8.5pp反映了observational
543	    setting 的更大不确定性。Self-Critique AUC=0.68略低于0.70阈值，但仍在"方向性有效"范围内。
544	
545	    '
546	  tables:
547	  - name: 'Table 15: 72B Observational Analysis'
548	    rows: 4
549	    columns:
550	    - benchmark
551	    - gamma_mean
552	    - gamma_ci_lower
553	    - gamma_ci_upper
554	    - calibrated_shift_pp
555	    - ci_width_pp
556	  figures_description:
557	  - 'Fig 20: Gamma estimates across model scales (0.5B→72B) showing decreasing trend'
558	  analysis: '72B结果支持"contamination effects exist at all scales but diminish with scale"的叙事。
559	    这是生态效度论证——不是定量验证，而是证明ContamCal在frontier scale下产生 plausible和internally consistent的结果。
560	
561	    '
562	- name: closed_weight_2signal_mode
563	  plan_id: exp-013
564	  description: '降级2-signal模式(ConStat + Self-Critique)的消融研究， 量化2-signal vs 4-signal的calibration
565	    accuracy差距。
566	
567	    '
568	  expected_results:
569	    contam_cal_2signal_mae_pp: 2.4
570	    contam_cal_4signal_mae_pp: 1.97
571	    mae_increase_2signal_relative: 0.1
572	    contam_cal_2signal_ci_coverage_95: 0.94
573	    contam_cal_2signal_ci_width_95_pp: 7.2
574	    contam_cal_2signal_kendall_tau: 0.87
575	    contam_cal_2signal_dose_response_spearman: 0.92
576	    still_beats_best_baseline: true
577	    margin_over_best_baseline_2signal_relative: 0.31
578	  result_rationale: 'best档下2-signal降级模式MAE增加10%(2.4pp vs 1.97pp)，在best档范围[0.05, 0.15]的
579	    中间位置。CI宽度从5.8pp增至7.2pp（+24%），coverage从93%升至94%——更宽的CI 正确补偿了更少信号带来的更大不确定性。Kendall
580	    τ从0.91降至0.87，ranking能力略降 但仍然strong。关键：2-signal模式仍然beat best baseline 31%（2.4pp
581	    vs 3.5pp）， 证明即使在closed-weight限制下ContamCal仍有实际价值。 MAE增加主要来自ConStat在某些benchmark上的noise较大（缺少embedding和Min-K%++
582	    的complementary information），但Self-Critique的reasoning-level信号提供了 必要的anchor。dose-response
583	    spearman=0.92仍然strong。
584	
585	    '
586	  tables:
587	  - name: 'Table 16: 2-Signal vs 4-Signal Degraded Mode Comparison'
588	    rows: 2
589	    columns:
590	    - mode
591	    - mae_pp
592	    - coverage_95
593	    - ci_width_pp
594	    - kendall_tau
595	    - margin_vs_baseline
596	  figures_description:
597	  - 'Fig 21: 2-signal vs 4-signal calibration accuracy per benchmark, grouped bar
598	    chart'
599	  analysis: 2-signal模式的10% MAE degradation是一个acceptable trade-off，证明ContamCal 可以gracefully
600	    degrade到closed-weight settings。论文可以confidence地claim "even without model internals
601	    access, ContamCal provides meaningful calibration improvement over baselines."
602	    这大幅扩展了方法的practical applicability。
603	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "606d76d4-cb49-4d53-a9af-8a73c9bd76ad",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "499abacd-9307-4112-ba88-739f14e5a080",
  "sourceToolAssistantUUID": "606d76d4-cb49-4d53-a9af-8a73c9bd76ad",
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

_source line 40 · 2026-05-13T16:42:55.996Z_

Now let me read the actual paper results (the "imagined experiments" for the median and worst tiers, and the review context for best tier) to understand what was actually presented versus what was imagined.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "499abacd-9307-4112-ba88-739f14e5a080",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuJaH19GixXgs7DmbXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16e7efbf-33b9-4c45-acb2-533458444467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NgZ86NKff8xQuqC5iaNWs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15596,
      "cache_read_input_tokens": 28788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15596,
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

_source line 41 · 2026-05-13T16:42:59.083Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nt6DgEDsm6wCwurmuxc5hG`</summary>

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
  "parentUuid": "16e7efbf-33b9-4c45-acb2-533458444467",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuJaH19GixXgs7DmbXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43fc2f49-aa4d-47e3-974b-5c8bca68b91f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NgZ86NKff8xQuqC5iaNWs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15596,
      "cache_read_input_tokens": 28788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15596,
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

_source line 42 · 2026-05-13T16:42:59.283Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YQvAHQkBF9X4PKBC5iuA49`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43fc2f49-aa4d-47e3-974b-5c8bca68b91f",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuJaH19GixXgs7DmbXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4c91093-9104-4998-9339-76295ecef661",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NgZ86NKff8xQuqC5iaNWs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15596,
      "cache_read_input_tokens": 28788,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15596
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 28788,
          "cache_creation_input_tokens": 15596,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15596,
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

_source line 43 · 2026-05-13T16:42:59.451Z_

<details><summary>↩ Tool result · `toolu_01Nt6DgEDsm6wCwurmuxc5hG`</summary>

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
  "parentUuid": "43fc2f49-aa4d-47e3-974b-5c8bca68b91f",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "d0acaef8-1403-407d-89fc-545ff9436b40",
  "sourceToolAssistantUUID": "43fc2f49-aa4d-47e3-974b-5c8bca68b91f",
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

_source line 44 · 2026-05-13T16:42:59.629Z_

<details><summary>↩ Tool result · `toolu_01YQvAHQkBF9X4PKBC5iuA49`</summary>

```text
1	tier: worst
2	narrative_guidance: '核心calibration claim不成立。Reframe为"Empirical Identifiability Boundaries
3	  for Contamination-Aware IRT"—— 系统性研究在什么条件下IRT校准才可行。exp-004仿真的identifiability map成为Core
4	  Contribution 1， exp-008 signal survival升级为Core，controlled SFT注入变为empirical validation证明仿真边界与真实数据吻合。
5	  叙事逻辑：在构建校准系统之前，先搞清楚它何时能工作。论文从"we solve calibration"转为"we map when calibration is
6	  solvable"。
7	
8	  '
9	imagined_experiments:
10	- name: controlled_sft_injection
11	  plan_id: exp-001
12	  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels.
13	    在worst档下，注入本身成功但产生的score inflation pattern不干净—— 低dosage几乎无可测效应，高dosage效应被模型capacity限制截断。
14	
15	    '
16	  expected_results:
17	    sft_runs_completed: 15
18	    mmlu_score_inflation_0pct_baseline_acc: 0.47
19	    mmlu_score_inflation_5pct_pp: 0.8
20	    mmlu_score_inflation_25pct_pp: 2.1
21	    mmlu_score_inflation_50pct_pp: 4.5
22	    mmlu_score_inflation_100pct_pp: 8.2
23	    gsm8k_score_inflation_100pct_pp: 5.1
24	    arc_score_inflation_100pct_pp: 6.8
25	    humaneval_score_inflation_100pct_pp: 3.9
26	    inflation_monotonicity_spearman_mmlu: 0.9
27	    inflation_monotonicity_spearman_gsm8k: 0.7
28	    inflation_variance_across_seeds_std_pp: 2.8
29	    qwen_0_5b_inflation_at_100pct_pp: 11.5
30	    qwen_3b_inflation_at_100pct_pp: 5.8
31	    low_dosage_detectable_5pct: false
32	    low_dosage_detectable_25pct_marginal: true
33	  result_rationale: 'SFT注入机制本身可靠（paraphrase SFT是成熟技术），所以15个run都会完成。 但worst档的核心问题在这里开始显现：(1)
34	    0.5B模型capacity极小，SFT后memorization严重但泛化到benchmark format的能力弱， 导致inflation方差大；(2)
35	    5%dosage（<700 items for MMLU）在SFT数据中被稀释，inflation <1pp， 与random seed noise不可区分——这直接导致后续dose-response非单调的关键问题；
36	    (3) GSM8K/HumanEval因为是生成式评估（非选择题），paraphrase memorization的转化率低于MMLU， inflation更弱；(4)
37	    3B模型因pretraining更强，SFT的边际效应递减—— 表现为"大模型inflation反而小于小模型"的反直觉模式，给后续γ估计制造confounding。
38	    整体inflation pattern存在但noisy，为后续信号检测和IRT拟合埋下问题。
39	
40	    '
41	  tables:
42	  - name: 'Table: Score Inflation by Model × Dosage × Benchmark'
43	    columns:
44	    - model
45	    - benchmark
46	    - 0%
47	    - 5%
48	    - 25%
49	    - 50%
50	    - 100%
51	    rows:
52	    - - Qwen2.5-0.5B
53	      - MMLU
54	      - 42.3
55	      - 43.5
56	      - 45.8
57	      - 49.1
58	      - 53.8
59	    - - Qwen2.5-0.5B
60	      - GSM8K
61	      - 31.2
62	      - 31.5
63	      - 32.8
64	      - 34.1
65	      - 36.3
66	    - - Qwen2.5-0.5B
67	      - ARC-C
68	      - 38.1
69	      - 38.6
70	      - 40.2
71	      - 42.5
72	      - 45.9
73	    - - Qwen2.5-0.5B
74	      - HumanEval
75	      - 22.0
76	      - 22.1
77	      - 23.0
78	      - 24.2
79	      - 25.9
80	    - - Qwen2.5-1.5B
81	      - MMLU
82	      - 53.1
83	      - 53.6
84	      - 54.8
85	      - 56.5
86	      - 59.7
87	    - - Qwen2.5-1.5B
88	      - GSM8K
89	      - 48.5
90	      - 48.8
91	      - 49.9
92	      - 51.8
93	      - 53.2
94	    - - Qwen2.5-1.5B
95	      - ARC-C
96	      - 52.0
97	      - 52.4
98	      - 53.5
99	      - 55.1
100	      - 57.8
101	    - - Qwen2.5-1.5B
102	      - HumanEval
103	      - 35.4
104	      - 35.6
105	      - 36.5
106	      - 37.8
107	      - 39.1
108	    - - Qwen2.5-3B
109	      - MMLU
110	      - 61.8
111	      - 62.1
112	      - 63.0
113	      - 64.5
114	      - 67.0
115	    - - Qwen2.5-3B
116	      - GSM8K
117	      - 62.3
118	      - 62.5
119	      - 63.1
120	      - 64.2
121	      - 65.8
122	    - - Qwen2.5-3B
123	      - ARC-C
124	      - 60.5
125	      - 60.8
126	      - 61.6
127	      - 63.0
128	      - 65.2
129	    - - Qwen2.5-3B
130	      - HumanEval
131	      - 48.2
132	      - 48.4
133	      - 49.0
134	      - 50.1
135	      - 52.1
136	  figures_description:
137	  - 'Fig: Dosage-Inflation curves per model×benchmark. Key observation: 5% dosage
138	    points overlap with 0% error bars on most benchmarks. GSM8K/HumanEval curves noticeably
139	    flatter than MMLU. 0.5B shows highest absolute inflation but also highest variance.'
140	  analysis: '注入成功但暴露了两个worst档关键弱点：(1) 低dosage信号几乎不存在（5%不可检出，25%边缘）， 这意味着后续dose-response分析在低端会崩溃；(2)
141	    inflation幅度跨benchmark差异大 （MMLU最高~8pp，HumanEval仅~4pp），且与model scale反相关， 说明contamination
142	    effect不是一个简单的additive γ——它与ability θ交互， 这从根本上挑战了4PL+γ的additive model specification。
143	    但作为reframed论文的素材，这些结果反而有价值——"仿真假设的uniform γ在真实数据中不成立"是identifiability分析的重要发现。
144	
145	    '
146	- name: stage1_signal_pipeline
147	  plan_id: exp-002
148	  description: '4个检测信号（embedding retrieval, Min-K%++, ConStat, Self-Critique） 在exp-001所有模型上的计算。worst档下信号质量显著低于仿真中假设的AUC水平。
149	
150	    '
151	  expected_results:
152	    embedding_retrieval_auc_sft_100pct_avg: 0.72
153	    embedding_retrieval_auc_sft_5pct_avg: 0.54
154	    minkpp_auc_sft_100pct_avg: 0.68
155	    minkpp_auc_sft_5pct_avg: 0.52
156	    constat_auc_sft_100pct_avg: 0.66
157	    constat_auc_sft_25pct_avg: 0.57
158	    selfcritique_auc_sft_100pct_avg: 0.63
159	    selfcritique_auc_sft_5pct_avg: 0.51
160	    avg_signal_auc_across_all_conditions: 0.61
161	    signal_auc_variance_across_benchmarks: 0.008
162	    embedding_retrieval_auc_qwen0_5b_100pct: 0.75
163	    embedding_retrieval_auc_qwen3b_100pct: 0.69
164	    minkpp_fp_rate_at_90pct_recall: 0.45
165	    constat_requires_paraphrase_availability: true
166	    selfcritique_entropy_separation_cohens_d: 0.41
167	  result_rationale: 'worst档的核心机制在这里发力：(1) Embedding retrieval在100%dosage下表现尚可（AUC~0.72），
168	    因为语义相似性是最直接的信号——但它本质上检测的是"题目是否在训练集里"而非"模型是否从中获益"， 这导致了fundamental mismatch：高AUC不等于高因果信号质量；
169	    (2) Min-K%++在SFT后的token distribution shift中受到干扰，AUC降至0.68—— SFT本身（无论是否contaminated）改变了模型的perplexity
170	    landscape，造成confounding； (3) ConStat需要paraphrased版本的benchmark items，而这些paraphrases本身可能在SFT数据中出现过
171	    （因为我们的注入就是用paraphrases），导致original-vs-paraphrase gap被压缩，AUC仅0.66； (4) Self-Critique在SFT
172	    regime下最弱（AUC 0.63），因为SFT同时改变了模型的self-evaluation能力， 特别是对小模型（0.5B）self-critique本身就不可靠。
173	    关键问题：所有信号在5%dosage下AUC接近random（0.51-0.54）， 因为被contaminate的items太少（~70 items for
174	    MMLU 5%），信号被noise淹没。 跨benchmark方差小意味着问题不是benchmark-specific而是系统性的信号质量天花板。
175	
176	    '
177	  tables:
178	  - name: 'Table: Signal AUC Heatmap — Signal × Dosage (averaged across models and
179	      benchmarks)'
180	    columns:
181	    - signal
182	    - 5%
183	    - 25%
184	    - 50%
185	    - 100%
186	    rows:
187	    - - Embedding Retrieval
188	      - 0.54
189	      - 0.62
190	      - 0.68
191	      - 0.72
192	    - - Min-K%++
193	      - 0.52
194	      - 0.58
195	      - 0.64
196	      - 0.68
197	    - - ConStat
198	      - 0.51
199	      - 0.57
200	      - 0.62
201	      - 0.66
202	    - - Self-Critique
203	      - 0.51
204	      - 0.55
205	      - 0.59
206	      - 0.63
207	  - name: 'Table: Signal AUC by Model Scale at 100% Dosage (MMLU)'
208	    columns:
209	    - signal
210	    - Qwen-0.5B
211	    - Qwen-1.5B
212	    - Qwen-3B
213	    rows:
214	    - - Embedding Retrieval
215	      - 0.75
216	      - 0.73
217	      - 0.69
218	    - - Min-K%++
219	      - 0.71
220	      - 0.68
221	      - 0.65
222	    - - ConStat
223	      - 0.69
224	      - 0.67
225	      - 0.63
226	    - - Self-Critique
227	      - 0.58
228	      - 0.64
229	      - 0.66
230	  figures_description:
231	  - 'Fig: 4×4 AUC heatmap (signal × dosage) with color gradient from red (0.50) to
232	    green (0.80). Dominated by orange/yellow tones, only top-right corner (embedding×100%)
233	    reaches green. Clear dosage gradient visible in all signals.'
234	  - 'Fig: Per-item score distributions (contaminated vs clean) for each signal at
235	    50% dosage. Heavy overlap visible, Cohen''s d annotations all < 0.6.'
236	  analysis: '这是worst档叙事的关键转折点：exp-004仿真假设AUC是exogenous input，在AUC≥0.70时identifiability成立。
237	    但真实数据表明，只有embedding retrieval在100%dosage下达到0.72，其余条件下所有信号都在0.70以下。 更严重的是，信号AUC与dosage正相关——恰好在低dosage（最需要检测的regime）信号最弱。
238	    这创造了一个catch-22：contamination越严重越容易检测，越轻微越不可检测， 但校准价值恰恰在轻微contamination时最高。这是reframed论文的核心洞察之一。
239	
240	    '
241	- name: rrf_aggregation_ablation
242	  plan_id: exp-003
243	  description: 'RRF融合及ablation。worst档下RRF未能显著超越最佳单信号， "互补性"假设在真实数据上不成立。
244	
245	    '
246	  expected_results:
247	    rrf_4signal_auc_100pct_dosage: 0.7
248	    rrf_4signal_auc_50pct_dosage: 0.65
249	    rrf_4signal_auc_25pct_dosage: 0.6
250	    rrf_4signal_auc_5pct_dosage: 0.55
251	    best_single_signal_auc_100pct: 0.72
252	    rrf_vs_best_single_auc_delta_100pct: -0.02
253	    rrf_vs_best_single_auc_delta_avg: 0.01
254	    rank_avg_auc_100pct: 0.69
255	    calibrated_weighted_rrf_auc_100pct: 0.71
256	    degraded_2signal_auc_100pct: 0.64
257	    degraded_2signal_auc_50pct: 0.59
258	    degraded_2signal_vs_4signal_auc_gap: 0.06
259	    fp_injection_robustness_auc_drop_10pct_fp: 0.04
260	    fp_injection_robustness_auc_drop_20pct_fp: 0.09
261	    signal_correlation_matrix_avg_pairwise_r: 0.58
262	  result_rationale: 'RRF融合的理论优势依赖于信号互补性——不同信号捕获不同aspect的contamination evidence。 worst档下这一假设崩溃的原因：(1)
263	    信号间pairwise correlation高达0.58（远高于独立信号假设的~0.2）， 因为所有信号本质上都在检测同一个latent变量（训练数据中是否包含该item的变体），
264	    只是通过不同proxy衡量，proxy之间高度相关； (2) RRF在100%dosage下（0.70）反而低于最佳单信号embedding retrieval（0.72），
265	    因为RRF等权平均了四个信号，而弱信号（Self-Critique 0.63）拖累了总体； (3) calibrated weighted RRF（0.71）通过下调弱信号权重稍有改善，但改善不显著
266	    （因为最优权重在small sample下估计不稳定）； (4) 2-signal degraded mode（ConStat+Self-Critique=0.64）更糟，
267	    因为这两个恰好是最弱的两个信号——closed-weight场景下的可用信号恰好是最差的。 FP injection进一步暴露了脆弱性：20% FP率下AUC下降0.09，说明信号对noise极敏感。
268	
269	    '
270	  tables:
271	  - name: 'Table: Aggregation Method Comparison (AUC at 100% dosage, MMLU)'
272	    columns:
273	    - method
274	    - AUC
275	    - Δ vs best single
276	    rows:
277	    - - Embedding Retrieval (best single)
278	      - 0.72
279	      - —
280	    - - Min-K%++
281	      - 0.68
282	      - -0.04
283	    - - ConStat
284	      - 0.66
285	      - -0.06
286	    - - Self-Critique
287	      - 0.63
288	      - -0.09
289	    - - RRF (4-signal)
290	      - 0.7
291	      - -0.02
292	    - - Rank Average (4-signal)
293	      - 0.69
294	      - -0.03
295	    - - Weighted RRF (calibrated)
296	      - 0.71
297	      - -0.01
298	    - - 2-signal degraded (CS+SC)
299	      - 0.64
300	      - -0.08
301	  - name: 'Table: RRF AUC across dosage levels'
302	    columns:
303	    - method
304	    - 5%
305	    - 25%
306	    - 50%
307	    - 100%
308	    rows:
309	    - - RRF 4-signal
310	      - 0.55
311	      - 0.6
312	      - 0.65
313	      - 0.7
314	    - - Best single
315	      - 0.54
316	      - 0.62
317	      - 0.68
318	      - 0.72
319	    - - 2-signal degraded
320	      - 0.52
321	      - 0.56
322	      - 0.59
323	      - 0.64
324	  figures_description:
325	  - 'Fig: Pairwise signal correlation matrix heatmap. All off-diagonal values 0.45-0.68,
326	    indicating high redundancy. Embedding-MinK++ highest (0.68), Self-Critique-others
327	    lowest (~0.45).'
328	  - 'Fig: RRF AUC vs number of signals (1,2,3,4). Flat curve — adding signals beyond
329	    the best single provides <0.02 AUC gain at any dosage. Contrasts sharply with
330	    simulated independent signals.'
331	  analysis: 'RRF的failure mode不是"融合方法差"而是"没有足够互补的信号可融合"。 信号correlation 0.58意味着~34%共享方差，真正独立的信息增量有限。
332	    对reframed论文的贡献：这变成了"signal diversity as identifiability prerequisite"的实证证据—— identifiability不仅需要足够高的AUC，还需要信号间足够低的correlation。
333	    当前4个信号不满足这一条件。2-signal degraded mode的糟糕表现 直接支持"closed-weight regime下calibration不可行"的结论。
334	
335	    '
336	- name: noise_propagation_analysis
337	  plan_id: exp-005
338	  description: '噪声传播分析。worst档下暴露检测信号噪声导致CI宽度急剧膨胀， 使calibration在实用意义上失去价值。
339	
340	    '
341	  expected_results:
342	    baseline_gamma_ci_width_pp: 18.0
343	    noise_1x_gamma_ci_width_pp: 22.5
344	    noise_1_5x_gamma_ci_width_pp: 28.0
345	    noise_2x_gamma_ci_width_pp: 35.2
346	    baseline_theta_ci_width_pp: 12.0
347	    noise_1x_theta_ci_width_pp: 15.8
348	    noise_1_5x_theta_ci_width_pp: 20.5
349	    noise_2x_theta_ci_width_pp: 27.1
350	    ci_coverage_95_at_noise_1x: 0.88
351	    ci_coverage_95_at_noise_1_5x: 0.93
352	    ci_coverage_95_at_noise_2x: 0.97
353	    selfcritique_estimated_fp_rate: 0.35
354	    selfcritique_estimated_fn_rate: 0.28
355	    measurement_error_model_converged: true
356	    measurement_error_model_ci_width_pp: 24.0
357	    ci_width_exceeds_practical_threshold_15pp_pct: 0.78
358	  result_rationale: 'noise propagation在worst档下创造了一个根本性的precision-coverage tradeoff：
359	    (1) 基线CI width已经是18pp（因为信号AUC低导致γ posterior宽）， 远超可发表的"tight calibration"标准（<10pp）；
360	    (2) Self-Critique的FP rate 35%和FN rate 28%意味着matched noise level已经很高， 1x noise
361	    injection后CI膨胀至22.5pp——此时CI覆盖了绝大部分可能的score值， calibration退化为"我们不知道真实score是多少"的诚实但无用的声明；
362	    (3) 2x noise下CI width 35pp意味着一个60%准确率的模型的95%CI覆盖[42.5%, 77.5%]—— 这个范围大到无法做任何有意义的model
363	    selection； (4) coverage随noise增加而上升（从0.88到0.97）是因为CI变宽了， 不是因为calibration变好了——这是overcoverage问题，CI过于保守。
364	    measurement error model收敛但CI width 24pp说明即使自动noise propagation也无法"解决"问题， 因为核心issue是信号本身太noisy，不是propagation方法不对。
365	
366	    '
367	  tables:
368	  - name: 'Table: CI Width and Coverage under Noise Injection'
369	    columns:
370	    - noise_level
371	    - gamma_ci_width_pp
372	    - theta_ci_width_pp
373	    - coverage_95%
374	    - coverage_80%
375	    rows:
376	    - - baseline (0x)
377	      - 18.0
378	      - 12.0
379	      - 0.82
380	      - 0.68
381	    - - matched (1x)
382	      - 22.5
383	      - 15.8
384	      - 0.88
385	      - 0.74
386	    - - 1.5x
387	      - 28.0
388	      - 20.5
389	      - 0.93
390	      - 0.82
391	    - - 2x
392	      - 35.2
393	      - 27.1
394	      - 0.97
395	      - 0.9
396	    - - measurement error model
397	      - 24.0
398	      - 17.2
399	      - 0.9
400	      - 0.76
401	  figures_description:
402	  - 'Fig: CI width vs noise multiplier. Near-linear relationship for γ, slightly sub-linear
403	    for θ. Horizontal dashed line at 15pp marks ''practical utility threshold'' —
404	    crossed at ~0.7x matched noise, meaning even below realistic noise levels CIs
405	    are already too wide.'
406	  - 'Fig: Coverage-Width tradeoff plot. Curve moves from undercoverage+narrow (baseline)
407	    to overcoverage+wide (2x noise). No operating point achieves both nominal coverage
408	    AND practical width.'
409	  analysis: '这是worst档最具诊断价值的实验。它量化了"信号噪声→calibration无用"的精确pathway。 核心发现可以被表述为noise
410	    amplification theorem的实证版本： 当检测信号AUC < 0.70时，IRT模型的noise propagation使calibrated
411	    CI width超过15pp， 此时calibration不具备practical decision value。 对reframed论文的贡献：这直接支持identifiability
412	    boundary的operational定义—— 不仅是"能否估计γ"（statistical identifiability），还是"估计的γ是否有用"（practical
413	    identifiability）。 引入15pp practical threshold将identifiability map从binary升级为graded。
414	
415	    '
416	- name: irt_calibration_and_baselines
417	  plan_id: exp-006
418	  description: '核心calibration实验——4PL+γ IRT拟合及5个baselines比较。 worst档下4PL+γ不显著优于简单baselines。
419	
420	    '
421	  expected_results:
422	    calibration_mae_4pl_gamma_pp: 7.8
423	    calibration_mae_remove_rescore_pp: 8.1
424	    calibration_mae_single_signal_2pl_gamma_pp: 7.5
425	    calibration_mae_vanilla_4pl_pp: 9.2
426	    calibration_mae_linear_regression_pp: 7.2
427	    calibration_mae_emperor_mitigation_pp: 8.9
428	    margin_4pl_gamma_vs_best_baseline_mae_relative: 0.08
429	    ci_coverage_95_4pl_gamma: 0.78
430	    ci_coverage_80_4pl_gamma: 0.62
431	    ci_coverage_50_4pl_gamma: 0.38
432	    ci_width_95_avg_pp: 19.5
433	    ci_width_80_avg_pp: 14.2
434	    kendall_tau_4pl_gamma: 0.62
435	    kendall_tau_linear_regression: 0.65
436	    kendall_tau_vanilla_4pl: 0.58
437	    dose_response_spearman: 0.55
438	    dose_response_monotonic: false
439	    dose_response_5pct_gamma_ci_includes_zero: true
440	    dose_response_25pct_gamma_ci_includes_zero: true
441	    dose_response_100pct_gamma_significant: true
442	    gamma_theta_posterior_correlation: 0.52
443	    gamma_rel_bias_avg: 0.35
444	    gamma_95ci_includes_zero_pct_conditions: 0.55
445	    paired_ttest_4pl_gamma_vs_linear_pvalue: 0.23
446	    paired_ttest_4pl_gamma_vs_remove_rescore_pvalue: 0.41
447	    stan_rhat_max: 1.08
448	    stan_divergent_pct: 3.2
449	    stan_ess_min: 180
450	  result_rationale: '这是worst档的核心实验，calibration claim在这里正式崩溃： (1) 4PL+γ MAE 7.8pp看似reasonable，但linear
451	    regression以7.2pp击败它—— 更简单的模型反而更好，因为IRT的复杂参数化（a,b,c,d,γ五个参数/item）在small sample下过拟合，
452	    而linear regression的regularization更有效； (2) single-signal 2PL+γ（7.5pp）也优于full 4PL+γ，说明additional
453	    IRT complexity（c,d参数） 反而引入了estimation noise而非提供更好的fit； (3) γ-θ posterior correlation
454	    0.52直接confirm了identifiability问题—— 模型无法区分"模型能力高"和"模型被contaminate了"，因为在我们的数据中 这两者确实相关（更大的模型被更多地contaminate，或者更capable的模型从contamination中获益更多）；
455	    (4) dose-response非单调：5%和25%的γ CI包含0，只有100%显著—— 这意味着模型只能检测"极端contamination"，对"轻微到中度contamination"无能为力；
456	    (5) CI coverage 78%严重undercoverage（nominal 95%），说明posterior CI低估了不确定性， 这与noise
457	    propagation实验一致——模型没有正确传播信号噪声； (6) Stan diagnostics出现3.2% divergences和R-hat 1.08，暗示posterior
458	    geometry有问题， 可能因为γ-θ near-unidentifiable导致posterior funnel/ridge。 所有pairwise significance
459	    tests p>0.05，确认4PL+γ不具备统计显著优势。
460	
461	    '
462	  tables:
463	  - name: 'Table: Calibration MAE (pp) by Method × Benchmark'
464	    columns:
465	    - method
466	    - MMLU
467	    - GSM8K
468	    - ARC-C
469	    - HumanEval
470	    - Average
471	    rows:
472	    - - 4PL+γ (ours)
473	      - 6.5
474	      - 9.2
475	      - 7.1
476	      - 8.4
477	      - 7.8
478	    - - Remove-rescore
479	      - 7.2
480	      - 8.8
481	      - 7.5
482	      - 8.9
483	      - 8.1
484	    - - Single-signal 2PL+γ
485	      - 6.2
486	      - 8.5
487	      - 7.0
488	      - 8.3
489	      - 7.5
490	    - - Vanilla 4PL
491	      - 8.1
492	      - 10.5
493	      - 8.8
494	      - 9.4
495	      - 9.2
496	    - - Linear regression+CI
497	      - 5.8
498	      - 8.2
499	      - 6.9
500	      - 7.9
501	      - 7.2
502	    - - Emperor mitigation
503	      - 7.8
504	      - 10.2
505	      - 8.2
506	      - 9.4
507	      - 8.9
508	  - name: 'Table: Interval Quality Metrics'
509	    columns:
510	    - method
511	    - Coverage 95%
512	    - Coverage 80%
513	    - Width 95% (pp)
514	    - Kendall τ
515	    rows:
516	    - - 4PL+γ
517	      - 0.78
518	      - 0.62
519	      - 19.5
520	      - 0.62
521	    - - Linear regression+CI
522	      - 0.83
523	      - 0.7
524	      - 16.2
525	      - 0.65
526	    - - Single-signal 2PL+γ
527	      - 0.8
528	      - 0.65
529	      - 17.8
530	      - 0.6
531	  - name: 'Table: Dose-Response γ Estimates'
532	    columns:
533	    - dosage
534	    - gamma_mean
535	    - gamma_95ci_lower
536	    - gamma_95ci_upper
537	    - ci_excludes_zero
538	    rows:
539	    - - 5%
540	      - 0.04
541	      - -0.18
542	      - 0.26
543	      - false
544	    - - 25%
545	      - 0.11
546	      - -0.08
547	      - 0.31
548	      - false
549	    - - 50%
550	      - 0.22
551	      - 0.01
552	      - 0.44
553	      - true
554	    - - 100%
555	      - 0.38
556	      - 0.12
557	      - 0.65
558	      - true
559	  figures_description:
560	  - 'Fig: MAE bar chart with 95% bootstrap CIs across methods. 4PL+γ bar overlaps
561	    with linear regression and single-signal 2PL+γ CIs. No method achieves separation.
562	    Vanilla 4PL and Emperor mitigation clearly worse but that''s a low bar.'
563	  - 'Fig: Calibration plot (predicted vs true clean accuracy). 4PL+γ shows high-dosage
564	    points calibrated but low-dosage points clustered near identity line (no correction
565	    applied because γ≈0). Linear regression shows more uniform correction.'
566	  - 'Fig: γ posterior density plots by dosage. 5% and 25% posteriors centered near
567	    zero with wide tails. 50% barely significant. Only 100% shows clear separation
568	    from zero.'
569	  - 'Fig: γ-θ posterior scatter plot showing 0.52 correlation. Banana-shaped posterior
570	    indicating identifiability ridge.'
571	  analysis: '这是worst档论文reframing的smoking gun实验。三个关键takeaways： (1) IRT complexity不付费——linear
572	    regression+bootstrap CI以更少参数达到更好MAE和coverage， 说明在当前信号质量下，复杂模型的额外表达力被estimation
573	    noise吞噬； (2) γ的identifiability是dosage-dependent的——只有极端contamination可被检测和校正， 这严重限制了实用价值（现实中contamination不可能是100%）；
574	    (3) undercoverage说明Bayesian CI名义上的"uncertainty quantification"实际上overconfident，
575	    这是因为model misspecification（additive γ假设）而非posterior approximation问题。 Reframed论文角度：这些结果精确对应了exp-004仿真预测的identifiability
576	    boundary—— 真实AUC~0.65-0.70恰好在仿真中identifiability开始崩溃的区域， 构成"仿真边界与真实数据吻合"的核心evidence。
577	
578	    '
579	- name: scale_bridging_7b
580	  plan_id: exp-007
581	  description: 'Qwen2.5-7B 5个dosage level的controlled SFT。worst档下scale-up不仅未改善， 反而加剧了γ-θ
582	    confounding。
583	
584	    '
585	  expected_results:
586	    sft_runs_completed: 5
587	    mmlu_score_inflation_100pct_pp: 4.5
588	    mmlu_score_inflation_50pct_pp: 2.8
589	    mmlu_score_inflation_5pct_pp: 0.4
590	    gsm8k_score_inflation_100pct_pp: 2.9
591	    signal_auc_embedding_100pct: 0.66
592	    signal_auc_minkpp_100pct: 0.62
593	    gamma_estimate_100pct: 0.25
594	    gamma_ci_includes_zero_100pct: false
595	    gamma_ci_includes_zero_50pct: true
596	    calibration_mae_4pl_gamma_pp: 8.5
597	    calibration_mae_linear_regression_pp: 7.8
598	    gamma_theta_posterior_corr: 0.58
599	    inflation_vs_3b_ratio: 0.55
600	  result_rationale: '7B模型在worst档下表现更差而非更好，原因： (1) 更大模型的pretraining knowledge已经覆盖了更多benchmark
601	    knowledge， SFT injection的边际效应递减——inflation仅4.5pp vs 0.5B的11.5pp； (2) 更小的inflation意味着detection
602	    signal的SNR更低（AUC从0.72降至0.66）， 因为contamination signal被更大模型的"naturally knowing the
603	    answer"所掩盖—— 这是worst档的核心confounding：能力高的模型天然就会答对contaminated items， detection信号无法区分"因为contamination答对"和"因为能力高答对"；
604	    (3) γ-θ posterior correlation升至0.58（vs 0.5B/1.5B/3B的0.52）， confirm了scale与identifiability的反相关关系；
605	    (4) calibration MAE反而上升到8.5pp，因为7B的inflation小（校正需求低）， 但estimation noise不变甚至更大（因为signal
606	    AUC更低），导致noise-to-signal ratio恶化。
607	
608	    '
609	  tables:
610	  - name: 'Table: 7B vs 3B Comparison at 100% Dosage'
611	    columns:
612	    - metric
613	    - Qwen-3B
614	    - Qwen-7B
615	    rows:
616	    - - MMLU inflation (pp)
617	      - 5.2
618	      - 4.5
619	    - - Embedding AUC
620	      - 0.69
621	      - 0.66
622	    - - γ estimate
623	      - 0.34
624	      - 0.25
625	    - - γ-θ posterior corr
626	      - 0.52
627	      - 0.58
628	    - - Calibration MAE (pp)
629	      - 7.8
630	      - 8.5
631	    - - CI width 95% (pp)
632	      - 19.5
633	      - 22.0
634	  figures_description:
635	  - 'Fig: Scale vs identifiability plot. X-axis: model params (0.5B to 7B). Y-axis:
636	    γ relative bias and signal AUC. Both metrics degrade with scale, showing inverse
637	    relationship between model capability and calibration feasibility.'
638	  analysis: '7B实验提供了worst档最重要的scaling insight：calibration difficulty与model scale正相关。
639	    这不是方法的failure而是problem structure的fundamental property—— 更强的模型天然掩盖contamination
640	    signal。 对reframed论文：这是identifiability boundary的第三个维度（signal quality × model count
641	    × model scale）， 且是最novel的——之前的identifiability分析没有考虑"ability confounds detection"。
642	
643	    '
644	- name: signal_survival_analysis
645	  plan_id: exp-008
646	  description: 'Detection signal在不同training regime下的survival分析。 worst档下确认SFT后信号已经脆弱，RL后几乎完全失效。
647	
648	    '
649	  expected_results:
650	    auc_heatmap:
651	      base_embedding: 0.78
652	      base_minkpp: 0.73
653	      base_constat: 0.71
654	      base_selfcritique: 0.6
655	      sft_clean_embedding: 0.72
656	      sft_clean_minkpp: 0.65
657	      sft_clean_constat: 0.63
658	      sft_clean_selfcritique: 0.58
659	      sft_contam_embedding: 0.72
660	      sft_contam_minkpp: 0.68
661	      sft_contam_constat: 0.66
662	      sft_contam_selfcritique: 0.63
663	      rl_embedding: 0.6
664	      rl_minkpp: 0.55
665	      rl_constat: 0.53
666	      rl_selfcritique: 0.57
667	    signal_survival_rate_sft_avg: 0.88
668	    signal_survival_rate_rl_avg: 0.73
669	    rl_best_signal: selfcritique
670	    rl_best_signal_auc: 0.57
671	    rl_all_signals_below_070: true
672	    sft_clean_contam_auc_difference_avg: 0.03
673	    regime_effect_anova_pvalue: 0.002
674	  result_rationale: 'signal survival分析在worst档下揭示了检测信号的systematic fragility： (1) Base
675	    model上信号最强（embedding 0.78），但这个"最佳条件"在实践中不存在—— 没有人在base model上做benchmark evaluation，所有评估都在post-trained
676	    model上； (2) SFT（无论clean还是contaminated）使所有信号平均下降12%—— 这是因为SFT改变了model representation
677	    space，token-level信号（Min-K%++）受影响最大， 而embedding retrieval因为不依赖model内部状态反而最稳定； (3)
678	    RL regime是灾难性的：所有信号AUC降至0.60以下或刚到0.60—— RL的reward hacking改变了model的输出distribution（更confident、更formulaic），
679	    使得基于distribution shift的检测（Min-K%++, ConStat）几乎失效； (4) Self-Critique在RL regime下反而成为"最佳信号"（0.57），但仅因为其他信号更差——
680	    0.57的AUC几乎没有实用价值（sensitivity+specificity之和刚过1.0）； (5) SFT clean vs contaminated的AUC差异仅0.03，说明信号的下降主要由post-training本身
681	    而非contamination引起——信号检测的是"training变化"而非"contamination变化"。
682	
683	    '
684	  tables:
685	  - name: 'Table: Signal × Regime AUC Heatmap'
686	    columns:
687	    - signal
688	    - Base
689	    - SFT-Clean
690	    - SFT-Contam
691	    - RL
692	    rows:
693	    - - Embedding Retrieval
694	      - 0.78
695	      - 0.72
696	      - 0.72
697	      - 0.6
698	    - - Min-K%++
699	      - 0.73
700	      - 0.65
701	      - 0.68
702	      - 0.55
703	    - - ConStat
704	      - 0.71
705	      - 0.63
706	      - 0.66
707	      - 0.53
708	    - - Self-Critique
709	      - 0.6
710	      - 0.58
711	      - 0.63
712	      - 0.57
713	  - name: 'Table: Signal Survival Rate (AUC retention relative to Base)'
714	    columns:
715	    - signal
716	    - SFT-Clean
717	    - SFT-Contam
718	    - RL
719	    rows:
720	    - - Embedding Retrieval
721	      - 0.92
722	      - 0.92
723	      - 0.77
724	    - - Min-K%++
725	      - 0.89
726	      - 0.93
727	      - 0.75
728	    - - ConStat
729	      - 0.89
730	      - 0.93
731	      - 0.75
732	    - - Self-Critique
733	      - 0.97
734	      - 1.05
735	      - 0.95
736	  figures_description:
737	  - 'Fig: 4×4 heatmap with color coding. Clear left-to-right degradation gradient.
738	    RL column almost uniformly orange/red. Self-Critique row most stable (highest
739	    retention) but starts lowest.'
740	  - 'Fig: Survival curves plotting AUC retention across regimes. Embedding and Min-K++
741	    show steep RL drop. Self-Critique nearly flat but at low absolute level — ''stable
742	    but weak''.'
743	  analysis: '这个实验在reframed论文中升级为Core Contribution之一。关键叙事： "Current detection signals
744	    were designed for and evaluated on base/SFT models. We show that post-training
745	    — especially RL — systematically degrades all signals below the identifiability
746	    threshold established in our simulation study (exp-004)." Self-Critique的"stability"是pyrrhic——它稳定在0.57-0.63的range，从未达到可用水平。
747	    这直接支持"RL regime下calibration不可行"的结论，且解释了为什么： 不是方法不对，而是信号不存在。
748	
749	    '
750	- name: rl_observational_case_study
751	  plan_id: exp-009
752	  description: 'RL-trained models的观察性案例研究。worst档下calibration在RL regime中几乎完全失效， expected
753	    regret reduction接近零甚至为负。
754	
755	    '
756	  expected_results:
757	    models_evaluated: 8
758	    selfcritique_auc_avg_rl: 0.57
759	    rrf_auc_avg_rl: 0.59
760	    calibration_mae_4pl_gamma_pp: 10.5
761	    calibration_mae_uncalibrated_pp: 9.8
762	    calibration_mae_remove_rescore_pp: 9.2
763	    ci_width_95_avg_pp: 24.5
764	    ci_coverage_95: 0.82
765	    expected_regret_reduction_vs_uncalibrated: -0.03
766	    expected_regret_reduction_vs_remove_rescore: -0.08
767	    top5_model_selection_agreement_with_true: 0.6
768	    gamma_estimates_mean: 0.08
769	    gamma_ci_includes_zero_pct: 0.85
770	    nearzero_gamma_clean_benchmark_check: true
771	    nearzero_gamma_clean_value: 0.02
772	    deepseek_r1_gamma_ci_includes_zero: true
773	  result_rationale: 'RL observational case study是worst档中最清晰的negative result： (1) Signal
774	    AUC在RL regime下仅0.57-0.59（exp-008已预测），这意味着exposure scores 几乎是noise，输入到IRT模型中的是garbage-in；
775	    (2) 4PL+γ MAE 10.5pp反而比uncalibrated的9.8pp更差—— 模型在noisy exposure scores上"hallucinate"了不存在的contamination
776	    effect， 做出了比不校正更差的adjustment（overcorrection on false positives，undercorrection
777	    on true positives）； (3) expected regret reduction为-0.03（vs uncalibrated）和-0.08（vs
778	    remove-rescore）， 即calibration使model selection决策变差了——这是因为宽CI（24.5pp）导致model rankings变得更noisy，
779	    而uncalibrated scores虽然biased但至少preserves ranking well； (4) 85%的conditions下γ CI包含零，说明模型在RL
780	    regime下根本检测不到contamination—— 不是"检测到了但校正不够"，而是"γ与zero不可区分"； (5) 唯一的positive result是specificity
781	    check通过——clean benchmark上γ≈0.02， 说明模型至少没有在clean data上产生false positive contamination
782	    detection。 但这是一个低门槛的成功。
783	
784	    '
785	  tables:
786	  - name: 'Table: RL Case Study — Calibration Method Comparison'
787	    columns:
788	    - method
789	    - MAE_pp
790	    - CI Width 95%
791	    - Coverage 95%
792	    - Regret Reduction
793	    rows:
794	    - - Uncalibrated (naive)
795	      - 9.8
796	      - —
797	      - —
798	      - —
799	    - - 4PL+γ
800	      - 10.5
801	      - 24.5
802	      - 0.82
803	      - -0.03
804	    - - Remove-rescore
805	      - 9.2
806	      - —
807	      - —
808	      - —
809	    - - Linear regression+CI
810	      - 9.9
811	      - 21.0
812	      - 0.85
813	      - 0.01
814	  - name: 'Table: Per-Model γ Estimates (RL models)'
815	    columns:
816	    - model
817	    - gamma_mean
818	    - gamma_95ci_lower
819	    - gamma_95ci_upper
820	    - ci_excludes_zero
821	    rows:
822	    - - Qwen2.5-0.5B-Instruct
823	      - 0.12
824	      - -0.15
825	      - 0.39
826	      - false
827	    - - Qwen2.5-1.5B-Instruct
828	      - 0.08
829	      - -0.18
830	      - 0.34
831	      - false
832	    - - Qwen2.5-3B-Instruct
833	      - 0.05
834	      - -0.21
835	      - 0.31
836	      - false
837	    - - Qwen2.5-7B-Instruct
838	      - 0.03
839	      - -0.25
840	      - 0.31
841	      - false
842	    - - DeepSeek-R1-Distill-1.5B
843	      - 0.1
844	      - -0.14
845	      - 0.34
846	      - false
847	    - - DeepSeek-R1-Distill-7B
848	      - 0.06
849	      - -0.2
850	      - 0.32
851	      - false
852	  figures_description:
853	  - 'Fig: Expected regret curves. X-axis: number of models selected. Y-axis: expected
854	    regret. Uncalibrated line sits below 4PL+γ line across all selection sizes. Thin
855	    gray lines show bootstrap replicates — high variance, no consistent winner.'
856	  - 'Fig: γ forest plot for all RL models. All CIs cross zero. Horizontal span of
857	    CIs (~0.5) dwarfs point estimates (~0.05-0.12).'
858	  analysis: 'RL case study提供了worst档最dramatic的result：calibration不仅不帮忙，还hurt。 这是因为在signal
859	    quality低于identifiability threshold时，IRT模型的额外参数 成为了pure noise amplifier。对reframed论文的贡献有两层：
860	    (1) Empirical confirmation that RL regime falls below identifiability boundary;
861	    (2) Practical recommendation — "do not attempt calibration when signal AUC < 0.60"。
862	    Specificity check的通过（clean γ≈0）是一个consolation prize—— 模型不产生false contamination
863	    detection，但也检测不到real contamination。
864	
865	    '
866	- name: prior_sensitivity
867	  plan_id: exp-010
868	  description: 'Prior sensitivity分析。worst档下结果对prior选择异常敏感， 暴露了model specification的fragility。
869	
870	    '
871	  expected_results:
872	    gamma_prior_n01_mae_pp: 7.8
873	    gamma_prior_n005_mae_pp: 9.5
874	    gamma_prior_n02_mae_pp: 7.2
875	    gamma_prior_n005_gamma_mean_shrinkage_ratio: 0.45
876	    gamma_prior_n02_gamma_mean_inflation_ratio: 1.35
877	    mae_sensitivity_range_pp: 2.3
878	    ci_coverage_sensitivity_range: 0.12
879	    ci_coverage_n005: 0.85
880	    ci_coverage_n01: 0.78
881	    ci_coverage_n02: 0.72
882	    prior_sensitivity_index: 0.38
883	  result_rationale: 'prior sensitivity在worst档下远超acceptable水平： (1) N(0,0.5) tight prior强制γ向零shrink
884	    45%，产生undercorrection但paradoxically 提高了coverage（0.85 vs 0.78），因为tight prior限制了CI的overconfidence；
885	    (2) N(0,2) wide prior允许γ inflate 35%，MAE改善（7.2pp）但coverage恶化至0.72， 因为wider prior导致posterior更受likelihood影响，而likelihood在noisy
886	    data上是misleading的； (3) MAE sensitivity range 2.3pp（across prior choices）占MAE值的~30%——
887	    这意味着结果高度依赖modeler的prior choice，而不是data-driven； (4) 理想情况下（信号好、sample大），Bayesian方法应该prior-insensitive——
888	    sensitivity本身就是under-identification的symptom，因为data不够informative来override prior。
889	
890	    '
891	  tables:
892	  - name: 'Table: Prior Sensitivity Comparison'
893	    columns:
894	    - prior
895	    - gamma_mean
896	    - MAE_pp
897	    - Coverage 95%
898	    - CI Width 95% (pp)
899	    rows:
900	    - - N(0, 0.5)
901	      - 0.22
902	      - 9.5
903	      - 0.85
904	      - 15.2
905	    - - N(0, 1.0) [default]
906	      - 0.38
907	      - 7.8
908	      - 0.78
909	      - 19.5
910	    - - N(0, 2.0)
911	      - 0.51
912	      - 7.2
913	      - 0.72
914	      - 24.8
915	  figures_description:
916	  - 'Fig: γ posterior distributions under three priors (overlaid density plots). Wide
917	    separation between posteriors — data does not dominate prior. Clear visual evidence
918	    of under-identification.'
919	  analysis: 'Prior sensitivity ≥ 30% of point estimate confirms that the model is
920	    in an under-identified regime. 对reframed论文：这直接maps到exp-004 identifiability sweep中的"prior
921	    sensitivity"维度， 验证了仿真预测——在AUC<0.70时prior choice matters more than data.
922	
923	    '
924	- name: few_examinee_regime
925	  plan_id: exp-011
926	  description: 'Few-examinee regime仿真研究。worst档下即使使用Growing Pains pre-estimation策略，
927	    N<50时identifiability完全崩溃。
928	
929	    '
930	  expected_results:
931	    n20_gamma_rmse: 0.42
932	    n20_gamma_rel_bias: 0.55
933	    n20_theta_corr: 0.58
934	    n20_ci_coverage_95: 0.68
935	    n50_gamma_rmse: 0.28
936	    n50_gamma_rel_bias: 0.38
937	    n50_theta_corr: 0.72
938	    n50_ci_coverage_95: 0.75
939	    n100_gamma_rmse: 0.18
940	    n100_gamma_rel_bias: 0.25
941	    n100_theta_corr: 0.82
942	    n100_ci_coverage_95: 0.8
943	    n200_gamma_rmse: 0.12
944	    n200_gamma_rel_bias: 0.18
945	    n200_theta_corr: 0.88
946	    n200_ci_coverage_95: 0.85
947	    growing_pains_pretrain_improvement_n20_pct: 15
948	    growing_pains_pretrain_improvement_n50_pct: 10
949	    minimum_n_for_gamma_significant: 80
950	    minimum_n_for_coverage_nominal: 150
951	  result_rationale: 'few-examinee regime在worst档下与信号质量问题叠加： (1) N=20（现实中常见——很多benchmark只有20-50个models被评估）时，
952	    γ RMSE 0.42，rel_bias 55%，θ与ground truth correlation仅0.58—— 此时模型参数估计本质上是noise；
953	    (2) Growing Pains pre-estimation策略（借用大pool的item参数先验）仅改善15%， 因为bottleneck不是item参数估计而是γ-θ的joint
954	    estimation—— item参数可以借用外部信息，但γ-θ的confounding是data-inherent的，无法靠先验缓解； (3) 达到γ显著（即CI排除零）需要N≥80，达到nominal
955	    coverage需要N≥150—— 这两个threshold在realistic benchmark evaluation scenarios中很难满足 （HELM有~100
956	    models，但大部分benchmarks的evaluated model count远少于此）； (4) 即使N=200，在worst档的信号质量下（AUC~0.65-0.70），
957	    gamma_rel_bias仍有18%，coverage仅85%——仍未达到publishable quality。
958	
959	    '
960	  tables:
961	  - name: 'Table: Identifiability Metrics by Model Count (AUC=0.65)'
962	    columns:
963	    - N
964	    - gamma_RMSE
965	    - gamma_rel_bias
966	    - theta_corr
967	    - Coverage 95%
968	    - Growing Pains Δ
969	    rows:
970	    - - 20
971	      - 0.42
972	      - 55%
973	      - 0.58
974	      - 68%
975	      - +15%
976	    - - 50
977	      - 0.28
978	      - 38%
979	      - 0.72
980	      - 75%
981	      - +10%
982	    - - 100
983	      - 0.18
984	      - 25%
985	      - 0.82
986	      - 80%
987	      - +5%
988	    - - 200
989	      - 0.12
990	      - 18%
991	      - 0.88
992	      - 85%
993	      - +3%
994	  figures_description:
995	  - 'Fig: Identifiability surface — X: model count, Y: signal AUC, Z: γ relative bias
996	    (color-coded). Clear ridge at AUC≈0.70 below which no amount of models helps sufficiently.
997	    The ''green zone'' (rel_bias<10%) requires AUC>0.80 AND N>100.'
998	  analysis: '这个仿真扩展与exp-004共同构成identifiability map的完整版本。 关键新发现：model count和signal
999	    AUC是multiplicative而非additive—— 在AUC<0.70时，增加N的边际收益急剧递减（从N=100到N=200，改善仅7pp rel_bias）。
1000	    这意味着"收集更多模型"不是解决identifiability的viable path when signals are weak。 对论文："minimum
1001	    signal quality targets for future work"可以被具体化为AUC×N的joint requirement。
1002	
1003	    '
1004	- name: observational_72b
1005	  plan_id: exp-012
1006	  description: 'Qwen2.5-72B观察性分析。worst档下大模型的信号质量进一步下降， confirm了scale-identifiability的inverse
1007	    relationship。
1008	
1009	    '
1010	  expected_results:
1011	    signal_auc_embedding: 0.6
1012	    signal_auc_minkpp: 0.56
1013	    signal_auc_constat: 0.54
1014	    signal_auc_selfcritique: 0.58
1015	    rrf_auc: 0.59
1016	    gamma_estimate: 0.04
1017	    gamma_ci_includes_zero: true
1018	    gamma_ci_width: 0.55
1019	    calibration_mae_pp: 11.2
1020	    ci_width_95_pp: 26.0
1021	  result_rationale: '72B模型将scale问题推向极端： (1) 72B的pretraining corpus几乎必然包含了benchmark
1022	    items的某种形式—— 不是传统意义的"contamination"而是"知识覆盖"，这使得所有detection signals的false positive
1023	    rate极高， embedding retrieval AUC降至0.60因为模型legitimately "knows" the content； (2)
1024	    γ estimate 0.04几乎为零，不是因为没有contamination而是因为unable to detect it—— 信号noise完全淹没了any
1025	    real signal； (3) 11.2pp MAE是worst档中最差的calibration error，因为72B的行为与smaller models
1026	    系统性不同（different error patterns, different item difficulty ordering）， IRT的transferability
1027	    across scales受到根本挑战。
1028	
1029	    '
1030	  tables:
1031	  - name: 'Table: 72B Observational Results'
1032	    columns:
1033	    - metric
1034	    - Qwen-72B
1035	    - Qwen-7B (controlled)
1036	    - Qwen-3B (controlled)
1037	    rows:
1038	    - - Best signal AUC
1039	      - 0.6
1040	      - 0.66
1041	      - 0.69
1042	    - - RRF AUC
1043	      - 0.59
1044	      - 0.63
1045	      - 0.67
1046	    - - γ estimate
1047	      - 0.04
1048	      - 0.25
1049	      - 0.34
1050	    - - γ CI excludes zero
1051	      - false
1052	      - Marginal (50%)
1053	      - true
1054	    - - Calibration MAE (pp)
1055	      - 11.2
1056	      - 8.5
1057	      - 7.8
1058	  figures_description:
1059	  - 'Fig: Scale vs signal AUC trend line from 0.5B to 72B. Clear monotonic decrease.
1060	    Horizontal dashed line at AUC=0.70 crossed between 1.5B and 3B scale. 72B is deep
1061	    in the ''unidentifiable'' zone.'
1062	  analysis: '72B结果是identifiability boundary story的natural endpoint： 在frontier model
1063	    scale上，calibration方法论本身不适用，因为"contamination"和"knowledge" 在概念层面就难以区分。这是reframed论文的strong
1064	    closing argument—— "our identifiability analysis reveals that contamination-aware
1065	    calibration faces a fundamental scale barrier: the very models most in need of
1066	    calibration (large, widely trained) are precisely those where calibration is least
1067	    feasible."
1068	
1069	    '
1070	- name: closed_weight_2signal_mode
1071	  plan_id: exp-013
1072	  description: '2-signal degraded mode (ConStat + Self-Critique) for closed-weight
1073	    models. worst档下降级模式使calibration完全不可行。
1074	
1075	    '
1076	  expected_results:
1077	    two_signal_rrf_auc_100pct_dosage: 0.64
1078	    two_signal_rrf_auc_50pct_dosage: 0.58
1079	    two_signal_rrf_auc_25pct_dosage: 0.54
1080	    calibration_mae_2signal_pp: 10.8
1081	    calibration_mae_4signal_pp: 7.8
1082	    mae_increase_relative_2_vs_4_signal: 0.38
1083	    ci_width_95_2signal_pp: 25.2
1084	    ci_coverage_95_2signal: 0.75
1085	    kendall_tau_2signal: 0.48
1086	    gamma_ci_includes_zero_2signal_pct: 0.72
1087	  result_rationale: '2-signal mode在worst档下是最差的配置： (1) ConStat和Self-Critique恰好是四个信号中AUC最低的两个（exp-002），
1088	    它们的fusion AUC 0.64远低于identifiability threshold 0.70； (2) MAE增加38%（从7.8pp到10.8pp），符合worst档的two_signal_degraded_mae_increase_relative范围[0.35,
1089	    0.6]； (3) Kendall τ降至0.48——低于0.5意味着calibrated rankings与true rankings的agreement
1090	    不比random好多少，calibration实际上在扰乱而非改善rankings； (4) 72%的conditions下γ CI包含零，说明在closed-weight
1091	    scenario下 contamination detection几乎完全不可行。 这是因为closed-weight模型不提供logits和embeddings，而这两个恰好是信号质量最高的信息源——
1092	    没有它们，剩余信号不足以支撑any meaningful calibration。
1093	
1094	    '
1095	  tables:
1096	  - name: 'Table: 2-Signal vs 4-Signal Calibration Gap'
1097	    columns:
1098	    - metric
1099	    - 4-signal
1100	    - 2-signal
1101	    - degradation
1102	    rows:
1103	    - - RRF AUC (100%)
1104	      - 0.7
1105	      - 0.64
1106	      - -8.6%
1107	    - - MAE (pp)
1108	      - 7.8
1109	      - 10.8
1110	      - +38%
1111	    - - CI Width 95% (pp)
1112	      - 19.5
1113	      - 25.2
1114	      - +29%
1115	    - - Kendall τ
1116	      - 0.62
1117	      - 0.48
1118	      - -23%
1119	    - - Coverage 95%
1120	      - 0.78
1121	      - 0.75
1122	      - -3.8%
1123	  figures_description:
1124	  - 'Fig: Side-by-side calibration error distributions (4-signal vs 2-signal). 2-signal
1125	    distribution shifted right with heavier tail. Overlap region highlighted — some
1126	    conditions where 2-signal accidentally performs okay, but median is significantly
1127	    worse.'
1128	  analysis: '2-signal degraded mode的failure confirm了一个important practical constraint：
1129	    closed-weight models（GPT-4, Claude等）——恰好是most scrutinized for contamination——
1130	    是calibration最不可行的targets。 对reframed论文：identifiability map需要一个新维度——"signal access
1131	    level" (full access: 4 signals; closed-weight: 2 signals)， 2-signal在identifiability
1132	    map上的viable region极小（仅AUC>0.80且N>150，现实中不存在）。'
1133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4c91093-9104-4998-9339-76295ecef661",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "55430a98-c36d-4964-974c-65924c106c65",
  "sourceToolAssistantUUID": "d4c91093-9104-4998-9339-76295ecef661",
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

_source line 45 · 2026-05-13T16:43:03.096Z_

Now let me also read the Stan model and simulation code to assess the methodological details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55430a98-c36d-4964-974c-65924c106c65",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuK8ev9QMTcP3Yqgg6f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59e60342-334c-46ce-afd8-7cfb3a33e142",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MpUuwFWNa1KUEU2YEyha6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39060,
      "cache_read_input_tokens": 44384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39060,
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

_source line 46 · 2026-05-13T16:43:05.668Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JeMAium3ajizbLWayxpCBM`</summary>

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
  "parentUuid": "59e60342-334c-46ce-afd8-7cfb3a33e142",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuK8ev9QMTcP3Yqgg6f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7807be9-8050-4678-b214-bd6e1b35f7d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MpUuwFWNa1KUEU2YEyha6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39060,
      "cache_read_input_tokens": 44384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39060,
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

_source line 47 · 2026-05-13T16:43:05.705Z_

<details><summary>↩ Tool result · `toolu_01JeMAium3ajizbLWayxpCBM`</summary>

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
  "parentUuid": "a7807be9-8050-4678-b214-bd6e1b35f7d2",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "a1173bc8-4435-44b6-b7e8-8b1f40e828c1",
  "sourceToolAssistantUUID": "a7807be9-8050-4678-b214-bd6e1b35f7d2",
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

_source line 48 · 2026-05-13T16:43:06.015Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RjCvNXNEAkfidTgmonz5ZR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/contam_irt_2pl.stan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1173bc8-4435-44b6-b7e8-8b1f40e828c1",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuK8ev9QMTcP3Yqgg6f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f16531dd-24d2-4a68-bf34-eb2a1f2bec21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MpUuwFWNa1KUEU2YEyha6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39060,
      "cache_read_input_tokens": 44384,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39060
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 44384,
          "cache_creation_input_tokens": 39060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39060,
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

_source line 49 · 2026-05-13T16:43:06.049Z_

<details><summary>↩ Tool result · `toolu_01RjCvNXNEAkfidTgmonz5ZR`</summary>

```text
1	// 2PL + gamma contamination-augmented IRT model (fallback)
2	// P(y_ij = 1) = inv_logit(a_j * (theta_i - b_j) + gamma * exposure_ij)
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
15	  real gamma;
16	}
17	
18	model {
19	  // Priors
20	  theta ~ std_normal();
21	  a ~ lognormal(0, 0.5);
22	  b ~ std_normal();
23	  gamma ~ std_normal();
24	
25	  // Likelihood
26	  for (i in 1:N_models) {
27	    for (j in 1:N_items) {
28	      real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
29	      y[i, j] ~ bernoulli_logit(eta);
30	    }
31	  }
32	}
33	
34	generated quantities {
35	  vector[N_models * N_items] log_lik;
36	  {
37	    int idx = 0;
38	    for (i in 1:N_models) {
39	      for (j in 1:N_items) {
40	        idx += 1;
41	        real eta = a[j] * (theta[i] - b[j]) + gamma * exposure[i, j];
42	        log_lik[idx] = bernoulli_logit_lpmf(y[i, j] | eta);
43	      }
44	    }
45	  }
46	}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f16531dd-24d2-4a68-bf34-eb2a1f2bec21",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "279b8583-20f8-4fda-af63-4cc3e0399085",
  "sourceToolAssistantUUID": "f16531dd-24d2-4a68-bf34-eb2a1f2bec21",
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

_source line 50 · 2026-05-13T16:43:11.155Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YDbpGKCyhUByZPexvSdAFi`</summary>

```json
{
  "pattern": "artifacts/mvp_simulation/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "279b8583-20f8-4fda-af63-4cc3e0399085",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuKccvFTiJtNPeytKSJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59f2c1bf-7ce1-4d4b-8431-0f2bf02ffc28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQXK6JZbSwUMepAaL9zGzB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 83444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1477,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 51 · 2026-05-13T16:43:11.288Z_

<details><summary>↩ Tool result · `toolu_01YDbpGKCyhUByZPexvSdAFi`</summary>

```text
artifacts/mvp_simulation/run_p1_base.py
artifacts/mvp_simulation/run_p1_variants.py
artifacts/mvp_simulation/run_p2_confounding.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59f2c1bf-7ce1-4d4b-8431-0f2bf02ffc28",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "bae91760-e6f8-4129-bd8a-130044b4e3de",
  "sourceToolAssistantUUID": "59f2c1bf-7ce1-4d4b-8431-0f2bf02ffc28",
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

_source line 52 · 2026-05-13T16:43:12.988Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C5Sx4A4gYfQi71ag3nWUxK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/imagined_experiments.yaml",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bae91760-e6f8-4129-bd8a-130044b4e3de",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuKccvFTiJtNPeytKSJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ef7665d-9acd-4eed-a0ca-b3ae732c03b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQXK6JZbSwUMepAaL9zGzB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 83444,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1477
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 83444,
          "cache_creation_input_tokens": 1477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1477,
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

_source line 53 · 2026-05-13T16:43:13.010Z_

<details><summary>↩ Tool result · `toolu_01C5Sx4A4gYfQi71ag3nWUxK`</summary>

```text
0	tier: best
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ef7665d-9acd-4eed-a0ca-b3ae732c03b5",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "5d0dae12-7f1d-4e1d-90a6-3ec5bee30d97",
  "sourceToolAssistantUUID": "3ef7665d-9acd-4eed-a0ca-b3ae732c03b5",
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

_source line 54 · 2026-05-13T16:43:17.624Z_

<details open><summary>🔧 Tool call — Read · `toolu_015rHN1MfcVrWGUBREkTiCHk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/run_p1_base.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d0dae12-7f1d-4e1d-90a6-3ec5bee30d97",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuL7P3gdkh8cFfLqCR7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "602c15f1-5e21-4ff3-9658-f672bb962ef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XgTRdcgHhuTSBMLGNVhTVJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 84921,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 84921,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 55 · 2026-05-13T16:43:17.639Z_

<details><summary>↩ Tool result · `toolu_015rHN1MfcVrWGUBREkTiCHk`</summary>

```text
1	# P1 Base Condition: 2PL+γ and 4PL+γ IRT, ADVI then NUTS
2	# N_items=100 for CPU feasibility. Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS
3	
4	import json
5	import os
6	import sys
7	import time
8	import numpy as np
9	from scipy.special import expit
10	import cmdstanpy
11	
12	SEED = 42
13	N_MODELS = 50
14	N_ITEMS = 100
15	GAMMA_TRUE = 0.5
16	EXPOSURE_RATE = 0.3
17	
18	ARTIFACTS_DIR = os.path.dirname(os.path.abspath(__file__))
19	STAN_4PL = os.path.join(ARTIFACTS_DIR, "contam_irt_4pl.stan")
20	STAN_2PL = os.path.join(ARTIFACTS_DIR, "contam_irt_2pl.stan")
21	
22	PASS_THRESHOLDS = {
23	    "gamma_ci_covers_true": True,
24	    "gamma_ci_excludes_zero": True,
25	    "gamma_rel_bias": 0.3,
26	    "theta_corr": 0.9,
27	    "theta_rmse": 0.2,
28	    "max_rhat": 1.01,
29	    "divergent_pct": 1.0,
30	}
31	
32	
33	def generate_data(rng):
34	    theta = rng.standard_normal(N_MODELS)
35	    a = rng.lognormal(0, 0.5, N_ITEMS)
36	    b = rng.standard_normal(N_ITEMS)
37	    c = rng.beta(5, 20, N_ITEMS)
38	    d = rng.beta(20, 5, N_ITEMS)
39	    exposure = rng.binomial(1, EXPOSURE_RATE, (N_MODELS, N_ITEMS)).astype(float)
40	
41	    eta = np.outer(np.ones(N_MODELS), a) * (
42	        theta[:, None] - b[None, :]
43	    ) + GAMMA_TRUE * exposure
44	    prob = c[None, :] + (d[None, :] - c[None, :]) * expit(eta)
45	    y = rng.binomial(1, prob)
46	
47	    true_params = {"theta": theta, "a": a, "b": b, "c": c, "d": d}
48	    stan_data = {
49	        "N_models": N_MODELS,
50	        "N_items": N_ITEMS,
51	        "y": y.tolist(),
52	        "exposure": exposure.tolist(),
53	    }
54	    return stan_data, true_params
55	
56	
57	def fit_advi(stan_file, stan_data, seed=SEED):
58	    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
59	    vb = model.variational(
60	        data=stan_data,
61	        seed=seed,
62	        algorithm="fullrank",
63	        output_samples=2000,
64	    )
65	    return vb
66	
67	
68	def fit_nuts(stan_file, stan_data, adapt_delta=0.95, max_treedepth=10):
69	    model = cmdstanpy.CmdStanModel(stan_file=stan_file)
70	    fit = model.sample(
71	        data=stan_data,
72	        chains=4,
73	        iter_warmup=1000,
74	        iter_sampling=1000,
75	        seed=SEED,
76	        adapt_delta=adapt_delta,
77	        max_treedepth=max_treedepth,
78	        show_progress=True,
79	    )
80	    return fit
81	
82	
83	def evaluate_advi(vb, true_params, model_name):
84	    # mean=False to get variational draws, not just the mean
85	    gamma_draws = vb.stan_variable("gamma", mean=False)
86	    gamma_draws = np.atleast_1d(gamma_draws)
87	    gamma_mean = float(np.mean(gamma_draws))
88	    gamma_sd = float(np.std(gamma_draws))
89	    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
90	    gamma_q975 = float(np.percentile(gamma_draws, 97.5))
91	    gamma_bias = gamma_mean - GAMMA_TRUE
92	    gamma_rel_bias = abs(gamma_bias / GAMMA_TRUE)
93	    gamma_ci_covers_true = bool(gamma_q025 <= GAMMA_TRUE <= gamma_q975)
94	    gamma_ci_excludes_zero = bool(gamma_q025 > 0 or gamma_q975 < 0)
95	
96	    theta_draws = vb.stan_variable("theta", mean=False)
97	    if theta_draws.ndim == 1:
98	        theta_post_mean = theta_draws
99	    else:
100	        theta_post_mean = np.mean(theta_draws, axis=0)
101	    theta_true = true_params["theta"]
102	    theta_corr = float(np.corrcoef(theta_post_mean, theta_true)[0, 1])
103	    theta_rmse = float(np.sqrt(np.mean((theta_post_mean - theta_true) ** 2)))
104	
105	    metrics = {
106	        "model": model_name,
107	        "method": "ADVI",
108	        "gamma_mean": round(gamma_mean, 4),
109	        "gamma_sd": round(gamma_sd, 4),
110	        "gamma_q025": round(gamma_q025, 4),
111	        "gamma_q975": round(gamma_q975, 4),
112	        "gamma_bias": round(gamma_bias, 4),
113	        "gamma_rel_bias": round(gamma_rel_bias, 4),
114	        "gamma_ci_covers_true": gamma_ci_covers_true,
115	        "gamma_ci_excludes_zero": gamma_ci_excludes_zero,
116	        "theta_corr": round(theta_corr, 4),
117	        "theta_rmse": round(theta_rmse, 4),
118	    }
119	
120	    pf = {}
121	    pf["gamma_ci_covers_true"] = gamma_ci_covers_true
122	    pf["gamma_ci_excludes_zero"] = gamma_ci_excludes_zero
123	    pf["gamma_rel_bias"] = gamma_rel_bias < PASS_THRESHOLDS["gamma_rel_bias"]
124	    pf["theta_corr"] = theta_corr > PASS_THRESHOLDS["theta_corr"]
125	    pf["theta_rmse"] = theta_rmse < PASS_THRESHOLDS["theta_rmse"]
126	    pf["overall"] = all(pf.values())
127	    metrics["pass_fail"] = pf
128	    return metrics
129	
130	
131	def evaluate_nuts(fit, true_params, model_name):
132	    summary = fit.summary()
133	
134	    gamma_draws = fit.stan_variable("gamma")
135	    gamma_mean = float(np.mean(gamma_draws))
136	    gamma_sd = float(np.std(gamma_draws))
137	    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
138	    gamma_q975 = float(np.percentile(gamma_draws, 97.5))
139	    gamma_bias = gamma_mean - GAMMA_TRUE
140	    gamma_rel_bias = abs(gamma_bias / GAMMA_TRUE)
141	    gamma_ci_covers_true = bool(gamma_q025 <= GAMMA_TRUE <= gamma_q975)
142	    gamma_ci_excludes_zero = bool(gamma_q025 > 0 or gamma_q975 < 0)
143	
144	    theta_draws = fit.stan_variable("theta")
145	    theta_post_mean = np.mean(theta_draws, axis=0)
146	    theta_true = true_params["theta"]
147	    theta_corr = float(np.corrcoef(theta_post_mean, theta_true)[0, 1])
148	    theta_rmse = float(np.sqrt(np.mean((theta_post_mean - theta_true) ** 2)))
149	
150	    diag = fit.diagnose()
151	    divergent = 0
152	    for line in diag.split('\n'):
153	        if 'divergent' in line.lower():
154	            parts = [w for w in line.split() if w.isdigit()]
155	            if parts:
156	                divergent = int(parts[0])
157	                break
158	
159	    num_chains = fit.chains
160	    total_draws = num_chains * 1000
161	    divergent_pct = 100.0 * divergent / total_draws
162	
163	    if 'R_hat' in summary.columns:
164	        max_rhat = float(summary['R_hat'].max())
165	    else:
166	        max_rhat = float(summary.iloc[:, -1].max())
167	
168	    if 'N_Eff' in summary.columns:
169	        min_ess = float(summary['N_Eff'].min())
170	    elif 'ESS_bulk' in summary.columns:
171	        min_ess = float(summary['ESS_bulk'].min())
172	    else:
173	        min_ess = float('nan')
174	
175	    metrics = {
176	        "model": model_name,
177	        "method": "NUTS",
178	        "gamma_mean": round(gamma_mean, 4),
179	        "gamma_sd": round(gamma_sd, 4),
180	        "gamma_q025": round(gamma_q025, 4),
181	        "gamma_q975": round(gamma_q975, 4),
182	        "gamma_bias": round(gamma_bias, 4),
183	        "gamma_rel_bias": round(gamma_rel_bias, 4),
184	        "gamma_ci_covers_true": gamma_ci_covers_true,
185	        "gamma_ci_excludes_zero": gamma_ci_excludes_zero,
186	        "theta_corr": round(theta_corr, 4),
187	        "theta_rmse": round(theta_rmse, 4),
188	        "max_rhat": round(max_rhat, 4),
189	        "divergent_count": divergent,
190	        "divergent_pct": round(divergent_pct, 4),
191	        "min_ess": round(min_ess, 1) if not np.isnan(min_ess) else None,
192	    }
193	
194	    pf = {}
195	    pf["gamma_ci_covers_true"] = gamma_ci_covers_true
196	    pf["gamma_ci_excludes_zero"] = gamma_ci_excludes_zero
197	    pf["gamma_rel_bias"] = gamma_rel_bias < PASS_THRESHOLDS["gamma_rel_bias"]
198	    pf["theta_corr"] = theta_corr > PASS_THRESHOLDS["theta_corr"]
199	    pf["theta_rmse"] = theta_rmse < PASS_THRESHOLDS["theta_rmse"]
200	    pf["max_rhat"] = max_rhat < PASS_THRESHOLDS["max_rhat"]
201	    pf["divergent_pct"] = divergent_pct < PASS_THRESHOLDS["divergent_pct"]
202	    pf["overall"] = all(pf.values())
203	    metrics["pass_fail"] = pf
204	    return metrics
205	
206	
207	def fmt_pf(v):
208	    return "PASS" if v else "**FAIL**"
209	
210	
211	def write_markdown(all_results):
212	    lines = [
213	        "# P1 Base Condition Results",
214	        "",
215	        f"- N_models={N_MODELS}, N_items={N_ITEMS}, γ_true={GAMMA_TRUE}, exposure_rate={EXPOSURE_RATE}",
216	        f"- seed={SEED}",
217	        "",
218	    ]
219	
220	    for key in ["2pl_advi", "2pl_nuts", "4pl_advi", "4pl_nuts"]:
221	        if key not in all_results:
222	            continue
223	        r = all_results[key]
224	        pf = r["pass_fail"]
225	        label = key.upper().replace("_", " ")
226	        lines += [f"## {label}", ""]
227	        lines += [
228	            "| Metric | Value | Threshold | Result |",
229	            "|--------|-------|-----------|--------|",
230	            f"| γ mean (sd) | {r['gamma_mean']} ({r['gamma_sd']}) | — | — |",
231	            f"| γ 95% CI | [{r['gamma_q025']}, {r['gamma_q975']}] | — | — |",
232	            f"| γ bias | {r['gamma_bias']} | — | — |",
233	            f"| γ relative bias | {r['gamma_rel_bias']} | < 0.3 | {fmt_pf(pf['gamma_rel_bias'])} |",
234	            f"| γ CI covers true | {r['gamma_ci_covers_true']} | Yes | {fmt_pf(pf['gamma_ci_covers_true'])} |",
235	            f"| γ CI excludes 0 | {r['gamma_ci_excludes_zero']} | Yes | {fmt_pf(pf['gamma_ci_excludes_zero'])} |",
236	            f"| θ correlation | {r['theta_corr']} | > 0.9 | {fmt_pf(pf['theta_corr'])} |",
237	            f"| θ RMSE | {r['theta_rmse']} | < 0.2 | {fmt_pf(pf['theta_rmse'])} |",
238	        ]
239	        if "max_rhat" in r:
240	            lines.append(f"| Max R-hat | {r['max_rhat']} | < 1.01 | {fmt_pf(pf['max_rhat'])} |")
241	            lines.append(f"| Divergent | {r['divergent_count']} ({r['divergent_pct']}%) | < 1% | {fmt_pf(pf['divergent_pct'])} |")
242	            lines.append(f"| Min ESS | {r['min_ess']} | — | — |")
243	        if "fit_time_sec" in r:
244	            lines.append(f"| Fit time | {r['fit_time_sec']}s | — | — |")
245	        lines += ["", f"**Overall: {'PASS' if pf['overall'] else 'FAIL'}**", ""]
246	
247	    return "\n".join(lines)
248	
249	
250	def main():
251	    rng = np.random.default_rng(SEED)
252	    all_results = {"config": {
253	        "N_models": N_MODELS, "N_items": N_ITEMS,
254	        "gamma_true": GAMMA_TRUE, "exposure_rate": EXPOSURE_RATE, "seed": SEED,
255	    }}
256	
257	    print("=== Generating data ===")
258	    stan_data, true_params = generate_data(rng)
259	    sys.stdout.flush()
260	
261	    # --- 2PL ADVI ---
262	    print("\n=== 2PL+γ ADVI ===")
263	    sys.stdout.flush()
264	    t0 = time.time()
265	    vb_2pl = fit_advi(STAN_2PL, stan_data)
266	    t_2pl_advi = time.time() - t0
267	    r = evaluate_advi(vb_2pl, true_params, "2pl")
268	    r["fit_time_sec"] = round(t_2pl_advi, 1)
269	    all_results["2pl_advi"] = r
270	    print(f"  Time: {t_2pl_advi:.1f}s | γ={r['gamma_mean']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
271	    sys.stdout.flush()
272	
273	    # Write intermediate result immediately
274	    json_path = os.path.join(ARTIFACTS_DIR, "p1_base_results.json")
275	    with open(json_path, "w") as f:
276	        json.dump(all_results, f, indent=2, default=str)
277	    print(f"  >> Intermediate results written (2PL ADVI)")
278	    print(f"\n=== 2PL ADVI RESULT: {'PASS' if r['pass_fail']['overall'] else 'FAIL'} ===")
279	    sys.stdout.flush()
280	
281	    # --- 2PL NUTS ---
282	    print("\n=== 2PL+γ NUTS ===")
283	    sys.stdout.flush()
284	    t0 = time.time()
285	    fit_2pl = fit_nuts(STAN_2PL, stan_data, adapt_delta=0.95)
286	    t_2pl_nuts = time.time() - t0
287	    r = evaluate_nuts(fit_2pl, true_params, "2pl")
288	    r["fit_time_sec"] = round(t_2pl_nuts, 1)
289	    all_results["2pl_nuts"] = r
290	    print(f"  Time: {t_2pl_nuts:.1f}s | γ={r['gamma_mean']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
291	    sys.stdout.flush()
292	
293	    with open(json_path, "w") as f:
294	        json.dump(all_results, f, indent=2, default=str)
295	
296	    # --- 4PL ADVI ---
297	    print("\n=== 4PL+γ ADVI ===")
298	    sys.stdout.flush()
299	    t0 = time.time()
300	    vb_4pl = fit_advi(STAN_4PL, stan_data)
301	    t_4pl_advi = time.time() - t0
302	    r = evaluate_advi(vb_4pl, true_params, "4pl")
303	    r["fit_time_sec"] = round(t_4pl_advi, 1)
304	    all_results["4pl_advi"] = r
305	    print(f"  Time: {t_4pl_advi:.1f}s | γ={r['gamma_mean']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
306	    sys.stdout.flush()
307	
308	    with open(json_path, "w") as f:
309	        json.dump(all_results, f, indent=2, default=str)
310	
311	    # --- 4PL NUTS ---
312	    print("\n=== 4PL+γ NUTS ===")
313	    sys.stdout.flush()
314	    t0 = time.time()
315	    fit_4pl = fit_nuts(STAN_4PL, stan_data, adapt_delta=0.95)
316	    t_4pl_nuts = time.time() - t0
317	    r = evaluate_nuts(fit_4pl, true_params, "4pl")
318	    r["fit_time_sec"] = round(t_4pl_nuts, 1)
319	    all_results["4pl_nuts"] = r
320	    print(f"  Time: {t_4pl_nuts:.1f}s | γ={r['gamma_mean']} | θ_corr={r['theta_corr']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
321	    sys.stdout.flush()
322	
323	    # Retry 4PL NUTS if convergence issues
324	    if r["divergent_pct"] > 5.0 or r["max_rhat"] > 1.1:
325	        print("\n=== 4PL+γ NUTS retry (adapt_delta=0.99, treedepth=12) ===")
326	        sys.stdout.flush()
327	        t0 = time.time()
328	        fit_4pl = fit_nuts(STAN_4PL, stan_data, adapt_delta=0.99, max_treedepth=12)
329	        t_retry = time.time() - t0
330	        r = evaluate_nuts(fit_4pl, true_params, "4pl")
331	        r["fit_time_sec"] = round(t_retry, 1)
332	        r["retried"] = True
333	        all_results["4pl_nuts"] = r
334	        print(f"  Retry: {t_retry:.1f}s | γ={r['gamma_mean']} | {'PASS' if r['pass_fail']['overall'] else 'FAIL'}")
335	        sys.stdout.flush()
336	
337	    # Final write
338	    with open(json_path, "w") as f:
339	        json.dump(all_results, f, indent=2, default=str)
340	
341	    md = write_markdown(all_results)
342	    md_path = os.path.join(ARTIFACTS_DIR, "p1_base_results.md")
343	    with open(md_path, "w") as f:
344	        f.write(md)
345	
346	    print(f"\n=== SUMMARY ===")
347	    for key in ["2pl_advi", "2pl_nuts", "4pl_advi", "4pl_nuts"]:
348	        if key in all_results:
349	            r = all_results[key]
350	            print(f"  {key}: γ={r['gamma_mean']}, θ_corr={r['theta_corr']}, {'PASS' if r['pass_fail']['overall'] else 'FAIL'} ({r['fit_time_sec']}s)")
351	    sys.stdout.flush()
352	
353	    return all_results
354	
355	
356	if __name__ == "__main__":
357	    main()
358	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "602c15f1-5e21-4ff3-9658-f672bb962ef1",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "9acb6d93-1600-4735-94ba-21b6ef5e1509",
  "sourceToolAssistantUUID": "602c15f1-5e21-4ff3-9658-f672bb962ef1",
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

_source line 56 · 2026-05-13T16:43:21.687Z_

Now I have a thorough understanding of the paper's methodology, experimental design, and the three tiers of imagined results. Let me also check the dream registry to understand which tier I should be reviewing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9acb6d93-1600-4735-94ba-21b6ef5e1509",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuLTAgSZsMxPGVSnmdv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45a81b0f-d645-4391-a0aa-67f25f647fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCjJq2a1hA7T5qpmCMp66V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6208,
      "cache_read_input_tokens": 86313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6208,
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

_source line 57 · 2026-05-13T16:43:23.930Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EbnUYRhpUwhgBdN3x2obpA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/dream_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45a81b0f-d645-4391-a0aa-67f25f647fe3",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuLTAgSZsMxPGVSnmdv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e517b4ce-ea00-40fd-b242-dd91316f9ac3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCjJq2a1hA7T5qpmCMp66V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6208,
      "cache_read_input_tokens": 86313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6208,
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

_source line 58 · 2026-05-13T16:43:23.944Z_

<details><summary>↩ Tool result · `toolu_01EbnUYRhpUwhgBdN3x2obpA`</summary>

```text
1	dreams:
2	  dream_20260513T155040:
3	    dream_id: dream_20260513T155040
4	    project: contamcal-irt-calibration
5	    status: reviewing
6	    review_mode: full
7	    review_visible: true
8	    writing_visible: true
9	    venue: AAAI 2027
10	    focus: 'Core concern: can 4PL+γ IRT with noisy RRF exposure scores actually improve
11	      model selection over baselines? Focus on calibration accuracy, baseline comparison
12	      strength, and RL observational validity.'
13	    what_if: []
14	    pid: 215498
15	    chat_id: oc_4960c7baa442eabd4fa0aceeac2693ca
16	    card_message_id: om_x100b6f7d93dde0a0c100635839c9b70
17	    started_at: '2026-05-13T15:50:40+00:00'
18	    updated_at: '2026-05-13T16:20:15+00:00'
19	    stages_completed:
20	    - imagine
21	    - write
22	    error: null
23	    context_hash: 8c67e68e87f880fffc2d79adfd9dcf254c74eceedc6ac17af1d56cfc75961d22
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e517b4ce-ea00-40fd-b242-dd91316f9ac3",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "d7e1f86f-e54b-4b26-be9d-93952417fc58",
  "sourceToolAssistantUUID": "e517b4ce-ea00-40fd-b242-dd91316f9ac3",
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

_source line 59 · 2026-05-13T16:43:24.714Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ABNtmynZNr6jUk5EPmTyd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7e1f86f-e54b-4b26-be9d-93952417fc58",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuLTAgSZsMxPGVSnmdv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18e72bfe-fce4-414f-a243-4e0bd8aeb7f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCjJq2a1hA7T5qpmCMp66V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6208,
      "cache_read_input_tokens": 86313,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 86313,
          "cache_creation_input_tokens": 6208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6208,
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

_source line 60 · 2026-05-13T16:43:25.040Z_

<details><summary>↩ Tool result · `toolu_013ABNtmynZNr6jUk5EPmTyd`</summary>

```text
1	narrative_guidance: '核心calibration claim不成立。Reframe为"Empirical Identifiability Boundaries
2	  for Contamination-Aware IRT"—— 系统性研究在什么条件下IRT校准才可行。exp-004仿真的identifiability map成为Core
3	  Contribution 1， exp-008 signal survival升级为Core，controlled SFT注入变为empirical validation证明仿真边界与真实数据吻合。
4	  叙事逻辑：在构建校准系统之前，先搞清楚它何时能工作。论文从"we solve calibration"转为"we map when calibration is
5	  solvable"。
6	
7	  '
8	imagined_experiments:
9	- name: controlled_sft_injection
10	  plan_id: exp-001
11	  description: 'SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels.
12	    在worst档下，注入本身成功但产生的score inflation pattern不干净—— 低dosage几乎无可测效应，高dosage效应被模型capacity限制截断。
13	
14	    '
15	  expected_results:
16	    sft_runs_completed: 15
17	    mmlu_score_inflation_0pct_baseline_acc: 0.47
18	    mmlu_score_inflation_5pct_pp: 0.8
19	    mmlu_score_inflation_25pct_pp: 2.1
20	    mmlu_score_inflation_50pct_pp: 4.5
21	    mmlu_score_inflation_100pct_pp: 8.2
22	    gsm8k_score_inflation_100pct_pp: 5.1
23	    arc_score_inflation_100pct_pp: 6.8
24	    humaneval_score_inflation_100pct_pp: 3.9
25	    inflation_monotonicity_spearman_mmlu: 0.9
26	    inflation_monotonicity_spearman_gsm8k: 0.7
27	    inflation_variance_across_seeds_std_pp: 2.8
28	    qwen_0_5b_inflation_at_100pct_pp: 11.5
29	    qwen_3b_inflation_at_100pct_pp: 5.8
30	    low_dosage_detectable_5pct: false
31	    low_dosage_detectable_25pct_marginal: true
32	  result_rationale: 'SFT注入机制本身可靠（paraphrase SFT是成熟技术），所以15个run都会完成。 但worst档的核心问题在这里开始显现：(1)
33	    0.5B模型capacity极小，SFT后memorization严重但泛化到benchmark format的能力弱， 导致inflation方差大；(2)
34	    5%dosage（<700 items for MMLU）在SFT数据中被稀释，inflation <1pp， 与random seed noise不可区分——这直接导致后续dose-response非单调的关键问题；
35	    (3) GSM8K/HumanEval因为是生成式评估（非选择题），paraphrase memorization的转化率低于MMLU， inflation更弱；(4)
36	    3B模型因pretraining更强，SFT的边际效应递减—— 表现为"大模型inflation反而小于小模型"的反直觉模式，给后续γ估计制造confounding。
37	    整体inflation pattern存在但noisy，为后续信号检测和IRT拟合埋下问题。
38	
39	    '
40	  tables:
41	  - name: 'Table: Score Inflation by Model × Dosage × Benchmark'
42	    columns:
43	    - model
44	    - benchmark
45	    - 0%
46	    - 5%
47	    - 25%
48	    - 50%
49	    - 100%
50	    rows:
51	    - - Qwen2.5-0.5B
52	      - MMLU
53	      - 42.3
54	      - 43.5
55	      - 45.8
56	      - 49.1
57	      - 53.8
58	    - - Qwen2.5-0.5B
59	      - GSM8K
60	      - 31.2
61	      - 31.5
62	      - 32.8
63	      - 34.1
64	      - 36.3
65	    - - Qwen2.5-0.5B
66	      - ARC-C
67	      - 38.1
68	      - 38.6
69	      - 40.2
70	      - 42.5
71	      - 45.9
72	    - - Qwen2.5-0.5B
73	      - HumanEval
74	      - 22.0
75	      - 22.1
76	      - 23.0
77	      - 24.2
78	      - 25.9
79	    - - Qwen2.5-1.5B
80	      - MMLU
81	      - 53.1
82	      - 53.6
83	      - 54.8
84	      - 56.5
85	      - 59.7
86	    - - Qwen2.5-1.5B
87	      - GSM8K
88	      - 48.5
89	      - 48.8
90	      - 49.9
91	      - 51.8
92	      - 53.2
93	    - - Qwen2.5-1.5B
94	      - ARC-C
95	      - 52.0
96	      - 52.4
97	      - 53.5
98	      - 55.1
99	      - 57.8
100	    - - Qwen2.5-1.5B
101	      - HumanEval
102	      - 35.4
103	      - 35.6
104	      - 36.5
105	      - 37.8
106	      - 39.1
107	    - - Qwen2.5-3B
108	      - MMLU
109	      - 61.8
110	      - 62.1
111	      - 63.0
112	      - 64.5
113	      - 67.0
114	    - - Qwen2.5-3B
115	      - GSM8K
116	      - 62.3
117	      - 62.5
118	      - 63.1
119	      - 64.2
120	      - 65.8
121	    - - Qwen2.5-3B
122	      - ARC-C
123	      - 60.5
124	      - 60.8
125	      - 61.6
126	      - 63.0
127	      - 65.2
128	    - - Qwen2.5-3B
129	      - HumanEval
130	      - 48.2
131	      - 48.4
132	      - 49.0
133	      - 50.1
134	      - 52.1
135	  figures_description:
136	  - 'Fig: Dosage-Inflation curves per model×benchmark. Key observation: 5% dosage
137	    points overlap with 0% error bars on most benchmarks. GSM8K/HumanEval curves noticeably
138	    flatter than MMLU. 0.5B shows highest absolute inflation but also highest variance.'
139	  analysis: '注入成功但暴露了两个worst档关键弱点：(1) 低dosage信号几乎不存在（5%不可检出，25%边缘）， 这意味着后续dose-response分析在低端会崩溃；(2)
140	    inflation幅度跨benchmark差异大 （MMLU最高~8pp，HumanEval仅~4pp），且与model scale反相关， 说明contamination
141	    effect不是一个简单的additive γ——它与ability θ交互， 这从根本上挑战了4PL+γ的additive model specification。
142	    但作为reframed论文的素材，这些结果反而有价值——"仿真假设的uniform γ在真实数据中不成立"是identifiability分析的重要发现。
143	
144	    '
145	- name: stage1_signal_pipeline
146	  plan_id: exp-002
147	  description: '4个检测信号（embedding retrieval, Min-K%++, ConStat, Self-Critique） 在exp-001所有模型上的计算。worst档下信号质量显著低于仿真中假设的AUC水平。
148	
149	    '
150	  expected_results:
151	    embedding_retrieval_auc_sft_100pct_avg: 0.72
152	    embedding_retrieval_auc_sft_5pct_avg: 0.54
153	    minkpp_auc_sft_100pct_avg: 0.68
154	    minkpp_auc_sft_5pct_avg: 0.52
155	    constat_auc_sft_100pct_avg: 0.66
156	    constat_auc_sft_25pct_avg: 0.57
157	    selfcritique_auc_sft_100pct_avg: 0.63
158	    selfcritique_auc_sft_5pct_avg: 0.51
159	    avg_signal_auc_across_all_conditions: 0.61
160	    signal_auc_variance_across_benchmarks: 0.008
161	    embedding_retrieval_auc_qwen0_5b_100pct: 0.75
162	    embedding_retrieval_auc_qwen3b_100pct: 0.69
163	    minkpp_fp_rate_at_90pct_recall: 0.45
164	    constat_requires_paraphrase_availability: true
165	    selfcritique_entropy_separation_cohens_d: 0.41
166	  result_rationale: 'worst档的核心机制在这里发力：(1) Embedding retrieval在100%dosage下表现尚可（AUC~0.72），
167	    因为语义相似性是最直接的信号——但它本质上检测的是"题目是否在训练集里"而非"模型是否从中获益"， 这导致了fundamental mismatch：高AUC不等于高因果信号质量；
168	    (2) Min-K%++在SFT后的token distribution shift中受到干扰，AUC降至0.68—— SFT本身（无论是否contaminated）改变了模型的perplexity
169	    landscape，造成confounding； (3) ConStat需要paraphrased版本的benchmark items，而这些paraphrases本身可能在SFT数据中出现过
170	    （因为我们的注入就是用paraphrases），导致original-vs-paraphrase gap被压缩，AUC仅0.66； (4) Self-Critique在SFT
171	    regime下最弱（AUC 0.63），因为SFT同时改变了模型的self-evaluation能力， 特别是对小模型（0.5B）self-critique本身就不可靠。
172	    关键问题：所有信号在5%dosage下AUC接近random（0.51-0.54）， 因为被contaminate的items太少（~70 items for
173	    MMLU 5%），信号被noise淹没。 跨benchmark方差小意味着问题不是benchmark-specific而是系统性的信号质量天花板。
174	
175	    '
176	  tables:
177	  - name: 'Table: Signal AUC Heatmap — Signal × Dosage (averaged across models and
178	      benchmarks)'
179	    columns:
180	    - signal
181	    - 5%
182	    - 25%
183	    - 50%
184	    - 100%
185	    rows:
186	    - - Embedding Retrieval
187	      - 0.54
188	      - 0.62
189	      - 0.68
190	      - 0.72
191	    - - Min-K%++
192	      - 0.52
193	      - 0.58
194	      - 0.64
195	      - 0.68
196	    - - ConStat
197	      - 0.51
198	      - 0.57
199	      - 0.62
200	      - 0.66
201	    - - Self-Critique
202	      - 0.51
203	      - 0.55
204	      - 0.59
205	      - 0.63
206	  - name: 'Table: Signal AUC by Model Scale at 100% Dosage (MMLU)'
207	    columns:
208	    - signal
209	    - Qwen-0.5B
210	    - Qwen-1.5B
211	    - Qwen-3B
212	    rows:
213	    - - Embedding Retrieval
214	      - 0.75
215	      - 0.73
216	      - 0.69
217	    - - Min-K%++
218	      - 0.71
219	      - 0.68
220	      - 0.65
221	    - - ConStat
222	      - 0.69
223	      - 0.67
224	      - 0.63
225	    - - Self-Critique
226	      - 0.58
227	      - 0.64
228	      - 0.66
229	  figures_description:
230	  - 'Fig: 4×4 AUC heatmap (signal × dosage) with color gradient from red (0.50) to
231	    green (0.80). Dominated by orange/yellow tones, only top-right corner (embedding×100%)
232	    reaches green. Clear dosage gradient visible in all signals.'
233	  - 'Fig: Per-item score distributions (contaminated vs clean) for each signal at
234	    50% dosage. Heavy overlap visible, Cohen''s d annotations all < 0.6.'
235	  analysis: '这是worst档叙事的关键转折点：exp-004仿真假设AUC是exogenous input，在AUC≥0.70时identifiability成立。
236	    但真实数据表明，只有embedding retrieval在100%dosage下达到0.72，其余条件下所有信号都在0.70以下。 更严重的是，信号AUC与dosage正相关——恰好在低dosage（最需要检测的regime）信号最弱。
237	    这创造了一个catch-22：contamination越严重越容易检测，越轻微越不可检测， 但校准价值恰恰在轻微contamination时最高。这是reframed论文的核心洞察之一。
238	
239	    '
240	- name: rrf_aggregation_ablation
241	  plan_id: exp-003
242	  description: 'RRF融合及ablation。worst档下RRF未能显著超越最佳单信号， "互补性"假设在真实数据上不成立。
243	
244	    '
245	  expected_results:
246	    rrf_4signal_auc_100pct_dosage: 0.7
247	    rrf_4signal_auc_50pct_dosage: 0.65
248	    rrf_4signal_auc_25pct_dosage: 0.6
249	    rrf_4signal_auc_5pct_dosage: 0.55
250	    best_single_signal_auc_100pct: 0.72
251	    rrf_vs_best_single_auc_delta_100pct: -0.02
252	    rrf_vs_best_single_auc_delta_avg: 0.01
253	    rank_avg_auc_100pct: 0.69
254	    calibrated_weighted_rrf_auc_100pct: 0.71
255	    degraded_2signal_auc_100pct: 0.64
256	    degraded_2signal_auc_50pct: 0.59
257	    degraded_2signal_vs_4signal_auc_gap: 0.06
258	    fp_injection_robustness_auc_drop_10pct_fp: 0.04
259	    fp_injection_robustness_auc_drop_20pct_fp: 0.09
260	    signal_correlation_matrix_avg_pairwise_r: 0.58
261	  result_rationale: 'RRF融合的理论优势依赖于信号互补性——不同信号捕获不同aspect的contamination evidence。 worst档下这一假设崩溃的原因：(1)
262	    信号间pairwise correlation高达0.58（远高于独立信号假设的~0.2）， 因为所有信号本质上都在检测同一个latent变量（训练数据中是否包含该item的变体），
263	    只是通过不同proxy衡量，proxy之间高度相关； (2) RRF在100%dosage下（0.70）反而低于最佳单信号embedding retrieval（0.72），
264	    因为RRF等权平均了四个信号，而弱信号（Self-Critique 0.63）拖累了总体； (3) calibrated weighted RRF（0.71）通过下调弱信号权重稍有改善，但改善不显著
265	    （因为最优权重在small sample下估计不稳定）； (4) 2-signal degraded mode（ConStat+Self-Critique=0.64）更糟，
266	    因为这两个恰好是最弱的两个信号——closed-weight场景下的可用信号恰好是最差的。 FP injection进一步暴露了脆弱性：20% FP率下AUC下降0.09，说明信号对noise极敏感。
267	
268	    '
269	  tables:
270	  - name: 'Table: Aggregation Method Comparison (AUC at 100% dosage, MMLU)'
271	    columns:
272	    - method
273	    - AUC
274	    - Δ vs best single
275	    rows:
276	    - - Embedding Retrieval (best single)
277	      - 0.72
278	      - —
279	    - - Min-K%++
280	      - 0.68
281	      - -0.04
282	    - - ConStat
283	      - 0.66
284	      - -0.06
285	    - - Self-Critique
286	      - 0.63
287	      - -0.09
288	    - - RRF (4-signal)
289	      - 0.7
290	      - -0.02
291	    - - Rank Average (4-signal)
292	      - 0.69
293	      - -0.03
294	    - - Weighted RRF (calibrated)
295	      - 0.71
296	      - -0.01
297	    - - 2-signal degraded (CS+SC)
298	      - 0.64
299	      - -0.08
300	  - name: 'Table: RRF AUC across dosage levels'
301	    columns:
302	    - method
303	    - 5%
304	    - 25%
305	    - 50%
306	    - 100%
307	    rows:
308	    - - RRF 4-signal
309	      - 0.55
310	      - 0.6
311	      - 0.65
312	      - 0.7
313	    - - Best single
314	      - 0.54
315	      - 0.62
316	      - 0.68
317	      - 0.72
318	    - - 2-signal degraded
319	      - 0.52
320	      - 0.56
321	      - 0.59
322	      - 0.64
323	  figures_description:
324	  - 'Fig: Pairwise signal correlation matrix heatmap. All off-diagonal values 0.45-0.68,
325	    indicating high redundancy. Embedding-MinK++ highest (0.68), Self-Critique-others
326	    lowest (~0.45).'
327	  - 'Fig: RRF AUC vs number of signals (1,2,3,4). Flat curve — adding signals beyond
328	    the best single provides <0.02 AUC gain at any dosage. Contrasts sharply with
329	    simulated independent signals.'
330	  analysis: 'RRF的failure mode不是"融合方法差"而是"没有足够互补的信号可融合"。 信号correlation 0.58意味着~34%共享方差，真正独立的信息增量有限。
331	    对reframed论文的贡献：这变成了"signal diversity as identifiability prerequisite"的实证证据—— identifiability不仅需要足够高的AUC，还需要信号间足够低的correlation。
332	    当前4个信号不满足这一条件。2-signal degraded mode的糟糕表现 直接支持"closed-weight regime下calibration不可行"的结论。
333	
334	    '
335	- name: noise_propagation_analysis
336	  plan_id: exp-005
337	  description: '噪声传播分析。worst档下暴露检测信号噪声导致CI宽度急剧膨胀， 使calibration在实用意义上失去价值。
338	
339	    '
340	  expected_results:
341	    baseline_gamma_ci_width_pp: 18.0
342	    noise_1x_gamma_ci_width_pp: 22.5
343	    noise_1_5x_gamma_ci_width_pp: 28.0
344	    noise_2x_gamma_ci_width_pp: 35.2
345	    baseline_theta_ci_width_pp: 12.0
346	    noise_1x_theta_ci_width_pp: 15.8
347	    noise_1_5x_theta_ci_width_pp: 20.5
348	    noise_2x_theta_ci_width_pp: 27.1
349	    ci_coverage_95_at_noise_1x: 0.88
350	    ci_coverage_95_at_noise_1_5x: 0.93
351	    ci_coverage_95_at_noise_2x: 0.97
352	    selfcritique_estimated_fp_rate: 0.35
353	    selfcritique_estimated_fn_rate: 0.28
354	    measurement_error_model_converged: true
355	    measurement_error_model_ci_width_pp: 24.0
356	    ci_width_exceeds_practical_threshold_15pp_pct: 0.78
357	  result_rationale: 'noise propagation在worst档下创造了一个根本性的precision-coverage tradeoff：
358	    (1) 基线CI width已经是18pp（因为信号AUC低导致γ posterior宽）， 远超可发表的"tight calibration"标准（<10pp）；
359	    (2) Self-Critique的FP rate 35%和FN rate 28%意味着matched noise level已经很高， 1x noise
360	    injection后CI膨胀至22.5pp——此时CI覆盖了绝大部分可能的score值， calibration退化为"我们不知道真实score是多少"的诚实但无用的声明；
361	    (3) 2x noise下CI width 35pp意味着一个60%准确率的模型的95%CI覆盖[42.5%, 77.5%]—— 这个范围大到无法做任何有意义的model
362	    selection； (4) coverage随noise增加而上升（从0.88到0.97）是因为CI变宽了， 不是因为calibration变好了——这是overcoverage问题，CI过于保守。
363	    measurement error model收敛但CI width 24pp说明即使自动noise propagation也无法"解决"问题， 因为核心issue是信号本身太noisy，不是propagation方法不对。
364	
365	    '
366	  tables:
367	  - name: 'Table: CI Width and Coverage under Noise Injection'
368	    columns:
369	    - noise_level
370	    - gamma_ci_width_pp
371	    - theta_ci_width_pp
372	    - coverage_95%
373	    - coverage_80%
374	    rows:
375	    - - baseline (0x)
376	      - 18.0
377	      - 12.0
378	      - 0.82
379	      - 0.68
380	    - - matched (1x)
381	      - 22.5
382	      - 15.8
383	      - 0.88
384	      - 0.74
385	    - - 1.5x
386	      - 28.0
387	      - 20.5
388	      - 0.93
389	      - 0.82
390	    - - 2x
391	      - 35.2
392	      - 27.1
393	      - 0.97
394	      - 0.9
395	    - - measurement error model
396	      - 24.0
397	      - 17.2
398	      - 0.9
399	      - 0.76
400	  figures_description:
401	  - 'Fig: CI width vs noise multiplier. Near-linear relationship for γ, slightly sub-linear
402	    for θ. Horizontal dashed line at 15pp marks ''practical utility threshold'' —
403	    crossed at ~0.7x matched noise, meaning even below realistic noise levels CIs
404	    are already too wide.'
405	  - 'Fig: Coverage-Width tradeoff plot. Curve moves from undercoverage+narrow (baseline)
406	    to overcoverage+wide (2x noise). No operating point achieves both nominal coverage
407	    AND practical width.'
408	  analysis: '这是worst档最具诊断价值的实验。它量化了"信号噪声→calibration无用"的精确pathway。 核心发现可以被表述为noise
409	    amplification theorem的实证版本： 当检测信号AUC < 0.70时，IRT模型的noise propagation使calibrated
410	    CI width超过15pp， 此时calibration不具备practical decision value。 对reframed论文的贡献：这直接支持identifiability
411	    boundary的operational定义—— 不仅是"能否估计γ"（statistical identifiability），还是"估计的γ是否有用"（practical
412	    identifiability）。 引入15pp practical threshold将identifiability map从binary升级为graded。
413	
414	    '
415	- name: irt_calibration_and_baselines
416	  plan_id: exp-006
417	  description: '核心calibration实验——4PL+γ IRT拟合及5个baselines比较。 worst档下4PL+γ不显著优于简单baselines。
418	
419	    '
420	  expected_results:
421	    calibration_mae_4pl_gamma_pp: 7.8
422	    calibration_mae_remove_rescore_pp: 8.1
423	    calibration_mae_single_signal_2pl_gamma_pp: 7.5
424	    calibration_mae_vanilla_4pl_pp: 9.2
425	    calibration_mae_linear_regression_pp: 7.2
426	    calibration_mae_emperor_mitigation_pp: 8.9
427	    margin_4pl_gamma_vs_best_baseline_mae_relative: 0.08
428	    ci_coverage_95_4pl_gamma: 0.78
429	    ci_coverage_80_4pl_gamma: 0.62
430	    ci_coverage_50_4pl_gamma: 0.38
431	    ci_width_95_avg_pp: 19.5
432	    ci_width_80_avg_pp: 14.2
433	    kendall_tau_4pl_gamma: 0.62
434	    kendall_tau_linear_regression: 0.65
435	    kendall_tau_vanilla_4pl: 0.58
436	    dose_response_spearman: 0.55
437	    dose_response_monotonic: false
438	    dose_response_5pct_gamma_ci_includes_zero: true
439	    dose_response_25pct_gamma_ci_includes_zero: true
440	    dose_response_100pct_gamma_significant: true
441	    gamma_theta_posterior_correlation: 0.52
442	    gamma_rel_bias_avg: 0.35
443	    gamma_95ci_includes_zero_pct_conditions: 0.55
444	    paired_ttest_4pl_gamma_vs_linear_pvalue: 0.23
445	    paired_ttest_4pl_gamma_vs_remove_rescore_pvalue: 0.41
446	    stan_rhat_max: 1.08
447	    stan_divergent_pct: 3.2
448	    stan_ess_min: 180
449	  result_rationale: '这是worst档的核心实验，calibration claim在这里正式崩溃： (1) 4PL+γ MAE 7.8pp看似reasonable，但linear
450	    regression以7.2pp击败它—— 更简单的模型反而更好，因为IRT的复杂参数化（a,b,c,d,γ五个参数/item）在small sample下过拟合，
451	    而linear regression的regularization更有效； (2) single-signal 2PL+γ（7.5pp）也优于full 4PL+γ，说明additional
452	    IRT complexity（c,d参数） 反而引入了estimation noise而非提供更好的fit； (3) γ-θ posterior correlation
453	    0.52直接confirm了identifiability问题—— 模型无法区分"模型能力高"和"模型被contaminate了"，因为在我们的数据中 这两者确实相关（更大的模型被更多地contaminate，或者更capable的模型从contamination中获益更多）；
454	    (4) dose-response非单调：5%和25%的γ CI包含0，只有100%显著—— 这意味着模型只能检测"极端contamination"，对"轻微到中度contamination"无能为力；
455	    (5) CI coverage 78%严重undercoverage（nominal 95%），说明posterior CI低估了不确定性， 这与noise
456	    propagation实验一致——模型没有正确传播信号噪声； (6) Stan diagnostics出现3.2% divergences和R-hat 1.08，暗示posterior
457	    geometry有问题， 可能因为γ-θ near-unidentifiable导致posterior funnel/ridge。 所有pairwise significance
458	    tests p>0.05，确认4PL+γ不具备统计显著优势。
459	
460	    '
461	  tables:
462	  - name: 'Table: Calibration MAE (pp) by Method × Benchmark'
463	    columns:
464	    - method
465	    - MMLU
466	    - GSM8K
467	    - ARC-C
468	    - HumanEval
469	    - Average
470	    rows:
471	    - - 4PL+γ (ours)
472	      - 6.5
473	      - 9.2
474	      - 7.1
475	      - 8.4
476	      - 7.8
477	    - - Remove-rescore
478	      - 7.2
479	      - 8.8
480	      - 7.5
481	      - 8.9
482	      - 8.1
483	    - - Single-signal 2PL+γ
484	      - 6.2
485	      - 8.5
486	      - 7.0
487	      - 8.3
488	      - 7.5
489	    - - Vanilla 4PL
490	      - 8.1
491	      - 10.5
492	      - 8.8
493	      - 9.4
494	      - 9.2
495	    - - Linear regression+CI
496	      - 5.8
497	      - 8.2
498	      - 6.9
499	      - 7.9
500	      - 7.2
501	    - - Emperor mitigation
502	      - 7.8
503	      - 10.2
504	      - 8.2
505	      - 9.4
506	      - 8.9
507	  - name: 'Table: Interval Quality Metrics'
508	    columns:
509	    - method
510	    - Coverage 95%
511	    - Coverage 80%
512	    - Width 95% (pp)
513	    - Kendall τ
514	    rows:
515	    - - 4PL+γ
516	      - 0.78
517	      - 0.62
518	      - 19.5
519	      - 0.62
520	    - - Linear regression+CI
521	      - 0.83
522	      - 0.7
523	      - 16.2
524	      - 0.65
525	    - - Single-signal 2PL+γ
526	      - 0.8
527	      - 0.65
528	      - 17.8
529	      - 0.6
530	  - name: 'Table: Dose-Response γ Estimates'
531	    columns:
532	    - dosage
533	    - gamma_mean
534	    - gamma_95ci_lower
535	    - gamma_95ci_upper
536	    - ci_excludes_zero
537	    rows:
538	    - - 5%
539	      - 0.04
540	      - -0.18
541	      - 0.26
542	      - false
543	    - - 25%
544	      - 0.11
545	      - -0.08
546	      - 0.31
547	      - false
548	    - - 50%
549	      - 0.22
550	      - 0.01
551	      - 0.44
552	      - true
553	    - - 100%
554	      - 0.38
555	      - 0.12
556	      - 0.65
557	      - true
558	  figures_description:
559	  - 'Fig: MAE bar chart with 95% bootstrap CIs across methods. 4PL+γ bar overlaps
560	    with linear regression and single-signal 2PL+γ CIs. No method achieves separation.
561	    Vanilla 4PL and Emperor mitigation clearly worse but that''s a low bar.'
562	  - 'Fig: Calibration plot (predicted vs true clean accuracy). 4PL+γ shows high-dosage
563	    points calibrated but low-dosage points clustered near identity line (no correction
564	    applied because γ≈0). Linear regression shows more uniform correction.'
565	  - 'Fig: γ posterior density plots by dosage. 5% and 25% posteriors centered near
566	    zero with wide tails. 50% barely significant. Only 100% shows clear separation
567	    from zero.'
568	  - 'Fig: γ-θ posterior scatter plot showing 0.52 correlation. Banana-shaped posterior
569	    indicating identifiability ridge.'
570	  analysis: '这是worst档论文reframing的smoking gun实验。三个关键takeaways： (1) IRT complexity不付费——linear
571	    regression+bootstrap CI以更少参数达到更好MAE和coverage， 说明在当前信号质量下，复杂模型的额外表达力被estimation
572	    noise吞噬； (2) γ的identifiability是dosage-dependent的——只有极端contamination可被检测和校正， 这严重限制了实用价值（现实中contamination不可能是100%）；
573	    (3) undercoverage说明Bayesian CI名义上的"uncertainty quantification"实际上overconfident，
574	    这是因为model misspecification（additive γ假设）而非posterior approximation问题。 Reframed论文角度：这些结果精确对应了exp-004仿真预测的identifiability
575	    boundary—— 真实AUC~0.65-0.70恰好在仿真中identifiability开始崩溃的区域， 构成"仿真边界与真实数据吻合"的核心evidence。
576	
577	    '
578	- name: scale_bridging_7b
579	  plan_id: exp-007
580	  description: 'Qwen2.5-7B 5个dosage level的controlled SFT。worst档下scale-up不仅未改善， 反而加剧了γ-θ
581	    confounding。
582	
583	    '
584	  expected_results:
585	    sft_runs_completed: 5
586	    mmlu_score_inflation_100pct_pp: 4.5
587	    mmlu_score_inflation_50pct_pp: 2.8
588	    mmlu_score_inflation_5pct_pp: 0.4
589	    gsm8k_score_inflation_100pct_pp: 2.9
590	    signal_auc_embedding_100pct: 0.66
591	    signal_auc_minkpp_100pct: 0.62
592	    gamma_estimate_100pct: 0.25
593	    gamma_ci_includes_zero_100pct: false
594	    gamma_ci_includes_zero_50pct: true
595	    calibration_mae_4pl_gamma_pp: 8.5
596	    calibration_mae_linear_regression_pp: 7.8
597	    gamma_theta_posterior_corr: 0.58
598	    inflation_vs_3b_ratio: 0.55
599	  result_rationale: '7B模型在worst档下表现更差而非更好，原因： (1) 更大模型的pretraining knowledge已经覆盖了更多benchmark
600	    knowledge， SFT injection的边际效应递减——inflation仅4.5pp vs 0.5B的11.5pp； (2) 更小的inflation意味着detection
601	    signal的SNR更低（AUC从0.72降至0.66）， 因为contamination signal被更大模型的"naturally knowing the
602	    answer"所掩盖—— 这是worst档的核心confounding：能力高的模型天然就会答对contaminated items， detection信号无法区分"因为contamination答对"和"因为能力高答对"；
603	    (3) γ-θ posterior correlation升至0.58（vs 0.5B/1.5B/3B的0.52）， confirm了scale与identifiability的反相关关系；
604	    (4) calibration MAE反而上升到8.5pp，因为7B的inflation小（校正需求低）， 但estimation noise不变甚至更大（因为signal
605	    AUC更低），导致noise-to-signal ratio恶化。
606	
607	    '
608	  tables:
609	  - name: 'Table: 7B vs 3B Comparison at 100% Dosage'
610	    columns:
611	    - metric
612	    - Qwen-3B
613	    - Qwen-7B
614	    rows:
615	    - - MMLU inflation (pp)
616	      - 5.2
617	      - 4.5
618	    - - Embedding AUC
619	      - 0.69
620	      - 0.66
621	    - - γ estimate
622	      - 0.34
623	      - 0.25
624	    - - γ-θ posterior corr
625	      - 0.52
626	      - 0.58
627	    - - Calibration MAE (pp)
628	      - 7.8
629	      - 8.5
630	    - - CI width 95% (pp)
631	      - 19.5
632	      - 22.0
633	  figures_description:
634	  - 'Fig: Scale vs identifiability plot. X-axis: model params (0.5B to 7B). Y-axis:
635	    γ relative bias and signal AUC. Both metrics degrade with scale, showing inverse
636	    relationship between model capability and calibration feasibility.'
637	  analysis: '7B实验提供了worst档最重要的scaling insight：calibration difficulty与model scale正相关。
638	    这不是方法的failure而是problem structure的fundamental property—— 更强的模型天然掩盖contamination
639	    signal。 对reframed论文：这是identifiability boundary的第三个维度（signal quality × model count
640	    × model scale）， 且是最novel的——之前的identifiability分析没有考虑"ability confounds detection"。
641	
642	    '
643	- name: signal_survival_analysis
644	  plan_id: exp-008
645	  description: 'Detection signal在不同training regime下的survival分析。 worst档下确认SFT后信号已经脆弱，RL后几乎完全失效。
646	
647	    '
648	  expected_results:
649	    auc_heatmap:
650	      base_embedding: 0.78
651	      base_minkpp: 0.73
652	      base_constat: 0.71
653	      base_selfcritique: 0.6
654	      sft_clean_embedding: 0.72
655	      sft_clean_minkpp: 0.65
656	      sft_clean_constat: 0.63
657	      sft_clean_selfcritique: 0.58
658	      sft_contam_embedding: 0.72
659	      sft_contam_minkpp: 0.68
660	      sft_contam_constat: 0.66
661	      sft_contam_selfcritique: 0.63
662	      rl_embedding: 0.6
663	      rl_minkpp: 0.55
664	      rl_constat: 0.53
665	      rl_selfcritique: 0.57
666	    signal_survival_rate_sft_avg: 0.88
667	    signal_survival_rate_rl_avg: 0.73
668	    rl_best_signal: selfcritique
669	    rl_best_signal_auc: 0.57
670	    rl_all_signals_below_070: true
671	    sft_clean_contam_auc_difference_avg: 0.03
672	    regime_effect_anova_pvalue: 0.002
673	  result_rationale: 'signal survival分析在worst档下揭示了检测信号的systematic fragility： (1) Base
674	    model上信号最强（embedding 0.78），但这个"最佳条件"在实践中不存在—— 没有人在base model上做benchmark evaluation，所有评估都在post-trained
675	    model上； (2) SFT（无论clean还是contaminated）使所有信号平均下降12%—— 这是因为SFT改变了model representation
676	    space，token-level信号（Min-K%++）受影响最大， 而embedding retrieval因为不依赖model内部状态反而最稳定； (3)
677	    RL regime是灾难性的：所有信号AUC降至0.60以下或刚到0.60—— RL的reward hacking改变了model的输出distribution（更confident、更formulaic），
678	    使得基于distribution shift的检测（Min-K%++, ConStat）几乎失效； (4) Self-Critique在RL regime下反而成为"最佳信号"（0.57），但仅因为其他信号更差——
679	    0.57的AUC几乎没有实用价值（sensitivity+specificity之和刚过1.0）； (5) SFT clean vs contaminated的AUC差异仅0.03，说明信号的下降主要由post-training本身
680	    而非contamination引起——信号检测的是"training变化"而非"contamination变化"。
681	
682	    '
683	  tables:
684	  - name: 'Table: Signal × Regime AUC Heatmap'
685	    columns:
686	    - signal
687	    - Base
688	    - SFT-Clean
689	    - SFT-Contam
690	    - RL
691	    rows:
692	    - - Embedding Retrieval
693	      - 0.78
694	      - 0.72
695	      - 0.72
696	      - 0.6
697	    - - Min-K%++
698	      - 0.73
699	      - 0.65
700	      - 0.68
701	      - 0.55
702	    - - ConStat
703	      - 0.71
704	      - 0.63
705	      - 0.66
706	      - 0.53
707	    - - Self-Critique
708	      - 0.6
709	      - 0.58
710	      - 0.63
711	      - 0.57
712	  - name: 'Table: Signal Survival Rate (AUC retention relative to Base)'
713	    columns:
714	    - signal
715	    - SFT-Clean
716	    - SFT-Contam
717	    - RL
718	    rows:
719	    - - Embedding Retrieval
720	      - 0.92
721	      - 0.92
722	      - 0.77
723	    - - Min-K%++
724	      - 0.89
725	      - 0.93
726	      - 0.75
727	    - - ConStat
728	      - 0.89
729	      - 0.93
730	      - 0.75
731	    - - Self-Critique
732	      - 0.97
733	      - 1.05
734	      - 0.95
735	  figures_description:
736	  - 'Fig: 4×4 heatmap with color coding. Clear left-to-right degradation gradient.
737	    RL column almost uniformly orange/red. Self-Critique row most stable (highest
738	    retention) but starts lowest.'
739	  - 'Fig: Survival curves plotting AUC retention across regimes. Embedding and Min-K++
740	    show steep RL drop. Self-Critique nearly flat but at low absolute level — ''stable
741	    but weak''.'
742	  analysis: '这个实验在reframed论文中升级为Core Contribution之一。关键叙事： "Current detection signals
743	    were designed for and evaluated on base/SFT models. We show that post-training
744	    — especially RL — systematically degrades all signals below the identifiability
745	    threshold established in our simulation study (exp-004)." Self-Critique的"stability"是pyrrhic——它稳定在0.57-0.63的range，从未达到可用水平。
746	    这直接支持"RL regime下calibration不可行"的结论，且解释了为什么： 不是方法不对，而是信号不存在。
747	
748	    '
749	- name: rl_observational_case_study
750	  plan_id: exp-009
751	  description: 'RL-trained models的观察性案例研究。worst档下calibration在RL regime中几乎完全失效， expected
752	    regret reduction接近零甚至为负。
753	
754	    '
755	  expected_results:
756	    models_evaluated: 8
757	    selfcritique_auc_avg_rl: 0.57
758	    rrf_auc_avg_rl: 0.59
759	    calibration_mae_4pl_gamma_pp: 10.5
760	    calibration_mae_uncalibrated_pp: 9.8
761	    calibration_mae_remove_rescore_pp: 9.2
762	    ci_width_95_avg_pp: 24.5
763	    ci_coverage_95: 0.82
764	    expected_regret_reduction_vs_uncalibrated: -0.03
765	    expected_regret_reduction_vs_remove_rescore: -0.08
766	    top5_model_selection_agreement_with_true: 0.6
767	    gamma_estimates_mean: 0.08
768	    gamma_ci_includes_zero_pct: 0.85
769	    nearzero_gamma_clean_benchmark_check: true
770	    nearzero_gamma_clean_value: 0.02
771	    deepseek_r1_gamma_ci_includes_zero: true
772	  result_rationale: 'RL observational case study是worst档中最清晰的negative result： (1) Signal
773	    AUC在RL regime下仅0.57-0.59（exp-008已预测），这意味着exposure scores 几乎是noise，输入到IRT模型中的是garbage-in；
774	    (2) 4PL+γ MAE 10.5pp反而比uncalibrated的9.8pp更差—— 模型在noisy exposure scores上"hallucinate"了不存在的contamination
775	    effect， 做出了比不校正更差的adjustment（overcorrection on false positives，undercorrection
776	    on true positives）； (3) expected regret reduction为-0.03（vs uncalibrated）和-0.08（vs
777	    remove-rescore）， 即calibration使model selection决策变差了——这是因为宽CI（24.5pp）导致model rankings变得更noisy，
778	    而uncalibrated scores虽然biased但至少preserves ranking well； (4) 85%的conditions下γ CI包含零，说明模型在RL
779	    regime下根本检测不到contamination—— 不是"检测到了但校正不够"，而是"γ与zero不可区分"； (5) 唯一的positive result是specificity
780	    check通过——clean benchmark上γ≈0.02， 说明模型至少没有在clean data上产生false positive contamination
781	    detection。 但这是一个低门槛的成功。
782	
783	    '
784	  tables:
785	  - name: 'Table: RL Case Study — Calibration Method Comparison'
786	    columns:
787	    - method
788	    - MAE_pp
789	    - CI Width 95%
790	    - Coverage 95%
791	    - Regret Reduction
792	    rows:
793	    - - Uncalibrated (naive)
794	      - 9.8
795	      - —
796	      - —
797	      - —
798	    - - 4PL+γ
799	      - 10.5
800	      - 24.5
801	      - 0.82
802	      - -0.03
803	    - - Remove-rescore
804	      - 9.2
805	      - —
806	      - —
807	      - —
808	    - - Linear regression+CI
809	      - 9.9
810	      - 21.0
811	      - 0.85
812	      - 0.01
813	  - name: 'Table: Per-Model γ Estimates (RL models)'
814	    columns:
815	    - model
816	    - gamma_mean
817	    - gamma_95ci_lower
818	    - gamma_95ci_upper
819	    - ci_excludes_zero
820	    rows:
821	    - - Qwen2.5-0.5B-Instruct
822	      - 0.12
823	      - -0.15
824	      - 0.39
825	      - false
826	    - - Qwen2.5-1.5B-Instruct
827	      - 0.08
828	      - -0.18
829	      - 0.34
830	      - false
831	    - - Qwen2.5-3B-Instruct
832	      - 0.05
833	      - -0.21
834	      - 0.31
835	      - false
836	    - - Qwen2.5-7B-Instruct
837	      - 0.03
838	      - -0.25
839	      - 0.31
840	      - false
841	    - - DeepSeek-R1-Distill-1.5B
842	      - 0.1
843	      - -0.14
844	      - 0.34
845	      - false
846	    - - DeepSeek-R1-Distill-7B
847	      - 0.06
848	      - -0.2
849	      - 0.32
850	      - false
851	  figures_description:
852	  - 'Fig: Expected regret curves. X-axis: number of models selected. Y-axis: expected
853	    regret. Uncalibrated line sits below 4PL+γ line across all selection sizes. Thin
854	    gray lines show bootstrap replicates — high variance, no consistent winner.'
855	  - 'Fig: γ forest plot for all RL models. All CIs cross zero. Horizontal span of
856	    CIs (~0.5) dwarfs point estimates (~0.05-0.12).'
857	  analysis: 'RL case study提供了worst档最dramatic的result：calibration不仅不帮忙，还hurt。 这是因为在signal
858	    quality低于identifiability threshold时，IRT模型的额外参数 成为了pure noise amplifier。对reframed论文的贡献有两层：
859	    (1) Empirical confirmation that RL regime falls below identifiability boundary;
860	    (2) Practical recommendation — "do not attempt calibration when signal AUC < 0.60"。
861	    Specificity check的通过（clean γ≈0）是一个consolation prize—— 模型不产生false contamination
862	    detection，但也检测不到real contamination。
863	
864	    '
865	- name: prior_sensitivity
866	  plan_id: exp-010
867	  description: 'Prior sensitivity分析。worst档下结果对prior选择异常敏感， 暴露了model specification的fragility。
868	
869	    '
870	  expected_results:
871	    gamma_prior_n01_mae_pp: 7.8
872	    gamma_prior_n005_mae_pp: 9.5
873	    gamma_prior_n02_mae_pp: 7.2
874	    gamma_prior_n005_gamma_mean_shrinkage_ratio: 0.45
875	    gamma_prior_n02_gamma_mean_inflation_ratio: 1.35
876	    mae_sensitivity_range_pp: 2.3
877	    ci_coverage_sensitivity_range: 0.12
878	    ci_coverage_n005: 0.85
879	    ci_coverage_n01: 0.78
880	    ci_coverage_n02: 0.72
881	    prior_sensitivity_index: 0.38
882	  result_rationale: 'prior sensitivity在worst档下远超acceptable水平： (1) N(0,0.5) tight prior强制γ向零shrink
883	    45%，产生undercorrection但paradoxically 提高了coverage（0.85 vs 0.78），因为tight prior限制了CI的overconfidence；
884	    (2) N(0,2) wide prior允许γ inflate 35%，MAE改善（7.2pp）但coverage恶化至0.72， 因为wider prior导致posterior更受likelihood影响，而likelihood在noisy
885	    data上是misleading的； (3) MAE sensitivity range 2.3pp（across prior choices）占MAE值的~30%——
886	    这意味着结果高度依赖modeler的prior choice，而不是data-driven； (4) 理想情况下（信号好、sample大），Bayesian方法应该prior-insensitive——
887	    sensitivity本身就是under-identification的symptom，因为data不够informative来override prior。
888	
889	    '
890	  tables:
891	  - name: 'Table: Prior Sensitivity Comparison'
892	    columns:
893	    - prior
894	    - gamma_mean
895	    - MAE_pp
896	    - Coverage 95%
897	    - CI Width 95% (pp)
898	    rows:
899	    - - N(0, 0.5)
900	      - 0.22
901	      - 9.5
902	      - 0.85
903	      - 15.2
904	    - - N(0, 1.0) [default]
905	      - 0.38
906	      - 7.8
907	      - 0.78
908	      - 19.5
909	    - - N(0, 2.0)
910	      - 0.51
911	      - 7.2
912	      - 0.72
913	      - 24.8
914	  figures_description:
915	  - 'Fig: γ posterior distributions under three priors (overlaid density plots). Wide
916	    separation between posteriors — data does not dominate prior. Clear visual evidence
917	    of under-identification.'
918	  analysis: 'Prior sensitivity ≥ 30% of point estimate confirms that the model is
919	    in an under-identified regime. 对reframed论文：这直接maps到exp-004 identifiability sweep中的"prior
920	    sensitivity"维度， 验证了仿真预测——在AUC<0.70时prior choice matters more than data.
921	
922	    '
923	- name: few_examinee_regime
924	  plan_id: exp-011
925	  description: 'Few-examinee regime仿真研究。worst档下即使使用Growing Pains pre-estimation策略，
926	    N<50时identifiability完全崩溃。
927	
928	    '
929	  expected_results:
930	    n20_gamma_rmse: 0.42
931	    n20_gamma_rel_bias: 0.55
932	    n20_theta_corr: 0.58
933	    n20_ci_coverage_95: 0.68
934	    n50_gamma_rmse: 0.28
935	    n50_gamma_rel_bias: 0.38
936	    n50_theta_corr: 0.72
937	    n50_ci_coverage_95: 0.75
938	    n100_gamma_rmse: 0.18
939	    n100_gamma_rel_bias: 0.25
940	    n100_theta_corr: 0.82
941	    n100_ci_coverage_95: 0.8
942	    n200_gamma_rmse: 0.12
943	    n200_gamma_rel_bias: 0.18
944	    n200_theta_corr: 0.88
945	    n200_ci_coverage_95: 0.85
946	    growing_pains_pretrain_improvement_n20_pct: 15
947	    growing_pains_pretrain_improvement_n50_pct: 10
948	    minimum_n_for_gamma_significant: 80
949	    minimum_n_for_coverage_nominal: 150
950	  result_rationale: 'few-examinee regime在worst档下与信号质量问题叠加： (1) N=20（现实中常见——很多benchmark只有20-50个models被评估）时，
951	    γ RMSE 0.42，rel_bias 55%，θ与ground truth correlation仅0.58—— 此时模型参数估计本质上是noise；
952	    (2) Growing Pains pre-estimation策略（借用大pool的item参数先验）仅改善15%， 因为bottleneck不是item参数估计而是γ-θ的joint
953	    estimation—— item参数可以借用外部信息，但γ-θ的confounding是data-inherent的，无法靠先验缓解； (3) 达到γ显著（即CI排除零）需要N≥80，达到nominal
954	    coverage需要N≥150—— 这两个threshold在realistic benchmark evaluation scenarios中很难满足 （HELM有~100
955	    models，但大部分benchmarks的evaluated model count远少于此）； (4) 即使N=200，在worst档的信号质量下（AUC~0.65-0.70），
956	    gamma_rel_bias仍有18%，coverage仅85%——仍未达到publishable quality。
957	
958	    '
959	  tables:
960	  - name: 'Table: Identifiability Metrics by Model Count (AUC=0.65)'
961	    columns:
962	    - N
963	    - gamma_RMSE
964	    - gamma_rel_bias
965	    - theta_corr
966	    - Coverage 95%
967	    - Growing Pains Δ
968	    rows:
969	    - - 20
970	      - 0.42
971	      - 55%
972	      - 0.58
973	      - 68%
974	      - +15%
975	    - - 50
976	      - 0.28
977	      - 38%
978	      - 0.72
979	      - 75%
980	      - +10%
981	    - - 100
982	      - 0.18
983	      - 25%
984	      - 0.82
985	      - 80%
986	      - +5%
987	    - - 200
988	      - 0.12
989	      - 18%
990	      - 0.88
991	      - 85%
992	      - +3%
993	  figures_description:
994	  - 'Fig: Identifiability surface — X: model count, Y: signal AUC, Z: γ relative bias
995	    (color-coded). Clear ridge at AUC≈0.70 below which no amount of models helps sufficiently.
996	    The ''green zone'' (rel_bias<10%) requires AUC>0.80 AND N>100.'
997	  analysis: '这个仿真扩展与exp-004共同构成identifiability map的完整版本。 关键新发现：model count和signal
998	    AUC是multiplicative而非additive—— 在AUC<0.70时，增加N的边际收益急剧递减（从N=100到N=200，改善仅7pp rel_bias）。
999	    这意味着"收集更多模型"不是解决identifiability的viable path when signals are weak。 对论文："minimum
1000	    signal quality targets for future work"可以被具体化为AUC×N的joint requirement。
1001	
1002	    '
1003	- name: observational_72b
1004	  plan_id: exp-012
1005	  description: 'Qwen2.5-72B观察性分析。worst档下大模型的信号质量进一步下降， confirm了scale-identifiability的inverse
1006	    relationship。
1007	
1008	    '
1009	  expected_results:
1010	    signal_auc_embedding: 0.6
1011	    signal_auc_minkpp: 0.56
1012	    signal_auc_constat: 0.54
1013	    signal_auc_selfcritique: 0.58
1014	    rrf_auc: 0.59
1015	    gamma_estimate: 0.04
1016	    gamma_ci_includes_zero: true
1017	    gamma_ci_width: 0.55
1018	    calibration_mae_pp: 11.2
1019	    ci_width_95_pp: 26.0
1020	  result_rationale: '72B模型将scale问题推向极端： (1) 72B的pretraining corpus几乎必然包含了benchmark
1021	    items的某种形式—— 不是传统意义的"contamination"而是"知识覆盖"，这使得所有detection signals的false positive
1022	    rate极高， embedding retrieval AUC降至0.60因为模型legitimately "knows" the content； (2)
1023	    γ estimate 0.04几乎为零，不是因为没有contamination而是因为unable to detect it—— 信号noise完全淹没了any
1024	    real signal； (3) 11.2pp MAE是worst档中最差的calibration error，因为72B的行为与smaller models
1025	    系统性不同（different error patterns, different item difficulty ordering）， IRT的transferability
1026	    across scales受到根本挑战。
1027	
1028	    '
1029	  tables:
1030	  - name: 'Table: 72B Observational Results'
1031	    columns:
1032	    - metric
1033	    - Qwen-72B
1034	    - Qwen-7B (controlled)
1035	    - Qwen-3B (controlled)
1036	    rows:
1037	    - - Best signal AUC
1038	      - 0.6
1039	      - 0.66
1040	      - 0.69
1041	    - - RRF AUC
1042	      - 0.59
1043	      - 0.63
1044	      - 0.67
1045	    - - γ estimate
1046	      - 0.04
1047	      - 0.25
1048	      - 0.34
1049	    - - γ CI excludes zero
1050	      - false
1051	      - Marginal (50%)
1052	      - true
1053	    - - Calibration MAE (pp)
1054	      - 11.2
1055	      - 8.5
1056	      - 7.8
1057	  figures_description:
1058	  - 'Fig: Scale vs signal AUC trend line from 0.5B to 72B. Clear monotonic decrease.
1059	    Horizontal dashed line at AUC=0.70 crossed between 1.5B and 3B scale. 72B is deep
1060	    in the ''unidentifiable'' zone.'
1061	  analysis: '72B结果是identifiability boundary story的natural endpoint： 在frontier model
1062	    scale上，calibration方法论本身不适用，因为"contamination"和"knowledge" 在概念层面就难以区分。这是reframed论文的strong
1063	    closing argument—— "our identifiability analysis reveals that contamination-aware
1064	    calibration faces a fundamental scale barrier: the very models most in need of
1065	    calibration (large, widely trained) are precisely those where calibration is least
1066	    feasible."
1067	
1068	    '
1069	- name: closed_weight_2signal_mode
1070	  plan_id: exp-013
1071	  description: '2-signal degraded mode (ConStat + Self-Critique) for closed-weight
1072	    models. worst档下降级模式使calibration完全不可行。
1073	
1074	    '
1075	  expected_results:
1076	    two_signal_rrf_auc_100pct_dosage: 0.64
1077	    two_signal_rrf_auc_50pct_dosage: 0.58
1078	    two_signal_rrf_auc_25pct_dosage: 0.54
1079	    calibration_mae_2signal_pp: 10.8
1080	    calibration_mae_4signal_pp: 7.8
1081	    mae_increase_relative_2_vs_4_signal: 0.38
1082	    ci_width_95_2signal_pp: 25.2
1083	    ci_coverage_95_2signal: 0.75
1084	    kendall_tau_2signal: 0.48
1085	    gamma_ci_includes_zero_2signal_pct: 0.72
1086	  result_rationale: '2-signal mode在worst档下是最差的配置： (1) ConStat和Self-Critique恰好是四个信号中AUC最低的两个（exp-002），
1087	    它们的fusion AUC 0.64远低于identifiability threshold 0.70； (2) MAE增加38%（从7.8pp到10.8pp），符合worst档的two_signal_degraded_mae_increase_relative范围[0.35,
1088	    0.6]； (3) Kendall τ降至0.48——低于0.5意味着calibrated rankings与true rankings的agreement
1089	    不比random好多少，calibration实际上在扰乱而非改善rankings； (4) 72%的conditions下γ CI包含零，说明在closed-weight
1090	    scenario下 contamination detection几乎完全不可行。 这是因为closed-weight模型不提供logits和embeddings，而这两个恰好是信号质量最高的信息源——
1091	    没有它们，剩余信号不足以支撑any meaningful calibration。
1092	
1093	    '
1094	  tables:
1095	  - name: 'Table: 2-Signal vs 4-Signal Calibration Gap'
1096	    columns:
1097	    - metric
1098	    - 4-signal
1099	    - 2-signal
1100	    - degradation
1101	    rows:
1102	    - - RRF AUC (100%)
1103	      - 0.7
1104	      - 0.64
1105	      - -8.6%
1106	    - - MAE (pp)
1107	      - 7.8
1108	      - 10.8
1109	      - +38%
1110	    - - CI Width 95% (pp)
1111	      - 19.5
1112	      - 25.2
1113	      - +29%
1114	    - - Kendall τ
1115	      - 0.62
1116	      - 0.48
1117	      - -23%
1118	    - - Coverage 95%
1119	      - 0.78
1120	      - 0.75
1121	      - -3.8%
1122	  figures_description:
1123	  - 'Fig: Side-by-side calibration error distributions (4-signal vs 2-signal). 2-signal
1124	    distribution shifted right with heavier tail. Overlap region highlighted — some
1125	    conditions where 2-signal accidentally performs okay, but median is significantly
1126	    worse.'
1127	  analysis: '2-signal degraded mode的failure confirm了一个important practical constraint：
1128	    closed-weight models（GPT-4, Claude等）——恰好是most scrutinized for contamination——
1129	    是calibration最不可行的targets。 对reframed论文：identifiability map需要一个新维度——"signal access
1130	    level" (full access: 4 signals; closed-weight: 2 signals)， 2-signal在identifiability
1131	    map上的viable region极小（仅AUC>0.80且N>150，现实中不存在）。'
1132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18e72bfe-fce4-414f-a243-4e0bd8aeb7f9",
  "isSidechain": true,
  "promptId": "f5b4b1be-f436-4f49-a431-ed03dead74ae",
  "agentId": "a5ae4aef38a931ce3",
  "type": "user",
  "uuid": "db711f3f-31da-4640-afea-8ad97078a8c9",
  "sourceToolAssistantUUID": "18e72bfe-fce4-414f-a243-4e0bd8aeb7f9",
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

_source line 61 · 2026-05-13T16:44:58.004Z_

I now have a comprehensive understanding of all three tiers and the full project. The paper I'm reviewing is the **worst tier** version -- the one titled "Empirical Identifiability Boundaries for Contamination-Aware IRT Calibration of LLM Benchmarks" which was reframed from a calibration paper into an identifiability analysis paper because the core calibration claims failed. Let me now compose my detailed R1 review.

---

## R1 Review: Methods and Experiments

**Paper**: "Empirical Identifiability Boundaries for Contamination-Aware IRT Calibration of LLM Benchmarks"
**Venue**: AAAI 2027
**Reviewer Focus**: Methods and Experiments

---

### Summary

This paper investigates when contamination-aware IRT calibration of LLM benchmarks is empirically identifiable. The authors augment 4PL IRT with a contamination covariate gamma, use RRF fusion of 4 detection signals as exposure estimates, and run controlled SFT injection experiments across Qwen2.5 models (0.5B--7B), 4 benchmarks, and 5 dosage levels. The core finding is negative: calibration is identifiable only under stringent conditions (signal AUC >= 0.70, N >= 80) that are rarely met in practice. RL post-training degrades all signals below threshold, and identifiability worsens with model scale. The paper was reframed from a "calibration solution" into a "when is calibration solvable" analysis.

---

### Strengths

**S1: Honest negative-result framing with rigorous self-diagnosis.** The paper makes a difficult but valuable intellectual contribution by systematically mapping the conditions under which a principled method fails. Table 6 shows 4PL+gamma MAE of 7.8pp vs linear regression's 7.2pp (p=0.23), and instead of cherry-picking favorable conditions, the authors present this transparently as evidence of under-identification. Table 16 shows the RL case study where 4PL+gamma actually performs WORSE than uncalibrated scores (MAE 10.5pp vs 9.8pp, negative regret reduction -0.03). This level of honesty is commendable and rare.

**S2: Comprehensive identifiability analysis across multiple dimensions.** The paper establishes identifiability boundaries along 5 axes: signal AUC (Table 2: only Embedding Retrieval at 100% dosage reaches 0.70), model count (Table 11: N>=80 for significance, N>=150 for coverage), model scale (Tables 14-15: 7B AUC 0.66, gamma-theta corr 0.58), prior sensitivity (Table 10: MAE varies 2.3pp, 30% of estimate), and training regime (Tables 12-13: RL causes 27% AUC reduction). The synthesis in Table 19 crystallizes these into actionable conditions. This multi-dimensional analysis is methodologically sophisticated.

**S3: Rigorous controlled experimental setup with appropriate ground truth.** The SFT injection design (exp-001) covering 3 model scales x 5 dosage levels x 4 benchmarks with paraphrase-based contamination is well-motivated by prior work (Emperor's New Clothes, ICML 2025). The dual-track validation approach -- controlled SFT for internal validity plus ecological RL case study for external validity -- is sound experimental methodology. The specificity check (near-zero gamma on clean benchmarks) is a thoughtful control.

**S4: Stan model specification is principled.** The 4PL+gamma Stan code correctly implements the contamination-augmented IRT model with appropriate priors (lognormal for discrimination, beta priors for guessing/ceiling, standard normal for gamma). The NUTS sampler configuration (adapt_delta=0.95, 4 chains, 1000 warmup + 1000 sampling) follows Stan best practices. The MVP simulation validated identifiability on synthetic data before moving to real experiments (gamma relative bias <8%, theta correlation >0.94).

**S5: Catch-22 insight is novel and impactful.** The finding that signal AUC positively correlates with dosage -- signals are strongest precisely when contamination is most obvious and calibration is least needed (100% dosage), while signals are near-random (AUC 0.51-0.54) when contamination is subtle (5% dosage) where calibration would be most valuable -- is a fundamental contribution to the contamination detection literature regardless of the IRT framework.

---

### Weaknesses

**W1: The additive gamma specification is a critical modeling limitation that the paper under-diagnoses.** The Stan model uses `gamma * exposure[i,j]` as a single scalar parameter, assuming contamination has a uniform additive effect on the logit scale across all items and models. Table 1 directly contradicts this: inflation at 100% dosage ranges from +3.9pp (HumanEval, 3B) to +11.5pp (MMLU, 0.5B) -- a 3x range. Inflation is inversely related to model scale (0.5B: +11.5pp vs 3B: +5.2pp at 100% dosage), demonstrating that gamma interacts with theta. This theta-gamma interaction means the additive model is structurally misspecified, which cascades into the high posterior correlation (0.52-0.58) reported as "identifiability failure" but is really model misspecification. The paper should have tested a multiplicative or interaction model (e.g., `gamma_j * exposure[i,j]` with item-specific gamma, or `gamma * f(theta_i) * exposure[i,j]`) and discussed whether the identifiability boundaries would shift under better-specified models. **Severity: Major.** The paper's central contribution -- identifiability boundaries -- may be artifacts of the model specification rather than fundamental limits.

**W2: RRF fusion provides no benefit over the best single signal, undermining Claim 2.** Tables 4-5 show RRF AUC of 0.70 vs best single signal (Embedding Retrieval) at 0.72 -- RRF is actually 2pp worse. The pairwise signal correlation averaging 0.58 explains this: signals lack sufficient complementarity. The paper still frames RRF as a contribution ("principled contamination exposure estimation"), but the data shows that simply using Embedding Retrieval alone would be superior. Claim 2 (Signal Aggregation Claim) from the paper framing should be explicitly abandoned or reframed as a negative finding about signal diversity requirements. As stated, the paper presents a method component (RRF) that actively harms performance while still claiming it as a contribution.

**W3: Single model family (Qwen2.5) severely limits generalizability.** All controlled experiments use Qwen2.5 at various scales. The RL observational study adds DeepSeek-R1-Distill models, but without ground truth. The identifiability boundaries established here may be specific to Qwen2.5's architecture, tokenizer, or training data distribution. Different model families (Llama, Mistral, GPT-NeoX) may have different memorization patterns and therefore different signal AUC profiles, potentially shifting the identifiability boundaries substantially. Table 3 already shows scale-dependent signal AUC (ER drops from 0.75 at 0.5B to 0.69 at 3B), and this trend may not generalize across architectures.

**W4: MCMC diagnostics indicate problematic posterior geometry.** The paper reports R-hat up to 1.08, 3.2% divergent transitions, and ESS as low as 180. Standard Stan recommendations require R-hat < 1.01, divergent fraction < 0.1%, and ESS > 400 per chain. These violations suggest the posterior has pathological geometry (ridges/funnels) that NUTS cannot properly explore, likely due to the gamma-theta near-non-identifiability. The reported posteriors and CIs may therefore be unreliable. The paper acknowledges this but does not attempt reparameterization, tighter priors, or alternative samplers to resolve it. This undercuts the paper's uncertainty quantification claims.

**W5: exp-004 (identifiability map) is synthesized across experiments rather than run as a standalone simulation sweep.** The experiment plan calls for a 144-condition systematic sweep (6 AUC levels x 4 model counts x 3 prior strengths x 2 exposure types, 10 seeds each). Instead, Table 19 synthesizes identifiability boundaries from across the other experiments. This means the boundaries are not established by a controlled simulation holding other factors constant, but inferred from experiments where multiple factors vary simultaneously. The boundaries may therefore conflate the effects of signal quality, model count, model scale, and training regime rather than isolating each factor's contribution.

---

### Minor Issues

1. **Table 8 (dose-response)**: gamma CI includes zero at both 5% and 25% dosage. The paper does not discuss what this means for real-world contamination, where most unintentional contamination is likely in the 5-25% range.

2. **ConStat circularity concern**: The paper uses paraphrase-based SFT injection, and ConStat measures original-vs-paraphrase performance gaps. Since the paraphrases ARE the contamination, ConStat's signal is partially tautological in this setup. Its AUC in a real-world setting (where contamination is not necessarily paraphrase-based) may be even lower.

3. **Self-Critique described as "stable" at 0.57 under RL (Table 12)**: This is misleading labeling. An AUC of 0.57 is barely above chance (0.50) and provides essentially no decision value. Calling it "stable" because it didn't degrade much from an already-poor baseline obscures the fact that it is not usable.

4. **Missing baseline -- DCR**: The paper framing lists DCR (EMNLP 2025) as baseline #6 and states "must include or reviewers will reject," but it does not appear in the reported results tables.

5. **No multiple testing correction**: Tables 4-5 report pairwise comparisons without Bonferroni or BH correction. Table 6 reports a single p-value (0.23) but the paper makes multiple comparisons across methods and benchmarks.

6. **The 15pp "practical utility threshold" for CI width appears arbitrary**: No justification is given for why 15pp (rather than 10pp or 20pp) is the boundary of practical utility.

---

### Questions for Authors

**Q1**: Have you considered a gamma specification that allows interaction with theta (e.g., gamma_i per model, or gamma * g(theta_i))? The scaling pattern in Table 1 (smaller models inflate more) strongly suggests the additive assumption is violated. Would identifiability boundaries shift under a better-specified model?

**Q2**: Given that RRF consistently underperforms the best single signal, why not simply use Embedding Retrieval as the sole exposure signal in the 4-signal regime? What is the principled argument for keeping RRF when the data shows it hurts?

**Q3**: The MCMC diagnostics (R-hat 1.08, 3.2% divergences, ESS 180) are substantially outside Stan's recommended thresholds. Did you attempt non-centered parameterization, prior tightening, or reparameterized models to improve sampling? How confident are you that the posterior CIs are reliable given these diagnostics?

**Q4**: Table 19 synthesizes identifiability boundaries from 13 different experiments. Have you verified these boundaries with the planned exp-004 standalone simulation sweep? If not, how do you disentangle the contributions of signal AUC vs model count vs model scale vs training regime?

**Q5**: What is the authors' recommendation to the community, given that their identifiability conditions are "rarely met" (as stated in the abstract)? If contamination-aware calibration is not feasible for the models and settings where it matters most, what should practitioners do instead?

---

### Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 4/10 | The core 4PL+gamma model has a structural misspecification (additive gamma) contradicted by the data. MCMC diagnostics are outside acceptable thresholds. The central identifiability boundaries may be artifacts of model choice. RRF is presented as a contribution despite degrading performance. |
| **Experimental Quality** | 6/10 | Comprehensive experimental design covering 13 planned experiments. Good controlled injection setup with dual-track validation. But: single model family, no standalone identifiability simulation, missing DCR baseline, problematic MCMC convergence. |
| **Clarity** | 6/10 | The reframing from calibration to identifiability is well-executed narratively. Tables are numerous and detailed. But the paper tries to tell too many stories across 19 tables, and some labeling is misleading (e.g., "stable" for AUC 0.57). |
| **Overall Assessment** | 4/10 | The paper presents interesting negative findings, but the core contribution -- identifiability boundaries -- may be specific to the (misspecified) additive gamma model rather than fundamental limits. The method component (RRF fusion) actively hurts performance. For AAAI 2027 at 17.6% acceptance, this is below threshold. The catch-22 insight and signal survival analysis are publishable contributions, but need to be disentangled from the questionable IRT specification. |
| **Confidence** | 4/5 | I have strong familiarity with IRT models, Bayesian computation, and benchmark contamination detection. The Stan code review and MCMC diagnostic analysis are based on established standards. My uncertainty is in whether a better model specification would substantially change the identifiability boundaries. |

**Recommendation**: Reject (with encouragement to resubmit after addressing W1). The catch-22 insight and signal survival analysis are genuinely novel contributions, but the paper's headline claim -- identifiability boundaries for contamination-aware IRT -- is undermined by a model specification that the paper's own data contradicts. Addressing the additive gamma assumption (W1) and running the standalone simulation sweep (W5) could transform this into a strong submission.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db711f3f-31da-4640-afea-8ad97078a8c9",
  "isSidechain": true,
  "agentId": "a5ae4aef38a931ce3",
  "requestId": "req_011CazuLzrArpPHVwWqxb4gH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f380ae3a-5ac7-41f7-9444-adaf518c8db5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "cf7713ee-84a1-45ab-aa08-0b655cc1ab71",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CTYjg9iTW7FFSRMg7XB3x4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19938,
      "cache_read_input_tokens": 92521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19938,
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
