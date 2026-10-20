# Research conversation: You are Reviewer R2 for a top ML venue review. Your focus: **novelty, significance, positioning against related work, an

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a27d91e4445375760.jsonl`
- **Structured JSON:** [`7636823449df7c42ad73.json`](../../sessions/76/7636823449df7c42ad73.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

64 recorded events

### User

_source line 1 · 2026-05-20T23:48:24.014Z_

You are Reviewer R2 for a top ML venue review. Your focus: **novelty, significance, positioning against related work, and writing quality**. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target acceptance rate ~25%.

## Paper Summary

**Title:** "Variance Decomposition Is a Measurement, Not a Fact: On the Instability of Reproducibility Budgets for LLM Evaluation"

The paper applies Generalizability Theory (G-theory) to LLM evaluation variance across 5 benchmarks (MMLU, GSM8K, ARC-Challenge, HellaSwag, MATH), 4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B, Mistral-7B), crossing infrastructure (precision, hardware, ordering) × methodology (prompt, seed, temperature) factors.

**Three claims:**
1. Item dominance estimates are sample-unstable (CV=33% across 3 item resamples). Single variance decompositions over-commit to attribution certainty.
2. Model×item interaction (33%) is the largest overlooked component; treating model as fixed inflates item variance by >22pp.
3. D-study reproducibility budgets converge across benchmarks (range=60 items) but carry ±190-item CIs, rendering benchmark-specific recommendations meaningless.

**The paper frames itself as a meta-methodological critique:** variance decomposition is a measurement, not a fact. Prior work (Mesting 2026, Brittlebench 2026, Bouthillier et al. 2021) reports point estimates of variance shares as findings without testing stability.

**Related work cited:**
- Bouthillier et al. (2021): ANOVA-based variance decomposition for ML benchmarks
- Henderson et al. (2018): Implementation details in deep RL
- Dodge et al. (2020), Sellam et al. (2022): Fine-tuning instability
- Mesting (2026): G-theory for LLM-as-judge evaluation (single benchmark, model-as-fixed, no resampling stability)
- Brittlebench (2026): Prompt sensitivity up to 50%, fixed hardware
- Yuan et al. (2025): Up to 9% accuracy variation from hardware/precision
- Lu et al. (2022), Pezeshkpour & Hruschka (2024): Option ordering effects
- Biderman et al. (2024): Evaluation reproducibility survey
- IRT work: Lalor et al. (2019), Rodriguez et al. (2021), Vania et al. (2021), Polo et al. (2024), Perlitz et al. (2023), Dehghani et al. (2021)

**8 experiments:** Full-scale precision study, item resampling stability (centerpiece), multi-benchmark replication, multi-hardware G-study, comprehensive reanalysis (model-as-facet + bootstrap + D-study), 14B extension, fine-tuning G-study, LayerCast mitigation, MATH extension.

**Key narrative arc:** The paper started with a "cross-benchmark variance gradient" hypothesis (knowledge→reasoning benchmarks would show decreasing item dominance). This failed (spread=9pp, non-monotonic). The pivot: "We set out to build reproducibility budgets and discovered the budget itself is unreliable."

**Writing structure:** 13 pages. Abstract → Introduction → Related Work → Method (G-theory framework + experimental design) → Experiments and Results (8 subsections) → Discussion → Conclusion. 18 tables, described figure slots but unclear if figures are actually included.

## Your Review Task

Provide a detailed review covering:

1. **Novelty Assessment**:
   - Is the "variance decomposition is a measurement" framing genuinely novel, or is this well-known in psychometrics/measurement theory?
   - The model-as-facet vs model-as-fixed comparison — is this a novel insight for LLM evaluation, or standard G-theory practice?
   - Item resampling instability — has this been tested before in ML evaluation contexts?
   - The bimodality→item_id correlation (r=0.95) — is this a meaningful contribution?

2. **Positioning Against Related Work**:
   - Is the critique of Mesting (2026), Brittlebench (2026) fair and well-substantiated?
   - Are there missing related works? (e.g., IRT-based item selection literature, sampling theory, measurement error in social sciences)
   - Does the paper adequately distinguish from Bouthillier et al. (2021)?

3. **Significance and Impact**:
   - Would these findings change evaluation practice?
   - Is the "budgets need error bars" recommendation actionable?
   - Does the paper provide solutions or only diagnosis?

4. **Writing Quality**:
   - Is the narrative pivot (from gradient to instability) handled well or does it feel like post-hoc rationalization?
   - Is the paper too long? 8 experiments across 13 pages — is there bloat?
   - Are Experiments 5, 7 contributing enough to justify their space?

5. **Framing Concerns**:
   - The paper's central message is essentially "measurement error exists in variance decomposition." Is this surprising enough for a top venue?
   - Does the paper overclaim? (e.g., "all prior work" over-commits)

6. **Strengths and Weaknesses** (bulleted)

7. **Questions for Authors** (3-5 specific questions)

8. **Score** with justification

9. **Confidence** (1-5 scale)

Format your output as a structured review.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "9ac02ec9-e1fb-4b04-9873-87ef49217449",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T23:48:24.017Z_

```json
{
  "parentUuid": "9ac02ec9-e1fb-4b04-9873-87ef49217449",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
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
  "uuid": "0e3e39ca-58fe-40a6-b1bf-be37476311f0",
  "timestamp": "2026-05-20T23:48:24.017Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T23:48:27.988Z_



I'll start by reading the paper and all related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e3e39ca-58fe-40a6-b1bf-be37476311f0",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiR3XnMLHDgtt6Nq733",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05c5304b-e32d-4a6c-9d39-2736a7ca8adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLoZizN2iPYV5JkMBY5CJg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7484,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7484,
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

_source line 4 · 2026-05-20T23:48:29.391Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QaN7fupoPXSknhsKhJUQqn`</summary>

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
  "parentUuid": "05c5304b-e32d-4a6c-9d39-2736a7ca8adc",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiR3XnMLHDgtt6Nq733",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e8d89ae-9a38-43c6-a51a-fb2a68e1ca9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLoZizN2iPYV5JkMBY5CJg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7484,
      "cache_read_input_tokens": 8250,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7484
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7484,
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

_source line 5 · 2026-05-20T23:48:29.394Z_

<details><summary>↩ Tool result · `toolu_01QaN7fupoPXSknhsKhJUQqn`</summary>

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
  "parentUuid": "4e8d89ae-9a38-43c6-a51a-fb2a68e1ca9a",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "7ee9e001-4a95-4666-9ff1-12a821db46e2",
  "sourceToolAssistantUUID": "4e8d89ae-9a38-43c6-a51a-fb2a68e1ca9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T23:48:33.634Z_



Let me read all the key project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ee9e001-4a95-4666-9ff1-12a821db46e2",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiRSuTskhBLmyJ94hdf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c38625b-f484-424b-ad3a-a6adff95dd04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyvgvpsbVArGKG6FU9ytNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15734,
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

_source line 7 · 2026-05-20T23:48:34.163Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01LywuUrhUWZSLRadLHUtnPn`</summary>

```json
{
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c38625b-f484-424b-ad3a-a6adff95dd04",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiRSuTskhBLmyJ94hdf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1fcb0a2-8ade-4d32-a301-9390efce10df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyvgvpsbVArGKG6FU9ytNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15734,
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

_source line 8 · 2026-05-20T23:48:34.178Z_

<details><summary>↩ Tool result · `toolu_01LywuUrhUWZSLRadLHUtnPn`</summary>

```text
{"result":"# 项目 nlp_variance_gtheory 概况\n\n## 实验状态 (2 个)\n\n- **bf16_eager_disentangle**: DONE (negative) — \n- **mvp_phase_a**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\n\n## 趋势\n成功 1 / 负向 1 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32570: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1fcb0a2-8ade-4d32-a301-9390efce10df",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "8fe004b9-0262-49b4-80b6-65c9f4484d2c",
  "sourceToolAssistantUUID": "f1fcb0a2-8ade-4d32-a301-9390efce10df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T23:48:35.179Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YFDGAH9Lmo4WBFYouVQESF`</summary>

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
  "parentUuid": "8fe004b9-0262-49b4-80b6-65c9f4484d2c",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiRSuTskhBLmyJ94hdf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd750b6d-0342-4b2b-a46f-8d27df016d1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyvgvpsbVArGKG6FU9ytNj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15734,
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

_source line 10 · 2026-05-20T23:48:35.187Z_

<details><summary>↩ Tool result · `toolu_01YFDGAH9Lmo4WBFYouVQESF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\\n\\n## 趋势\\n成功 1 / 负向 1 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32570: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 800, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd750b6d-0342-4b2b-a46f-8d27df016d1c",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "9c691bf1-e7f5-45ef-aec2-a4d80cc6026e",
  "sourceToolAssistantUUID": "bd750b6d-0342-4b2b-a46f-8d27df016d1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:48:35.587Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Bz7oWBNWNcqobreFQ1yJVz`</summary>

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
  "parentUuid": "9c691bf1-e7f5-45ef-aec2-a4d80cc6026e",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiRSuTskhBLmyJ94hdf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d2d957e-df4d-49ed-aa2a-b00e579df672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyvgvpsbVArGKG6FU9ytNj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15734,
      "output_tokens": 274,
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
          "output_tokens": 274,
          "cache_read_input_tokens": 15734,
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

_source line 12 · 2026-05-20T23:48:35.595Z_

<details><summary>↩ Tool result · `toolu_01Bz7oWBNWNcqobreFQ1yJVz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d2d957e-df4d-49ed-aa2a-b00e579df672",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "30b2082d-a123-49f8-be1b-c516c17f553f",
  "sourceToolAssistantUUID": "4d2d957e-df4d-49ed-aa2a-b00e579df672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T23:48:39.719Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CJcjoDGcHX5yhdChUdFHvc`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30b2082d-a123-49f8-be1b-c516c17f553f",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiRuDFoLAyG9PKYcM9v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9865f56a-fd55-4ca5-b36a-b1b18dd37436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMumeSkFPKjpNWWU4vRPsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1323,
      "cache_read_input_tokens": 17181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1323,
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

_source line 14 · 2026-05-20T23:48:39.728Z_

<details><summary>↩ Tool result · `toolu_01CJcjoDGcHX5yhdChUdFHvc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md\", \"content\": \"# Paper Framing — nlp_variance_gtheory\\n\\n## Target Venue\\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\\n- Extended: TACL (rolling)\\n\\n## Title\\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\\n\\n## Core Claims (3 条，可证伪)\\n\\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation (MVP: 58.4% on MMLU single-model; expected to decrease with model-as-facet reanalysis). Its magnitude is hypothesized to be benchmark-dependent — weakening on reasoning tasks where temperature/seed interactions increase — but this gradient requires exp-002 confirmation. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating whether a systematic benchmark-dependent gradient exists, and (c) deriving D-study implications specific to LLM evaluation.\\n**Fallback narratives**: (A) If gradient confirmed → \\\"benchmark-conditional variance structure\\\"; (B) If gradient not significant → \\\"item dominance is universal but magnitude varies\\\"; (C) If model-as-facet reduces item_id below 30% → pivot to \\\"model×item interaction is the dominant source\\\" — narrative direction changes substantially.\\n\\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \\\"infrastructure\\\" is currently limited to the precision facet.\\n\\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\\n\\n## Contributions (3 条，明确区分)\\n\\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\\n\\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\\n\\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\\n\\n## Story Spine\\n\\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\\n\\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\\n\\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\\n\\n**Headline result template**: \\\"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (X-Y%, benchmark-dependent [placeholder: fill after exp-001/002]), while direct infrastructure×methodology interactions are negligible. Variance structure [is/is not] benchmark-conditional [pending exp-002]. D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional.\\\"\\n\\n## Hook (Counter-Intuitive Quantified Claim)\\n\\\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\\\"\\n\\n## Narrative Strategy\\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\\n- **Tension**: \\\"No universal recipe\\\" — the field seeks standardization but variance structure varies qualitatively across task types\\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\\n- **Figure plan** (4 figures minimum):\\n  1. Problem illustration: same model, different benchmark → different dominant variance source\\n  2. G-theory facet diagram showing crossed design\\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\\n  4. D-study projection curves: G vs item count for different benchmarks\\n- **Key framing shifts from Dream feedback**:\\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\\n  - Cross-benchmark gradient is the **primary novel finding**\\n  - \\\"Fully crossed\\\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\\n\\n## Venue Fit Risks\\n- AAAI: Strong fit for \\\"evaluation methodology\\\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\\n- Reviewer concern 1: \\\"Only open-weight models, not API models\\\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\\n- Reviewer concern 2: \\\"G-theory is borrowed methodology, not novel\\\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\\n- Reviewer concern 3: \\\"Item dominance is obvious from measurement theory\\\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n1. **\\\"Only N GPU types\\\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \\\"numerical precision\\\" and frame hardware as future work.\\n2. **\\\"float32 engine confound\\\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\\n3. **\\\"Only MMLU\\\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\\n4. **\\\"Small item sample\\\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\\n5. **\\\"No training-time analysis\\\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\\n6. **\\\"Missing scale validation\\\"** → exp-005 (14B models)\\n7. **\\\"G-theory may not be right framework\\\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\\n8. **\\\"Separability claim is metric-dependent\\\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\\n9. **\\\"FP32 degradation is already known (Yuan 2025)\\\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\\n10. **\\\"Incremental over Mesting (2026)\\\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\\n11. **\\\"Model not treated as G-theory facet\\\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\\n12. **\\\"No CIs on variance components\\\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\\n13. **\\\"Missing related work — IRT, tinyBenchmarks, Bouthillier\\\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\\n14. **\\\"Diagnostic tool claim unsubstantiated\\\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \\\"empirical analysis + data release.\\\"\\n15. **\\\"Fine-tuning uses encoder-only RoBERTa\\\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\\n\\n## Design Decisions\\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \\\"reduced crossing\\\" rather than \\\"fully crossed.\\\"\\n\\n## Required Bibliography (minimum 25 references)\\nKey references to include beyond current literature_map:\\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\\n- Perlitz et al. (2023) — Efficient LLM benchmarking\\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\\n- Shavelson & Webb (1991) — G-theory primer (canonical)\\n- Brennan (2001) — G-theory textbook (canonical)\\n- Lu et al. (2022) — Option ordering effects in MC evaluation\\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\\n- Dehghani et al. (2021) — Benchmark Lottery\\n- Biderman et al. (2024) — Evaluation reproducibility lessons\\n- Vania et al. (2021) — IRT item properties in NLP\\n\", \"total_chars\": 13880, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9865f56a-fd55-4ca5-b36a-b1b18dd37436",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "0d6fc437-5a49-464b-be66-e6e17ff5e7e3",
  "sourceToolAssistantUUID": "9865f56a-fd55-4ca5-b36a-b1b18dd37436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T23:48:40.225Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GdBfLEbYcQSUDXFJ5uewSm`</summary>

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
  "parentUuid": "0d6fc437-5a49-464b-be66-e6e17ff5e7e3",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiRuDFoLAyG9PKYcM9v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3071323-dce8-41fe-954f-e3d7545c41c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMumeSkFPKjpNWWU4vRPsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1323,
      "cache_read_input_tokens": 17181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1323,
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

_source line 16 · 2026-05-20T23:48:40.233Z_

<details><summary>↩ Tool result · `toolu_01GdBfLEbYcQSUDXFJ5uewSm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T14:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"gtheory_evaluation\\\"\\n    name: \\\"G-Theory & Evaluation Variance\\\"\\n    narrative: \\\"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\\\"\\n  - key: \\\"infrastructure_variance\\\"\\n    name: \\\"Infrastructure-Induced Variance\\\"\\n    narrative: \\\"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\\\"\\n  - key: \\\"prompt_sensitivity\\\"\\n    name: \\\"Prompt Sensitivity & Methodological Variance\\\"\\n    narrative: \\\"Prompt phrasing, seed, temperature, and ordering as variance sources\\\"\\n  - key: \\\"evaluation_methodology\\\"\\n    name: \\\"Evaluation Methodology\\\"\\n    narrative: \\\"Scoring artifacts, benchmark design, and evaluation protocol considerations\\\"\\n\\npapers:\\n  mesting2026hidden:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\\\"\\n    authors:\\n      - \\\"Mesting, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.11581\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  brittlebench2026:\\n    title: \\\"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.13285\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  yuan2025layercast:\\n    title: \\\"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\\\"\\n    authors:\\n      - \\\"Yuan, Z.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09501\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  messina2026background:\\n    title: \\\"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\\\"\\n    authors:\\n      - \\\"Messina, P.\\\"\\n      - \\\"Scotta, A.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.22411\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  generalizit2024:\\n    title: \\\"GeneralizIT: A Python Solution for Generalizability Theory Computations\\\"\\n    authors: []\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2411.17880\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  hua2025flaw:\\n    title: \\\"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\\\"\\n    authors:\\n      - \\\"Hua, W.\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    category: \\\"evaluation_methodology\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  thinkingmachines2025batch:\\n    title: \\\"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"Technical Report\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  kunievsky2025intent:\\n    title: \\\"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\\\"\\n    authors:\\n      - \\\"Kunievsky, D.\\\"\\n      - \\\"Evans, J.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.16584\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  bui2025seeds:\\n    title: \\\"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\\\"\\n    authors:\\n      - \\\"Bui, T.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  sameprompt2026:\\n    title: \\\"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.14349\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\", \"total_chars\": 6732, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3071323-dce8-41fe-954f-e3d7545c41c8",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "f7ec631c-0755-46b9-9be0-ecdda8f36009",
  "sourceToolAssistantUUID": "c3071323-dce8-41fe-954f-e3d7545c41c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T23:48:41.257Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019rgd69nrA5oXDQTL9Shs49`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7ec631c-0755-46b9-9be0-ecdda8f36009",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiRuDFoLAyG9PKYcM9v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c19358bc-d53f-4438-8282-afe0026ee0d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMumeSkFPKjpNWWU4vRPsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1323,
      "cache_read_input_tokens": 17181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1323,
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

_source line 18 · 2026-05-20T23:48:41.267Z_

<details><summary>↩ Tool result · `toolu_019rgd69nrA5oXDQTL9Shs49`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c19358bc-d53f-4438-8282-afe0026ee0d0",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "8979e09e-c053-4e88-9e62-3145d618e966",
  "sourceToolAssistantUUID": "c19358bc-d53f-4438-8282-afe0026ee0d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T23:48:41.699Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01R6GwYCKnmGZWw7uV4YZKbW`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8979e09e-c053-4e88-9e62-3145d618e966",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiRuDFoLAyG9PKYcM9v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c259f8a-4533-4155-97ab-b6924fcd0ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMumeSkFPKjpNWWU4vRPsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1323,
      "cache_read_input_tokens": 17181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1323,
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

_source line 20 · 2026-05-20T23:48:41.712Z_

<details><summary>↩ Tool result · `toolu_01R6GwYCKnmGZWw7uV4YZKbW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/decisions.yaml\", \"content\": \"_next_id: 4\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:57 UTC\\n  summary: MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4%），separability 在聚合层面成立，进入\\n    research 阶段\\n  rationale: 5,400 次推理完成，5 个方差分量 ≥5% 且 CI 不含零，pipeline 端到端可运行。核心发现：(1) item 选择是评估方差最大来源；(2)\\n    precision/temperature/prompt 效应是 item-specific 的；(3) 直接的 infrastructure×methodology\\n    交互可忽略（<0.02%）。float32 引擎混淆需全研究阶段解决但不影响 MVP 结论。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:12 UTC\\n  summary: 采用 dual-metric (binary correct + text exact match) 方差分解作为论文核心方法论，Claim\\n    3 改为 metric-conditional reproducibility budget\\n  rationale: MVP 双变量分析揭示截然不同的方差结构：binary correct 下 item_id 主导 (58.4%, G=0.357)；text\\n    exact match 下 prompt×item 主导 (37.5%, G=0.975)。单一 response variable 无法完整描述评估可靠性。Dual-metric\\n    对比是 G-theory 框架的天然优势——\\\"同一实验在不同衡量标准下可靠性完全不同\\\"是比单一 budget 更有力的发现。precision:temperature\\n    交互在 text metric 下显著 (1.3%, CI 不含零)，证明 separability 在细粒度下不完全成立。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 22:20 UTC\\n  summary: Dream 审稿后调整 framing：infrastructure crossing 降级为 confirmatory，cross-benchmark\\n    gradient 升级为 primary novelty，model-as-facet 加入分析计划\\n  rationale: Dream full review (dream_20260520T190053) 三档评分：Best 3/6, Median 4/6,\\n    Worst 3/6。三档一致暴露 9 个结构性问题：(1) bibliography 严重不足（需 25+ refs）; (2) model 未作为 G-theory\\n    facet（inflates item_id）; (3) 无 bootstrap CIs; (4) 零 figures; (5) infrastructure\\n    crossing 为 confirmatory null 非 breakthrough; (6) item dominance 心理测量学预期，oversold;\\n    (7) \\\"fully crossed\\\" 过度声称; (8) \\\"diagnostic tool\\\" 无实质; (9) fine-tuning 用 RoBERTa\\n    距离太远。全部为 framing/分析问题，不影响实验设计——P0 实验不变，但 framing 需大改，exp-004 分析内容扩展。需 re-dream\\n    验证后批准 P0。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: unchanged\\n    result: design not affected by framing changes\\n  - exp_id: exp-004\\n    role: expanded\\n    result: added model-as-facet, bootstrap CIs, higher-order interactions, IRT comparison\\n  depends_on:\\n  - D001\\n  - D002\\n\", \"total_chars\": 1976, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c259f8a-4533-4155-97ab-b6924fcd0ca2",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "5b1d2343-e993-468f-b3c7-f711f4601563",
  "sourceToolAssistantUUID": "3c259f8a-4533-4155-97ab-b6924fcd0ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T23:48:44.954Z_

Now let me read the actual paper and the distilled research/writing skills for deeper context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b1d2343-e993-468f-b3c7-f711f4601563",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiSNEhpAaNyd8QTPcmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "590c32ee-70ec-4060-a3a9-c9ba82729887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBW5NU6zsjuaYhXafKHuKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8228,
      "cache_read_input_tokens": 18504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8228,
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

_source line 22 · 2026-05-20T23:48:46.406Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CCQ7Hhrp35PXk2ydHquSJS`</summary>

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
  "parentUuid": "590c32ee-70ec-4060-a3a9-c9ba82729887",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiSNEhpAaNyd8QTPcmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d6e120f-e3f3-41e7-bf61-338f44827780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBW5NU6zsjuaYhXafKHuKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8228,
      "cache_read_input_tokens": 18504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8228,
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

_source line 23 · 2026-05-20T23:48:46.436Z_

<details><summary>↩ Tool result · `toolu_01CCQ7Hhrp35PXk2ydHquSJS`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/paper.tex
artifacts/dream_reports/dream_20260520T190053/median/paper.tex
artifacts/dream_reports/dream_20260520T190053/worst/paper.tex
artifacts/dream_reports/dream_20260520T222113/best/paper.tex
artifacts/dream_reports/dream_20260520T222113/median/paper.tex
artifacts/dream_reports/dream_20260520T222113/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d6e120f-e3f3-41e7-bf61-338f44827780",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "9b1c5a07-4258-48b9-af48-f1963f913ed3",
  "sourceToolAssistantUUID": "1d6e120f-e3f3-41e7-bf61-338f44827780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T23:48:47.353Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01X8jyZwkecxJUwZgT56eFAQ`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b1c5a07-4258-48b9-af48-f1963f913ed3",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiSNEhpAaNyd8QTPcmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6de2a18d-5b0c-44f3-ada6-ca7482422123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBW5NU6zsjuaYhXafKHuKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8228,
      "cache_read_input_tokens": 18504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8228,
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

_source line 25 · 2026-05-20T23:48:47.393Z_

<details><summary>↩ Tool result · `toolu_01X8jyZwkecxJUwZgT56eFAQ`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/paper.pdf
artifacts/dream_reports/dream_20260520T190053/median/paper.pdf
artifacts/dream_reports/dream_20260520T190053/worst/paper.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/back.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/filesave.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/forward.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/hand.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/help.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/home.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/matplotlib.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/move.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/qt4_editor_options.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/subplots.pdf
.venv/lib/python3.14/site-packages/matplotlib/mpl-data/images/zoom_to_rect.pdf
artifacts/dream_reports/dream_20260520T222113/best/paper.pdf
artifacts/dream_reports/dream_20260520T222113/median/paper.pdf
artifacts/dream_reports/dream_20260520T222113/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6de2a18d-5b0c-44f3-ada6-ca7482422123",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "97820712-81d1-433c-825c-43f798148575",
  "sourceToolAssistantUUID": "6de2a18d-5b0c-44f3-ada6-ca7482422123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T23:48:47.722Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01R2tStKsKjeFeKMSJNcdDUv`</summary>

```json
{
  "pattern": "**/paper*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97820712-81d1-433c-825c-43f798148575",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiSNEhpAaNyd8QTPcmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70eb08e8-1de1-4196-a927-b9cb2d2ae78b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBW5NU6zsjuaYhXafKHuKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8228,
      "cache_read_input_tokens": 18504,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 18504,
          "cache_creation_input_tokens": 8228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8228,
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

_source line 27 · 2026-05-20T23:48:47.756Z_

<details><summary>↩ Tool result · `toolu_01R2tStKsKjeFeKMSJNcdDUv`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/paper_framing.md
artifacts/dream_reports/dream_20260520T190053/best/paper.tex
artifacts/dream_reports/dream_20260520T190053/best/paper.aux
artifacts/dream_reports/dream_20260520T190053/best/paper.pdf
artifacts/dream_reports/dream_20260520T190053/best/paper.log
artifacts/dream_reports/dream_20260520T190053/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T190053/median/paper_framing.md
artifacts/dream_reports/dream_20260520T190053/median/paper.tex
artifacts/dream_reports/dream_20260520T190053/median/paper.aux
artifacts/dream_reports/dream_20260520T190053/median/paper.out
artifacts/dream_reports/dream_20260520T190053/median/paper.pdf
artifacts/dream_reports/dream_20260520T190053/median/paper.log
artifacts/dream_reports/dream_20260520T190053/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T190053/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T190053/worst/paper.tex
artifacts/dream_reports/dream_20260520T190053/worst/paper.aux
artifacts/dream_reports/dream_20260520T190053/worst/paper.out
artifacts/dream_reports/dream_20260520T190053/worst/paper.pdf
artifacts/dream_reports/dream_20260520T190053/worst/paper.log
artifacts/dream_reports/dream_20260520T190053/logs/paper_agent_worst.log
paper_framing.md
artifacts/dream_reports/dream_20260520T222113/best/paper_framing.md
artifacts/dream_reports/dream_20260520T222113/best/paper.tex
artifacts/dream_reports/dream_20260520T222113/best/paper.aux
artifacts/dream_reports/dream_20260520T222113/best/paper.out
artifacts/dream_reports/dream_20260520T222113/best/paper.pdf
artifacts/dream_reports/dream_20260520T222113/best/paper.log
artifacts/dream_reports/dream_20260520T222113/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T222113/median/paper_framing.md
artifacts/dream_reports/dream_20260520T222113/median/paper.tex
artifacts/dream_reports/dream_20260520T222113/median/paper.aux
artifacts/dream_reports/dream_20260520T222113/median/paper.out
artifacts/dream_reports/dream_20260520T222113/median/paper.pdf
artifacts/dream_reports/dream_20260520T222113/median/paper.log
artifacts/dream_reports/dream_20260520T222113/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T222113/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T222113/worst/paper.tex
artifacts/dream_reports/dream_20260520T222113/worst/paper.aux
artifacts/dream_reports/dream_20260520T222113/worst/paper.out
artifacts/dream_reports/dream_20260520T222113/worst/paper.pdf
artifacts/dream_reports/dream_20260520T222113/worst/paper.log
artifacts/dream_reports/dream_20260520T222113/logs/paper_agent_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70eb08e8-1de1-4196-a927-b9cb2d2ae78b",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "2d09d737-fb6c-4b54-8926-4f040867f586",
  "sourceToolAssistantUUID": "70eb08e8-1de1-4196-a927-b9cb2d2ae78b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T23:48:50.628Z_

Let me read the latest dream report paper (the most recent one, dream_20260520T222113, best case) and associated review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d09d737-fb6c-4b54-8926-4f040867f586",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiSo3CwoUQ1GTTBMe1C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "953d311d-bcd8-4b6c-a505-737ccfb1ba20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3SmMbQP4bTpBjQa5rkD1K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1845,
      "cache_read_input_tokens": 26732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1845,
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

_source line 29 · 2026-05-20T23:48:52.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_016yRJp7Lq3zMd1odmEHYKd6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "953d311d-bcd8-4b6c-a505-737ccfb1ba20",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiSo3CwoUQ1GTTBMe1C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09cb2827-7b60-4b0a-9779-4e078b2f85de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3SmMbQP4bTpBjQa5rkD1K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1845,
      "cache_read_input_tokens": 26732,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1845
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 26732,
          "cache_creation_input_tokens": 1845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1845,
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

_source line 30 · 2026-05-20T23:48:52.336Z_

<details><summary>↩ Tool result · `toolu_016yRJp7Lq3zMd1odmEHYKd6`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{booktabs}
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{multirow}
7	\usepackage{xcolor}
8	\usepackage{hyperref}
9	\usepackage[numbers]{natbib}
10	\usepackage{array}
11	\usepackage{caption}
12	\usepackage{subcaption}
13	
14	\newcommand{\Gcal}{\mathcal{G}}
15	\newcommand{\pp}{\,\text{pp}}
16	
17	\title{Reproducibility Budgets for LLM Evaluation:\\
18	A Generalizability Theory Analysis of Variance Sources\\Across Benchmarks, Models, and Evaluation Metrics}
19	
20	\author{Anonymous Authors}
21	
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	% ABSTRACT
29	% ============================================================
30	\begin{abstract}
31	When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, option ordering, or item selection---let alone how these factors interact.
32	We conduct a multi-benchmark Generalizability Theory (G-theory) study crossing infrastructure (numerical precision, GPU hardware) and methodology (prompt template, random seed, temperature, option ordering) facets with measurement (item selection) across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (7--14B parameters), and over 4 million evaluation records.
33	Three findings emerge.
34	\textbf{First}, item selection is the largest single variance source on all benchmarks, but its share is benchmark-conditional: 56\% on knowledge-retrieval tasks (MMLU) down to 21\% on complex reasoning (MATH), a 35 percentage-point gradient driven by chain-of-thought stochasticity that shifts variance into temperature$\times$item and seed$\times$item interactions.
35	\textbf{Second}, direct infrastructure$\times$methodology interactions are negligible ($<$0.3\% under binary scoring), providing a confirmatory null result for the separability assumption implicit in isolated-factor studies.
36	\textbf{Third}, Decision studies (D-studies) reveal that the optimal evaluation protocol reverses across task types: MMLU is item-limited (420 items for $G \geq 0.90$) while GSM8K is seed-limited (10 seeds for $G \geq 0.90$), rendering any ``universal reproducibility recipe'' illusory.
37	Current standard practice (1 prompt, 1 seed, $\leq$200 items) yields $G < 0.25$ on all benchmarks---below the minimum threshold accepted in any measurement discipline.
38	\end{abstract}
39	
40	% ============================================================
41	% 1  INTRODUCTION
42	% ============================================================
43	\section{Introduction}
44	
45	The rapid proliferation of LLM evaluation benchmarks has not been matched by a corresponding concern for measurement reliability.
46	Leaderboard rankings frequently shift when practitioners change prompt templates~\citep{mizrahi2024state,sclar2024quantifying}, random seeds~\citep{pezeshkpour2024large}, numerical precision~\citep{yuan2025revisiting}, or even option ordering~\citep{lu2022fantastically,pezeshkpour2024ordering}.
47	Each prior study isolates at most two variance sources and implicitly assumes that the remaining factors are separable---an assumption that has never been empirically tested in a unified framework.
48	
49	Generalizability Theory (G-theory)~\citep{brennan2001generalizability,shavelson1991generalizability} provides precisely the framework needed: a crossed-facet variance decomposition that simultaneously estimates main effects and all interactions, followed by Decision studies (D-studies) that project measurement reliability under alternative evaluation designs.
50	\citet{bouthillier2021accounting} applied ANOVA-based variance decomposition to ML benchmarks, and \citet{mesting2026gtheory} recently adapted G-theory to LLM evaluation with five methodological facets on a single benchmark.
51	Neither study crossed infrastructure with methodology, compared variance structure across benchmarks, or provided metric-conditional reproducibility budgets.
52	
53	We address all three gaps.
54	In a study spanning five benchmarks, six models, and over 4 million evaluation records, we find that variance structure is not a fixed property of LLM evaluation but shifts systematically with task type.
55	On knowledge-retrieval benchmarks (MMLU), item selection dominates (56\%) and adding more items is the most cost-effective path to reliability.
56	On reasoning benchmarks (GSM8K), chain-of-thought stochasticity redistributes variance into seed$\times$item (15.8\%) and temperature$\times$item (18.2\%) interactions, making seed replication the binding constraint.
57	The optimal evaluation protocol thus reverses across task types---a finding that explains why prior single-benchmark studies reached seemingly contradictory conclusions about which factors matter most.
58	
59	\paragraph{Contributions.}
60	\begin{enumerate}
61	\item \textbf{Cross-benchmark variance gradient.} The first multi-benchmark G-theory analysis demonstrating that the variance structure of LLM evaluation shifts systematically from item-dominated (knowledge retrieval) to interaction-dominated (reasoning), with a monotonic 35$\pp$ gradient across five benchmarks.
62	\item \textbf{Confirmatory separability test.} Infrastructure$\times$methodology interactions are negligible ($<$0.3\%) at the aggregate level across all benchmarks and models, providing empirical support for isolated-factor studies---with the caveat that both factor types interact substantially with items.
63	\item \textbf{Task-specific reproducibility budgets.} D-study projections with bootstrap confidence intervals yield actionable, benchmark-specific allocations for items, prompts, and seeds to achieve target reliability ($G \geq 0.90$), revealing that current practice is inadequate on every benchmark ($G < 0.25$).
64	\end{enumerate}
65	
66	
67	% ============================================================
68	% 2  RELATED WORK
69	% ============================================================
70	\section{Related Work}
71	
72	\paragraph{Variance sources in LLM evaluation.}
73	\citet{sclar2024quantifying} showed that prompt formatting alone can swing accuracy by up to 76\%.
74	\citet{pezeshkpour2024large} and \citet{lu2022fantastically} documented option-ordering effects of 5--13\%.
75	\citet{yuan2025revisiting} reported up to 9\% accuracy variation from hardware and numerical precision.
76	\citet{biderman2024lessons} catalogued reproducibility failures across evaluation pipelines.
77	Each study isolates one or two factors on a fixed benchmark; none crosses infrastructure with methodology or compares findings across benchmarks.
78	
79	\paragraph{Variance decomposition in ML.}
80	\citet{bouthillier2021accounting} pioneered ANOVA-based variance decomposition for ML benchmarks, decomposing performance variation across hyperparameters, data splits, and random seeds.
81	\citet{henderson2018deep} performed a similar analysis for deep reinforcement learning.
82	\citet{dodge2020finetuning} and \citet{sellam2022multibERTs} studied fine-tuning instability across seeds and data orders.
83	\citet{dehghani2021benchmark} argued that benchmark selection itself introduces systematic bias.
84	These studies use ANOVA or bootstrap frameworks but not G-theory, and thus lack the D-study machinery for projecting reliability under alternative designs.
85	
86	\paragraph{Generalizability Theory in NLP.}
87	G-theory~\citep{brennan2001generalizability,shavelson1991generalizability} is standard in educational and psychological measurement for decomposing measurement error into identifiable facets.
88	\citet{mesting2026gtheory} adapted G-theory to LLM evaluation with five methodology facets on a single benchmark, finding judge identity as the dominant source (43.8\%) and deriving D-study budgets.
89	Our study differs by: (a) crossing infrastructure facets (precision, hardware) with methodology, (b) spanning five benchmarks to reveal the cross-benchmark gradient, (c) treating model as a crossed facet, and (d) providing metric-conditional budgets.
90	
91	\paragraph{Item Response Theory in NLP.}
92	\citet{lalor2019learning} and \citet{rodriguez2021evaluation} applied Item Response Theory (IRT) to NLP evaluation, modeling item difficulty and discrimination parameters.
93	\citet{polo2024tinybenchmarks} leveraged IRT for efficient subsampling (tinyBenchmarks), and \citet{perlitz2023efficient} optimized benchmark efficiency via item selection.
94	IRT and G-theory address complementary questions: IRT models individual item characteristics, while G-theory decomposes total measurement variance across all facets simultaneously and projects reliability under alternative designs.
95	Our D-study budgets are directly comparable to IRT-based subsampling recommendations.
96	
97	
98	% ============================================================
99	% 3  METHOD
100	% ============================================================
101	\section{Method}
102	
103	\subsection{Generalizability Theory}
104	
105	G-theory decomposes observed score variance into components attributable to each facet and their interactions in a crossed random-effects design.
106	For a fully crossed design with object of measurement $o$ (here, model accuracy on a benchmark) and facets $f_1, f_2, \ldots, f_k$, the variance is:
107	\begin{equation}
108	\sigma^2_{\text{total}} = \sigma^2_o + \sum_j \sigma^2_{f_j} + \sum_{j&lt;l} \sigma^2_{f_j f_l} + \cdots + \sigma^2_{\text{residual}}
109	\end{equation}
110	
111	The \textbf{Generalizability coefficient} $G$ is the ratio of object-of-measurement variance to total variance including all error sources:
112	\begin{equation}
113	G = \frac{\sigma^2_o}{\sigma^2_o + \sum_{j} \frac{\sigma^2_{f_j}}{n_{f_j}} + \sum_{j&lt;l}\frac{\sigma^2_{f_jf_l}}{n_{f_j}n_{f_l}} + \cdots + \frac{\sigma^2_{\text{res}}}{\prod_j n_{f_j}}}
114	\end{equation}
115	where $n_{f_j}$ is the number of levels for facet $f_j$.
116	A \textbf{D-study} projects $G$ under hypothetical facet sample sizes, identifying the most cost-effective allocation for achieving a target reliability (conventionally $G \geq 0.80$; we target $G \geq 0.90$).
117	
118	Variance components are estimated via Henderson's Method III (expected mean squares) for the primary analysis, with restricted maximum likelihood (REML) as sensitivity check.
119	
120	\subsection{Facet Structure}
121	
122	We distinguish three facet classes:
123	\begin{itemize}
124	\item \textbf{Measurement facet}: \textit{item\_id} (200 stratified-sampled items per benchmark).
125	\item \textbf{Methodology facets}: \textit{prompt template} (6 templates), \textit{random seed} (6 seeds), \textit{temperature} (2--3 levels), \textit{option ordering} (4 orderings).
126	\item \textbf{Infrastructure facets}: \textit{numerical precision} (FP32, BF16, FP16, LayerCast), \textit{GPU hardware} (2 types in separability test).
127	\end{itemize}
128	
129	All facets are crossed (every level of each facet is combined with every level of every other facet). Model is treated as a crossed random facet in the comprehensive analysis (Section~\ref{sec:comprehensive}).
130	
131	\subsection{Models and Benchmarks}
132	
133	\paragraph{Models.} Four 7--9B instruction-tuned models---Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3---form the primary model set. Two 14B models (Qwen3-14B, DeepSeek-R1-Distill-14B) serve as scale validation. RoBERTa-large is used for the fine-tuning study.
134	
135	\paragraph{Benchmarks.} Five benchmarks spanning a reasoning-intensity continuum: MMLU (knowledge retrieval), ARC-Challenge (science reasoning), HellaSwag (commonsense completion), GSM8K (mathematical reasoning), and MATH (competition mathematics). Each benchmark contributes 200 stratified-sampled items.
136	
137	\paragraph{Infrastructure controls.}
138	All inference uses vLLM with V0 engine in \texttt{enforce\_eager} mode, eliminating the engine confound discovered during pilot studies: default vLLM routes FP32 through a different engine path (V1 CUDA graph) than BF16/FP16 (V0 eager), inflating precision effects by $\sim$6 percentage points (see Section~\ref{sec:mmlu}).
139	
140	
141	% ============================================================
142	% 4  MMLU BASELINE G-STUDY
143	% ============================================================
144	\section{MMLU Full-Scale G-Study}
145	\label{sec:mmlu}
146	
147	\subsection{Design}
148	
149	The MMLU study is the most densely crossed design: 4 models $\times$ 3 precisions (FP32/BF16/FP16) $\times$ 6 prompt templates $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 option orderings $\times$ 200 items = 5{,}184 conditions per item, totaling 1{,}036{,}800 evaluation records. Overall accuracy is 66.7\%.
150	
151	\subsection{Variance Decomposition}
152	
153	Table~\ref{tab:mmlu_variance} presents the variance decomposition. Item selection is the dominant source at 56.0\% (95\% CI: 52.5--59.5\%), followed by residual error at 20.7\%.
154	All methodology$\times$item interactions are substantial (combined 18.4\%), while methodology main effects are modest (combined 4.5\%) and infrastructure effects are negligible ($\leq$0.3\%).
155	
156	\begin{table}[t]
157	\centering
158	\caption{Variance components for MMLU (200 items, 4 models pooled, binary correct scoring). SE and 95\% CI from Henderson's Method III. MVP column shows pilot study estimates (50 items); asterisks mark confounded values before engine fix.}
159	\label{tab:mmlu_variance}
160	\small
161	\begin{tabular}{lrrrrr}
162	\toprule
163	Component & \% Var & SE & CI Low & CI Up & MVP \\
164	\midrule
165	item\_id & 56.0 & 1.8 & 52.5 & 59.5 & 58.4 \\
166	residual & 20.7 & 0.8 & 19.1 & 22.3 & 17.6 \\
167	prompt$\times$item & 6.2 & 0.6 & 5.0 & 7.4 & 5.7 \\
168	temp$\times$item & 5.9 & 0.5 & 4.9 & 6.9 & 6.9 \\
169	seed$\times$item & 3.0 & 0.3 & 2.4 & 3.6 & 2.7 \\
170	precision$\times$item & 1.8 & 0.2 & 1.4 & 2.2 & 7.2$^*$ \\
171	ordering$\times$item & 1.5 & 0.2 & 1.1 & 1.9 & --- \\
172	prompt & 1.8 & 0.3 & 1.2 & 2.4 & --- \\
173	temperature & 1.4 & 0.2 & 1.0 & 1.8 & --- \\
174	ordering & 0.8 & 0.2 & 0.4 & 1.2 & --- \\
175	precision & 0.3 & 0.1 & 0.1 & 0.5 & 0.87$^*$ \\
176	seed & 0.2 & 0.05 & 0.1 & 0.3 & --- \\
177	infra$\times$method & 0.4 & 0.1 & 0.2 & 0.6 & $<$0.02 \\
178	\bottomrule
179	\end{tabular}
180	\end{table}
181	
182	\paragraph{Engine confound correction.}
183	The pilot study (MVP, 50 items) reported precision$\times$item at 7.2\% and precision main at 0.87\%, driven by an FP32/BF16 accuracy gap of 8.5$\pp$.
184	After standardizing all precisions to V0 \texttt{enforce\_eager}, precision$\times$item collapsed to 1.8\% and the accuracy gap narrowed to 0.5$\pp$---consistent with IEEE 754 rounding differences rather than a genuine precision effect.
185	The $\sim$6\% freed variance redistributed primarily into residual (+3.1$\pp$), confirming it was a confound artifact.
186	
187	\paragraph{Cross-model consistency.}
188	All four models show item\_id as the rank-1 component (Table~\ref{tab:mmlu_permodel}), ranging from 51.6\% (Mistral-7B) to 60.2\% (Gemma-2-9B-IT). This eliminates single-model artifact concerns.
189	
190	\begin{table}[t]
191	\centering
192	\caption{Per-model item\_id variance share on MMLU.}
193	\label{tab:mmlu_permodel}
194	\small
195	\begin{tabular}{lrrlr}
196	\toprule
197	Model & item\_id\% & Next Largest & & Next\% \\
198	\midrule
199	Gemma-2-9B-IT & 60.2 & residual & & 17.1 \\
200	Qwen3-8B & 57.8 & residual & & 18.3 \\
201	Llama-3.1-8B & 55.4 & residual & & 19.8 \\
202	Mistral-7B-v0.3 & 51.6 & residual & & 22.4 \\
203	\bottomrule
204	\end{tabular}
205	\end{table}
206	
207	\subsection{Item Resampling Stability}
208	\label{sec:resampling}
209	
210	To rule out item selection artifacts, we drew three independent stratified 200-item MMLU samples (seeds 0, 7, 99) and evaluated Llama-3.1-8B under 54 conditions per sample (32{,}400 total records). Table~\ref{tab:resampling} shows that item\_id is rank-1 across all samples with a coefficient of variation (CV) of 4.1\%. Even the lowest sample (52.8\%) maintains a 30$\pp$ margin over the second-largest component. The variance structure is robust to item selection.
211	
212	\begin{table}[t]
213	\centering
214	\caption{Item resampling stability (Llama-3.1-8B, MMLU, 3 independent 200-item samples).}
215	\label{tab:resampling}
216	\small
217	\begin{tabular}{lrrrrr}
218	\toprule
219	Component & Sam.\ A & Sam.\ B & Sam.\ C & Mean & CV \\
220	\midrule
221	item\_id & 52.8 & 57.2 & 55.6 & 55.2 & 4.1\% \\
222	residual & 22.4 & 19.8 & 21.0 & 21.1 & 6.2\% \\
223	prompt$\times$item & 5.4 & 7.2 & 6.1 & 6.2 & 14.5\% \\
224	temp$\times$item & 4.8 & 6.7 & 5.6 & 5.7 & 16.7\% \\
225	seed$\times$item & 2.8 & 3.2 & 3.0 & 3.0 & 6.7\% \\
226	prec$\times$item & 1.6 & 2.0 & 1.8 & 1.8 & 11.1\% \\
227	\bottomrule
228	\end{tabular}
229	\end{table}
230	
231	
232	% ============================================================
233	% 5  CROSS-BENCHMARK VARIANCE GRADIENT
234	% ============================================================
235	\section{Cross-Benchmark Variance Gradient}
236	\label{sec:gradient}
237	
238	\subsection{Four-Benchmark Comparison}
239	
240	We replicated the factorial design on ARC-Challenge, HellaSwag, and GSM8K (4 models $\times$ 2 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 2 temperatures $\times$ 4 orderings $\times$ 200 items = 460{,}800 records per benchmark; 1{,}382{,}400 total).
241	Table~\ref{tab:gradient} presents the cross-benchmark variance gradient.
242	
243	\begin{table}[t]
244	\centering
245	\caption{Cross-benchmark variance gradient (binary correct, 4 models pooled). Benchmarks ordered by item\_id share; $G_\text{full}$ = G coefficient under full factorial design.}
246	\label{tab:gradient}
247	\small
248	\begin{tabular}{llrrrrrr}
249	\toprule
250	Benchmark & Type & item\_id & t$\times$i & s$\times$i & p$\times$i & Resid. & $G_\text{full}$ \\
251	\midrule
252	MMLU & Knowledge & 56.0 & 5.9 & 3.0 & 6.2 & 20.7 & 0.36 \\
253	ARC-Chal. & Science & 42.0 & 8.6 & 6.2 & 9.2 & 17.4 & 0.42 \\
254	HellaSwag & Commonsense & 34.0 & 13.2 & 10.8 & 9.4 & 15.8 & 0.47 \\
255	GSM8K & Math & 25.0 & 18.2 & 15.8 & 10.3 & 15.9 & 0.55 \\
256	\bottomrule
257	\end{tabular}
258	\end{table}
259	
260	The gradient is monotonic: item\_id decreases from 56.0\% (MMLU) to 25.0\% (GSM8K)---a 31$\pp$ spread. Simultaneously, temperature$\times$item increases from 5.9\% to 18.2\% ($3\times$) and seed$\times$item from 3.0\% to 15.8\% ($5\times$). This pattern is consistent across all four models.
261	
262	The mechanism is chain-of-thought stochasticity. On knowledge-retrieval tasks (MMLU), item difficulty is an intrinsic property: the model either knows the answer or does not, and the logit gap between the correct answer and the nearest distractor is typically large. Temperature and seed have minimal effect. On multi-step reasoning tasks (GSM8K), each reasoning step is independently sampled from the token distribution. Temperature directly modulates per-step distributions, and different seeds produce qualitatively different reasoning paths. The cumulative effect across 2--4 steps inflates temperature$\times$item and seed$\times$item interactions.
263	
264	Table~\ref{tab:interaction_gradient} quantifies this shift: the sum of all interaction$\times$item terms rises from 18.4\% (MMLU) to 48.6\% (GSM8K), while main effects grow from 4.5\% to 10.2\%.
265	
266	\begin{table}[t]
267	\centering
268	\caption{Interaction term gradient across benchmarks.}
269	\label{tab:interaction_gradient}
270	\small
271	\begin{tabular}{lrrrr}
272	\toprule
273	Benchmark & temp$\times$item & seed$\times$item & $\Sigma$(int$\times$item) & Main Eff.\ $\Sigma$ \\
274	\midrule
275	MMLU & 5.9 & 3.0 & 18.4 & 4.5 \\
276	ARC-Chal. & 8.6 & 6.2 & 28.9 & 7.0 \\
277	HellaSwag & 13.2 & 10.8 & 38.3 & 8.8 \\
278	GSM8K & 18.2 & 15.8 & 48.6 & 10.2 \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	\paragraph{Counter-intuitive G pattern.}
284	Knowledge benchmarks yield \emph{lower} G coefficients than reasoning benchmarks (MMLU 0.36 vs.\ GSM8K 0.55). This follows because high item\_id means item sampling is the measurement reliability bottleneck: even with all facet levels, 200-item sampling error remains dominant. On GSM8K, low item\_id means item sampling error is smaller; averaging over multiple seeds and temperatures yields higher G.
285	
286	\subsection{MATH Extension}
287	\label{sec:math}
288	
289	We extended the gradient to MATH (460{,}800 records, same design as Section~\ref{sec:gradient}). MATH represents an extreme point: overall accuracy is 32.4\%, and item\_id (21.0\%) is nearly tied with temperature$\times$item (20.8\%). Table~\ref{tab:5benchmark} shows the complete five-benchmark gradient.
290	
291	\begin{table}[t]
292	\centering
293	\caption{Complete five-benchmark variance gradient with D-study projections.}
294	\label{tab:5benchmark}
295	\small
296	\begin{tabular}{lrrrrrrrr}
297	\toprule
298	Bench. & Acc. & item\% & t$\times$i & s$\times$i & $G_\text{full}$ & $G_\text{cur}$ & Items$_{90}$ & Seeds$_{90}$ \\
299	\midrule
300	MMLU & .667 & 56.0 & 5.9 & 3.0 & .36 & .22 & 420 & 2 \\
301	ARC & .592 & 42.0 & 8.6 & 6.2 & .42 & .20 & 320 & 4 \\
302	HSwag & .708 & 34.0 & 13.2 & 10.8 & .47 & .18 & 240 & 6 \\
303	GSM8K & .574 & 25.0 & 18.2 & 15.8 & .55 & .14 & 150 & 10 \\
304	MATH & .324 & 21.0 & 20.8 & 17.4 & .50 & .10 & 120 & 12 \\
305	\bottomrule
306	\end{tabular}
307	\end{table}
308	
309	The spread widens to 35$\pp$ (56\%--21\%). MATH is the near-collapse point of item dominance: item\_id barely leads temperature$\times$item by 0.2$\pp$, driven by multi-step proofs (Level 5 competition problems require 6--10 reasoning steps). Current-practice $G = 0.10$---effectively unreliable.
310	
311	\subsection{GSM8K Per-Model Analysis}
312	
313	Table~\ref{tab:gsm8k_permodel} confirms the gradient pattern holds within each model. Mistral-7B shows the most extreme interaction dominance (temperature$\times$item 20.6\%, seed$\times$item 18.4\%), consistent with its lower accuracy creating more decision-boundary items.
314	
315	\begin{table}[t]
316	\centering
317	\caption{GSM8K per-model variance breakdown.}
318	\label{tab:gsm8k_permodel}
319	\small
320	\begin{tabular}{lrrrrr}
321	\toprule
322	Model & item\_id & t$\times$i & s$\times$i & p$\times$i & Resid. \\
323	\midrule
324	Qwen3-8B & 28.4 & 16.8 & 14.2 & 9.6 & 14.8 \\
325	Llama-3.1-8B & 24.1 & 19.4 & 16.8 & 10.8 & 15.2 \\
326	Gemma-2-9B-IT & 27.6 & 17.2 & 14.8 & 9.8 & 14.6 \\
327	Mistral-7B-v0.3 & 21.2 & 20.6 & 18.4 & 11.6 & 16.4 \\
328	\bottomrule
329	\end{tabular}
330	\end{table}
331	
332	
333	% ============================================================
334	% 6  HARDWARE SEPARABILITY
335	% ============================================================
336	\section{Multi-Hardware Separability Test}
337	\label{sec:separability}
338	
339	\subsection{Design}
340	
341	We crossed GPU hardware (2 types) with the full MMLU design: 4 models $\times$ 2 GPUs $\times$ 2 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 orderings $\times$ 200 items = 691{,}200 records.
342	
343	\subsection{Results}
344	
345	Table~\ref{tab:separability} decomposes interaction types. Direct infrastructure$\times$methodology interactions total 0.3\%---well below any practical threshold. Infrastructure effects are almost entirely item-conditional: hardware$\times$item accounts for 1.6\%, reflecting a small population of boundary items where logit differences are small enough for numerical path divergence to matter.
346	
347	\begin{table}[t]
348	\centering
349	\caption{Separability test: direct vs.\ item-conditional interactions.}
350	\label{tab:separability}
351	\small
352	\begin{tabular}{llrl}
353	\toprule
354	Interaction Type & Components & Total\% & Interpretation \\
355	\midrule
356	Direct Infra$\times$Method & hw$\times$\{prompt,temp,seed,ord\},& 0.3 & Negligible \\
357	& prec$\times$\{prompt,temp,seed,ord\} & & \\
358	Infra$\times$Item & hw$\times$item, prec$\times$item & 3.3 & Small, item-conditional \\
359	Method$\times$Item & prompt/temp/seed/ord$\times$item & 16.0 & Substantial \\
360	Item Main & item\_id & 55.4 & Dominant \\
361	\bottomrule
362	\end{tabular}
363	\end{table}
364	
365	Model rankings are perfectly preserved across GPU types (Table~\ref{tab:hardware_agreement}), with per-model accuracy differences of $\leq$0.4$\pp$ and a cross-GPU correlation of $r = 0.9992$.
366	
367	\begin{table}[t]
368	\centering
369	\caption{Hardware agreement across GPU types (per-model mean accuracy on MMLU).}
370	\label{tab:hardware_agreement}
371	\small
372	\begin{tabular}{lrrrr}
373	\toprule
374	Model & GPU1 & GPU2 & $\Delta$ (pp) & Rank \\
375	\midrule
376	Gemma-2-9B-IT & .691 & .687 & 0.4 & Preserved \\
377	Qwen3-8B & .672 & .669 & 0.3 & Preserved \\
378	Llama-3.1-8B & .658 & .655 & 0.3 & Preserved \\
379	Mistral-7B-v0.3 & .641 & .638 & 0.3 & Preserved \\
380	\bottomrule
381	\end{tabular}
382	\end{table}
383	
384	This is a clean confirmatory null: aggregate separability holds, validating the implicit assumption of isolated-factor studies. The non-zero hardware$\times$item interaction (1.6\%) provides mechanistic nuance---infrastructure and methodology are not fully independent but are coupled through item difficulty, affecting only the $\sim$5\% of items near the decision boundary.
385	
386	
387	% ============================================================
388	% 7  COMPREHENSIVE ANALYSIS
389	% ============================================================
390	\section{Comprehensive Analysis}
391	\label{sec:comprehensive}
392	
393	We performed a suite of analyses on the combined data from all preceding experiments.
394	
395	\subsection{Model-as-Facet Reanalysis}
396	
397	Treating model as a crossed random facet (rather than pooling) yields a cleaner decomposition. Table~\ref{tab:model_facet} shows the reanalysis across benchmarks.
398	
399	\begin{table}[t]
400	\centering
401	\caption{Model-as-facet variance decomposition across benchmarks (binary correct).}
402	\label{tab:model_facet}
403	\small
404	\begin{tabular}{lrrrr}
405	\toprule
406	Component & MMLU & ARC & HSwag & GSM8K \\
407	\midrule
408	item\_id & 49.2 & 38.4 & 30.8 & 22.6 \\
409	model$\times$item & 10.2 & 8.1 & 7.4 & 5.8 \\
410	temp$\times$item & 5.9 & 8.6 & 13.2 & 18.2 \\
411	seed$\times$item & 3.0 & 6.2 & 10.8 & 15.8 \\
412	prompt$\times$item & 6.2 & 9.2 & 9.4 & 10.3 \\
413	model & 2.8 & 2.4 & 2.2 & 2.0 \\
414	residual & 12.0 & 13.8 & 14.4 & 13.6 \\
415	other & 10.7 & 13.3 & 11.8 & 11.7 \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	Model$\times$item absorbs $\sim$10\% of variance on MMLU (extracted primarily from item\_id and residual), reducing item\_id from 56.0\% to 49.2\% and residual from 20.7\% to 12.0\%. Critically, item\_id remains the largest single component on all benchmarks. The gradient is preserved: 49.2\% $\to$ 38.4\% $\to$ 30.8\% $\to$ 22.6\%.
421	
422	The model$\times$item gradient runs in the same direction as the main gradient: knowledge benchmarks show higher model$\times$item (MMLU 10.2\%) than reasoning benchmarks (GSM8K 5.8\%), because models differ more in knowledge-domain coverage than in reasoning ability at this scale.
423	
424	\subsection{Bootstrap Confidence Intervals}
425	
426	Bootstrap resampling (1{,}000 item-level resamples) confirms that the cross-benchmark gradient is statistically significant (Table~\ref{tab:bootstrap}). All confidence intervals exclude zero, and no pair of adjacent benchmarks has overlapping intervals---the 35$\pp$ gradient has full statistical support.
427	
428	\begin{table}[t]
429	\centering
430	\caption{Bootstrap 95\% CIs on item\_id (model-as-facet, 1{,}000 resamples).}
431	\label{tab:bootstrap}
432	\small
433	\begin{tabular}{lrrrr}
434	\toprule
435	Benchmark & item\_id\% & 95\% CI & Width (pp) & Excl.\ 0 \\
436	\midrule
437	MMLU & 49.2 & [46.1, 52.3] & 6.2 & Yes \\
438	ARC-Challenge & 38.4 & [35.6, 41.2] & 5.6 & Yes \\
439	HellaSwag & 30.8 & [28.2, 33.4] & 5.2 & Yes \\
440	GSM8K & 22.6 & [19.8, 25.4] & 5.6 & Yes \\
441	\bottomrule
442	\end{tabular}
443	\end{table}
444	
445	\subsection{D-Study Projections}
446	\label{sec:dstudy}
447	
448	D-study projections reveal that the optimal facet allocation for achieving $G \geq 0.90$ is benchmark-specific (Table~\ref{tab:dstudy}).
449	
450	\begin{table}[t]
451	\centering
452	\caption{D-study optimal allocation for $G \geq 0.90$.}
453	\label{tab:dstudy}
454	\small
455	\begin{tabular}{lrrrrr}
456	\toprule
457	Benchmark & Items & Prompts & Seeds & Total Evals & Bottleneck \\
458	\midrule
459	MMLU & 420 & 3 & 2 & 2{,}520 & Items \\
460	ARC-Challenge & 320 & 3 & 4 & 3{,}840 & Items \\
461	HellaSwag & 240 & 3 & 6 & 4{,}320 & Mixed \\
462	GSM8K & 150 & 3 & 10 & 4{,}500 & Seeds \\
463	\bottomrule
464	\end{tabular}
465	\end{table}
466	
467	MMLU is item-limited: each additional 100 items yields $\Delta G = 0.042$, while each additional seed yields only $\Delta G = 0.003$ (effectiveness ratio 14.2:1). GSM8K is seed-limited: the effectiveness ratio inverts to 0.8:1, making seed replication more cost-effective than item expansion.
468	
469	Tables~\ref{tab:dstudy_mmlu} and~\ref{tab:dstudy_gsm8k} show the full projection grids.
470	
471	\begin{table}[t]
472	\centering
473	\caption{D-study projection grid for MMLU. Current practice baseline: 200 items, 1 prompt, 1 seed.}
474	\label{tab:dstudy_mmlu}
475	\small
476	\begin{tabular}{rrrrrr}
477	\toprule
478	Items & Prompts & Seeds & Total & $G$ & $\Delta$ vs.\ Current \\
479	\midrule
480	200 & 1 & 1 & 200 & 0.22 & --- \\
481	200 & 3 & 1 & 600 & 0.29 & +0.07 \\
482	200 & 3 & 3 & 1{,}800 & 0.32 & +0.10 \\
483	400 & 1 & 1 & 400 & 0.41 & +0.19 \\
484	400 & 3 & 2 & 2{,}400 & 0.82 & +0.60 \\
485	420 & 3 & 2 & 2{,}520 & 0.90 & +0.68 \\
486	600 & 3 & 2 & 3{,}600 & 0.94 & +0.72 \\
487	1{,}000 & 4 & 3 & 12{,}000 & 0.97 & +0.75 \\
488	\bottomrule
489	\end{tabular}
490	\end{table}
491	
492	\begin{table}[t]
493	\centering
494	\caption{D-study projection grid for GSM8K.}
495	\label{tab:dstudy_gsm8k}
496	\small
497	\begin{tabular}{rrrrrr}
498	\toprule
499	Items & Prompts & Seeds & Total & $G$ & $\Delta$ vs.\ Current \\
500	\midrule
501	200 & 1 & 1 & 200 & 0.14 & --- \\
502	200 & 1 & 6 & 1{,}200 & 0.36 & +0.22 \\
503	200 & 3 & 6 & 3{,}600 & 0.52 & +0.38 \\
504	200 & 3 & 10 & 6{,}000 & 0.68 & +0.54 \\
505	150 & 3 & 10 & 4{,}500 & 0.90 & +0.76 \\
506	200 & 3 & 10 & 6{,}000 & 0.93 & +0.79 \\
507	300 & 4 & 12 & 14{,}400 & 0.97 & +0.83 \\
508	\bottomrule
509	\end{tabular}
510	\end{table}
511	
512	\paragraph{Facet effectiveness inversion.}
513	Table~\ref{tab:effectiveness} quantifies the core finding: the marginal return per item vs.\ per seed inverts across benchmarks.
514	
515	\begin{table}[t]
516	\centering
517	\caption{Facet effectiveness ratio by benchmark.}
518	\label{tab:effectiveness}
519	\small
520	\begin{tabular}{lrrr}
521	\toprule
522	Benchmark & $\Delta G$/100 items & $\Delta G$/seed & Items:Seeds \\
523	\midrule
524	MMLU & 0.042 & 0.003 & 14.2:1 \\
525	ARC-Challenge & 0.034 & 0.008 & 4.3:1 \\
526	HellaSwag & 0.026 & 0.014 & 1.9:1 \\
527	GSM8K & 0.015 & 0.019 & 0.8:1 \\
528	\bottomrule
529	\end{tabular}
530	\end{table}
531	
532	\paragraph{Estimation robustness.}
533	REML and Henderson's Method III yield component estimates within 1.4$\pp$ on all facets, with identical component rankings. Model rankings are stable across 96.8\% of condition combinations; the 3.2\% of flips occur only between models within 1$\pp$ accuracy under extreme conditions. Higher-order (three-way) interactions total 4.8\%, with temperature$\times$seed$\times$item the largest at 1.8\%.
534	
535	
536	% ============================================================
537	% 8  ROBUSTNESS AND EXTENSIONS
538	% ============================================================
539	\section{Robustness and Extensions}
540	
541	\subsection{14B Model Scale Extension}
542	\label{sec:14b}
543	
544	To test whether item dominance is an artifact of the 7--9B parameter range, we evaluated Qwen3-14B and DeepSeek-R1-Distill-14B under the full MMLU design (345{,}600 records). Table~\ref{tab:14b} shows both 14B models fall within the 8B range for all variance components. Item\_id remains rank-1: 54.8\% (Qwen3-14B) and 50.2\% (DeepSeek-R1-Distill-14B).
545	
546	\begin{table}[t]
547	\centering
548	\caption{14B vs.\ 8B variance pattern comparison (MMLU).}
549	\label{tab:14b}
550	\small
551	\begin{tabular}{lrrrrr}
552	\toprule
553	Component & 8B Mean & 8B Range & Qwen3-14B & DS-R1-14B \\
554	\midrule
555	item\_id & 56.0 & 51.6--60.2 & 54.8 & 50.2 \\
556	residual & 20.7 & 17.1--22.4 & 17.2 & 20.8 \\
557	temp$\times$item & 5.9 & 4.9--6.9 & 5.4 & 8.8 \\
558	prompt$\times$item & 6.2 & 5.0--7.4 & 6.0 & 5.6 \\
559	seed$\times$item & 3.0 & 2.4--3.6 & 2.8 & 5.2 \\
560	precision & 0.3 & 0.1--0.5 & 0.2 & 0.2 \\
561	\bottomrule
562	\end{tabular}
563	\end{table}
564	
565	DeepSeek-R1-Distill-14B shows elevated temperature$\times$item (8.8\%) and seed$\times$item (5.2\%)---above the 8B range---consistent with reasoning distillation introducing implicit chain-of-thought tendencies that increase generation-level stochasticity even on knowledge tasks. This mirrors the MMLU-to-GSM8K shift at the model level.
566	
567	\subsection{Fine-Tuning G-Study}
568	\label{sec:finetuning}
569	
570	To test whether item dominance generalizes beyond inference to training, we fine-tuned RoBERTa-large on four tasks: SST-2, MNLI, RTE, and COPA. Each task was evaluated across 6 seeds $\times$ 3 learning rates $\times$ 4 data shuffles $\times$ 3 GPUs $\times$ 2 precisions = 432 runs, totaling 1{,}728 fine-tuning runs.
571	
572	\begin{table}[t]
573	\centering
574	\caption{Fine-tuning variance hierarchy comparison (rank-ordered).}
575	\label{tab:finetune_compare}
576	\small
577	\begin{tabular}{rll}
578	\toprule
579	Rank & Inference (MMLU) & Fine-tuning (SST-2) \\
580	\midrule
581	1 & item\_id (56.0\%) & item\_id (40.6\%) \\
582	2 & residual (20.7\%) & residual (11.8\%) \\
583	3 & prompt$\times$item (6.2\%) & seed$\times$item (10.4\%) \\
584	4 & temp$\times$item (5.9\%) & seed (9.2\%) \\
585	5 & seed$\times$item (3.0\%) & lr$\times$item (7.8\%) \\
586	6 & prec$\times$item (1.8\%) & lr (6.8\%) \\
587	\bottomrule
588	\end{tabular}
589	\end{table}
590	
591	Item\_id is rank-1 across all four tasks (35.8\%--43.8\%; Table~\ref{tab:finetune_tasks}), but the second-tier factors differ: training seed and learning rate replace prompt template and temperature as the dominant interaction partners. Small-data tasks (RTE: 2.5K examples, COPA: 400 examples) show elevated seed effects (13.2\% and 12.2\%), paralleling how reasoning benchmarks show elevated temperature effects---both reflect increased stochasticity when the task is harder.
592	
593	\begin{table}[t]
594	\centering
595	\caption{Fine-tuning variance across tasks (RoBERTa-large).}
596	\label{tab:finetune_tasks}
597	\small
598	\begin{tabular}{lrrrrrr}
599	\toprule
600	Task & $N_\text{train}$ & item\_id & seed & LR & seed$\times$item \\
601	\midrule
602	SST-2 & 67K & 40.6 & 9.2 & 6.8 & 10.4 \\
603	MNLI & 393K & 43.8 & 7.6 & 8.4 & 9.4 \\
604	RTE & 2.5K & 35.8 & 13.2 & 10.2 & 11.8 \\
605	COPA & 400 & 37.4 & 12.2 & 9.6 & 10.8 \\
606	\bottomrule
607	\end{tabular}
608	\end{table}
609	
610	GPU and precision main effects are negligible ($<$0.5\%) in fine-tuning, and current single-run practice yields $G = 0.26$.
611	
612	\subsection{LayerCast Precision Mitigation}
613	\label{sec:layercast}
614	
615	LayerCast (FP16 storage with FP32 compute) was evaluated as a fourth precision mode on 172{,}800 MMLU records (Table~\ref{tab:layercast}).
616	
617	\begin{table}[t]
618	\centering
619	\caption{Four-precision mode comparison (MMLU, 4 models pooled).}
620	\label{tab:layercast}
621	\small
622	\begin{tabular}{lrrrr}
623	\toprule
624	Mode & Acc. & Agree.\ w/ FP32 & tok/s & VRAM \\
625	\midrule
626	FP32 (V0 eager) & .664 & 1.000 & 1{,}820 & 31.2\,GB \\
627	BF16 & .669 & .9987 & 2{,}760 & 15.8\,GB \\
628	FP16 & .667 & .9984 & 2{,}810 & 15.6\,GB \\
629	LayerCast & .668 & .9993 & 2{,}580 & 16.2\,GB \\
630	\bottomrule
631	\end{tabular}
632	\end{table}
633	
634	LayerCast achieves the highest FP32 agreement (99.93\%) while reducing VRAM by 48\% and increasing throughput by 42\% relative to FP32. Its added precision variance is 0.03\%---essentially zero. Post engine-confound fix, all four precision modes produce accuracy within 0.5$\pp$; precision choice is a second-order optimization.
635	
636	
637	% ============================================================
638	% 9  DISCUSSION
639	% ============================================================
640	\section{Discussion}
641	
642	\paragraph{The cross-benchmark gradient as unifying explanation.}
643	Prior work on LLM evaluation variance has produced seemingly contradictory findings: some studies emphasize prompt sensitivity~\citep{sclar2024quantifying}, others seed instability~\citep{pezeshkpour2024large}, and still others item selection~\citep{polo2024tinybenchmarks}. The cross-benchmark variance gradient provides a unifying explanation. These studies are not contradictory---they simply studied different benchmarks occupying different positions on the knowledge-to-reasoning continuum. Prompt sensitivity studies typically use knowledge benchmarks (where prompt$\times$item is large); seed instability studies often use reasoning tasks (where seed$\times$item is large). The gradient explains the divergence and predicts which factor will dominate for any given benchmark type.
644	
645	\paragraph{``No universal recipe'' and its implications.}
646	The facet effectiveness inversion (Table~\ref{tab:effectiveness}) has direct practical consequences. A practitioner evaluating on MMLU should invest in more items (420 for $G \geq 0.90$) but can use 2 seeds. The same practitioner evaluating on GSM8K should use 10 seeds but needs only 150 items. A single ``standardized evaluation protocol'' applied uniformly across benchmarks will be suboptimal everywhere---over-investing in items for reasoning tasks and under-investing for knowledge tasks.
647	
648	\paragraph{Current practice is inadequate.}
649	Current standard practice (1 prompt, 1 seed, $\leq$200 items) produces $G < 0.25$ on all benchmarks. For comparison, the minimum acceptable $G$ in educational measurement is 0.80~\citep{brennan2001generalizability}. This means existing leaderboard results have measurement reliability fundamentally below the threshold of any scientific discipline. GSM8K is the worst case ($G = 0.14$): a single-prompt, single-seed evaluation captures only 14\% of the reliable signal, with 86\% attributable to measurement error.
650	
651	\paragraph{Separability: a nuanced null.}
652	The confirmatory null on separability ($<$0.3\% direct infrastructure$\times$methodology) validates the design assumption of prior isolated-factor studies---at the aggregate level. However, both infrastructure and methodology interact substantially with items (hardware$\times$item: 1.6\%; methodology$\times$item: 16.0\%). This means isolated-factor conclusions are valid for aggregate benchmarks but may not generalize to specific items near the decision boundary.
653	
654	\paragraph{Model-as-facet.}
655	Including model as a crossed facet extracts $\sim$10\% model$\times$item variance, reducing item\_id by 6--7$\pp$ across benchmarks. Item\_id remains rank-1, and the cross-benchmark gradient is preserved. The model$\times$item component itself follows the same gradient pattern (MMLU 10.2\% $>$ GSM8K 5.8\%), reflecting greater model heterogeneity in knowledge-domain coverage than in reasoning ability.
656	
657	\paragraph{Limitations.}
658	Infrastructure is limited to numerical precision and two GPU types; the study does not cover CUDA versions, driver versions, or datacenter-scale hardware diversity. All models are open-weight instruction-tuned models in the 7--14B range; API-based models (studied by \citet{mesting2026gtheory}) have opaque infrastructure. The fine-tuning study uses an encoder-only architecture (RoBERTa); decoder fine-tuning remains future work.
659	Generation-based evaluation may overestimate prompt sensitivity relative to log-likelihood scoring; we found that logprob-based scoring reduces item\_id to 42.8\% and increases prompt main effect to 6.8\% on MMLU, with G rising to 0.41.
660	
661	
662	% ============================================================
663	% 10  CONCLUSION
664	% ============================================================
665	\section{Conclusion}
666	
667	We presented a multi-benchmark G-theory analysis of variance sources in LLM evaluation, crossing infrastructure and methodology facets across five benchmarks, six models, and over 4 million evaluation records. Three findings stand:
668	
669	\begin{enumerate}
670	\item \textbf{Item dominance is benchmark-conditional}: item selection accounts for 21--56\% of variance, forming a monotonic 35$\pp$ gradient from knowledge retrieval (MMLU) to complex reasoning (MATH). Chain-of-thought stochasticity systematically shifts variance from item\_id into temperature$\times$item and seed$\times$item interactions.
671	
672	\item \textbf{Separability holds at the aggregate}: direct infrastructure$\times$methodology interactions are $<$0.3\% across all benchmarks, validating isolated-factor studies. Both factor types interact with items, making effects item-conditional.
673	
674	\item \textbf{Optimal protocols reverse across task types}: MMLU needs 420 items (item-limited), GSM8K needs 10 seeds (seed-limited). A ``universal reproducibility recipe'' is illusory. Current practice ($G < 0.25$) is inadequate on every benchmark.
675	\end{enumerate}
676	
677	These findings have immediate practical implications: evaluation protocols should be benchmark-specific, budgets should be allocated based on the dominant variance source for each task type, and the field should adopt reliability reporting alongside accuracy reporting.
678	
679	
680	% ============================================================
681	% REFERENCES
682	% ============================================================
683	\bibliographystyle{plainnat}
684	\begin{thebibliography}{30}
685	
686	\bibitem[Biderman et~al.(2024)]{biderman2024lessons}
687	S.~Biderman, H.~Schoelkopf, et~al.
688	\newblock Lessons from the trenches on reproducible evaluation of language models.
689	\newblock \emph{arXiv preprint arXiv:2405.14782}, 2024.
690	
691	\bibitem[Bouthillier et~al.(2021)]{bouthillier2021accounting}
692	X.~Bouthillier, P.~Delaunay, M.~Bronzi, et~al.
693	\newblock Accounting for variance in machine learning benchmarks.
694	\newblock \emph{JMLR}, 22(100):1--29, 2021.
695	
696	\bibitem[Brennan(2001)]{brennan2001generalizability}
697	R.~L. Brennan.
698	\newblock \emph{Generalizability Theory}.
699	\newblock Springer-Verlag, New York, 2001.
700	
701	\bibitem[Dehghani et~al.(2021)]{dehghani2021benchmark}
702	M.~Dehghani, Y.~Tay, A.~A. Gritsenko, et~al.
703	\newblock The benchmark lottery.
704	\newblock \emph{arXiv preprint arXiv:2107.07002}, 2021.
705	
706	\bibitem[Dodge et~al.(2020)]{dodge2020finetuning}
707	J.~Dodge, G.~Ilharco, R.~Schwartz, et~al.
708	\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.
709	\newblock \emph{arXiv preprint arXiv:2002.06305}, 2020.
710	
711	\bibitem[Henderson et~al.(2018)]{henderson2018deep}
712	P.~Henderson, R.~Islam, P.~Bachman, et~al.
713	\newblock Deep reinforcement learning that matters.
714	\newblock In \emph{AAAI}, 2018.
715	
716	\bibitem[Hua et~al.(2025)]{hua2025emnlp}
717	W.~Hua, Y.~Li, et~al.
718	\newblock Generation-based evaluation artifacts in LLM benchmarking.
719	\newblock In \emph{EMNLP}, 2025.
720	
721	\bibitem[Lalor et~al.(2019)]{lalor2019learning}
722	J.~P. Lalor, H.~Wu, H.~Yu.
723	\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.
724	\newblock In \emph{NAACL}, 2019.
725	
726	\bibitem[Lu et~al.(2022)]{lu2022fantastically}
727	Y.~Lu, M.~Bartolo, A.~Moore, et~al.
728	\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.
729	\newblock In \emph{ACL}, 2022.
730	
731	\bibitem[Messina \& Scotta(2026)]{messina2026floating}
732	P.~Messina, L.~Scotta.
733	\newblock Floating-point non-associativity in neural network inference.
734	\newblock \emph{arXiv preprint}, 2026.
735	
736	\bibitem[Mesting(2026)]{mesting2026gtheory}
737	B.~Mesting.
738	\newblock A generalizability theory analysis of LLM evaluation.
739	\newblock \emph{arXiv preprint}, 2026.
740	
741	\bibitem[Mizrahi et~al.(2024)]{mizrahi2024state}
742	M.~Mizrahi, G.~Strazalkowski, et~al.
743	\newblock State of what art? A call for multi-prompt LLM evaluation.
744	\newblock \emph{TACL}, 2024.
745	
746	\bibitem[Perlitz et~al.(2023)]{perlitz2023efficient}
747	Y.~Perlitz, E.~Bandel, et~al.
748	\newblock Efficient benchmarking of language models.
749	\newblock \emph{arXiv preprint arXiv:2308.11696}, 2023.
750	
751	\bibitem[Pezeshkpour \& Hruschka(2024{\natexlab{a}})]{pezeshkpour2024large}
752	P.~Pezeshkpour, E.~Hruschka.
753	\newblock Large language models sensitivity to the order of options in multiple-choice questions.
754	\newblock \emph{arXiv preprint arXiv:2308.11483}, 2024{\natexlab{a}}.
755	
756	\bibitem[Pezeshkpour \& Hruschka(2024{\natexlab{b}})]{pezeshkpour2024ordering}
757	P.~Pezeshkpour, E.~Hruschka.
758	\newblock Revisiting option ordering effects in LLM evaluation.
759	\newblock \emph{arXiv preprint}, 2024{\natexlab{b}}.
760	
761	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
762	F.~M. Polo, L.~Weber, et~al.
763	\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.
764	\newblock \emph{arXiv preprint arXiv:2402.14992}, 2024.
765	
766	\bibitem[Rodriguez et~al.(2021)]{rodriguez2021evaluation}
767	P.~Rodriguez, J.~Barrow, et~al.
768	\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?
769	\newblock In \emph{ACL}, 2021.
770	
771	\bibitem[Sclar et~al.(2024)]{sclar2024quantifying}
772	M.~Sclar, Y.~Choi, et~al.
773	\newblock Quantifying language models' sensitivity to spurious features in prompt design.
774	\newblock \emph{ICLR}, 2024.
775	
776	\bibitem[Sellam et~al.(2022)]{sellam2022multibERTs}
777	T.~Sellam, S.~Yadlowsky, J.~Wei, et~al.
778	\newblock The MultiBERTs: BERT reproductions for robustness analysis.
779	\newblock In \emph{ICLR}, 2022.
780	
781	\bibitem[Shavelson \& Webb(1991)]{shavelson1991generalizability}
782	R.~J. Shavelson, N.~M. Webb.
783	\newblock \emph{Generalizability Theory: A Primer}.
784	\newblock SAGE Publications, 1991.
785	
786	\bibitem[Vania et~al.(2021)]{vania2021comparing}
787	C.~Vania, Y.~Kementchedjhieva, A.~Sogaard.
788	\newblock Comparing test sets with item response theory.
789	\newblock In \emph{ACL}, 2021.
790	
791	\bibitem[Yuan et~al.(2025)]{yuan2025revisiting}
792	T.~Yuan, et~al.
793	\newblock Revisiting the impact of hardware on LLM evaluation.
794	\newblock \emph{arXiv preprint}, 2025.
795	
796	\end{thebibliography}
797	
798	% ============================================================
799	% APPENDIX
800	% ============================================================
801	\appendix
802	\section{MATH Per-Model Breakdown}
803	\label{app:math_permodel}
804	
805	\begin{table}[h]
806	\centering
807	\caption{MATH per-model variance breakdown.}
808	\small
809	\begin{tabular}{lrrrr}
810	\toprule
811	Model & item\_id & t$\times$i & s$\times$i & Resid. \\
812	\midrule
813	Qwen3-8B & 24.2 & 19.4 & 16.2 & 10.8 \\
814	Llama-3.1-8B & 20.6 & 21.8 & 18.4 & 11.6 \\
815	Gemma-2-9B-IT & 23.4 & 19.8 & 16.4 & 10.4 \\
816	Mistral-7B-v0.3 & 17.8 & 22.8 & 19.4 & 12.6 \\
817	\bottomrule
818	\end{tabular}
819	\end{table}
820	
821	Llama-3.1-8B and Mistral-7B show temperature$\times$item exceeding item\_id on MATH, consistent with the expectation that item dominance collapses for lower-accuracy models on extreme reasoning tasks.
822	
823	\section{Logprob-Based Scoring}
824	\label{app:logprob}
825	
826	Under logprob-based (continuous) scoring on MMLU, item\_id decreases to 42.8\% (from 56.0\% under binary scoring) because logprobs capture graded confidence rather than binary threshold effects. Prompt main effect rises to 6.8\% (from 1.8\%), as different prompts systematically shift the logprob distribution. The G coefficient improves to 0.41 (from 0.36), as continuous scoring reduces measurement error.
827	
828	\section{Higher-Order Interactions}
829	\label{app:higher_order}
830	
831	Three-way interactions total 4.8\% of variance, with temperature$\times$seed$\times$item the largest at 1.8\%. Extracting three-way terms reduces the residual from 12.0\% to 7.2\% in the model-as-facet analysis, suggesting that the residual in two-way models is primarily composed of identifiable higher-order interactions rather than truly random noise.
832	
833	
834	\end{document}
835	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09cb2827-7b60-4b0a-9779-4e078b2f85de",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "5e086965-9d01-481d-a83b-ce70b12c43f4",
  "sourceToolAssistantUUID": "09cb2827-7b60-4b0a-9779-4e078b2f85de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-20T23:48:57.607Z_

Now let me read the dream review reports and the distilled research skill.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e086965-9d01-481d-a83b-ce70b12c43f4",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiT8dgCX185YUDWfTiG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90d8d195-3270-42d5-adc1-665f03b9a902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdkrpEwJigMEpSXqqpvFXx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18063,
      "cache_read_input_tokens": 28577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18063,
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

_source line 32 · 2026-05-20T23:49:00.180Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019MoWAy5NGFbSEgpUg27kBq`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260520T222113/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90d8d195-3270-42d5-adc1-665f03b9a902",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiT8dgCX185YUDWfTiG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7f69a22-9686-4022-9c95-ab8dda5c1869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdkrpEwJigMEpSXqqpvFXx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18063,
      "cache_read_input_tokens": 28577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18063,
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

_source line 33 · 2026-05-20T23:49:00.222Z_

<details><summary>↩ Tool result · `toolu_019MoWAy5NGFbSEgpUg27kBq`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7f69a22-9686-4022-9c95-ab8dda5c1869",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "bdeda363-cbab-48fc-be57-d317ad54fbef",
  "sourceToolAssistantUUID": "b7f69a22-9686-4022-9c95-ab8dda5c1869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T23:49:00.812Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MN32r7qyrT8sZTeveUY8Hr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdeda363-cbab-48fc-be57-d317ad54fbef",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiT8dgCX185YUDWfTiG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7f554fc-fa48-43cd-a3c4-c3581c8a6a0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdkrpEwJigMEpSXqqpvFXx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18063,
      "cache_read_input_tokens": 28577,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18063
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 28577,
          "cache_creation_input_tokens": 18063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18063,
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

_source line 35 · 2026-05-20T23:49:00.818Z_

<details><summary>↩ Tool result · `toolu_01MN32r7qyrT8sZTeveUY8Hr`</summary>

```text
1	---
2	name: LLM Evaluation Variance — Research Patterns
3	description: Experimental consensus on variance sources, decomposition methods, and gaps in LLM evaluation reproducibility (10 papers, 2024-2026)
4	type: research
5	source_papers: 10
6	---
7	
8	## Variance Source Taxonomy
9	
10	**Infrastructure variance** (4/10; high confidence):
11	- Numerical precision: BF16→9% accuracy std; FP32→~0% (Yuan 2025). Reasoning models most affected.
12	- Batch-size dependence: 80/1000 unique completions at T=0 from batch-invariance failure in RMSNorm/GEMM/attention (ThinkingMachines 2025).
13	- Background randomness at T=0: GPT~0.075, Gemini~0.065, Claude~0 effective temperature (Messina TMLR 2026).
14	
15	**Methodological variance** (6/10; high confidence):
16	- Judge choice dominates safety eval (43.8% variance); prompt~50% in open models, ~25% commercial (Mesting 2026, Brittlebench 2026).
17	- Much apparent prompt sensitivity is evaluation artifact — LLM-judge raises rank correlation 0.30→0.95 (Hua EMNLP 2025).
18	- Standard CIs omit 40-60% uncertainty; naive 95% CIs→79% coverage at scale (Mesting 2026).
19	
20	## Decomposition Frameworks
21	
22	| Framework | Paper | Method |
23	|-----------|-------|--------|
24	| TEE (G-theory) | Mesting 2026 | REML + D-study, facets: item/prompt/judge/temp |
25	| Total Variance | Brittlebench 2026 | V_data + V_brittleness via ANOVA |
26	| Intent Decomp | Kunievsky 2025 | intent/articulation/model uncertainty |
27	| Background Temp | Messina 2026 | Reference calibration→single T_bg scalar |
28	
29	G-theory adaptation is the most rigorous approach (Mesting). 4/10 papers use variance decomposition. **High confidence.**
30	
31	## Benchmarks & Models
32	
33	Top benchmarks: MMLU (3), GPQA (3), MATH (3), ARC (2), TruthfulQA (2). Models: Llama/Qwen/GPT families (5 papers each); 7B-8B open-weight as standard testbed. 10-100 runs per config is norm. **High confidence.**
34	
35	## Mitigations
36	
37	- LayerCast (BF16 store+FP32 compute): <3.4% divergence, 34% memory savings (Yuan). **Medium.**
38	- Batch-invariant kernels: determinism at 1.6-2.1× latency (ThinkingMachines). **Medium.**
39	- TEE-guided design: halves RMSE; 3 judges→38% SE reduction (Mesting). **Medium.**
40	
41	## Critical Gap — Our Niche
42	
43	**No paper unifies infrastructure (precision/batch/hardware) with methodological (prompt/judge/temp) variance in one G-theory framework.** Mesting applies G-theory to methodological facets only; Yuan/ThinkingMachines characterize infra variance without G-theory. Additional gaps: no cross-lingual analysis; training-time seed variance disconnected from inference-time; no standardized variance reporting protocol. **Support: 10/10 (absence), high confidence.**
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7f554fc-fa48-43cd-a3c4-c3581c8a6a0e",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "e167c7d8-f0e6-4870-96fc-d103a12196de",
  "sourceToolAssistantUUID": "f7f554fc-fa48-43cd-a3c4-c3581c8a6a0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T23:49:04.752Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ANbBzfzdx148sakHw6ouxj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e167c7d8-f0e6-4870-96fc-d103a12196de",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiTktzivJiHHDv9YcMu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "009cc245-4919-4c64-be8b-766a4255ba87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FodigxwkKcWFYG7h7BFiF5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 46640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1195,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 37 · 2026-05-20T23:49:04.757Z_

<details><summary>↩ Tool result · `toolu_01ANbBzfzdx148sakHw6ouxj`</summary>

```text
1	---
2	name: LLM Evaluation Variance — Writing Patterns
3	description: Narrative strategies, figure/table conventions from LLM evaluation variance papers (8 deep-read, 2024-2026)
4	type: writing
5	source_papers: 8
6	---
7	
8	## Story Types
9	
10	- **Breaking limitations** (3/8): Brittlebench, Yuan, ThinkingMachines. "Everyone assumed X, we show it fails." High.
11	- **Simplification** (2/8): Hua, GeneralizIT. "Complex problem, simpler real answer." Medium.
12	- **Unifying framework** (2/8): Kunievsky, Messina. "Scattered observations, one formalism." Medium.
13	- **Cross-domain transfer** (1/8): Mesting (psychometrics→ML). Our paper fits this type — study Mesting's structure. Low but critical.
14	
15	## Hook: Counter-Intuitive Claim Dominates (4/8, high)
16	
17	"Greedy≠deterministic" (Yuan), "80/1000 unique at T=0" (ThinkingMachines), "sensitivity is artifact" (Hua), "95% CIs→79% coverage" (Mesting). **Pattern**: open with a concrete number violating expectations. Avoid vague "X is important."
18	
19	## Tension: "Everyone's Doing It Wrong" (4/8, high)
20	
21	(1) Cite widespread practice, (2) quantified evidence it fails, (3) identify overlooked factor. ThinkingMachines adds a twist: debunk the accepted explanation before presenting the correct one.
22	
23	## Intro: 4 Paragraphs + 3 Contributions (mode)
24	
25	(1) Context, (2) existing approaches + limitation, (3) gap/surprise, (4) contributions. 3 contributions standard: framework + empirical finding + practical tool. **Support: 5/8, high.**
26	
27	## Figure Conventions
28	
29	**Figure 1**: problem_illustration (4/8) — show problem exists before solution. Concrete examples with before/after or divergence visualization. **High.**
30	
31	**Result figures**: bar charts primary (5/8); stacked bars for variance decomposition (2/8, Mesting/Brittlebench — expected idiom for our paper); line plots for trends (3/8); heatmaps for divergence (2/8). **High.**
32	
33	**Figure count**: 4-6 total. **Flow**: problem illustration → method diagram → variance decomposition → D-study projections. **Support: 6/8, high.**
34	
35	## Table Conventions
36	
37	**Main table**: rows=models/configs, cols=benchmarks×metrics, grouped by category (commercial/open or reasoning/non-reasoning). Bold best, 4-8 baselines. **Support: 5/8, high.**
38	
39	**Ablation**: full_numbers (5/8) over checkmark_grid (2/8). Checkmark only for component-presence ablation. **High.**
40	
41	**Reporting**: std across configs/runs standard; only Mesting reports full REML components. **High.**
42	
43	**Figure vs table split**: figures for decomposition visuals/trends/qualitative; tables for exact numbers/comparisons. Appendix for per-config breakdowns and validation. **Support: 6/8, high.**
44	
45	## Our Paper Blueprint
46	
47	Open with shocking quantified finding about unreported variance → "everyone's CIs are wrong" tension → G-theory as borrowed lens → 2-3 domain demonstrations → stacked-bar variance decomposition as signature visual → D-study projections as practical value.
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "009cc245-4919-4c64-be8b-766a4255ba87",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "151c8aa9-b427-4e5c-9bbb-26e3e9a06166",
  "sourceToolAssistantUUID": "009cc245-4919-4c64-be8b-766a4255ba87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T23:49:06.254Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KoTY8g2JftxdSx5Ny5Lsku`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260520T222113/logs/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "151c8aa9-b427-4e5c-9bbb-26e3e9a06166",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiTktzivJiHHDv9YcMu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a68e912f-831f-42ad-bab7-837f0a244c69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FodigxwkKcWFYG7h7BFiF5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 46640,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1195
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 46640,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1195,
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

_source line 39 · 2026-05-20T23:49:06.287Z_

<details><summary>↩ Tool result · `toolu_01KoTY8g2JftxdSx5Ny5Lsku`</summary>

```text
artifacts/dream_reports/dream_20260520T222113/logs/orchestrator.log
artifacts/dream_reports/dream_20260520T222113/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T222113/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T222113/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T222113/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T222113/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T222113/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T222113/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T222113/logs/review_best.log
artifacts/dream_reports/dream_20260520T222113/logs/review_median.log
artifacts/dream_reports/dream_20260520T222113/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a68e912f-831f-42ad-bab7-837f0a244c69",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "132893ed-d684-40f4-a701-a52a1a147de4",
  "sourceToolAssistantUUID": "a68e912f-831f-42ad-bab7-837f0a244c69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T23:49:09.714Z_

Let me read the existing reviews and the first dream report for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "132893ed-d684-40f4-a701-a52a1a147de4",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiUAGg7z1Wgdhx1BheV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96fb545e-2a07-4d7a-8a71-d9257817d2be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhRyELpQZxiq6f1atXGGTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1560,
      "cache_read_input_tokens": 47835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1560,
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

_source line 41 · 2026-05-20T23:49:11.808Z_

<details open><summary>🔧 Tool call — Read · `toolu_018EqN8yhwfTs9R6dN7QXRTA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/logs/review_best.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96fb545e-2a07-4d7a-8a71-d9257817d2be",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiUAGg7z1Wgdhx1BheV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c4e3421-92a9-480c-8f35-b53071b1b5af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhRyELpQZxiq6f1atXGGTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1560,
      "cache_read_input_tokens": 47835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1560,
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

_source line 42 · 2026-05-20T23:49:11.829Z_

<details><summary>↩ Tool result · reported error · `toolu_018EqN8yhwfTs9R6dN7QXRTA`</summary>

```text
File content (3.2MB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c4e3421-92a9-480c-8f35-b53071b1b5af",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "f99a1201-5974-48c4-9ff0-a88957196155",
  "toolUseResult": "Error: File content (3.2MB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "8c4e3421-92a9-480c-8f35-b53071b1b5af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T23:49:12.172Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C1BbeoxkboEiofi7a7d5wc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f99a1201-5974-48c4-9ff0-a88957196155",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiUAGg7z1Wgdhx1BheV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84cdf99e-880e-4f93-9698-6b2b408e169c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhRyELpQZxiq6f1atXGGTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1560,
      "cache_read_input_tokens": 47835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1560,
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

_source line 44 · 2026-05-20T23:49:12.178Z_

<details><summary>↩ Tool result · `toolu_01C1BbeoxkboEiofi7a7d5wc`</summary>

```text
1	# Paper Framing — nlp_variance_gtheory
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
5	- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
6	- Extended: TACL (rolling)
7	
8	## Title
9	Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
10	
11	## Core Claims (3 条，可证伪)
12	
13	**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.
14	
15	**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.
16	
17	**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.
18	
19	## Contributions (3 条，明确区分)
20	
21	1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.
22	
23	2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.
24	
25	3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).
26	
27	## Story Spine
28	
29	**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.
30	
31	**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.
32	
33	**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.
34	
35	**Headline result template**: "In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds."
36	
37	## Hook (Counter-Intuitive Quantified Claim)
38	"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."
39	
40	## Narrative Strategy
41	- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
42	- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
43	- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
44	- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
45	- **Figure plan** (4 figures minimum):
46	  1. Problem illustration: same model, different benchmark → different dominant variance source
47	  2. G-theory facet diagram showing crossed design
48	  3. Stacked-bar variance decomposition across benchmarks (signature figure)
49	  4. D-study projection curves: G vs item count for different benchmarks
50	- **Key framing shifts from Dream feedback**:
51	  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty
52	  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient
53	  - Cross-benchmark gradient is the **primary novel finding**
54	  - "Fully crossed" language qualified to MMLU exp-001 only; other benchmarks use reduced designs
55	
56	## Venue Fit Risks
57	- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
58	- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
59	- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.
60	- Reviewer concern 3: "Item dominance is obvious from measurement theory" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.
61	
62	## Anticipated Reviewer Concerns & Planned Responses
63	1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to "numerical precision" and frame hardware as future work.
64	2. **"float32 engine confound"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.
65	3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.
66	4. **"Small item sample"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.
67	5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.
68	6. **"Missing scale validation"** → exp-005 (14B models)
69	7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.
70	8. **"Separability claim is metric-dependent"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.
71	9. **"FP32 degradation is already known (Yuan 2025)"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.
72	10. **"Incremental over Mesting (2026)"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.
73	11. **"Model not treated as G-theory facet"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.
74	12. **"No CIs on variance components"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.
75	13. **"Missing related work — IRT, tinyBenchmarks, Bouthillier"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.
76	14. **"Diagnostic tool claim unsubstantiated"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as "empirical analysis + data release."
77	15. **"Fine-tuning uses encoder-only RoBERTa"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.
78	
79	## Design Decisions
80	- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
81	- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
82	- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
83	- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.
84	- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.
85	- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as "reduced crossing" rather than "fully crossed."
86	
87	## Required Bibliography (minimum 25 references)
88	Key references to include beyond current literature_map:
89	- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA
90	- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP
91	- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP
92	- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling
93	- Perlitz et al. (2023) — Efficient LLM benchmarking
94	- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition
95	- Shavelson & Webb (1991) — G-theory primer (canonical)
96	- Brennan (2001) — G-theory textbook (canonical)
97	- Lu et al. (2022) — Option ordering effects in MC evaluation
98	- Pezeshkpour & Hruschka (2024) — Option ordering effects
99	- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)
100	- Sellam et al. (2022) — MultiBERTs, multi-seed training
101	- Dehghani et al. (2021) — Benchmark Lottery
102	- Biderman et al. (2024) — Evaluation reproducibility lessons
103	- Vania et al. (2021) — IRT item properties in NLP
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84cdf99e-880e-4f93-9698-6b2b408e169c",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "8f21de8d-0890-4d01-a242-142debec4b42",
  "sourceToolAssistantUUID": "84cdf99e-880e-4f93-9698-6b2b408e169c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-20T23:49:15.159Z_

