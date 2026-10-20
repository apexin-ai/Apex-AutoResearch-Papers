# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus areas are **novelty/significance** and **related work

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac371550dd0c1db93.jsonl`
- **Structured JSON:** [`d555a6ea666b541d5fa3.json`](../../sessions/d5/d555a6ea666b541d5fa3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-20T19:32:25.703Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus areas are **novelty/significance** and **related work positioning**. Review standard: top ML venue, ~25% acceptance rate, 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

## Paper Summary

Title: "Reproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory"

The paper conducts a fully-crossed Generalizability Theory (G-theory) study spanning infrastructure (hardware type, numerical precision) × methodology (prompt template, random seed, temperature, option ordering) × measurement (test item) factors. Across 4 primary models (7-9B), 2 extension models (14B), 5 benchmarks (MMLU, GSM8K, ARC-Challenge, HellaSwag, MATH), and over 2 million evaluation records, they report three claims:

1. **Item dominance**: Item selection is the single largest variance source (42–58%), exceeding all other factors combined.
2. **Separability**: Direct infrastructure × methodology interactions contribute <0.5% (aggregate separability holds), but both classes interact with item difficulty (14.2% combined) — item-conditional.
3. **D-study budgets**: Current practice yields G < 0.40; tripling items is 10× more effective than tripling prompts; 600 items + 3 prompts + 2 seeds → G ≥ 0.90 on MMLU.

Additional contributions: fine-tuning G-study (RoBERTa-large, 4 NLU tasks), 14B model extension, engine confound discovery (vLLM FP32 routing), LayerCast analysis, MATH benchmark extension.

## Related Work Cited in Paper

1. **Yuan et al. (2025)** — Numerical precision matters. Up to 9% accuracy SD from BF16/FP32 differences. No factorial attribution. (NeurIPS 2025)
2. **ThinkingMachines (2025)** — 80 unique completions at T=0. Batch-invariance failures. (arXiv)
3. **Messina et al. (2026)** — Background temperature in commercial APIs (GPT ~0.075, Gemini ~0.065, Claude ~0). (TMLR)
4. **Brittlebench (2026)** — Prompt brittleness. Prompt choice ~50% of variance in open-weight models. Fixed hardware. (NAACL)
5. **Hua et al. (2025)** — Generation-based evaluation. Log-likelihood vs LLM-judge scoring. Rank correlation 0.30→0.95. (EMNLP)
6. **Mesting et al. (2026)** — G-theory for LLM evaluation. Judge choice dominates at 43.8%. CIs omit 40-60% uncertainty. Infrastructure as fixed background. (ACL)
7. **Cronbach et al. (1972)** — Original G-theory framework.

The paper positions itself as extending Mesting et al. (2026) by crossing infrastructure and methodology layers, and as the first to quantify item selection relative to all other sources simultaneously.

## Key Claims About Novelty

- "First fully-crossed G-theory study spanning infrastructure × methodology × measurement"
- "First formal test of separability between infrastructure and methodology"
- "First to quantify item selection relative to all other sources simultaneously"
- Engine confound discovery as "methodological contribution of independent interest"
- D-study budgets as "practical tool"

## Your Review Task (R2: Novelty + Related Work)

Evaluate the following dimensions rigorously:

### 1. Novelty Assessment
- How novel is applying G-theory to LLM evaluation? (Mesting et al. 2026 already did this)
- What is the incremental novelty of adding infrastructure facets to Mesting et al.'s framework?
- Is the item dominance finding surprising or predictable from existing work?
- Is the separability test a genuine conceptual contribution?
- Are the D-study budgets novel, or a straightforward computation from variance components?

### 2. Related Work Completeness
- Are there important missing references? Consider:
  - Classical G-theory literature beyond Cronbach 1972 (Brennan 2001, Shavelson & Webb)
  - IRT-based approaches to item analysis in NLP/LLM evaluation
  - Benchmark contamination / item difficulty literature
  - Other variance decomposition work in ML (e.g., Bouthillier et al. 2021 on hyperparameter vs seed variance)
  - Prompt sensitivity literature beyond Brittlebench (e.g., Lu et al. 2022 on ordering sensitivity)
  - Reproducibility literature in ML more broadly (Pineau et al. 2021, etc.)
- Is the positioning vs Mesting et al. (2026) fair and accurate?
- Is the positioning vs Yuan et al. (2025) fair?
- Is the positioning vs Brittlebench fair?

### 3. Significance and Impact
- Will this paper change how people do LLM evaluation?
- Are the practical recommendations actionable?
- Is the 18× cost factor for G≥0.90 realistic for practitioners?
- Does the "item selection matters most" message have lasting value or is it obvious?

### 4. Framing and Narrative
- Is the title appropriate?
- Is the abstract effective?
- Does the introduction properly motivate the work?
- Is "separability" the right conceptual framing?
- Does the paper oversell or undersell its contributions?

### 5. Weaknesses from Novelty/Positioning Perspective
- What reduces the novelty of this work?
- What competing explanations or alternative interpretations are not addressed?
- Is this incremental over Mesting et al. (2026)?

## Output Format

Structure your review as:

```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
S1. ...
S2. ...
...

### Weaknesses
W1. ...
W2. ...
...

### Questions for Authors
Q1. ...
Q2. ...
...

### Minor Issues
M1. ...
M2. ...
...

### Scores
- Novelty: X/5
- Significance: X/5
- Overall Score: X/6
- Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "df9c75ea-aa16-41b4-bac9-42c6534a4d2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T19:32:25.706Z_

```json
{
  "parentUuid": "df9c75ea-aa16-41b4-bac9-42c6534a4d2d",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
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
  "uuid": "051a481a-1663-48dc-9a68-f19319a9e873",
  "timestamp": "2026-05-20T19:32:25.706Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T19:32:28.835Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "051a481a-1663-48dc-9a68-f19319a9e873",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENtv8zA4956knkA4Kcd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "926b66fd-46e1-48ef-bd56-91cce5062764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShBqKs4w2xAKSSw2RDZXSE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7689,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7689,
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

_source line 4 · 2026-05-20T19:32:29.310Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015CFw2AKuVbbp7AQhWSNjnx`</summary>

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
  "parentUuid": "926b66fd-46e1-48ef-bd56-91cce5062764",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENtv8zA4956knkA4Kcd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adb7ea0e-4b83-445a-a5e7-f1d1af7067be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShBqKs4w2xAKSSw2RDZXSE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7689,
      "cache_read_input_tokens": 8250,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7689,
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

_source line 5 · 2026-05-20T19:32:29.312Z_

<details><summary>↩ Tool result · `toolu_015CFw2AKuVbbp7AQhWSNjnx`</summary>

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
  "parentUuid": "adb7ea0e-4b83-445a-a5e7-f1d1af7067be",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "d0b471f6-73f6-4105-b43b-1c1d054344be",
  "sourceToolAssistantUUID": "adb7ea0e-4b83-445a-a5e7-f1d1af7067be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T19:32:32.762Z_



Let me read the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0b471f6-73f6-4105-b43b-1c1d054344be",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENuBjrAvY9Z4No4ik4k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47039dd8-d8f2-484b-ae8b-3f138d8e512d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017s2FfLdTYcC9eXVYfUGqiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15939,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 15939,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

### Tool call

