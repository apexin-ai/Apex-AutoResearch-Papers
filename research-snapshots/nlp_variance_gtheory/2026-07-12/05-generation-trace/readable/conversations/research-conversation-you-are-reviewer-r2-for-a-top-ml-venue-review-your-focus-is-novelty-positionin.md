# Research conversation: You are Reviewer R2 for a top ML venue review. Your focus is **novelty, positioning, and related work**. Evaluate the pa

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-adac42d84d8448a91.jsonl`
- **Structured JSON:** [`fc30bcd4f3e6b737f649.json`](../../sessions/fc/fc30bcd4f3e6b737f649.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-20T19:38:55.860Z_

You are Reviewer R2 for a top ML venue review. Your focus is **novelty, positioning, and related work**. Evaluate the paper below using a 6-point scale (1=Strong Reject, 6=Strong Accept), with acceptance rate ~25%.

## Paper Summary

**Title:** Benchmark-Dependent Variance Structure in LLM Evaluation: A Generalizability Theory Analysis of Infrastructure and Methodological Reproducibility

**Core claims:**
1. Item selection is the single largest variance source across MC benchmarks (30–46%), but this dominance is benchmark-dependent: on reasoning tasks (GSM8K, MATH), temperature–item and seed–item interactions rival or exceed item main effects.
2. Infrastructure and methodology factors are approximately separable at the aggregate level (direct interaction < 1%), though both interact substantially with item difficulty.
3. D-study projections show tripling item count is 3–5× more cost-effective than tripling prompts or seeds for G ≥ 0.90, but required budgets are benchmark-dependent (380–950 items).

The paper extends the analysis to fine-tuning (RoBERTa-large on GLUE/SuperGLUE), showing the variance hierarchy inverts: LR and seed dominate over item selection.

**Methodology:**
- G-theory framework (Cronbach et al., 1972; Brennan, 2001) applied to LLM evaluation with infrastructure facets
- Three facet layers: Infrastructure (hardware type, numerical precision), Methodology (prompt template, random seed, sampling temperature, option ordering), Measurement (items)
- 6 models (4×8B, 2×14B), 5 benchmarks (MMLU, ARC-C, HellaSwag, GSM8K, MATH), fine-tuning with RoBERTa-large
- Over 1 million evaluation records
- vLLM 0.9.2 with V0 engine and enforce_eager=True to fix float32 confound

**Related work cited:**
1. Yuan et al. (2025, ICML) — BF16 vs FP32 produces up to 9% accuracy SD
2. ThinkingMachines (2025, arXiv) — batch-size nondeterminism in GPU kernels, 80 unique completions at T=0
3. Messina (2026, TMLR) — background randomness as effective temperature
4. Brittlebench (2026, NAACL) — ~50% of variance from prompt sensitivity
5. Hua et al. (2025, EMNLP) — prompt sensitivity is evaluation artifact of log-likelihood scoring
6. Mesting (2026, AAAI) — G-theory for LLM evaluation, 5 methodology facets (judge, prompt, temp, seed, items), judge=43.8%, but fixed infrastructure and used LLM-as-judge
7. Kunievsky (2025, ACL) — intent-based decomposition without factorial structure
8. Cronbach et al. (1972) and Brennan (2001) — classical G-theory references

**Claimed contributions:**
1. Benchmark-dependent variance taxonomy: item dominance holds for MC knowledge tasks (38–46%) but weakens for reasoning-generation tasks (22–28%)
2. Empirical separability test: first direct test of infrastructure×methodology interaction (<1% across all benchmarks)
3. Task-specific reproducibility budgets: D-study projections with concrete numbers (380–950 items for G≥0.90)

**Key positioning:** "First fully-crossed G-study spanning infrastructure and methodology facets" — Mesting (2026) did G-theory but with fixed infrastructure and LLM-as-judge. This paper adds hardware type and precision as facets.

## Your Review Task

Evaluate:
1. **Novelty**: How novel is each contribution? Is the "benchmark-dependent variance structure" finding surprising or expected? Is adding infrastructure facets to G-theory a meaningful extension? How does the fine-tuning extension add value?
2. **Related work coverage**: Are there missing related works? Is the positioning against Mesting (2026) fair and accurate? Are there relevant works on evaluation reproducibility, variance decomposition, or measurement theory that should be cited?
3. **Significance and impact**: Will this paper change how people do LLM evaluation? Are the practical recommendations actionable? Is the "benchmark-dependent" framing a genuine insight or obvious in retrospect?
4. **Writing quality**: Is the paper well-organized? Are the claims calibrated to the evidence? Is the abstract accurate?
5. **Scope and ambition**: Is covering 8 experiments in 13 pages too ambitious? Does breadth come at the cost of depth?

Consider these potential gaps in related work:
- Other measurement theory approaches in NLP (IRT, classical test theory)
- Prior work on benchmark subsampling (e.g., HELM-lite, mini-benchmarks)
- Work on evaluation contamination, memorization effects
- Multi-seed reporting conventions and their justification
- Prior variance decomposition studies outside G-theory

Provide:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: minor/moderate/major)
- Questions for authors (numbered)
- Score (1-6) with confidence (low/medium/high)
- Recommendation: Accept / Borderline Accept / Borderline Reject / Reject

Be rigorous but fair. This is a full review for a top ML venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "06b77842-c637-4a8e-8469-b793d1471aa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T19:38:55.862Z_

```json
{
  "parentUuid": "06b77842-c637-4a8e-8469-b793d1471aa6",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
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
  "uuid": "ed8c5be4-3044-4fa7-bbb7-0cc2a775a230",
  "timestamp": "2026-05-20T19:38:55.862Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T19:38:58.776Z_



I'll start by reading the project files to understand the full paper and context before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed8c5be4-3044-4fa7-bbb7-0cc2a775a230",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPPgEsxy5s5UFiKjsj3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbbf140b-c78b-46c5-b15d-1b28e3e07bc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWPxbRTU8w3XnfMNxse2xj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7404,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7404,
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

_source line 4 · 2026-05-20T19:39:03.639Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Wo5SNDfN5Y79Vfi7hFhKnW`</summary>

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
  "parentUuid": "cbbf140b-c78b-46c5-b15d-1b28e3e07bc5",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPPgEsxy5s5UFiKjsj3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2574a7d-b083-40e9-adc5-1ba2ccc977bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWPxbRTU8w3XnfMNxse2xj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7404,
      "cache_read_input_tokens": 8250,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7404,
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

_source line 5 · 2026-05-20T19:39:03.643Z_

<details><summary>↩ Tool result · `toolu_01Wo5SNDfN5Y79Vfi7hFhKnW`</summary>

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
  "parentUuid": "e2574a7d-b083-40e9-adc5-1ba2ccc977bd",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "3dbab4bc-ea66-444a-ab69-c5ede6060b60",
  "sourceToolAssistantUUID": "e2574a7d-b083-40e9-adc5-1ba2ccc977bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T19:39:06.229Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Fvb4UTgCNz3gHzimQvoBBp`</summary>

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
  "parentUuid": "3dbab4bc-ea66-444a-ab69-c5ede6060b60",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPQFugGhArYNQZJSdQ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e12f6c59-fa87-437f-b4a9-ba0e467abfe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MidQ6ZX3yMTqNkJ4TQqJpE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 7 · 2026-05-20T19:39:06.244Z_

<details><summary>↩ Tool result · `toolu_01Fvb4UTgCNz3gHzimQvoBBp`</summary>

```text
{"result":"# 项目 nlp_variance_gtheory 概况\n\n## 实验状态 (2 个)\n\n- **bf16_eager_disentangle**: DONE (negative) — \n- **mvp_phase_a**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\n\n## 趋势\n成功 1 / 负向 1 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32570: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e12f6c59-fa87-437f-b4a9-ba0e467abfe7",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "1ffcab3f-b7d8-4314-ba5e-39027b1bbafc",
  "sourceToolAssistantUUID": "e12f6c59-fa87-437f-b4a9-ba0e467abfe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T19:39:06.934Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011bLQo6DMxXv34pSmeT8z56`</summary>

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
  "parentUuid": "1ffcab3f-b7d8-4314-ba5e-39027b1bbafc",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPQFugGhArYNQZJSdQ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd8bc9f8-c193-4ad3-9fa4-f36d8c7cefb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MidQ6ZX3yMTqNkJ4TQqJpE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15654,
      "output_tokens": 166,
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
          "output_tokens": 166,
          "cache_read_input_tokens": 15654,
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

_source line 9 · 2026-05-20T19:39:06.942Z_

<details><summary>↩ Tool result · `toolu_011bLQo6DMxXv34pSmeT8z56`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\\n\\n## 趋势\\n成功 1 / 负向 1 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32570: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 800, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd8bc9f8-c193-4ad3-9fa4-f36d8c7cefb8",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "bd77d94d-70a7-4be6-9f40-71bc91c6bc3d",
  "sourceToolAssistantUUID": "bd8bc9f8-c193-4ad3-9fa4-f36d8c7cefb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T19:39:10.596Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017A1aHnyeeVxbNGiMMADv6E`</summary>

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
  "parentUuid": "bd77d94d-70a7-4be6-9f40-71bc91c6bc3d",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPQVpbMBZywDFMWsNky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76ba4a44-5d1c-467f-9f38-f08e0dc1009c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019goFoYjYU6dVeK45APejpa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 17103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 11 · 2026-05-20T19:39:10.604Z_

<details><summary>↩ Tool result · `toolu_017A1aHnyeeVxbNGiMMADv6E`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76ba4a44-5d1c-467f-9f38-f08e0dc1009c",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "0e5bd11b-398f-4ed4-ba25-bd4f16dcf34f",
  "sourceToolAssistantUUID": "76ba4a44-5d1c-467f-9f38-f08e0dc1009c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T19:39:11.109Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DojjaqYfyiSDkNvpBk2vW9`</summary>

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
  "parentUuid": "0e5bd11b-398f-4ed4-ba25-bd4f16dcf34f",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPQVpbMBZywDFMWsNky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d4e5ddf-5986-493d-ac41-3715fbaadbae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019goFoYjYU6dVeK45APejpa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 17103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 13 · 2026-05-20T19:39:11.124Z_

<details><summary>↩ Tool result · `toolu_01DojjaqYfyiSDkNvpBk2vW9`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No memory.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d4e5ddf-5986-493d-ac41-3715fbaadbae",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "46c9d268-985b-4cc7-99e3-6655b1f25d37",
  "sourceToolAssistantUUID": "2d4e5ddf-5986-493d-ac41-3715fbaadbae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T19:39:11.988Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QZquXmhMsoFdMK9R3KKcrr`</summary>

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
  "parentUuid": "46c9d268-985b-4cc7-99e3-6655b1f25d37",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPQVpbMBZywDFMWsNky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d89b545-9d50-4e2e-b772-82faf9e6d08e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019goFoYjYU6dVeK45APejpa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 17103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 15 · 2026-05-20T19:39:11.999Z_

<details><summary>↩ Tool result · `toolu_01QZquXmhMsoFdMK9R3KKcrr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T14:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"gtheory_evaluation\\\"\\n    name: \\\"G-Theory & Evaluation Variance\\\"\\n    narrative: \\\"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\\\"\\n  - key: \\\"infrastructure_variance\\\"\\n    name: \\\"Infrastructure-Induced Variance\\\"\\n    narrative: \\\"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\\\"\\n  - key: \\\"prompt_sensitivity\\\"\\n    name: \\\"Prompt Sensitivity & Methodological Variance\\\"\\n    narrative: \\\"Prompt phrasing, seed, temperature, and ordering as variance sources\\\"\\n  - key: \\\"evaluation_methodology\\\"\\n    name: \\\"Evaluation Methodology\\\"\\n    narrative: \\\"Scoring artifacts, benchmark design, and evaluation protocol considerations\\\"\\n\\npapers:\\n  mesting2026hidden:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\\\"\\n    authors:\\n      - \\\"Mesting, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.11581\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  brittlebench2026:\\n    title: \\\"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.13285\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  yuan2025layercast:\\n    title: \\\"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\\\"\\n    authors:\\n      - \\\"Yuan, Z.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09501\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  messina2026background:\\n    title: \\\"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\\\"\\n    authors:\\n      - \\\"Messina, P.\\\"\\n      - \\\"Scotta, A.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.22411\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  generalizit2024:\\n    title: \\\"GeneralizIT: A Python Solution for Generalizability Theory Computations\\\"\\n    authors: []\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2411.17880\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  hua2025flaw:\\n    title: \\\"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\\\"\\n    authors:\\n      - \\\"Hua, W.\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    category: \\\"evaluation_methodology\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  thinkingmachines2025batch:\\n    title: \\\"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"Technical Report\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  kunievsky2025intent:\\n    title: \\\"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\\\"\\n    authors:\\n      - \\\"Kunievsky, D.\\\"\\n      - \\\"Evans, J.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.16584\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  bui2025seeds:\\n    title: \\\"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\\\"\\n    authors:\\n      - \\\"Bui, T.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  sameprompt2026:\\n    title: \\\"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.14349\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\", \"total_chars\": 6732, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d89b545-9d50-4e2e-b772-82faf9e6d08e",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "7e2ac5fc-2ab0-449a-9ece-efb203048e9a",
  "sourceToolAssistantUUID": "1d89b545-9d50-4e2e-b772-82faf9e6d08e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T19:39:12.495Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CedN7okPSANyohvgEDiBFy`</summary>

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
  "parentUuid": "7e2ac5fc-2ab0-449a-9ece-efb203048e9a",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPQVpbMBZywDFMWsNky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "199ca966-b128-400c-897c-18966f08accb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019goFoYjYU6dVeK45APejpa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 17103,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 390,
          "cache_read_input_tokens": 17103,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1132,
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

_source line 17 · 2026-05-20T19:39:12.505Z_

<details><summary>↩ Tool result · `toolu_01CedN7okPSANyohvgEDiBFy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md\", \"content\": \"# Paper Framing — nlp_variance_gtheory\\n\\n## Target Venue\\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\\n- Extended: TACL (rolling)\\n\\n## Title\\nReproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory\\n\\n## Core Claims (3 条，可证伪)\\n\\n**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)\\n\\n**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.\\n\\n**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.\\n\\n## Story Spine\\n\\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.\\n\\n**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.\\n\\n**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.\\n\\n**Headline result template**: \\\"In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90.\\\"\\n\\n## Hook (Counter-Intuitive Quantified Claim)\\n\\\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined.\\\"\\n\\n## Narrative Strategy\\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)\\n- **Tension**: \\\"Everyone's optimizing the wrong thing\\\" — the field focuses on prompt/seed/hardware standardization while ignoring item selection\\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\\n- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)\\n- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves\\n\\n## Venue Fit Risks\\n- AAAI: Strong fit for \\\"evaluation methodology\\\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\\n- Reviewer concern 1: \\\"Only open-weight models, not API models\\\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\\n- Reviewer concern 2: \\\"G-theory is borrowed methodology, not novel\\\" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.\\n- Reviewer concern 3: \\\"Item dominance is obvious — harder items have more variance\\\" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n1. **\\\"Only N GPU types\\\"** → exp-003 (multi-hardware crossing) addresses this\\n2. **\\\"float32 engine confound\\\"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)\\n3. **\\\"Only MMLU\\\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag\\n4. **\\\"Small item sample\\\"** → exp-001 expands from 50 to 200 items\\n5. **\\\"No training-time analysis\\\"** → exp-006 (fine-tuning G-study with RoBERTa)\\n6. **\\\"Missing scale validation\\\"** → exp-005 (14B models)\\n7. **\\\"G-theory may not be right framework\\\"** → Compare with ANOVA and regression decomposition as sensitivity analysis\\n\\n## Design Decisions\\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.\\n\", \"total_chars\": 6768, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "199ca966-b128-400c-897c-18966f08accb",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "1531abbf-1067-4b44-bb81-11802c4308f8",
  "sourceToolAssistantUUID": "199ca966-b128-400c-897c-18966f08accb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T19:39:16.430Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M6jpJ8oK4roBB4rsfoyp5R`</summary>

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
  "parentUuid": "1531abbf-1067-4b44-bb81-11802c4308f8",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPQuZ6kbnyfCbnanKxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80560ce3-b48d-40a7-84e9-8f58fc316695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K43EZVHMaPqyNmATibRHBG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5162,
      "cache_read_input_tokens": 18235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5162,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 19 · 2026-05-20T19:39:16.438Z_

<details><summary>↩ Tool result · `toolu_01M6jpJ8oK4roBB4rsfoyp5R`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/ROADMAP.md\", \"content\": \"# nlp_variance_gtheory — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:01 UTC | 更新原因: Post-MVP kickoff: paper_framing + experiment_plan 完成，Dream 已提交，ROADMAP 转 Research 阶段 dashboard\\n\\n## 核心方向\\n用 G-theory 联合分解 LLM 评估中 infrastructure × methodology × item 的方差。核心发现：item 选择主导方差（58.4%），infrastructure 与 methodology 在聚合层面近似可分但效应是 item-conditional 的。产出可量化的 reproducibility budget。详见 paper_framing.md。\\n\\n## 当前进展\\n- 阶段: **Research**（MVP 已通过，D001）\\n- MVP 结论: item_id=58.4%, precision×item=7.2%, temp×item=6.9%, prompt×item=5.7%, 直接 infra×method <0.02%\\n- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟进行中 (dream_20260520T190053)\\n- 服务器: westd-32570（4× RTX PRO 6000 96GB），第二种 GPU 待 Manager 分配\\n- float32 引擎混淆需 exp-001 解决（统一 V0 enforce_eager）\\n\\n## 实验计划（详见 experiment_plan.yaml）\\n| ID | Claim | Priority | GPU·h | 状态 |\\n|----|-------|----------|-------|------|\\n| exp-001 | Item dominance at scale (4 models × 200 items × fix FP32) | P0 | 100 | planned |\\n| exp-002 | Multi-benchmark (GSM8K/ARC/HellaSwag) | P0 | 200 | planned |\\n| exp-003 | Multi-hardware crossing | P0 | 120 | blocked (待第二种 GPU) |\\n| exp-004 | D-study reproducibility budget | P0 | 0 | planned (分析) |\\n| exp-005 | 14B scale extension | P1 | 100 | planned |\\n| exp-006 | Fine-tuning G-study (RoBERTa) | P1 | 200 | planned |\\n| exp-007 | LayerCast mitigation | P2 | 30 | planned |\\n| exp-008 | MATH benchmark | P2 | 50 | planned |\\n\\nTotal: P0=420h, P1=300h, P2=80h\\n\\n## 近期任务\\n- [ ] Dream 模拟完成 → 审视报告 → 调整 framing/plan（如需要）\\n- [ ] Dream 通过后批准 exp-001（可立即在 westd-32570 上执行）\\n- [ ] Agent 完成 text_exact_match 双变量分析（MVP 数据补充分析）\\n- [ ] 等待 Manager 回复第二种 GPU → 解除 exp-003 blocked\\n\\n## GPU 预算\\n- 本项目分配: westd-32570 cuda:0-3（4× RTX PRO 6000 96GB）\\n- 第二种 GPU: 待 Manager 分配\\n- P0 预估: 420 GPU·h | P1: 300 | P2: 80\\n\\n## 投稿目标\\n- 主投: AAAI 2027（abstract Jul 21, paper Jul 28 — 9 周）\\n- 备选: ACL 2027 ARR Oct 15（21 周）/ TACL rolling\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-20 | 采用 dual-metric (binary correct + text exact match) | — |\\n| D001 | 2026-05-20 | MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4 | — |\\n\\n\", \"total_chars\": 2064, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80560ce3-b48d-40a7-84e9-8f58fc316695",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "7e0d98f1-6fb1-49d6-b96e-24899e0059e2",
  "sourceToolAssistantUUID": "80560ce3-b48d-40a7-84e9-8f58fc316695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T19:39:17.025Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Mta1rMG8ijUHPr6THynyRH`</summary>

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
  "parentUuid": "7e0d98f1-6fb1-49d6-b96e-24899e0059e2",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPQuZ6kbnyfCbnanKxV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4f2f872-3909-474b-a027-1c5244754584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K43EZVHMaPqyNmATibRHBG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5162,
      "cache_read_input_tokens": 18235,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5162
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 18235,
          "cache_creation_input_tokens": 5162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5162,
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

_source line 21 · 2026-05-20T19:39:17.033Z_

<details><summary>↩ Tool result · `toolu_01Mta1rMG8ijUHPr6THynyRH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/decisions.yaml\", \"content\": \"_next_id: 3\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:57 UTC\\n  summary: MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4%），separability 在聚合层面成立，进入\\n    research 阶段\\n  rationale: 5,400 次推理完成，5 个方差分量 ≥5% 且 CI 不含零，pipeline 端到端可运行。核心发现：(1) item 选择是评估方差最大来源；(2)\\n    precision/temperature/prompt 效应是 item-specific 的；(3) 直接的 infrastructure×methodology\\n    交互可忽略（<0.02%）。float32 引擎混淆需全研究阶段解决但不影响 MVP 结论。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:12 UTC\\n  summary: 采用 dual-metric (binary correct + text exact match) 方差分解作为论文核心方法论，Claim\\n    3 改为 metric-conditional reproducibility budget\\n  rationale: MVP 双变量分析揭示截然不同的方差结构：binary correct 下 item_id 主导 (58.4%, G=0.357)；text\\n    exact match 下 prompt×item 主导 (37.5%, G=0.975)。单一 response variable 无法完整描述评估可靠性。Dual-metric\\n    对比是 G-theory 框架的天然优势——\\\"同一实验在不同衡量标准下可靠性完全不同\\\"是比单一 budget 更有力的发现。precision:temperature\\n    交互在 text metric 下显著 (1.3%, CI 不含零)，证明 separability 在细粒度下不完全成立。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n\", \"total_chars\": 997, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4f2f872-3909-474b-a027-1c5244754584",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "b20aa94e-d868-4ba2-8cf9-95b433e0e571",
  "sourceToolAssistantUUID": "f4f2f872-3909-474b-a027-1c5244754584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-20T19:39:20.205Z_

Now let me read the distilled research and writing skills to understand the literature landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b20aa94e-d868-4ba2-8cf9-95b433e0e571",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRExf4tN23XompkuN3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6aff365-7eac-4f80-af96-04821ef80322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgJv2onioNTfz8DGvzC929",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2272,
      "cache_read_input_tokens": 23397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2272,
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

_source line 23 · 2026-05-20T19:39:20.825Z_

<details open><summary>🔧 Tool call — Read · `toolu_011X42H8tJ9z6SrMqrv6DCjF`</summary>

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
  "parentUuid": "d6aff365-7eac-4f80-af96-04821ef80322",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRExf4tN23XompkuN3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39287bd3-03d8-43d7-8d44-67104867f0d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgJv2onioNTfz8DGvzC929",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2272,
      "cache_read_input_tokens": 23397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2272,
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

_source line 24 · 2026-05-20T19:39:20.831Z_

<details><summary>↩ Tool result · `toolu_011X42H8tJ9z6SrMqrv6DCjF`</summary>

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
  "parentUuid": "39287bd3-03d8-43d7-8d44-67104867f0d9",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "79b2c4ec-269b-4b6b-bda0-b87a7391c768",
  "sourceToolAssistantUUID": "39287bd3-03d8-43d7-8d44-67104867f0d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T19:39:21.209Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EHdeuQ4TCfXcQ81MoMDaYc`</summary>

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
  "parentUuid": "79b2c4ec-269b-4b6b-bda0-b87a7391c768",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRExf4tN23XompkuN3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe49cb10-b914-483f-b2ed-e70c0947db0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgJv2onioNTfz8DGvzC929",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2272,
      "cache_read_input_tokens": 23397,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 23397,
          "cache_creation_input_tokens": 2272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2272,
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

_source line 26 · 2026-05-20T19:39:21.213Z_

<details><summary>↩ Tool result · `toolu_01EHdeuQ4TCfXcQ81MoMDaYc`</summary>

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
  "parentUuid": "fe49cb10-b914-483f-b2ed-e70c0947db0e",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "6ebac3c6-8103-405d-b0c7-35e042abf12f",
  "sourceToolAssistantUUID": "fe49cb10-b914-483f-b2ed-e70c0947db0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T19:39:24.653Z_

Now let me look at the experiment plan and any artifacts to understand the experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ebac3c6-8103-405d-b0c7-35e042abf12f",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRYqh61Z8J6713yKLU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47cbce5d-5702-4a5e-a26e-26dcbf845083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EwrAjg1ZptXG4m2fYa1WD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2114,
      "cache_read_input_tokens": 25669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2114,
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

_source line 28 · 2026-05-20T19:39:26.505Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01D3B3QeEfk5ZKuWEAMUMxAZ`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47cbce5d-5702-4a5e-a26e-26dcbf845083",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRYqh61Z8J6713yKLU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41fa3097-0da1-40e5-9e9e-dea7fac806b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EwrAjg1ZptXG4m2fYa1WD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2114,
      "cache_read_input_tokens": 25669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2114,
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

_source line 29 · 2026-05-20T19:39:26.520Z_

<details><summary>↩ Tool result · `toolu_01D3B3QeEfk5ZKuWEAMUMxAZ`</summary>

```text
literature_map.yaml
distill_tmp/hua2025flaw.yaml
distill_tmp/mesting2026hidden.yaml
distill_tmp/brittlebench2026.yaml
distill_tmp/yuan2025layercast.yaml
distill_tmp/kunievsky2025intent.yaml
distill_tmp/thinkingmachines2025batch.yaml
distill_tmp/messina2026background.yaml
distill_tmp/generalizit2024.yaml
distill_tmp/bui2025seeds.yaml
distill_tmp/sameprompt2026.yaml
artifacts/manifest.yaml
experiment_plan.yaml
decisions.yaml
artifacts/dream_reports/dream_20260520T190053/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T190053/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T190053/worst/imagined_experiments.yaml
registry.yaml
artifacts/dream_reports/dream_20260520T190053/best/review_context.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T190053/median/review_context.yaml
mistakes.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41fa3097-0da1-40e5-9e9e-dea7fac806b2",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "16f1c809-16c3-45ba-9bba-0fd17eb4e691",
  "sourceToolAssistantUUID": "41fa3097-0da1-40e5-9e9e-dea7fac806b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T19:39:26.987Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014vgpvUBe5ideC6xDJzp4bZ`</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16f1c809-16c3-45ba-9bba-0fd17eb4e691",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRYqh61Z8J6713yKLU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4278b490-d9a8-44d2-a794-dbe35f5e5822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EwrAjg1ZptXG4m2fYa1WD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2114,
      "cache_read_input_tokens": 25669,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2114
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 25669,
          "cache_creation_input_tokens": 2114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2114,
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

_source line 31 · 2026-05-20T19:39:26.996Z_

<details><summary>↩ Tool result · `toolu_014vgpvUBe5ideC6xDJzp4bZ`</summary>

```text
artifacts/code/pyproject.toml
artifacts/code/src/__init__.py
artifacts/code/src/data/__init__.py
artifacts/code/src/design/__init__.py
artifacts/code/src/inference/__init__.py
artifacts/code/src/analysis/__init__.py
artifacts/code/src/data/sample_mmlu.py
artifacts/code/src/data/few_shot.py
artifacts/_project/intermediate/README.md
artifacts/code/README.md
artifacts/code/src/analysis/visualize.py
artifacts/code/src/__pycache__/__init__.cpython-314.pyc
artifacts/code/src/design/__pycache__/__init__.cpython-314.pyc
artifacts/code/src/design/__pycache__/generate_design.cpython-314.pyc
artifacts/code/src/analysis/d_study.py
artifacts/code/run_mvp.sh
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
artifacts/dream_reports/dream_20260520T190053/best/review_report.md
artifacts/dream_reports/dream_20260520T190053/logs/review_best.log
artifacts/dream_reports/dream_20260520T190053/median/review_context.yaml
artifacts/code/src/inference/vllm_runner.py
artifacts/code/src/design/generate_design.py
artifacts/code/src/data/prompt_templates.py
artifacts/code/src/inference/run_experiment.py
artifacts/dream_reports/dream_20260520T190053/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4278b490-d9a8-44d2-a794-dbe35f5e5822",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "2da6879d-6d82-452e-ae99-448029663783",
  "sourceToolAssistantUUID": "4278b490-d9a8-44d2-a794-dbe35f5e5822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T19:39:30.068Z_

Let me read the dream review report to understand existing review feedback, and the best/median paper.tex files to understand the paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2da6879d-6d82-452e-ae99-448029663783",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRyWkSQGmKos9X4UtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26776dde-0a06-4c8a-8cf6-2ac44271c3e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTFEstpcri26X6LUY82fEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 27783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1731,
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

_source line 33 · 2026-05-20T19:39:31.555Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EVQyXrnKmXP114pLB6167r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26776dde-0a06-4c8a-8cf6-2ac44271c3e6",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRyWkSQGmKos9X4UtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ee1c1a9-dbe7-432e-a81b-9db42421fa24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTFEstpcri26X6LUY82fEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 27783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1731,
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

_source line 34 · 2026-05-20T19:39:31.563Z_

<details><summary>↩ Tool result · `toolu_01EVQyXrnKmXP114pLB6167r`</summary>

```text
1	---
2	dream_id: dream_20260520T190053
3	tier: best
4	overall_score: borderline
5	timestamp: 2026-05-20T19:37:05.298566+00:00
6	---
7	
8	
9	# Dream Review Report
10	
11	**Paper:** Reproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory
12	
13	**Review Mode:** Full (2 Reviewers + Roundtable)
14	**Review Standard:** Top ML venue, ~25% acceptance rate, 6-point scale
15	
16	---
17	
18	## Reviewer Scores
19	
20	| Reviewer | Focus | Initial Score | Post-Discussion |
21	|----------|-------|--------------|-----------------|
22	| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/6 (Weak Accept) |
23	| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 3/6 (Weak Reject) |
24	| **Consensus** | | | **3.5/6 (Borderline)** |
25	
26	---
27	
28	## Paper Summary
29	
30	The paper conducts a fully-crossed Generalizability Theory (G-theory) study unifying infrastructure (hardware, precision) × methodology (prompt, seed, temperature, ordering) × measurement (test items) factors in LLM evaluation. Across 6 models (7–14B), 5 benchmarks, and 2M+ records, the authors report: (1) item selection dominates variance (42–58%), (2) infrastructure–methodology separability holds at aggregate (<0.5%) but is item-conditional (14.2%), and (3) current practices yield G < 0.40 while D-study budgets show items are 10× more cost-effective than prompts for reliability. A fine-tuning extension with RoBERTa-large shows item dominance generalizes to training.
31	
32	---
33	
34	## Consolidated Strengths
35	
36	**S1. Ambitious experimental scale and systematic design.**
37	Seven experiments totaling 2M+ evaluation records, building from single-benchmark to cross-benchmark, cross-model, cross-hardware, and cross-paradigm coverage. All 8 planned experiments are reflected in the paper. This is a serious empirical effort.
38	
39	**S2. Engine confound discovery is a genuine methodological contribution.**
40	The finding that vLLM routes FP32 through a different compute path (non-V0 engine), inflating precision variance from 0.3% to 0.87% (main) and from 1.8% to 7.24% (interaction) with an 8.5pp accuracy gap, is independently valuable. It serves as a concrete cautionary tale for any study comparing precision modes and demonstrates how infrastructure configuration can systematically bias variance attribution.
41	
42	**S3. Nuanced two-level separability result.**
43	Rather than a simple binary answer, the separability test yields complementary findings: aggregate separability holds (<0.5% direct interactions), licensing isolated-factor studies, while item-conditional interactions (14.2%) warn that such conclusions are contingent on item selection. This is more informative than either finding alone.
44	
45	**S4. D-study budgets are actionable.**
46	The budget tables (Table 7, Table 8) provide concrete, immediately usable guidance: 600 items + 3 prompts + 2 seeds → G ≥ 0.90 for MMLU. The 10:1 marginal effectiveness ratio (items vs. prompts) is a memorable, practical takeaway. Cross-benchmark budget differences (550–1100 items) provide task-specific guidance.
47	
48	**S5. Cross-benchmark difficulty gradient.**
49	The systematic relationship between task difficulty and variance structure (item_id decreases 58.4% → 42.1%, residual increases 16.8% → 24.8%, temp×item increases 5.8% → 10.4% as accuracy drops) quantifies why reasoning benchmarks are less reproducible. This is a genuinely useful empirical finding.
50	
51	---
52	
53	## Consolidated Weaknesses
54	
55	**W1. Incremental over Mesting et al. (2026) — the core methodological contribution is an extension, not a new framework.** [Both reviewers, R2 primary]
56	Mesting et al. (2026) already applied G-theory to LLM evaluation with item, prompt, judge, and temperature facets, finding judge dominance at 43.8%. This paper extends that framework by adding infrastructure facets (hardware, precision). However, these infrastructure facets turn out to contribute negligibly: hardware main effect 0.6%, precision main effect 0.3%. The extension is real but modest in substance — the paper's most important finding (item dominance) could plausibly have emerged from a Mesting-style design without the infrastructure layer. The "first fully-crossed" framing oversells what is fundamentally an incremental extension.
57	
58	**W2. "Fully crossed" design is overstated.** [R1 primary]
59	The paper claims a fully-crossed design but the factorial structure is unbalanced:
60	- MMLU has the richest design (3 precisions, 3 temperatures, 4 orderings, 2 GPUs)
61	- Other benchmarks use reduced designs (2 precisions, 2 temperatures)
62	- Hardware crossing is only on MMLU (Exp. 3)
63	- 14B extension uses a reduced facet set
64	- Fine-tuning uses a completely different model/task family
65	Claims about cross-benchmark separability and scale invariance rest on narrower evidence than the "fully crossed" framing implies. The paper should clearly delineate which claims are supported by full crossing and which by partial designs.
66	
67	**W3. Pooled-model analysis likely inflates item_id variance.** [R1 primary]
68	The primary analysis pools 4 models, treating them as exchangeable observations. But model × item interactions (some items are harder for Mistral than Qwen3) get absorbed into the item_id component, inflating its apparent dominance. The per-model analysis (Table 2) partially addresses this (item_id range 54.7–62.0%), but should be the primary presentation. The pooled analysis overstates the universality of the 58.4% figure.
69	
70	**W4. Item dominance is partially predictable from first principles.** [R2 primary]
71	Any assessment with a steep difficulty gradient (items ranging from trivial to expert) will show item difficulty as the dominant variance source. The paper's own Discussion explains exactly why this must be so. While quantifying the magnitude is useful, framing it as surprising ("researchers are optimizing the wrong knobs") oversells the finding. A more measured framing — "item dominance is expected but its magnitude (>50%) and the relative inefficiency of other interventions have not been quantified" — would be more appropriate.
72	
73	**W5. Separability threshold (0.5%) is arbitrary and the result is borderline.** [R1 primary, R2 concurs]
74	The 0.5% threshold for "separability" is not justified from G-theory, psychometrics, or any principled argument. The observed value (0.5%) lands exactly on the threshold boundary, making the binary "separability holds" conclusion fragile. A bootstrap confidence interval on the total direct interaction variance would be more informative. The result should be presented as a continuous measure with uncertainty rather than a pass/fail test.
75	
76	**W6. D-study projections lack uncertainty quantification.** [R1 primary]
77	The budget recommendations (e.g., "600 items + 3 prompts + 2 seeds → G ≥ 0.90") are point estimates derived from estimated variance components. No confidence intervals or sensitivity analysis is provided for the projected G values. Given that the input variance components have SEs of 0.1–2.1%, the projected G values could shift meaningfully. The paper should propagate estimation uncertainty through the D-study projections (e.g., via bootstrap).
78	
79	**W7. Very sparse reference list (only 7 references).** [R2 primary, R1 concurs]
80	For a top ML venue, 7 references is far below expectations. Critical omissions include:
81	- Classical G-theory: Brennan (2001) "Generalizability Theory," Shavelson & Webb (1991) — foundational references for G-theory methodology
82	- ML variance decomposition: Bouthillier et al. (2021) "Accounting for Variance in Machine Learning Benchmarks" — the closest ML-native predecessor, not cited
83	- IRT in NLP: Lalor et al. (2019), Rodriguez et al. (2021), Vania et al. (2021) — item-level analysis frameworks directly relevant to the item dominance finding
84	- Ordering effects: Lu et al. (2022) — relevant to the ordering facet
85	- ML reproducibility: Henderson et al. (2018), Pineau et al. (2021) — broader context
86	This is not a minor issue: the missing references include direct methodological predecessors and would substantially change the novelty positioning.
87	
88	**W8. Fine-tuning generalization is weak.** [Both reviewers]
89	The claim that "findings extend to fine-tuning settings" is based solely on RoBERTa-large (355M, encoder-only) on 4 NLU classification tasks. This is a large architectural and paradigm gap from the 7–14B decoder models used in inference experiments. Fine-tuning a 7B+ decoder model with LoRA/QLoRA on a generation task would be far more convincing as a generalization argument. As presented, this is a separate (interesting) finding rather than evidence of generalization.
90	
91	---
92	
93	## Questions for Authors
94	
95	**Q1.** How would the variance decomposition change if model were treated as a random facet rather than pooling? Specifically, would model × item interactions reduce the item_id share substantially?
96	
97	**Q2.** Can you provide a direct numerical comparison with Mesting et al. (2026) on overlapping facets (item, prompt, temperature)? This would clarify the incremental contribution.
98	
99	**Q3.** Would item dominance survive adding judge/scorer as a facet? Mesting found judge at 43.8% — this could substantially alter the variance hierarchy. The paper uses fixed generation-based scoring, which removes this source but also limits comparability.
100	
101	**Q4.** Can you provide bootstrap confidence intervals for the D-study G projections? The headline recommendation (600/3/2 → G = 0.90) would be more credible with uncertainty bounds.
102	
103	**Q5.** What is the justification for the 0.5% separability threshold? Would results change with 1% or 0.25%?
104	
105	**Q6.** The MATH entry in Table 8 shows 1,100 items with "66× cost factor" but 1100 × 3 prompts × 2 seeds = 6,600 evaluations, not 13,200. Is this a typo, or does MATH require more prompts/seeds?
106	
107	**Q7.** How were the 6 prompt templates selected? Were they designed to maximize diversity, or sampled from existing evaluation suites? The prompt × item interaction (6.1%) depends critically on prompt diversity.
108	
109	---
110	
111	## Minor Issues
112	
113	**M1.** Table 3 column headers are misaligned in the PDF — "item_id %" appears to span the wrong column.
114	
115	**M2.** The ThinkingMachines (2025) reference has placeholder arXiv ID "2501.xxxxx" — needs the real ID.
116	
117	**M3.** The abstract says "6 models" but the paper primarily analyzes 4 models with 2 as extension. Should be clearer about primary vs. extension.
118	
119	**M4.** The paper claims "over 2 million evaluation records" — the sum of stated record counts (1,036,800 + 3×230,400 + 691,200 + 2×172,800 + 1,728 + 230,400 + 172,800) ≈ 3.17M. The "over 2 million" is an undercount of the actual total. Clarify.
120	
121	**M5.** "LayerCast" is not a standard term — should be cited or defined more precisely.
122	
123	**M6.** The D-study discussion mentions G ≥ 0.80 as the psychometric minimum but doesn't cite the source for this threshold (Nunnally & Bernstein 1994 or similar).
124	
125	---
126	
127	## Experiment Coverage Assessment
128	
129	All 8 planned experiments from the design document are reflected in the paper:
130	- ✅ exp-001: Full-scale precision study (MMLU)
131	- ✅ exp-002: Multi-benchmark replication (GSM8K, ARC, HellaSwag)
132	- ✅ exp-003: Multi-hardware G-study
133	- ✅ exp-004: D-study projections
134	- ✅ exp-005: 14B model extension
135	- ✅ exp-006: Fine-tuning G-study
136	- ✅ exp-007: LayerCast precision study
137	- ✅ exp-008: MATH benchmark extension
138	
139	Coverage is complete. However, several figures described in the experiment plan (stacked-bar decompositions, heatmaps, scatter plots, D-study projection curves, iso-G contour plots) are absent from the paper. The paper is table-heavy with no figures, which significantly weakens communication of key results — particularly the D-study projection curves (planned Fig 8–10) and the variance decomposition comparisons (planned Fig 1, 4, 15) which would be far more effective visually than as tables.
140	
141	---
142	
143	## Recommendation
144	
145	**Consensus Score: 3.5/6 (Borderline — between Weak Reject and Weak Accept)**
146	
147	**For acceptance, the paper would need:**
148	1. Reframe novelty claims to acknowledge extension-of-Mesting positioning honestly
149	2. Add per-model analysis as primary, pooled as secondary
150	3. Add uncertainty quantification to D-study projections
151	4. Substantially expand the reference list (add ≥15 missing key references)
152	5. Justify or remove the 0.5% separability threshold
153	6. Add figures — at minimum D-study projection curves and variance decomposition stacked bars
154	
155	**The paper's core strengths** — the engine confound discovery, the nuanced separability result, the cross-benchmark difficulty gradient, and the actionable D-study budgets — represent genuine value. But the incremental positioning over Mesting et al., inflated novelty claims, methodological concerns (pooled analysis, arbitrary threshold, no uncertainty propagation), and severely sparse references pull it below the acceptance threshold in its current form.
156	
157	**If revised to address the top 4 weaknesses**, this could become a solid Weak Accept (4/6). The empirical effort is substantial and the practical recommendations fill a real need. The revisions are achievable without new experiments.
158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ee1c1a9-dbe7-432e-a81b-9db42421fa24",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "d4955fd2-0ecf-4c1d-9fca-b665ef7e7dcb",
  "sourceToolAssistantUUID": "2ee1c1a9-dbe7-432e-a81b-9db42421fa24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T19:39:32.199Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JExWi9ikavjdVBY4YaYKqV`</summary>

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
  "parentUuid": "d4955fd2-0ecf-4c1d-9fca-b665ef7e7dcb",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPRyWkSQGmKos9X4UtV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ce0346f-f6d6-426d-a427-6e893e456588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTFEstpcri26X6LUY82fEP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 27783,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 27783,
          "cache_creation_input_tokens": 1731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1731,
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

_source line 36 · 2026-05-20T19:39:32.478Z_

<details><summary>↩ Tool result · `toolu_01JExWi9ikavjdVBY4YaYKqV`</summary>

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
  "parentUuid": "3ce0346f-f6d6-426d-a427-6e893e456588",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "c3a01913-49c0-46c6-950f-deea917a668c",
  "sourceToolAssistantUUID": "3ce0346f-f6d6-426d-a427-6e893e456588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-20T19:39:35.436Z_

Now let me also read the median paper and its review context, plus the experiment plan for full understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3a01913-49c0-46c6-950f-deea917a668c",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPSNqx2d5oP7UGPsBi4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc5e25a6-c036-4258-9dbf-63303ba979e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cb2fn7a8cF3qAdce5VAof",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15478,
      "cache_read_input_tokens": 29514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15478,
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

_source line 38 · 2026-05-20T19:39:37.212Z_

<details open><summary>🔧 Tool call — Read · `toolu_012ooAcAqQWJVaxnzTLgs7bD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc5e25a6-c036-4258-9dbf-63303ba979e0",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPSNqx2d5oP7UGPsBi4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13dc0f7b-edb3-448b-bf49-a328ac7643e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cb2fn7a8cF3qAdce5VAof",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15478,
      "cache_read_input_tokens": 29514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15478,
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

_source line 39 · 2026-05-20T19:39:37.219Z_

<details><summary>↩ Tool result · `toolu_012ooAcAqQWJVaxnzTLgs7bD`</summary>

```text
1	experiments:
2	  # === P0: Must-run for paper submission ===
3	
4	  - id: exp-001
5	    claim: 1  # Item dominance at scale
6	    description: >
7	      Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3)
8	      × 3 precisions (FP32, BF16, FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings
9	      × 200 MMLU items (stratified). All precisions use consistent vLLM engine (V0 enforce_eager)
10	      to eliminate the float32 engine confound found in MVP. Validates item dominance finding at
11	      scale and with multiple models.
12	    priority: P0
13	    gpu_budget_hours: 100
14	    hardware: westd-32570 (RTX PRO 6000 96GB)
15	    deps: []
16	    status: planned
17	
18	  - id: exp-002
19	    claim: 1  # Item dominance generalizes across benchmarks
20	    description: >
21	      Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts × 6 seeds
22	      × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200 items),
23	      HellaSwag (200 items). Tests whether item dominance and separability hold across
24	      task types (math reasoning, science reasoning, commonsense).
25	    priority: P0
26	    gpu_budget_hours: 200
27	    hardware: westd-32570
28	    deps: [exp-001]  # need analysis pipeline validated first
29	    status: planned
30	
31	  - id: exp-003
32	    claim: 2  # Separability with hardware factor
33	    description: >
34	      Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16, FP16)
35	      × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items.
36	      Tests hardware × methodology interaction — the core separability question
37	      that MVP couldn't address with only 1 GPU type.
38	    priority: P0
39	    gpu_budget_hours: 120
40	    hardware: westd-32570 + TBD (second GPU type from Manager)
41	    deps: []  # independent, can run as soon as second GPU available
42	    status: blocked  # waiting for second GPU type
43	
44	  - id: exp-004
45	    claim: 3  # D-study reproducibility budget
46	    description: >
47	      D-study projections from combined exp-001/002/003 data. Compute optimal
48	      allocation across facets (items, prompts, seeds, orderings) for G≥0.90/0.95/0.99.
49	      Generate practitioner-facing reproducibility budget tables.
50	    priority: P0
51	    gpu_budget_hours: 0  # pure analysis, no GPU
52	    hardware: none
53	    deps: [exp-001, exp-002, exp-003]
54	    status: planned
55	
56	  # === P1: Important for paper strength ===
57	
58	  - id: exp-005
59	    claim: 2  # Scale validation
60	    description: >
61	      14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter GPUs
62	      at BF16/FP16. Tests whether variance attribution patterns change with model scale
63	      and architecture (dense vs reasoning-distilled).
64	    priority: P1
65	    gpu_budget_hours: 100
66	    hardware: TBD (needs ≥48GB VRAM per GPU)
67	    deps: [exp-003]
68	    status: planned
69	
70	  - id: exp-006
71	    claim: 2  # Training-time variance
72	    description: >
73	      Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA.
74	      Fully crossed: 6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions
75	      = 432 runs/task × 4 tasks = 1,728 total fine-tuning runs.
76	      Validates whether variance hierarchy differs between inference and fine-tuning.
77	    priority: P1
78	    gpu_budget_hours: 200
79	    hardware: westd-32570 (RoBERTa-large fits easily on 96GB)
80	    deps: []
81	    status: planned
82	
83	  # === P2: Nice-to-have ===
84	
85	  - id: exp-007
86	    claim: 2  # LayerCast mitigation
87	    description: >
88	      Test LayerCast (FP16 storage + FP32 compute) as additional precision condition
89	      on MMLU. Quantifies variance reduction from this mitigation strategy.
90	    priority: P2
91	    gpu_budget_hours: 30
92	    hardware: westd-32570
93	    deps: [exp-001]
94	    status: planned
95	
96	  - id: exp-008
97	    claim: 1  # Reasoning benchmark extension
98	    description: >
99	      MATH benchmark (200 items) — tests whether item dominance pattern differs
100	      for reasoning-heavy tasks where chain-of-thought introduces additional variance.
101	    priority: P2
102	    gpu_budget_hours: 50
103	    hardware: westd-32570
104	    deps: [exp-002]
105	    status: planned
106	
107	# MVP experiment (completed)
108	mvp:
109	  - id: mvp-001
110	    registry_id: null  # MVP was run directly, not through registry
111	    description: >
112	      MVP Phase A: 1 model (Llama-3.1-8B) × 1 hardware (RTX PRO 6000) × 3 precisions
113	      × 3 prompts × 3 seeds × 2 temps × 2 orderings = 108 conditions × 50 MMLU items.
114	    result: >
115	      PASS. item_id=58.4%, precision×item=7.2%, temp×item=6.9%, prompt×item=5.7%.
116	      Direct precision×methodology <0.02%. G=0.357. float32 engine confound identified.
117	    status: completed
118	
119	# GPU budget summary
120	budget:
121	  P0_total: 420  # exp-001(100) + exp-002(200) + exp-003(120) + exp-004(0)
122	  P1_total: 300  # exp-005(100) + exp-006(200)
123	  P2_total: 80   # exp-007(30) + exp-008(50)
124	  grand_total: 800
125	  available: "4× RTX PRO 6000 96GB (westd-32570) + TBD second GPU type"
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13dc0f7b-edb3-448b-bf49-a328ac7643e3",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "9411e952-54a3-4d79-bcf6-18a6622c9e48",
  "sourceToolAssistantUUID": "13dc0f7b-edb3-448b-bf49-a328ac7643e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T19:39:38.339Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LaDUqcfm6535zPzBmFBhEc`</summary>

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
  "parentUuid": "9411e952-54a3-4d79-bcf6-18a6622c9e48",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPSNqx2d5oP7UGPsBi4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23aa9b03-93b8-4b63-bf9c-f96876176b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cb2fn7a8cF3qAdce5VAof",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15478,
      "cache_read_input_tokens": 29514,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15478
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 29514,
          "cache_creation_input_tokens": 15478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15478,
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