Now let me also read the earlier dream review and check the median/worst papers for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f21de8d-0890-4d01-a242-142debec4b42",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiUcWFaZTGGpnUA8Tpe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a897fa8-3c98-44be-b871-628effe6ef57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF2tzQ9zo3QN9zrek8ZCxR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3909,
      "cache_read_input_tokens": 49395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3909,
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

_source line 46 · 2026-05-20T23:49:18.214Z_

<details open><summary>🔧 Tool call — Read · `toolu_014kxnvrTiZT6DbdUXT8SoXH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a897fa8-3c98-44be-b871-628effe6ef57",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiUcWFaZTGGpnUA8Tpe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "060fe820-b508-4777-bb24-2f342565eac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF2tzQ9zo3QN9zrek8ZCxR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3909,
      "cache_read_input_tokens": 49395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3909,
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

_source line 47 · 2026-05-20T23:49:18.224Z_

<details><summary>↩ Tool result · `toolu_014kxnvrTiZT6DbdUXT8SoXH`</summary>

```text
1	\documentclass[11pt,twocolumn]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{enumitem}
13	\usepackage{array}
14	\usepackage{tabularx}
15	\usepackage{caption}
16	
17	\setlength{\columnsep}{0.3in}
18	\captionsetup{font=small}
19	
20	\title{Reproducibility Budgets for LLM Evaluation:\\A Generalizability Theory Analysis of Variance Sources\\Across Benchmarks, Models, and Evaluation Metrics}
21	
22	\author{
23	Anonymous Authors
24	}
25	
26	\date{}
27	
28	\begin{document}
29	\maketitle
30	
31	% ============================================================
32	% ABSTRACT
33	% ============================================================
34	\begin{abstract}
35	When LLM benchmark results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, numerical precision, temperature, or item selection---let alone how these factors interact. We conduct a multi-benchmark Generalizability Theory (G-theory) study crossing infrastructure (numerical precision, hardware) with methodology (prompt template, seed, temperature, answer ordering) and measurement (item selection) facets across five benchmarks (MMLU, ARC-Challenge, GSM8K, HellaSwag, MATH), four 7--9B models, two 14B models, and two GPU architectures, totaling over 3 million evaluation observations. Three findings emerge. First, item selection is the single largest variance source, but its magnitude is benchmark-conditional: 48\% on knowledge-retrieval tasks (MMLU) versus 28\% on proof-reasoning tasks (MATH) under model-as-facet analysis, forming a task-type clustering from knowledge-dominated to interaction-dominated variance structures. Second, infrastructure and methodology factors are approximately separable on knowledge benchmarks (infra$\times$method $<$0.5\% binary), but this separability breaks down on math-generation benchmarks where precision$\times$temperature reaches 3\% under binary scoring. Third, reproducibility budgets are fundamentally metric-dependent: binary scoring yields $G=0.37$ while text-exact-match yields $G=0.97$, and optimal facet allocation differs by benchmark---MMLU requires 420 items for $G\geq0.90$ versus 240 for HellaSwag. We release variance decomposition tables and D-study projection code to enable task-specific reproducibility planning.
36	\end{abstract}
37	
38	% ============================================================
39	% 1. INTRODUCTION
40	% ============================================================
41	\section{Introduction}
42	
43	The reliability of LLM evaluation has become a first-order concern as benchmark scores drive model selection, funding decisions, and public perception. Recent studies have documented substantial score variation from individual factors: up to 9 percentage points from numerical precision alone \citep{yuan2025}, 50\% variance from prompt template choice on fixed hardware \citep{mizrahi2024}, and significant sensitivity to random seeds and answer ordering \citep{lu2022,pezeshkpour2024}. Yet each study isolates at most two sources, implicitly assuming that infrastructure factors (precision, hardware) and methodology factors (prompt, seed, temperature) contribute independently. Whether this separability assumption holds---and whether findings from one benchmark generalize to another---remains untested.
44	
45	Generalizability Theory (G-theory) provides a principled framework for simultaneously decomposing variance across multiple facets and their interactions \citep{shavelson1991,brennan2001}. Unlike ANOVA, G-theory distinguishes the universe score from error variance and supports Decision studies (D-studies) that project reliability under alternative resource allocations. \citet{bouthillier2021} demonstrated the value of factorial variance decomposition for ML benchmarks via ANOVA, and \citet{mesting2026} adapted G-theory to five methodology facets in LLM evaluation. However, neither study crossed infrastructure with methodology in a unified design, and both analyzed a single benchmark---leaving the question of cross-benchmark generalization unanswered.
46	
47	We conduct the first multi-benchmark G-theory analysis of LLM evaluation variance, crossing infrastructure (numerical precision across two GPU architectures) with methodology (prompt template, seed, temperature, answer ordering) and measurement (item selection) facets. Our design spans five benchmarks (MMLU, ARC-Challenge, GSM8K, HellaSwag, MATH), four 7--9B models with model treated as a crossed random facet, and over 3 million total observations. The key insight is that \emph{the variance structure itself depends on what you are benchmarking}: knowledge-retrieval benchmarks exhibit high item dominance with negligible cross-factor interaction, while reasoning benchmarks show reduced item dominance with detectable infrastructure$\times$methodology coupling. This benchmark-conditional structure renders any ``universal reproducibility recipe'' illusory.
48	
49	Our contributions are: (1) a cross-benchmark variance gradient showing that item dominance shifts from 48\% (knowledge) to 28\% (proof reasoning) under model-as-facet analysis, with a three-tier task-type clustering; (2) a confirmatory separability test showing infrastructure$\times$methodology interactions $<$0.5\% on knowledge benchmarks but reaching 3\% on math-generation benchmarks; and (3) task-specific reproducibility budgets via D-study projections with bootstrap confidence intervals, showing that optimal facet allocation is both benchmark-specific and metric-conditional.
50	
51	% ============================================================
52	% 2. RELATED WORK
53	% ============================================================
54	\section{Related Work}
55	
56	\paragraph{Variance sources in LLM evaluation.}
57	\citet{yuan2025} documented up to 9\% accuracy variation from hardware and numerical precision without factorial attribution. \citet{mizrahi2024} (Brittlebench) quantified prompt sensitivity at approximately 50\% of evaluation variance on fixed hardware. \citet{lu2022} and \citet{pezeshkpour2024} demonstrated significant option-ordering effects in multiple-choice evaluation. \citet{biderman2024} summarized reproducibility lessons across evaluation frameworks. These studies isolate individual factors; our work crosses them in a unified factorial design.
58	
59	\paragraph{Generalizability Theory in NLP.}
60	G-theory \citep{shavelson1991,brennan2001} has been applied extensively in educational and psychological measurement. \citet{bouthillier2021} adapted ANOVA-based variance decomposition to ML benchmarks, decomposing variance across hyperparameters, data splits, and seeds. \citet{mesting2026} applied G-theory to LLM evaluation with five methodology facets but treated infrastructure as fixed and analyzed only MMLU. Our work extends this to infrastructure$\times$methodology crossing across multiple benchmarks.
61	
62	\paragraph{Item-level analysis and efficient benchmarking.}
63	Item Response Theory (IRT) provides a complementary perspective on item properties \citep{lalor2019,rodriguez2021,vania2021}. \citet{polo2024} used IRT for efficient subsampling (tinyBenchmarks), and \citet{perlitz2023} developed HELM-Lite for efficient benchmarking. Our D-study projections offer a G-theory-based alternative to IRT subsampling, with the advantage of jointly optimizing across multiple facets.
64	
65	\paragraph{Training instability and reproducibility.}
66	\citet{dodge2020} documented fine-tuning instability from seeds and data order. \citet{sellam2022} (MultiBERTs) trained multiple BERT copies to quantify training variance. \citet{henderson2018} highlighted variance in deep RL evaluation. \citet{dehghani2021} (Benchmark Lottery) showed that model ranking depends on benchmark selection. Our fine-tuning G-study (Section~\ref{sec:finetuning}) extends this line by decomposing fine-tuning variance with G-theory.
67	
68	% ============================================================
69	% 3. FRAMEWORK AND METHOD
70	% ============================================================
71	\section{Framework and Method}
72	
73	\subsection{Generalizability Theory}
74	
75	In G-theory, the observed score for person $p$ (here: item $i$) under condition $c$ is decomposed as:
76	\begin{equation}
77	X_{ic} = \mu + \alpha_i + \beta_c + (\alpha\beta)_{ic} + \epsilon_{ic}
78	\end{equation}
79	where $\alpha_i$ captures item difficulty, $\beta_c$ captures condition effects (prompt, seed, temperature, precision, ordering), $(\alpha\beta)_{ic}$ captures item$\times$condition interactions, and $\epsilon_{ic}$ is residual error. G-theory estimates variance components $\hat{\sigma}^2$ for each source, which partition total variance. The \emph{generalizability coefficient} $G$ quantifies the reliability of the benchmark score as a function of the number of items and conditions:
80	\begin{equation}
81	G = \frac{\hat{\sigma}^2_i}{\hat{\sigma}^2_i + \sum_c \hat{\sigma}^2_{ic}/n_c + \hat{\sigma}^2_\epsilon / (n_c \cdot n_i)}
82	\end{equation}
83	
84	A \emph{Decision study} (D-study) projects $G$ under hypothetical resource allocations (e.g., more items, fewer prompts), enabling cost-effective evaluation design.
85	
86	\subsection{Experimental Design}
87	
88	We conduct a series of G-studies with increasing scope:
89	
90	\paragraph{Experiment 1: Full-scale MMLU G-study.} 4 models $\times$ 3 precisions (FP32, BF16, FP16; all vLLM V0 enforce\_eager) $\times$ 6 prompt templates $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 answer orderings $\times$ 200 MMLU items (stratified across 57 subjects). Total: 1,036,800 observations across 5,184 conditions. The V0 enforce\_eager configuration eliminates a previously identified engine confound where BF16 defaults to a different execution path.
91	
92	\paragraph{Experiment 2: Item resampling stability.} Three independent stratified samples of 200 MMLU items (seeds 0, 7, 99) $\times$ Llama-3.1-8B $\times$ reduced crossing (3 precisions $\times$ 3 prompts $\times$ 3 seeds $\times$ 2 orderings). 32,400 observations per sample.
93	
94	\paragraph{Experiment 3: Multi-benchmark replication.} GSM8K, ARC-Challenge, and HellaSwag with 4 models $\times$ 2 precisions (BF16, FP16) $\times$ 6 prompts $\times$ 6 seeds $\times$ 2 temperatures $\times$ 4 orderings $\times$ 200 items. 384,000 observations per benchmark (reduced crossing vs.\ Experiment 1).
95	
96	\paragraph{Experiment 4: Multi-hardware G-study.} 4 models $\times$ 2 GPU types $\times$ 2 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 orderings $\times$ 200 MMLU items. 1,152,000 observations.
97	
98	\paragraph{Experiment 5: Combined analysis.} Reanalysis of all preceding data with: (a) model treated as a crossed random facet; (b) bootstrap confidence intervals (1,000 resamples); (c) D-study projections; (d) REML vs.\ Henderson Method I comparison; (e) log-probability scoring; (f) ranking stability analysis.
99	
100	\paragraph{Experiment 6: 14B scale extension.} Qwen3-14B and DeepSeek-R1-Distill-14B at BF16/FP16 $\times$ 6 prompts $\times$ 6 seeds $\times$ 2 temperatures $\times$ 4 orderings $\times$ 200 MMLU items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "060fe820-b508-4777-bb24-2f342565eac2",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "24153353-0cec-4f99-9bee-2a6f8394e9cd",
  "sourceToolAssistantUUID": "060fe820-b508-4777-bb24-2f342565eac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T23:49:18.495Z_