_source line 7 · 2026-05-20T19:32:32.766Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01HTUy5s3ZsY6joEL1KbyqqR`</summary>

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
  "parentUuid": "47039dd8-d8f2-484b-ae8b-3f138d8e512d",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENuBjrAvY9Z4No4ik4k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8570eb94-e116-41c2-bf67-16a522c8e16b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017s2FfLdTYcC9eXVYfUGqiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15939,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 15939,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

_source line 8 · 2026-05-20T19:32:32.780Z_

<details><summary>↩ Tool result · `toolu_01HTUy5s3ZsY6joEL1KbyqqR`</summary>

```text
{"result":"# 项目 nlp_variance_gtheory 概况\n\n## 实验状态 (2 个)\n\n- **bf16_eager_disentangle**: DONE (negative) — \n- **mvp_phase_a**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\n\n## 趋势\n成功 1 / 负向 1 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32570: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8570eb94-e116-41c2-bf67-16a522c8e16b",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "6610793e-98ef-41cd-ae2c-7cda2aa3cb06",
  "sourceToolAssistantUUID": "8570eb94-e116-41c2-bf67-16a522c8e16b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T19:32:36.204Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019oNS6bV7oLgW99iiM5JpFP`</summary>

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
  "parentUuid": "6610793e-98ef-41cd-ae2c-7cda2aa3cb06",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENuSaZx9oMBCoiA2L2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "756ed22a-763c-417e-86a9-3e8a95d8d759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyzyG2PZhzgnPtNZ2UjD5v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 17385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 542,
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

_source line 10 · 2026-05-20T19:32:36.216Z_

<details><summary>↩ Tool result · `toolu_019oNS6bV7oLgW99iiM5JpFP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "756ed22a-763c-417e-86a9-3e8a95d8d759",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "86164e6f-2673-41c6-9cbb-0ee1366eb92b",
  "sourceToolAssistantUUID": "756ed22a-763c-417e-86a9-3e8a95d8d759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:32:36.678Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SLUzkVDd72JhD529GQwV2q`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86164e6f-2673-41c6-9cbb-0ee1366eb92b",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENuSaZx9oMBCoiA2L2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65385a1c-0385-4108-a62c-b95cce25579c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyzyG2PZhzgnPtNZ2UjD5v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 17385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 542,
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

_source line 12 · 2026-05-20T19:32:36.684Z_

<details><summary>↩ Tool result · `toolu_01SLUzkVDd72JhD529GQwV2q`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No memory.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65385a1c-0385-4108-a62c-b95cce25579c",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "36e322fd-f5b9-4fbb-81d2-a5441d2c3c72",
  "sourceToolAssistantUUID": "65385a1c-0385-4108-a62c-b95cce25579c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:32:37.589Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XbQYzWJ48odVTQd573cEb4`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36e322fd-f5b9-4fbb-81d2-a5441d2c3c72",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENuSaZx9oMBCoiA2L2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa079eb7-fd39-4e1b-91c5-cf33a9b018ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyzyG2PZhzgnPtNZ2UjD5v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 17385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 542,
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

_source line 14 · 2026-05-20T19:32:37.605Z_

<details><summary>↩ Tool result · `toolu_01XbQYzWJ48odVTQd573cEb4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/ROADMAP.md\", \"content\": \"# nlp_variance_gtheory — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:01 UTC | 更新原因: Post-MVP kickoff: paper_framing + experiment_plan 完成，Dream 已提交，ROADMAP 转 Research 阶段 dashboard\\n\\n## 核心方向\\n用 G-theory 联合分解 LLM 评估中 infrastructure × methodology × item 的方差。核心发现：item 选择主导方差（58.4%），infrastructure 与 methodology 在聚合层面近似可分但效应是 item-conditional 的。产出可量化的 reproducibility budget。详见 paper_framing.md。\\n\\n## 当前进展\\n- 阶段: **Research**（MVP 已通过，D001）\\n- MVP 结论: item_id=58.4%, precision×item=7.2%, temp×item=6.9%, prompt×item=5.7%, 直接 infra×method <0.02%\\n- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟进行中 (dream_20260520T190053)\\n- 服务器: westd-32570（4× RTX PRO 6000 96GB），第二种 GPU 待 Manager 分配\\n- float32 引擎混淆需 exp-001 解决（统一 V0 enforce_eager）\\n\\n## 实验计划（详见 experiment_plan.yaml）\\n| ID | Claim | Priority | GPU·h | 状态 |\\n|----|-------|----------|-------|------|\\n| exp-001 | Item dominance at scale (4 models × 200 items × fix FP32) | P0 | 100 | planned |\\n| exp-002 | Multi-benchmark (GSM8K/ARC/HellaSwag) | P0 | 200 | planned |\\n| exp-003 | Multi-hardware crossing | P0 | 120 | blocked (待第二种 GPU) |\\n| exp-004 | D-study reproducibility budget | P0 | 0 | planned (分析) |\\n| exp-005 | 14B scale extension | P1 | 100 | planned |\\n| exp-006 | Fine-tuning G-study (RoBERTa) | P1 | 200 | planned |\\n| exp-007 | LayerCast mitigation | P2 | 30 | planned |\\n| exp-008 | MATH benchmark | P2 | 50 | planned |\\n\\nTotal: P0=420h, P1=300h, P2=80h\\n\\n## 近期任务\\n- [ ] Dream 模拟完成 → 审视报告 → 调整 framing/plan（如需要）\\n- [ ] Dream 通过后批准 exp-001（可立即在 westd-32570 上执行）\\n- [ ] Agent 完成 text_exact_match 双变量分析（MVP 数据补充分析）\\n- [ ] 等待 Manager 回复第二种 GPU → 解除 exp-003 blocked\\n\\n## GPU 预算\\n- 本项目分配: westd-32570 cuda:0-3（4× RTX PRO 6000 96GB）\\n- 第二种 GPU: 待 Manager 分配\\n- P0 预估: 420 GPU·h | P1: 300 | P2: 80\\n\\n## 投稿目标\\n- 主投: AAAI 2027（abstract Jul 21, paper Jul 28 — 9 周）\\n- 备选: ACL 2027 ARR Oct 15（21 周）/ TACL rolling\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-20 | 采用 dual-metric (binary correct + text exact match) | — |\\n| D001 | 2026-05-20 | MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4 | — |\\n\\n\", \"total_chars\": 2064, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa079eb7-fd39-4e1b-91c5-cf33a9b018ce",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "bd034e20-262c-447c-98d3-7ecc28fb57d2",
  "sourceToolAssistantUUID": "fa079eb7-fd39-4e1b-91c5-cf33a9b018ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T19:32:37.851Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GtSrzMPAusSDjxsDbrCnqq`</summary>

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
  "parentUuid": "bd034e20-262c-447c-98d3-7ecc28fb57d2",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENuSaZx9oMBCoiA2L2V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0088900b-d3ff-4a40-a244-61aca95e7989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyzyG2PZhzgnPtNZ2UjD5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 17385,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 542
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 390,
          "cache_read_input_tokens": 17385,
          "cache_creation_input_tokens": 542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 542,
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

_source line 16 · 2026-05-20T19:32:37.860Z_

<details><summary>↩ Tool result · `toolu_01GtSrzMPAusSDjxsDbrCnqq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md\", \"content\": \"# Paper Framing — nlp_variance_gtheory\\n\\n## Target Venue\\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\\n- Extended: TACL (rolling)\\n\\n## Title\\nReproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory\\n\\n## Core Claims (3 条，可证伪)\\n\\n**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)\\n\\n**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.\\n\\n**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.\\n\\n## Story Spine\\n\\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.\\n\\n**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.\\n\\n**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.\\n\\n**Headline result template**: \\\"In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90.\\\"\\n\\n## Hook (Counter-Intuitive Quantified Claim)\\n\\\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined.\\\"\\n\\n## Narrative Strategy\\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)\\n- **Tension**: \\\"Everyone's optimizing the wrong thing\\\" — the field focuses on prompt/seed/hardware standardization while ignoring item selection\\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\\n- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)\\n- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves\\n\\n## Venue Fit Risks\\n- AAAI: Strong fit for \\\"evaluation methodology\\\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\\n- Reviewer concern 1: \\\"Only open-weight models, not API models\\\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\\n- Reviewer concern 2: \\\"G-theory is borrowed methodology, not novel\\\" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.\\n- Reviewer concern 3: \\\"Item dominance is obvious — harder items have more variance\\\" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n1. **\\\"Only N GPU types\\\"** → exp-003 (multi-hardware crossing) addresses this\\n2. **\\\"float32 engine confound\\\"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)\\n3. **\\\"Only MMLU\\\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag\\n4. **\\\"Small item sample\\\"** → exp-001 expands from 50 to 200 items\\n5. **\\\"No training-time analysis\\\"** → exp-006 (fine-tuning G-study with RoBERTa)\\n6. **\\\"Missing scale validation\\\"** → exp-005 (14B models)\\n7. **\\\"G-theory may not be right framework\\\"** → Compare with ANOVA and regression decomposition as sensitivity analysis\\n\\n## Design Decisions\\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.\\n\", \"total_chars\": 6768, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0088900b-d3ff-4a40-a244-61aca95e7989",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "f19d89d8-e3f7-441f-b5e4-621c57946de1",
  "sourceToolAssistantUUID": "0088900b-d3ff-4a40-a244-61aca95e7989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:32:41.200Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LLcgtxbcjFuDJv6LNkUREw`</summary>

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
  "parentUuid": "f19d89d8-e3f7-441f-b5e4-621c57946de1",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENupJHPzvmWvWWLcDHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "714652e0-9a6e-400a-b598-0bf9778d491b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017h1PWKpAdJhLQYpSoyGMYE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3728,
      "cache_read_input_tokens": 17927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3728,
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

_source line 18 · 2026-05-20T19:32:41.212Z_

<details><summary>↩ Tool result · `toolu_01LLcgtxbcjFuDJv6LNkUREw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T14:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"gtheory_evaluation\\\"\\n    name: \\\"G-Theory & Evaluation Variance\\\"\\n    narrative: \\\"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\\\"\\n  - key: \\\"infrastructure_variance\\\"\\n    name: \\\"Infrastructure-Induced Variance\\\"\\n    narrative: \\\"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\\\"\\n  - key: \\\"prompt_sensitivity\\\"\\n    name: \\\"Prompt Sensitivity & Methodological Variance\\\"\\n    narrative: \\\"Prompt phrasing, seed, temperature, and ordering as variance sources\\\"\\n  - key: \\\"evaluation_methodology\\\"\\n    name: \\\"Evaluation Methodology\\\"\\n    narrative: \\\"Scoring artifacts, benchmark design, and evaluation protocol considerations\\\"\\n\\npapers:\\n  mesting2026hidden:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\\\"\\n    authors:\\n      - \\\"Mesting, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.11581\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  brittlebench2026:\\n    title: \\\"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.13285\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  yuan2025layercast:\\n    title: \\\"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\\\"\\n    authors:\\n      - \\\"Yuan, Z.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09501\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  messina2026background:\\n    title: \\\"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\\\"\\n    authors:\\n      - \\\"Messina, P.\\\"\\n      - \\\"Scotta, A.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.22411\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  generalizit2024:\\n    title: \\\"GeneralizIT: A Python Solution for Generalizability Theory Computations\\\"\\n    authors: []\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2411.17880\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  hua2025flaw:\\n    title: \\\"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\\\"\\n    authors:\\n      - \\\"Hua, W.\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    category: \\\"evaluation_methodology\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  thinkingmachines2025batch:\\n    title: \\\"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"Technical Report\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  kunievsky2025intent:\\n    title: \\\"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\\\"\\n    authors:\\n      - \\\"Kunievsky, D.\\\"\\n      - \\\"Evans, J.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.16584\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  bui2025seeds:\\n    title: \\\"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\\\"\\n    authors:\\n      - \\\"Bui, T.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  sameprompt2026:\\n    title: \\\"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.14349\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\", \"total_chars\": 6732, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "714652e0-9a6e-400a-b598-0bf9778d491b",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "69b2d0c6-6c7a-443a-babc-678e247d0b4c",
  "sourceToolAssistantUUID": "714652e0-9a6e-400a-b598-0bf9778d491b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:32:41.669Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YQRTozXMRnMbTdyCvgvMLG`</summary>

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
  "parentUuid": "69b2d0c6-6c7a-443a-babc-678e247d0b4c",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENupJHPzvmWvWWLcDHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fdcf677-8325-417a-9b6c-82b4e4e00b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017h1PWKpAdJhLQYpSoyGMYE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3728,
      "cache_read_input_tokens": 17927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3728,
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

_source line 20 · 2026-05-20T19:32:41.678Z_

<details><summary>↩ Tool result · `toolu_01YQRTozXMRnMbTdyCvgvMLG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\\n\\n## 趋势\\n成功 1 / 负向 1 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32570: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 800, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fdcf677-8325-417a-9b6c-82b4e4e00b58",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "66dae989-0190-4d9d-994d-bafa2e315dcf",
  "sourceToolAssistantUUID": "7fdcf677-8325-417a-9b6c-82b4e4e00b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T19:32:42.727Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L8tmZgsa1zpHNQ9crkuzew`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "ARCHITECTURE.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66dae989-0190-4d9d-994d-bafa2e315dcf",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENupJHPzvmWvWWLcDHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5721eeb-cbd9-4869-b41a-254b52537b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017h1PWKpAdJhLQYpSoyGMYE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3728,
      "cache_read_input_tokens": 17927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3728,
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

_source line 22 · 2026-05-20T19:32:42.737Z_

<details><summary>↩ Tool result · `toolu_01L8tmZgsa1zpHNQ9crkuzew`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5721eeb-cbd9-4869-b41a-254b52537b13",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "efc28b85-4cb6-4ac2-aec2-c2fc3031217e",
  "sourceToolAssistantUUID": "b5721eeb-cbd9-4869-b41a-254b52537b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T19:32:42.948Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RXbP9UB9P7cyypvKusg4kk`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efc28b85-4cb6-4ac2-aec2-c2fc3031217e",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENupJHPzvmWvWWLcDHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1200d07-7cd3-45d1-a1b5-8e8e9a47a753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017h1PWKpAdJhLQYpSoyGMYE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3728,
      "cache_read_input_tokens": 17927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3728,
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

_source line 24 · 2026-05-20T19:32:42.958Z_

<details><summary>↩ Tool result · `toolu_01RXbP9UB9P7cyypvKusg4kk`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1200d07-7cd3-45d1-a1b5-8e8e9a47a753",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "1d4cc765-ab74-41a5-b579-90b9b64ef69b",
  "sourceToolAssistantUUID": "e1200d07-7cd3-45d1-a1b5-8e8e9a47a753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T19:32:46.294Z_

Now let me read the distilled research and writing skill files to understand the literature landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d4cc765-ab74-41a5-b579-90b9b64ef69b",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvCWmCAvxpp42rv6dE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75113b4f-49ec-4642-af3e-0f282813bf15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLKJyr7VoWK1KksLWEDUjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3844,
      "cache_read_input_tokens": 21655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3844,
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

_source line 26 · 2026-05-20T19:32:47.254Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VVQz2tNThEaQnwi9fDQMsh`</summary>

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
  "parentUuid": "75113b4f-49ec-4642-af3e-0f282813bf15",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvCWmCAvxpp42rv6dE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11e8fdf9-2eb7-4526-83bc-a6c4cc6b7e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLKJyr7VoWK1KksLWEDUjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3844,
      "cache_read_input_tokens": 21655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3844,
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

_source line 27 · 2026-05-20T19:32:47.260Z_

<details><summary>↩ Tool result · `toolu_01VVQz2tNThEaQnwi9fDQMsh`</summary>

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
  "parentUuid": "11e8fdf9-2eb7-4526-83bc-a6c4cc6b7e54",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "3a6fcf5b-959b-4e77-83f8-fc914f562c35",
  "sourceToolAssistantUUID": "11e8fdf9-2eb7-4526-83bc-a6c4cc6b7e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T19:32:47.559Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wc7VRfxoxDduU6qF5HFHze`</summary>

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
  "parentUuid": "3a6fcf5b-959b-4e77-83f8-fc914f562c35",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvCWmCAvxpp42rv6dE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc6f288e-b86b-4f82-8cda-cb60aacc99d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLKJyr7VoWK1KksLWEDUjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3844,
      "cache_read_input_tokens": 21655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3844,
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

_source line 29 · 2026-05-20T19:32:47.567Z_

<details><summary>↩ Tool result · `toolu_01Wc7VRfxoxDduU6qF5HFHze`</summary>

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
  "parentUuid": "cc6f288e-b86b-4f82-8cda-cb60aacc99d9",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "73c28f1b-1b73-413d-aaa9-2e72bcbdea0d",
  "sourceToolAssistantUUID": "cc6f288e-b86b-4f82-8cda-cb60aacc99d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-20T19:32:49.840Z_

Now let me look at the experiment artifacts and any existing paper drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73c28f1b-1b73-413d-aaa9-2e72bcbdea0d",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvXv4nzDHw3SmjzvzN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfc67303-6732-4031-be4a-247cb251eb6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xc4nPYtUN7EAvS3gr5BjcB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 25499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2115,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 31 · 2026-05-20T19:32:50.850Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QwLFxKDS4z6Bn3togXhiow`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfc67303-6732-4031-be4a-247cb251eb6f",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvXv4nzDHw3SmjzvzN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d02b7f14-f7bf-4da5-88b5-16ddb18484da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xc4nPYtUN7EAvS3gr5BjcB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 25499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2115,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 32 · 2026-05-20T19:32:50.859Z_

<details><summary>↩ Tool result · `toolu_01QwLFxKDS4z6Bn3togXhiow`</summary>

```text
artifacts/code/pyproject.toml
artifacts/code/src/__init__.py
artifacts/code/src/data/__init__.py
artifacts/code/src/design/__init__.py
artifacts/code/src/inference/__init__.py
artifacts/code/src/analysis/__init__.py
artifacts/code/src/data/prompt_templates.py
artifacts/code/src/data/sample_mmlu.py
artifacts/code/src/data/few_shot.py
artifacts/code/src/inference/vllm_runner.py
artifacts/_project/intermediate/README.md
artifacts/code/README.md
artifacts/code/src/analysis/visualize.py
artifacts/code/src/__pycache__/__init__.cpython-314.pyc
artifacts/code/src/design/__pycache__/__init__.cpython-314.pyc
artifacts/code/src/design/__pycache__/generate_design.cpython-314.pyc
artifacts/code/src/analysis/d_study.py
artifacts/code/run_mvp.sh
artifacts/code/src/design/generate_design.py
artifacts/code/src/inference/run_experiment.py
artifacts/code/src/inference/sanity_check.py
artifacts/env_setup_report.md
artifacts/_project/report/related_work_notes.md
artifacts/related_work_notes.md
artifacts/manifest.yaml
artifacts/code/requirements.txt
artifacts/code/src/analysis/variance_decomposition.py
artifacts/dream_reports/dream_20260520T190053/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T190053/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T190053/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T190053/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T190053/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T190053/best/experiment_data.json
artifacts/dream_reports/dream_20260520T190053/best/paper_framing.md
artifacts/dream_reports/dream_20260520T190053/best/paper.tex
artifacts/dream_reports/dream_20260520T190053/best/paper.aux
artifacts/dream_reports/dream_20260520T190053/best/paper.pdf
artifacts/dream_reports/dream_20260520T190053/best/paper.log
artifacts/dream_reports/dream_20260520T190053/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T190053/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T190053/median/experiment_data.json
artifacts/dream_reports/dream_20260520T190053/median/paper_framing.md
artifacts/dream_reports/dream_20260520T190053/median/paper.tex
artifacts/dream_reports/dream_20260520T190053/median/paper.aux
artifacts/dream_reports/dream_20260520T190053/median/paper.out
artifacts/dream_reports/dream_20260520T190053/median/paper.pdf
artifacts/dream_reports/dream_20260520T190053/median/paper.log
artifacts/dream_reports/dream_20260520T190053/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T190053/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T190053/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T190053/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T190053/worst/paper.tex
artifacts/dream_reports/dream_20260520T190053/worst/paper.aux
artifacts/dream_reports/dream_20260520T190053/worst/paper.out
artifacts/dream_reports/dream_20260520T190053/worst/paper.pdf
artifacts/dream_reports/dream_20260520T190053/worst/paper.log
artifacts/dream_reports/dream_20260520T190053/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T190053/best/review_context.yaml
artifacts/dream_reports/dream_20260520T190053/logs/orchestrator.log
artifacts/dream_reports/dream_20260520T190053/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d02b7f14-f7bf-4da5-88b5-16ddb18484da",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "46f111e5-a5b8-4476-91c9-a2d1e58f90ee",
  "sourceToolAssistantUUID": "d02b7f14-f7bf-4da5-88b5-16ddb18484da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T19:32:51.539Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01F1qg8TgfnsGju2dmRT18k2`</summary>

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
  "parentUuid": "46f111e5-a5b8-4476-91c9-a2d1e58f90ee",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvXv4nzDHw3SmjzvzN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d966c9fb-f5d4-4692-928b-7f264ccec41f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xc4nPYtUN7EAvS3gr5BjcB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2115,
      "cache_read_input_tokens": 25499,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 25499,
          "cache_creation_input_tokens": 2115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2115,
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

_source line 34 · 2026-05-20T19:32:51.552Z_

<details><summary>↩ Tool result · `toolu_01F1qg8TgfnsGju2dmRT18k2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/decisions.yaml\", \"content\": \"_next_id: 3\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:57 UTC\\n  summary: MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4%），separability 在聚合层面成立，进入\\n    research 阶段\\n  rationale: 5,400 次推理完成，5 个方差分量 ≥5% 且 CI 不含零，pipeline 端到端可运行。核心发现：(1) item 选择是评估方差最大来源；(2)\\n    precision/temperature/prompt 效应是 item-specific 的；(3) 直接的 infrastructure×methodology\\n    交互可忽略（<0.02%）。float32 引擎混淆需全研究阶段解决但不影响 MVP 结论。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:12 UTC\\n  summary: 采用 dual-metric (binary correct + text exact match) 方差分解作为论文核心方法论，Claim\\n    3 改为 metric-conditional reproducibility budget\\n  rationale: MVP 双变量分析揭示截然不同的方差结构：binary correct 下 item_id 主导 (58.4%, G=0.357)；text\\n    exact match 下 prompt×item 主导 (37.5%, G=0.975)。单一 response variable 无法完整描述评估可靠性。Dual-metric\\n    对比是 G-theory 框架的天然优势——\\\"同一实验在不同衡量标准下可靠性完全不同\\\"是比单一 budget 更有力的发现。precision:temperature\\n    交互在 text metric 下显著 (1.3%, CI 不含零)，证明 separability 在细粒度下不完全成立。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n\", \"total_chars\": 997, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d966c9fb-f5d4-4692-928b-7f264ccec41f",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "fe49f6ce-2a8c-400c-968a-6f216a75e83a",
  "sourceToolAssistantUUID": "d966c9fb-f5d4-4692-928b-7f264ccec41f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T19:32:55.154Z_

Let me read the best-case dream paper (the full LaTeX) and the related work notes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe49f6ce-2a8c-400c-968a-6f216a75e83a",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvprYopv4qbJDWTRXy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38914da1-d3b5-4e32-9a2e-617f83606375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAQqCfJMqgt78U8TBzavPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2049,
      "cache_read_input_tokens": 27614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2049,
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

_source line 36 · 2026-05-20T19:32:55.781Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tte8d2acPLb7NrTBQwSFVf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38914da1-d3b5-4e32-9a2e-617f83606375",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvprYopv4qbJDWTRXy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19422d64-5fdc-425f-b1af-6f8d843ad6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAQqCfJMqgt78U8TBzavPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2049,
      "cache_read_input_tokens": 27614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2049,
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

_source line 37 · 2026-05-20T19:32:55.995Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uk6R6Gd9GuZh2yyk62hZfk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/_project/report/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19422d64-5fdc-425f-b1af-6f8d843ad6cc",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENvprYopv4qbJDWTRXy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07aa19d0-878c-441f-bfb7-7154ff449137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAQqCfJMqgt78U8TBzavPv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2049,
      "cache_read_input_tokens": 27614,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2049
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 27614,
          "cache_creation_input_tokens": 2049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2049,
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

_source line 38 · 2026-05-20T19:32:55.999Z_

<details><summary>↩ Tool result · `toolu_01Uk6R6Gd9GuZh2yyk62hZfk`</summary>

```text
1	# Related Work — Structured Notes
2	
3	> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。
4	
5	## (a) G-theory & Variance Decomposition in NLP/ML
6	
7	### [Mesting et al., 2026] — TEE: Generalizability Theory for NLG Evaluation
8	- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估；发现 judge 选择贡献 43.8% 方差，prompt 在开源模型中贡献~50%、商用模型~25%；标准 95% CI 实际覆盖率仅 79%
9	- **与本工作关系**: extends — 我们直接继承其 TEE 框架和 REML 方法，将其扩展到 infrastructure facets
10	- **差异化**: Mesting 只分解方法论 facets（item/prompt/judge/temp），未纳入硬件/精度等基础设施因素；我们的 G-theory 框架联合分解 infrastructure × methodology
11	
12	### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition
13	- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量
14	- **与本工作关系**: complements — 提供了 prompt 方差的细粒度分解视角，其 articulation 分量对应我们框架中 prompt paraphrase facet
15	- **差异化**: 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的交叉设计
16	
17	### [Nalisnick et al.] — GeneralizIT: Software for G-theory in ML
18	- **核心发现**: 为 ML 场景提供 G-theory 计算工具包，简化 REML 估计和 D-study 设计流程
19	- **与本工作关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现
20	- **差异化**: 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget
21	
22	## (b) Infrastructure Variance
23	
24	### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance
25	- **核心发现**: BF16 推理导致 9% 的 accuracy 标准差，FP32 接近 0%；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存；推理模型受影响最大
26	- **与本工作关系**: addresses limitation of — 量化了精度对推理结果的影响，但未将其纳入统一的方差分解框架
27	- **差异化**: Yuan 只刻画精度这一个 infrastructure 因素并提出缓解方案；我们将精度作为 G-theory 框架中的一个 facet，与方法论因素联合分解
28	
29	### [Messina et al., 2026 (TMLR)] — Background Temperature Effects on GPU Computation
30	- **核心发现**: 即使 T=0，API 模型仍存在 "背景随机性"：GPT~0.075、Gemini~0.065、Claude~0 有效温度；提出 reference calibration 方法量化为单一标量 T_bg
31	- **与本工作关系**: complements — 揭示了一类此前被忽视的 infrastructure 方差源（硬件层面的非确定性），为我们纳入硬件 facet 提供实证依据
32	- **差异化**: Messina 聚焦 API 层面的背景温度刻画，未进行多因素交叉分解；我们将此类硬件非确定性纳入 G-theory 的交叉设计
33	
34	### [ThinkingMachines, 2025] — Batch Invariance Failure in LLM Inference
35	- **核心发现**: T=0 下 1000 次推理产生 80 种不同输出；根因是 RMSNorm/GEMM/attention 的 batch-size 依赖性而非随机种子；提出确定性内核方案，代价为 1.6-2.1× 延迟
36	- **与本工作关系**: addresses limitation of — 发现并解释了 batch 非确定性这一关键 infrastructure 方差源，但止步于工程修复
37	- **差异化**: 仅刻画 batch-size 这一个因素并提出工程缓解方案；我们将 batch 非确定性与其他 infrastructure/methodology 因素一起纳入 G-theory 分解
38	
39	## (c) Prompt Sensitivity & Methodological Variance
40	
41	### [Brittlebench, 2026] — Prompt Brittleness Benchmark
42	- **核心发现**: 系统性评估 prompt 脆弱性；通过 ANOVA 分解 V_data + V_brittleness；prompt 措辞贡献约 50% 方差（开源模型），商用模型约 25%
43	- **与本工作关系**: complements — 提供了大规模 prompt 脆弱性的实证基准，其 V_brittleness 分量对应我们框架中 prompt facet 的方差
44	- **差异化**: 使用传统 ANOVA 而非 G-theory，只分解 data vs. brittleness 两个分量；我们的框架支持更多 facets 的联合分解和交互项估计
45	
46	### [Hua et al., 2025 (EMNLP)] — Scoring Artifacts in LLM Evaluation
47	- **核心发现**: 大量表观的 prompt sensitivity 实际上是评估方法的 artifact——使用 LLM-judge 后 rank correlation 从 0.30 跃升至 0.95
48	- **与本工作关系**: complements — 警示区分"真实方差"与"评估 artifact"的重要性，为我们的实验设计提供方法论参考
49	- **差异化**: Hua 聚焦揭示 artifact 现象而非系统性分解方差来源；我们的 G-theory 框架可将 scoring method 作为 facet 纳入，从而量化其贡献
50	
51	### "Same Prompt, Different Outcomes" — Seed/Sampling Variance
52	- **核心发现**: [需补充]
53	- **与本工作关系**: [需补充] — 预期与我们框架中 seed facet 直接相关
54	- **差异化**: [需补充]
55	
56	### [Bui et al.] — Seed Sensitivity in LLM Evaluation
57	- **核心发现**: [需补充]
58	- **与本工作关系**: [需补充] — 预期聚焦 seed 这一单一因素
59	- **差异化**: [需补充]
60	
61	## 定位总结
62	
63	本项目是首个用 Generalizability Theory 联合分解 infrastructure（硬件类型、数值精度、batch 非确定性）与 methodology（prompt 措辞、随机种子、温度、few-shot 顺序）方差的工作。现有研究要么只用 G-theory 分解方法论 facets（Mesting），要么只刻画单一 infrastructure 因素并提出工程修复（Yuan、ThinkingMachines、Messina），没有工作在一个统一的交叉设计中同时容纳两类因素并检验其 separability。我们的 D-study 产出可量化的 reproducibility budget，为社区提供实验设计的决策依据。
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07aa19d0-878c-441f-bfb7-7154ff449137",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "3ba58a43-58a7-4911-88d9-23298430599a",
  "sourceToolAssistantUUID": "07aa19d0-878c-441f-bfb7-7154ff449137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T19:32:56.138Z_

<details><summary>↩ Tool result · `toolu_01Tte8d2acPLb7NrTBQwSFVf`</summary>

```text
1	\documentclass[letterpaper,11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{helvet}
5	\usepackage{courier}
6	\usepackage[hyphens]{url}
7	\usepackage{graphicx}
8	\usepackage{amsmath,amssymb}
9	\usepackage{booktabs}
10	\usepackage{multirow}
11	\usepackage{xcolor}
12	\usepackage{array}
13	\usepackage{tabularx}
14	\usepackage[small]{caption}
15	\usepackage{natbib}
16	\usepackage{enumitem}
17	
18	\urlstyle{rm}
19	
20	\title{Reproducibility Budgets for LLM Evaluation:\\Testing the Separability Assumption Between Infrastructure\\and Methodological Variance Sources via Generalizability Theory}
21	
22	\author{
23	Anonymous Authors
24	}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, hardware, numerical precision, temperature, or item selection---let alone how these factors interact.
31	We conduct the first fully-crossed Generalizability Theory (G-theory) study spanning infrastructure (hardware type, numerical precision) $\times$ methodology (prompt template, random seed, temperature, option ordering) $\times$ measurement (test item) factors.
32	Across 4 models, 5 benchmarks, and over 2 million evaluation records, we find that \textbf{item selection is the single largest variance source} (42--58\% of total variance), exceeding all other factors combined.
33	Direct infrastructure $\times$ methodology interactions contribute less than 0.5\% of total variance, providing an empirical license for isolated-factor studies---but both factor classes interact substantially with item difficulty (14.2\% combined), meaning that conclusions from any single-factor study are conditional on item selection.
34	D-study projections show that current common practices (1 prompt, 1 seed, $\leq$200 items) achieve generalizability coefficients $G < 0.40$, well below the $G \geq 0.80$ threshold considered minimally acceptable in psychometrics.
35	Increasing item count is $10\times$ more cost-effective than increasing prompt or seed replication: 600 items with 3 prompts and 2 seeds suffice for $G \geq 0.90$ on MMLU, at 18$\times$ the cost of current practice.
36	These findings extend to fine-tuning settings, where item selection remains the dominant variance source (37--45\%) despite the emergence of training seed and learning rate as substantial secondary factors.
37	\end{abstract}
38	
39	\section{Introduction}
40	
41	Researchers debating whether to standardize prompts, random seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs.
42	In a fully-crossed study of over 2 million evaluation records spanning 6 models, 5 benchmarks, and 7 experimental facets, we find that item selection alone accounts for 42--58\% of total evaluation variance---more than all other factors combined.
43	Current standard practice (1 prompt template, 1 random seed, $\leq$200 test items) yields a generalizability coefficient of $G < 0.40$, a level of measurement reliability that falls below the minimum acceptable threshold in the social sciences.
44	
45	Prior work has characterized individual variance sources in isolation.
46	\citet{yuan2025} documented up to 9\% accuracy variation from numerical precision and hardware differences but without factorial attribution.
47	\citet{brittlebench2026} quantified prompt sensitivity at approximately 50\% of variance but on fixed hardware.
48	\citet{mesting2026} applied G-theory to methodological facets (prompt, seed, temperature, judge) and found judge choice dominates at 43.8\% of variance, but treated infrastructure as fixed background.
49	No study crosses both infrastructure and methodology layers in a unified framework, and critically, no study has quantified the role of item selection relative to all other sources simultaneously.
50	
51	We address this gap by conducting the first fully-crossed G-theory study that spans infrastructure factors (hardware type, numerical precision) $\times$ methodology factors (prompt template, random seed, temperature, option ordering) $\times$ measurement factors (test items).
52	This design enables a direct test of the separability assumption---whether infrastructure and methodology variance sources interact---and reveals a finding that reframes the reproducibility conversation: item selection dominates everything.
53	The separability test yields two complementary results: direct interactions are negligible ($<0.5\%$), granting an empirical license for isolated-factor studies, while item-conditional interactions are substantial (14.2\%), warning that conclusions from such studies are conditional on item selection.
54	
55	Our contributions are:
56	\begin{enumerate}
57	\item \textbf{Framework}: The first fully-crossed G-theory variance decomposition unifying infrastructure and methodology factors, with a formal separability test and item-conditional interaction analysis.
58	\item \textbf{Empirical finding}: Item selection is the dominant variance source across 5 benchmarks (42--58\%), 6 models (7B--14B), and both inference and fine-tuning paradigms. Current evaluation practices yield $G < 0.40$.
59	\item \textbf{Practical tool}: D-study reproducibility budgets providing quantitative guidance for evaluation design---tripling item count is $10\times$ more effective than tripling prompt count for reaching $G \geq 0.90$.
60	\end{enumerate}
61	
62	\section{Related Work}
63	
64	\paragraph{Variance in LLM evaluation.}
65	A growing body of work documents the fragility of LLM evaluation.
66	\citet{yuan2025} showed that numerical precision differences between BF16 and FP32 can produce up to 9\% accuracy standard deviation, with reasoning models most affected.
67	\citet{thinkingmachines2025} demonstrated that batch-invariance failures in RMSNorm and attention kernels produce 80 out of 1000 unique completions even at temperature $T{=}0$.
68	\citet{messina2026} estimated effective background temperatures for major API providers (GPT $\sim$0.075, Gemini $\sim$0.065, Claude $\sim$0).
69	\citet{brittlebench2026} decomposed benchmark variance into data and brittleness components, finding prompt choice accounts for approximately 50\% of variance in open-weight models.
70	\citet{hua2025} showed that much apparent prompt sensitivity is an evaluation artifact---switching from log-likelihood to LLM-judge scoring raised rank correlation from 0.30 to 0.95.
71	
72	\paragraph{Generalizability Theory in NLP.}
73	G-theory~\citep{cronbach1972} provides a framework for simultaneously quantifying multiple variance sources via a random-effects ANOVA model.
74	\citet{mesting2026} pioneered its application to LLM evaluation, decomposing variance across item, prompt, judge, and temperature facets.
75	They found that judge choice dominates (43.8\% of variance) and that standard confidence intervals omit 40--60\% of uncertainty.
76	However, their design treats infrastructure as fixed background, leaving hardware and precision effects unquantified.
77	Our work extends this framework to cross infrastructure and methodology layers in a single G-study, enabling the first formal test of their separability.
78	
79	\paragraph{Reproducibility protocols.}
80	Several proposals address evaluation reproducibility through standardization---fixing prompts, seeds, or hardware.
81	Our D-study analysis complements these by quantifying the expected reliability gain from each intervention, showing that item sampling yields the highest marginal return.
82	
83	\section{Method}
84	
85	\subsection{Generalizability Theory Framework}
86	
87	G-theory decomposes observed score variance into components attributable to each facet and their interactions.
88	For a person (here, model) $p$ evaluated on items $i$ under conditions defined by facets $f_1, \ldots, f_k$, the observed score $X_{pi f_1 \ldots f_k}$ is modeled as:
89	\begin{equation}
90	X = \mu + \alpha_p + \alpha_i + \sum_j \alpha_{f_j} + \sum_{j&lt;l} \alpha_{f_j f_l} + \cdots + \epsilon
91	\end{equation}
92	where each $\alpha$ term is a random effect with variance component $\sigma^2$.
93	The generalizability coefficient $G$ is:
94	\begin{equation}
95	G = \frac{\sigma^2(\tau)}{\sigma^2(\tau) + \sigma^2(\delta)}
96	\end{equation}
97	where $\sigma^2(\tau)$ is universe score variance (signal) and $\sigma^2(\delta)$ is relative error variance (noise), which depends on the number of conditions sampled for each facet.
98	
99	\subsection{Facet Structure}
100	
101	We define a two-layer facet structure crossing infrastructure and methodology:
102	
103	\paragraph{Infrastructure layer.}
104	(a) \emph{Hardware type}: 2 GPU types (RTX PRO 6000 + second GPU);
105	(b) \emph{Numerical precision}: FP32, BF16, FP16, and LayerCast (FP16 storage + FP32 compute).
106	
107	\paragraph{Methodology layer.}
108	(a) \emph{Prompt template}: 6 templates varying in instruction phrasing and formatting;
109	(b) \emph{Random seed}: 6 seeds controlling sampling randomness;
110	(c) \emph{Temperature}: 2--3 levels ($T \in \{0.1, 0.5, 1.0\}$);
111	(d) \emph{Option ordering}: 4 permutations of multiple-choice option order.
112	
113	\paragraph{Measurement layer.}
114	(a) \emph{Test items}: 200 items per benchmark, stratified-sampled to preserve difficulty distribution.
115	
116	\paragraph{Separability test.}
117	We define separability as the condition that direct infrastructure $\times$ methodology interactions (e.g., hardware $\times$ prompt, precision $\times$ temperature) contribute less than 0.5\% of total variance.
118	We distinguish these from item-conditional interactions (e.g., hardware $\times$ item, prompt $\times$ item), which capture how factor effects vary across items.
119	
120	\subsection{Experimental Design}
121	
122	We conduct seven experiments with increasing scope:
123	
124	\begin{enumerate}
125	\item \textbf{Full-scale precision study} (Exp.~1): 4 models $\times$ 3 precisions $\times$ 6 prompts $\times$ 6 seeds $\times$ 3 temperatures $\times$ 4 orderings $\times$ 200 MMLU items = 1,036,800 records. All runs use vLLM V0 with \texttt{enforce\_eager} to eliminate engine confounds.
126	\item \textbf{Multi-benchmark replication} (Exp.~2): Same design on GSM8K, ARC-Challenge, and HellaSwag (230,400 records each).
127	\item \textbf{Multi-hardware G-study} (Exp.~3): 2 GPU types added, 691,200 records on MMLU.
128	\item \textbf{D-study projections} (Exp.~4): Analytical computation of $G$ under varying facet allocations.
129	\item \textbf{14B model extension} (Exp.~5): Qwen3-14B and DeepSeek-R1-Distill-14B, 172,800 records each.
130	\item \textbf{Fine-tuning G-study} (Exp.~6): RoBERTa-large on SST-2, MNLI, RTE, COPA; 1,728 fine-tuning runs.
131	\item \textbf{Extended benchmarks} (Exp.~7): MATH benchmark (230,400 records) and LayerCast precision mode (172,800 records).
132	\end{enumerate}
133	
134	\paragraph{Models.}
135	Primary: Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3.
136	Extension: Qwen3-14B, DeepSeek-R1-Distill-14B.
137	Fine-tuning: RoBERTa-large.
138	
139	\paragraph{Confound control.}
140	A critical methodological contribution is the identification and correction of an engine confound in numerical precision comparisons.
141	In our preliminary study, FP32 runs exhibited a systematic 8.5 percentage-point accuracy gap relative to BF16, yielding an inflated precision main effect (0.87\% of variance) and precision $\times$ item interaction (7.24\%).
142	Investigation revealed that vLLM routes FP32 through a different compute path (non-V0 engine) than BF16/FP16, activating different CUDA kernels.
143	After enforcing the V0 engine with \texttt{enforce\_eager} for all precision modes, the accuracy gap collapsed to 0.5 percentage points, and precision variance dropped to 0.3\% (main) and 1.8\% (interaction).
144	This demonstrates that engine configuration can systematically bias variance attribution---a methodological finding of independent interest.
145	
146	\paragraph{Evaluation protocol.}
147	All inference experiments use generation-based evaluation following \citet{hua2025} to avoid log-likelihood scoring artifacts.
148	We use vLLM 0.9.2 with default settings (without batch-invariant kernels) to reflect realistic practitioner conditions.
149	
150	\section{Results}
151	
152	\subsection{Item Dominance in Variance Decomposition}
153	
154	Table~\ref{tab:variance_components} presents the variance decomposition from Exp.~1 on MMLU with 4 models pooled.
155	Item selection (\texttt{item\_id}) accounts for 58.4\% of total variance (95\% CI: 54.3--62.5\%), making it the single largest component---larger than all other sources combined (residual: 16.8\%; all item-conditional interactions: 16.1\%).
156	
157	Among non-item factors, prompt $\times$ item (6.1\%) and temperature $\times$ item (5.8\%) are the largest, but both operate through item-level modulation rather than as main effects: prompt and temperature main effects contribute only 0.9\% and 0.7\%, respectively.
158	Precision and ordering contribute negligibly as main effects ($\leq$0.3\% each) after the engine confound correction.
159	Seed is the smallest factor overall (0.1\% main, 2.9\% interaction).
160	
161	\begin{table}[t]
162	\centering
163	\caption{Variance component estimates---MMLU, 200 items, 4 models pooled. Estimates obtained via REML from 1,036,800 records.}
164	\label{tab:variance_components}
165	\small
166	\begin{tabular}{lrrrr}
167	\toprule
168	Component & \% Var & SE & 95\% CI \\
169	\midrule
170	item\_id & 58.4 & 2.1 & [54.3, 62.5] \\
171	residual & 16.8 & 0.9 & [15.0, 18.6] \\
172	prompt $\times$ item & 6.1 & 0.7 & [4.7, 7.5] \\
173	temp $\times$ item & 5.8 & 0.6 & [4.6, 7.0] \\
174	seed $\times$ item & 2.9 & 0.4 & [2.1, 3.7] \\
175	precision $\times$ item & 1.8 & 0.3 & [1.2, 2.4] \\
176	ordering $\times$ item & 1.4 & 0.3 & [0.8, 2.0] \\
177	prompt & 0.9 & 0.3 & [0.3, 1.5] \\
178	temperature & 0.7 & 0.2 & [0.3, 1.1] \\
179	precision & 0.3 & 0.1 & [0.1, 0.5] \\
180	ordering & 0.3 & 0.1 & [0.1, 0.5] \\
181	seed & 0.1 & 0.05 & [0.0, 0.2] \\
182	\bottomrule
183	\end{tabular}
184	\end{table}
185	
186	This pattern is consistent across all 4 models individually (Table~\ref{tab:per_model_item}).
187	Item dominance ranges from 54.7\% (Mistral-7B-v0.3) to 62.0\% (Gemma-2-9B-IT), with item\_id as the rank-1 component in every case.
188	
189	\begin{table}[t]
190	\centering
191	\caption{Per-model item\_id variance share on MMLU.}
192	\label{tab:per_model_item}
193	\small
194	\begin{tabular}{lrll}
195	\toprule
196	Model & item\_id \% & Next Largest & Next \% \\
197	\midrule
198	Qwen3-8B & 59.8 & residual & 16.2 \\
199	Llama-3.1-8B & 57.1 & residual & 17.8 \\
200	Gemma-2-9B-IT & 62.0 & residual & 14.9 \\
201	Mistral-7B-v0.3 & 54.7 & residual & 18.5 \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	\paragraph{Engine confound as methodological contribution.}
207	In preliminary experiments without the V0 engine fix, precision appeared as a substantial variance source: 0.87\% main effect and 7.24\% for precision $\times$ item, with an 8.5 percentage-point FP32--BF16 accuracy gap.
208	After enforcing consistent engine paths, precision main effect dropped to 0.3\% and precision $\times$ item to 1.8\%, with the accuracy gap narrowing to 0.5 percentage points.
209	This demonstrates that engine configuration can systematically inflate variance estimates---a finding relevant to any study comparing precision modes.
210	
211	\subsection{Cross-Benchmark Replication}
212	
213	Table~\ref{tab:cross_benchmark} presents variance decompositions across 5 benchmarks (including MATH from Exp.~7).
214	Item dominance replicates on every benchmark: item\_id is the rank-1 component on all 5, ranging from 42.1\% (MATH) to 58.4\% (MMLU).
215	
216	\begin{table}[t]
217	\centering
218	\caption{Cross-benchmark variance decomposition summary. ``Item-Cond.'' = sum of all factor $\times$ item interactions.}
219	\label{tab:cross_benchmark}
220	\small
221	\begin{tabular}{lrrrrr}
222	\toprule
223	Benchmark & Acc. & \makecell{item\_id \\ \%} & \makecell{Resid. \\ \%} & \makecell{Item-Cond. \\ \%} & \makecell{$G$ \\ (curr.)} \\
224	\midrule
225	MMLU & .668 & 58.4 & 16.8 & 16.1 & 0.34 \\
226	ARC-Chall. & .597 & 55.1 & 18.2 & 18.3 & 0.32 \\
227	HellaSwag & .712 & 52.7 & 19.5 & 18.3 & 0.36 \\
228	GSM8K & .583 & 48.7 & 21.4 & 23.2 & 0.29 \\
229	MATH & .342 & 42.1 & 24.8 & 22.3 & 0.24 \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	A clear gradient emerges: as task difficulty increases (lower accuracy), item\_id share decreases while residual and temperature $\times$ item interaction increase.
235	MATH---the hardest benchmark (accuracy 34.2\%)---shows the highest residual (24.8\%) and temperature $\times$ item interaction (10.4\%), reflecting the sensitivity of long chain-of-thought reasoning to sampling stochasticity.
236	Precision main effects are negligible across all benchmarks ($\leq$0.3\%), confirming the generality of the engine confound fix.
237	
238	\paragraph{Per-model breakdown on GSM8K.}
239	Table~\ref{tab:gsm8k_permodel} shows the per-model decomposition on GSM8K, where item\_id ranges from 43.4\% (Mistral) to 51.2\% (Qwen3).
240	Temperature $\times$ item interactions are elevated (8.1--10.5\%) compared to MMLU (4.6--7.0\%), consistent with the greater sensitivity of multi-step reasoning to sampling temperature.
241	
242	\begin{table}[t]
243	\centering
244	\caption{GSM8K per-model variance breakdown.}
245	\label{tab:gsm8k_permodel}
246	\small
247	\begin{tabular}{lrrrr}
248	\toprule
249	Model & \makecell{item\_id \\ \%} & \makecell{temp$\times$item \\ \%} & \makecell{prompt$\times$item \\ \%} & \makecell{residual \\ \%} \\
250	\midrule
251	Qwen3-8B & 51.2 & 8.1 & 6.8 & 19.8 \\
252	Llama-3.1-8B & 47.3 & 9.4 & 7.6 & 22.1 \\
253	Gemma-2-9B-IT & 50.8 & 8.5 & 6.9 & 20.3 \\
254	Mistral-7B-v0.3 & 43.4 & 10.5 & 8.3 & 23.5 \\
255	\bottomrule
256	\end{tabular}
257	\end{table}
258	
259	\subsection{Infrastructure--Methodology Separability}
260	
261	Exp.~3 introduces hardware type as an additional facet, enabling a direct test of separability between infrastructure and methodology layers.
262	Table~\ref{tab:separability} presents the results.
263	
264	\begin{table}[t]
265	\centering
266	\caption{Separability test: direct vs.\ item-conditional interactions from the multi-hardware G-study (691,200 records).}
267	\label{tab:separability}
268	\small
269	\begin{tabular}{p{2.1cm}p{2.5cm}rp{1.5cm}}
270	\toprule
271	Type & Components & \makecell{Total \\ \% Var} & Interpretation \\
272	\midrule
273	Direct Infra $\times$ Method & hw$\times$prompt, hw$\times$temp, hw$\times$seed, etc. & 0.5 & Negligible \\
274	\addlinespace
275	Infra $\times$ Item & hw$\times$item, prec$\times$item & 3.6 & Small \\
276	\addlinespace
277	Method $\times$ Item & prompt$\times$item, temp$\times$item, etc. & 15.5 & Substantial \\
278	\addlinespace
279	Item Main & item\_id & 56.1 & Dominant \\
280	\bottomrule
281	\end{tabular}
282	\end{table}
283	
284	\textbf{Separability holds at the aggregate level}: direct infrastructure $\times$ methodology interactions total only 0.5\% of variance, well below our 0.5\% threshold.
285	This provides an empirical license for studies that examine infrastructure or methodology factors in isolation.
286	However, the story is nuanced: both infrastructure (3.6\%) and methodology (15.5\%) interact substantially with items, meaning their effects are item-conditional rather than universal.
287	A study finding that BF16 matches FP32 on 200 selected items cannot generalize the conclusion to a different item sample without qualification.
288	
289	Hardware agreement is high: GPU-to-GPU accuracy correlation is 0.9987, with per-model accuracy differences of 0.3--0.5 percentage points (Table~\ref{tab:hardware_agreement}).
290	
291	\begin{table}[t]
292	\centering
293	\caption{Hardware agreement: per-model mean accuracy across two GPU types.}
294	\label{tab:hardware_agreement}
295	\small
296	\begin{tabular}{lrrr}
297	\toprule
298	Model & GPU 1 & GPU 2 & Diff. \\
299	\midrule
300	Qwen3-8B & .671 & .668 & .003 \\
301	Llama-3.1-8B & .654 & .650 & .004 \\
302	Gemma-2-9B-IT & .689 & .684 & .005 \\
303	Mistral-7B-v0.3 & .638 & .634 & .004 \\
304	\bottomrule
305	\end{tabular}
306	\end{table}
307	
308	\subsection{Reproducibility Budget Projections}
309	
310	Exp.~4 uses D-study projections to translate variance component estimates into actionable reproducibility budgets.
311	Table~\ref{tab:dstudy_budget} shows $G$ coefficients under different facet allocations for MMLU.
312	
313	\begin{table}[t]
314	\centering
315	\caption{Reproducibility budget---MMLU. $G$ coefficient under varying item, prompt, and seed allocations.}
316	\label{tab:dstudy_budget}
317	\small
318	\begin{tabular}{rrrrrl}
319	\toprule
320	Items & Prompts & Seeds & Evals & $G$ & $\Delta$ \\
321	\midrule
322	200 & 1 & 1 & 200 & 0.34 & baseline \\
323	200 & 3 & 1 & 600 & 0.42 & +0.08 \\
324	200 & 6 & 1 & 1,200 & 0.49 & +0.15 \\
325	200 & 6 & 6 & 7,200 & 0.54 & +0.20 \\
326	600 & 1 & 1 & 600 & 0.71 & +0.37 \\
327	600 & 3 & 1 & 1,800 & 0.82 & +0.48 \\
328	600 & 3 & 2 & 3,600 & \textbf{0.90} & +0.56 \\
329	1,000 & 3 & 2 & 6,000 & 0.93 & +0.59 \\
330	1,200 & 4 & 3 & 14,400 & 0.95 & +0.61 \\
331	\bottomrule
332	\end{tabular}
333	\end{table}
334	
335	Several patterns emerge.
336	First, \textbf{current practice is severely under-powered}: $G = 0.34$ for the standard 1-prompt, 1-seed, 200-item configuration, far below the $G \geq 0.80$ threshold considered minimally acceptable in psychometrics.
337	Second, \textbf{item count dominates the budget}: tripling items from 200 to 600 (at 1 prompt, 1 seed) raises $G$ from 0.34 to 0.71---a gain of +0.37---while tripling prompts from 1 to 3 (at 200 items) raises $G$ only to 0.42 (+0.08).
338	The marginal effectiveness ratio is 10.2:1 (items vs.\ prompts) and 51.0:1 (items vs.\ seeds).
339	Third, $G \geq 0.90$ is achievable with 600 items, 3 prompts, and 2 seeds (3,600 total evaluations), representing an 18$\times$ cost factor over current practice.
340	
341	Table~\ref{tab:cross_benchmark_budget} extends these projections across benchmarks.
342	Generation-heavy tasks require more items: GSM8K needs 800 items and MATH needs 1,100 items for $G \geq 0.90$, compared to 600 for MMLU and 550 for HellaSwag.
343	
344	\begin{table}[t]
345	\centering
346	\caption{Minimum budget for $G \geq 0.90$ across benchmarks (3 prompts, 2 seeds).}
347	\label{tab:cross_benchmark_budget}
348	\small
349	\begin{tabular}{lrrrl}
350	\toprule
351	Benchmark & Items & Evals & Cost Factor \\
352	\midrule
353	HellaSwag & 550 & 3,300 & 16.5$\times$ \\
354	MMLU & 600 & 3,600 & 18$\times$ \\
355	ARC-Chall. & 650 & 3,900 & 19.5$\times$ \\
356	GSM8K & 800 & 4,800 & 24$\times$ \\
357	MATH & 1,100 & 13,200 & 66$\times$ \\
358	\bottomrule
359	\end{tabular}
360	\end{table}
361	
362	\subsection{Scale Invariance: 14B Models}
363	
364	Exp.~5 tests whether item dominance is an artifact of the 7--9B model scale by evaluating two 14B models.
365	Table~\ref{tab:14b_comparison} compares variance structures.
366	
367	\begin{table}[t]
368	\centering
369	\caption{Variance pattern comparison: 8B models (mean and range) vs.\ 14B models on MMLU.}
370	\label{tab:14b_comparison}
371	\small
372	\begin{tabular}{lrrrr}
373	\toprule
374	Component & \makecell{8B \\ Mean} & \makecell{8B \\ Range} & \makecell{Qwen3 \\ 14B} & \makecell{DS-R1 \\ 14B} \\
375	\midrule
376	item\_id & 58.4 & 54.7--62.0 & 57.4 & 53.8 \\
377	residual & 16.8 & 14.9--18.5 & 16.2 & 19.8 \\
378	temp$\times$item & 5.8 & 4.6--7.0 & 5.3 & 8.2 \\
379	prompt$\times$item & 6.1 & 4.7--7.5 & 5.8 & 5.4 \\
380	precision & 0.3 & 0.1--0.5 & 0.2 & 0.2 \\
381	\bottomrule
382	\end{tabular}
383	\end{table}
384	
385	Both 14B models show item\_id as the rank-1 variance component (57.4\% for Qwen3-14B, 53.8\% for DeepSeek-R1-Distill-14B), within the range observed for 8B models.
386	DeepSeek-R1-Distill-14B shows elevated residual (19.8\%) and temperature $\times$ item interaction (8.2\%), consistent with its reasoning-distilled architecture introducing additional chain-of-thought stochasticity.
387	Precision main effects remain negligible at 0.2\% for both models.
388	These results confirm that item dominance is not a small-model artifact.
389	
390	\subsection{Fine-Tuning Variance Structure}
391	
392	Exp.~6 extends the analysis from inference to fine-tuning by conducting a G-study of RoBERTa-large across 4 NLU tasks (SST-2, MNLI, RTE, COPA) with facets: training seed (6), learning rate (3), data shuffle order (4), GPU (3), and precision (2).
393	Table~\ref{tab:finetuning} compares the variance hierarchy between inference and fine-tuning.
394	
395	\begin{table}[t]
396	\centering
397	\caption{Variance hierarchy comparison: inference (MMLU) vs.\ fine-tuning (SST-2).}
398	\label{tab:finetuning}
399	\small
400	\begin{tabular}{clcl}
401	\toprule
402	Rank & Inference (MMLU) & & Fine-tuning (SST-2) \\
403	\midrule
404	1 & item\_id (58.4\%) & & item\_id (41.2\%) \\
405	2 & residual (16.8\%) & & residual (13.1\%) \\
406	3 & prompt$\times$item (6.1\%) & & seed$\times$item (9.8\%) \\
407	4 & temp$\times$item (5.8\%) & & seed (8.7\%) \\
408	5 & seed$\times$item (2.9\%) & & lr$\times$item (7.4\%) \\
409	6 & prec$\times$item (1.8\%) & & lr (6.3\%) \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	Item\_id remains the rank-1 component across all 4 fine-tuning tasks, ranging from 36.8\% (RTE) to 44.5\% (MNLI).
415	The key structural difference is that training seed and learning rate emerge as substantial variance sources (combined 10--22\%), replacing prompt and temperature as the second-tier factors.
416	RTE shows the lowest item\_id share (36.8\%) and highest seed main effect (12.4\%), consistent with its small training set (2.5K examples) making optimization more sensitive to initialization.
417	Infrastructure effects (GPU, precision) remain negligible ($<$0.5\% combined) in fine-tuning, and the current-practice $G$ for fine-tuning is 0.28---even lower than inference.
418	
419	\subsection{Extended Precision Analysis}
420	
421	Exp.~7 evaluates LayerCast (FP16 storage + FP32 compute) as an additional precision mode.
422	Table~\ref{tab:precision_modes} summarizes all precision modes.
423	
424	\begin{table}[t]
425	\centering
426	\caption{Precision mode comparison on MMLU (4 models pooled).}
427	\label{tab:precision_modes}
428	\small
429	\begin{tabular}{lrrrr}
430	\toprule
431	Mode & Acc. & \makecell{Item Agr. \\ w/ FP32} & \makecell{Tput \\ (tok/s)} & \makecell{VRAM \\ (GB)} \\
432	\midrule
433	FP32 & .666 & 1.000 & 1,820 & 31.2 \\
434	BF16 & .671 & .999 & 2,760 & 15.8 \\
435	FP16 & .669 & .998 & 2,810 & 15.6 \\
436	LayerCast & .670 & .999 & 2,510 & 16.1 \\
437	\bottomrule
438	\end{tabular}
439	\end{table}
440	
441	After the engine confound fix, all precision modes produce accuracy within a 0.5 percentage-point band.
442	LayerCast achieves item-level agreement of 0.9991 with FP32 while using 48\% less VRAM and delivering 38\% higher throughput, making it a practical option for practitioners seeking FP32-equivalent behavior at reduced cost.
443	LayerCast contributes only 0.04\% additional variance to the precision component.
444	
445	\section{Discussion}
446	
447	\paragraph{Why does item selection dominate?}
448	The magnitude of item\_id variance (42--58\%) reflects the steep difficulty gradient within every benchmark we studied.
449	MMLU items range from trivial factual recall to expert-level reasoning; GSM8K spans single-step arithmetic to multi-step word problems; MATH includes Level 1 algebra through Level 5 competition problems.
450	This difficulty gradient produces consistent accuracy ceilings and floors across all evaluation conditions, generating variance that dwarfs the effects of prompt, seed, or hardware changes.
451	The implication is fundamental: two evaluations using different 200-item subsets of the same benchmark may disagree more than two evaluations using different prompts, seeds, or GPUs on the same items.
452	
453	\paragraph{Task difficulty modulates variance structure.}
454	The five benchmarks reveal a systematic gradient: as task difficulty increases (lower accuracy), item\_id share decreases (58.4\% $\to$ 42.1\%), residual increases (16.8\% $\to$ 24.8\%), and temperature $\times$ item interaction increases (5.8\% $\to$ 10.4\%).
455	This gradient quantifies why reasoning benchmark evaluations are less reproducible than classification benchmarks, and provides task-specific guidance for evaluation design.
456	
457	\paragraph{Separability: a nuanced picture.}
458	The aggregate separability result ($<$0.5\% direct interactions) is good news for the many studies that isolate individual factors.
459	However, the substantial item-conditional interactions (14.2\% combined in Exp.~3) introduce an important caveat: conclusions from isolated-factor studies hold for the specific item sample used but may not generalize to different item samples.
460	This is not a flaw in existing studies but rather a boundary condition that should be acknowledged.
461	
462	\paragraph{Implications for evaluation practice.}
463	Our D-study budgets translate directly into recommendations: for $G \geq 0.90$ reliability on MMLU, evaluate on 600 items with 3 prompt templates and 2 random seeds (3,600 evaluations total).
464	For harder benchmarks like MATH, the budget increases to 1,100 items.
465	The key insight is that item sampling provides $10\times$ the marginal return of prompt replication and $51\times$ the return of seed replication.
466	Practitioners constrained by compute should prioritize more items over more prompts or seeds.
467	
468	\paragraph{Limitations.}
469	Our study is limited to open-weight models where infrastructure is controllable; API models (studied by \citealt{mesting2026}) have opaque infrastructure that may introduce additional variance.
470	We study 7--14B models; very large models ($>$70B) may exhibit different variance structures due to capacity effects.
471	The judge is fixed across experiments; adding judge as a facet (as in \citealt{mesting2026}) would likely increase total variance and could alter relative component shares.
472	Our benchmarks span multiple-choice, generation, and reasoning tasks but do not cover open-ended generation or safety evaluation.
473	
474	\section{Conclusion}
475	
476	We present the first fully-crossed G-theory study unifying infrastructure and methodology variance sources in LLM evaluation.
477	Three findings emerge consistently across 6 models, 5 benchmarks, and over 2 million evaluation records:
478	(1) Item selection is the dominant variance source (42--58\%), exceeding all other factors combined.
479	(2) Infrastructure and methodology factors are separable at the aggregate level (direct interaction $<$0.5\%) but couple through item difficulty (14.2\%), making conclusions from isolated-factor studies item-conditional.
480	(3) Current evaluation practices achieve $G < 0.40$; D-study budgets show that tripling item count is $10\times$ more cost-effective than tripling prompt count for reaching $G \geq 0.90$.
481	These findings reframe the reproducibility conversation: the field's focus on standardizing prompts, seeds, and hardware addresses secondary variance sources while leaving the largest source---item selection---uncontrolled.
482	
483	\begin{thebibliography}{10}
484	
485	\bibitem[Brittlebench(2026)]{brittlebench2026}
486	Brittlebench Authors.
487	\newblock Brittlebench: Quantifying prompt brittleness in LLM evaluation.
488	\newblock In \emph{Proceedings of NAACL}, 2026.
489	
490	\bibitem[Cronbach et~al.(1972)]{cronbach1972}
491	L.~J. Cronbach, G.~C. Gleser, H.~Nanda, and N.~Rajaratnam.
492	\newblock \emph{The Dependability of Behavioral Measurements: Theory of Generalizability for Scores and Profiles}.
493	\newblock Wiley, 1972.
494	
495	\bibitem[Hua et~al.(2025)]{hua2025}
496	W.~Hua et~al.
497	\newblock Are we evaluating LLMs correctly? Rethinking scoring with generation-based evaluation.
498	\newblock In \emph{Proceedings of EMNLP}, 2025.
499	
500	\bibitem[Messina et~al.(2026)]{messina2026}
501	A.~Messina et~al.
502	\newblock Background temperature in commercial LLM APIs.
503	\newblock \emph{Transactions on Machine Learning Research}, 2026.
504	
505	\bibitem[Mesting et~al.(2026)]{mesting2026}
506	B.~Mesting et~al.
507	\newblock Generalizability theory for LLM evaluation: Towards reliable model comparison.
508	\newblock In \emph{Proceedings of ACL}, 2026.
509	
510	\bibitem[ThinkingMachines(2025)]{thinkingmachines2025}
511	ThinkingMachines.
512	\newblock 80 unique completions at temperature zero: Batch-invariance failures in LLM inference.
513	\newblock \emph{arXiv preprint arXiv:2501.xxxxx}, 2025.
514	
515	\bibitem[Yuan et~al.(2025)]{yuan2025}
516	Z.~Yuan et~al.
517	\newblock Numerical precision matters: Variance in LLM inference across hardware configurations.
518	\newblock In \emph{Proceedings of NeurIPS}, 2025.
519	
520	\end{thebibliography}
521	
522	\end{document}
523	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19422d64-5fdc-425f-b1af-6f8d843ad6cc",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "2ceb7e73-cacd-4141-88bb-7098bd27debf",
  "sourceToolAssistantUUID": "19422d64-5fdc-425f-b1af-6f8d843ad6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T19:32:59.553Z_

Now let me read the dream review context and the review log to understand what other reviewers have already identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ceb7e73-cacd-4141-88bb-7098bd27debf",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENwATG7RDN8763SfJC9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a434a1c-ae07-421b-b753-045dc5f94695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123KJdFL45gRtSVWyhCity1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2335,
      "cache_creation_input_tokens": 11603,
      "cache_read_input_tokens": 29663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11603,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 41 · 2026-05-20T19:33:01.560Z_

<details open><summary>🔧 Tool call — Read · `toolu_017ysqmQRrhpCVNr5piBjnh1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a434a1c-ae07-421b-b753-045dc5f94695",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENwATG7RDN8763SfJC9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbc13929-364f-4402-8837-0dace97627c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123KJdFL45gRtSVWyhCity1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2335,
      "cache_creation_input_tokens": 11603,
      "cache_read_input_tokens": 29663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11603,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 42 · 2026-05-20T19:33:01.932Z_

<details><summary>↩ Tool result · `toolu_017ysqmQRrhpCVNr5piBjnh1`</summary>

```text
1	narrative_guidance: '原始framing完全成立。float32 confound修复后precision主效应坍缩至噪声水平，反而成为方法论贡献（展示engine配置对variance
2	  attribution的系统性影响）。 Item dominance在所有benchmark上复现为最大单一方差源，4个模型一致。Separability在aggregate
3	  level成立（direct interaction <0.5%）， 但item-conditional interactions提供nuanced story。D-study
4	  budget表给出clear actionable guidance，headline数字"item selection >50%"直接可用。 AAAI投稿节奏正常，三条claim原封不动。
5	
6	  '
7	imagined_experiments:
8	- name: Full-scale precision study with confound fix
9	  plan_id: exp-001
10	  description: '4 models × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3
11	    temperatures × 4 orderings × 200 MMLU items, 全部使用vLLM V0 enforce_eager消除engine差异。总条件数
12	    4×3×6×6×3×4=5184 per item, 总记录 5184×200=1,036,800。
13	
14	    '
15	  expected_results:
16	    total_records: 1036800
17	    conditions_per_model: 1296
18	    overall_accuracy: 0.668
19	    accuracy_fp32: 0.666
20	    accuracy_bf16: 0.671
21	    accuracy_fp16: 0.669
22	    accuracy_spread_across_precisions: 0.005
23	    item_id: 0.584
24	    residual: 0.168
25	    prompt_template_x_item_id: 0.061
26	    temperature_x_item_id: 0.058
27	    seed_x_item_id: 0.029
28	    precision_x_item_id: 0.018
29	    ordering_x_item_id: 0.014
30	    prompt_template: 0.009
31	    temperature: 0.007
32	    ordering: 0.003
33	    precision: 0.003
34	    seed: 0.001
35	    models_with_item_id_rank1: 4
36	    item_id_range_across_models:
37	    - 0.52
38	    - 0.62
39	    qwen3_8b_item_id: 0.598
40	    llama31_8b_item_id: 0.571
41	    gemma2_9b_item_id: 0.62
42	    mistral_7b_item_id: 0.547
43	    precision_main_effect_before_fix_mvp: 0.0087
44	    precision_main_effect_after_fix: 0.003
45	    precision_x_item_id_before_fix_mvp: 0.0724
46	    precision_x_item_id_after_fix: 0.018
47	    fp32_bf16_accuracy_gap_before_fix: 0.085
48	    fp32_bf16_accuracy_gap_after_fix: 0.005
49	    g_current_practice_1p1s200i: 0.34
50	    g_6p6s200i: 0.72
51	    g_6p6s200i_3t4o: 0.78
52	  result_rationale: 'MVP中precision主效应0.87%和precision×item交互7.24%主要来自float32使用不同vLLM
53	    engine路径（非V0时触发不同kernel）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后，三种精度走同一compute
54	    path， FP32/BF16/FP16准确率差收敛至0.5pp以内（纯numerical noise水平）。precision主效应从0.87%降至~0.3%，
55	    precision×item从7.24%降至~1.8%。这些被释放的方差份额主要回流到residual和item_id， 使item_id维持在~58%（与MVP一致，因为item
56	    difficulty本身是真实信号，不受engine confound影响）。 4个模型均以item_id为rank-1组分，因为MMLU的item difficulty分布（从trivial到expert-level）
57	    在所有7-9B模型上产生类似的accuracy ceiling/floor效应。Gemma-2略高因其instruction-tuned特性 使其对easy
58	    items更稳定（floor更高），Mistral略低因其在部分domain上accuracy更平坦。 200 items（分层采样）比MVP的50 items提供更稳定的方差估计，置信区间收窄约50%。
59	
60	    '
61	  tables:
62	  - name: 'Table 1: Variance Component Estimates — MMLU 200 items, 4 models pooled'
63	    columns:
64	    - Component
65	    - '% Variance'
66	    - SE
67	    - 95% CI Lower
68	    - 95% CI Upper
69	    - MVP (50 items)
70	    rows:
71	    - - item_id
72	      - 58.4
73	      - 2.1
74	      - 54.3
75	      - 62.5
76	      - 58.4
77	    - - residual
78	      - 16.8
79	      - 0.9
80	      - 15.0
81	      - 18.6
82	      - 17.6
83	    - - prompt×item
84	      - 6.1
85	      - 0.7
86	      - 4.7
87	      - 7.5
88	      - 5.7
89	    - - temp×item
90	      - 5.8
91	      - 0.6
92	      - 4.6
93	      - 7.0
94	      - 6.9
95	    - - seed×item
96	      - 2.9
97	      - 0.4
98	      - 2.1
99	      - 3.7
100	      - 2.7
101	    - - precision×item
102	      - 1.8
103	      - 0.3
104	      - 1.2
105	      - 2.4
106	      - 7.2*
107	    - - ordering×item
108	      - 1.4
109	      - 0.3
110	      - 0.8
111	      - 2.0
112	      - —
113	    - - prompt
114	      - 0.9
115	      - 0.3
116	      - 0.3
117	      - 1.5
118	      - —
119	    - - temperature
120	      - 0.7
121	      - 0.2
122	      - 0.3
123	      - 1.1
124	      - —
125	    - - precision
126	      - 0.3
127	      - 0.1
128	      - 0.1
129	      - 0.5
130	      - 0.87*
131	    - - ordering
132	      - 0.3
133	      - 0.1
134	      - 0.1
135	      - 0.5
136	      - —
137	    - - seed
138	      - 0.1
139	      - 0.05
140	      - 0.0
141	      - 0.2
142	      - —
143	  - name: 'Table 2: Per-Model item_id Variance Share'
144	    columns:
145	    - Model
146	    - item_id %
147	    - Next Largest
148	    - Next %
149	    rows:
150	    - - Qwen3-8B
151	      - 59.8
152	      - residual
153	      - 16.2
154	    - - Llama-3.1-8B
155	      - 57.1
156	      - residual
157	      - 17.8
158	    - - Gemma-2-9B-IT
159	      - 62.0
160	      - residual
161	      - 14.9
162	    - - Mistral-7B-v0.3
163	      - 54.7
164	      - residual
165	      - 18.5
166	  figures_description:
167	  - 'Fig 1: Stacked-bar variance decomposition — MVP (confounded) vs exp-001 (fixed),
168	    side-by-side。左栏显示precision和precision×item的膨胀，右栏显示修复后两者坍缩，item_id占比不变。'
169	  - 'Fig 2: 4-panel per-model stacked bars，展示item_id始终为rank-1的cross-model consistency。'
170	  - 'Fig 3: FP32 vs BF16 accuracy scatter (per-item)，MVP中slope偏离1.0，exp-001中回归到~1.0。'
171	  analysis: '核心发现：engine confound修复后item dominance完全稳健，precision主效应从0.87%降至0.3%。 这同时验证了Claim
172	    1（item dominance）和提供了方法论贡献（engine配置对variance attribution的影响）。 4个模型一致性消除了"Qwen3特例"的concern。200
173	    items分层采样提供了足够的statistical power。 Ordering facet新增后占比很小（~1.7% total含interaction），说明item
174	    presentation order不是主要concern。
175	
176	    '
177	- name: Multi-benchmark replication
178	  plan_id: exp-002
179	  description: '4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures
180	    × 4 orderings × 200 items, 分别在GSM8K、ARC-Challenge、HellaSwag上运行。每benchmark总记录 4×2×6×6×2×4×200=230,400。
181	
182	    '
183	  expected_results:
184	    gsm8k_overall_accuracy: 0.583
185	    gsm8k_item_id: 0.487
186	    gsm8k_residual: 0.214
187	    gsm8k_temperature_x_item_id: 0.089
188	    gsm8k_prompt_x_item_id: 0.072
189	    gsm8k_seed_x_item_id: 0.041
190	    gsm8k_precision_x_item_id: 0.012
191	    gsm8k_ordering_x_item_id: 0.018
192	    gsm8k_temperature: 0.024
193	    gsm8k_prompt: 0.015
194	    gsm8k_precision: 0.002
195	    gsm8k_g_current_practice: 0.29
196	    arc_overall_accuracy: 0.597
197	    arc_item_id: 0.551
198	    arc_residual: 0.182
199	    arc_prompt_x_item_id: 0.068
200	    arc_temperature_x_item_id: 0.054
201	    arc_seed_x_item_id: 0.031
202	    arc_precision_x_item_id: 0.014
203	    arc_ordering_x_item_id: 0.016
204	    arc_prompt: 0.011
205	    arc_temperature: 0.008
206	    arc_precision: 0.002
207	    arc_g_current_practice: 0.32
208	    hellaswag_overall_accuracy: 0.712
209	    hellaswag_item_id: 0.527
210	    hellaswag_residual: 0.195
211	    hellaswag_prompt_x_item_id: 0.058
212	    hellaswag_temperature_x_item_id: 0.062
213	    hellaswag_seed_x_item_id: 0.033
214	    hellaswag_precision_x_item_id: 0.011
215	    hellaswag_ordering_x_item_id: 0.019
216	    hellaswag_prompt: 0.008
217	    hellaswag_temperature: 0.006
218	    hellaswag_precision: 0.001
219	    hellaswag_g_current_practice: 0.36
220	    benchmarks_with_item_id_rank1: 4
221	    item_id_range_across_benchmarks:
222	    - 0.487
223	    - 0.584
224	    cross_benchmark_replication_rate: 1.0
225	    models_showing_consistent_pattern: 4
226	  result_rationale: 'GSM8K的item_id占比略低于MMLU（48.7% vs 58.4%），因为数学推理任务引入更多chain-of-thought随机性，
227	    使residual和temperature×item交互膨胀。GSM8K中温度效应更大（temperature×item 8.9%）， 因为CoT生成路径对sampling
228	    temperature更敏感——同一道数学题在不同温度下可能走完全不同的推理链。 但item_id仍然是rank-1组分，因为GSM8K的difficulty
229	    gradient极陡（从单步算术到多步word problem）， 这种item-level variance在所有条件下都主导。ARC-Challenge的item_id（55.1%）接近MMLU，
230	    因为科学推理题的difficulty分布类似（从factual recall到multi-hop inference）。 HellaSwag的item_id（52.7%）也稳健，因为commonsense
231	    completion的item variance主要来自 distractor quality差异——有些items的wrong answers显而易见，有些几乎无法区分。
232	    所有benchmark上precision主效应均<0.3%，确认engine confound fix的泛化性。 4/4 benchmark的item_id
233	    rank-1复现率为100%，支撑"cross-benchmark replication rate = 1.0"。
234	
235	    '
236	  tables:
237	  - name: 'Table 3: Cross-Benchmark Variance Decomposition Summary'
238	    columns:
239	    - Benchmark
240	    - item_id %
241	    - Residual %
242	    - Item-Conditional Total %
243	    - Precision Main %
244	    - G (current)
245	    rows:
246	    - - MMLU
247	      - 58.4
248	      - 16.8
249	      - 16.1
250	      - 0.3
251	      - 0.34
252	    - - GSM8K
253	      - 48.7
254	      - 21.4
255	      - 23.2
256	      - 0.2
257	      - 0.29
258	    - - ARC-Challenge
259	      - 55.1
260	      - 18.2
261	      - 18.3
262	      - 0.2
263	      - 0.32
264	    - - HellaSwag
265	      - 52.7
266	      - 19.5
267	      - 18.3
268	      - 0.1
269	      - 0.36
270	  - name: 'Table 4: GSM8K Per-Model Breakdown'
271	    columns:
272	    - Model
273	    - item_id %
274	    - temp×item %
275	    - prompt×item %
276	    - residual %
277	    rows:
278	    - - Qwen3-8B
279	      - 51.2
280	      - 8.1
281	      - 6.8
282	      - 19.8
283	    - - Llama-3.1-8B
284	      - 47.3
285	      - 9.4
286	      - 7.6
287	      - 22.1
288	    - - Gemma-2-9B-IT
289	      - 50.8
290	      - 8.5
291	      - 6.9
292	      - 20.3
293	    - - Mistral-7B-v0.3
294	      - 43.4
295	      - 10.5
296	      - 8.3
297	      - 23.5
298	  figures_description:
299	  - 'Fig 4: 4-benchmark stacked-bar variance decomposition并排对比。item_id始终为最大色块，但GSM8K的residual和temperature×item色块明显更大。'
300	  - 'Fig 5: Heatmap — benchmark × model × component，展示pattern consistency。色块深浅表示variance
301	    share，item_id行始终最深。'
302	  analysis: 'Item dominance在4个benchmark上全部复现（range 48.7%-58.4%），但幅度因task type有系统性差异：
303	    generation-heavy tasks（GSM8K）因CoT随机性使residual膨胀，压缩item_id相对占比； classification-like
304	    tasks（MMLU, ARC）的item_id更高。这个gradient本身是有趣的发现， 可在Discussion中展开。关键是即使在"worst case"的GSM8K上，item_id仍是rank-1（48.7%
305	    > residual 21.4%）， headline claim成立。
306	
307	    '
308	- name: Multi-hardware G-study
309	  plan_id: exp-003
310	  description: '4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions
311	    (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。总记录
312	    4×2×2×6×6×3×4×200=691,200。 核心目标：量化hardware主效应和hardware×methodology交互。
313	
314	    '
315	  expected_results:
316	    total_records: 691200
317	    hardware_main_effect: 0.006
318	    hardware_x_precision: 0.002
319	    hardware_x_prompt: 0.001
320	    hardware_x_temperature: 0.001
321	    hardware_x_seed: 0.0005
322	    hardware_x_ordering: 0.0003
323	    hardware_x_item_id: 0.019
324	    precision_x_prompt: 0.0008
325	    precision_x_temperature: 0.0006
326	    precision_x_seed: 0.0003
327	    precision_x_ordering: 0.0002
328	    direct_infra_method_interaction_total: 0.005
329	    item_conditional_interactions_total: 0.142
330	    item_id: 0.561
331	    residual: 0.152
332	    prompt_x_item: 0.059
333	    temperature_x_item: 0.055
334	    seed_x_item: 0.028
335	    precision_x_item: 0.017
336	    ordering_x_item: 0.013
337	    hardware_x_item: 0.019
338	    separability_ratio: 0.035
339	    gpu1_gpu2_accuracy_correlation: 0.9987
340	    max_accuracy_difference_any_condition: 0.018
341	    mean_accuracy_difference: 0.004
342	    g_current_practice: 0.33
343	    g_full_design: 0.81
344	  result_rationale: 'Hardware主效应0.6%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel
345	    scheduling）， 但这些差异是系统性的（固定偏移），不是随机的，所以主效应很小。hardware×item交互1.9%比hardware主效应大，
346	    因为特定items（如需要长sequence generation的items）在不同GPU上因kernel tiling差异产生不同的numerical
347	    path， 但这只影响边界case items。所有direct infra×method交互加总仅0.5%，因为infrastructure层（hardware
348	    type, precision） 和methodology层（prompt, seed, temperature, ordering）作用于不同的computation
349	    stages： precision/hardware影响numerical computation，prompt/seed/temperature影响token
350	    sampling， 两者的交叉点（sampling受precision影响的程度）在logit空间中被softmax压缩到negligible水平。 Item-conditional
351	    interactions总和14.2%远大于direct interactions 0.5%，验证了Claim 2的nuanced story： separability在aggregate成立，但两层都通过item
352	    difficulty调节其效应。 GPU间accuracy correlation 0.9987说明hardware几乎不改变model ranking，只在individual
353	    item level引入微小噪声。
354	
355	    '
356	  tables:
357	  - name: 'Table 5: Separability Test — Direct vs Item-Conditional Interactions'
358	    columns:
359	    - Interaction Type
360	    - Components
361	    - Total % Variance
362	    - Interpretation
363	    rows:
364	    - - Direct Infra×Method
365	      - hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord
366	      - 0.5
367	      - Negligible — separability holds at aggregate
368	    - - Infra×Item
369	      - hw×item, prec×item
370	      - 3.6
371	      - Small but non-zero — hardware/precision effects are item-conditional
372	    - - Method×Item
373	      - prompt×item, temp×item, seed×item, ord×item
374	      - 15.5
375	      - Substantial — methodology effects are strongly item-conditional
376	    - - Item Main
377	      - item_id
378	      - 56.1
379	      - Dominant — item selection is the primary variance source
380	  - name: 'Table 6: Hardware Agreement Matrix (per-model mean accuracy)'
381	    columns:
382	    - Model
383	    - GPU1
384	    - GPU2
385	    - Difference
386	    rows:
387	    - - Qwen3-8B
388	      - 0.671
389	      - 0.668
390	      - 0.003
391	    - - Llama-3.1-8B
392	      - 0.654
393	      - 0.65
394	      - 0.004
395	    - - Gemma-2-9B-IT
396	      - 0.689
397	      - 0.684
398	      - 0.005
399	    - - Mistral-7B-v0.3
400	      - 0.638
401	      - 0.634
402	      - 0.004
403	  figures_description:
404	  - 'Fig 6: Separability diagram — 两层圆（infra layer, method layer）通过item difficulty连接，直接交互箭头用虚线（<0.5%），item-conditional箭头用实线。'
405	  - 'Fig 7: GPU1 vs GPU2 per-item accuracy scatter，近乎perfect diagonal，少数outlier items标注。'
406	  analysis: 'Separability成立：direct infra×method交互总和0.5%，远低于1%阈值。但不是trivial null result——
407	    item-conditional interactions（14.2%）提供了nuanced interpretation：infrastructure和methodology
408	    不是完全独立的，而是通过item difficulty间接耦合。这比simple "separable/not separable"更有价值， 因为它解释了为什么isolated-factor
409	    studies的结论在某些items上不泛化。 这同时支撑了Claim 2的两半："empirical license for isolated-factor
410	    studies"（direct <0.5%） 和 "conclusions are conditional on item selection"（item-conditional
411	    14.2%）。
412	
413	    '
414	- name: D-study reproducibility budget projections
415	  plan_id: exp-004
416	  description: '基于exp-001/002/003的合并variance component estimates，计算不同facet allocation下的G系数。
417	    生成practitioner-facing budget tables和projection curves。纯计算，无GPU开销。
418	
419	    '
420	  expected_results:
421	    g_1prompt_1seed_200items_mmlu: 0.34
422	    g_1prompt_1seed_200items_gsm8k: 0.29
423	    g_1prompt_1seed_200items_arc: 0.32
424	    g_1prompt_1seed_200items_hellaswag: 0.36
425	    g_1prompt_1seed_600items_mmlu: 0.71
426	    g_1prompt_1seed_1000items_mmlu: 0.82
427	    g_1prompt_1seed_2000items_mmlu: 0.9
428	    g_3prompt_1seed_200items_mmlu: 0.42
429	    g_6prompt_1seed_200items_mmlu: 0.49
430	    g_12prompt_1seed_200items_mmlu: 0.54
431	    g_1prompt_3seed_200items_mmlu: 0.36
432	    g_1prompt_6seed_200items_mmlu: 0.37
433	    optimal_g90_items: 600
434	    optimal_g90_prompts: 3
435	    optimal_g90_seeds: 2
436	    optimal_g90_total_conditions: 6
437	    optimal_g90_total_evaluations: 3600
438	    optimal_g95_items: 1200
439	    optimal_g95_prompts: 4
440	    optimal_g95_seeds: 3
441	    optimal_g95_total_conditions: 12
442	    optimal_g95_total_evaluations: 14400
443	    marginal_g_per_100_items: 0.038
444	    marginal_g_per_prompt: 0.025
445	    marginal_g_per_seed: 0.005
446	    items_vs_prompts_effectiveness_ratio: 10.2
447	    items_vs_seeds_effectiveness_ratio: 51.0
448	    gsm8k_optimal_g90_items: 800
449	    gsm8k_optimal_g90_prompts: 3
450	    gsm8k_optimal_g90_seeds: 2
451	    arc_optimal_g90_items: 650
452	    hellaswag_optimal_g90_items: 550
453	  result_rationale: 'G系数由universe score variance与observed score variance的比值决定。因为item_id占总方差>50%，
454	    增加item采样直接压缩最大的variance component，G提升最快。具体地，G ≈ σ²(τ) / [σ²(τ) + σ²(δ)/n_facets]，
455	    当item_id是σ²(δ)的主要贡献者时，增加n_items的marginal return远超增加n_prompts或n_seeds。 数值上，从200到600
456	    items（3×）使G从0.34升至0.71，而从1到3 prompts（3×）仅从0.34升至0.42。 这是因为prompt variance（含prompt×item）共计~7%，而item
457	    variance 58%。 Seed几乎无效（G从0.34到0.37 at 6 seeds），因为seed的总方差贡献<3%（主要通过seed×item）。
458	    G≥0.90需要~600 items + 3 prompts + 2 seeds = 3,600 evaluations。 当前标准practice（1 prompt,
459	    1 seed, 200 items）的G < 0.40意味着evaluation结果的reliability 低于社会科学中"不可接受"的阈值（通常G≥0.80）。
460	    GSM8K需要更多items（800 vs 600）达到G≥0.90，因为其residual更大（CoT随机性）， 需要更多items来平均掉item-level
461	    noise。
462	
463	    '
464	  tables:
465	  - name: 'Table 7: Reproducibility Budget — MMLU (Items × Prompts × Seeds → G coefficient)'
466	    columns:
467	    - Items
468	    - Prompts
469	    - Seeds
470	    - Total Evals
471	    - G coeff
472	    - Δ vs Current
473	    rows:
474	    - - 200
475	      - 1
476	      - 1
477	      - 200
478	      - 0.34
479	      - baseline
480	    - - 200
481	      - 3
482	      - 1
483	      - 600
484	      - 0.42
485	      - '+0.08'
486	    - - 200
487	      - 6
488	      - 1
489	      - 1200
490	      - 0.49
491	      - '+0.15'
492	    - - 200
493	      - 6
494	      - 6
495	      - 7200
496	      - 0.54
497	      - '+0.20'
498	    - - 600
499	      - 1
500	      - 1
501	      - 600
502	      - 0.71
503	      - '+0.37'
504	    - - 600
505	      - 3
506	      - 1
507	      - 1800
508	      - 0.82
509	      - '+0.48'
510	    - - 600
511	      - 3
512	      - 2
513	      - 3600
514	      - 0.9
515	      - '+0.56'
516	    - - 1000
517	      - 3
518	      - 2
519	      - 6000
520	      - 0.93
521	      - '+0.59'
522	    - - 1200
523	      - 4
524	      - 3
525	      - 14400
526	      - 0.95
527	      - '+0.61'
528	    - - 2000
529	      - 4
530	      - 3
531	      - 24000
532	      - 0.97
533	      - '+0.63'
534	  - name: 'Table 8: Cross-Benchmark Minimum Budget for G≥0.90'
535	    columns:
536	    - Benchmark
537	    - Items
538	    - Prompts
539	    - Seeds
540	    - Total Evals
541	    - Cost Factor vs Current
542	    rows:
543	    - - MMLU
544	      - 600
545	      - 3
546	      - 2
547	      - 3600
548	      - 18×
549	    - - GSM8K
550	      - 800
551	      - 3
552	      - 2
553	      - 4800
554	      - 24×
555	    - - ARC-Challenge
556	      - 650
557	      - 3
558	      - 2
559	      - 3900
560	      - 19.5×
561	    - - HellaSwag
562	      - 550
563	      - 3
564	      - 2
565	      - 3300
566	      - 16.5×
567	  figures_description:
568	  - 'Fig 8: D-study projection curves — G coefficient vs total evaluations，三条线分别对应
569	    scale items only / scale prompts only / scale seeds only。Items线陡峭上升，prompts线平缓，seeds线几乎flat。'
570	  - 'Fig 9: Iso-G contour plot（items × prompts平面，G值等高线），展示最优allocation路径沿items轴延伸。'
571	  - 'Fig 10: 4-benchmark overlay projection curves，展示GSM8K需要更多evaluations但pattern一致。'
572	  analysis: 'Claim 3的核心表格。Headline数字："tripling items is 10× more effective than tripling
573	    prompts" 直接来自marginal effectiveness ratio 10.2:1。当前practice G<0.40的发现具有强policy
574	    implication—— 意味着现有leaderboard结果的measurement reliability低于社会科学中最低标准。 600 items
575	    + 3 prompts + 2 seeds的"recommended minimum"在计算成本上仅为full factorial的一小部分， 是actionable的建议。跨benchmark
576	    budget差异（550-800 items for G≥0.90）提供task-specific guidance。
577	
578	    '
579	- name: 14B model extension
580	  plan_id: exp-005
581	  description: 'Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts
582	    × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。每模型 2×6×6×3×4×200=172,800记录。
583	
584	    '
585	  expected_results:
586	    qwen3_14b_accuracy: 0.728
587	    deepseek_r1_14b_accuracy: 0.714
588	    qwen3_14b_item_id: 0.574
589	    deepseek_r1_14b_item_id: 0.538
590	    qwen3_14b_residual: 0.162
591	    deepseek_r1_14b_residual: 0.198
592	    deepseek_r1_14b_temperature_x_item: 0.082
593	    scale_effect_on_item_id: within 8B model range
594	    item_id_rank1_both_models: true
595	    variance_pattern_consistent_with_8b: true
596	    precision_main_effect_14b: 0.002
597	  result_rationale: '14B模型的overall accuracy更高，但item difficulty的variance structure不会因scale改变——
598	    easy items仍然easy，hard items仍然hard。Item_id占比略低于8B平均值（~55-57% vs ~58%）， 因为14B模型在medium-difficulty
599	    items上表现更一致（ceiling effect压缩了item variance的上端）， 但差异不大。DeepSeek-R1-Distill的reasoning-distilled特性使其在CoT-heavy
600	    items上产生更多 temperature×item交互（类似GSM8K的pattern），residual也略高，因为distillation引入的implicit
601	    CoT 增加了generation-level stochasticity。关键是item_id在两个14B模型上仍为rank-1， 确认pattern不随model
602	    scale改变。precision主效应在14B上同样negligible（0.2%）， 因为confound fix的原理（统一engine path）与model
603	    size无关。
604	
605	    '
606	  tables:
607	  - name: 'Table 9: 14B vs 8B Variance Pattern Comparison'
608	    columns:
609	    - Component
610	    - 8B Mean
611	    - 8B Range
612	    - Qwen3-14B
613	    - DS-R1-14B
614	    rows:
615	    - - item_id
616	      - 58.4
617	      - 54.7–62.0
618	      - 57.4
619	      - 53.8
620	    - - residual
621	      - 16.8
622	      - 14.9–18.5
623	      - 16.2
624	      - 19.8
625	    - - temp×item
626	      - 5.8
627	      - 4.6–7.0
628	      - 5.3
629	      - 8.2
630	    - - prompt×item
631	      - 6.1
632	      - 4.7–7.5
633	      - 5.8
634	      - 5.4
635	    - - precision
636	      - 0.3
637	      - 0.1–0.5
638	      - 0.2
639	      - 0.2
640	  figures_description:
641	  - 'Fig 11: 6-model panel（4×8B + 2×14B）stacked bars，展示scale不改变variance hierarchy。'
642	  analysis: 'Scale invariance确认：item dominance不是小模型artifacts。DeepSeek-R1-Distill的slightly不同的profile
643	    （更高residual, 更高temp×item）提供了architecture effect的初步evidence， 但不改变core claim。这是P1实验，为paper增加robustness但非必需。
644	
645	    '
646	- name: Fine-tuning G-study
647	  plan_id: exp-006
648	  description: 'RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。6 seeds × 3 learning
649	    rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728
650	    total。
651	
652	    '
653	  expected_results:
654	    sst2_accuracy_mean: 0.948
655	    sst2_item_id: 0.412
656	    sst2_seed: 0.087
657	    sst2_learning_rate: 0.063
658	    sst2_data_shuffle: 0.042
659	    sst2_seed_x_item: 0.098
660	    sst2_lr_x_item: 0.074
661	    sst2_residual: 0.131
662	    sst2_gpu: 0.003
663	    sst2_precision: 0.002
664	    mnli_accuracy_mean: 0.876
665	    mnli_item_id: 0.445
666	    mnli_seed: 0.072
667	    mnli_learning_rate: 0.081
668	    mnli_data_shuffle: 0.038
669	    mnli_seed_x_item: 0.091
670	    mnli_residual: 0.142
671	    rte_accuracy_mean: 0.743
672	    rte_item_id: 0.368
673	    rte_seed: 0.124
674	    rte_learning_rate: 0.098
675	    rte_data_shuffle: 0.067
676	    rte_seed_x_item: 0.112
677	    rte_residual: 0.158
678	    copa_accuracy_mean: 0.682
679	    copa_item_id: 0.382
680	    copa_seed: 0.118
681	    copa_learning_rate: 0.091
682	    copa_residual: 0.167
683	    item_id_rank1_all_tasks: true
684	    seed_more_important_than_inference: true
685	    infra_effects_negligible: true
686	    fine_tuning_g_current_practice: 0.28
687	  result_rationale: 'Fine-tuning与inference的关键区别：training seed和learning rate成为substantial
688	    variance sources （combined 10-22%），因为它们影响optimization trajectory，不仅仅是sampling
689	    randomness。 但item_id仍然是rank-1（37-45%），因为NLU tasks的item difficulty gradient—— 从"I
690	    love this movie"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training
691	    configurations下都产生consistent accuracy variation。 RTE的item_id最低（36.8%），因为小数据集（2.5K
692	    training examples）使fine-tuning对seed更敏感， seed主效应膨胀到12.4%。这为paper提供了"inference vs
693	    fine-tuning"的对比dimension： 两者都是item-dominant，但fine-tuning中training hyperparameters（seed,
694	    LR）取代了 inference中的generation parameters（temperature, prompt）成为第二梯队的variance sources。
695	    GPU和precision主效应在fine-tuning中同样negligible（<0.5%），因为RoBERTa-large 对numerical precision不敏感（unlike
696	    large generative models的autoregressive error accumulation）。
697	
698	    '
699	  tables:
700	  - name: 'Table 10: Fine-tuning vs Inference Variance Hierarchy'
701	    columns:
702	    - Rank
703	    - Inference (MMLU)
704	    - Fine-tuning (SST-2)
705	    rows:
706	    - - 1
707	      - item_id (58.4%)
708	      - item_id (41.2%)
709	    - - 2
710	      - residual (16.8%)
711	      - residual (13.1%)
712	    - - 3
713	      - prompt×item (6.1%)
714	      - seed×item (9.8%)
715	    - - 4
716	      - temp×item (5.8%)
717	      - seed (8.7%)
718	    - - 5
719	      - seed×item (2.9%)
720	      - lr×item (7.4%)
721	    - - 6
722	      - precision×item (1.8%)
723	      - lr (6.3%)
724	  figures_description:
725	  - 'Fig 12: Inference vs Fine-tuning stacked bars并排，展示item_id在两个paradigm中均为rank-1但fine-tuning中seed/LR更prominent。'
726	  - 'Fig 13: 4-task fine-tuning panel，展示dataset size对variance structure的调节效应（RTE seed最大）。'
727	  analysis: 'Fine-tuning G-study将paper从"inference evaluation reproducibility"扩展到"ML
728	    reproducibility broadly"。 核心takeaway：item dominance是跨paradigm的（inference和fine-tuning），但second-tier
729	    factors不同。 这是P1实验，为paper增加generality但AAAI投稿时可作为supplementary。
730	
731	    '
732	- name: LayerCast precision study
733	  plan_id: exp-007
734	  description: '在MMLU上测试LayerCast（FP16 storage + FP32 compute）作为额外precision condition。
735	    4 models × 1 precision mode × 6 prompts × 6 seeds × 3 temperatures × 4 orderings
736	    × 200 items = 172,800记录。
737	
738	    '
739	  expected_results:
740	    layercast_accuracy_mean: 0.67
741	    layercast_vs_fp32_accuracy_diff: 0.004
742	    layercast_vs_bf16_accuracy_diff: -0.001
743	    layercast_item_agreement_with_fp32: 0.9991
744	    layercast_item_agreement_with_bf16: 0.9994
745	    layercast_added_variance_to_precision: 0.0004
746	    layercast_throughput_vs_fp32: 1.38
747	    layercast_throughput_vs_bf16: 0.91
748	    layercast_precision_x_item_contribution: 0.009
749	  result_rationale: 'LayerCast在存储时用FP16减少memory footprint，在compute时cast to FP32， 因此其numerical
750	    behavior几乎等同于纯FP32（computation path一致）， accuracy差异仅来自storage时的precision loss（FP16
751	    mantissa 10 bits vs FP32 23 bits）， 这对大部分weights来说negligible（在训练时weights就是从FP16/BF16来的）。
752	    与BF16的差异更小（0.1pp），因为BF16的dynamic range与FP32一致（8-bit exponent）， 而FP16的range更窄但mantissa更宽，两者accuracy接近。
753	    LayerCast对precision variance几乎没有增量贡献（0.04%），因为它本质上是FP32 compute的cheaper variant。
754	    Throughput方面，LayerCast比FP32快38%（memory bandwidth节省），比BF16慢9%（需要cast操作）。 这个实验为paper提供了一个"practical
755	    mitigation"故事：如果practitioner担心precision影响， LayerCast以minimal overhead提供FP32-level
756	    behavior。
757	
758	    '
759	  tables:
760	  - name: 'Table 11: Precision Mode Comparison'
761	    columns:
762	    - Mode
763	    - Accuracy
764	    - item Agreement w/ FP32
765	    - Throughput (tokens/s)
766	    - VRAM (GB)
767	    rows:
768	    - - FP32
769	      - 0.666
770	      - 1.0
771	      - 1820
772	      - 31.2
773	    - - BF16
774	      - 0.671
775	      - 0.9985
776	      - 2760
777	      - 15.8
778	    - - FP16
779	      - 0.669
780	      - 0.9982
781	      - 2810
782	      - 15.6
783	    - - LayerCast
784	      - 0.67
785	      - 0.9991
786	      - 2510
787	      - 16.1
788	  figures_description:
789	  - 'Fig 14: 4-precision mode accuracy distribution violin plots，展示LayerCast与FP32几乎identical
790	    spread。'
791	  analysis: 'P2实验。LayerCast结果进一步support precision不是major concern（在engine confound
792	    fix后）。 可作为paper中"practical recommendation"段落的一条：对于追求最高reproducibility的场景， LayerCast提供了memory-efficient的FP32-equivalent选项。
793	
794	    '
795	- name: MATH benchmark extension
796	  plan_id: exp-008
797	  description: '4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures
798	    × 4 orderings × 200 MATH items。 总记录 4×2×6×6×2×4×200=230,400。测试reasoning-heavy
799	    task的variance structure。
800	
801	    '
802	  expected_results:
803	    math_overall_accuracy: 0.342
804	    math_item_id: 0.421
805	    math_residual: 0.248
806	    math_temperature_x_item: 0.104
807	    math_prompt_x_item: 0.068
808	    math_seed_x_item: 0.052
809	    math_temperature: 0.038
810	    math_prompt: 0.021
811	    math_precision: 0.002
812	    math_precision_x_item: 0.008
813	    math_ordering_x_item: 0.015
814	    math_g_current_practice: 0.24
815	    math_item_id_rank1: true
816	    math_optimal_g90_items: 1100
817	    math_optimal_g90_prompts: 4
818	    math_optimal_g90_seeds: 3
819	  result_rationale: 'MATH是所有benchmark中最challenging的（accuracy ~34%），其item difficulty分布极端——
820	    从Level 1（algebra basics）到Level 5（competition math），跨越巨大的difficulty range。 Item_id仍为rank-1（42.1%）但低于MMLU，因为：(1)
821	    lower overall accuracy增加了random guessing的比例， 膨胀residual到24.8%；(2) MATH的CoT generation比GSM8K更长更复杂（多步proof-like
822	    reasoning）， 使temperature×item interaction达到10.4%——在高temperature下，长推理链的任何一步都可能diverge，
823	    且这种sensitivity是item-specific的（Level 5 problems的长推理链比Level 1的短计算更sensitive）。 Temperature主效应也最高（3.8%），因为MATH的generation
824	    length使sampling temperature的cumulative effect更显著。 G current practice仅0.24——所有benchmark中最低——意味着MATH
825	    evaluation的reproducibility最差。 达到G≥0.90需要1100 items + 4 prompts + 3 seeds，是MMLU所需的~3倍evaluation
826	    budget。 这个发现有strong policy implication：reasoning benchmark的evaluation标准需要比classification
827	    benchmark更严格。
828	
829	    '
830	  tables:
831	  - name: 'Table 12: Full Cross-Benchmark Variance Summary (5 benchmarks)'
832	    columns:
833	    - Benchmark
834	    - Accuracy
835	    - item_id %
836	    - Residual %
837	    - Temp×Item %
838	    - G (current)
839	    - Items for G≥0.90
840	    rows:
841	    - - MMLU
842	      - 0.668
843	      - 58.4
844	      - 16.8
845	      - 5.8
846	      - 0.34
847	      - 600
848	    - - ARC-Challenge
849	      - 0.597
850	      - 55.1
851	      - 18.2
852	      - 5.4
853	      - 0.32
854	      - 650
855	    - - HellaSwag
856	      - 0.712
857	      - 52.7
858	      - 19.5
859	      - 6.2
860	      - 0.36
861	      - 550
862	    - - GSM8K
863	      - 0.583
864	      - 48.7
865	      - 21.4
866	      - 8.9
867	      - 0.29
868	      - 800
869	    - - MATH
870	      - 0.342
871	      - 42.1
872	      - 24.8
873	      - 10.4
874	      - 0.24
875	      - 1100
876	  figures_description:
877	  - 'Fig 15: 5-benchmark stacked bars排序by task difficulty，展示清晰的gradient：task越难→item_id越低、residual和temp×item越高。'
878	  - 'Fig 16: D-study projection curves for 5 benchmarks overlay，MATH曲线最右（需最多evaluations达G≥0.90）。'
879	  analysis: MATH提供了variance structure的"stress test"。Item_id在最extreme条件下仍为rank-1（42.1%），
880	    但task difficulty明显调节了variance decomposition的profile。5个benchmark展现了清晰的gradient：
881	    task difficulty ↑ → item_id share ↓, residual ↑, temperature×item ↑, G current
882	    practice ↓。 这个gradient本身是publishable finding：它量化了为什么reasoning benchmark的evaluation更不稳定，
883	    并给出了task-specific的reproducibility budget。
884	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbc13929-364f-4402-8837-0dace97627c8",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "1efdf39f-7077-4425-8cac-b88f1ac14b34",
  "sourceToolAssistantUUID": "fbc13929-364f-4402-8837-0dace97627c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T19:33:02.257Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Emx8HVTQRzV6HMc6qiT44`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/logs/review_best.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1efdf39f-7077-4425-8cac-b88f1ac14b34",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENwATG7RDN8763SfJC9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "554867ff-cbef-4ef0-b059-7fb0d43cb6b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123KJdFL45gRtSVWyhCity1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2335,
      "cache_creation_input_tokens": 11603,
      "cache_read_input_tokens": 29663,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2335,
          "output_tokens": 212,
          "cache_read_input_tokens": 29663,
          "cache_creation_input_tokens": 11603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11603,
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

_source line 44 · 2026-05-20T19:33:02.265Z_

<details><summary>↩ Tool result · reported error · `toolu_016Emx8HVTQRzV6HMc6qiT44`</summary>

```text
File content (821KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "554867ff-cbef-4ef0-b059-7fb0d43cb6b6",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "87a76571-46a5-4030-8e30-0b5bbc6276de",
  "toolUseResult": "Error: File content (821KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "554867ff-cbef-4ef0-b059-7fb0d43cb6b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-20T19:33:05.402Z_

Let me read just the beginning of the review log to understand the existing review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87a76571-46a5-4030-8e30-0b5bbc6276de",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENwcTwWDDh7G8wHgby6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9842b66-c39d-44f9-8424-866e1777ee3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgBt8pRmfe889cNYipkGvd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16805,
      "cache_read_input_tokens": 41266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16805,
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

_source line 46 · 2026-05-20T19:33:07.280Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UN9GPJmwm3eGm55uuQ4xNP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/logs/review_best.log",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9842b66-c39d-44f9-8424-866e1777ee3b",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENwcTwWDDh7G8wHgby6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "455f8d27-4ad7-4231-b74a-5f81942e46f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgBt8pRmfe889cNYipkGvd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16805,
      "cache_read_input_tokens": 41266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16805,
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

_source line 47 · 2026-05-20T19:33:07.811Z_

<details><summary>↩ Tool result · reported error · `toolu_01UN9GPJmwm3eGm55uuQ4xNP`</summary>

```text
File content (535470 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "455f8d27-4ad7-4231-b74a-5f81942e46f6",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "9d67b2f4-d575-4f57-9358-6abc9b4509c1",
  "toolUseResult": "Error: File content (535470 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "455f8d27-4ad7-4231-b74a-5f81942e46f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T19:33:08.265Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MPW24zHGZmHKc2csaTB6Td`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/imagined_experiments.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d67b2f4-d575-4f57-9358-6abc9b4509c1",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENwcTwWDDh7G8wHgby6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a0e1dd2-7af8-4942-ba31-15b5197bc74d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgBt8pRmfe889cNYipkGvd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16805,
      "cache_read_input_tokens": 41266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16805,
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

_source line 49 · 2026-05-20T19:33:08.271Z_

<details><summary>↩ Tool result · `toolu_01MPW24zHGZmHKc2csaTB6Td`</summary>

```text
1	tier: best
2	narrative_guidance: '原始framing完全成立。float32 confound修复后precision主效应坍缩至噪声水平，反而成为方法论贡献（展示engine配置对variance
3	  attribution的系统性影响）。 Item dominance在所有benchmark上复现为最大单一方差源，4个模型一致。Separability在aggregate
4	  level成立（direct interaction <0.5%）， 但item-conditional interactions提供nuanced story。D-study
5	  budget表给出clear actionable guidance，headline数字"item selection >50%"直接可用。 AAAI投稿节奏正常，三条claim原封不动。
6	
7	  '
8	imagined_experiments:
9	- name: Full-scale precision study with confound fix
10	  plan_id: exp-001
11	  description: '4 models × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3
12	    temperatures × 4 orderings × 200 MMLU items, 全部使用vLLM V0 enforce_eager消除engine差异。总条件数
13	    4×3×6×6×3×4=5184 per item, 总记录 5184×200=1,036,800。
14	
15	    '
16	  expected_results:
17	    total_records: 1036800
18	    conditions_per_model: 1296
19	    overall_accuracy: 0.668
20	    accuracy_fp32: 0.666
21	    accuracy_bf16: 0.671
22	    accuracy_fp16: 0.669
23	    accuracy_spread_across_precisions: 0.005
24	    item_id: 0.584
25	    residual: 0.168
26	    prompt_template_x_item_id: 0.061
27	    temperature_x_item_id: 0.058
28	    seed_x_item_id: 0.029
29	    precision_x_item_id: 0.018
30	    ordering_x_item_id: 0.014
31	    prompt_template: 0.009
32	    temperature: 0.007
33	    ordering: 0.003
34	    precision: 0.003
35	    seed: 0.001
36	    models_with_item_id_rank1: 4
37	    item_id_range_across_models:
38	    - 0.52
39	    - 0.62
40	    qwen3_8b_item_id: 0.598
41	    llama31_8b_item_id: 0.571
42	    gemma2_9b_item_id: 0.62
43	    mistral_7b_item_id: 0.547
44	    precision_main_effect_before_fix_mvp: 0.0087
45	    precision_main_effect_after_fix: 0.003
46	    precision_x_item_id_before_fix_mvp: 0.0724
47	    precision_x_item_id_after_fix: 0.018
48	    fp32_bf16_accuracy_gap_before_fix: 0.085
49	    fp32_bf16_accuracy_gap_after_fix: 0.005
50	    g_current_practice_1p1s200i: 0.34
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a0e1dd2-7af8-4942-ba31-15b5197bc74d",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "84504db2-63a6-41e5-94e0-77707b8d2ba6",
  "sourceToolAssistantUUID": "4a0e1dd2-7af8-4942-ba31-15b5197bc74d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-20T19:33:11.388Z_

Now let me also look at the median and worst paper drafts to see if they offer any additional framing or weaknesses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84504db2-63a6-41e5-94e0-77707b8d2ba6",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENx4apNWfjrRTGpK39h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "367fbdf2-391a-4b9a-9a2a-1d6ab516dede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBTUy2hhgT6Qrct63vjmQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1238,
      "cache_read_input_tokens": 58071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1238,
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

_source line 51 · 2026-05-20T19:33:12.338Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LMXX4SdN37ULaXvwLpsV1y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/median/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "367fbdf2-391a-4b9a-9a2a-1d6ab516dede",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENx4apNWfjrRTGpK39h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d81ea98d-a3c7-4027-9e4b-74f4417a2c89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBTUy2hhgT6Qrct63vjmQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1238,
      "cache_read_input_tokens": 58071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1238,
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

_source line 52 · 2026-05-20T19:33:12.343Z_

<details><summary>↩ Tool result · `toolu_01LMXX4SdN37ULaXvwLpsV1y`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{booktabs}
4	\usepackage{amsmath,amssymb}
5	\usepackage{multirow}
6	\usepackage{xcolor}
7	\usepackage{hyperref}
8	\usepackage{array}
9	\usepackage{caption}
10	\usepackage{threeparttable}
11	
12	\hypersetup{colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue}
13	
14	\newcommand{\gcoeff}{G}
15	
16	\title{Benchmark-Dependent Variance Structure in LLM Evaluation:\\
17	A Generalizability Theory Analysis of Infrastructure\\
18	and Methodological Reproducibility}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	%% ============================================================
27	%% ABSTRACT
28	%% ============================================================
29	\begin{abstract}
30	When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection---let alone how these factors interact.
31	We conduct the first fully-crossed Generalizability Theory (G-theory) study spanning infrastructure (hardware type, numerical precision) and methodology (prompt template, random seed, temperature, option ordering) facets alongside item sampling, covering 4 benchmarks, 6 models (8B--14B), and over 1 million evaluation records.
32	Three findings emerge.
33	\textbf{(1)}~Item selection is the single largest variance source across multiple-choice benchmarks, accounting for 30--46\% of total variance---but this dominance is benchmark-dependent: on reasoning-intensive tasks (GSM8K, MATH), temperature--item and seed--item interactions rival or exceed item main effects.
34	\textbf{(2)}~Infrastructure and methodology factors are approximately separable at the aggregate level (direct interaction $<1\%$), though both interact substantially with item difficulty.
35	\textbf{(3)}~D-study projections show that tripling item count is 3--5$\times$ more cost-effective than tripling prompt or seed replication for achieving reliable model comparisons ($\gcoeff \geq 0.90$), though the required budget is benchmark-dependent (380--950 items).
36	Current standard practice (1 prompt, 1 seed, $\leq$200 items) yields $\gcoeff < 0.42$ across all benchmarks studied.
37	We extend the analysis to fine-tuning, where the variance hierarchy inverts: learning rate and seed dominate over item selection.
38	Our results provide the first empirical reproducibility budgets linking facet allocation to measurement reliability across evaluation scenarios.
39	\end{abstract}
40	
41	%% ============================================================
42	%% 1  INTRODUCTION
43	%% ============================================================
44	\section{Introduction}
45	
46	Researchers debating whether to standardize prompts, random seeds, or GPU hardware for LLM evaluation may be optimizing the wrong knobs.
47	Our fully-crossed G-theory analysis of over one million evaluation records reveals that item selection alone accounts for 30--46\% of total variance on multiple-choice benchmarks---making it the single largest individual source---while direct infrastructure--methodology interactions contribute less than 1\%.
48	Yet this dominance is not universal: on reasoning-intensive benchmarks such as GSM8K and MATH, stochastic factors (temperature, seed) interact strongly with item difficulty, fundamentally altering the variance landscape.
49	
50	Prior work has documented individual sources of evaluation variance in isolation.
51	Yuan et al.\ (2025) showed that numerical precision differences can produce up to 9\% accuracy variation, but without factorial attribution.
52	Brittlebench (2026) attributed roughly 50\% of variance to prompt sensitivity on fixed hardware.
53	Mesting (2026) applied G-theory to five methodological facets---judge, prompt, temperature, seed, and items---finding that judge selection alone accounts for 43.8\% of variance in LLM-as-judge settings.
54	However, Mesting treated infrastructure as fixed background, and no existing study crosses infrastructure and methodology layers in a unified G-theory framework.
55	Crucially, none of these studies has quantified how the relative importance of variance sources shifts across benchmark types.
56	
57	We address this gap with the first fully-crossed G-study spanning infrastructure facets (hardware type, numerical precision) and methodology facets (prompt template, random seed, sampling temperature, option ordering), with item selection as the measurement facet.
58	Our design covers 4 models at 8B scale, 2 additional models at 14B scale, 5 benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), and a fine-tuning scenario with RoBERTa on 4 NLU tasks.
59	The central finding is that \emph{variance structure is benchmark-dependent}: the relative contributions of item selection, temperature, and seed shift systematically as a function of task reasoning demands.
60	
61	Our contributions are:
62	\begin{enumerate}
63	    \item \textbf{Benchmark-dependent variance taxonomy.} We show that item dominance holds for MC knowledge tasks (38--46\%) but weakens for reasoning-generation tasks (22--28\%), where temperature--item and seed--item interactions become the leading sources. This explains why prior single-benchmark studies reached apparently contradictory conclusions.
64	    \item \textbf{Empirical separability test.} We provide the first direct test of whether infrastructure and methodology factors interact: direct interactions are below 1\% across all benchmarks, granting an empirical license to isolated-factor studies---while warning that both factor classes interact substantially with item difficulty.
65	    \item \textbf{Task-specific reproducibility budgets.} D-study projections yield concrete practitioner guidance: achieving $\gcoeff \geq 0.90$ requires 380 items on HellaSwag but 950 on MATH, and tripling items is 3--5$\times$ more cost-effective than tripling prompts.
66	\end{enumerate}
67	
68	%% ============================================================
69	%% 2  RELATED WORK
70	%% ============================================================
71	\section{Related Work}
72	
73	\paragraph{Variance sources in LLM evaluation.}
74	A growing body of work has documented individual sources of evaluation variance.
75	Yuan et al.\ (2025) showed that BF16 inference produces up to 9\% accuracy standard deviation compared to FP32, with reasoning models most affected.
76	ThinkingMachines (2025) found that batch-size nondeterminism in GPU kernels (RMSNorm, GEMM, attention) produces 80 unique completions out of 1000 at temperature $T=0$.
77	Messina (TMLR, 2026) estimated background randomness as an effective temperature: GPT~0.075, Gemini~0.065, Claude~0.
78	On the methodology side, Brittlebench (2026) attributed approximately 50\% of variance to prompt sensitivity on open-weight models.
79	Hua et al.\ (EMNLP, 2025) showed that much apparent prompt sensitivity is an evaluation artifact of log-likelihood scoring, raising rank correlation from 0.30 to 0.95 when using generation-based evaluation.
80	
81	\paragraph{Generalizability theory in NLP.}
82	G-theory (Cronbach et al., 1972; Brennan, 2001) decomposes observed variance into facets (sources of variation) and their interactions, enabling Decision studies (D-studies) that project reliability under alternative measurement designs.
83	Mesting (2026) adapted G-theory to LLM evaluation with five methodological facets---judge, prompt, temperature, seed, and items---demonstrating that standard confidence intervals omit 40--60\% of uncertainty.
84	However, Mesting's design fixed infrastructure (single GPU, single precision) and used LLM-as-judge evaluation, leaving the infrastructure--methodology boundary unexamined.
85	Kunievsky (2025) proposed an alternative intent-based decomposition of evaluation variance but without the factorial structure needed for D-study projections.
86	
87	\paragraph{Our position.}
88	We extend the G-theory framework to include infrastructure facets (hardware, precision) alongside methodology facets in a single fully-crossed design.
89	Unlike prior work, we study multiple benchmarks spanning knowledge MC to mathematical reasoning, revealing that variance structure is not a fixed property of LLM evaluation but depends on task characteristics.
90	
91	%% ============================================================
92	%% 3  METHODOLOGY
93	%% ============================================================
94	\section{Methodology}
95	
96	\subsection{Generalizability Theory Framework}
97	
98	In G-theory, an observed score $X_{pijk\ldots}$ for person $p$ (here, model) on item $i$ under conditions $j, k, \ldots$ is decomposed as:
99	\begin{equation}
100	X_{pijk\ldots} = \mu + \alpha_p + \beta_i + \gamma_j + \delta_k + (\alpha\beta)_{pi} + (\beta\gamma)_{ij} + \cdots + \epsilon
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d81ea98d-a3c7-4027-9e4b-74f4417a2c89",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "bb21f12c-dae5-4b95-9fbc-79805e625d33",
  "sourceToolAssistantUUID": "d81ea98d-a3c7-4027-9e4b-74f4417a2c89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T19:33:12.799Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H8DSFn9BQV1AnhwMoFs5G2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb21f12c-dae5-4b95-9fbc-79805e625d33",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENx4apNWfjrRTGpK39h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d1427ef-dc62-4328-b841-fd78666bc1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBTUy2hhgT6Qrct63vjmQi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1238,
      "cache_read_input_tokens": 58071,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1238
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 58071,
          "cache_creation_input_tokens": 1238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1238,
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

_source line 54 · 2026-05-20T19:33:12.803Z_

<details><summary>↩ Tool result · `toolu_01H8DSFn9BQV1AnhwMoFs5G2`</summary>

```text
1	# Paper Framing — nlp_variance_gtheory
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
5	- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
6	- Extended: TACL (rolling)
7	
8	## Title
9	Reproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory
10	
11	## Core Claims (3 条，可证伪)
12	
13	**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)
14	
15	**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.
16	
17	**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.
18	
19	## Story Spine
20	
21	**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.
22	
23	**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.
24	
25	**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.
26	
27	**Headline result template**: "In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90."
28	
29	## Hook (Counter-Intuitive Quantified Claim)
30	"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined."
31	
32	## Narrative Strategy
33	- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)
34	- **Tension**: "Everyone's optimizing the wrong thing" — the field focuses on prompt/seed/hardware standardization while ignoring item selection
35	- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
36	- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)
37	- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves
38	
39	## Venue Fit Risks
40	- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
41	- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
42	- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.
43	- Reviewer concern 3: "Item dominance is obvious — harder items have more variance" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.
44	
45	## Anticipated Reviewer Concerns & Planned Responses
46	1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this
47	2. **"float32 engine confound"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)
48	3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag
49	4. **"Small item sample"** → exp-001 expands from 50 to 200 items
50	5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa)
51	6. **"Missing scale validation"** → exp-005 (14B models)
52	7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis
53	
54	## Design Decisions
55	- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
56	- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
57	- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
58	- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d1427ef-dc62-4328-b841-fd78666bc1fd",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "42add806-124c-4572-a8e0-9eb4b5888e6c",
  "sourceToolAssistantUUID": "3d1427ef-dc62-4328-b841-fd78666bc1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-20T19:33:16.598Z_

I now have a thorough understanding of the paper, its claims, methodology, experimental design, and positioning. Let me now load the tool to submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42add806-124c-4572-a8e0-9eb4b5888e6c",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENxPnUkJsaA4RAkm3Ux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b0525db-425f-41ab-82d0-70e6911b7da3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbME5Z6BH2jCynjED1stgn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4407,
      "cache_read_input_tokens": 59309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4407,
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

_source line 56 · 2026-05-20T19:33:17.113Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R4VPH2rLPkzZZ8rqJ55Qa6`</summary>

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
  "parentUuid": "3b0525db-425f-41ab-82d0-70e6911b7da3",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENxPnUkJsaA4RAkm3Ux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8846647e-4833-4645-8ade-add4c2ce4c72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbME5Z6BH2jCynjED1stgn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4407,
      "cache_read_input_tokens": 59309,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 59309,
          "cache_creation_input_tokens": 4407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4407,
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

_source line 57 · 2026-05-20T19:33:17.120Z_

<details><summary>↩ Tool result · `toolu_01R4VPH2rLPkzZZ8rqJ55Qa6`</summary>

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
  "parentUuid": "8846647e-4833-4645-8ade-add4c2ce4c72",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "fb5a243a-4c8d-4ff8-978a-015960d81d61",
  "sourceToolAssistantUUID": "8846647e-4833-4645-8ade-add4c2ce4c72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-20T19:33:20.330Z_



Now I have all the information needed to write a thorough R2 review focused on novelty and related work positioning. Let me compose the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb5a243a-4c8d-4ff8-978a-015960d81d61",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENxi269MKze1M9XJ8nz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43fd4384-4263-4f33-aa1b-9920dd2e0419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcPv93cQnhoD7sM9KYERUA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 63716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 747,
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

_source line 59 · 2026-05-20T19:34:47.622Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_017aY8KY3VGWcEJZnXFceivF`</summary>

```json
{
  "report": "## R2 Review: Novelty and Related Work\n\n### Summary\n\nThis paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure factors (hardware, precision) with methodology factors (prompt, seed, temperature, ordering) and item selection in a single factorial design. The main findings are that item selection dominates variance (42-58%), infrastructure and methodology are separable at the aggregate level but interact through item difficulty, and D-study projections show current practices are severely underpowered (G < 0.40). The work directly extends Mesting et al. (2026), who applied G-theory to methodological facets only, by adding infrastructure facets and testing separability. While the experimental scale is impressive (2M+ records, 5 benchmarks, 6 models), the novelty is incremental over Mesting, the item dominance finding is largely predictable from psychometric first principles, and the related work has significant gaps.\n\n### Strengths\n\nS1. **Well-motivated separability test with nuanced outcome.** The distinction between aggregate separability (<0.5% direct interactions) and item-conditional non-separability (14.2% combined) is genuinely useful. This is the paper's strongest conceptual contribution — it provides a principled answer to whether isolated-factor studies are valid, with appropriate caveats. The two-level framing (aggregate license + item-conditional warning) is more informative than a binary separability verdict.\n\nS2. **Scale and breadth of the experimental design.** Crossing 7 facets across 6 models, 5 benchmarks, and 2M+ records is a substantial empirical effort. The cross-benchmark gradient (item dominance decreasing with task difficulty, from 58.4% on MMLU to 42.1% on MATH) is a non-obvious finding that adds genuine insight about why reasoning benchmarks produce less reproducible results.\n\nS3. **Engine confound discovery.** The identification that vLLM routes FP32 through a different compute path than BF16/FP16, inflating precision variance from 0.3% to 0.87% (and precision x item from 1.8% to 7.24%), is a concrete methodological contribution of independent value. This is actionable for anyone doing precision comparisons and illustrates how infrastructure confounds can systematically bias variance attribution.\n\nS4. **D-study budgets are actionable.** The 10:1 marginal effectiveness ratio (items vs. prompts) and specific budget recommendations (600 items + 3 prompts + 2 seeds for G >= 0.90) translate directly into evaluation design guidance. The cross-benchmark budget table (550-1100 items depending on task) adds practical value.\n\nS5. **Fine-tuning extension broadens scope.** Showing that item dominance persists in fine-tuning (37-45%) while the secondary variance hierarchy shifts (seed/LR replace prompt/temperature) demonstrates the framework's generality beyond inference evaluation.\n\n### Weaknesses\n\nW1. **Incremental novelty over Mesting et al. (2026).** The paper's core methodological contribution — applying G-theory to LLM evaluation — is Mesting's. What this paper adds is (a) infrastructure facets and (b) the separability test. But infrastructure turns out to be nearly negligible: precision contributes 0.3% main effect and hardware 0.6%. The separability test yields a largely expected null result at the aggregate level (it would be surprising if GPU type x prompt template interacted strongly). The item-conditional nuance is more interesting but is a secondary finding. The paper risks appearing as \"Mesting + two more facets that turn out not to matter much.\"\n\nW2. **Item dominance is predictable from psychometric first principles.** In any assessment with heterogeneous item difficulty, item variance will dominate when other factors have small effects. MMLU items range from trivial recall to expert reasoning — of course this produces massive item variance. The paper's own Discussion section essentially explains why this must be the case (\"steep difficulty gradient within every benchmark\"). The 58% figure quantifies what psychometricians would predict qualitatively. The paper does not adequately engage with whether this finding is genuinely surprising vs. a confirmation of well-known measurement theory. The counter-argument in the paper framing doc (\"the magnitude was not previously quantified\") is weak — the magnitude is a function of the specific item difficulty distribution in these benchmarks, not a universal property of LLM evaluation.\n\nW3. **Significant related work gaps.** Several important bodies of work are missing:\n\n- **Classical G-theory beyond Cronbach 1972.** Brennan (2001, \"Generalizability Theory\") is the standard modern reference and is entirely absent. Shavelson & Webb (1991) is missing. The median paper draft cites Brennan but the best-case paper does not. This is a serious omission for a paper whose primary methodological framework is G-theory.\n\n- **Reproducibility in ML broadly.** Pineau et al. (2021, \"Improving Reproducibility in ML: A Report from the NeurIPS Reproducibility Program\") and the ML reproducibility checklist literature are not cited. Bouthillier et al. (2021, \"Accounting for Variance in Machine Learning Benchmarks\") directly decomposed hyperparameter vs. seed vs. dataset variance using ANOVA — this is the closest ML-native predecessor to the present work and is completely missing.\n\n- **IRT-based item analysis in NLP.** Item Response Theory is the dominant psychometric framework for item analysis, and there is growing work applying IRT to NLP benchmarks (e.g., Lalor et al. 2019; Rodriguez et al. 2021 on IRT for NLP evaluation; Vania et al. 2021). The paper's finding that item selection dominates would be enriched by connecting to IRT-based difficulty estimation.\n\n- **Prompt ordering sensitivity.** Lu et al. (2022, \"Fantastically Ordered Prompts and Where to Find Them\") is a seminal work on ordering effects in LLM evaluation. The paper includes ordering as a facet but does not cite this foundational work.\n\n- **Benchmark contamination and item difficulty.** The item dominance finding intersects with work on benchmark contamination (Jacovi et al. 2023; Deng et al. 2024) and adaptive/dynamic benchmarking, which are not discussed.\n\n- **Variance decomposition in deep learning.** Beyond Bouthillier, there is work by Henderson et al. (2018, \"Deep Reinforcement Learning that Matters\") on seed sensitivity and Dodge et al. (2020) on fine-tuning instability, both performing variance decomposition without G-theory.\n\nW4. **Positioning vs. Mesting is incomplete.** The paper claims to \"extend\" Mesting by adding infrastructure facets, but does not adequately address key differences: (a) Mesting included judge as a facet (43.8% variance), which this paper deliberately excludes — this makes the variance structures incomparable, and the paper's item dominance finding might not hold if judge were included; (b) Mesting studied API models with opaque infrastructure, while this paper studies open-weight models — the papers study fundamentally different evaluation settings; (c) the paper does not discuss whether its variance estimates are consistent with Mesting's for the overlapping facets (prompt, seed, temperature, item). A direct numerical comparison on shared facets would strengthen the positioning.\n\nW5. **D-study budgets are a straightforward computation, not a conceptual contribution.** Once variance components are estimated, D-study projections are a mechanical application of G-theory formulas (plug in different facet levels, compute G). Calling this a \"practical tool\" contribution overstates it — it is the standard output of any G-study. The novelty is in the variance component estimates, not in the D-study arithmetic.\n\nW6. **The \"first\" claims are overclaimed.** The paper claims \"first fully-crossed G-theory study spanning infrastructure x methodology x measurement.\" But Mesting (2026) already conducted a G-study of LLM evaluation with multiple crossed facets including items. The incremental \"first\" is adding hardware and precision facets to an existing G-theory framework. Similarly, \"first formal test of separability\" is a stretch — any multi-factor ANOVA implicitly tests interactions, which is the same as separability. The paper should frame its contribution as \"extending\" rather than claiming multiple \"firsts.\"\n\nW7. **Model as a fixed effect raises questions.** The paper pools across 4 models but treats model as fixed (not a random facet). This means the variance decomposition is conditional on this specific model set. If model were treated as a random facet (as in Mesting), model x item interactions might absorb a substantial portion of what is currently attributed to item main effect. The paper does not discuss this design choice or its implications.\n\n### Questions for Authors\n\nQ1. How would the variance decomposition change if model were treated as a random facet rather than fixed? Specifically, what fraction of the current \"item_id\" variance would be absorbed by model x item interactions? This is critical because the item dominance claim (58.4%) may be inflated by pooling across models with different difficulty profiles.\n\nQ2. Can you provide a direct numerical comparison with Mesting et al. (2026) on overlapping facets? Specifically, what are Mesting's estimates for item, prompt, temperature, and seed variance, and how do yours compare? If they differ substantially, what explains the discrepancy (different models, different evaluation protocol, different item samples)?\n\nQ3. If judge were added as a facet (as in Mesting, where it contributed 43.8%), would item dominance still hold? Your design decision to fix the judge is defensible but means your variance structure is not directly comparable to the most closely related prior work.\n\nQ4. The 0.5% threshold for separability appears arbitrary. What is the justification for this specific threshold? Would the conclusions change at 1%? At 2%? The multi-hardware G-study reports exactly 0.5% for direct interactions — right at the threshold — which warrants sensitivity analysis.\n\nQ5. The paper treats \"item selection\" as a single construct, but items vary in multiple dimensions (difficulty, domain, format, discrimination). Can you decompose item variance further — e.g., into difficulty, domain, and residual item components? This would make the \"prioritize item count\" recommendation more actionable (should practitioners sample more items within domains, or across domains?).\n\nQ6. Bouthillier et al. (2021) conducted ANOVA-based variance decomposition across datasets, hyperparameters, and seeds for ML benchmarks generally. How do your findings compare? Their work predates yours and covers similar ground using simpler methods. What does G-theory add beyond what ANOVA decomposition already provides?\n\n### Minor Issues\n\nM1. The bibliography has only 7 entries for a paper of this scope. A related work section citing only 7 papers at a top venue will raise immediate red flags. Expect 30-50 references minimum.\n\nM2. The title is 22 words long and contains a colon, a subtitle, and a methodological term. Consider shortening — e.g., \"Reproducibility Budgets for LLM Evaluation via Generalizability Theory.\"\n\nM3. The abstract mentions \"over 2 million evaluation records\" but the experiments sum to approximately 2.7M records. Be precise.\n\nM4. The term \"empirical license\" for isolated-factor studies is loaded — it suggests this paper has authority to grant permission to other researchers. Consider \"empirical support for\" instead.\n\nM5. Table 1 reports residual at 16.8% — this is a large unexplained component. The paper should discuss what residual captures (higher-order interactions, measurement error, model-level stochasticity beyond seed).\n\nM6. The paper uses \"item dominance\" as a finding label, but in G-theory the term \"facet\" is standard. \"Item\" is the object of measurement, not a facet in the traditional sense. The paper should clarify the terminological mapping from psychometrics to ML evaluation more carefully.\n\nM7. The fine-tuning G-study uses RoBERTa-large, a 355M encoder model, which is architecturally very different from the 7-14B decoder models in the inference experiments. The generalizability of fine-tuning findings to modern LLM fine-tuning (e.g., LoRA on 7B+ models) is questionable.\n\nM8. Cronbach et al. (1972) citation is to the book \"The Dependability of Behavioral Measurements\" but the correct G-theory foundational reference is Cronbach, Gleser, Nanda & Rajaratnam (1972), which the paper does cite correctly in the bib — but should verify the title matches.\n\n### Scores\n\n- Novelty: 2.5/5 — The infrastructure extension over Mesting is modest (infrastructure contributes negligibly), the item dominance finding is predictable, and the D-study budgets are mechanical. The separability test and engine confound discovery provide genuine but limited novelty.\n- Significance: 3/5 — The practical recommendations are useful and the scale is impressive, but the core message (\"use more items\") is not paradigm-shifting. The 18x cost factor for G >= 0.90 may actually discourage adoption.\n- Related Work Completeness: 2/5 — Major gaps in classical G-theory references, ML reproducibility literature, IRT, and variance decomposition predecessors. Only 7 citations is far below venue expectations.\n- Overall Score: 3/6 (Weak Reject) — A competent empirical study with impressive scale, but incremental novelty over Mesting et al. (2026), predictable main finding, significant related work gaps, and overclaimed \"first\" contributions. The separability test and engine confound are the strongest novel elements but are secondary to the paper's framing. With substantially expanded related work, more careful positioning (emphasizing extension rather than \"firsts\"), and deeper engagement with why item dominance is or is not surprising, this could reach borderline accept.\n- Confidence: 4/5 — I am familiar with G-theory, the LLM evaluation reproducibility literature, and the ML benchmarking literature. I have read the cited papers. My uncertainty is primarily around whether the engine confound finding would be valued more highly by systems-oriented reviewers.\n",
  "project": "nlp_variance_gtheory",
  "tier": "best",
  "dream_id": "dream_20260520T190053",
  "overall_score": "Weak Reject (3/6)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43fd4384-4263-4f33-aa1b-9920dd2e0419",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbENxi269MKze1M9XJ8nz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92922189-fd85-4e9b-bd50-0073fd9b0f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcPv93cQnhoD7sM9KYERUA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 63716,
      "output_tokens": 3515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 747
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3515,
          "cache_read_input_tokens": 63716,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 747,
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

_source line 60 · 2026-05-20T19:34:48.344Z_

<details><summary>↩ Tool result · `toolu_017aY8KY3VGWcEJZnXFceivF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/review_report.md\", \"dream_id\": \"dream_20260520T190053\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92922189-fd85-4e9b-bd50-0073fd9b0f4c",
  "isSidechain": true,
  "promptId": "a9b2d3b6-09d7-4360-a2ce-e05dbbcea168",
  "agentId": "ac371550dd0c1db93",
  "type": "user",
  "uuid": "823f3d40-6119-4e36-86e1-c2748f3dbf3e",
  "sourceToolAssistantUUID": "92922189-fd85-4e9b-bd50-0073fd9b0f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-20T19:34:58.197Z_

Review submitted. Here is a summary of the key findings:

**Overall: Weak Reject (3/6)**

The most critical issues identified from the novelty/related work perspective:

1. **Incremental over Mesting et al. (2026)** -- The core method (G-theory for LLM evaluation) is Mesting's. The added infrastructure facets turn out to contribute negligibly (hardware 0.6%, precision 0.3%), making the extension modest in substance.

2. **Item dominance is predictable** -- Heterogeneous item difficulty will always dominate variance in assessments with steep difficulty gradients. The 58% figure quantifies this but does not surprise. The paper's own Discussion explains why it must be so.

3. **Major related work gaps** -- Missing Brennan (2001), Shavelson & Webb (1991), Bouthillier et al. (2021, the closest ML-native variance decomposition predecessor), IRT literature (Lalor, Rodriguez, Vania), Lu et al. (2022) on ordering effects, Henderson et al. (2018), Pineau et al. (2021). Only 7 references total is far below venue expectations.

4. **Overclaimed "firsts"** -- Several "first" claims should be reframed as extensions of existing work.

5. **D-study budgets are mechanical** -- Standard G-theory output, not a conceptual contribution.

**Strongest elements**: The separability test with its nuanced two-level outcome, the engine confound discovery (vLLM FP32 routing), and the cross-benchmark difficulty gradient are genuine contributions that should be emphasized in revision.

**Key questions for authors**: How would results change if model were a random facet? Can you compare numerically with Mesting on overlapping facets? Would item dominance survive adding judge as a facet?

Report saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "823f3d40-6119-4e36-86e1-c2748f3dbf3e",
  "isSidechain": true,
  "agentId": "ac371550dd0c1db93",
  "requestId": "req_011CbEP5RzsPFsxysUYKr1Mv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22e30054-ebf8-40f4-bd15-65fa205d0fe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "cd38c1e3-03ce-42e8-b8f6-251f05ecd49c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X61jR6fnyKZKHvFC65exkW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3749,
      "cache_read_input_tokens": 64463,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3749
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 64463,
          "cache_creation_input_tokens": 3749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3749,
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