_source line 41 · 2026-05-20T19:39:38.762Z_

<details><summary>↩ Tool result · `toolu_01LaDUqcfm6535zPzBmFBhEc`</summary>

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
  "parentUuid": "23aa9b03-93b8-4b63-bf9c-f96876176b0b",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "0cc48288-fa26-4e78-ab3a-f38a8dbf7f66",
  "sourceToolAssistantUUID": "23aa9b03-93b8-4b63-bf9c-f96876176b0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T19:39:42.486Z_

Now let me also check the related work notes to understand what literature has already been considered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc48288-fa26-4e78-ab3a-f38a8dbf7f66",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPSqfk9qKe9UHJXBH6X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc0f3425-28fe-482f-a675-a6bad0d71f7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYX5GkTYRj3jsrJ2cxKcFd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16325,
      "cache_read_input_tokens": 44992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16325,
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

_source line 43 · 2026-05-20T19:39:43.682Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VTVtzpacp9JfBTAmSwCEZi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc0f3425-28fe-482f-a675-a6bad0d71f7b",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPSqfk9qKe9UHJXBH6X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a641b9b-c404-4aad-af74-e3a30c0c503f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYX5GkTYRj3jsrJ2cxKcFd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16325,
      "cache_read_input_tokens": 44992,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16325
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 44992,
          "cache_creation_input_tokens": 16325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16325,
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

