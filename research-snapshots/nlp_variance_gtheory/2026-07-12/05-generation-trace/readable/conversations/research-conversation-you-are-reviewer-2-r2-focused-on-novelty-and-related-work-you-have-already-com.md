# Research conversation: You are Reviewer 2 (R2), focused on Novelty and Related Work. You have already completed your independent review (below)

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4c74b9b0b0cbe40b.jsonl`
- **Structured JSON:** [`dc56fc3ef4bfdfa5a2b0.json`](../../sessions/dc/dc56fc3ef4bfdfa5a2b0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-21T06:06:22.404Z_

You are Reviewer 2 (R2), focused on Novelty and Related Work. You have already completed your independent review (below). Now you are shown Reviewer 1's review. Please react to R1's points — identify areas where you agree, disagree, or have additional insights. Also note if R1 raised something that changes your assessment.

## YOUR (R2) ORIGINAL REVIEW:

### Strengths (Novelty/Positioning)
- S1: IRT vs G-theory comparison is genuinely novel and actionable
- S2: Model-as-crossed-facet is a meaningful design choice extending Mesting (2026)
- S3: Cross-benchmark variance gradient would be strong if completed
- S4: Positioning against IRT literature is thoughtful
- S5: Dual-metric analysis (binary vs text-exact-match) is genuinely non-obvious

### Weaknesses (Novelty/Positioning)
- W1: Primarily empirical extension of Mesting (2026), not methodological advance, but framed as if more
- W2: Missing citations (Sclar et al. 2024, Kunievsky & Evans 2025, Bui et al. 2025, classical psychometrics on binary G-theory)
- W3: Positioning against Mesting needs nuance — judge excluded here but was 43.8% in Mesting, mechanically inflating item_id
- W4: Item dominance partially expected from measurement theory, oversold
- W5: model×item on 4 models is marginal for random-effects estimation
- W6: Scope narrowing weakens title's ambition

### Scores: Novelty 5, Significance 6, Related Work 5, Overall 5

---

## R1'S REVIEW (Methods and Experiments focus):

### Strengths (Methods/Experiments)
- S1: Comprehensive factorial design (7-facet fully crossed, 825,600 records)
- S2: Extensive robustness checking (6 methodological defenses)
- S3: IRT vs G-theory comparison (3.3× ratio)
- S4: Item resampling stability test (CV=0.30 honestly reported)
- S5: Dual-metric analysis (87× gap)

### Weaknesses (Methods/Experiments)
- W1: model×item CI [3.1, 12.8] includes trivially small values
- W2: Cross-benchmark evidence inadequate (1.5 benchmarks)
- W3: REML on binary data — fundamental concern not fully resolved; no comparison with logistic-link generalized G-theory (Jiang & Skorupski 2017)
- W4: Single GPU architecture undermines separability claims
- W5: Item resampling CV=0.30 undermines precision; D-study projections should propagate this uncertainty
- W6: Four models insufficient for stable model-as-facet estimation (guidelines: 5-6+ levels)

### Questions for Authors
- Q1: D-study projections across the 3 resampling draws — are item count recommendations stable?
- Q2: Pairwise 2-model model×item estimates for all 6 pairs?
- Q3: IRT model specifics (2PL) and SE<0.3 threshold justification?
- Q4: Qwen3 re-execution time confound verification?

### Scores: Soundness 5, Experimental Quality 5, Overall 5

---

## YOUR TASK

React to R1's review in 300-500 words. Structure:

1. **Points of Agreement** — which of R1's points do you find compelling from a novelty perspective?
2. **Points of Disagreement** — where do you think R1 is too harsh or too lenient?
3. **New Insights** — did R1 raise anything that changes your novelty/significance assessment?
4. **Score Adjustment** — would you adjust your scores after seeing R1's review? If so, how and why?


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "1ee5b7cf-6fc6-4295-86fc-9d531d02db0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T06:06:22.407Z_

```json
{
  "parentUuid": "1ee5b7cf-6fc6-4295-86fc-9d531d02db0c",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
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
  "uuid": "974a0d07-ec5b-496d-9456-41855f184d4e",
  "timestamp": "2026-05-21T06:06:22.407Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T06:06:25.357Z_



I'll first read the report and any relevant project files to ground my reaction properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "974a0d07-ec5b-496d-9456-41855f184d4e",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDEmRWpWtmDxmtS9RpW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae8f3377-b527-41a8-a176-a44f5b691168",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CozmcfUTWCf1k4s5MbKGeN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7050,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7050,
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

_source line 4 · 2026-05-21T06:06:25.735Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WTCaDegKpi3NYPwskM2XHc`</summary>

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
  "parentUuid": "ae8f3377-b527-41a8-a176-a44f5b691168",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDEmRWpWtmDxmtS9RpW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ca97f0b-8d71-427b-951d-34b5be387458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CozmcfUTWCf1k4s5MbKGeN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7050,
      "cache_read_input_tokens": 8250,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7050
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 106,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7050,
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

_source line 5 · 2026-05-21T06:06:25.738Z_

<details><summary>↩ Tool result · `toolu_01WTCaDegKpi3NYPwskM2XHc`</summary>

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
  "parentUuid": "7ca97f0b-8d71-427b-951d-34b5be387458",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "3041b184-b6da-4ea0-a1c0-5f85eba0127f",
  "sourceToolAssistantUUID": "7ca97f0b-8d71-427b-951d-34b5be387458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T06:06:28.590Z_



Let me read the report to fully ground my reaction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3041b184-b6da-4ea0-a1c0-5f85eba0127f",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDF1fm84i2E7NnxEcRZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "debacebe-1a21-4e06-8a15-e22160f86fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013AryM9xmukF6XMjHK6vzFe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 15300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

_source line 7 · 2026-05-21T06:06:28.993Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018ZvG3vmSb5DdYkP5fL5yZx`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "debacebe-1a21-4e06-8a15-e22160f86fc9",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDF1fm84i2E7NnxEcRZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "510f2d07-ce73-4798-b95b-34d9c0f0274a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013AryM9xmukF6XMjHK6vzFe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 15300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

_source line 8 · 2026-05-21T06:06:29.005Z_

<details><summary>↩ Tool result · `toolu_018ZvG3vmSb5DdYkP5fL5yZx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp001_qwen | Qwen3-8B variance decomposition at full scale (1,296 conditions × 200 items) completes the 4-model design for cross-model G-theory analysis — tests whether item_id dominance and model×item interaction patterns hold with a 4th architecturally distinct model (Claim 1) | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp001_mistral** (success): Mistral-7B-Instruct-v0.3 variance decomposition at full scale (1,296 conditions × 200 items) will contribute to cross-model G-theory analysis — model-as-facet tests whether item_id dominance holds across architecturally diverse models (Claim 1) ← 基于 exp001_llama\\n- **exp001_gemma** (success): Gemma-2-9b-it variance decomposition at full scale (1,296 conditions × 200 items) will show model-specific variance structure differences compared to Llama — enabling model-as-facet analysis (Claim 1 make-or-break) ← 基于 exp001_llama\\n- **exp001_llama** (success): Single-model (Llama-3.1-8B-Instruct) G-theory variance decomposition at full scale (1,296 conditions × 200 items across 3 precisions × 3 temperatures × 6 prompts × 6 seeds × 4 orderings) will confirm MVP findings: item_id dominates binary_correct variance, while text_exact_match reveals infrastructure×methodology interactions ← 基于 mvp_phase_a\\n\\n## 趋势\\n成功 5 / 负向 1 / 失败 0 / 共 6\\nitems_per_condition: 200 →（近 3 次 success）\\ntotal_records: 259200 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32570: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1584, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "510f2d07-ce73-4798-b95b-34d9c0f0274a",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "db088e6c-f092-4389-8e89-5632ebeda223",
  "sourceToolAssistantUUID": "510f2d07-ce73-4798-b95b-34d9c0f0274a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T06:06:29.456Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H5akJQJw7pVMdEvcr2nhm5`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db088e6c-f092-4389-8e89-5632ebeda223",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDF1fm84i2E7NnxEcRZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21468bd3-cc7f-433c-842b-c05aa6a63a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013AryM9xmukF6XMjHK6vzFe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 15300,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1288
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 15300,
          "cache_creation_input_tokens": 1288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1288,
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

_source line 10 · 2026-05-21T06:06:29.464Z_

<details><summary>↩ Tool result · `toolu_01H5akJQJw7pVMdEvcr2nhm5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T14:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"gtheory_evaluation\\\"\\n    name: \\\"G-Theory & Evaluation Variance\\\"\\n    narrative: \\\"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\\\"\\n  - key: \\\"infrastructure_variance\\\"\\n    name: \\\"Infrastructure-Induced Variance\\\"\\n    narrative: \\\"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\\\"\\n  - key: \\\"prompt_sensitivity\\\"\\n    name: \\\"Prompt Sensitivity & Methodological Variance\\\"\\n    narrative: \\\"Prompt phrasing, seed, temperature, and ordering as variance sources\\\"\\n  - key: \\\"evaluation_methodology\\\"\\n    name: \\\"Evaluation Methodology\\\"\\n    narrative: \\\"Scoring artifacts, benchmark design, and evaluation protocol considerations\\\"\\n\\npapers:\\n  mesting2026hidden:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\\\"\\n    authors:\\n      - \\\"Mesting, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.11581\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  brittlebench2026:\\n    title: \\\"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.13285\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  yuan2025layercast:\\n    title: \\\"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\\\"\\n    authors:\\n      - \\\"Yuan, Z.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09501\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  messina2026background:\\n    title: \\\"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\\\"\\n    authors:\\n      - \\\"Messina, P.\\\"\\n      - \\\"Scotta, A.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.22411\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  generalizit2024:\\n    title: \\\"GeneralizIT: A Python Solution for Generalizability Theory Computations\\\"\\n    authors: []\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2411.17880\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  hua2025flaw:\\n    title: \\\"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\\\"\\n    authors:\\n      - \\\"Hua, W.\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    category: \\\"evaluation_methodology\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  thinkingmachines2025batch:\\n    title: \\\"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"Technical Report\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  kunievsky2025intent:\\n    title: \\\"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\\\"\\n    authors:\\n      - \\\"Kunievsky, D.\\\"\\n      - \\\"Evans, J.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.16584\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  bui2025seeds:\\n    title: \\\"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\\\"\\n    authors:\\n      - \\\"Bui, T.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  sameprompt2026:\\n    title: \\\"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.14349\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\", \"total_chars\": 6732, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21468bd3-cc7f-433c-842b-c05aa6a63a7f",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "3a25f6be-d081-403a-8ba3-e64b17af9bce",
  "sourceToolAssistantUUID": "21468bd3-cc7f-433c-842b-c05aa6a63a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T06:06:32.134Z_

Now let me read the paper draft itself for full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a25f6be-d081-403a-8ba3-e64b17af9bce",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDFHmdrFLXCw6Tfom4y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8320ada-d2a6-4061-9376-aaec2eca52a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Wb1BGw87V2om7ykUShTi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3707,
      "cache_read_input_tokens": 16588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3707,
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

_source line 12 · 2026-05-21T06:06:32.802Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VWd25kSRR1Bt7fhNAnqVsg`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8320ada-d2a6-4061-9376-aaec2eca52a3",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDFHmdrFLXCw6Tfom4y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8551f5b5-5a08-4f90-95fa-1bea827083ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Wb1BGw87V2om7ykUShTi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3707,
      "cache_read_input_tokens": 16588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3707,
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

_source line 13 · 2026-05-21T06:06:32.833Z_

<details><summary>↩ Tool result · `toolu_01VWd25kSRR1Bt7fhNAnqVsg`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/paper.tex
artifacts/dream_reports/dream_20260520T190053/median/paper.tex
artifacts/dream_reports/dream_20260520T190053/worst/paper.tex
artifacts/dream_reports/dream_20260520T222113/best/paper.tex
artifacts/dream_reports/dream_20260520T222113/median/paper.tex
artifacts/dream_reports/dream_20260520T222113/worst/paper.tex
artifacts/dream_reports/dream_20260521T032813/best/paper.tex
artifacts/dream_reports/dream_20260521T032813/median/paper.tex
artifacts/dream_reports/dream_20260521T032813/worst/paper.tex
artifacts/dream_reports/dream_20260521T044739/best/paper.tex
artifacts/dream_reports/dream_20260521T044739/median/paper.tex
artifacts/dream_reports/dream_20260521T044739/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8551f5b5-5a08-4f90-95fa-1bea827083ec",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "ab2c894c-5a08-4238-9f9e-073b0370b449",
  "sourceToolAssistantUUID": "8551f5b5-5a08-4f90-95fa-1bea827083ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T06:06:33.680Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01G45pJQGZL2Nof8fGfCnzs7`</summary>

```json
{
  "pattern": "**/paper*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab2c894c-5a08-4238-9f9e-073b0370b449",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDFHmdrFLXCw6Tfom4y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0a8333b-0889-4dbd-92b7-39a03a5512cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Wb1BGw87V2om7ykUShTi3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3707,
      "cache_read_input_tokens": 16588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3707,
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

_source line 15 · 2026-05-21T06:06:33.712Z_

<details><summary>↩ Tool result · `toolu_01G45pJQGZL2Nof8fGfCnzs7`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/paper_framing.md
artifacts/dream_reports/dream_20260520T190053/median/paper_framing.md
artifacts/dream_reports/dream_20260520T190053/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T222113/best/paper_framing.md
artifacts/dream_reports/dream_20260520T222113/median/paper_framing.md
artifacts/dream_reports/dream_20260520T222113/worst/paper_framing.md
artifacts/dream_reports/dream_20260521T032813/best/paper_framing.md
artifacts/dream_reports/dream_20260521T032813/median/paper_framing.md
artifacts/dream_reports/dream_20260521T032813/worst/paper_framing.md
artifacts/dream_reports/dream_20260521T044739/best/paper_framing.md
artifacts/dream_reports/dream_20260521T044739/median/paper_framing.md
artifacts/dream_reports/dream_20260521T044739/worst/paper_framing.md
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0a8333b-0889-4dbd-92b7-39a03a5512cb",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "7b7adc53-c393-485a-93ea-5cbbe88be30e",
  "sourceToolAssistantUUID": "d0a8333b-0889-4dbd-92b7-39a03a5512cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T06:06:33.809Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014rJo8A8RDp327EnwZjuM8n`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b7adc53-c393-485a-93ea-5cbbe88be30e",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDFHmdrFLXCw6Tfom4y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21bb2146-1b19-419b-89a2-b579b3cf4ed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Wb1BGw87V2om7ykUShTi3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3707,
      "cache_read_input_tokens": 16588,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 16588,
          "cache_creation_input_tokens": 3707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3707,
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

_source line 17 · 2026-05-21T06:06:33.817Z_

<details><summary>↩ Tool result · `toolu_014rJo8A8RDp327EnwZjuM8n`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21bb2146-1b19-419b-89a2-b579b3cf4ed6",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "119349ac-35b8-4e73-b97d-e02d45215086",
  "sourceToolAssistantUUID": "21bb2146-1b19-419b-89a2-b579b3cf4ed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T06:06:36.624Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L29Ggx17H8mkBGh9p7wea8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "119349ac-35b8-4e73-b97d-e02d45215086",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDFcMan8df68bVruBfh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "049c370e-9741-40fb-9834-0ea1711a151e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEhqTg9wpTMayAahmC1z4U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 20295,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 974
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 20295,
          "cache_creation_input_tokens": 974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 974,
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

_source line 19 · 2026-05-21T06:06:36.639Z_

<details><summary>↩ Tool result · `toolu_01L29Ggx17H8mkBGh9p7wea8`</summary>

```text
1	\documentclass[letterpaper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[margin=1in]{geometry}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{natbib}
11	\usepackage{caption}
12	\usepackage{subcaption}
13	\usepackage{array}
14	\usepackage{tablefootnote}
15	
16	\newcommand{\gcoeff}{\ensuremath{G}}
17	\newcommand{\pct}{\%}
18	
19	\title{Reproducibility Budgets for LLM Evaluation:\\A Generalizability Theory Analysis of Variance Sources\\Across Benchmarks, Models, and Evaluation Metrics}
20	
21	\author{Anonymous}
22	
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	% ============================================================
29	% ABSTRACT
30	% ============================================================
31	\begin{abstract}
32	When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, or item selection---let alone how these factors interact.
33	We conduct the first multi-benchmark Generalizability Theory (G-theory) study that crosses infrastructure (numerical precision, GPU hardware) with methodology (prompt template, random seed, sampling temperature, option ordering) and measurement (test items) factors, treating model as a crossed random facet.
34	Across 4.3 million item-level records spanning four models (Llama-3.1-8B, Gemma-2-9B, Mistral-7B, Qwen3-8B), five benchmarks (MMLU, HellaSwag, ARC-Challenge, GSM8K, MATH), and two GPU architectures, we report three findings.
35	First, item selection dominates single-model variance (60.4\pct{} on MMLU) but model$\times$item interaction emerges as the second-largest source (24.1\pct{}) when model is a crossed facet, collapsing cross-model generalizability from $\gcoeff{}=0.618$ to $\gcoeff{}=0.065$.
36	Second, infrastructure$\times$methodology interactions are negligible under binary scoring ($<$0.5\pct{}), confirming conditional separability.
37	Third, item dominance follows a monotonically decreasing gradient from knowledge-retrieval (MMLU: 60.4\pct{}) to multi-step reasoning benchmarks (MATH: 22.1\pct{}), with Spearman $\rho=1.0$ against task complexity---the variance structure itself is benchmark-conditional.
38	D-study projections show that G-theory requires $4.4\times$ more items than IRT to achieve $\gcoeff{}\geq0.80$ because it accounts for prompt, seed, and ordering dimensions that IRT ignores.
39	Reasoning-intensive benchmarks demand 1.9$\times$ the item budget of knowledge benchmarks (GSM8K: 900 vs.\ MMLU: 480 items).
40	A fine-tuning G-study reveals a qualitative regime change: training-time variance (seed$\times$learning-rate: 28.4\pct{}) supplants item dominance.
41	We release an open-source G-theory toolkit for computing benchmark-specific reproducibility budgets.
42	\end{abstract}
43	
44	% ============================================================
45	% 1. INTRODUCTION
46	% ============================================================
47	\section{Introduction}
48	
49	Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks.
50	A growing body of work has documented substantial variance from individual factors: up to 9\pct{} accuracy fluctuation from numerical precision alone \citep{yuan2025}, 50\pct{} of variance attributable to prompt phrasing on open-weight models \citep{brittlebench2026}, and 80 out of 1,000 unique completions at temperature zero due to batch-invariant kernel failures \citep{thinkingmachines2025}.
51	Yet every prior study isolates at most two sources, leaving the field without a unified picture of how infrastructure, methodology, and measurement factors interact---and whether conclusions drawn from one benchmark transfer to another.
52	
53	Generalizability Theory \citep{shavelson1991,brennan2001}, a psychometric framework for decomposing measurement variance into attributable sources, offers a principled lens.
54	\citet{mesting2026} adapted G-theory to LLM evaluation with five methodological facets (prompt, judge, temperature, seed, item) but treated infrastructure as fixed and studied a single benchmark.
55	IRT-based approaches \citep{lalor2019,rodriguez2021,polo2024} have analyzed item-level properties and efficient subsampling but from a fundamentally different perspective: IRT models person ability and item difficulty on a shared scale, while G-theory decomposes total variance into facet contributions and their interactions, yielding D-study projections for reliability under alternative designs.
56	No study has crossed infrastructure and methodology in a unified G-theory framework, compared variance structure across benchmarks, or provided metric-conditional reproducibility budgets.
57	
58	Our G-theory analysis across five benchmarks reveals that the variance structure itself is benchmark-conditional, rendering any ``universal reproducibility recipe'' illusory.
59	Item dominance decreases monotonically from knowledge-retrieval tasks (MMLU: 60.4\pct{}) through commonsense reasoning (HellaSwag: 50.4\pct{}) and science reasoning (ARC-C: 42.1\pct{}) to mathematical reasoning (GSM8K: 28.3\pct{}, MATH: 22.1\pct{}), with a perfect rank correlation ($\rho=1.0$) against cognitive complexity.
60	Meanwhile, model$\times$item interaction remains persistently high (21--25\pct{}) across all benchmarks, constituting a fundamental, benchmark-modulated barrier to cross-model generalizability.
61	
62	We make four contributions:
63	\begin{enumerate}
64	    \item \textbf{Model$\times$item interaction as hidden dominant source.} When model is treated as a crossed facet, model$\times$item interaction (24.1\pct{} on MMLU) collapses cross-model $\gcoeff{}$ from 0.618 to 0.065. This is the first G-theory quantification of cross-model item-level disagreement in LLM evaluation.
65	    \item \textbf{Confirmatory separability with metric qualification.} Infrastructure$\times$methodology interactions are negligible under binary scoring ($<$0.5\pct{}), providing empirical support for isolated-factor studies. Under text-exact-match, precision$\times$temperature reaches 0.83\pct{}, consistent with floating-point non-associativity.
66	    \item \textbf{IRT vs.\ G-theory: the cost of multi-facet reliability.} G-theory requires $4.4\times$ more items than IRT (510 vs.\ 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores.
67	    \item \textbf{Practitioner toolkit.} Open-source G-theory pipeline with benchmark-specific D-study budget tables, temperature-stratified reliability guides, and model-as-facet analysis templates.
68	\end{enumerate}
69	
70	% ============================================================
71	% 2. RELATED WORK
72	% ============================================================
73	\section{Related Work}
74	
75	\paragraph{Variance in ML evaluation.}
76	\citet{bouthillier2021} decomposed ML benchmark variance via ANOVA across hyperparameters, data splits, and random seeds, establishing factorial variance decomposition as a tool for understanding irreproducibility.
77	\citet{henderson2018} applied similar methodology to deep reinforcement learning, showing that implementation details can reverse algorithm rankings.
78	\citet{dodge2020} and \citet{sellam2022} demonstrated fine-tuning instability from random seeds and data ordering in BERT-family models.
79	\citet{dehghani2021} showed that benchmark ``winners'' depend on which subset of tasks and metrics are selected.
80	
81	\paragraph{LLM evaluation variance.}
82	\citet{yuan2025} documented up to 9\pct{} accuracy variation from numerical precision, attributing it to floating-point non-determinism.
83	\citet{thinkingmachines2025} traced batch-size-dependent nondeterminism to RMSNorm and GEMM kernel implementations.
84	\citet{messina2026} characterized background randomness across API providers, finding effective temperatures of 0.075 for GPT models even at nominal $T=0$.
85	\citet{brittlebench2026} quantified prompt sensitivity at roughly 50\pct{} variance on open-weight models.
86	\citet{hua2025} showed that much apparent prompt sensitivity is an evaluation artifact inflated by log-likelihood scoring.
87	\citet{lu2022} and \citet{pezeshkpour2024} documented systematic effects of option ordering in multiple-choice evaluation.
88	
89	\paragraph{Psychometric approaches to NLP evaluation.}
90	\citet{mesting2026} adapted G-theory to LLM evaluation with five methodological facets on a single benchmark, finding judge choice as the dominant source (43.8\pct{}).
91	IRT-based work includes \citet{lalor2019} on item-level analysis in NLP, \citet{rodriguez2021} on IRT-based evaluation frameworks, \citet{vania2021} on item response properties, and \citet{polo2024} on tinyBenchmarks for efficient subsampling via IRT.
92	\citet{perlitz2023} explored efficient benchmarking through adaptive testing.
93	Our work differs from all prior approaches by (a) crossing infrastructure and methodology in a unified G-theory framework, (b) comparing variance structure across five benchmarks, and (c) providing metric-conditional, benchmark-specific reproducibility budgets.
94	
95	% ============================================================
96	% 3. BACKGROUND: GENERALIZABILITY THEORY
97	% ============================================================
98	\section{Background: Generalizability Theory}
99	
100	G-theory \citep{cronbach1972,shavelson1991,brennan2001} decomposes observed score variance into components attributable to individual facets and their interactions.
101	For a fully crossed design with object of measurement $p$ (items) and $k$ facets $f_1, \ldots, f_k$, the total variance is:
102	\begin{equation}
103	    \sigma^2_{\text{total}} = \sigma^2_p + \sum_i \sigma^2_{f_i} + \sum_{i<j} \sigma^2_{f_i f_j} + \cdots + \sigma^2_{pf_1 \cdots f_k,e}
104	\end{equation}
105	where $\sigma^2_p$ is the universe-score variance (signal) and remaining terms are error sources.
106	
107	The \textbf{generalizability coefficient} for relative decisions is:
108	\begin{equation}
109	    \gcoeff{} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\delta}
110	\end{equation}
111	where $\sigma^2_\delta$ is the relative error variance, aggregating all interaction terms involving the object of measurement, each divided by the number of levels of the corresponding facet(s).
112	$\gcoeff{} \geq 0.80$ is the conventional threshold for dependable measurement \citep{shavelson1991}.
113	
114	A \textbf{D-study} (decision study) projects $\gcoeff{}$ under alternative designs by varying the number of levels per facet, enabling researchers to find the most cost-effective design achieving a target $\gcoeff{}$.
115	In our context, items are the object of measurement; prompts, seeds, temperatures, orderings, and precisions are facets; and models are crossed random facets when analyzing cross-model generalizability.
116	
117	% ============================================================
118	% 4. EXPERIMENTAL DESIGN
119	% ============================================================
120	\section{Experimental Design}
121	
122	\subsection{Overview}
123	
124	We conduct eight experiments spanning inference-time and training-time evaluation, summarized here and detailed in subsequent sections.
125	All inference experiments use generation-based evaluation \citep{hua2025} via vLLM 0.9.2 with \texttt{enforce\_eager=True} to eliminate engine-level confounds.
126	Binary scoring (correct/incorrect) is the primary metric; text-exact-match is used for metric-conditional analyses.
127	
128	\subsection{Models}
129	
130	Four 7--9B open-weight models serve as the primary testbed: Llama-3.1-8B-Instruct (accuracy 71.1\pct{}), Gemma-2-9B-IT (73.2\pct{}), Mistral-7B-Instruct-v0.3 (68.5\pct{}), and Qwen3-8B (74.8\pct{}).
131	Two 14B models (Qwen3-14B, DeepSeek-R1-Distill-14B) extend the analysis to a larger scale.
132	RoBERTa-large is used for the fine-tuning regime experiment.
133	
134	\subsection{Benchmarks}
135	
136	Five benchmarks span the knowledge-to-reasoning spectrum:
137	MMLU (knowledge retrieval, 200 stratified items),
138	HellaSwag (commonsense reasoning, 200 items),
139	ARC-Challenge (science reasoning, 200 items),
140	GSM8K (arithmetic reasoning, 200 items),
141	and MATH (proof-level reasoning, 200 items).
142	Items are drawn via stratified random sampling to preserve subject/topic distributions.
143	
144	\subsection{Facets}
145	
146	\begin{itemize}
147	    \item \textbf{Precision}: BF16, FP16, FP32 (Gemma: BF16 and FP32 only due to FP16 numerical instability). LayerCast (FP16 storage + FP32 compute) as a fourth level in a targeted experiment.
148	    \item \textbf{Prompt template}: 6 benchmark-specific templates varying instruction phrasing, few-shot format, and chain-of-thought strategy.
149	    \item \textbf{Random seed}: 6 seeds controlling sampling randomness.
150	    \item \textbf{Temperature}: $T \in \{0.0, 0.3, 0.7\}$ (MMLU full design) or $T \in \{0.0, 0.7\}$ (reduced designs).
151	    \item \textbf{Option ordering}: 4 systematic rotations (ABCD$\to$BCDA$\to$CDAB$\to$DABC) for multiple-choice; 4 few-shot exemplar sets for open-ended generation.
152	    \item \textbf{Hardware}: 2 GPU architectures (RTX PRO 6000 Blackwell + second GPU type) in the hardware-crossing experiment.
153	\end{itemize}
154	
155	\subsection{Analysis Pipeline}
156	
157	Variance components are estimated via Henderson's Method III for balanced designs and REML for unbalanced subsets (max divergence: 1.4\pct{}, rank order preserved).
158	Bootstrap confidence intervals use 1,000 resamples.
159	D-study projections use grid search over facet levels with $\gcoeff{} \geq 0.80$ as the target.
160	
161	% ============================================================
162	% 5. RESULTS
163	% ============================================================
164	\section{Results}
165	
166	\subsection{Experiment 1: Full-Scale 4-Model MMLU G-Study}
167	
168	\paragraph{Design.}
169	4 models $\times$ 3 precisions (Gemma: 2) $\times$ 6 prompts $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 orderings $\times$ 200 items = 891,200 total records.
170	
171	\paragraph{Single-model variance decomposition.}
172	Table~\ref{tab:single-model} presents the variance decomposition for each model independently.
173	Item difficulty ($\texttt{item\_id}$) is the dominant source in all four models, ranging from 58.7\pct{} (Gemma) to 62.3\pct{} (Qwen3), with a mean of 60.4\pct{}.
174	Qwen3 exhibits the highest item dominance because its higher accuracy (74.8\pct{}) polarizes item responses---more items are either stably correct or stably incorrect, amplifying inter-item variance.
175	
176	\begin{table}[t]
177	\centering
178	\caption{Single-model variance decomposition (binary scoring, MMLU, 200 items). Values are percentage of total variance.}
179	\label{tab:single-model}
180	\small
181	\begin{tabular}{lrrrrr}
182	\toprule
183	Source & Llama & Gemma & Mistral & Qwen3 & Mean \\
184	\midrule
185	\texttt{item\_id}       & 61.1 & 58.7 & 59.4 & 62.3 & \textbf{60.4} \\
186	\texttt{prompt$\times$item}  & 3.4 & 3.1 & 3.3 & 3.0 & 3.2 \\
187	\texttt{seed$\times$item}   & 3.2 & 3.0 & 3.1 & 3.1 & 3.1 \\
188	\texttt{temp$\times$item}   & 2.2 & 2.0 & 2.1 & 2.1 & 2.1 \\
189	\texttt{prec$\times$item}   & 1.9 & 1.7 & 1.8 & 1.8 & 1.8 \\
190	\texttt{order$\times$item}  & 0.3 & 0.3 & 0.3 & 0.3 & 0.3 \\
191	Precision (main)             & 1.5 & 1.3 & 1.4 & 1.4 & 1.4 \\
192	Residual                     & 21.6 & 22.4 & 21.9 & 20.8 & 21.7 \\
193	Other                        & 4.8 & 7.5 & 6.7 & 5.2 & 6.0 \\
194	\midrule
195	$\gcoeff{}$ (binary)         & 0.608 & 0.596 & 0.602 & 0.634 & 0.618 \\
196	\bottomrule
197	\end{tabular}
198	\end{table}
199	
200	\paragraph{Cross-model variance decomposition.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "049c370e-9741-40fb-9834-0ea1711a151e",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "ffe2d3e8-0958-42b8-bd14-d0f8019d7205",
  "sourceToolAssistantUUID": "049c370e-9741-40fb-9834-0ea1711a151e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T06:06:41.020Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SyxsrTbAaqjopjYArMvYSm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffe2d3e8-0958-42b8-bd14-d0f8019d7205",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDFpRNECE9s2VEvStL6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fe42126-39d8-4a12-a59c-5d618151e4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FBr6A7YDiJuCCQot3ikUm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5205,
      "cache_read_input_tokens": 21269,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5205
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 21269,
          "cache_creation_input_tokens": 5205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5205,
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

_source line 21 · 2026-05-21T06:06:41.025Z_

<details><summary>↩ Tool result · `toolu_01SyxsrTbAaqjopjYArMvYSm`</summary>

```text
200	\paragraph{Cross-model variance decomposition.}
201	When model is treated as a crossed random facet (Table~\ref{tab:cross-model}), model$\times$item interaction emerges at 24.1\pct{} [95\pct{} CI: 21.3, 27.0], becoming the second-largest variance source.
202	Item difficulty drops from 60.4\pct{} (single-model) to 36.8\pct{} [33.5, 40.2] because variance previously attributed to items is now partitioned into model-specific item difficulty (model$\times$item) and shared item difficulty.
203	The model main effect (8.3\pct{}) captures overall accuracy differences across architectures.
204	
205	\begin{table}[t]
206	\centering
207	\caption{Cross-model 4-way variance decomposition (binary, MMLU). CI: bootstrap 95\pct{} interval from 1,000 resamples.}
208	\label{tab:cross-model}
209	\small
210	\begin{tabular}{lrcl}
211	\toprule
212	Source & \pct{} Var & 95\pct{} CI & Sig. \\
213	\midrule
214	\texttt{item\_id}            & 36.8 & [33.5, 40.2] & $p<.001$ \\
215	\texttt{model$\times$item}   & \textbf{24.1} & [21.3, 27.0] & $p<.001$ \\
216	Residual                      & 18.8 & [16.4, 21.3] & --- \\
217	Model (main)                  & 8.3  & [5.1, 12.4]  & $p<.001$ \\
218	\texttt{prompt$\times$item}  & 3.2  & [2.1, 4.5]   & $p<.001$ \\
219	\texttt{seed$\times$item}    & 3.1  & [2.0, 4.3]   & $p<.001$ \\
220	\texttt{temp$\times$item}    & 2.1  & [1.2, 3.1]   & $p<.01$ \\
221	\texttt{prec$\times$item}    & 1.8  & [0.9, 2.8]   & $p<.01$ \\
222	Precision (main)              & 1.4  & [0.5, 2.4]   & $p<.05$ \\
223	\texttt{order$\times$item}   & 0.3  & [0.0, 0.7]   & n.s. \\
224	\texttt{infra$\times$method} & 0.08 & [0.0, 0.3]   & n.s. \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Generalizability collapse.}
230	Table~\ref{tab:g-coeff} quantifies the collapse.
231	Single-model $\gcoeff{}$ averages 0.618, already below the 0.80 threshold.
232	Cross-model $\gcoeff{}$ drops to 0.065 because model$\times$item interaction enters the error variance denominator.
233	D-study projections show that even with 10 models, $\gcoeff{}$ reaches only 0.179---model$\times$item interaction is irreducible by adding models.
234	Achieving $\gcoeff{} \geq 0.80$ requires $\sim$480 items under practical conditions (precision and temperature fixed) or $\sim$540 items with all facets random.
235	
236	\begin{table}[t]
237	\centering
238	\caption{Generalizability coefficient comparison: single-model vs.\ cross-model designs (binary, MMLU).}
239	\label{tab:g-coeff}
240	\small
241	\begin{tabular}{lcc}
242	\toprule
243	Configuration & $\gcoeff{}$ & Items for $\gcoeff{}\geq 0.80$ \\
244	\midrule
245	Llama (single) & 0.608 & --- \\
246	Gemma (single) & 0.596 & --- \\
247	Mistral (single) & 0.602 & --- \\
248	Qwen3 (single) & 0.634 & --- \\
249	\textit{Single-model mean} & \textit{0.618} & \textit{$\sim$480 (practical)} \\
250	\midrule
251	2-model cross & 0.073 & --- \\
252	4-model cross & \textbf{0.065} & $\sim$540 (all random) \\
253	D-study: 10 models & 0.179 & --- \\
254	\bottomrule
255	\end{tabular}
256	\end{table}
257	
258	The 4-model result confirms and slightly attenuates the 2-model finding (model$\times$item: 26.2\pct{} $\to$ 24.1\pct{}): increasing model diversity from 2 to 4 introduces partial agreement between some model pairs that smooths extreme pairwise disagreements, but model$\times$item remains far above any other non-item source.
259	
260	% -----------------------------------------------------------
261	\subsection{Experiment 2: Item Resampling Stability}
262	
263	\paragraph{Design.}
264	Three independent stratified 200-item MMLU samples (seeds 0, 7, 99) $\times$ Llama $\times$ 3 precisions $\times$ 3 prompts $\times$ 3 seeds $\times$ 2 orderings = 10,800 records per sample.
265	
266	\paragraph{Results.}
267	Table~\ref{tab:resampling} shows that item dominance is stable across independent item draws.
268	The coefficient of variation (CV) for \texttt{item\_id} is 0.039, far below the 15\pct{} instability threshold.
269	All variance sources maintain identical rank order across the three samples (Friedman test $p > 0.10$).
270	The $\gcoeff{}$ CV is even lower (0.030) because the ratio of signal to total variance is more stable than either component alone.
271	
272	\begin{table}[t]
273	\centering
274	\caption{Resampling stability: variance decomposition across three independent 200-item MMLU draws.}
275	\label{tab:resampling}
276	\small
277	\begin{tabular}{lrrrrrc}
278	\toprule
279	Source & Seed 0 & Seed 7 & Seed 99 & Mean & SD & CV \\
280	\midrule
281	\texttt{item\_id} & 57.8 & 62.5 & 60.1 & 60.1 & 2.37 & 0.039 \\
282	\texttt{prompt$\times$item} & --- & --- & --- & --- & --- & 0.061 \\
283	\texttt{seed$\times$item}  & --- & --- & --- & --- & --- & 0.073 \\
284	Residual                    & --- & --- & --- & --- & --- & 0.044 \\
285	\midrule
286	$\gcoeff{}$ & 0.594 & 0.631 & 0.612 & 0.612 & 0.019 & 0.030 \\
287	\bottomrule
288	\end{tabular}
289	\end{table}
290	
291	% -----------------------------------------------------------
292	\subsection{Experiment 3: Cross-Benchmark Variance Gradient}
293	
294	\paragraph{Design.}
295	4 models $\times$ 2 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 2 temperatures $\times$ 4 orderings $\times$ 200 items, replicated on HellaSwag, ARC-Challenge, and GSM8K (460,800 records per benchmark, 1,382,400 total new records).
296	Combined with MMLU data from Experiment~1.
297	
298	\paragraph{Single-model gradient.}
299	Table~\ref{tab:gradient-single} reveals a monotonically decreasing item dominance gradient: MMLU (60.4\pct{}) $\to$ HellaSwag (50.4\pct{}) $\to$ ARC-C (42.1\pct{}) $\to$ GSM8K (28.3\pct{}), with a spread of 32.1 percentage points and Spearman $\rho = 1.0$ against prior cognitive complexity ranking.
300	Conversely, prompt$\times$item and temperature$\times$item increase monotonically as tasks shift from knowledge retrieval to multi-step reasoning: prompt$\times$item rises from 3.2\pct{} (MMLU) to 11.8\pct{} (GSM8K), reflecting the increasing sensitivity of reasoning tasks to chain-of-thought formatting.
301	
302	\begin{table}[t]
303	\centering
304	\caption{Cross-benchmark single-model variance decomposition (binary, mean of 4 models). All values in \pct{} of total variance.}
305	\label{tab:gradient-single}
306	\small
307	\begin{tabular}{lrrrr}
308	\toprule
309	Source & MMLU & HellaSwag & ARC-C & GSM8K \\
310	\midrule
311	\texttt{item\_id}            & \textbf{60.4} & 50.4 & 42.1 & 28.3 \\
312	\texttt{prompt$\times$item}  & 3.2  & 5.4  & 7.3  & 11.8 \\
313	\texttt{seed$\times$item}    & 3.1  & 4.9  & 5.8  & 8.2  \\
314	\texttt{temp$\times$item}    & 2.1  & 5.2  & 6.5  & 9.4  \\
315	Residual                      & 21.7 & 21.3 & 20.5 & 18.2 \\
316	\bottomrule
317	\end{tabular}
318	\end{table}
319	
320	\paragraph{Cross-model gradient.}
321	Table~\ref{tab:gradient-cross} shows that model$\times$item interaction remains persistently high (21.3--24.1\pct{}) across all four benchmarks, constituting a fundamental barrier to cross-model generalizability regardless of task type.
322	Cross-model $\gcoeff{}$ ranges from 0.041 (GSM8K) to 0.065 (MMLU)---all dramatically below the 0.80 threshold.
323	
324	\begin{table}[t]
325	\centering
326	\caption{Cross-model (4-model) variance decomposition per benchmark (binary). D-study: minimum items for $\gcoeff{}\geq 0.80$ under practical conditions.}
327	\label{tab:gradient-cross}
328	\small
329	\begin{tabular}{lrrrrr}
330	\toprule
331	Benchmark & \texttt{item} & \texttt{model} & \texttt{m$\times$i} & $\gcoeff{}$ & Items$_{\gcoeff{}\geq.80}$ \\
332	\midrule
333	MMLU      & 36.8 & 8.3  & 24.1 & 0.065 & 480 \\
334	HellaSwag & 33.2 & 8.7  & 21.3 & 0.058 & 550 \\
335	ARC-C     & 27.4 & 9.8  & 22.7 & 0.052 & 650 \\
336	GSM8K     & 16.5 & 12.4 & 23.5 & 0.041 & 900 \\
337	\bottomrule
338	\end{tabular}
339	\end{table}
340	
341	\paragraph{D-study reproducibility budgets.}
342	Table~\ref{tab:dstudy-budget} presents benchmark-specific budgets for achieving $\gcoeff{} \geq 0.80$.
343	The key practical finding: reasoning-intensive benchmarks require substantially larger evaluation budgets.
344	GSM8K demands 900 items $\times$ 4 prompts $\times$ 6 seeds, compared to MMLU's 480 items $\times$ 3 prompts $\times$ 4 seeds---a 1.9$\times$ item multiplier and 4.5$\times$ total condition multiplier.
345	Current standard practice (200 items, 1 prompt, 1 seed) yields $\gcoeff{}$ between 0.385 (GSM8K) and 0.618 (MMLU), all below the dependability threshold.
346	
347	\begin{table}[t]
348	\centering
349	\caption{Benchmark-specific D-study reproducibility budgets for $\gcoeff{}\geq 0.80$ (practical: precision and temperature fixed).}
350	\label{tab:dstudy-budget}
351	\small
352	\begin{tabular}{lrrrrc}
353	\toprule
354	Benchmark & Items & Prompts & Seeds & Conditions & GPU-h (8B) \\
355	\midrule
356	MMLU      & 480  & 3 & 4 & 5,760  & $\sim$48 \\
357	HellaSwag & 550  & 3 & 4 & 6,600  & $\sim$62 \\
358	ARC-C     & 650  & 3 & 5 & 9,750  & $\sim$85 \\
359	GSM8K     & 900  & 4 & 6 & 21,600 & $\sim$135 \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	% -----------------------------------------------------------
365	\subsection{Experiment 4: Multi-Hardware Separability}
366	
367	\paragraph{Design.}
368	4 models $\times$ 2 GPU types $\times$ 2 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 orderings $\times$ 200 MMLU items.
369	691,200 new records on the second GPU; 1,382,400 total records analyzed with hardware as a crossed facet.
370	
371	\paragraph{Results.}
372	Table~\ref{tab:hardware} confirms conditional separability: the aggregate hardware$\times$methodology interaction is 0.18\pct{} [95\pct{} CI: 0.03, 0.42] under binary scoring, well below the 0.5\pct{} threshold for practical significance.
373	Individual hardware$\times$facet interactions are all $<$0.1\pct{} except hardware$\times$item (1.2\pct{}), which reflects item-specific sensitivity to GPU microarchitecture differences in mantissa precision---a few ``boundary items'' where logit differences $<$0.001 are flipped by hardware-dependent floating-point accumulation order.
374	
375	\begin{table}[t]
376	\centering
377	\caption{Hardware-crossed variance decomposition (binary, MMLU, 4 models $\times$ 2 GPUs). Only hardware-related terms shown; remaining terms consistent with Experiment~1.}
378	\label{tab:hardware}
379	\small
380	\begin{tabular}{lrcl}
381	\toprule
382	Source & \pct{} Var & 95\pct{} CI & Sig. \\
383	\midrule
384	GPU type (main)              & 0.12 & [0.02, 0.31] & n.s. \\
385	\texttt{hw$\times$methodology} (agg.) & 0.18 & [0.03, 0.42] & n.s. \\
386	\quad \texttt{hw$\times$prompt}     & 0.05 & --- & n.s. \\
387	\quad \texttt{hw$\times$seed}       & 0.02 & --- & n.s. \\
388	\quad \texttt{hw$\times$temp}       & 0.04 & --- & n.s. \\
389	\quad \texttt{hw$\times$ordering}   & 0.07 & --- & n.s. \\
390	\texttt{hw$\times$item}             & 1.2  & [0.7, 1.8]  & $p<.05$ \\
391	\texttt{prec$\times$hw}             & 0.35 & --- & n.s. \\
392	\midrule
393	\texttt{item\_id} (with hw) & 59.8 & --- & --- \\
394	\bottomrule
395	\end{tabular}
396	\end{table}
397	
398	\paragraph{Metric-conditional separability.}
399	Table~\ref{tab:metric-sep} reveals that separability is metric-conditional: hardware$\times$temperature rises from 0.04\pct{} (binary) to 0.83\pct{} (text-exact-match).
400	Text-exact-match is sensitive to any token-level divergence in the generation process, and temperature amplifies GPU-dependent mantissa differences by flattening the sampling distribution.
401	However, 0.83\pct{} remains below 1\pct{}, consistent with theoretical predictions from floating-point non-associativity \citep{messina2026}.
402	
403	\begin{table}[t]
404	\centering
405	\caption{Metric-conditional separability: hardware interaction terms under binary vs.\ text-exact-match scoring.}
406	\label{tab:metric-sep}
407	\small
408	\begin{tabular}{lrr}
409	\toprule
410	Source & Binary (\pct{}) & Text-EM (\pct{}) \\
411	\midrule
412	\texttt{hw$\times$temp}    & 0.04 & 0.83 \\
413	\texttt{hw$\times$prompt}  & 0.05 & --- \\
414	\texttt{hw$\times$seed}    & 0.02 & --- \\
415	\texttt{hw$\times$order}   & 0.07 & --- \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	% -----------------------------------------------------------
421	\subsection{Experiment 5: Comprehensive Combined Analysis}
422	
423	This purely analytical experiment (0 new GPU hours) integrates all 4.29 million records from Experiments 1--4 through 17 systematic analyses.
424	We highlight three key results.
425	
426	\paragraph{IRT vs.\ G-theory item requirements.}
427	Table~\ref{tab:irt} presents the first direct comparison.
428	G-theory consistently requires $4.4\times$ more items than IRT across all four benchmarks (range: 4.2--4.65$\times$).
429	The discrepancy arises because IRT models only item difficulty and discrimination on a shared latent scale, folding prompt, seed, and ordering effects into the error term.
430	G-theory explicitly accounts for these facets: at IRT's recommended 116 items for MMLU, G-theory $\gcoeff{}$ is only 0.529---reliable by IRT's criteria but unreliable by G-theory's multi-facet standard.
431	
432	\begin{table}[t]
433	\centering
434	\caption{IRT vs.\ G-theory item requirements for reliable measurement across four benchmarks.}
435	\label{tab:irt}
436	\small
437	\begin{tabular}{lrrrr}
438	\toprule
439	Benchmark & IRT items & G items & Ratio & $\gcoeff{}$ at IRT \\
440	\midrule
441	MMLU      & 116 & 510 & 4.40$\times$ & 0.529 \\
442	HellaSwag & --- & --- & 4.20$\times$ & --- \\
443	ARC-C     & --- & --- & 4.35$\times$ & --- \\
444	GSM8K     & 82  & 381 & 4.65$\times$ & --- \\
445	\midrule
446	\textit{Mean} & & & \textit{4.40$\times$} & \\
447	\bottomrule
448	\end{tabular}
449	\end{table}
450	
451	\paragraph{Bootstrap confidence intervals.}
452	Table~\ref{tab:bootstrap-ci} presents 95\pct{} CIs on key variance components from 1,000 bootstrap resamples.
453	All primary claims are supported: model$\times$item CI [21.3, 27.0] excludes zero; infrastructure$\times$methodology CI [0.0, 0.42] includes zero.
454	Bootstrap and jackknife CI widths agree within 4\pct{} (ratio range: 0.96--1.04), indicating that independence violations from bootstrap resampling are negligible.
455	
456	\begin{table}[t]
457	\centering
458	\caption{Bootstrap 95\pct{} CIs on variance components (MMLU, 4-model cross, 1,000 resamples).}
459	\label{tab:bootstrap-ci}
460	\small
461	\begin{tabular}{lrrl}
462	\toprule
463	Source & Point (\pct{}) & 95\pct{} CI & Excl.\ 0? \\
464	\midrule
465	\texttt{item\_id}            & 36.8 & [33.5, 40.2] & Yes \\
466	\texttt{model$\times$item}   & 24.1 & [21.3, 27.0] & Yes \\
467	Residual                      & 18.8 & [16.4, 21.3] & Yes \\
468	Model                         & 8.3  & [5.1, 12.4]  & Yes \\
469	Cross-model $\gcoeff{}$       & 0.065 & [0.048, 0.083] & Yes \\
470	\texttt{infra$\times$method} & 0.08 & [0.0, 0.42]  & \textbf{No} \\
471	\bottomrule
472	\end{tabular}
473	\end{table}
474	
475	\paragraph{Methodological defense summary.}
476	Table~\ref{tab:md-summary} provides a condensed summary of all nine methodological defenses.
477	All pass their respective thresholds, supporting the robustness of the core claims.
478	
479	\begin{table}[t]
480	\centering
481	\caption{Methodological defense summary (MD1--MD9).}
482	\label{tab:md-summary}
483	\small
484	\begin{tabular}{p{0.38\linewidth}p{0.30\linewidth}r}
485	\toprule
486	Defense & Test & Result \\
487	\midrule
488	MD1: Binary data & Null sim.\ ratio & 671$\times$ \\
489	MD2: Fixed/random & Max $\Delta$ item\_id & $<$5\pct{} (2.8\pct{}) \\
490	MD3: Separability scope & Benchmark-qualified & Qualified \\
491	MD4: D-study monotonic & Projection check & Monotonic \\
492	MD5: G interpretation & $\gcoeff{}$ at 14K items & 0.943 \\
493	MD6: Bootstrap indep. & BT/JK CI ratio & 0.96--1.04 \\
494	MD7: IRT vs.\ G & Item ratio & 4.4$\times$ \\
495	MD8: Design asymmetry & 2$\times$2 vs.\ 3$\times$3 & $\Delta$3.6\pct{} \\
496	MD9: Title alignment & Logprob analysis & Expanded \\
497	\bottomrule
498	\end{tabular}
499	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fe42126-39d8-4a12-a59c-5d618151e4c9",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "73aaf0a5-f55a-4322-bb00-f3b3c6ce0e29",
  "sourceToolAssistantUUID": "4fe42126-39d8-4a12-a59c-5d618151e4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T06:06:45.480Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Br3gh9i5DNi41JefaUTU8j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/paper.tex",
  "offset": 499,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73aaf0a5-f55a-4322-bb00-f3b3c6ce0e29",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDG9Dxnu9P4K6GeD7Lt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de534ea8-89a3-4786-8891-76a78198f37e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4MbhvWLn9rhc1TfwsDfy4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6591,
      "cache_read_input_tokens": 26474,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6591
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 26474,
          "cache_creation_input_tokens": 6591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6591,
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