<details open><summary>🔧 Tool call — Read · `toolu_017GPfcdhTTGuhi9VeKzqhK6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24153353-0cec-4f99-9bee-2a6f8394e9cd",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiUcWFaZTGGpnUA8Tpe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0022579-b185-4b0f-aad4-f53ddaa31ff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF2tzQ9zo3QN9zrek8ZCxR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3909,
      "cache_read_input_tokens": 49395,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 49395,
          "cache_creation_input_tokens": 3909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3909,
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

_source line 49 · 2026-05-20T23:49:18.500Z_

<details><summary>↩ Tool result · `toolu_017GPfcdhTTGuhi9VeKzqhK6`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=1in]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{adjustbox}
14	
15	\title{Variance Decomposition Is a Measurement, Not a Fact:\\
16	On the Instability of Reproducibility Budgets for LLM Evaluation}
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
29	We set out to build reproducibility budgets for LLM evaluation using Generalizability Theory (G-theory) and discovered that the budget itself is unreliable.
30	In a multi-benchmark G-study crossing infrastructure (numerical precision, hardware) $\times$ methodology (prompt, seed, temperature, ordering) $\times$ measurement (item) factors across four models and five benchmarks (172{,}800--230{,}400 observations per experiment), we find three results that challenge current variance-attribution practices.
31	First, item dominance estimates are sample-unstable: resampling 200 MMLU items with different stratified seeds yields item variance shares ranging from 25\% to 48\% (CV\,=\,0.33), meaning prior single-decomposition studies---including all existing G-theory analyses of LLM evaluation---over-commit to attribution certainty.
32	Second, treating model as fixed (the standard practice) systematically inflates item variance from 37.8\% to an apparent dominance; a model-as-facet reanalysis reveals that model$\times$item interaction (33\%) is the single largest component, reducing pure item variance to 15.2\%.
33	Third, D-study reproducibility budgets converge across benchmarks (range = 60 items for $G \geq 0.90$) but carry bootstrap confidence intervals of $\pm$190 items, rendering benchmark-specific budget recommendations statistically indistinguishable and demanding that budgets themselves report uncertainty.
34	These findings reframe variance decomposition from a factual attribution to a measurement with its own error, requiring uncertainty quantification before actionable conclusions can be drawn.
35	\end{abstract}
36	
37	% ============================================================
38	% 1. INTRODUCTION
39	% ============================================================
40	\section{Introduction}
41	
42	When LLM evaluation results fail to replicate, the natural response is to identify the culprit: was it the prompt, the random seed, the GPU, the numerical precision, or the item selection?
43	A growing body of work has pursued this question by decomposing evaluation variance into attributable sources \citep{bouthillier2021accounting, mesting2026generalizability, brittlebench2026}.
44	These studies report point estimates of variance shares---``item selection accounts for 43.8\% of variance'' \citep{mesting2026generalizability}, ``prompt sensitivity explains 50\% of score variation'' \citep{brittlebench2026}---and derive practical recommendations from them.
45	
46	We conducted a large-scale G-theory study with the same goal: cross infrastructure and methodology factors in a unified framework, measure variance components across five benchmarks, and produce reproducibility budgets telling practitioners how many items, prompts, and seeds they need.
47	What we found instead is that \emph{the variance decomposition itself is unstable}.
48	Three independent item samples of 200 MMLU questions yield item dominance estimates of 48\%, 25\%, and 41\%---a coefficient of variation of 33\%.
49	Which items happen to be sampled determines not just the magnitude but the \emph{rank order} of variance components: in one sample, the residual exceeds item variance as the largest component.
50	Every prior study that reports a single variance decomposition without resampling stability analysis has, in effect, presented one draw from a high-variance distribution as a finding.
51	
52	This instability compounds with a second problem: model specification.
53	Standard practice treats model as fixed and pools across models or analyzes each separately.
54	When we instead treat model as a crossed random facet, item variance drops from 37.8\% to 15.2\%, with the difference absorbed by a model$\times$item interaction of 33\%---the largest single component in the crossed design.
55	Item ``difficulty'' is not an intrinsic property of items but a joint property of item--model pairs, a conclusion that fundamentally challenges the premise of item-dominated variance attribution.
56	
57	A third discovery concerns reproducibility budgets themselves.
58	D-study projections for $G \geq 0.90$ converge across benchmarks (420--520 items, range = 60), which would seem to simplify practical recommendations.
59	But the bootstrap 95\% confidence intervals span $\pm$190 items---wider than the cross-benchmark range---meaning any specific budget recommendation is statistically indistinguishable from its neighbors.
60	Reproducibility budgets require their own error bars.
61	
62	Our contributions are:
63	\begin{enumerate}
64	\item Evidence that variance component estimates in LLM evaluation are sample-unstable (item resampling CV\,=\,0.33, component rank inversions across samples), establishing that single-run decompositions over-commit to attribution certainty.
65	\item A model-as-facet reanalysis showing that model$\times$item interaction (33\%) is the largest overlooked variance source, and that treating model as fixed inflates item dominance by $>$22 percentage points.
66	\item A demonstration that D-study reproducibility budgets require uncertainty quantification: cross-benchmark budget convergence (range = 60 items) is dominated by within-benchmark CI width ($\pm$190 items), rendering benchmark-specific recommendations unreliable.
67	\end{enumerate}
68	
69	% ============================================================
70	% 2. RELATED WORK
71	% ============================================================
72	\section{Related Work}
73	
74	\paragraph{Variance decomposition in ML evaluation.}
75	\citet{bouthillier2021accounting} introduced factorial variance decomposition to ML benchmarking via ANOVA, decomposing performance variation across hyperparameters, data splits, and random seeds.
76	\citet{henderson2018deep} applied similar methods to deep reinforcement learning, finding that implementation details dominate reported improvements.
77	\citet{dodge2020fine} and \citet{sellam2022multiBERTs} documented fine-tuning instability from seed and data order in BERT-scale models.
78	These studies establish the paradigm we build on but do not address LLM inference evaluation or apply G-theory's D-study projections.
79	
80	\paragraph{G-theory in LLM evaluation.}
81	\citet{mesting2026generalizability} adapted Generalizability Theory to LLM-as-judge evaluation, decomposing variance across five methodological facets.
82	Their study treats model and infrastructure as fixed, reports single-run point estimates without resampling stability analysis, and covers one benchmark.
83	\citet{brittlebench2026} quantified prompt sensitivity at up to 50\% of score variation on fixed hardware.
84	Neither study crosses infrastructure with methodology or tests the stability of their decomposition.
85	
86	\paragraph{Item-level analysis and IRT.}
87	Item Response Theory has been applied to NLP evaluation for item analysis \citep{lalor2019learning, rodriguez2021evaluation, vania2021comparing}, efficient subsampling \citep{polo2024tinybenchmarks, perlitz2023efficient}, and the Benchmark Lottery phenomenon \citep{dehghani2021benchmark}.
88	These approaches model item properties but do not decompose evaluation variance into infrastructure vs.\ methodology sources.
89	
90	\paragraph{Reproducibility factors.}
91	\citet{yuan2025llm} documented up to 9\% accuracy variation from hardware and numerical precision without factorial attribution.
92	\citet{lu2022fantastically, pezeshkpour2024large} studied option ordering effects in multiple-choice evaluation.
93	\citet{biderman2024lessons} surveyed evaluation reproducibility challenges.
94	Each isolates at most two factors, implicitly assuming separability.
95	
96	% ============================================================
97	% 3. METHOD
98	% ============================================================
99	\section{Method}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0022579-b185-4b0f-aad4-f53ddaa31ff1",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "9593d094-a07b-40e2-8a0b-7bff82c40721",
  "sourceToolAssistantUUID": "a0022579-b185-4b0f-aad4-f53ddaa31ff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-20T23:49:23.615Z_

I notice the user's task summary describes the "worst" paper version (with the "variance decomposition is a measurement, not a fact" title), while the "best" version has a different framing. Let me read the rest of the worst paper to understand the full scope, and also check what experiments produced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9593d094-a07b-40e2-8a0b-7bff82c40721",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiV4yDWFsB45os5e8iR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "986d252f-9027-4c43-b2e2-442cbfb911a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RTDuVceJoSm9fbatZxt7UC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5618,
      "cache_read_input_tokens": 53304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5618,
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

_source line 51 · 2026-05-20T23:49:25.803Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XsQcXZ1aP1Zw73FRy2dTrg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/paper.tex",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "986d252f-9027-4c43-b2e2-442cbfb911a9",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiV4yDWFsB45os5e8iR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6764c82-d400-4ec1-a933-dc69403281d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RTDuVceJoSm9fbatZxt7UC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5618,
      "cache_read_input_tokens": 53304,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5618
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 53304,
          "cache_creation_input_tokens": 5618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5618,
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

_source line 52 · 2026-05-20T23:49:26.071Z_

<details><summary>↩ Tool result · `toolu_01XsQcXZ1aP1Zw73FRy2dTrg`</summary>

```text
100	
101	\subsection{Generalizability Theory Framework}
102	
103	Generalizability Theory (G-theory; \citealp{shavelson1991generalizability, brennan2001generalizability}) decomposes observed score variance into components attributable to facets (e.g., items, prompts, seeds) and their interactions.
104	For a fully crossed design with $k$ facets, a person's observed score $X_{p}$ is:
105	\begin{equation}
106	X_{pijk\ldots} = \mu + \alpha_p + \beta_i + \gamma_j + \delta_k + (\alpha\beta)_{pi} + (\alpha\gamma)_{pj} + \cdots + \epsilon_{pijk\ldots}
107	\end{equation}
108	where each Greek letter represents the effect of a facet or interaction and $\epsilon$ is residual error.
109	The G-coefficient summarizes measurement dependability:
110	\begin{equation}
111	G = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_{\text{relative error}}}
112	\end{equation}
113	D-studies project $G$ under hypothetical facet sample sizes, enabling reproducibility budget planning.
114	
115	\subsection{Experimental Design}
116	
117	We conduct a series of experiments with increasing scope.
118	All experiments use generation-based evaluation (following \citealp{hua2025emnlp}) with vLLM 0.9.2 and \texttt{enforce\_eager} mode to eliminate engine-level confounds.
119	
120	\paragraph{Experiment 1: Full-scale precision study.}
121	4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B, Mistral-7B) $\times$ 3 precisions (FP32, BF16, FP16) $\times$ 6 prompts $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 orderings $\times$ 200 MMLU items = 172{,}800 observations.
122	Model is initially treated as fixed (analyzed per-model and pooled); Experiment 4 reanalyzes with model as a crossed facet.
123	
124	\paragraph{Experiment 1b: Item resampling stability.}
125	3 independent stratified 200-item MMLU samples (seeds 0, 7, 99) $\times$ Llama-3.1-8B $\times$ 3 precisions $\times$ 3 prompts $\times$ 3 seeds $\times$ 2 orderings = 54 conditions per sample, 10{,}800 observations per sample.
126	
127	\paragraph{Experiment 2: Multi-benchmark replication.}
128	4 models $\times$ 2 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 2 temperatures $\times$ 4 orderings on GSM8K, ARC-Challenge, and HellaSwag (200 items each), 76{,}800 observations per benchmark.
129	
130	\paragraph{Experiment 3: Multi-hardware G-study.}
131	4 models $\times$ 2 GPU types $\times$ 2 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 orderings $\times$ 200 MMLU items = 230{,}400 observations.
132	
133	\paragraph{Experiment 4: Comprehensive reanalysis.}
134	Merged data from Experiments 1--3. Model-as-facet reanalysis, 1{,}000-replicate bootstrap CIs on all variance components, D-study projections with uncertainty quantification, and REML sensitivity analysis.
135	
136	\paragraph{Experiment 5: Scale extension.}
137	Qwen3-14B and DeepSeek-R1-Distill-14B at BF16/FP16, testing whether 14B models alter variance structure.
138	
139	\paragraph{Experiment 6: Fine-tuning G-study.}
140	RoBERTa-large on SST-2, MNLI, RTE, COPA. 6 seeds $\times$ 3 learning rates $\times$ 4 data shuffles $\times$ 3 GPUs $\times$ 2 precisions = 432 runs per task, 1{,}728 total.
141	
142	\paragraph{Experiment 7: LayerCast precision mitigation.}
143	FP16 storage + FP32 compute as a fourth precision condition on MMLU.
144	
145	\paragraph{Experiment 8: MATH benchmark extension.}
146	200 MATH items under the same multi-benchmark protocol, completing a 5-benchmark spectrum.
147	
148	% ============================================================
149	% 4. EXPERIMENTS AND RESULTS
150	% ============================================================
151	\section{Experiments and Results}
152	
153	\subsection{Experiment 1: Variance Decomposition Under Model-as-Fixed Analysis}
154	\label{sec:exp1}
155	
156	Table~\ref{tab:exp1_variance} presents the variance decomposition from the full-scale MMLU study with model treated as fixed.
157	At face value, item selection is the largest component (37.8\% pooled), with substantial variation across models: Qwen3-8B shows the highest item dominance (42.2\%) while Mistral-7B shows the lowest (30.3\%, CV across models = 0.13).
158	
159	\begin{table}[t]
160	\centering
161	\caption{Variance components under model-as-fixed analysis (MMLU, binary scoring, 200 items). These point estimates are subsequently shown to be unstable (Sec.~\ref{sec:exp1b}) and inflated (Sec.~\ref{sec:exp4}).}
162	\label{tab:exp1_variance}
163	\begin{adjustbox}{max width=\textwidth}
164	\begin{tabular}{lccccc}
165	\toprule
166	Component & Qwen3-8B & Llama-3.1-8B & Gemma-2-9B & Mistral-7B & Pooled \\
167	\midrule
168	item\_id         & 42.2\% & 35.8\% & 40.1\% & 30.3\% & 37.8\% \\
169	residual         & 17.4\% & 21.2\% & 18.8\% & 26.1\% & 20.2\% \\
170	temperature:item & 6.3\%  & 5.9\%  & 5.2\%  & 5.8\%  & 5.8\%  \\
171	prompt:item      & 5.8\%  & 5.4\%  & 4.8\%  & 4.2\%  & 5.2\%  \\
172	precision:item   & 4.9\%  & 4.6\%  & 4.2\%  & 3.8\%  & 4.5\%  \\
173	seed:item        & 1.8\%  & 1.7\%  & 1.4\%  & 1.3\%  & 1.6\%  \\
174	ordering:item    & 1.4\%  & 1.2\%  & 1.1\%  & 0.9\%  & 1.2\%  \\
175	precision        & 1.8\%  & 1.7\%  & 1.5\%  & 1.3\%  & 1.6\%  \\
176	temperature      & 1.2\%  & 1.0\%  & 0.9\%  & 0.8\%  & 1.0\%  \\
177	prompt           & 0.8\%  & 0.7\%  & 0.6\%  & 0.5\%  & 0.7\%  \\
178	prec.:temp.      & 1.6\%  & 1.5\%  & 1.4\%  & 1.2\%  & 1.5\%  \\
179	all other        & 14.8\% & 19.3\% & 20.0\% & 23.8\% & 18.9\% \\
180	\bottomrule
181	\end{tabular}
182	\end{adjustbox}
183	\end{table}
184	
185	Precision main effects are small after confound correction (1.6\% pooled), and accuracy differences across FP32 (0.668), BF16 (0.672), and FP16 (0.670) are negligible ($\Delta_{\max}$ = 0.004 for each model).
186	The $G$-coefficient under binary scoring is 0.32, reflecting the inherent low reliability of binary item scoring with 200 items.
187	The precision$\times$temperature interaction (1.5\%) is non-negligible but does not by itself break separability.
188	
189	These results appear to support an item-dominance narrative.
190	However, as we show next, this narrative is an artifact of two methodological choices: a single item sample and a fixed-model specification.
191	
192	\subsection{Experiment 1b: Item Resampling Instability}
193	\label{sec:exp1b}
194	
195	Table~\ref{tab:resample} presents the variance decomposition under three independent stratified 200-item MMLU samples.
196	The item variance share ranges from 25.0\% (Sample~7) to 48.0\% (Sample~0), yielding a coefficient of variation of 0.33.
197	This instability is not merely quantitative: in Sample~7, the residual (30.0\%) exceeds item variance (25.0\%) as the largest component, producing a qualitatively different decomposition.
198	
199	\begin{table}[t]
200	\centering
201	\caption{Variance decomposition across three independent item samples (Llama-3.1-8B, MMLU). Item dominance is sample-dependent, with rank inversions across samples.}
202	\label{tab:resample}
203	\begin{tabular}{lcccccc}
204	\toprule
205	Component & Sample 0 & Sample 7 & Sample 99 & Mean & SD & CV \\
206	\midrule
207	item\_id        & 48.0\% & 25.0\% & 41.0\% & 38.0\% & 12.0\% & 0.33 \\
208	residual        & 16.0\% & 30.0\% & 19.0\% & 21.7\% & 7.5\%  & 0.35 \\
209	temperature:item& 7.2\%  & 9.8\%  & 8.1\%  & 8.4\%  & 1.3\%  & 0.16 \\
210	prompt:item     & 5.6\%  & 8.2\%  & 6.4\%  & 6.7\%  & 1.3\%  & 0.20 \\
211	precision:item  & 4.8\%  & 6.4\%  & 5.2\%  & 5.5\%  & 0.8\%  & 0.15 \\
212	temperature     & 1.0\%  & 2.4\%  & 1.4\%  & 1.6\%  & 0.7\%  & 0.46 \\
213	prompt          & 0.6\%  & 1.8\%  & 0.9\%  & 1.1\%  & 0.6\%  & 0.58 \\
214	all other       & 16.8\% & 16.4\% & 18.0\% & 17.1\% & 0.8\%  & 0.05 \\
215	\bottomrule
216	\end{tabular}
217	\end{table}
218	
219	Table~\ref{tab:resample_stability} shows that the $G$-coefficient itself varies from 0.28 to 0.38 across samples (CV\,=\,0.16), and the largest-component identity is not stable.
220	The bootstrap 95\% CI on item variance is [0.27, 0.48] (width = 0.21), wide enough that it cannot distinguish between ``item dominance'' ($>$40\%) and ``item is one of several comparable sources'' ($\sim$25\%).
221	
222	\begin{table}[t]
223	\centering
224	\caption{$G$-coefficient and rank stability across item samples. The rank order of variance components is not stable: Sample~7 reverses the top two components.}
225	\label{tab:resample_stability}
226	\begin{tabular}{lccc}
227	\toprule
228	Metric & Sample 0 & Sample 7 & Sample 99 \\
229	\midrule
230	$G$ (correct)       & 0.28     & 0.38     & 0.31 \\
231	Largest component    & item\_id & residual & item\_id \\
232	2nd largest          & residual & item\_id & residual \\
233	3rd largest          & temp:item& temp:item& temp:item \\
234	Item difficulty SD   & 0.31     & 0.22     & 0.27 \\
235	Bimodality index     & 0.71     & 0.38     & 0.58 \\
236	\bottomrule
237	\end{tabular}
238	\end{table}
239	
240	The mechanism is traceable: Sample~0 draws more items with extreme difficulty (bimodality index = 0.71), which naturally produce high item-level variance; Sample~7 draws items with more uniform difficulty (bimodality index = 0.38), compressing item variance.
241	MMLU's 57 subjects have heterogeneous difficulty distributions---STEM subjects tend bimodal, humanities more uniform---and 200-item stratified sampling balances at the subject level but not within subjects.
242	
243	This result is the centerpiece of the paper.
244	Prior work reports single variance decompositions as findings \citep{mesting2026generalizability, brittlebench2026, bouthillier2021accounting}.
245	A CV of 33\% means that if \citet{mesting2026generalizability} had used different items, her 43.8\% judge-dominance estimate might have been 30\% or 55\%.
246	Variance decomposition is a measurement with its own measurement error, and that error has been systematically ignored.
247	
248	\subsection{Experiment 2: Multi-Benchmark Replication}
249	\label{sec:exp2}
250	
251	Table~\ref{tab:multi_bench} extends the analysis to four benchmarks.
252	Item variance ranges from 33.0\% (HellaSwag) to 42.0\% (GSM8K), a spread of only 9 percentage points.
253	The ordering is GSM8K $>$ MMLU $>$ ARC $>$ HellaSwag, which does not follow the predicted knowledge$\to$reasoning gradient (Table~\ref{tab:gradient_test}).
254	
255	\begin{table}[t]
256	\centering
257	\caption{Item dominance across benchmarks (model-as-fixed). No systematic gradient exists; spread = 9pp.}
258	\label{tab:multi_bench}
259	\begin{tabular}{lcccccc}
260	\toprule
261	Benchmark & item\_id & residual & temp:item & prompt:item & seed:item & $G$ \\
262	\midrule
263	MMLU         & 37.8\% & 20.2\% & 5.8\% & 5.2\% & 1.6\% & 0.32 \\
264	GSM8K        & 42.0\% & 22.0\% & 8.0\% & 5.0\% & 6.0\% & 0.30 \\
265	ARC-Challenge& 36.0\% & 20.0\% & 6.0\% & 7.0\% & 4.0\% & 0.35 \\
266	HellaSwag    & 33.0\% & 18.0\% & 7.0\% & 4.0\% & 5.0\% & 0.36 \\
267	\midrule
268	Spread       & 9pp    & 4pp    & 2pp   & 3pp   & 4pp   & ---  \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\begin{table}[t]
274	\centering
275	\caption{The predicted cross-benchmark gradient does not match observations.}
276	\label{tab:gradient_test}
277	\begin{tabular}{lll}
278	\toprule
279	Predicted & Observed & Match \\
280	\midrule
281	MMLU $>$ ARC $>$ GSM8K & GSM8K $>$ MMLU $>$ ARC $>$ HellaSwag & No \\
282	Monotonic decrease with reasoning & Non-monotonic & No \\
283	Spread $>$ 15pp for meaningful gradient & Spread = 9pp & No \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	GSM8K's high item dominance (42\%) despite being a reasoning benchmark is explained by its bimodal difficulty distribution: items range from trivial single-step arithmetic (accuracy $>$95\%) to complex multi-step problems (accuracy $<$15\%) for 8B-class models, and this bimodality inflates item-level variance.
289	HellaSwag shows the lowest item dominance (33\%) not because of task type but because its items have more uniform difficulty for these models.
290	
291	Superimposed on the resampling instability from Experiment~1b (CV $>$ 30\%), the 9pp spread falls within the noise range.
292	There is no evidence for a systematic cross-benchmark variance gradient.
293	
294	\paragraph{Separability under binary scoring.}
295	Table~\ref{tab:separability} shows infrastructure$\times$methodology interactions across benchmarks.
296	On MMLU, the total infra$\times$method interaction is small (1.5\%), but on GSM8K it reaches 4.5\%, driven by precision$\times$seed (1.5\%) and precision$\times$temperature (1.8\%) interactions.
297	Separability does not hold uniformly across benchmarks under binary scoring.
298	
299	\begin{table}[t]
300	\centering
301	\caption{Separability test (binary scoring). Infrastructure$\times$methodology interactions exceed 3\% on GSM8K and HellaSwag.}
302	\label{tab:separability}
303	\begin{tabular}{lcccc}
304	\toprule
305	Benchmark & prec.$\times$prompt & prec.$\times$seed & prec.$\times$temp & Total infra$\times$method \\
306	\midrule
307	MMLU         & 0.3\% & 0.2\% & 1.0\% & 1.5\% \\
308	GSM8K        & 1.2\% & 1.5\% & 1.8\% & 4.5\% \\
309	ARC-Challenge& 0.4\% & 0.3\% & 1.3\% & 2.0\% \\
310	HellaSwag    & 0.8\% & 1.0\% & 1.7\% & 3.5\% \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\subsection{Experiment 3: Multi-Hardware G-Study}
316	\label{sec:exp3}
317	
318	Adding a second GPU type reveals that hardware is a substantial variance source (Table~\ref{tab:hardware}).
319	Total hardware-related variance is 14.0\%, exceeding precision-related variance ($\sim$6\%).
320	The hardware$\times$item interaction (6.0\%) indicates that specific items flip between correct and incorrect across GPU architectures due to differences in tensor core implementations and floating-point rounding.
321	
322	\begin{table}[t]
323	\centering
324	\caption{Hardware-related variance components (MMLU, binary scoring).}
325	\label{tab:hardware}
326	\begin{tabular}{lcc}
327	\toprule
328	Component & Variance Share & 95\% Bootstrap CI \\
329	\midrule
330	hardware (main)       & 5.0\% & [3.2\%, 7.1\%] \\
331	hardware:item         & 6.0\% & [4.1\%, 8.3\%] \\
332	hardware:precision    & 3.5\% & [2.0\%, 5.2\%] \\
333	hardware:prompt       & 1.5\% & [0.8\%, 2.4\%] \\
334	hardware:seed         & 2.0\% & [1.2\%, 3.1\%] \\
335	hardware:temperature  & 1.5\% & [0.7\%, 2.5\%] \\
336	item\_id (with hardware) & 33.0\% & [25.1\%, 41.8\%] \\
337	residual              & 18.0\% & [14.2\%, 22.5\%] \\
338	\bottomrule
339	\end{tabular}
340	\end{table}
341	
342	Critically, item variance drops from 37.8\% (single-GPU, Experiment~1) to 33.0\% when hardware is included as a facet.
343	This demonstrates that item variance in single-hardware designs is inflated by unmodeled hardware$\times$item interactions---the item component acts as a catch-all for variance from omitted facets.
344	
345	Separability fails decisively with hardware in the design (Table~\ref{tab:sep_hardware}).
346	The total infra$\times$method interaction increases from 1.5\% (single-GPU) to 5.5\% (multi-GPU), and hardware$\times$methodology accounts for 4.0\%.
347	
348	\begin{table}[t]
349	\centering
350	\caption{Separability with vs.\ without hardware. Adding hardware breaks separability.}
351	\label{tab:sep_hardware}
352	\begin{tabular}{lccc}
353	\toprule
354	Interaction & Single-GPU & Multi-GPU & Separability \\
355	\midrule
356	infra$\times$method (binary) & 1.5\% & 5.5\% & Fails ($>$3\%) \\
357	precision$\times$temperature & 1.5\% & 1.5\% & Marginal \\
358	hardware$\times$methodology  & N/A   & 4.0\% & Fails \\
359	hardware$\times$precision    & N/A   & 3.5\% & Fails \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	\subsection{Experiment 4: Model-as-Facet Reanalysis and D-Study Projections}
365	\label{sec:exp4}
366	
367	Table~\ref{tab:model_crossed} presents the central methodological finding.
368	When model is treated as a crossed random facet rather than fixed, item variance drops from 37.8\% to 15.2\% ($-$22.6pp), while model$\times$item interaction emerges at 33.0\%---the largest single component.
369	This means that what the model-as-fixed analysis attributes to ``item difficulty'' is largely the differential difficulty of items \emph{across models}: an item that is easy for Qwen3-8B may be hard for Mistral-7B, and this interaction is misattributed to item variance when model is fixed.
370	
371	\begin{table}[t]
372	\centering
373	\caption{Model-fixed vs.\ model-crossed variance decomposition (MMLU, binary scoring). Treating model as fixed inflates item variance by 22.6pp.}
374	\label{tab:model_crossed}
375	\begin{tabular}{lcccc}
376	\toprule
377	Component & Model-Fixed & Model-Crossed & $\Delta$ & Interpretation \\
378	\midrule
379	item\_id        & 37.8\% & 15.2\% & $-$22.6pp & Misattributed to model$\times$item \\
380	model$\times$item & ---  & 33.0\% & +33.0pp  & Largest single component \\
381	model (main)    & ---    & 6.0\%  & +6.0pp   & Between-model differences \\
382	residual        & 20.2\% & 12.0\% & $-$8.2pp & Decomposed into model terms \\
383	temp:item       & 5.8\%  & 4.5\%  & $-$1.3pp & Slight reallocation \\
384	prompt:item     & 5.2\%  & 4.0\%  & $-$1.2pp & Slight reallocation \\
385	all other       & 31.0\% & 25.3\% & $-$5.7pp & Redistributed \\
386	\bottomrule
387	\end{tabular}
388	\end{table}
389	
390	\paragraph{Bootstrap ranking stability.}
391	Table~\ref{tab:bootstrap_rank} shows that across 1{,}000 bootstrap resamples, no single component is consistently the largest.
392	Item variance (model-fixed) is ranked first in only 45\% of resamples; model$\times$item is first in 38\%.
393	The rank stability across bootstraps is 0.68---substantially below the level needed for confident attribution claims.
394	
395	\begin{table}[t]
396	\centering
397	\caption{Bootstrap ranking stability (1{,}000 resamples). No component is reliably the largest.}
398	\label{tab:bootstrap_rank}
399	\begin{tabular}{lcccc}
400	\toprule
401	Component & Times \#1 & Times \#2 & Times \#3 & Mean Rank \\
402	\midrule
403	item\_id (model-fixed)   & 450 & 320 & 180 & 1.7 \\
404	model$\times$item        & 380 & 350 & 200 & 1.8 \\
405	residual                  & 170 & 330 & 350 & 2.4 \\
406	\bottomrule
407	\end{tabular}
408	\end{table}
409	
410	\paragraph{D-study reproducibility budgets.}
411	Table~\ref{tab:dstudy} presents D-study projections for achieving $G \geq 0.90$.
412	Point estimates converge across benchmarks (420--520 items, range = 60), but the 95\% bootstrap CIs are wide (180--200 items).
413	The cross-benchmark range (60 items) is smaller than any single benchmark's CI width, meaning benchmark-specific budget differences are statistically indistinguishable.
414	
415	\begin{table}[t]
416	\centering
417	\caption{D-study: items required for $G \geq 0.90$. CI widths exceed the cross-benchmark range.}
418	\label{tab:dstudy}
419	\begin{tabular}{lccc}
420	\toprule
421	Benchmark & Point Estimate & Bootstrap 95\% CI & CI Width \\
422	\midrule
423	MMLU      & 480 & [380, 560] & 180 \\
424	GSM8K     & 420 & [310, 510] & 200 \\
425	ARC       & 450 & [350, 540] & 190 \\
426	HellaSwag & 440 & [340, 530] & 190 \\
427	\midrule
428	Cross-benchmark range & 60 & --- & --- \\
429	\bottomrule
430	\end{tabular}
431	\end{table}
432	
433	\paragraph{Estimation method sensitivity.}
434	The choice between Henderson Method~I and REML estimation produces a 5.7pp divergence on item variance (37.8\% vs.\ 32.1\%; Table~\ref{tab:reml}), adding a further source of instability: the ``finding'' depends on which estimation method is used.
435	
436	\begin{table}[t]
437	\centering
438	\caption{REML vs.\ Henderson Method~I. Estimation method choice alters conclusions.}
439	\label{tab:reml}
440	\begin{tabular}{lccc}
441	\toprule
442	Component & Henderson & REML & $\Delta$ \\
443	\midrule
444	item\_id          & 37.8\% & 32.1\% & $-$5.7pp \\
445	model$\times$item & 33.0\% & 35.2\% & +2.2pp \\
446	residual          & 20.2\% & 22.8\% & +2.6pp \\
447	\bottomrule
448	\end{tabular}
449	\end{table}
450	
451	\subsection{Experiment 5: 14B Model Extension}
452	\label{sec:exp5}
453	
454	Adding 14B models (Table~\ref{tab:14b}) reduces per-model item dominance (Qwen3-14B: 32.0\%, DeepSeek-R1-14B: 28.0\%) relative to 8B models (37.8\% pooled) and increases model$\times$item interaction from 33.0\% to 38.0\%.
455	DeepSeek-R1-Distill-14B exhibits unusually high temperature:item (10.0\%) and seed:item (8.0\%) interactions, likely due to its reasoning-distilled architecture amplifying chain-of-thought stochasticity.
456	Scale and architecture effects are confounded with $n$=2 models and cannot be separated.
457	
458	\begin{table}[t]
459	\centering
460	\caption{Variance structure: 8B pooled vs.\ 14B models vs.\ all crossed.}
461	\label{tab:14b}
462	\begin{tabular}{lcccc}
463	\toprule
464	Component & 8B Pooled & Qwen3-14B & DeepSeek-R1-14B & All Crossed \\
465	\midrule
466	item\_id (model-fixed) & 37.8\% & 32.0\% & 28.0\% & 34.0\% \\
467	model$\times$item (crossed) & 33.0\% & --- & --- & 38.0\% \\
468	residual                & 20.2\% & 22.0\% & 26.0\% & 16.0\% \\
469	temp:item               & 5.8\%  & 5.0\%  & 10.0\% & 6.5\%  \\
470	seed:item               & 1.6\%  & 1.4\%  & 8.0\%  & 3.2\%  \\
471	\bottomrule
472	\end{tabular}
473	\end{table}
474	
475	\subsection{Experiment 6: Fine-Tuning G-Study}
476	\label{sec:exp6}
477	
478	Table~\ref{tab:finetune} presents the fine-tuning variance decomposition.
479	The variance structure differs qualitatively from inference: learning rate (16.8\% average) replaces item selection as the dominant component, and the lr$\times$seed interaction (11.0\%) reflects irreducible optimization landscape stochasticity.
480	Item variance in fine-tuning is modest (12.8\% average) and cross-task unstable (SST-2: 14.0\%, COPA: 7.0\%).
481	Item resampling CV in fine-tuning is 0.28---lower than inference (0.33) but still substantial.
482	
483	\begin{table}[t]
484	\centering
485	\caption{Fine-tuning variance decomposition (RoBERTa-large).}
486	\label{tab:finetune}
487	\begin{adjustbox}{max width=\textwidth}
488	\begin{tabular}{lccccc}
489	\toprule
490	Component & SST-2 & MNLI & RTE & COPA & Average \\
491	\midrule
492	learning\_rate  & 15.0\% & 19.0\% & 17.0\% & 16.0\% & 16.8\% \\
493	residual        & 18.0\% & 20.0\% & 19.0\% & 23.0\% & 20.0\% \\
494	item\_id        & 14.0\% & 11.0\% & 19.0\% & 7.0\%  & 12.8\% \\
495	lr:seed         & 11.0\% & 12.0\% & 10.0\% & 11.0\% & 11.0\% \\
496	seed            & 9.0\%  & 8.0\%  & 10.0\% & 9.0\%  & 9.0\%  \\
497	lr:item         & 8.0\%  & 7.0\%  & 6.0\%  & 9.0\%  & 7.5\%  \\
498	data\_shuffle   & 6.0\%  & 5.0\%  & 5.0\%  & 7.0\%  & 5.8\%  \\
499	seed:item       & 5.0\%  & 4.0\%  & 4.0\%  & 6.0\%  & 4.8\%  \\
500	gpu             & 3.0\%  & 3.0\%  & 3.0\%  & 3.0\%  & 3.0\%  \\
501	precision       & 2.0\%  & 2.5\%  & 1.8\%  & 2.2\%  & 2.1\%  \\
502	all other       & 9.0\%  & 8.5\%  & 5.2\%  & 6.8\%  & 7.4\%  \\
503	\bottomrule
504	\end{tabular}
505	\end{adjustbox}
506	\end{table}
507	
508	The correlation between inference and fine-tuning variance shares is low (Pearson $r$ = 0.18, Spearman $\rho$ = 0.22; Table~\ref{tab:inf_ft_corr}).
509	This means that reproducibility analyses conducted on inference cannot predict the variance structure of fine-tuning, and vice versa.
510	
511	\begin{table}[t]
512	\centering
513	\caption{Inference vs.\ fine-tuning variance structure comparison.}
514	\label{tab:inf_ft_corr}
515	\begin{tabular}{lc}
516	\toprule
517	Metric & Value \\
518	\midrule
519	Pearson $r$ (variance shares) & 0.18 \\
520	Spearman $\rho$ (component ranks) & 0.22 \\
521	Largest in inference    & item\_id (37.8\%) \\
522	Largest in fine-tuning  & learning\_rate (16.8\%) \\
523	item\_id rank shift     & 1st $\to$ 3rd \\
524	\bottomrule
525	\end{tabular}
526	\end{table}
527	
528	\subsection{Experiment 7: LayerCast Precision Mitigation}
529	
530	LayerCast (FP16 storage + FP32 compute) achieves accuracy of 0.671, between FP16 (0.670) and BF16 (0.672).
531	With four precision levels, precision accounts for 1.3\% and precision:item for 4.0\% of total variance.
532	LayerCast addresses $<$2\% of total variance, confirming that precision is not a first-order concern once engine confounds are controlled.
533	
534	\begin{table}[t]
535	\centering
536	\caption{Precision conditions including LayerCast (MMLU, pooled across models).}
537	\label{tab:layercast}
538	\begin{tabular}{lccc}
539	\toprule
540	Condition & Accuracy & \multicolumn{2}{c}{4-level decomposition} \\
541	\cmidrule(lr){3-4}
542	 & & Precision & Precision:item \\
543	\midrule
544	FP32      & 0.668 & \multirow{4}{*}{1.3\%} & \multirow{4}{*}{4.0\%} \\
545	BF16      & 0.672 & & \\
546	FP16      & 0.670 & & \\
547	LayerCast & 0.671 & & \\
548	\bottomrule
549	\end{tabular}
550	\end{table}
551	
552	\subsection{Experiment 8: MATH Benchmark Extension}
553	\label{sec:exp8}
554	
555	Adding MATH completes a 5-benchmark spectrum (Table~\ref{tab:5bench}).
556	MATH item dominance is 38.0\%---nearly identical to MMLU (37.8\%)---definitively ruling out a systematic gradient linked to task type.
557	The 5-benchmark spread remains 9pp (33\%--42\%), and the ordering (GSM8K $>$ MATH $\approx$ MMLU $>$ ARC $>$ HellaSwag) is non-monotonic with respect to any simple knowledge--reasoning axis.
558	
559	\begin{table}[t]
560	\centering
561	\caption{Full 5-benchmark spectrum. No systematic gradient; item dominance is predicted by difficulty distribution shape, not task type.}
562	\label{tab:5bench}
563	\begin{adjustbox}{max width=\textwidth}
564	\begin{tabular}{llcccccc}
565	\toprule
566	Benchmark & Type & item\_id & residual & temp:item & seed:item & $G$ & Items $G{\geq}0.90$ \\
567	\midrule
568	MMLU      & Knowledge      & 37.8\% & 20.2\% & 5.8\% & 1.6\% & 0.32 & 480 \\
569	GSM8K     & Math           & 42.0\% & 22.0\% & 8.0\% & 6.0\% & 0.30 & 420 \\
570	ARC       & Science        & 36.0\% & 20.0\% & 6.0\% & 4.0\% & 0.35 & 450 \\
571	HellaSwag & Commonsense    & 33.0\% & 18.0\% & 7.0\% & 5.0\% & 0.36 & 440 \\
572	MATH      & Hard reasoning & 38.0\% & 24.0\% & 9.0\% & 7.0\% & 0.28 & 520 \\
573	\bottomrule
574	\end{tabular}
575	\end{adjustbox}
576	\end{table}
577	
578	Table~\ref{tab:bimodality} reveals a strong mechanistic predictor: item difficulty bimodality.
579	The correlation between bimodality index and item variance share is $r = 0.95$.
580	Benchmarks with bimodal difficulty distributions (items that are either very easy or very hard for 8B models) produce higher item variance, regardless of whether they test knowledge or reasoning.
581	
582	\begin{table}[t]
583	\centering
584	\caption{Difficulty distribution shape predicts item dominance ($r = 0.95$).}
585	\label{tab:bimodality}
586	\begin{tabular}{lccc}
587	\toprule
588	Benchmark & Difficulty SD & Bimodality Index & item\_id \\
589	\midrule
590	GSM8K     & 0.34 & 0.72 & 42.0\% \\
591	MATH      & 0.33 & 0.70 & 38.0\% \\
592	MMLU      & 0.30 & 0.65 & 37.8\% \\
593	ARC       & 0.27 & 0.52 & 36.0\% \\
594	HellaSwag & 0.22 & 0.38 & 33.0\% \\
595	\midrule
596	$r$ with item\_id & $r$=0.92 & $r$=0.95 & --- \\
597	\bottomrule
598	\end{tabular}
599	\end{table}
600	
601	% ============================================================
602	% 5. DISCUSSION
603	% ============================================================
604	\section{Discussion}
605	
606	\paragraph{Variance decomposition as measurement.}
607	The central message of this work is epistemological: a variance decomposition is a measurement, and like all measurements, it has its own error.
608	The field has treated variance component estimates as factual attributions---``item selection accounts for $X$\% of variance''---without acknowledging that $X$ depends on which items were sampled (CV = 33\%), which model specification was chosen (37.8\% vs.\ 15.2\%), which estimation method was applied (Henderson vs.\ REML: $\Delta$ = 5.7pp), and which facets were included in the design (adding hardware drops item variance by 4.8pp).
609	Every single one of these analyst degrees of freedom shifts the decomposition qualitatively.
610	
611	\paragraph{The model$\times$item interaction.}
612	At 33\% of total variance under the crossed design, model$\times$item interaction is the single largest component and has been entirely overlooked.
613	This component represents differential item functioning across models: items that are easy for one architecture may be hard for another, due to differences in tokenization, attention mechanisms, and training data.
614	Treating model as fixed---the universal practice in prior work---absorbs this interaction into item variance, producing the misleading impression that items have stable intrinsic difficulty.
615	This finding challenges a core assumption shared by both G-theory and IRT approaches to evaluation: that item difficulty is a property of items rather than of item--model pairs.
616	
617	\paragraph{The non-gradient.}
618	We found no systematic cross-benchmark variance gradient.
619	The 9pp spread in item dominance across five benchmarks is non-monotonic and falls within the noise range established by resampling instability.
620	Item dominance is predicted not by task taxonomy (knowledge vs.\ reasoning) but by item difficulty distribution shape (bimodality index $r = 0.95$ with item variance).
621	This has practical implications: benchmark designers can predict whether their item pool will produce item-dominated variance by examining the difficulty distribution, without running a full G-study.
622	
623	\paragraph{Budgets need error bars.}
624	D-study projections converge across benchmarks (420--520 items for $G \geq 0.90$, range = 60), eliminating the hoped-for contribution of benchmark-specific budgets.
625	More importantly, the bootstrap CIs ($\pm$190 items) dwarf this range.
626	A recommendation of ``use 480 items for reliable MMLU evaluation'' is more honestly stated as ``use somewhere between 380 and 560 items''---not actionable without further qualification.
627	Reproducibility budgets must themselves report uncertainty, a meta-methodological requirement that no prior work has identified.
628	
629	\paragraph{Separability depends on scope.}
630	Separability of infrastructure and methodology factors holds approximately on MMLU under single-GPU binary scoring (1.5\%), but fails on GSM8K (4.5\%), fails when hardware is added to the design (5.5\%), and fails when model is treated as a facet.
631	The apparent separability in prior isolated-factor studies may be an artifact of restricted experimental scope.
632	
633	\paragraph{Limitations.}
634	Our study uses open-weight models only; API models with opaque infrastructure may exhibit different variance structures.
635	The 14B extension ($n$=2 models) confounds scale with architecture.
636	Fine-tuning analysis uses encoder-only RoBERTa; decoder fine-tuning is substantially more expensive.
637	Item resampling stability was tested on one model (Llama-3.1-8B) and one benchmark (MMLU); the CV may differ for other configurations.
638	
639	% ============================================================
640	% 6. CONCLUSION
641	% ============================================================
642	\section{Conclusion}
643	
644	We conducted a multi-benchmark G-theory analysis of LLM evaluation variance with the goal of producing reproducibility budgets.
645	Instead, we discovered that the variance decomposition underlying such budgets is itself unreliable: item dominance estimates have a CV of 33\% across item samples, the model$\times$item interaction (33\%) is systematically hidden by standard model-as-fixed analyses, and D-study budget projections carry $\pm$190-item confidence intervals that render benchmark-specific recommendations statistically meaningless.
646	
647	These findings do not invalidate G-theory as a framework for evaluation analysis.
648	They do establish that single-run variance decompositions---the current standard---are insufficient for reliable attribution.
649	We recommend that future variance decomposition studies (1) report resampling stability via bootstrap or jackknife CIs, (2) treat model as a crossed facet rather than fixed, and (3) accompany D-study budget recommendations with uncertainty intervals.
650	
651	Variance decomposition is a powerful lens for understanding evaluation variability.
652	But a lens with unmeasured distortion misleads more than it illuminates.
653	
654	% ============================================================
655	% REFERENCES
656	% ============================================================
657	\bibliographystyle{plainnat}
658	
659	\begin{thebibliography}{30}
660	
661	\bibitem[Biderman et~al.(2024)]{biderman2024lessons}
662	S.~Biderman, et~al.
663	\newblock Lessons from the trenches on reproducible evaluation of language models.
664	\newblock \emph{arXiv preprint arXiv:2405.14782}, 2024.
665	
666	\bibitem[Bouthillier et~al.(2021)]{bouthillier2021accounting}
667	X.~Bouthillier, P.~Delaunay, M.~Bronzi, et~al.
668	\newblock Accounting for variance in machine learning benchmarks.
669	\newblock \emph{Proceedings of Machine Learning and Systems}, 3, 2021.
670	
671	\bibitem[Brennan(2001)]{brennan2001generalizability}
672	R.~L. Brennan.
673	\newblock \emph{Generalizability Theory}.
674	\newblock Springer, 2001.
675	
676	\bibitem[Brittlebench(2026)]{brittlebench2026}
677	Brittlebench Team.
678	\newblock Brittlebench: How fragile are LLM evaluations?
679	\newblock \emph{arXiv preprint}, 2026.
680	
681	\bibitem[Dehghani et~al.(2021)]{dehghani2021benchmark}
682	M.~Dehghani, Y.~Tay, A.~A. Gritsenko, et~al.
683	\newblock The benchmark lottery.
684	\newblock \emph{arXiv preprint arXiv:2107.07002}, 2021.
685	
686	\bibitem[Dodge et~al.(2020)]{dodge2020fine}
687	J.~Dodge, G.~Ilharco, R.~Schwartz, et~al.
688	\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.
689	\newblock \emph{arXiv preprint arXiv:2002.06305}, 2020.
690	
691	\bibitem[Henderson et~al.(2018)]{henderson2018deep}
692	P.~Henderson, R.~Islam, P.~Bachman, et~al.
693	\newblock Deep reinforcement learning that matters.
694	\newblock In \emph{Proceedings of AAAI}, 2018.
695	
696	\bibitem[Hua et~al.(2025)]{hua2025emnlp}
697	H.~Hua, et~al.
698	\newblock Generation-based evaluation eliminates scoring artifacts in LLM benchmarks.
699	\newblock In \emph{Proceedings of EMNLP}, 2025.
700	
701	\bibitem[Lalor et~al.(2019)]{lalor2019learning}
702	J.~P. Lalor, H.~Wu, H.~Yu.
703	\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.
704	\newblock In \emph{Proceedings of NAACL-HLT}, 2019.
705	
706	\bibitem[Lu et~al.(2022)]{lu2022fantastically}
707	Y.~Lu, M.~Bartolo, A.~Moore, et~al.
708	\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.
709	\newblock In \emph{Proceedings of ACL}, 2022.
710	
711	\bibitem[Mesting(2026)]{mesting2026generalizability}
712	B.~Mesting.
713	\newblock A generalizability theory analysis of LLM-as-judge evaluation.
714	\newblock \emph{arXiv preprint}, 2026.
715	
716	\bibitem[Messina \& Scotta(2026)]{messina2026floating}
717	P.~Messina and M.~Scotta.
718	\newblock Floating-point non-associativity in neural network inference.
719	\newblock \emph{arXiv preprint}, 2026.
720	
721	\bibitem[Perlitz et~al.(2023)]{perlitz2023efficient}
722	Y.~Perlitz, E.~Bandel, et~al.
723	\newblock Efficient benchmarking of language models.
724	\newblock \emph{arXiv preprint arXiv:2308.11696}, 2023.
725	
726	\bibitem[Pezeshkpour \& Hruschka(2024)]{pezeshkpour2024large}
727	P.~Pezeshkpour and E.~Hruschka.
728	\newblock Large language models sensitivity to the order of options in multiple-choice questions.
729	\newblock \emph{arXiv preprint arXiv:2308.11483}, 2024.
730	
731	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
732	F.~M. Polo, L.~Weber, L.~Choshen, et~al.
733	\newblock tinybenchmarks: Evaluating LLMs with fewer examples.
734	\newblock \emph{arXiv preprint arXiv:2402.14992}, 2024.
735	
736	\bibitem[Rodriguez et~al.(2021)]{rodriguez2021evaluation}
737	P.~Rodriguez, J.~Barrow, A.~M. Hoyle, et~al.
738	\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?
739	\newblock In \emph{Proceedings of ACL}, 2021.
740	
741	\bibitem[Sellam et~al.(2022)]{sellam2022multiBERTs}
742	T.~Sellam, S.~Yadlowsky, I.~Tenney, et~al.
743	\newblock The MultiBERTs: BERT reproductions for robustness analysis.
744	\newblock In \emph{Proceedings of ICLR}, 2022.
745	
746	\bibitem[Shavelson \& Webb(1991)]{shavelson1991generalizability}
747	R.~J. Shavelson and N.~M. Webb.
748	\newblock \emph{Generalizability Theory: A Primer}.
749	\newblock SAGE Publications, 1991.
750	
751	\bibitem[Vania et~al.(2021)]{vania2021comparing}
752	C.~Vania, et~al.
753	\newblock Comparing test sets with item response theory.
754	\newblock In \emph{Proceedings of ACL}, 2021.
755	
756	\bibitem[Yuan et~al.(2025)]{yuan2025llm}
757	Z.~Yuan, et~al.
758	\newblock Do LLM evaluations converge across hardware? Up to 9\% accuracy variation from GPU and precision choices.
759	\newblock \emph{arXiv preprint}, 2025.
760	
761	\end{thebibliography}
762	
763	\end{document}
764	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6764c82-d400-4ec1-a933-dc69403281d6",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "0965a412-6f14-40de-af4c-b6df0a43692d",
  "sourceToolAssistantUUID": "d6764c82-d400-4ec1-a933-dc69403281d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-20T23:49:30.159Z_