_source line 44 · 2026-05-20T19:39:43.686Z_

<details><summary>↩ Tool result · `toolu_01VTVtzpacp9JfBTAmSwCEZi`</summary>

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
  "parentUuid": "2a641b9b-c404-4aad-af74-e3a30c0c503f",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "f5b73091-3407-48a9-95cf-f37789e6dd02",
  "sourceToolAssistantUUID": "2a641b9b-c404-4aad-af74-e3a30c0c503f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-20T19:39:47.875Z_

Now I have a thorough understanding of the paper, its claims, experimental design, related work, and the previous dream review. Let me now write my review as R2 focused on novelty, positioning, and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5b73091-3407-48a9-95cf-f37789e6dd02",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPTCuBxDjSsNKNgA1bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb3c3423-0c3f-4db8-ad8e-365e7e8d1840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa1WJaeTc9idBc5Uy6iUF1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2426,
      "cache_read_input_tokens": 61317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2426,
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

_source line 46 · 2026-05-20T19:39:50.066Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018ixmoPQJBgwbzBFbvVngrz`</summary>

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
  "parentUuid": "bb3c3423-0c3f-4db8-ad8e-365e7e8d1840",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPTCuBxDjSsNKNgA1bQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9607579-b388-429b-b1be-3d6efc34c586",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa1WJaeTc9idBc5Uy6iUF1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2426,
      "cache_read_input_tokens": 61317,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 61317,
          "cache_creation_input_tokens": 2426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2426,
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

_source line 47 · 2026-05-20T19:39:50.070Z_

<details><summary>↩ Tool result · `toolu_018ixmoPQJBgwbzBFbvVngrz`</summary>

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
  "parentUuid": "f9607579-b388-429b-b1be-3d6efc34c586",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "adac42d84d8448a91",
  "type": "user",
  "uuid": "96f8379e-f6e7-4ae5-8a82-c01f3de9e961",
  "sourceToolAssistantUUID": "f9607579-b388-429b-b1be-3d6efc34c586",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-20T19:41:24.610Z_



Here is my review as Reviewer R2 (Novelty, Positioning, and Related Work).

---

## Summary

This paper applies Generalizability Theory to LLM evaluation, crossing infrastructure facets (hardware type, numerical precision) with methodology facets (prompt, seed, temperature, ordering) and measurement (items) in a single factorial design. Across 6 models, 5 benchmarks, and 2M+ evaluation records, the authors find item selection dominates variance (42--58%), direct infrastructure-methodology interactions are negligible (<0.5%), and current evaluation practices yield unacceptably low generalizability coefficients (G < 0.40). D-study projections provide concrete reproducibility budgets showing item count is 10x more cost-effective than prompt replication for achieving G >= 0.90. A fine-tuning extension with RoBERTa-large shows the variance hierarchy shifts but item dominance persists.

---

## Strengths

- **S1. Empirically rigorous factorial design.** The fully-crossed structure spanning 7 facets across 5 benchmarks is a serious engineering and experimental effort. The 2M+ record scale and systematic confound control (engine fix) go well beyond typical evaluation papers. The confound discovery itself is a standalone methodological contribution that will benefit future precision-comparison studies.

- **S2. The benchmark-dependent variance gradient is a genuine empirical contribution.** The systematic relationship between task difficulty and variance structure (item_id decreasing from 58.4% to 42.1%, temperature-item interactions increasing from 5.8% to 10.4% as accuracy drops) is not something that could be predicted from first principles in its precise quantitative form. This quantifies an intuition the field has had but never pinned down, and provides task-specific guidance for evaluation design.

- **S3. The two-level separability result is well-formulated.** Decomposing separability into aggregate (<0.5%) and item-conditional (14.2%) components is more informative than a binary answer. The "empirical license with caveats" framing is mature and useful for practitioners.

- **S4. D-study budgets fill a real practical gap.** The concrete recommendation of 600 items / 3 prompts / 2 seeds for G >= 0.90 on MMLU, with cross-benchmark variation (550--1100 items), is immediately actionable. The 10:1 marginal effectiveness ratio (items vs. prompts) is a memorable, policy-relevant number.

- **S5. Cross-paradigm extension is conceptually valuable.** Showing that the variance hierarchy inverts between inference (prompt/temperature dominate secondary factors) and fine-tuning (seed/LR dominate) adds structural insight, even if the specific fine-tuning setup is narrow.

---

## Weaknesses

- **W1 (Major). Incremental novelty over Mesting (2026).** The core methodological contribution is extending Mesting's G-theory framework by adding infrastructure facets. But these infrastructure facets turn out to contribute negligibly: hardware 0.6%, precision 0.3%. The paper's most cited finding -- item dominance -- does not depend on the infrastructure extension; it would emerge from a Mesting-style design with fixed infrastructure. The "first fully-crossed" claim is technically true but the marginal novelty of crossing infrastructure with methodology is thin when the crossed factors contribute <1% variance each. The paper needs to be more honest about this: the infrastructure extension is a confirmatory null result (good to know, but not a breakthrough), and the paper's actual novelty lies in the cross-benchmark variance gradient, the engine confound, and the D-study budgets -- none of which require infrastructure crossing.

- **W2 (Major). Severely deficient related work -- critical methodological predecessors are missing.** The bibliography contains only 7 references, which is far below the standard for a top venue submission. Specific omissions that directly affect novelty positioning:

  - **Bouthillier et al. (2021), "Accounting for Variance in Machine Learning Benchmarks" (JMLR):** This is the closest ML-native predecessor -- it decomposes variance across hyperparameters, data splits, and random seeds using ANOVA. Not citing it is a serious omission that inflates the paper's apparent novelty.
  - **IRT-based item analysis in NLP:** Lalor et al. (2019, NAACL), Rodriguez et al. (2021, ACL), Vania et al. (2021) apply Item Response Theory to NLP benchmarks, directly relevant to the item dominance finding. The paper claims item selection is under-studied, but IRT has been analyzing item-level properties for years.
  - **Benchmark subsampling literature:** Polo et al. (2024, "tinyBenchmarks"), HELM-Lite, Perlitz et al. (2023) all address the same practical question (how many items do you need?) from different angles. The D-study budget contribution would be better contextualized against these.
  - **Brennan (2001), "Generalizability Theory":** The foundational G-theory textbook is mentioned in the paper summary but absent from the actual bibliography. For a paper whose entire methodology is G-theory, this is a conspicuous omission.
  - **Shavelson & Webb (1991):** Another canonical G-theory reference.
  - **Henderson et al. (2018), "Deep Reinforcement Learning that Matters":** Pioneering work on variance in ML evaluation, directly relevant context.
  - **Pineau et al. (2021), ML Reproducibility Checklist:** Broader reproducibility context.
  - **Lu et al. (2022):** Ordering effects in multiple-choice evaluation, relevant to the ordering facet.
  - **Nunnally & Bernstein (1994):** The paper invokes G >= 0.80 as a psychometric threshold without citing the source.

  The missing references include direct methodological predecessors (Bouthillier), alternative measurement frameworks for the same phenomenon (IRT papers), and work addressing the same practical question (tinyBenchmarks). Adding these would substantially change the novelty positioning and likely require rewriting the related work section.

- **W3 (Major). Item dominance is partially a tautological consequence of item difficulty variation.** Any assessment instrument with a wide difficulty range will show item variance as the dominant source -- this is a well-known property in psychometrics (Brennan, 2001, Chapter 3). The paper's own Discussion section explains exactly why this must be the case. The framing as "surprising" ("researchers are optimizing the wrong knobs") oversells a finding that is expected from first principles. The contribution is in quantifying the magnitude and its benchmark-dependence, but the paper frames it as if the community should be shocked. A more honest framing would acknowledge: "Item dominance is expected from measurement theory; what we contribute is (a) its precise magnitude in LLM evaluation, (b) its systematic variation with task difficulty, and (c) the D-study implications showing current practices are far more under-powered than previously appreciated."

- **W4 (Moderate). Pooled-model analysis inflates item_id and obscures the signal.** Pooling 4 models treats them as exchangeable observations, but model-item interactions (some items are harder for Mistral than Qwen) get absorbed into the item_id component. The per-model analysis (Table 2) partially addresses this (range 54.7--62.0%), but the headline 58.4% figure from the pooled analysis is the one emphasized throughout. If model were treated as a crossed random facet (as G-theory would normally prescribe), the item_id share could decrease and model-item interaction would become visible. The paper should explain why model is not treated as a facet in the primary analysis.

- **W5 (Moderate). The fine-tuning extension is architecturally mismatched.** The paper claims findings "extend to fine-tuning settings," but RoBERTa-large (355M, encoder-only, classification) is architecturally distant from the 7--14B decoder-only models used in inference experiments. Fine-tuning a decoder model (even 7B with LoRA) on a generation task would be far more compelling evidence of cross-paradigm generalization. As stated, the fine-tuning results are an independent (interesting) study of RoBERTa variance structure, not evidence that the inference findings generalize to fine-tuning.

- **W6 (Moderate). The 0.5% separability threshold is arbitrary.** The threshold is not derived from G-theory, psychometrics, or any principled argument. The observed value (0.5%) lands exactly on this threshold, making the binary "separability holds" conclusion fragile. A sensitivity analysis (what happens at 0.25%? at 1%?) or a bootstrap CI on the total direct interaction variance would be more informative than a pass/fail test against an arbitrary cutoff.

- **W7 (Minor). The "fully crossed" claim is overstated across experiments.** MMLU has the richest factorial design; other benchmarks use reduced designs (2 precisions, 2 temperatures). Hardware crossing is only on MMLU (Exp. 3). The 14B extension uses a reduced facet set. Claims about cross-benchmark separability and scale invariance rest on narrower evidence than the "fully crossed" framing implies. The paper should clearly delineate which claims rest on full crossing and which on partial designs.

- **W8 (Minor). No figures.** The paper is entirely tables, which significantly weakens communication. The D-study projection curves (G vs. evaluation budget, with separate lines for scaling items/prompts/seeds) would make the 10:1 effectiveness ratio immediately visible. Stacked-bar variance decompositions across benchmarks would make the difficulty gradient visually compelling. The absence of any figures is unusual for a top venue paper and reduces impact.

- **W9 (Minor). Mesting (2026) venue discrepancy.** The paper cites Mesting as "Proceedings of ACL, 2026" but the literature map lists it as "arXiv" (2604.11581). If Mesting is an arXiv preprint, the positioning claim ("first fully-crossed G-study") is weaker because Mesting may not have been peer-reviewed, and the comparison is less meaningful. The venue should be verified and stated accurately.

---

## Questions for Authors

1. How would the variance decomposition change if model were included as a crossed random facet rather than pooled? Specifically, what share of variance would model-item interaction absorb, and would it reduce item_id's dominance below 50%?

2. How does your D-study budget recommendation compare to tinyBenchmarks (Polo et al., 2024) and HELM-Lite, which also address "how many items suffice?" from different methodological angles? Do your G-theory projections agree with or contradict their empirical subsampling results?

3. Can you justify the 0.5% separability threshold from psychometric or statistical principles? If the observed direct interaction were 0.7% instead of 0.5%, would you change the conclusion?

4. Bouthillier et al. (2021) decomposed ML benchmark variance using ANOVA across hyperparameters, data splits, and seeds. How does your G-theory decomposition relate to and improve upon their approach? This comparison is essential for positioning.

5. Why was RoBERTa-large chosen for the fine-tuning extension rather than a decoder-only model (e.g., Llama-3.1-8B with LoRA on a generation task)? The architectural mismatch makes cross-paradigm generalization claims difficult to sustain.

6. The paper invokes G >= 0.80 as "minimally acceptable in psychometrics" -- what is the citation for this threshold? Is it appropriate to transfer psychometric reliability standards to LLM evaluation without discussion of whether the analogy holds?

7. Would item dominance survive if the judge/scorer were added as a facet? Mesting found judge at 43.8%. If your design included judge variation, item_id might drop to 25--30%, fundamentally changing the narrative. How do you reconcile your "item dominance" story with Mesting's "judge dominance" story?

8. The paper claims "over 2 million evaluation records" but the experiment counts appear to sum to ~3.17M. Which is correct?

---

## Score and Recommendation

**Score: 3/6 (Weak Reject)**
**Confidence: High**

**Recommendation: Borderline Reject**

The paper presents a substantial empirical effort with real practical value in the D-study budgets and the cross-benchmark variance gradient. The engine confound discovery is a genuine methodological contribution. However, the novelty over Mesting (2026) is incremental -- the infrastructure extension yields near-null results -- and the paper's framing significantly oversells the findings. The headline claim of item dominance is expected from measurement theory and would emerge without the infrastructure extension. The severely sparse bibliography (7 references) with critical omissions (Bouthillier et al., IRT literature, tinyBenchmarks, Brennan, Shavelson & Webb) inflates the apparent novelty and is below the standard for a top venue. The fine-tuning extension is architecturally mismatched, the separability threshold is arbitrary with the result landing exactly on the boundary, and the paper lacks any figures.

The core empirical contribution -- quantifying the benchmark-dependent variance gradient and providing actionable D-study budgets -- is valuable and fills a genuine gap. If the authors (a) honestly reframe novelty as "confirmatory null on infrastructure + quantitative benchmark-dependent gradient + D-study budgets" rather than "first fully-crossed G-study," (b) expand the bibliography to include critical predecessors (especially Bouthillier et al., IRT literature, and tinyBenchmarks), (c) add figures, and (d) address the pooled-model concern, this could become a solid contribution. These revisions are achievable without new experiments, and I would consider upgrading to a 4 (Weak Accept) if addressed satisfactorily.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96f8379e-f6e7-4ae5-8a82-c01f3de9e961",
  "isSidechain": true,
  "agentId": "adac42d84d8448a91",
  "requestId": "req_011CbEPTgPfk5s9inLGRYt4t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbeb0187-da3a-4651-869a-cd97d2c1a174",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uGwRWWXrMnf4VB81iZowM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 63743,
      "output_tokens": 3289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 761
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3289,
          "cache_read_input_tokens": 63743,
          "cache_creation_input_tokens": 761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 761,
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