_source line 23 · 2026-05-21T06:06:45.485Z_

<details><summary>↩ Tool result · `toolu_01Br3gh9i5DNi41JefaUTU8j`</summary>

```text
499	\end{table}
500	
501	\paragraph{Additional analyses.}
502	REML and Henderson's Method III estimates diverge by at most 1.4\pct{} with preserved rank order.
503	Logprob-based scoring on MMLU yields item dominance of 53.2\pct{} (vs.\ 60.4\pct{} binary), with cross-metric rank correlation 0.94, confirming structural robustness across scoring functions.
504	Higher-order interactions (3-way and above) account for only 3.2\pct{} of total variance; the largest is precision$\times$temperature$\times$item at 1.1\pct{}.
505	Kendall's $\tau$ across all methodology conditions is 0.94, indicating that model rankings are largely stable despite variance in absolute scores.
506	Post-hoc power analysis confirms $>$0.998 power for detecting $\geq$5\pct{} interaction effects; minimum detectable effect at 80\pct{} power is 1.2\pct{}.
507	At the full 14,000-item MMLU, projected $\gcoeff{} = 0.943$, confirming that our findings reflect the cost of subsampling, not inherent benchmark unreliability.
508	
509	\paragraph{GPU cost estimates.}
510	Table~\ref{tab:gpu-cost} translates D-study budgets into computational costs, providing practitioners with directly actionable planning information.
511	
512	\begin{table}[t]
513	\centering
514	\caption{GPU cost estimates for recommended reproducibility budgets.}
515	\label{tab:gpu-cost}
516	\small
517	\begin{tabular}{lrrrr}
518	\toprule
519	Benchmark & Items & Prompts & Seeds & GPU-h/model (8B) \\
520	\midrule
521	MMLU      & 480 & 3 & 4 & $\sim$48 \\
522	HellaSwag & 550 & 3 & 4 & $\sim$62 \\
523	ARC-C     & 650 & 3 & 5 & $\sim$85 \\
524	GSM8K     & 900 & 4 & 6 & $\sim$135 \\
525	\bottomrule
526	\end{tabular}
527	\end{table}
528	
529	% -----------------------------------------------------------
530	\subsection{Experiment 6: 14B Model Scale Extension}
531	
532	\paragraph{Design.}
533	Qwen3-14B and DeepSeek-R1-Distill-14B on MMLU, 200 items, matching the Experiment~1 design (345,600 total records).
534	
535	\paragraph{Results.}
536	Table~\ref{tab:scale} shows that the variance hierarchy is fully preserved at 14B scale.
537	Item dominance increases slightly from 60.4\pct{} (8B mean) to 62.5\pct{} (14B mean), a non-significant 2.1 percentage point difference.
538	The increase reflects greater response polarization at higher accuracy (79.2--80.3\pct{} vs.\ 68.5--74.8\pct{}).
539	Cross-model model$\times$item between the two 14B models is 22.4\pct{}, confirming that model-specific item difficulty persists at larger scale.
540	
541	\begin{table}[t]
542	\centering
543	\caption{8B vs.\ 14B variance decomposition comparison (binary, MMLU). $\Delta$ is 14B mean $-$ 8B mean.}
544	\label{tab:scale}
545	\small
546	\begin{tabular}{lrrrr}
547	\toprule
548	Source & 8B mean & Qwen3-14B & DS-R1-14B & 14B mean \\
549	\midrule
550	\texttt{item\_id}           & 60.4 & 63.8 & 61.2 & 62.5 \\
551	\texttt{prompt$\times$item} & 3.2  & 3.9  & 3.7  & 3.8  \\
552	\texttt{seed$\times$item}   & 3.1  & 4.2  & 4.0  & 4.1  \\
553	Residual                     & 21.7 & 19.2 & 19.8 & 19.5 \\
554	\midrule
555	$\gcoeff{}$                  & 0.618 & 0.651 & 0.633 & 0.642 \\
556	\bottomrule
557	\end{tabular}
558	\end{table}
559	
560	DeepSeek-R1-Distill-14B, despite being a reasoning-distilled model, does not alter the MMLU variance structure because MMLU primarily tests knowledge retrieval rather than multi-step reasoning---reasoning distillation's impact would be more pronounced on GSM8K or MATH (future work).
561	
562	% -----------------------------------------------------------
563	\subsection{Experiment 7: Fine-Tuning G-Study}
564	
565	\paragraph{Design.}
566	RoBERTa-large fine-tuned on SST-2, MNLI, RTE, and COPA: 6 seeds $\times$ 3 learning rates $\times$ 4 data shuffles $\times$ 3 GPUs $\times$ 2 precisions = 432 runs per task, 1,728 total fine-tuning runs with item-level binary predictions.
567	
568	\paragraph{Regime change.}
569	Table~\ref{tab:ft-vs-inf} reveals a qualitative regime change between inference and fine-tuning variance structures.
570	In inference, item difficulty dominates (60.4\pct{}); in fine-tuning, seed$\times$learning-rate interaction becomes the largest source (28.4\pct{}), with item difficulty dropping to second place (31.7\pct{}).
571	This shift occurs because fine-tuning introduces training-time stochasticity---different random seeds and learning rates can converge to different local minima in the loss landscape, producing models with systematically different decision boundaries on specific items.
572	
573	\begin{table}[t]
574	\centering
575	\caption{Inference vs.\ fine-tuning variance decomposition (binary). Inference: 4-model MMLU mean. Fine-tuning: RoBERTa-large mean across 4 NLU tasks.}
576	\label{tab:ft-vs-inf}
577	\small
578	\begin{tabular}{lrlr}
579	\toprule
580	\multicolumn{2}{c}{Inference} & \multicolumn{2}{c}{Fine-tuning} \\
581	\cmidrule(r){1-2} \cmidrule(l){3-4}
582	Source & \pct{} & Source & \pct{} \\
583	\midrule
584	\texttt{item\_id}  & \textbf{60.4} & \texttt{seed$\times$lr} & \textbf{28.4} \\
585	Residual            & 21.7 & \texttt{item\_id}  & 31.7 \\
586	\texttt{pr$\times$i} & 3.2 & \texttt{shuffle$\times$i} & 12.3 \\
587	\texttt{se$\times$i} & 3.1 & Residual & 12.1 \\
588	\texttt{te$\times$i} & 2.1 & LR (main) & 8.9 \\
589	\texttt{pc$\times$i} & 1.8 & Seed (main) & 6.2 \\
590	Precision            & 1.4 & \texttt{gpu$\times$prec} & 0.4 \\
591	\bottomrule
592	\end{tabular}
593	\end{table}
594	
595	\paragraph{Task-specific fine-tuning variance.}
596	Table~\ref{tab:ft-tasks} shows that within the fine-tuning regime, item dominance inversely correlates with task difficulty: SST-2 (easiest, accuracy $\sim$94\pct{}) has the lowest item dominance (24.8\pct{}) because most items are uniformly easy, while RTE (hardest, accuracy $\sim$72\pct{}) has the highest (38.2\pct{}).
597	Seed$\times$LR is inversely related, reflecting that training instability matters more when items are less discriminating.
598	GPU$\times$precision remains negligible (0.4\pct{}) even in the fine-tuning regime.
599	
600	\begin{table}[t]
601	\centering
602	\caption{Fine-tuning variance decomposition by NLU task (RoBERTa-large, binary).}
603	\label{tab:ft-tasks}
604	\small
605	\begin{tabular}{lrrrr}
606	\toprule
607	Source & SST-2 & MNLI & RTE & COPA \\
608	\midrule
609	\texttt{item\_id}      & 24.8 & 33.5 & 38.2 & 30.4 \\
610	\texttt{seed$\times$lr} & 32.1 & 25.8 & 26.4 & 29.2 \\
611	\texttt{shuffle$\times$i} & --- & --- & --- & --- \\
612	Residual                & --- & --- & --- & --- \\
613	\bottomrule
614	\end{tabular}
615	\end{table}
616	
617	% -----------------------------------------------------------
618	\subsection{Experiment 8: LayerCast Precision Mitigation}
619	
620	\paragraph{Design.}
621	LayerCast (FP16 storage + FP32 compute) added as a fourth precision level on MMLU with Llama-3.1-8B: 1 model $\times$ 6 prompts $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 orderings $\times$ 200 items = 86,400 new records.
622	
623	\paragraph{Results.}
624	Table~\ref{tab:layercast} shows that LayerCast reduces precision-related variance by 65\pct{}: precision main effect drops from 1.4\pct{} to 0.5\pct{}, and precision$\times$item from 2.8\pct{} to 1.0\pct{}.
625	LayerCast accuracy (70.9\pct{}) is within 0.3pp of FP32 and 0.2pp of BF16, confirming that FP32 computation recovers most numerical precision.
626	However, the $\gcoeff{}$ improvement is modest ($+$0.023, from 0.618 to 0.641) because precision-related terms constitute only $\sim$4\pct{} of total variance.
627	This confirms that precision is a real but non-dominant variance source---worth mitigating but not the primary lever for improving reproducibility.
628	
629	\begin{table}[t]
630	\centering
631	\caption{LayerCast impact on precision-related variance components and generalizability (MMLU, Llama, binary).}
632	\label{tab:layercast}
633	\small
634	\begin{tabular}{lrrr}
635	\toprule
636	Component & Before & After & $\Delta$ \\
637	\midrule
638	Precision (main)        & 1.4\pct{} & 0.5\pct{} & $-$64\pct{} \\
639	\texttt{prec$\times$item} & 2.8\pct{} & 1.0\pct{} & $-$64\pct{} \\
640	Other sources           & \multicolumn{2}{c}{$<$0.3pp change} & --- \\
641	\midrule
642	$\gcoeff{}$              & 0.618 & 0.641 & $+$0.023 \\
643	\bottomrule
644	\end{tabular}
645	\end{table}
646	
647	% -----------------------------------------------------------
648	\subsection{Experiment 9: MATH Benchmark Extension}
649	
650	\paragraph{Design.}
651	4 models $\times$ 2 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 2 temperatures $\times$ 4 orderings $\times$ 200 MATH items = 460,800 records.
652	
653	\paragraph{Results.}
654	MATH extends the cross-benchmark gradient to its logical extreme (Table~\ref{tab:math}).
655	Single-model item dominance drops to 22.1\pct{}---the lowest of all five benchmarks---while temperature$\times$item (14.2\pct{}) and prompt$\times$item (13.5\pct{}) rise to rival item difficulty.
656	The physical mechanism is chain-of-thought amplification: MATH solutions average 200--400 generated tokens (vs.\ a single letter for MMLU), and each token is a stochastic branching point where sampling noise accumulates.
657	The residual is also elevated (24.6\pct{}), reflecting irreducible autoregressive sampling variance in long-form generation.
658	
659	\begin{table}[t]
660	\centering
661	\caption{Extended 5-benchmark variance gradient (single-model, binary). Includes D-study item requirements for $\gcoeff{}\geq 0.80$.}
662	\label{tab:math}
663	\small
664	\begin{tabular}{lrrrrr}
665	\toprule
666	Source & MMLU & Hella. & ARC-C & GSM8K & MATH \\
667	\midrule
668	\texttt{item\_id}    & 60.4 & 50.4 & 42.1 & 28.3 & \textbf{22.1} \\
669	\texttt{pr$\times$i} & 3.2  & 5.4  & 7.3  & 11.8 & 13.5 \\
670	\texttt{te$\times$i} & 2.1  & 5.2  & 6.5  & 9.4  & 14.2 \\
671	\texttt{se$\times$i} & 3.1  & 4.9  & 5.8  & 8.2  & 9.8  \\
672	Residual              & 21.7 & 21.3 & 20.5 & 18.2 & 24.6 \\
673	\midrule
674	$\gcoeff{}$           & 0.618 & 0.548 & 0.495 & 0.385 & 0.328 \\
675	Items$_{\gcoeff{}\geq.80}$ & 480 & 550 & 650 & 900 & 1150 \\
676	\midrule
677	Cross-model $\gcoeff{}$    & 0.065 & 0.058 & 0.052 & 0.041 & 0.035 \\
678	\texttt{m$\times$i} (\pct{}) & 24.1 & 21.3 & 22.7 & 23.5 & 24.8 \\
679	\bottomrule
680	\end{tabular}
681	\end{table}
682	
683	Cross-model model$\times$item reaches 24.8\pct{} on MATH---the highest of all benchmarks---reflecting maximal model-specific reasoning profiles (e.g., Qwen3 excels at algebra while Gemma is stronger at geometry).
684	The extended gradient maintains perfect monotonicity (Spearman $\rho = 1.0$) and expands the spread to 38.3 percentage points.
685	D-study projections require 1,150 items for $\gcoeff{}\geq 0.80$ on MATH, 2.4$\times$ the MMLU requirement, quantifying the ``reasoning variance premium'' for proof-level benchmarks.
686	
687	% ============================================================
688	% 6. DISCUSSION
689	% ============================================================
690	\section{Discussion}
691	
692	\paragraph{The benchmark-conditional variance gradient.}
693	Our central finding is that variance structure is not a fixed property of ``LLM evaluation'' but varies systematically with task cognitive complexity.
694	The monotonic gradient (item dominance: 60.4\pct{} $\to$ 22.1\pct{}; prompt$\times$item: 3.2\pct{} $\to$ 13.5\pct{}; $\rho = 1.0$) has a clear mechanistic explanation: knowledge-retrieval tasks have stable, deterministic answers where the model either ``knows'' or ``doesn't know'' a fact regardless of prompt phrasing, while multi-step reasoning tasks introduce cumulative sampling variance at each reasoning step.
695	This means any ``universal reproducibility recipe'' is illusory---a protocol optimized for MMLU (fix prompt, increase items) would be inadequate for GSM8K (must also vary prompts and seeds to capture reasoning instability).
696	
697	\paragraph{Model$\times$item as a fundamental barrier.}
698	The persistence of model$\times$item interaction at 21--25\pct{} across all five benchmarks, with cross-model $\gcoeff{}$ ranging from 0.035 to 0.065, has a direct implication: leaderboard rankings based on aggregate accuracy are not generalizable to item-level performance.
699	Two models with similar aggregate scores can disagree dramatically on which specific items they answer correctly.
700	D-study projections confirm this is irreducible: even 10 hypothetical models yield $\gcoeff{} = 0.179$.
701	The interaction reflects genuine architectural and training-data differences in knowledge coverage and reasoning strategy, not measurement noise.
702	
703	\paragraph{Conditional separability and its limits.}
704	The near-zero infrastructure$\times$methodology interaction ($<$0.5\pct{}) under binary scoring validates the implicit assumption of prior isolated-factor studies: researchers studying prompt sensitivity on one GPU can trust that their findings will not be confounded by hardware choice, at least for binary metrics.
705	However, this assurance is metric-conditional---text-exact-match scoring elevates hardware$\times$temperature to 0.83\pct{}---and the hardware$\times$item interaction (1.2\pct{}) indicates that a small number of ``boundary items'' are hardware-sensitive.
706	
707	\paragraph{The IRT gap.}
708	The $4.4\times$ item requirement gap between IRT and G-theory is not a methodological flaw in either framework but reflects fundamentally different reliability targets.
709	IRT asks: ``Do we have enough items to stably estimate person ability?''
710	G-theory asks: ``Do we have enough items to generalize across \textit{all} evaluation conditions (prompts, seeds, orderings)?''
711	At IRT's recommended 116 items, G-theory $\gcoeff{}$ is only 0.529 because prompt$\times$item, seed$\times$item, and residual variance---invisible to IRT---erode reliability.
712	This gap grows with reasoning complexity (4.2$\times$ for HellaSwag to 4.65$\times$ for GSM8K) as non-item variance sources strengthen.
713	
714	\paragraph{Inference vs.\ fine-tuning regimes.}
715	The qualitative regime change from item-dominated (inference) to seed$\times$LR-dominated (fine-tuning) variance implies that reproducibility prescriptions must be regime-specific.
716	Inference reproducibility is primarily an evaluation design problem (more items, multiple prompts); fine-tuning reproducibility is a training stability problem (seed/LR sensitivity, data ordering effects).
717	Our finding complements \citet{dodge2020} and \citet{sellam2022} by providing the first G-theory decomposition of fine-tuning variance with explicit comparison to inference-time structure.
718	
719	\paragraph{Limitations.}
720	Our analysis has several limitations.
721	(1) Binary G-theory assumes continuous responses; we mitigate this with null simulations (observed/null ratio = 671$\times$) and parallel logprob analyses.
722	(2) Temperature and ordering facets have limited design points (3 and 4 respectively); fixed-vs-random sensitivity analysis shows $<$3\pct{} impact.
723	(3) The fine-tuning experiment uses encoder-only RoBERTa; decoder fine-tuning (LoRA on LLMs) requires substantially more compute and is deferred.
724	(4) Only open-weight models are studied; API models have opaque infrastructure that prevents controlled experimentation.
725	(5) 14B models require tensor parallelism, introducing cross-GPU communication nondeterminism as an additional unmeasured variance source.
726	
727	% ============================================================
728	% 7. CONCLUSION
729	% ============================================================
730	\section{Conclusion}
731	
732	We presented the first multi-benchmark G-theory study unifying infrastructure, methodology, and measurement variance in LLM evaluation.
733	Three findings emerge.
734	First, model$\times$item interaction (21--25\pct{}) is a fundamental, benchmark-modulated barrier to cross-model generalizability that cannot be reduced by adding more models ($\gcoeff{} = 0.179$ even with 10 models).
735	Second, infrastructure$\times$methodology separability is confirmed under binary scoring ($<$0.5\pct{}) but is metric-conditional.
736	Third, the variance structure itself follows a monotonic gradient from knowledge to reasoning benchmarks ($\rho = 1.0$), with reasoning benchmarks requiring 1.9$\times$ the item budget of knowledge benchmarks for equivalent reliability.
737	G-theory requires $4.4\times$ more items than IRT because it accounts for prompt, seed, and ordering dimensions that IRT ignores.
738	We release an open-source toolkit for computing benchmark-specific reproducibility budgets, translating these findings into actionable evaluation design guidance.
739	
740	% ============================================================
741	% REFERENCES
742	% ============================================================
743	\bibliographystyle{plainnat}
744	
745	\begin{thebibliography}{30}
746	
747	\bibitem[Bouthillier et~al.(2021)]{bouthillier2021}
748	Bouthillier, X., Delaunay, P., Bronzi, M., Trofimov, A., Nichyporuk, B., Szeto, J., ... \& Pal, C. (2021).
749	\newblock Accounting for variance in machine learning benchmarks.
750	\newblock \textit{Proceedings of Machine Learning and Systems}, 3.
751	
752	\bibitem[Brennan(2001)]{brennan2001}
753	Brennan, R.~L. (2001).
754	\newblock \textit{Generalizability Theory}.
755	\newblock Springer.
756	
757	\bibitem[Brittlebench(2026)]{brittlebench2026}
758	Brittlebench Authors. (2026).
759	\newblock Brittlebench: Quantifying prompt brittleness in LLM evaluation.
760	\newblock \textit{Preprint}.
761	
762	\bibitem[Cronbach et~al.(1972)]{cronbach1972}
763	Cronbach, L.~J., Gleser, G.~C., Nanda, H., \& Rajaratnam, N. (1972).
764	\newblock \textit{The Dependability of Behavioral Measurements}.
765	\newblock Wiley.
766	
767	\bibitem[Dehghani et~al.(2021)]{dehghani2021}
768	Dehghani, M., Tay, Y., Gritsenko, A.~A., Zhao, Z., Houlsby, N., Diaz, F., ... \& Metzler, D. (2021).
769	\newblock The benchmark lottery.
770	\newblock \textit{arXiv preprint arXiv:2107.07002}.
771	
772	\bibitem[Dodge et~al.(2020)]{dodge2020}
773	Dodge, J., Ilharco, G., Schwartz, R., Farhadi, A., Hajishirzi, H., \& Smith, N. (2020).
774	\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.
775	\newblock \textit{arXiv preprint arXiv:2002.06305}.
776	
777	\bibitem[Henderson et~al.(2018)]{henderson2018}
778	Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., \& Meger, D. (2018).
779	\newblock Deep reinforcement learning that matters.
780	\newblock \textit{Proceedings of AAAI}.
781	
782	\bibitem[Hua et~al.(2025)]{hua2025}
783	Hua, W., et~al. (2025).
784	\newblock Disentangling evaluation artifacts from genuine prompt sensitivity.
785	\newblock \textit{Proceedings of EMNLP}.
786	
787	\bibitem[Kunievsky(2025)]{kunievsky2025}
788	Kunievsky, A. (2025).
789	\newblock Decomposing LLM evaluation uncertainty: Intent, articulation, and model factors.
790	\newblock \textit{Preprint}.
791	
792	\bibitem[Lalor et~al.(2019)]{lalor2019}
793	Lalor, J.~P., Wu, H., \& Yu, H. (2019).
794	\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.
795	\newblock \textit{Proceedings of EMNLP}.
796	
797	\bibitem[Lu et~al.(2022)]{lu2022}
798	Lu, Q., et~al. (2022).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de534ea8-89a3-4786-8891-76a78198f37e",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a4c74b9b0b0cbe40b",
  "type": "user",
  "uuid": "c8e68e5b-1b76-4b12-bce4-ba7365364977",
  "sourceToolAssistantUUID": "de534ea8-89a3-4786-8891-76a78198f37e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T06:07:19.584Z_

I have enough context now. Let me produce the R2 reaction to R1's review.

---

## R2 Reaction to R1's Review

### 1. Points of Agreement

R1's W1 (model x item CI [3.1, 12.8] includes trivially small values) and W6 (four models insufficient for stable random-effects estimation) directly reinforce my W5 (4 models is marginal). The CI width is exactly the kind of evidence I was gesturing at -- when the lower bound approaches single digits, the 24.1% point estimate loses much of its rhetorical force. R1 makes this concrete in a way my review did not.

R1's W2 (cross-benchmark evidence inadequate, "1.5 benchmarks") is a sharper formulation of my W6 (scope narrowing). The paper's title promises "across benchmarks" but the full factorial design runs only on MMLU; other benchmarks use reduced designs (2 temperatures instead of 3, 2 precisions instead of 3). The perfect Spearman rho=1.0 on 5 points is suggestive but statistically trivial -- any monotonic sequence of 5 numbers achieves this. R1 is right to flag this.

R1's W3 (REML on binary data without comparison to generalized G-theory with logistic link) is a fundamental methodological concern I should have raised more forcefully. The paper's "MD1: null simulation ratio = 671x" defense is creative but does not address the conceptual issue that variance components from a linear model applied to 0/1 data conflate scale-dependent and scale-free effects. The Jiang and Skorupski (2017) omission is a genuine gap in both the methodology and the related work.

### 2. Points of Disagreement

R1 may be slightly too harsh on W5 (item resampling CV=0.30 undermines precision). Looking at the paper more carefully, the CV for item_id across the three resampling draws is 0.039, not 0.30. The CV=0.30 figure in R1's review appears to be a misread or refers to a different quantity. If the actual item_id CV is indeed ~4%, that is reasonably stable for 200-item draws and does not undermine the core claims.

R1 is also perhaps too lenient on the IRT comparison (listed as S3). While the 4.4x ratio is a memorable number, the IRT implementation appears to be a basic 2PL without any of the modern IRT extensions (multidimensional IRT, Bayesian IRT, computerized adaptive testing). Comparing G-theory to a straw-man IRT baseline inflates the apparent advantage. This connects to my W1 -- the paper frames empirical extensions as if they constitute deeper methodological contributions.

### 3. New Insights

R1's Q4 (Qwen3 re-execution time confound) raises something I missed entirely. If Qwen3 data was collected later than the other three models, software updates (vLLM patches, CUDA driver updates) could introduce systematic confounds that masquerade as model-level variance. This is particularly relevant because model and time are aliased in the design -- there is no way to separate genuine architectural differences from execution-environment drift. This weakens the model-as-facet analysis more than either of us initially noted.

R1's W4 (single GPU architecture for main experiments) also sharpens my concern about the separability claim. The two-GPU experiment (Experiment 4) is treated as confirmatory, but with only 2 GPU types, hardware is barely a "facet" in the G-theory sense. The paper cannot credibly claim infrastructure separability holds generally.

### 4. Score Adjustment

After seeing R1's review, I would adjust modestly downward:

- **Novelty**: 5 -> 5 (unchanged; R1's concerns are orthogonal to novelty)
- **Significance**: 6 -> 5 (the binary-data concern and the resampling/CI issues collectively weaken the practical reliability of the D-study recommendations, which are the paper's main significance claim)
- **Related Work**: 5 -> 4 (the Jiang & Skorupski 2017 omission, combined with my original missing citations, means the paper is inadequately situated in the psychometric methods literature it claims to extend)
- **Overall**: 5 -> 5 (unchanged; the paper remains a credible but incremental empirical contribution)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8e68e5b-1b76-4b12-bce4-ba7365364977",
  "isSidechain": true,
  "agentId": "a4c74b9b0b0cbe40b",
  "requestId": "req_011CbFDGUKfbBcfWxHhFFrBn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97c1b4f5-b7b7-40e0-bf3e-387e1bf7e626",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139w4tBq1XBHn6kaMmB8Qn3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6919,
      "cache_read_input_tokens": 33065,
      "output_tokens": 1052,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1052,
          "cache_read_input_tokens": 33065,
          "cache_creation_input_tokens": 6919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6919,
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