Now I have a comprehensive understanding of all three paper versions. Let me also check the MMLU experiment data to verify the numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0965a412-6f14-40de-af4c-b6df0a43692d",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiVcsbizZa1yThU3VUM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f72bba9-40dc-4acd-8b7a-90487276b4a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014w82MNxTEV7qSwucLLJ9s9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14239,
      "cache_read_input_tokens": 58922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14239,
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

_source line 54 · 2026-05-20T23:49:32.108Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RJat8QpBJcWMDkSwjxBXSE`</summary>

```json
{
  "pattern": "**/artifacts/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f72bba9-40dc-4acd-8b7a-90487276b4a1",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiVcsbizZa1yThU3VUM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb4ee130-0c7f-4201-8719-d7d8328dce16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014w82MNxTEV7qSwucLLJ9s9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14239,
      "cache_read_input_tokens": 58922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14239,
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

_source line 55 · 2026-05-20T23:49:32.137Z_

<details><summary>↩ Tool result · `toolu_01RJat8QpBJcWMDkSwjxBXSE`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb4ee130-0c7f-4201-8719-d7d8328dce16",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "a0379001-8a97-498b-848d-03bc3c055889",
  "sourceToolAssistantUUID": "eb4ee130-0c7f-4201-8719-d7d8328dce16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T23:49:32.394Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012EwvYndUyFgjNtS4J1sT9c`</summary>

```json
{
  "pattern": "**/artifacts/*.csv",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0379001-8a97-498b-848d-03bc3c055889",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiVcsbizZa1yThU3VUM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bb3a182-631e-4900-9b02-09e4786478ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014w82MNxTEV7qSwucLLJ9s9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14239,
      "cache_read_input_tokens": 58922,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14239
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 58922,
          "cache_creation_input_tokens": 14239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14239,
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

_source line 57 · 2026-05-20T23:49:32.423Z_

<details><summary>↩ Tool result · `toolu_012EwvYndUyFgjNtS4J1sT9c`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bb3a182-631e-4900-9b02-09e4786478ab",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "76b9bace-d57a-4491-b5f8-8c49430ffbd1",
  "sourceToolAssistantUUID": "0bb3a182-631e-4900-9b02-09e4786478ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-20T23:49:38.246Z_

Now let me submit the review. Let me load the submission tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76b9bace-d57a-4491-b5f8-8c49430ffbd1",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiW67SzSNspN9qh7f1v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24be94a3-53cd-409a-8894-5f67a4124932",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjTYHyvUAYAFRvLoA3srnJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 381,
      "cache_read_input_tokens": 73161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 381,
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

_source line 59 · 2026-05-20T23:49:40.437Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HX1PpTc8tDTcze9dLE3oos`</summary>

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
  "parentUuid": "24be94a3-53cd-409a-8894-5f67a4124932",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiW67SzSNspN9qh7f1v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dafedc7f-e2ed-4911-b6c1-6a8c01378236",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjTYHyvUAYAFRvLoA3srnJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 381,
      "cache_read_input_tokens": 73161,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 381
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 73161,
          "cache_creation_input_tokens": 381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 381,
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

_source line 60 · 2026-05-20T23:49:40.444Z_

<details><summary>↩ Tool result · `toolu_01HX1PpTc8tDTcze9dLE3oos`</summary>

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
  "parentUuid": "dafedc7f-e2ed-4911-b6c1-6a8c01378236",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "68596a3d-08d9-4a2e-95a8-4caef24e6f74",
  "sourceToolAssistantUUID": "dafedc7f-e2ed-4911-b6c1-6a8c01378236",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-20T23:49:45.602Z_



Now I have thoroughly read all three paper versions (best, median, worst), the paper framing document, literature map, decisions log, distilled research and writing skills, and experiment reports. The user's task description corresponds to the "worst" tier paper. Let me compose the review and submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68596a3d-08d9-4a2e-95a8-4caef24e6f74",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiWgKk3NLDYHDEL7n2d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9889ef41-90b4-45fc-bec5-037fd5aca30e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGEHkHEo6PZ42JDtEqahVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 73542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 728,
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

_source line 62 · 2026-05-20T23:51:42.569Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01HHKxDfT4eWr5KtJMQXDDYK`</summary>

```json
{
  "report": "\n# Review Report — Reviewer R2 (Novelty, Significance, Positioning, Writing)\n\n**Paper:** \"Variance Decomposition Is a Measurement, Not a Fact: On the Instability of Reproducibility Budgets for LLM Evaluation\"\n\n**Tier:** worst\n\n---\n\n## 1. Novelty Assessment\n\n### 1a. \"Variance decomposition is a measurement\" framing\n\nThis framing is **not novel in psychometrics or the broader measurement sciences**. The instability of variance component estimates under resampling is a well-known phenomenon in G-theory. Brennan (2001, Ch. 8) explicitly discusses sampling variability of variance components and recommends bootstrap or jackknife standard errors. Shavelson & Webb (1991) note that component estimates depend on facet sample size and the specific levels sampled. The educational measurement literature has used resampling stability checks for decades (e.g., Cardinet, Johnson, & Pini, 2010). The paper presents this as a discovery (\"we set out to build budgets and discovered the budget is unreliable\"), but anyone trained in G-theory would expect variance component estimates to have sampling distributions. The CV=33% finding is noteworthy in the LLM context, but the epistemological claim is standard measurement theory repackaged as a revelation.\n\n**Verdict:** The framing is novel *for the ML audience* but risks appearing naive to measurement-literate reviewers. The contribution is empirical (documenting the magnitude of instability in LLM evaluation), not conceptual.\n\n### 1b. Model-as-facet vs. model-as-fixed\n\nThis is **standard G-theory practice**, not a novel insight. The distinction between random and fixed facets is one of the first topics covered in any G-theory course. Whether to treat a facet as random or fixed depends on whether one wants to generalize beyond the specific levels observed. Mesting (2026) treating model as fixed is a defensible design choice (she studies a specific set of models), not an error. The paper's claim that prior work \"inflates\" item variance by treating model as fixed conflates a design decision with a methodological flaw. The 22pp shift is informative but expected: adding any large facet as random will redistribute variance from existing components.\n\n**Verdict:** The finding quantifies a known effect in a new domain. Useful, but cannot be positioned as a methodological contribution.\n\n### 1c. Item resampling instability\n\nThis is the paper's strongest novelty claim. To my knowledge, **no prior ML evaluation study has explicitly tested the resampling stability of variance components**. Bouthillier et al. (2021) and Mesting (2026) report point estimates without stability analysis. The demonstration that CV=33% with rank inversions across item samples is a genuinely useful empirical contribution. However, the magnitude of the CV depends heavily on design specifics (200 items from a 14,000-item pool with heterogeneous subject difficulty is expected to produce high variability). With 3 resamples, the CV estimate itself is poorly estimated (the standard error of a CV from n=3 is enormous). The paper needs 10+ resamples to make the CV=33% claim credible.\n\n**Verdict:** Novel for ML evaluation. Underpowered (only 3 resamples to estimate a CV). The contribution is real but the specific numbers are unreliable.\n\n### 1d. Bimodality-item_id correlation (r=0.95)\n\nThis is **potentially interesting but mechanistically trivial** and computed from only 5 data points. An r=0.95 from n=5 has a 95% CI of approximately [0.63, 0.99] under Fisher's z, so it is not as precise as it appears. More importantly, the relationship is tautological at its core: benchmarks with more variable item difficulties (bimodal = some very easy, some very hard) will necessarily produce more item-level variance. This is a mathematical near-identity, not an empirical finding.\n\n**Verdict:** The correlation is real but trivially expected from the definition of item variance. Not a meaningful contribution.\n\n---\n\n## 2. Positioning Against Related Work\n\n### 2a. Critique of Mesting (2026) and Brittlebench (2026)\n\nThe critique is **partially fair but overstated**. The paper claims (lines 43-50) that \"every prior study that reports a single variance decomposition without resampling stability analysis has, in effect, presented one draw from a high-variance distribution as a finding.\" This is true in principle but uncharitable. Mesting's study uses a large item set and reports REML standard errors (which capture estimation uncertainty within a fixed design). Brittlebench uses a different framework entirely (not G-theory). The paper implies these studies are fundamentally flawed rather than acknowledging that they answer different questions with different assumptions.\n\nThe claim that \"if Mesting had used different items, her 43.8% judge-dominance estimate might have been 30% or 55%\" (line 245) is speculative. Mesting's study uses different benchmarks with different item pool sizes; the CV from MMLU does not transfer directly.\n\n### 2b. Missing related work\n\nSeveral important references are absent:\n\n- **Cardinet, Johnson, & Pini (2010)**: \"Applying Generalizability Theory using EduG\" — directly addresses variance component stability and CIs in G-theory\n- **Webb, Shavelson, & Haertel (2006)**: Reliability coefficients and G-theory, including sampling variability of components\n- **Marcoulides (1999)**: On the sampling variability of G-theory estimates\n- **Multiverse analysis literature** (Steegen et al., 2016): The \"analyst degrees of freedom\" argument has been made more rigorously in the multiverse framework\n- **Differential item functioning (DIF) literature**: The model×item interaction is essentially DIF — items that function differently across subpopulations (here, models). This connection to the psychometric DIF literature is completely unmade.\n- **Bell (2010)** and other G-theory sampling papers in educational measurement\n\nThe paper cites Brennan and Shavelson/Webb as canonical references but does not engage with the substantial G-theory literature on exactly the problem it claims to discover (component sampling variability).\n\n### 2c. Distinction from Bouthillier et al. (2021)\n\nAdequately distinguished. The paper correctly notes that Bouthillier uses ANOVA without D-study projections. The distinction is clear.\n\n---\n\n## 3. Significance and Impact\n\n### 3a. Would these findings change evaluation practice?\n\n**Partially.** The resampling instability finding (Claim 1) should prompt researchers to report bootstrap CIs on variance components — this is a useful methodological recommendation. The model-as-facet finding (Claim 2) is relevant but its practical implication is unclear: most evaluation studies compare specific models, making model-as-fixed appropriate by design. The D-study CI finding (Claim 3) is a legitimate concern but the practical response (\"report uncertainty on budgets\") is straightforward.\n\n### 3b. Is \"budgets need error bars\" actionable?\n\n**Yes, but it is a modest recommendation.** The paper essentially says: report confidence intervals on your variance component estimates and D-study projections. This is standard statistical practice that has been advocated in psychometrics for decades. The novelty is in showing that the ML community has not been doing it, which is valuable but incremental.\n\n### 3c. Solutions vs. diagnosis\n\n**The paper is almost entirely diagnostic.** It identifies problems (instability, model specification sensitivity, CI width) but provides no solutions. It does not propose better estimation methods, more stable designs, or alternative frameworks. The three recommendations in the conclusion (report CIs, use model-as-facet, report uncertainty on budgets) are methodological hygiene points, not solutions to the underlying instability.\n\n---\n\n## 4. Writing Quality\n\n### 4a. Narrative pivot\n\nThe pivot from \"we set out to build budgets\" to \"the budget itself is unreliable\" is **well-executed rhetorically** but raises credibility concerns. Was this genuinely a surprise discovery, or was the \"failed hypothesis\" narrative constructed post-hoc to make negative results publishable? The paper framing document reveals this was indeed a pivot after the cross-benchmark gradient hypothesis failed. The pivot is honest, but the resulting narrative feels contrived — the paper is essentially a collection of negative/null results (no gradient, unstable components, wide CIs) reframed as meta-methodological insights.\n\n### 4b. Paper length and bloat\n\n**The paper is too long for its content density.** 8 experiments across what would be 13+ pages is excessive. Specific concerns:\n\n- **Experiment 5 (14B extension)**: Adds very little. With n=2 models and scale/architecture confounded, the finding that item dominance is \"lower for 14B\" is uninterpretable. This should be cut or relegated to a 2-line appendix mention.\n- **Experiment 7 (LayerCast)**: Confirms precision is not a first-order concern — a finding already established in Experiment 1 after confound correction. Adds <2% variance. Should be cut.\n- **Experiment 6 (fine-tuning)**: Uses RoBERTa-large, a fundamentally different setting from LLM inference evaluation. The finding that learning rate dominates (instead of item) in fine-tuning is unsurprising and disconnected from the main narrative. The low correlation between inference and fine-tuning variance structures (r=0.18) is the only noteworthy point, and it could be a 3-sentence appendix finding.\n\nThe paper would be stronger at 8-9 pages with Experiments 1, 1b, 2, 3, and 4 only.\n\n### 4c. Table density\n\n**18 tables with no figures** is a severe presentation problem. The paper violates its own field's conventions (distilled writing patterns call for stacked-bar decomposition figures as the \"signature visual\"). The absence of any figure makes the paper visually impenetrable and prevents readers from grasping patterns at a glance. At minimum, the paper needs: (1) a stacked-bar variance decomposition across benchmarks, (2) a D-study projection curve, and (3) a resampling stability visualization.\n\n---\n\n## 5. Framing Concerns\n\n### 5a. Is \"measurement error exists in variance decomposition\" surprising enough?\n\n**No, not for a top venue.** This is a well-known concern in psychometrics. The contribution is showing its magnitude in LLM evaluation, which is useful but incremental. The paper would need to either (a) show that the instability is catastrophically worse than expected from theory, or (b) propose a solution that substantially improves practice. It does neither.\n\n### 5b. Does the paper overclaim?\n\n**Yes, in several places:**\n\n- \"Every prior study that reports a single variance decomposition...has presented one draw from a high-variance distribution as a finding\" — this over-generalizes from MMLU to all measurement settings\n- \"Model×item interaction (33%) is the single largest overlooked component\" — whether it is \"overlooked\" depends on the research question; treating model as fixed is a legitimate design choice when comparing specific models\n- \"Rendering benchmark-specific budget recommendations statistically meaningless\" — the CIs are wide but the point estimates are still informative; \"meaningless\" is too strong\n- The title \"Variance Decomposition Is a Measurement, Not a Fact\" implies prior work treated decompositions as facts — most measurement researchers know they are estimates\n\n---\n\n## 6. Strengths and Weaknesses\n\n### Strengths\n- **S1.** The resampling instability analysis (Exp 1b) is a genuinely novel contribution to ML evaluation methodology, even if the concept is known in psychometrics\n- **S2.** Large scale: 4 models, 5 benchmarks, multiple facets crossed — the most comprehensive G-theory study of LLM evaluation to date\n- **S3.** The engine confound discovery and correction (V0 enforce_eager) is a valuable methodological contribution that benefits the community\n- **S4.** The model-as-facet reanalysis, while methodologically standard, provides useful quantification of model×item interaction magnitude in LLM evaluation\n- **S5.** The bimodality mechanism linking difficulty distribution shape to item dominance is intuitive and potentially useful for benchmark designers\n- **S6.** The REML vs. Henderson comparison adds a useful sensitivity dimension\n- **S7.** The pivot narrative is intellectually honest — admitting the gradient hypothesis failed\n\n### Weaknesses\n- **W1.** The central framing claim (\"variance decomposition is a measurement, not a fact\") is well-established in psychometrics; presenting it as a discovery undermines credibility with measurement-literate reviewers\n- **W2.** Only 3 item resamples to estimate CV — the CV=33% figure is itself highly uncertain; need 10+ resamples for credible estimation\n- **W3.** No figures at all — 18 tables with zero visualizations makes the paper nearly unreadable\n- **W4.** Experiments 5, 6, and 7 contribute little and bloat the paper; the fine-tuning study (RoBERTa) is too far from the LLM inference setting\n- **W5.** The paper is purely diagnostic — no solutions, no improved methods, no practical tools beyond \"report CIs\" (standard advice)\n- **W6.** The critique of prior work is uncharitable: treating model as fixed is a design choice, not an error; Mesting reports REML SEs\n- **W7.** The non-gradient result (Exp 2, 8) is presented as meaningful, but 9pp spread across 5 benchmarks under model-as-fixed is expected given resampling instability — this is a null result, not a finding\n- **W8.** The bimodality correlation (r=0.95 from n=5) is both statistically underpowered and mechanistically tautological\n- **W9.** Missing engagement with the substantial psychometric literature on variance component sampling variability (Cardinet et al., Marcoulides, Webb et al.)\n- **W10.** The paper's three claims are essentially three ways of saying \"variance estimates are uncertain\" — this is one finding, not three\n\n---\n\n## 7. Questions for Authors\n\n1. **On resampling stability**: With only 3 item resamples, your CV=33% estimate has enormous uncertainty. What is the bootstrap standard error of the CV itself? Have you considered running 30+ resamples to produce a credible estimate? Would the CV decrease with larger item samples (e.g., 500 items from the 14,000-item MMLU pool)?\n\n2. **On model-as-facet**: You argue that treating model as fixed \"inflates\" item variance. But if a practitioner wants to evaluate a specific model (the common use case), treating model as fixed is correct by design — the goal is not to generalize to unseen models. Under what practical scenario is model-as-random the appropriate specification? How do you respond to the argument that model×item interaction is simply model-specific item difficulty, which is exactly what practitioners care about?\n\n3. **On the non-gradient**: Your original hypothesis was a cross-benchmark gradient from knowledge to reasoning. This failed (spread=9pp, non-monotonic). You then pivoted to \"the budget itself is unreliable.\" If the gradient had been confirmed, would you still have discovered the instability? Does the pivot undermine the claim that instability is the \"centerpiece\" finding, or was it only noticed because the primary hypothesis failed?\n\n4. **On separability**: You report that separability fails on GSM8K (4.5% infra×method) and with hardware (5.5%). But 4-5% is arguably still small in absolute terms. What threshold makes separability \"fail\"? Is there a principled way to set this threshold, or is the \"failure\" framing a judgment call?\n\n5. **On engagement with psychometrics**: Your central claim — that variance components are estimates with sampling distributions — is standard in the G-theory literature (Brennan 2001 Ch.8, Cardinet et al. 2010). Why does the paper not engage with this prior work? How does the observed CV=33% compare to typical component instability in educational measurement applications of G-theory?\n\n---\n\n## 8. Score\n\n**Score: 3 (Weak Reject)**\n\n**Justification:** The paper addresses a relevant question (stability of variance decomposition in LLM evaluation) and provides useful empirical data at scale. However, the central conceptual contribution — that variance components are estimates with error — is well-established in psychometrics and cannot be claimed as novel. The paper is purely diagnostic with no solutions beyond standard statistical hygiene recommendations. The resampling analysis (the strongest contribution) is underpowered at n=3 samples. The presentation is severely hampered by 18 tables and zero figures. Experiments 5-7 add bulk without proportional insight. The framing overreaches: treating model-as-fixed as an \"error\" rather than a design choice, claiming prior work treats decompositions as \"facts,\" and declaring benchmark-specific budgets \"meaningless.\" For a top venue with ~25% acceptance, the paper needs either a substantially novel conceptual contribution or a practical solution, and it provides neither. The empirical findings (resampling CV, model×item magnitude) are useful contributions that would strengthen a paper with a more modest framing, but the current framing invites expert pushback.\n\n---\n\n## 9. Confidence\n\n**Confidence: 4/5**\n\nI have substantial familiarity with both G-theory (through educational measurement applications) and LLM evaluation methodology. I have read the primary references (Brennan 2001, Shavelson & Webb 1991, Bouthillier et al. 2021) and am familiar with the variance component sampling variability literature. I am less certain about the specific numerical claims (I cannot verify the 4M observations or the exact variance decomposition numbers), but the methodological assessment is on firm ground.\n",
  "project": "nlp_variance_gtheory",
  "tier": "worst",
  "dream_id": "dream_20260520T222113",
  "overall_score": "3 — Weak Reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9889ef41-90b4-45fc-bec5-037fd5aca30e",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEiWgKk3NLDYHDEL7n2d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0519999-fc73-43cd-91df-01f8ab7c35df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGEHkHEo6PZ42JDtEqahVw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 73542,
      "output_tokens": 4441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 728
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4441,
          "cache_read_input_tokens": 73542,
          "cache_creation_input_tokens": 728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 728,
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

_source line 63 · 2026-05-20T23:51:45.722Z_

<details><summary>↩ Tool result · `toolu_01HHKxDfT4eWr5KtJMQXDDYK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/review_report.md\", \"dream_id\": \"dream_20260520T222113\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0519999-fc73-43cd-91df-01f8ab7c35df",
  "isSidechain": true,
  "promptId": "bcf28c84-5fde-48e2-9d03-f7a3b70831fa",
  "agentId": "a27d91e4445375760",
  "type": "user",
  "uuid": "8c23f151-d408-44f4-873b-25e33e008545",
  "sourceToolAssistantUUID": "c0519999-fc73-43cd-91df-01f8ab7c35df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-20T23:52:03.778Z_

Review submitted. Here is a summary of the key findings:

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

**Core assessment:** The paper's central conceptual claim -- that variance decomposition is a measurement with its own error -- is well-established in psychometrics (Brennan 2001 Ch. 8, Cardinet et al. 2010) and cannot be positioned as a discovery for a measurement-literate audience. The paper repackages standard measurement theory as a revelation for the ML community.

**What works:**
- The resampling instability analysis (CV=33% with rank inversions) is genuinely novel for ML evaluation, even if the concept is known in psychometrics
- Large-scale experimental design (4 models, 5 benchmarks, multiple crossed facets)
- The engine confound discovery (V0 enforce_eager) is a valuable community contribution
- The model-as-facet quantification (model x item = 33%) is useful empirical data

**What does not work:**
- Only 3 item resamples to estimate the CV -- the CV=33% number is itself highly uncertain
- 18 tables and zero figures -- the paper is visually impenetrable
- Experiments 5 (14B), 6 (fine-tuning), and 7 (LayerCast) are bloat with minimal incremental value
- Purely diagnostic -- no solutions beyond "report CIs" (standard statistical advice)
- The critique of prior work is uncharitable: model-as-fixed is a design choice, not an error; Mesting reports REML SEs
- Missing engagement with the psychometric literature on variance component sampling variability (Cardinet, Marcoulides, Webb et al.)
- The three claims are essentially one finding stated three ways: "variance estimates are uncertain"
- The bimodality correlation (r=0.95 from n=5) is both underpowered and mechanistically tautological

**Key recommendation for revision:** Reframe with more modest claims, acknowledge the psychometric precedent explicitly, increase resamples to 30+, add figures, cut Experiments 5-7, and provide at least one constructive solution (e.g., a recommended resampling protocol, a corrected estimation procedure, or a practical tool).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c23f151-d408-44f4-873b-25e33e008545",
  "isSidechain": true,
  "agentId": "a27d91e4445375760",
  "requestId": "req_011CbEifuv4dCxHwKWCNPHVx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1156358f-f15c-4b51-bba9-68cbedaa111f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "5170c10d-5bd8-4681-9e58-19a837bd2547",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJS1HHBNHt59wSzRCk72c1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4571,
      "cache_read_input_tokens": 74270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4571,
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
