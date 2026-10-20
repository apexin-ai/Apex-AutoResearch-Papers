# Research conversation: You are Reviewer R1 for a top ML venue review. Your focus is **methodology and experimental rigor**. Evaluate the paper 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab95321e8cc70eb32.jsonl`
- **Structured JSON:** [`a1589c91ebaec6bd6cb5.json`](../../sessions/a1/a1589c91ebaec6bd6cb5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-20T19:38:28.673Z_

You are Reviewer R1 for a top ML venue review. Your focus is **methodology and experimental rigor**. Evaluate the paper below using a 6-point scale (1=Strong Reject, 6=Strong Accept), with acceptance rate ~25%.

## Paper Summary

**Title:** Benchmark-Dependent Variance Structure in LLM Evaluation: A Generalizability Theory Analysis of Infrastructure and Methodological Reproducibility

**Core claims:**
1. Item selection is the single largest variance source across MC benchmarks (30–46%), but this dominance is benchmark-dependent: on reasoning tasks (GSM8K, MATH), temperature–item and seed–item interactions rival or exceed item main effects.
2. Infrastructure and methodology factors are approximately separable at the aggregate level (direct interaction < 1%), though both interact substantially with item difficulty.
3. D-study projections show tripling item count is 3–5× more cost-effective than tripling prompts or seeds for G ≥ 0.90, but required budgets are benchmark-dependent (380–950 items).

**Methodology:**
- G-theory framework (Cronbach et al., 1972; Brennan, 2001) applied to LLM evaluation
- Three facet layers: Infrastructure (hardware type, precision: FP32/BF16/FP16/LayerCast), Methodology (6 prompt templates, 6 seeds, temperatures {0.0, 0.3, 0.7}, 4 option orderings), Measurement (200 stratified-sampled items per benchmark)
- Variance components estimated via REML using mixed-effects models
- Bootstrap CIs (1000 resamples), Kruskal-Wallis tests, permutation tests
- 6 models: 4 at 8B (Llama-3.1-8B-Instruct, Qwen3-8B, Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3), 2 at 14B (Qwen3-14B, DeepSeek-R1-Distill-14B)
- 5 benchmarks: MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH
- Fine-tuning scenario: RoBERTa-large on SST-2, MNLI, RTE, COPA
- All inference uses vLLM 0.9.2 with V0 engine and enforce_eager=True

**Experiments:**
1. Full-Scale G-Study on MMLU: 4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 items = 1,036,800 records. Item(i)=43%, Residual=21%, Prompt×Item=6.2%, Temp×Item=5.8%, Infra×Method=0.3%. G(current)=0.42.
2. Multi-Benchmark Replication: GSM8K, ARC-C, HellaSwag (230,400 records each). HellaSwag item=45%, ARC-C item=38%, GSM8K item=28% with residual+temp dominating. Kruskal-Wallis H=47.3, p<0.001.
3. MATH Extension: 200 items. Item=22%, Temp×Item=15%, Seed×Item=11%, Residual=30%. G=0.30, needs ~950 items for G≥0.90 (MATH has only 500 total).
4. Multi-Hardware G-Study: 2 GPU types, partial crossing (2/4 models). Total hardware-related=4.1%, Direct Hardware×Method=0.5%. G drops 0.42→0.38 with hardware.
5. 14B Model Extension: Qwen3-14B item=46%, DeepSeek-R1-Distill-14B item=34% with elevated temp×item=11%.
6. Fine-Tuning G-Study: RoBERTa-large, 1728 runs. SST-2: LR=31%, Seed=18%, Item=22%. G(current)=0.52, G(5seeds,3LR)=0.78.
7. LayerCast Precision Study: 4th precision condition. ~18% reduction in precision-related variance, item agreement with BF16=94%.
8. D-Study Projections: Triple items → G=0.82, triple prompts → G=0.51. Items for G≥0.90: MMLU=520, HellaSwag=380, GSM8K=780, MATH=950. Cost-effectiveness ratio items/prompts=3.8×, items/seeds=7.2×.

**Key tables:** Table 1 (MMLU variance decomposition with CI only for item), Table 3 (G-coefficients, single row), Table 4 (cross-benchmark), Tables 7-8 (hardware, partial crossing), Table 10 (fine-tuning), Table 13-15 (D-study).

## Experimental Design Reference (what was planned)

The full experimental design planned 8 experiments:
- exp-001: Full-scale MMLU with confound fix (covered as Exp 1)
- exp-002: Multi-benchmark on GSM8K/ARC-C/HellaSwag (covered as Exp 2)
- exp-003: Multi-hardware G-study (covered as Exp 4, but partial)
- exp-004: D-study projections (covered as Exp 8)
- exp-005: 14B model extension (covered as Exp 5)
- exp-006: Fine-tuning G-study (covered as Exp 6)
- exp-007: LayerCast precision study (covered as Exp 7)
- exp-008: MATH benchmark extension (covered as Exp 3)

All 8 planned experiments appear in the paper.

## Your Review Task

Evaluate:
1. **Statistical methodology**: Is G-theory correctly applied? Are REML estimates appropriate? Are the bootstrap CIs adequate? Are there issues with the mixed-effects model specification?
2. **Experimental design**: Is the fully-crossed design truly fully crossed? Are there confounds? Is 200 items sufficient for stable variance component estimation? How does the partial hardware crossing affect claims?
3. **Results interpretation**: Are claims well-supported by the data? Are effect sizes meaningful? Are CIs reported where needed?
4. **Reproducibility**: Is the methodology described in enough detail to replicate?
5. **Missing experiments or controls**: What's missing relative to the claims?

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
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "527c3aa5-66d1-4a09-b452-8a1236873102",
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

_source line 2 · 2026-05-20T19:38:28.677Z_

```json
{
  "parentUuid": "527c3aa5-66d1-4a09-b452-8a1236873102",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
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
  "uuid": "287d9c5f-0b34-4842-982c-4e67cfbca21f",
  "timestamp": "2026-05-20T19:38:28.677Z",
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

_source line 3 · 2026-05-20T19:38:31.598Z_



I need to thoroughly review this paper. Let me first read the actual paper and any available artifacts to ground my review in the specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "287d9c5f-0b34-4842-982c-4e67cfbca21f",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPMg2vEUkWipPdwAcoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2574e4da-e23b-4e10-9386-669de9a59725",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WAimrMTFNN1Ey9pKWUopJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7801,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7801,
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

_source line 4 · 2026-05-20T19:38:33.178Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016VUs9ABP7khHVwL7RBRYCw`</summary>

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
  "parentUuid": "2574e4da-e23b-4e10-9386-669de9a59725",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPMg2vEUkWipPdwAcoG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2d8f573-9128-42d5-9b3a-2e0f2d76d4e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WAimrMTFNN1Ey9pKWUopJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7801,
      "cache_read_input_tokens": 8250,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7801,
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

_source line 5 · 2026-05-20T19:38:33.183Z_

<details><summary>↩ Tool result · `toolu_016VUs9ABP7khHVwL7RBRYCw`</summary>

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
  "parentUuid": "d2d8f573-9128-42d5-9b3a-2e0f2d76d4e1",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "193f0940-cd99-44de-b78f-34ab4974c5d3",
  "sourceToolAssistantUUID": "d2d8f573-9128-42d5-9b3a-2e0f2d76d4e1",
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

_source line 6 · 2026-05-20T19:38:35.230Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01RBKjzcb344ow3YT1JPmwiB`</summary>

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
  "parentUuid": "193f0940-cd99-44de-b78f-34ab4974c5d3",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPN1JYWb6RLZRFsZvTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af51b512-90ed-4b6f-9b7c-0b5044294093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SG33AesnDXEtHJaLmpfnqA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16051,
      "output_tokens": 74,
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
          "output_tokens": 74,
          "cache_read_input_tokens": 16051,
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

_source line 7 · 2026-05-20T19:38:35.258Z_

<details><summary>↩ Tool result · `toolu_01RBKjzcb344ow3YT1JPmwiB`</summary>

```text
{"result":"# 项目 nlp_variance_gtheory 概况\n\n## 实验状态 (2 个)\n\n- **bf16_eager_disentangle**: DONE (negative) — \n- **mvp_phase_a**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\n\n## 趋势\n成功 1 / 负向 1 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32570: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af51b512-90ed-4b6f-9b7c-0b5044294093",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "f3f045fc-8dbf-48ec-b29a-a0dd9849d261",
  "sourceToolAssistantUUID": "af51b512-90ed-4b6f-9b7c-0b5044294093",
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

_source line 8 · 2026-05-20T19:38:47.185Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SuGreEo4EH13KtJrjRmFVi`</summary>

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
  "parentUuid": "f3f045fc-8dbf-48ec-b29a-a0dd9849d261",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPNAh6aFjroNbS88Tpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f789b3d-5751-46a2-bc23-fc43fa5d974b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pmft6RwX1iZmcMhEJt6p3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 17508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 523,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 9 · 2026-05-20T19:38:47.193Z_

<details><summary>↩ Tool result · `toolu_01SuGreEo4EH13KtJrjRmFVi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\\n\\n## 趋势\\n成功 1 / 负向 1 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32570: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 800, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f789b3d-5751-46a2-bc23-fc43fa5d974b",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "53ae83f3-96d4-438d-b5d6-d1dcfc795e5c",
  "sourceToolAssistantUUID": "3f789b3d-5751-46a2-bc23-fc43fa5d974b",
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

_source line 10 · 2026-05-20T19:38:47.647Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XpMxcYAxNq2HXR9r49cFzL`</summary>

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
  "parentUuid": "53ae83f3-96d4-438d-b5d6-d1dcfc795e5c",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPNAh6aFjroNbS88Tpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e4ad2c7-7881-4d34-b056-017457547aba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pmft6RwX1iZmcMhEJt6p3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 17508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 523,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 11 · 2026-05-20T19:38:47.655Z_

<details><summary>↩ Tool result · `toolu_01XpMxcYAxNq2HXR9r49cFzL`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No memory.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e4ad2c7-7881-4d34-b056-017457547aba",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "19a66825-05d0-4ba3-bdf4-7e5a3b563c89",
  "sourceToolAssistantUUID": "8e4ad2c7-7881-4d34-b056-017457547aba",
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

_source line 12 · 2026-05-20T19:38:48.237Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019vz9fMddoe9rNKeGkhbLTf`</summary>

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
  "parentUuid": "19a66825-05d0-4ba3-bdf4-7e5a3b563c89",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPNAh6aFjroNbS88Tpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3f484a5-2a6e-4b01-b6a4-6e35a1c31cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pmft6RwX1iZmcMhEJt6p3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 17508,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 523
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 17508,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 523,
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

_source line 13 · 2026-05-20T19:38:48.245Z_

<details><summary>↩ Tool result · `toolu_019vz9fMddoe9rNKeGkhbLTf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/ROADMAP.md\", \"content\": \"# nlp_variance_gtheory — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:01 UTC | 更新原因: Post-MVP kickoff: paper_framing + experiment_plan 完成，Dream 已提交，ROADMAP 转 Research 阶段 dashboard\\n\\n## 核心方向\\n用 G-theory 联合分解 LLM 评估中 infrastructure × methodology × item 的方差。核心发现：item 选择主导方差（58.4%），infrastructure 与 methodology 在聚合层面近似可分但效应是 item-conditional 的。产出可量化的 reproducibility budget。详见 paper_framing.md。\\n\\n## 当前进展\\n- 阶段: **Research**（MVP 已通过，D001）\\n- MVP 结论: item_id=58.4%, precision×item=7.2%, temp×item=6.9%, prompt×item=5.7%, 直接 infra×method <0.02%\\n- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟进行中 (dream_20260520T190053)\\n- 服务器: westd-32570（4× RTX PRO 6000 96GB），第二种 GPU 待 Manager 分配\\n- float32 引擎混淆需 exp-001 解决（统一 V0 enforce_eager）\\n\\n## 实验计划（详见 experiment_plan.yaml）\\n| ID | Claim | Priority | GPU·h | 状态 |\\n|----|-------|----------|-------|------|\\n| exp-001 | Item dominance at scale (4 models × 200 items × fix FP32) | P0 | 100 | planned |\\n| exp-002 | Multi-benchmark (GSM8K/ARC/HellaSwag) | P0 | 200 | planned |\\n| exp-003 | Multi-hardware crossing | P0 | 120 | blocked (待第二种 GPU) |\\n| exp-004 | D-study reproducibility budget | P0 | 0 | planned (分析) |\\n| exp-005 | 14B scale extension | P1 | 100 | planned |\\n| exp-006 | Fine-tuning G-study (RoBERTa) | P1 | 200 | planned |\\n| exp-007 | LayerCast mitigation | P2 | 30 | planned |\\n| exp-008 | MATH benchmark | P2 | 50 | planned |\\n\\nTotal: P0=420h, P1=300h, P2=80h\\n\\n## 近期任务\\n- [ ] Dream 模拟完成 → 审视报告 → 调整 framing/plan（如需要）\\n- [ ] Dream 通过后批准 exp-001（可立即在 westd-32570 上执行）\\n- [ ] Agent 完成 text_exact_match 双变量分析（MVP 数据补充分析）\\n- [ ] 等待 Manager 回复第二种 GPU → 解除 exp-003 blocked\\n\\n## GPU 预算\\n- 本项目分配: westd-32570 cuda:0-3（4× RTX PRO 6000 96GB）\\n- 第二种 GPU: 待 Manager 分配\\n- P0 预估: 420 GPU·h | P1: 300 | P2: 80\\n\\n## 投稿目标\\n- 主投: AAAI 2027（abstract Jul 21, paper Jul 28 — 9 周）\\n- 备选: ACL 2027 ARR Oct 15（21 周）/ TACL rolling\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-20 | 采用 dual-metric (binary correct + text exact match) | — |\\n| D001 | 2026-05-20 | MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4 | — |\\n\\n\", \"total_chars\": 2064, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3f484a5-2a6e-4b01-b6a4-6e35a1c31cb3",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "c33664c3-09a2-45b4-8b9b-6f35a116d98c",
  "sourceToolAssistantUUID": "a3f484a5-2a6e-4b01-b6a4-6e35a1c31cb3",
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

_source line 14 · 2026-05-20T19:38:51.313Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01414x1qeBtr6T5PJXrNNrAm`</summary>

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
  "parentUuid": "c33664c3-09a2-45b4-8b9b-6f35a116d98c",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPP82dwmZBkSJE1uGRU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8192ed70-5047-4810-8d4d-d5238fe5e82f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZRWiYgUd1Pqr99gz4uMNC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2128,
      "cache_read_input_tokens": 18031,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 15 · 2026-05-20T19:38:51.324Z_

<details><summary>↩ Tool result · `toolu_01414x1qeBtr6T5PJXrNNrAm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md\", \"content\": \"# Paper Framing — nlp_variance_gtheory\\n\\n## Target Venue\\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\\n- Extended: TACL (rolling)\\n\\n## Title\\nReproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory\\n\\n## Core Claims (3 条，可证伪)\\n\\n**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)\\n\\n**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.\\n\\n**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.\\n\\n## Story Spine\\n\\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.\\n\\n**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.\\n\\n**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.\\n\\n**Headline result template**: \\\"In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90.\\\"\\n\\n## Hook (Counter-Intuitive Quantified Claim)\\n\\\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined.\\\"\\n\\n## Narrative Strategy\\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)\\n- **Tension**: \\\"Everyone's optimizing the wrong thing\\\" — the field focuses on prompt/seed/hardware standardization while ignoring item selection\\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\\n- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)\\n- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves\\n\\n## Venue Fit Risks\\n- AAAI: Strong fit for \\\"evaluation methodology\\\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\\n- Reviewer concern 1: \\\"Only open-weight models, not API models\\\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\\n- Reviewer concern 2: \\\"G-theory is borrowed methodology, not novel\\\" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.\\n- Reviewer concern 3: \\\"Item dominance is obvious — harder items have more variance\\\" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n1. **\\\"Only N GPU types\\\"** → exp-003 (multi-hardware crossing) addresses this\\n2. **\\\"float32 engine confound\\\"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)\\n3. **\\\"Only MMLU\\\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag\\n4. **\\\"Small item sample\\\"** → exp-001 expands from 50 to 200 items\\n5. **\\\"No training-time analysis\\\"** → exp-006 (fine-tuning G-study with RoBERTa)\\n6. **\\\"Missing scale validation\\\"** → exp-005 (14B models)\\n7. **\\\"G-theory may not be right framework\\\"** → Compare with ANOVA and regression decomposition as sensitivity analysis\\n\\n## Design Decisions\\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.\\n\", \"total_chars\": 6768, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8192ed70-5047-4810-8d4d-d5238fe5e82f",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "8173ebb9-8e89-4cd3-8bb1-77a05503c1ff",
  "sourceToolAssistantUUID": "8192ed70-5047-4810-8d4d-d5238fe5e82f",
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

_source line 16 · 2026-05-20T19:38:51.883Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01N4kT2qAMK4a1XHnkssBSDi`</summary>

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
  "parentUuid": "8173ebb9-8e89-4cd3-8bb1-77a05503c1ff",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPP82dwmZBkSJE1uGRU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23ec45c7-2495-44a6-bb69-571decefa24d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZRWiYgUd1Pqr99gz4uMNC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2128,
      "cache_read_input_tokens": 18031,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 18031,
          "cache_creation_input_tokens": 2128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2128,
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

_source line 17 · 2026-05-20T19:38:51.890Z_

<details><summary>↩ Tool result · `toolu_01N4kT2qAMK4a1XHnkssBSDi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/decisions.yaml\", \"content\": \"_next_id: 3\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:57 UTC\\n  summary: MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4%），separability 在聚合层面成立，进入\\n    research 阶段\\n  rationale: 5,400 次推理完成，5 个方差分量 ≥5% 且 CI 不含零，pipeline 端到端可运行。核心发现：(1) item 选择是评估方差最大来源；(2)\\n    precision/temperature/prompt 效应是 item-specific 的；(3) 直接的 infrastructure×methodology\\n    交互可忽略（<0.02%）。float32 引擎混淆需全研究阶段解决但不影响 MVP 结论。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:12 UTC\\n  summary: 采用 dual-metric (binary correct + text exact match) 方差分解作为论文核心方法论，Claim\\n    3 改为 metric-conditional reproducibility budget\\n  rationale: MVP 双变量分析揭示截然不同的方差结构：binary correct 下 item_id 主导 (58.4%, G=0.357)；text\\n    exact match 下 prompt×item 主导 (37.5%, G=0.975)。单一 response variable 无法完整描述评估可靠性。Dual-metric\\n    对比是 G-theory 框架的天然优势——\\\"同一实验在不同衡量标准下可靠性完全不同\\\"是比单一 budget 更有力的发现。precision:temperature\\n    交互在 text metric 下显著 (1.3%, CI 不含零)，证明 separability 在细粒度下不完全成立。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n\", \"total_chars\": 997, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23ec45c7-2495-44a6-bb69-571decefa24d",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "133310e0-1852-4a07-a271-c2239583b905",
  "sourceToolAssistantUUID": "23ec45c7-2495-44a6-bb69-571decefa24d",
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

_source line 18 · 2026-05-20T19:38:55.509Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018TTNZqBqhLWnWbYkALrzPk`</summary>

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
  "parentUuid": "133310e0-1852-4a07-a271-c2239583b905",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPPPU58zxMKzN8za76v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cb78fbe-4fc8-478f-a69b-b73bf76b742a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6bhWMewgfvwNcug9zzHqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2810,
      "cache_read_input_tokens": 20159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2810,
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

_source line 19 · 2026-05-20T19:38:55.525Z_

<details><summary>↩ Tool result · `toolu_018TTNZqBqhLWnWbYkALrzPk`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/paper.tex
artifacts/dream_reports/dream_20260520T190053/median/paper.tex
artifacts/dream_reports/dream_20260520T190053/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cb78fbe-4fc8-478f-a69b-b73bf76b742a",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "ab0a70fd-af8f-4042-95a3-57362eeb16c6",
  "sourceToolAssistantUUID": "4cb78fbe-4fc8-478f-a69b-b73bf76b742a",
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

_source line 20 · 2026-05-20T19:38:56.580Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01We7tDLRHJbk4Gx48ETdgPY`</summary>

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
  "parentUuid": "ab0a70fd-af8f-4042-95a3-57362eeb16c6",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPPPU58zxMKzN8za76v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e51d57b-ae97-49c4-ae7a-3879afde66da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6bhWMewgfvwNcug9zzHqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2810,
      "cache_read_input_tokens": 20159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2810,
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

_source line 21 · 2026-05-20T19:38:56.604Z_

<details><summary>↩ Tool result · `toolu_01We7tDLRHJbk4Gx48ETdgPY`</summary>

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
mistakes.yaml
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e51d57b-ae97-49c4-ae7a-3879afde66da",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "2e0cd148-87b1-4f5d-afc5-918fd213fe5a",
  "sourceToolAssistantUUID": "3e51d57b-ae97-49c4-ae7a-3879afde66da",
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

_source line 22 · 2026-05-20T19:38:56.704Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vo23LeewC1ZxfGBxkkxB5a`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e0cd148-87b1-4f5d-afc5-918fd213fe5a",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPPPU58zxMKzN8za76v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b457d27-1bda-4fb7-8735-16087e4c761d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6bhWMewgfvwNcug9zzHqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2810,
      "cache_read_input_tokens": 20159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2810,
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

_source line 23 · 2026-05-20T19:38:56.719Z_

<details><summary>↩ Tool result · `toolu_01Vo23LeewC1ZxfGBxkkxB5a`</summary>

```text
artifacts/code/src/__init__.py
artifacts/code/src/data/__init__.py
artifacts/code/src/design/__init__.py
artifacts/code/src/inference/__init__.py
artifacts/code/src/analysis/__init__.py
artifacts/code/src/data/sample_mmlu.py
artifacts/code/src/data/few_shot.py
artifacts/code/src/analysis/visualize.py
artifacts/code/src/analysis/d_study.py
artifacts/code/src/inference/sanity_check.py
artifacts/code/src/analysis/variance_decomposition.py
artifacts/code/src/inference/vllm_runner.py
artifacts/code/src/design/generate_design.py
artifacts/code/src/data/prompt_templates.py
artifacts/code/src/inference/run_experiment.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b457d27-1bda-4fb7-8735-16087e4c761d",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "b0430c54-3504-470e-b289-a9cb93a206b5",
  "sourceToolAssistantUUID": "1b457d27-1bda-4fb7-8735-16087e4c761d",
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

_source line 24 · 2026-05-20T19:38:59.853Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TZcXpY44yMSQ3HzqR9BJcr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0430c54-3504-470e-b289-a9cb93a206b5",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPPkpi43DvznxFFKcH9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44192de7-e748-4e09-8236-21e7f85e6361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4ruHxfxPnyXCTnUZbqbwR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 22969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1002,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 25 · 2026-05-20T19:38:59.862Z_

<details><summary>↩ Tool result · `toolu_01TZcXpY44yMSQ3HzqR9BJcr`</summary>

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
90	X = \mu + \alpha_p + \alpha_i + \sum_j \alpha_{f_j} + \sum_{j<l} \alpha_{f_j f_l} + \cdots + \epsilon
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44192de7-e748-4e09-8236-21e7f85e6361",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "f03e8a3f-5c20-4a0b-bb2e-cec4acf3ac9a",
  "sourceToolAssistantUUID": "44192de7-e748-4e09-8236-21e7f85e6361",
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

_source line 26 · 2026-05-20T19:39:00.120Z_

<details open><summary>🔧 Tool call — Read · `toolu_013m1jHaZAifkFpduVVaQZB2`</summary>

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
  "parentUuid": "f03e8a3f-5c20-4a0b-bb2e-cec4acf3ac9a",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPPkpi43DvznxFFKcH9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16e994cd-4f0e-4c19-8dbc-7f944112fced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4ruHxfxPnyXCTnUZbqbwR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 22969,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1002
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 22969,
          "cache_creation_input_tokens": 1002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1002,
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

_source line 27 · 2026-05-20T19:39:00.127Z_

<details><summary>↩ Tool result · `toolu_013m1jHaZAifkFpduVVaQZB2`</summary>

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
  "parentUuid": "16e994cd-4f0e-4c19-8dbc-7f944112fced",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "59e8d1ba-b172-4a8a-92f0-fb9a330b41a0",
  "sourceToolAssistantUUID": "16e994cd-4f0e-4c19-8dbc-7f944112fced",
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

_source line 28 · 2026-05-20T19:39:04.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_015nRJkZPwmPxUegias5vCdb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e8d1ba-b172-4a8a-92f0-fb9a330b41a0",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPPzhPUix8cmfwsM4Zu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86947f79-7387-4be7-aca2-204076c3ac4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QD61vTM8qahFbGfhaNyoCN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6807,
      "cache_read_input_tokens": 23971,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6807
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 23971,
          "cache_creation_input_tokens": 6807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6807,
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

_source line 29 · 2026-05-20T19:39:04.781Z_

<details><summary>↩ Tool result · `toolu_015nRJkZPwmPxUegias5vCdb`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86947f79-7387-4be7-aca2-204076c3ac4a",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "77741cb3-4b5f-44f6-ab99-643bea460a8b",
  "sourceToolAssistantUUID": "86947f79-7387-4be7-aca2-204076c3ac4a",
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

_source line 30 · 2026-05-20T19:39:09.344Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BCczLYjW7bsB1FSmsBFETh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
  "offset": 500,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77741cb3-4b5f-44f6-ab99-643bea460a8b",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPQLdCT86EKRYQG4LPc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6836127d-9839-43a8-b77f-0120735dd0fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rh9WsRwFmCdjvR1dunsaVn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6541,
      "cache_read_input_tokens": 30778,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6541
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 30778,
          "cache_creation_input_tokens": 6541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6541,
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

_source line 31 · 2026-05-20T19:39:09.348Z_

<details><summary>↩ Tool result · `toolu_01BCczLYjW7bsB1FSmsBFETh`</summary>

```text
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
  "parentUuid": "6836127d-9839-43a8-b77f-0120735dd0fd",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "0dcfe115-976a-44bf-918c-3eb570248078",
  "sourceToolAssistantUUID": "6836127d-9839-43a8-b77f-0120735dd0fd",
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

_source line 32 · 2026-05-20T19:39:12.202Z_

Now let me also check the imagined experiments and review context for the dream report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dcfe115-976a-44bf-918c-3eb570248078",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPQg8htq9oTUEM8x6d3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba1951ff-68af-40b9-b79f-f360ccffaa2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxfUXjuqc5bQo2erNndXLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 37319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 506,
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

_source line 33 · 2026-05-20T19:39:12.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JtP8HgHDcJDEM5t2dZqhqH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba1951ff-68af-40b9-b79f-f360ccffaa2f",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPQg8htq9oTUEM8x6d3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed512405-973c-4520-bdb5-17b55f63fcce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxfUXjuqc5bQo2erNndXLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 37319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 506,
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

_source line 34 · 2026-05-20T19:39:12.939Z_

<details><summary>↩ Tool result · `toolu_01JtP8HgHDcJDEM5t2dZqhqH`</summary>

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
51	    g_6p6s200i: 0.72
52	    g_6p6s200i_3t4o: 0.78
53	  result_rationale: 'MVP中precision主效应0.87%和precision×item交互7.24%主要来自float32使用不同vLLM
54	    engine路径（非V0时触发不同kernel）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后，三种精度走同一compute
55	    path， FP32/BF16/FP16准确率差收敛至0.5pp以内（纯numerical noise水平）。precision主效应从0.87%降至~0.3%，
56	    precision×item从7.24%降至~1.8%。这些被释放的方差份额主要回流到residual和item_id， 使item_id维持在~58%（与MVP一致，因为item
57	    difficulty本身是真实信号，不受engine confound影响）。 4个模型均以item_id为rank-1组分，因为MMLU的item difficulty分布（从trivial到expert-level）
58	    在所有7-9B模型上产生类似的accuracy ceiling/floor效应。Gemma-2略高因其instruction-tuned特性 使其对easy
59	    items更稳定（floor更高），Mistral略低因其在部分domain上accuracy更平坦。 200 items（分层采样）比MVP的50 items提供更稳定的方差估计，置信区间收窄约50%。
60	
61	    '
62	  tables:
63	  - name: 'Table 1: Variance Component Estimates — MMLU 200 items, 4 models pooled'
64	    columns:
65	    - Component
66	    - '% Variance'
67	    - SE
68	    - 95% CI Lower
69	    - 95% CI Upper
70	    - MVP (50 items)
71	    rows:
72	    - - item_id
73	      - 58.4
74	      - 2.1
75	      - 54.3
76	      - 62.5
77	      - 58.4
78	    - - residual
79	      - 16.8
80	      - 0.9
81	      - 15.0
82	      - 18.6
83	      - 17.6
84	    - - prompt×item
85	      - 6.1
86	      - 0.7
87	      - 4.7
88	      - 7.5
89	      - 5.7
90	    - - temp×item
91	      - 5.8
92	      - 0.6
93	      - 4.6
94	      - 7.0
95	      - 6.9
96	    - - seed×item
97	      - 2.9
98	      - 0.4
99	      - 2.1
100	      - 3.7
101	      - 2.7
102	    - - precision×item
103	      - 1.8
104	      - 0.3
105	      - 1.2
106	      - 2.4
107	      - 7.2*
108	    - - ordering×item
109	      - 1.4
110	      - 0.3
111	      - 0.8
112	      - 2.0
113	      - —
114	    - - prompt
115	      - 0.9
116	      - 0.3
117	      - 0.3
118	      - 1.5
119	      - —
120	    - - temperature
121	      - 0.7
122	      - 0.2
123	      - 0.3
124	      - 1.1
125	      - —
126	    - - precision
127	      - 0.3
128	      - 0.1
129	      - 0.1
130	      - 0.5
131	      - 0.87*
132	    - - ordering
133	      - 0.3
134	      - 0.1
135	      - 0.1
136	      - 0.5
137	      - —
138	    - - seed
139	      - 0.1
140	      - 0.05
141	      - 0.0
142	      - 0.2
143	      - —
144	  - name: 'Table 2: Per-Model item_id Variance Share'
145	    columns:
146	    - Model
147	    - item_id %
148	    - Next Largest
149	    - Next %
150	    rows:
151	    - - Qwen3-8B
152	      - 59.8
153	      - residual
154	      - 16.2
155	    - - Llama-3.1-8B
156	      - 57.1
157	      - residual
158	      - 17.8
159	    - - Gemma-2-9B-IT
160	      - 62.0
161	      - residual
162	      - 14.9
163	    - - Mistral-7B-v0.3
164	      - 54.7
165	      - residual
166	      - 18.5
167	  figures_description:
168	  - 'Fig 1: Stacked-bar variance decomposition — MVP (confounded) vs exp-001 (fixed),
169	    side-by-side。左栏显示precision和precision×item的膨胀，右栏显示修复后两者坍缩，item_id占比不变。'
170	  - 'Fig 2: 4-panel per-model stacked bars，展示item_id始终为rank-1的cross-model consistency。'
171	  - 'Fig 3: FP32 vs BF16 accuracy scatter (per-item)，MVP中slope偏离1.0，exp-001中回归到~1.0。'
172	  analysis: '核心发现：engine confound修复后item dominance完全稳健，precision主效应从0.87%降至0.3%。 这同时验证了Claim
173	    1（item dominance）和提供了方法论贡献（engine配置对variance attribution的影响）。 4个模型一致性消除了"Qwen3特例"的concern。200
174	    items分层采样提供了足够的statistical power。 Ordering facet新增后占比很小（~1.7% total含interaction），说明item
175	    presentation order不是主要concern。
176	
177	    '
178	- name: Multi-benchmark replication
179	  plan_id: exp-002
180	  description: '4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures
181	    × 4 orderings × 200 items, 分别在GSM8K、ARC-Challenge、HellaSwag上运行。每benchmark总记录 4×2×6×6×2×4×200=230,400。
182	
183	    '
184	  expected_results:
185	    gsm8k_overall_accuracy: 0.583
186	    gsm8k_item_id: 0.487
187	    gsm8k_residual: 0.214
188	    gsm8k_temperature_x_item_id: 0.089
189	    gsm8k_prompt_x_item_id: 0.072
190	    gsm8k_seed_x_item_id: 0.041
191	    gsm8k_precision_x_item_id: 0.012
192	    gsm8k_ordering_x_item_id: 0.018
193	    gsm8k_temperature: 0.024
194	    gsm8k_prompt: 0.015
195	    gsm8k_precision: 0.002
196	    gsm8k_g_current_practice: 0.29
197	    arc_overall_accuracy: 0.597
198	    arc_item_id: 0.551
199	    arc_residual: 0.182
200	    arc_prompt_x_item_id: 0.068
201	    arc_temperature_x_item_id: 0.054
202	    arc_seed_x_item_id: 0.031
203	    arc_precision_x_item_id: 0.014
204	    arc_ordering_x_item_id: 0.016
205	    arc_prompt: 0.011
206	    arc_temperature: 0.008
207	    arc_precision: 0.002
208	    arc_g_current_practice: 0.32
209	    hellaswag_overall_accuracy: 0.712
210	    hellaswag_item_id: 0.527
211	    hellaswag_residual: 0.195
212	    hellaswag_prompt_x_item_id: 0.058
213	    hellaswag_temperature_x_item_id: 0.062
214	    hellaswag_seed_x_item_id: 0.033
215	    hellaswag_precision_x_item_id: 0.011
216	    hellaswag_ordering_x_item_id: 0.019
217	    hellaswag_prompt: 0.008
218	    hellaswag_temperature: 0.006
219	    hellaswag_precision: 0.001
220	    hellaswag_g_current_practice: 0.36
221	    benchmarks_with_item_id_rank1: 4
222	    item_id_range_across_benchmarks:
223	    - 0.487
224	    - 0.584
225	    cross_benchmark_replication_rate: 1.0
226	    models_showing_consistent_pattern: 4
227	  result_rationale: 'GSM8K的item_id占比略低于MMLU（48.7% vs 58.4%），因为数学推理任务引入更多chain-of-thought随机性，
228	    使residual和temperature×item交互膨胀。GSM8K中温度效应更大（temperature×item 8.9%）， 因为CoT生成路径对sampling
229	    temperature更敏感——同一道数学题在不同温度下可能走完全不同的推理链。 但item_id仍然是rank-1组分，因为GSM8K的difficulty
230	    gradient极陡（从单步算术到多步word problem）， 这种item-level variance在所有条件下都主导。ARC-Challenge的item_id（55.1%）接近MMLU，
231	    因为科学推理题的difficulty分布类似（从factual recall到multi-hop inference）。 HellaSwag的item_id（52.7%）也稳健，因为commonsense
232	    completion的item variance主要来自 distractor quality差异——有些items的wrong answers显而易见，有些几乎无法区分。
233	    所有benchmark上precision主效应均<0.3%，确认engine confound fix的泛化性。 4/4 benchmark的item_id
234	    rank-1复现率为100%，支撑"cross-benchmark replication rate = 1.0"。
235	
236	    '
237	  tables:
238	  - name: 'Table 3: Cross-Benchmark Variance Decomposition Summary'
239	    columns:
240	    - Benchmark
241	    - item_id %
242	    - Residual %
243	    - Item-Conditional Total %
244	    - Precision Main %
245	    - G (current)
246	    rows:
247	    - - MMLU
248	      - 58.4
249	      - 16.8
250	      - 16.1
251	      - 0.3
252	      - 0.34
253	    - - GSM8K
254	      - 48.7
255	      - 21.4
256	      - 23.2
257	      - 0.2
258	      - 0.29
259	    - - ARC-Challenge
260	      - 55.1
261	      - 18.2
262	      - 18.3
263	      - 0.2
264	      - 0.32
265	    - - HellaSwag
266	      - 52.7
267	      - 19.5
268	      - 18.3
269	      - 0.1
270	      - 0.36
271	  - name: 'Table 4: GSM8K Per-Model Breakdown'
272	    columns:
273	    - Model
274	    - item_id %
275	    - temp×item %
276	    - prompt×item %
277	    - residual %
278	    rows:
279	    - - Qwen3-8B
280	      - 51.2
281	      - 8.1
282	      - 6.8
283	      - 19.8
284	    - - Llama-3.1-8B
285	      - 47.3
286	      - 9.4
287	      - 7.6
288	      - 22.1
289	    - - Gemma-2-9B-IT
290	      - 50.8
291	      - 8.5
292	      - 6.9
293	      - 20.3
294	    - - Mistral-7B-v0.3
295	      - 43.4
296	      - 10.5
297	      - 8.3
298	      - 23.5
299	  figures_description:
300	  - 'Fig 4: 4-benchmark stacked-bar variance decomposition并排对比。item_id始终为最大色块，但GSM8K的residual和temperature×item色块明显更大。'
301	  - 'Fig 5: Heatmap — benchmark × model × component，展示pattern consistency。色块深浅表示variance
302	    share，item_id行始终最深。'
303	  analysis: 'Item dominance在4个benchmark上全部复现（range 48.7%-58.4%），但幅度因task type有系统性差异：
304	    generation-heavy tasks（GSM8K）因CoT随机性使residual膨胀，压缩item_id相对占比； classification-like
305	    tasks（MMLU, ARC）的item_id更高。这个gradient本身是有趣的发现， 可在Discussion中展开。关键是即使在"worst case"的GSM8K上，item_id仍是rank-1（48.7%
306	    > residual 21.4%）， headline claim成立。
307	
308	    '
309	- name: Multi-hardware G-study
310	  plan_id: exp-003
311	  description: '4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions
312	    (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。总记录
313	    4×2×2×6×6×3×4×200=691,200。 核心目标：量化hardware主效应和hardware×methodology交互。
314	
315	    '
316	  expected_results:
317	    total_records: 691200
318	    hardware_main_effect: 0.006
319	    hardware_x_precision: 0.002
320	    hardware_x_prompt: 0.001
321	    hardware_x_temperature: 0.001
322	    hardware_x_seed: 0.0005
323	    hardware_x_ordering: 0.0003
324	    hardware_x_item_id: 0.019
325	    precision_x_prompt: 0.0008
326	    precision_x_temperature: 0.0006
327	    precision_x_seed: 0.0003
328	    precision_x_ordering: 0.0002
329	    direct_infra_method_interaction_total: 0.005
330	    item_conditional_interactions_total: 0.142
331	    item_id: 0.561
332	    residual: 0.152
333	    prompt_x_item: 0.059
334	    temperature_x_item: 0.055
335	    seed_x_item: 0.028
336	    precision_x_item: 0.017
337	    ordering_x_item: 0.013
338	    hardware_x_item: 0.019
339	    separability_ratio: 0.035
340	    gpu1_gpu2_accuracy_correlation: 0.9987
341	    max_accuracy_difference_any_condition: 0.018
342	    mean_accuracy_difference: 0.004
343	    g_current_practice: 0.33
344	    g_full_design: 0.81
345	  result_rationale: 'Hardware主效应0.6%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel
346	    scheduling）， 但这些差异是系统性的（固定偏移），不是随机的，所以主效应很小。hardware×item交互1.9%比hardware主效应大，
347	    因为特定items（如需要长sequence generation的items）在不同GPU上因kernel tiling差异产生不同的numerical
348	    path， 但这只影响边界case items。所有direct infra×method交互加总仅0.5%，因为infrastructure层（hardware
349	    type, precision） 和methodology层（prompt, seed, temperature, ordering）作用于不同的computation
350	    stages： precision/hardware影响numerical computation，prompt/seed/temperature影响token
351	    sampling， 两者的交叉点（sampling受precision影响的程度）在logit空间中被softmax压缩到negligible水平。 Item-conditional
352	    interactions总和14.2%远大于direct interactions 0.5%，验证了Claim 2的nuanced story： separability在aggregate成立，但两层都通过item
353	    difficulty调节其效应。 GPU间accuracy correlation 0.9987说明hardware几乎不改变model ranking，只在individual
354	    item level引入微小噪声。
355	
356	    '
357	  tables:
358	  - name: 'Table 5: Separability Test — Direct vs Item-Conditional Interactions'
359	    columns:
360	    - Interaction Type
361	    - Components
362	    - Total % Variance
363	    - Interpretation
364	    rows:
365	    - - Direct Infra×Method
366	      - hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord
367	      - 0.5
368	      - Negligible — separability holds at aggregate
369	    - - Infra×Item
370	      - hw×item, prec×item
371	      - 3.6
372	      - Small but non-zero — hardware/precision effects are item-conditional
373	    - - Method×Item
374	      - prompt×item, temp×item, seed×item, ord×item
375	      - 15.5
376	      - Substantial — methodology effects are strongly item-conditional
377	    - - Item Main
378	      - item_id
379	      - 56.1
380	      - Dominant — item selection is the primary variance source
381	  - name: 'Table 6: Hardware Agreement Matrix (per-model mean accuracy)'
382	    columns:
383	    - Model
384	    - GPU1
385	    - GPU2
386	    - Difference
387	    rows:
388	    - - Qwen3-8B
389	      - 0.671
390	      - 0.668
391	      - 0.003
392	    - - Llama-3.1-8B
393	      - 0.654
394	      - 0.65
395	      - 0.004
396	    - - Gemma-2-9B-IT
397	      - 0.689
398	      - 0.684
399	      - 0.005
400	    - - Mistral-7B-v0.3
401	      - 0.638
402	      - 0.634
403	      - 0.004
404	  figures_description:
405	  - 'Fig 6: Separability diagram — 两层圆（infra layer, method layer）通过item difficulty连接，直接交互箭头用虚线（<0.5%），item-conditional箭头用实线。'
406	  - 'Fig 7: GPU1 vs GPU2 per-item accuracy scatter，近乎perfect diagonal，少数outlier items标注。'
407	  analysis: 'Separability成立：direct infra×method交互总和0.5%，远低于1%阈值。但不是trivial null result——
408	    item-conditional interactions（14.2%）提供了nuanced interpretation：infrastructure和methodology
409	    不是完全独立的，而是通过item difficulty间接耦合。这比simple "separable/not separable"更有价值， 因为它解释了为什么isolated-factor
410	    studies的结论在某些items上不泛化。 这同时支撑了Claim 2的两半："empirical license for isolated-factor
411	    studies"（direct <0.5%） 和 "conclusions are conditional on item selection"（item-conditional
412	    14.2%）。
413	
414	    '
415	- name: D-study reproducibility budget projections
416	  plan_id: exp-004
417	  description: '基于exp-001/002/003的合并variance component estimates，计算不同facet allocation下的G系数。
418	    生成practitioner-facing budget tables和projection curves。纯计算，无GPU开销。
419	
420	    '
421	  expected_results:
422	    g_1prompt_1seed_200items_mmlu: 0.34
423	    g_1prompt_1seed_200items_gsm8k: 0.29
424	    g_1prompt_1seed_200items_arc: 0.32
425	    g_1prompt_1seed_200items_hellaswag: 0.36
426	    g_1prompt_1seed_600items_mmlu: 0.71
427	    g_1prompt_1seed_1000items_mmlu: 0.82
428	    g_1prompt_1seed_2000items_mmlu: 0.9
429	    g_3prompt_1seed_200items_mmlu: 0.42
430	    g_6prompt_1seed_200items_mmlu: 0.49
431	    g_12prompt_1seed_200items_mmlu: 0.54
432	    g_1prompt_3seed_200items_mmlu: 0.36
433	    g_1prompt_6seed_200items_mmlu: 0.37
434	    optimal_g90_items: 600
435	    optimal_g90_prompts: 3
436	    optimal_g90_seeds: 2
437	    optimal_g90_total_conditions: 6
438	    optimal_g90_total_evaluations: 3600
439	    optimal_g95_items: 1200
440	    optimal_g95_prompts: 4
441	    optimal_g95_seeds: 3
442	    optimal_g95_total_conditions: 12
443	    optimal_g95_total_evaluations: 14400
444	    marginal_g_per_100_items: 0.038
445	    marginal_g_per_prompt: 0.025
446	    marginal_g_per_seed: 0.005
447	    items_vs_prompts_effectiveness_ratio: 10.2
448	    items_vs_seeds_effectiveness_ratio: 51.0
449	    gsm8k_optimal_g90_items: 800
450	    gsm8k_optimal_g90_prompts: 3
451	    gsm8k_optimal_g90_seeds: 2
452	    arc_optimal_g90_items: 650
453	    hellaswag_optimal_g90_items: 550
454	  result_rationale: 'G系数由universe score variance与observed score variance的比值决定。因为item_id占总方差>50%，
455	    增加item采样直接压缩最大的variance component，G提升最快。具体地，G ≈ σ²(τ) / [σ²(τ) + σ²(δ)/n_facets]，
456	    当item_id是σ²(δ)的主要贡献者时，增加n_items的marginal return远超增加n_prompts或n_seeds。 数值上，从200到600
457	    items（3×）使G从0.34升至0.71，而从1到3 prompts（3×）仅从0.34升至0.42。 这是因为prompt variance（含prompt×item）共计~7%，而item
458	    variance 58%。 Seed几乎无效（G从0.34到0.37 at 6 seeds），因为seed的总方差贡献<3%（主要通过seed×item）。
459	    G≥0.90需要~600 items + 3 prompts + 2 seeds = 3,600 evaluations。 当前标准practice（1 prompt,
460	    1 seed, 200 items）的G < 0.40意味着evaluation结果的reliability 低于社会科学中"不可接受"的阈值（通常G≥0.80）。
461	    GSM8K需要更多items（800 vs 600）达到G≥0.90，因为其residual更大（CoT随机性）， 需要更多items来平均掉item-level
462	    noise。
463	
464	    '
465	  tables:
466	  - name: 'Table 7: Reproducibility Budget — MMLU (Items × Prompts × Seeds → G coefficient)'
467	    columns:
468	    - Items
469	    - Prompts
470	    - Seeds
471	    - Total Evals
472	    - G coeff
473	    - Δ vs Current
474	    rows:
475	    - - 200
476	      - 1
477	      - 1
478	      - 200
479	      - 0.34
480	      - baseline
481	    - - 200
482	      - 3
483	      - 1
484	      - 600
485	      - 0.42
486	      - '+0.08'
487	    - - 200
488	      - 6
489	      - 1
490	      - 1200
491	      - 0.49
492	      - '+0.15'
493	    - - 200
494	      - 6
495	      - 6
496	      - 7200
497	      - 0.54
498	      - '+0.20'
499	    - - 600
500	      - 1
501	      - 1
502	      - 600
503	      - 0.71
504	      - '+0.37'
505	    - - 600
506	      - 3
507	      - 1
508	      - 1800
509	      - 0.82
510	      - '+0.48'
511	    - - 600
512	      - 3
513	      - 2
514	      - 3600
515	      - 0.9
516	      - '+0.56'
517	    - - 1000
518	      - 3
519	      - 2
520	      - 6000
521	      - 0.93
522	      - '+0.59'
523	    - - 1200
524	      - 4
525	      - 3
526	      - 14400
527	      - 0.95
528	      - '+0.61'
529	    - - 2000
530	      - 4
531	      - 3
532	      - 24000
533	      - 0.97
534	      - '+0.63'
535	  - name: 'Table 8: Cross-Benchmark Minimum Budget for G≥0.90'
536	    columns:
537	    - Benchmark
538	    - Items
539	    - Prompts
540	    - Seeds
541	    - Total Evals
542	    - Cost Factor vs Current
543	    rows:
544	    - - MMLU
545	      - 600
546	      - 3
547	      - 2
548	      - 3600
549	      - 18×
550	    - - GSM8K
551	      - 800
552	      - 3
553	      - 2
554	      - 4800
555	      - 24×
556	    - - ARC-Challenge
557	      - 650
558	      - 3
559	      - 2
560	      - 3900
561	      - 19.5×
562	    - - HellaSwag
563	      - 550
564	      - 3
565	      - 2
566	      - 3300
567	      - 16.5×
568	  figures_description:
569	  - 'Fig 8: D-study projection curves — G coefficient vs total evaluations，三条线分别对应
570	    scale items only / scale prompts only / scale seeds only。Items线陡峭上升，prompts线平缓，seeds线几乎flat。'
571	  - 'Fig 9: Iso-G contour plot（items × prompts平面，G值等高线），展示最优allocation路径沿items轴延伸。'
572	  - 'Fig 10: 4-benchmark overlay projection curves，展示GSM8K需要更多evaluations但pattern一致。'
573	  analysis: 'Claim 3的核心表格。Headline数字："tripling items is 10× more effective than tripling
574	    prompts" 直接来自marginal effectiveness ratio 10.2:1。当前practice G<0.40的发现具有强policy
575	    implication—— 意味着现有leaderboard结果的measurement reliability低于社会科学中最低标准。 600 items
576	    + 3 prompts + 2 seeds的"recommended minimum"在计算成本上仅为full factorial的一小部分， 是actionable的建议。跨benchmark
577	    budget差异（550-800 items for G≥0.90）提供task-specific guidance。
578	
579	    '
580	- name: 14B model extension
581	  plan_id: exp-005
582	  description: 'Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts
583	    × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。每模型 2×6×6×3×4×200=172,800记录。
584	
585	    '
586	  expected_results:
587	    qwen3_14b_accuracy: 0.728
588	    deepseek_r1_14b_accuracy: 0.714
589	    qwen3_14b_item_id: 0.574
590	    deepseek_r1_14b_item_id: 0.538
591	    qwen3_14b_residual: 0.162
592	    deepseek_r1_14b_residual: 0.198
593	    deepseek_r1_14b_temperature_x_item: 0.082
594	    scale_effect_on_item_id: within 8B model range
595	    item_id_rank1_both_models: true
596	    variance_pattern_consistent_with_8b: true
597	    precision_main_effect_14b: 0.002
598	  result_rationale: '14B模型的overall accuracy更高，但item difficulty的variance structure不会因scale改变——
599	    easy items仍然easy，hard items仍然hard。Item_id占比略低于8B平均值（~55-57% vs ~58%）， 因为14B模型在medium-difficulty
600	    items上表现更一致（ceiling effect压缩了item variance的上端）， 但差异不大。DeepSeek-R1-Distill的reasoning-distilled特性使其在CoT-heavy
601	    items上产生更多 temperature×item交互（类似GSM8K的pattern），residual也略高，因为distillation引入的implicit
602	    CoT 增加了generation-level stochasticity。关键是item_id在两个14B模型上仍为rank-1， 确认pattern不随model
603	    scale改变。precision主效应在14B上同样negligible（0.2%）， 因为confound fix的原理（统一engine path）与model
604	    size无关。
605	
606	    '
607	  tables:
608	  - name: 'Table 9: 14B vs 8B Variance Pattern Comparison'
609	    columns:
610	    - Component
611	    - 8B Mean
612	    - 8B Range
613	    - Qwen3-14B
614	    - DS-R1-14B
615	    rows:
616	    - - item_id
617	      - 58.4
618	      - 54.7–62.0
619	      - 57.4
620	      - 53.8
621	    - - residual
622	      - 16.8
623	      - 14.9–18.5
624	      - 16.2
625	      - 19.8
626	    - - temp×item
627	      - 5.8
628	      - 4.6–7.0
629	      - 5.3
630	      - 8.2
631	    - - prompt×item
632	      - 6.1
633	      - 4.7–7.5
634	      - 5.8
635	      - 5.4
636	    - - precision
637	      - 0.3
638	      - 0.1–0.5
639	      - 0.2
640	      - 0.2
641	  figures_description:
642	  - 'Fig 11: 6-model panel（4×8B + 2×14B）stacked bars，展示scale不改变variance hierarchy。'
643	  analysis: 'Scale invariance确认：item dominance不是小模型artifacts。DeepSeek-R1-Distill的slightly不同的profile
644	    （更高residual, 更高temp×item）提供了architecture effect的初步evidence， 但不改变core claim。这是P1实验，为paper增加robustness但非必需。
645	
646	    '
647	- name: Fine-tuning G-study
648	  plan_id: exp-006
649	  description: 'RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。6 seeds × 3 learning
650	    rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728
651	    total。
652	
653	    '
654	  expected_results:
655	    sst2_accuracy_mean: 0.948
656	    sst2_item_id: 0.412
657	    sst2_seed: 0.087
658	    sst2_learning_rate: 0.063
659	    sst2_data_shuffle: 0.042
660	    sst2_seed_x_item: 0.098
661	    sst2_lr_x_item: 0.074
662	    sst2_residual: 0.131
663	    sst2_gpu: 0.003
664	    sst2_precision: 0.002
665	    mnli_accuracy_mean: 0.876
666	    mnli_item_id: 0.445
667	    mnli_seed: 0.072
668	    mnli_learning_rate: 0.081
669	    mnli_data_shuffle: 0.038
670	    mnli_seed_x_item: 0.091
671	    mnli_residual: 0.142
672	    rte_accuracy_mean: 0.743
673	    rte_item_id: 0.368
674	    rte_seed: 0.124
675	    rte_learning_rate: 0.098
676	    rte_data_shuffle: 0.067
677	    rte_seed_x_item: 0.112
678	    rte_residual: 0.158
679	    copa_accuracy_mean: 0.682
680	    copa_item_id: 0.382
681	    copa_seed: 0.118
682	    copa_learning_rate: 0.091
683	    copa_residual: 0.167
684	    item_id_rank1_all_tasks: true
685	    seed_more_important_than_inference: true
686	    infra_effects_negligible: true
687	    fine_tuning_g_current_practice: 0.28
688	  result_rationale: 'Fine-tuning与inference的关键区别：training seed和learning rate成为substantial
689	    variance sources （combined 10-22%），因为它们影响optimization trajectory，不仅仅是sampling
690	    randomness。 但item_id仍然是rank-1（37-45%），因为NLU tasks的item difficulty gradient—— 从"I
691	    love this movie"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training
692	    configurations下都产生consistent accuracy variation。 RTE的item_id最低（36.8%），因为小数据集（2.5K
693	    training examples）使fine-tuning对seed更敏感， seed主效应膨胀到12.4%。这为paper提供了"inference vs
694	    fine-tuning"的对比dimension： 两者都是item-dominant，但fine-tuning中training hyperparameters（seed,
695	    LR）取代了 inference中的generation parameters（temperature, prompt）成为第二梯队的variance sources。
696	    GPU和precision主效应在fine-tuning中同样negligible（<0.5%），因为RoBERTa-large 对numerical precision不敏感（unlike
697	    large generative models的autoregressive error accumulation）。
698	
699	    '
700	  tables:
701	  - name: 'Table 10: Fine-tuning vs Inference Variance Hierarchy'
702	    columns:
703	    - Rank
704	    - Inference (MMLU)
705	    - Fine-tuning (SST-2)
706	    rows:
707	    - - 1
708	      - item_id (58.4%)
709	      - item_id (41.2%)
710	    - - 2
711	      - residual (16.8%)
712	      - residual (13.1%)
713	    - - 3
714	      - prompt×item (6.1%)
715	      - seed×item (9.8%)
716	    - - 4
717	      - temp×item (5.8%)
718	      - seed (8.7%)
719	    - - 5
720	      - seed×item (2.9%)
721	      - lr×item (7.4%)
722	    - - 6
723	      - precision×item (1.8%)
724	      - lr (6.3%)
725	  figures_description:
726	  - 'Fig 12: Inference vs Fine-tuning stacked bars并排，展示item_id在两个paradigm中均为rank-1但fine-tuning中seed/LR更prominent。'
727	  - 'Fig 13: 4-task fine-tuning panel，展示dataset size对variance structure的调节效应（RTE seed最大）。'
728	  analysis: 'Fine-tuning G-study将paper从"inference evaluation reproducibility"扩展到"ML
729	    reproducibility broadly"。 核心takeaway：item dominance是跨paradigm的（inference和fine-tuning），但second-tier
730	    factors不同。 这是P1实验，为paper增加generality但AAAI投稿时可作为supplementary。
731	
732	    '
733	- name: LayerCast precision study
734	  plan_id: exp-007
735	  description: '在MMLU上测试LayerCast（FP16 storage + FP32 compute）作为额外precision condition。
736	    4 models × 1 precision mode × 6 prompts × 6 seeds × 3 temperatures × 4 orderings
737	    × 200 items = 172,800记录。
738	
739	    '
740	  expected_results:
741	    layercast_accuracy_mean: 0.67
742	    layercast_vs_fp32_accuracy_diff: 0.004
743	    layercast_vs_bf16_accuracy_diff: -0.001
744	    layercast_item_agreement_with_fp32: 0.9991
745	    layercast_item_agreement_with_bf16: 0.9994
746	    layercast_added_variance_to_precision: 0.0004
747	    layercast_throughput_vs_fp32: 1.38
748	    layercast_throughput_vs_bf16: 0.91
749	    layercast_precision_x_item_contribution: 0.009
750	  result_rationale: 'LayerCast在存储时用FP16减少memory footprint，在compute时cast to FP32， 因此其numerical
751	    behavior几乎等同于纯FP32（computation path一致）， accuracy差异仅来自storage时的precision loss（FP16
752	    mantissa 10 bits vs FP32 23 bits）， 这对大部分weights来说negligible（在训练时weights就是从FP16/BF16来的）。
753	    与BF16的差异更小（0.1pp），因为BF16的dynamic range与FP32一致（8-bit exponent）， 而FP16的range更窄但mantissa更宽，两者accuracy接近。
754	    LayerCast对precision variance几乎没有增量贡献（0.04%），因为它本质上是FP32 compute的cheaper variant。
755	    Throughput方面，LayerCast比FP32快38%（memory bandwidth节省），比BF16慢9%（需要cast操作）。 这个实验为paper提供了一个"practical
756	    mitigation"故事：如果practitioner担心precision影响， LayerCast以minimal overhead提供FP32-level
757	    behavior。
758	
759	    '
760	  tables:
761	  - name: 'Table 11: Precision Mode Comparison'
762	    columns:
763	    - Mode
764	    - Accuracy
765	    - item Agreement w/ FP32
766	    - Throughput (tokens/s)
767	    - VRAM (GB)
768	    rows:
769	    - - FP32
770	      - 0.666
771	      - 1.0
772	      - 1820
773	      - 31.2
774	    - - BF16
775	      - 0.671
776	      - 0.9985
777	      - 2760
778	      - 15.8
779	    - - FP16
780	      - 0.669
781	      - 0.9982
782	      - 2810
783	      - 15.6
784	    - - LayerCast
785	      - 0.67
786	      - 0.9991
787	      - 2510
788	      - 16.1
789	  figures_description:
790	  - 'Fig 14: 4-precision mode accuracy distribution violin plots，展示LayerCast与FP32几乎identical
791	    spread。'
792	  analysis: 'P2实验。LayerCast结果进一步support precision不是major concern（在engine confound
793	    fix后）。 可作为paper中"practical recommendation"段落的一条：对于追求最高reproducibility的场景， LayerCast提供了memory-efficient的FP32-equivalent选项。
794	
795	    '
796	- name: MATH benchmark extension
797	  plan_id: exp-008
798	  description: '4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures
799	    × 4 orderings × 200 MATH items。 总记录 4×2×6×6×2×4×200=230,400。测试reasoning-heavy
800	    task的variance structure。
801	
802	    '
803	  expected_results:
804	    math_overall_accuracy: 0.342
805	    math_item_id: 0.421
806	    math_residual: 0.248
807	    math_temperature_x_item: 0.104
808	    math_prompt_x_item: 0.068
809	    math_seed_x_item: 0.052
810	    math_temperature: 0.038
811	    math_prompt: 0.021
812	    math_precision: 0.002
813	    math_precision_x_item: 0.008
814	    math_ordering_x_item: 0.015
815	    math_g_current_practice: 0.24
816	    math_item_id_rank1: true
817	    math_optimal_g90_items: 1100
818	    math_optimal_g90_prompts: 4
819	    math_optimal_g90_seeds: 3
820	  result_rationale: 'MATH是所有benchmark中最challenging的（accuracy ~34%），其item difficulty分布极端——
821	    从Level 1（algebra basics）到Level 5（competition math），跨越巨大的difficulty range。 Item_id仍为rank-1（42.1%）但低于MMLU，因为：(1)
822	    lower overall accuracy增加了random guessing的比例， 膨胀residual到24.8%；(2) MATH的CoT generation比GSM8K更长更复杂（多步proof-like
823	    reasoning）， 使temperature×item interaction达到10.4%——在高temperature下，长推理链的任何一步都可能diverge，
824	    且这种sensitivity是item-specific的（Level 5 problems的长推理链比Level 1的短计算更sensitive）。 Temperature主效应也最高（3.8%），因为MATH的generation
825	    length使sampling temperature的cumulative effect更显著。 G current practice仅0.24——所有benchmark中最低——意味着MATH
826	    evaluation的reproducibility最差。 达到G≥0.90需要1100 items + 4 prompts + 3 seeds，是MMLU所需的~3倍evaluation
827	    budget。 这个发现有strong policy implication：reasoning benchmark的evaluation标准需要比classification
828	    benchmark更严格。
829	
830	    '
831	  tables:
832	  - name: 'Table 12: Full Cross-Benchmark Variance Summary (5 benchmarks)'
833	    columns:
834	    - Benchmark
835	    - Accuracy
836	    - item_id %
837	    - Residual %
838	    - Temp×Item %
839	    - G (current)
840	    - Items for G≥0.90
841	    rows:
842	    - - MMLU
843	      - 0.668
844	      - 58.4
845	      - 16.8
846	      - 5.8
847	      - 0.34
848	      - 600
849	    - - ARC-Challenge
850	      - 0.597
851	      - 55.1
852	      - 18.2
853	      - 5.4
854	      - 0.32
855	      - 650
856	    - - HellaSwag
857	      - 0.712
858	      - 52.7
859	      - 19.5
860	      - 6.2
861	      - 0.36
862	      - 550
863	    - - GSM8K
864	      - 0.583
865	      - 48.7
866	      - 21.4
867	      - 8.9
868	      - 0.29
869	      - 800
870	    - - MATH
871	      - 0.342
872	      - 42.1
873	      - 24.8
874	      - 10.4
875	      - 0.24
876	      - 1100
877	  figures_description:
878	  - 'Fig 15: 5-benchmark stacked bars排序by task difficulty，展示清晰的gradient：task越难→item_id越低、residual和temp×item越高。'
879	  - 'Fig 16: D-study projection curves for 5 benchmarks overlay，MATH曲线最右（需最多evaluations达G≥0.90）。'
880	  analysis: MATH提供了variance structure的"stress test"。Item_id在最extreme条件下仍为rank-1（42.1%），
881	    但task difficulty明显调节了variance decomposition的profile。5个benchmark展现了清晰的gradient：
882	    task difficulty ↑ → item_id share ↓, residual ↑, temperature×item ↑, G current
883	    practice ↓。 这个gradient本身是publishable finding：它量化了为什么reasoning benchmark的evaluation更不稳定，
884	    并给出了task-specific的reproducibility budget。
885	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed512405-973c-4520-bdb5-17b55f63fcce",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "34f6ac28-3137-4757-851c-890dd3d0cd21",
  "sourceToolAssistantUUID": "ed512405-973c-4520-bdb5-17b55f63fcce",
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

_source line 35 · 2026-05-20T19:39:13.199Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VmNeC1GchtFzQuossjK3br`</summary>

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
  "parentUuid": "34f6ac28-3137-4757-851c-890dd3d0cd21",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPQg8htq9oTUEM8x6d3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0b93724-9b0d-4f12-8acf-a333d96e5c2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxfUXjuqc5bQo2erNndXLJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 37319,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 37319,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 506,
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

_source line 36 · 2026-05-20T19:39:13.487Z_

<details><summary>↩ Tool result · `toolu_01VmNeC1GchtFzQuossjK3br`</summary>

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
  "parentUuid": "a0b93724-9b0d-4f12-8acf-a333d96e5c2a",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "4dcf7c98-5ce1-4c57-b5d5-f7ce826cfd80",
  "sourceToolAssistantUUID": "a0b93724-9b0d-4f12-8acf-a333d96e5c2a",
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

_source line 37 · 2026-05-20T19:39:16.757Z_

Now let me check the analysis code and the distilled research skill to understand methodology context better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dcf7c98-5ce1-4c57-b5d5-f7ce826cfd80",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPQydvJbEhyWaRS3FLN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fa8f6bc-60b1-4a99-978a-5ebd2364ee55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2BBe5SGVzhKrdn8TGDPyg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28387,
      "cache_read_input_tokens": 37825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28387,
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

_source line 38 · 2026-05-20T19:39:18.264Z_

<details open><summary>🔧 Tool call — Read · `toolu_015uRCH43yavQKofwWkbFRJy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/variance_decomposition.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fa8f6bc-60b1-4a99-978a-5ebd2364ee55",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPQydvJbEhyWaRS3FLN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a10451a-4227-4440-91ae-b1abcc7fc03b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2BBe5SGVzhKrdn8TGDPyg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28387,
      "cache_read_input_tokens": 37825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28387,
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

_source line 39 · 2026-05-20T19:39:18.269Z_

<details><summary>↩ Tool result · `toolu_015uRCH43yavQKofwWkbFRJy`</summary>

```text
1	"""G-theory variance decomposition for LLM evaluation.
2	
3	Estimates variance components for all 6 facets (main effects) and all
4	15 two-way interactions using ANOVA-based estimation (Henderson Method I)
5	for balanced fully-crossed designs.  Higher-order interactions (≥3-way) are
6	absorbed into the residual.
7	
8	Estimation treats all facets as random (standard G-study practice).  The
9	fixed/random distinction is used downstream in the D-study to partition
10	universe-score variance from error variance.
11	
12	Bootstrap 95 %% CIs are computed by resampling items with replacement.
13	
14	Facets
15	------
16	precision, temperature                    — fixed  (in D-study)
17	prompt_template, seed, ordering, item_id  — random (in D-study)
18	
19	Input:  JSONL from ``run_experiment.py`` (one row per item × condition).
20	Output: JSON with ANOVA table, variance components, and bootstrap CIs.
21	"""
22	
23	import argparse
24	import json
25	from itertools import combinations
26	from math import prod
27	from pathlib import Path
28	from collections import Counter
29	from typing import Optional
30	
31	import numpy as np
32	import pandas as pd
33	
34	ALL_FACETS = [
35	    "precision", "temperature",
36	    "prompt_template", "seed", "ordering", "item_id",
37	]
38	FIXED_FACETS = ["precision", "temperature"]
39	RANDOM_FACETS = ["prompt_template", "seed", "ordering", "item_id"]
40	
41	
42	# ---------------------------------------------------------------------------
43	# ANOVA helpers
44	# ---------------------------------------------------------------------------
45	
46	def compute_ss(
47	    df: pd.DataFrame,
48	    response: str,
49	    facets: list[str],
50	) -> tuple[dict, dict[str, int]]:
51	    """Compute Type-I sums of squares for main effects and 2-way interactions.
52	
53	    For a balanced design, Type I = Type III, so the order of terms does not
54	    matter.
55	
56	    Returns:
57	        (effects_dict, n_levels_dict) where each effect entry has keys
58	        ``ss``, ``df``, ``ms``.
59	    """
60	    grand_mean = df[response].mean()
61	    N = len(df)
62	    n_levels = {f: df[f].nunique() for f in facets}
63	
64	    effects: dict = {}
65	
66	    # --- main effects ---
67	    for f in facets:
68	        group_means = df.groupby(f, observed=True)[response].mean()
69	        n_per_group = N // n_levels[f]
70	        ss = float(n_per_group * ((group_means - grand_mean) ** 2).sum())
71	        df_eff = n_levels[f] - 1
72	        effects[f] = {
73	            "ss": ss,
74	            "df": df_eff,
75	            "ms": ss / df_eff if df_eff > 0 else 0.0,
76	        }
77	
78	    # --- 2-way interactions ---
79	    for fi, fj in combinations(facets, 2):
80	        cell_means = df.groupby([fi, fj], observed=True)[response].mean()
81	        main_fi = df.groupby(fi, observed=True)[response].mean()
82	        main_fj = df.groupby(fj, observed=True)[response].mean()
83	        n_per_cell = N // (n_levels[fi] * n_levels[fj])
84	
85	        ss = 0.0
86	        for (li, lj), cell_mean in cell_means.items():
87	            interaction = cell_mean - main_fi[li] - main_fj[lj] + grand_mean
88	            ss += n_per_cell * interaction ** 2
89	
90	        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
91	        key = f"{fi}:{fj}"
92	        effects[key] = {
93	            "ss": ss,
94	            "df": df_eff,
95	            "ms": ss / df_eff if df_eff > 0 else 0.0,
96	        }
97	
98	    # --- residual (confounds ≥3-way interactions) ---
99	    ss_total = float(((df[response] - grand_mean) ** 2).sum())
100	    ss_model = sum(e["ss"] for e in effects.values())
101	    ss_res = max(0.0, ss_total - ss_model)
102	    df_res = N - 1 - sum(e["df"] for e in effects.values())
103	    effects["residual"] = {
104	        "ss": ss_res,
105	        "df": df_res,
106	        "ms": ss_res / df_res if df_res > 0 else 0.0,
107	    }
108	
109	    return effects, n_levels
110	
111	
112	def estimate_variance_components(
113	    effects: dict,
114	    facets: list[str],
115	    n_levels: dict[str, int],
116	) -> dict[str, float]:
117	    """Solve EMS equations for variance components.
118	
119	    For a balanced crossed design with all-random facets and effects up to
120	    2-way interactions:
121	
122	    * 2-way σ²_{ij} = (MS_{ij} − MS_res) / ∏_{k∉{i,j}} n_k
123	    * main  σ²_i    = (MS_i − ∑_j c_{ij} σ²_{ij} − MS_res) / ∏_{k≠i} n_k
124	
125	    Negative estimates are truncated to zero.
126	    """
127	    ms_res = effects["residual"]["ms"]
128	    vc: dict[str, float] = {}
129	
130	    # --- 2-way interactions first ---
131	    for fi, fj in combinations(facets, 2):
132	        key = f"{fi}:{fj}"
133	        coeff = prod(n_levels[f] for f in facets if f not in (fi, fj))
134	        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
135	        vc[key] = max(0.0, raw)
136	
137	    # --- main effects (require 2-way estimates) ---
138	    for fi in facets:
139	        coeff_main = prod(n_levels[f] for f in facets if f != fi)
140	        interaction_contrib = 0.0
141	        for fj in facets:
142	            if fj == fi:
143	                continue
144	            int_key = (
145	                f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
146	            )
147	            coeff_ij = prod(
148	                n_levels[f] for f in facets if f not in (fi, fj)
149	            )
150	            interaction_contrib += coeff_ij * vc[int_key]
151	
152	        raw = (
153	            (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main
154	            if coeff_main > 0
155	            else 0.0
156	        )
157	        vc[fi] = max(0.0, raw)
158	
159	    vc["residual"] = ms_res
160	    return vc
161	
162	
163	# ---------------------------------------------------------------------------
164	# Bootstrap
165	# ---------------------------------------------------------------------------
166	
167	def bootstrap_ci(
168	    df: pd.DataFrame,
169	    response: str,
170	    facets: list[str],
171	    n_bootstrap: int = 1000,
172	    alpha: float = 0.05,
173	    seed: int = 42,
174	) -> dict[str, dict[str, float]]:
175	    """Bootstrap 95 % CIs for variance components by resampling items.
176	
177	    Each bootstrap sample draws 50 items with replacement, assigns unique
178	    item IDs, re-runs the full ANOVA, and records variance components.
179	    """
180	    rng = np.random.RandomState(seed)
181	    items = df["item_id"].unique()
182	    n_items = len(items)
183	
184	    boot_vcs: list[dict[str, float]] = []
185	    for _ in range(n_bootstrap):
186	        sampled = rng.choice(items, size=n_items, replace=True)
187	        frames = []
188	        for new_idx, item in enumerate(sampled):
189	            sub = df[df["item_id"] == item].copy()
190	            sub["item_id"] = f"boot_{new_idx}"
191	            frames.append(sub)
192	        boot_df = pd.concat(frames, ignore_index=True)
193	
194	        eff, nl = compute_ss(boot_df, response, facets)
195	        vc = estimate_variance_components(eff, facets, nl)
196	        boot_vcs.append(vc)
197	
198	    ci: dict[str, dict[str, float]] = {}
199	    for key in boot_vcs[0]:
200	        values = [bv[key] for bv in boot_vcs]
201	        ci[key] = {
202	            "lower": float(np.percentile(values, 100 * alpha / 2)),
203	            "upper": float(np.percentile(values, 100 * (1 - alpha / 2))),
204	        }
205	    return ci
206	
207	
208	# ---------------------------------------------------------------------------
209	# Text exact match
210	# ---------------------------------------------------------------------------
211	
212	def compute_text_exact_match(df: pd.DataFrame) -> pd.DataFrame:
213	    """Add ``text_exact_match`` column (0/1) to *df*.
214	
215	    For each item_id the canonical text is the most frequent generated_text
216	    across all conditions.  A record scores 1 iff its generated_text equals
217	    the canonical text for that item.
218	    """
219	    canonical = (
220	        df.groupby("item_id")["generated_text"]
221	        .agg(lambda texts: Counter(texts).most_common(1)[0][0])
222	    )
223	    df = df.copy()
224	    df["text_exact_match"] = (
225	        df.apply(lambda r: int(r["generated_text"] == canonical[r["item_id"]]), axis=1)
226	    )
227	    return df
228	
229	
230	# ---------------------------------------------------------------------------
231	# Public entry point
232	# ---------------------------------------------------------------------------
233	
234	def run_analysis(
235	    input_path: str,
236	    output_path: str,
237	    n_bootstrap: int = 1000,
238	    response_var: str = "correct",
239	) -> dict:
240	    """Full G-theory analysis: ANOVA → variance components → bootstrap CIs.
241	
242	    Args:
243	        input_path: JSONL from ``run_experiment.py``.
244	        output_path: Destination JSON.
245	        n_bootstrap: Number of bootstrap iterations (default 1000).
246	        response_var: Response variable — ``"correct"`` or ``"text_exact_match"``.
247	
248	    Returns:
249	        Results dict (also written to ``output_path``).
250	    """
251	    df = pd.read_json(input_path, lines=True)
252	
253	    for f in ALL_FACETS:
254	        df[f] = df[f].astype(str)
255	
256	    if response_var == "text_exact_match":
257	        df = compute_text_exact_match(df)
258	
259	    print(f"Running G-study on {len(df)} observations (response={response_var}) …")
260	
261	    effects, n_levels = compute_ss(df, response_var, ALL_FACETS)
262	    vc = estimate_variance_components(effects, ALL_FACETS, n_levels)
263	
264	    print(f"Bootstrapping ({n_bootstrap} iterations) …")
265	    ci = bootstrap_ci(df, response_var, ALL_FACETS, n_bootstrap=n_bootstrap)
266	
267	    total_var = sum(vc.values())
268	    results = {
269	        "variance_components": {
270	            k: {
271	                "estimate": v,
272	                "pct": v / total_var * 100 if total_var > 0 else 0.0,
273	                "ci_95": ci[k],
274	            }
275	            for k, v in vc.items()
276	        },
277	        "total_variance": total_var,
278	        "n_observations": len(df),
279	        "n_levels": {k: int(v) for k, v in n_levels.items()},
280	        "fixed_facets": FIXED_FACETS,
281	        "random_facets": RANDOM_FACETS,
282	        "anova_table": {
283	            k: {"ss": v["ss"], "df": v["df"], "ms": v["ms"]}
284	            for k, v in effects.items()
285	        },
286	    }
287	
288	    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
289	    with open(output_path, "w") as f:
290	        json.dump(results, f, indent=2)
291	
292	    # --- print summary ---
293	    print(
294	        f"\nG-theory Variance Decomposition  "
295	        f"({len(df)} obs, {len(ALL_FACETS)} facets)"
296	    )
297	    header = f"{'Component':<30} {'Estimate':>10} {'%':>8}  {'95% CI':>24}"
298	    print(header)
299	    print("-" * len(header))
300	    for name, info in sorted(
301	        results["variance_components"].items(),
302	        key=lambda x: -x[1]["estimate"],
303	    ):
304	        lo, hi = info["ci_95"]["lower"], info["ci_95"]["upper"]
305	        print(
306	            f"{name:<30} {info['estimate']:>10.6f} {info['pct']:>7.1f}%  "
307	            f"[{lo:.6f}, {hi:.6f}]"
308	        )
309	
310	    print(f"\n→ {output_path}")
311	    return results
312	
313	
314	if __name__ == "__main__":
315	    parser = argparse.ArgumentParser(
316	        description="G-theory variance decomposition"
317	    )
318	    parser.add_argument(
319	        "--input", required=True, help="Path to experiment results JSONL"
320	    )
321	    parser.add_argument("--output", default=None)
322	    parser.add_argument("--n-bootstrap", type=int, default=1000)
323	    parser.add_argument(
324	        "--response-var",
325	        default="correct",
326	        choices=["correct", "text_exact_match"],
327	        help="Response variable: 'correct' (binary accuracy) or 'text_exact_match' (text-level determinism)",
328	    )
329	    args = parser.parse_args()
330	
331	    if args.output is None:
332	        if args.response_var == "text_exact_match":
333	            args.output = "results/variance_components_text.json"
334	        else:
335	            args.output = "results/variance_components.json"
336	
337	    run_analysis(args.input, args.output, args.n_bootstrap, args.response_var)
338	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a10451a-4227-4440-91ae-b1abcc7fc03b",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "6eb61c8d-b611-4fe4-8114-fb790ca44194",
  "sourceToolAssistantUUID": "2a10451a-4227-4440-91ae-b1abcc7fc03b",
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

_source line 40 · 2026-05-20T19:39:18.838Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L73SNx7Gr1gNCbXNPJUf8y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/d_study.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eb61c8d-b611-4fe4-8114-fb790ca44194",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPQydvJbEhyWaRS3FLN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98805fac-7889-4494-ae62-7b8c160162c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2BBe5SGVzhKrdn8TGDPyg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28387,
      "cache_read_input_tokens": 37825,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28387
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 37825,
          "cache_creation_input_tokens": 28387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28387,
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

_source line 41 · 2026-05-20T19:39:18.842Z_

<details><summary>↩ Tool result · `toolu_01L73SNx7Gr1gNCbXNPJUf8y`</summary>

```text
1	"""D-study projections for G-theory variance decomposition.
2	
3	Given the estimated variance components from the G-study, computes the
4	generalizability coefficient (G) for different measurement designs by
5	varying the number of replications of each random facet.
6	
7	Partition rule
8	--------------
9	* σ²_τ  (universe score): components involving *only* fixed facets
10	  (precision, temperature and their interactions).
11	* σ²_δ  (relative error): components involving ≥1 random facet, each
12	  divided by the product of the sample sizes of the random facets in
13	  that component.
14	* G = σ²_τ / (σ²_τ + σ²_δ)
15	
16	Input:  ``variance_components.json`` from ``variance_decomposition.py``.
17	Output: ``d_study_results.json`` — current G, per-facet sweep, minimum
18	        replications for target G thresholds.
19	"""
20	
21	import argparse
22	import json
23	from pathlib import Path
24	
25	FIXED_FACETS = {"precision", "temperature"}
26	RANDOM_FACETS = ["prompt_template", "seed", "ordering", "item_id"]
27	
28	MVP_LEVELS = {
29	    "prompt_template": 3,
30	    "seed": 3,
31	    "ordering": 2,
32	    "item_id": 50,
33	}
34	
35	
36	def compute_g_coefficient(
37	    variance_components: dict,
38	    random_n: dict[str, int],
39	) -> tuple[float, float, float]:
40	    """Compute G for a given D-study design.
41	
42	    Args:
43	        variance_components: Keys are component names (e.g. ``"seed"``,
44	            ``"precision:prompt_template"``), values are dicts with an
45	            ``"estimate"`` key **or** plain floats.
46	        random_n: Number of replications for each random facet.
47	
48	    Returns:
49	        (G, σ²_τ, σ²_δ).
50	    """
51	    sigma_tau = 0.0
52	    sigma_delta = 0.0
53	
54	    for component, info in variance_components.items():
55	        est = info["estimate"] if isinstance(info, dict) else info
56	
57	        if component == "residual":
58	            divisor = 1
59	            for f in RANDOM_FACETS:
60	                divisor *= random_n.get(f, 1)
61	            sigma_delta += est / divisor
62	            continue
63	
64	        facets_in = component.split(":")
65	        random_in = [f for f in facets_in if f not in FIXED_FACETS]
66	
67	        if len(random_in) == 0:
68	            sigma_tau += est
69	        else:
70	            divisor = 1
71	            for f in random_in:
72	                divisor *= random_n.get(f, 1)
73	            sigma_delta += est / divisor
74	
75	    total = sigma_tau + sigma_delta
76	    g = sigma_tau / total if total > 0 else 0.0
77	    return g, sigma_tau, sigma_delta
78	
79	
80	def find_min_replications(
81	    vc: dict,
82	    target_g: float,
83	    target_facet: str,
84	    base_levels: dict[str, int],
85	    max_n: int = 100,
86	) -> int | None:
87	    """Binary-search the minimum *n* for ``target_facet`` to reach ``target_g``.
88	
89	    Other facets stay at ``base_levels``.  Returns ``None`` if not reachable
90	    within ``max_n``.
91	    """
92	    for n in range(1, max_n + 1):
93	        levels = base_levels.copy()
94	        levels[target_facet] = n
95	        g, _, _ = compute_g_coefficient(vc, levels)
96	        if g >= target_g:
97	            return n
98	    return None
99	
100	
101	def run_d_study(input_path: str, output_path: str) -> dict:
102	    """Run full D-study analysis.
103	
104	    Args:
105	        input_path: Path to ``variance_components.json``.
106	        output_path: Destination JSON.
107	
108	    Returns:
109	        Results dict.
110	    """
111	    with open(input_path) as f:
112	        data = json.load(f)
113	
114	    vc = data["variance_components"]
115	
116	    g_current, tau, delta = compute_g_coefficient(vc, MVP_LEVELS)
117	
118	    # --- per-facet sweeps (1 … 20) ---
119	    sweeps: dict[str, list[dict]] = {}
120	    for facet in RANDOM_FACETS:
121	        sweep = []
122	        for n in range(1, 21):
123	            levels = MVP_LEVELS.copy()
124	            levels[facet] = n
125	            g, _, _ = compute_g_coefficient(vc, levels)
126	            sweep.append({"n": n, "g": round(g, 6)})
127	        sweeps[facet] = sweep
128	
129	    # --- minimum replications for target thresholds ---
130	    targets = [0.90, 0.95, 0.99]
131	    min_reps: dict[str, dict[str, int | None]] = {}
132	    for target in targets:
133	        min_reps[str(target)] = {}
134	        for facet in RANDOM_FACETS:
135	            min_reps[str(target)][facet] = find_min_replications(
136	                vc, target, facet, MVP_LEVELS
137	            )
138	
139	    results = {
140	        "current_design": {
141	            "levels": MVP_LEVELS,
142	            "g_coefficient": round(g_current, 6),
143	            "sigma_tau": round(tau, 8),
144	            "sigma_delta": round(delta, 8),
145	        },
146	        "sweeps": sweeps,
147	        "min_replications": min_reps,
148	    }
149	
150	    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
151	    with open(output_path, "w") as f:
152	        json.dump(results, f, indent=2)
153	
154	    # --- print summary ---
155	    print(f"D-study Results  (current G = {g_current:.4f})")
156	    print(f"\nMinimum replications for target G:")
157	    print(f"{'Facet':<20} {'G≥0.90':>8} {'G≥0.95':>8} {'G≥0.99':>8}")
158	    print("-" * 48)
159	    for facet in RANDOM_FACETS:
160	        vals = [min_reps[str(t)].get(facet) for t in targets]
161	        strs = [str(v) if v is not None else ">100" for v in vals]
162	        print(f"{facet:<20} {strs[0]:>8} {strs[1]:>8} {strs[2]:>8}")
163	
164	    print(f"\n→ {output_path}")
165	    return results
166	
167	
168	if __name__ == "__main__":
169	    parser = argparse.ArgumentParser(
170	        description="G-theory D-study projections"
171	    )
172	    parser.add_argument(
173	        "--input", required=True, help="Path to variance_components.json"
174	    )
175	    parser.add_argument("--output", default="results/d_study_results.json")
176	    args = parser.parse_args()
177	    run_d_study(args.input, args.output)
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98805fac-7889-4494-ae62-7b8c160162c1",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "6655d5bb-b7e9-4467-8d18-8f0f82ed81da",
  "sourceToolAssistantUUID": "98805fac-7889-4494-ae62-7b8c160162c1",
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

_source line 42 · 2026-05-20T19:39:21.703Z_

Now let me check the paper summary numbers against what's in the dream report, and read the distilled research skill for methodological context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6655d5bb-b7e9-4467-8d18-8f0f82ed81da",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPRNdH1oX2hrF3qShFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72119b08-badb-4b34-9af7-6bf494d528c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4paHqQBwBK7efDwexTbvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6822,
      "cache_read_input_tokens": 66212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6822,
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

_source line 43 · 2026-05-20T19:39:23.851Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JrLG4mXBK83BujNZXxaQQc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72119b08-badb-4b34-9af7-6bf494d528c9",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPRNdH1oX2hrF3qShFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c638981-083c-48ff-b30a-3936ba439613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4paHqQBwBK7efDwexTbvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6822,
      "cache_read_input_tokens": 66212,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6822
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 66212,
          "cache_creation_input_tokens": 6822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6822,
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

_source line 44 · 2026-05-20T19:39:23.868Z_

<details><summary>↩ Tool result · `toolu_01JrLG4mXBK83BujNZXxaQQc`</summary>

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
  "parentUuid": "0c638981-083c-48ff-b30a-3936ba439613",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "b5878d20-e699-4fdb-a93a-ea34863e3cac",
  "sourceToolAssistantUUID": "0c638981-083c-48ff-b30a-3936ba439613",
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

_source line 45 · 2026-05-20T19:39:27.507Z_

Now I have a thorough understanding of the paper, the underlying code, the experimental plan, the dream-simulated results, and the related work context. Let me now write the formal review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5878d20-e699-4fdb-a93a-ea34863e3cac",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPRk7bawcTJPzj1Swbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a99ffc61-de94-4f45-b85a-f255bc5b6924",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DiAVzHweuHg42FwfWQUJH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1080,
      "cache_read_input_tokens": 73034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1080,
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

_source line 46 · 2026-05-20T19:39:28.342Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ly26k6g9RK6xuCcLJ51ChZ`</summary>

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
  "parentUuid": "a99ffc61-de94-4f45-b85a-f255bc5b6924",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPRk7bawcTJPzj1Swbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4790ac0e-f657-4047-af26-187a66cbf853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DiAVzHweuHg42FwfWQUJH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1080,
      "cache_read_input_tokens": 73034,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1080
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 73034,
          "cache_creation_input_tokens": 1080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1080,
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

_source line 47 · 2026-05-20T19:39:28.344Z_

<details><summary>↩ Tool result · `toolu_01Ly26k6g9RK6xuCcLJ51ChZ`</summary>

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
  "parentUuid": "4790ac0e-f657-4047-af26-187a66cbf853",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "349ec621-6faf-45f2-b6ec-384a6a831aa4",
  "sourceToolAssistantUUID": "4790ac0e-f657-4047-af26-187a66cbf853",
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

_source line 48 · 2026-05-20T19:39:31.113Z_



Now I have all the information needed. Let me compile my thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "349ec621-6faf-45f2-b6ec-384a6a831aa4",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPS5K1FPH3w6HxZZUqp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d791cb4a-880c-460c-9412-d3102d36c978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNwG2GALpMGWAVoy1YEhMS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 74114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 754,
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

_source line 49 · 2026-05-20T19:41:03.076Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01C6nhefC7jffGb4pAAJQR9A`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "tier": "best",
  "dream_id": "dream_20260520T190053",
  "overall_score": "borderline accept",
  "report": "\n# Reviewer R1: Methodology and Experimental Rigor\n\n## Summary\n\nThis paper applies Generalizability Theory (G-theory) to decompose variance in LLM evaluation across infrastructure (hardware, precision), methodology (prompt, seed, temperature, ordering), and measurement (item) facets. Across 6 models, 5 benchmarks, and 2M+ evaluation records, the authors find that item selection dominates variance (42--58%), direct infrastructure x methodology interactions are negligible (<0.5%), and current evaluation practices yield unacceptably low generalizability coefficients (G < 0.40). D-study projections provide actionable reproducibility budgets showing item count increases are far more cost-effective than prompt or seed replication. The paper is ambitious in scope and the cross-domain transfer of G-theory to LLM evaluation is well-motivated, but several methodological concerns---particularly around the treatment of \"model\" in the G-theory framework, the interpretation of item variance, and incomplete uncertainty quantification---temper my enthusiasm.\n\n## Strengths\n\n- **Timely and well-motivated problem.** The paper addresses a genuine gap: no prior work crosses infrastructure and methodology layers in a single G-theory framework. The positioning relative to Mesting (2026), Yuan et al. (2025), and Brittlebench (2026) is accurate and clearly articulated.\n\n- **Impressive experimental scale.** 8 experiments, 2M+ records, 6 models, 5 benchmarks, and extension to fine-tuning. The breadth of coverage strengthens the generality claims substantially. All 8 planned experiments are present.\n\n- **Engine confound identification is a genuine methodological contribution.** The discovery that vLLM routes FP32 through a different compute path than BF16/FP16, inflating precision variance from 0.87% to 7.24% (interaction), is a valuable finding of independent interest. The before/after comparison is convincing.\n\n- **Actionable D-study budgets.** The reproducibility budget tables translate abstract variance component estimates into concrete design recommendations. The cross-benchmark budget table (Table 8 / Table 13-15 in the summary) showing task-specific item requirements is practically useful.\n\n- **Good confound control.** Uniform vLLM V0 + enforce_eager across all precision modes, generation-based evaluation following Hua et al. (2025) to avoid log-likelihood artifacts, and stratified item sampling all reflect careful experimental design.\n\n- **Fine-tuning extension adds generality.** Showing that item dominance holds in fine-tuning (36.8--44.5%) with seed/LR replacing prompt/temperature as secondary factors is a non-trivial extension.\n\n- **Clear task-difficulty gradient.** The systematic pattern across 5 benchmarks (item_id share decreasing, residual and temp x item increasing with difficulty) is a well-supported finding that provides theoretical insight.\n\n## Weaknesses\n\n### Major\n\n- **(W1) Model is pooled rather than treated as a facet---this fundamentally distorts the variance decomposition.** The paper pools 4 models and decomposes variance across the pooled data, but \"model\" is not included as a facet in the G-study. In standard G-theory, the object of measurement (here, presumably each model's ability) should be the differentiation facet. By pooling across models without including model as a facet, model-level variance is absorbed into item_id (since different models have different difficulty profiles on the same items) and into the residual. This means the 58.4% attributed to item_id is confounded with model x item interaction---the very thing G-theory is designed to separate. The per-model analyses (Table 2) partially address this, but the headline numbers and the D-study projections are based on the pooled analysis. This is a fundamental design choice that needs explicit justification. If the goal is to assess reliability of a *single model's* evaluation, the per-model G-studies should be primary. If the goal is reliability of *cross-model comparisons*, model must be a facet. The paper's framing suggests both goals but delivers neither cleanly.\n\n- **(W2) The 0.5% separability threshold is arbitrary and self-serving.** The paper defines separability as \"direct infrastructure x methodology interactions contribute less than 0.5% of total variance\" and then finds exactly 0.5%. This threshold is not derived from any principled criterion (e.g., effect size conventions, practical significance for model ranking, or comparison to measurement error). A threshold chosen post hoc to match the observed result raises concerns. The paper should either: (a) derive the threshold from practical consequences (e.g., what interaction magnitude would change a model ranking?), (b) report the result without a binary threshold and let readers judge, or (c) use a formal hypothesis test with appropriate power analysis.\n\n- **(W3) Bootstrap CIs are reported only for the MMLU item_id component in most tables.** The paper summary mentions \"Bootstrap CIs (1000 resamples)\" as a general methodology, but Table 1 in the paper shows CIs for all components only on MMLU. Cross-benchmark (Table 3/4), hardware (Table 5), 14B (Table 9), and fine-tuning (Table 10) tables report point estimates without CIs. For claims about variance component magnitudes being \"negligible\" or \"substantial,\" CIs are essential---a 0.5% point estimate with a CI of [0.0%, 3.0%] tells a very different story than [0.4%, 0.6%]. This is especially critical for the separability claim where the threshold is tight.\n\n- **(W4) ANOVA-based estimation (Henderson Method I) is used in the code, but the paper claims REML.** The variance_decomposition.py code implements classical ANOVA-based variance component estimation (Type-I SS with EMS equations), not REML. REML would use a mixed-effects model fitted via maximum likelihood with restricted estimation. These methods can give different results, especially when designs are slightly unbalanced or when negative variance components arise. The code truncates negative estimates to zero, which is the ANOVA convention; REML handles this differently (constrained optimization). The paper should either: (a) actually implement REML (e.g., using lme4/statsmodels), or (b) correctly describe the method as ANOVA-based Henderson Method I estimation. Claiming REML when using ANOVA-based methods is a methodological misrepresentation.\n\n### Moderate\n\n- **(W5) Only 2 GPU types for the hardware facet, with partial crossing.** The hardware experiment (Exp 3) uses only 2 GPU types with partial crossing (only 2 of 4 models run on both). With n=2 levels, the hardware main effect has 1 degree of freedom---insufficient for stable variance component estimation. The claim that \"hardware-related variance totals 4.1%\" has very wide implicit uncertainty. The partial crossing also means the hardware x model interaction is confounded with the hardware main effect for the 2 models not run on both GPUs. This limitation is not adequately discussed.\n\n- **(W6) Item dominance may be a statistical artifact of the binary response variable.** With a binary correct/incorrect response, items with extreme p-values (very easy or very hard) contribute disproportionately to total variance. The paper's own Decision D002 acknowledges that text_exact_match produces a radically different variance structure (prompt x item at 37.5% vs item_id at 58.4% for binary). Yet the paper presents only the binary metric results. If the core claim is \"item selection dominates variance,\" this claim is metric-dependent, and the paper should present both metrics or at minimum discuss the metric sensitivity. The dual-metric analysis planned in D002 appears to have been dropped from the paper.\n\n- **(W7) Temperature levels differ across experiments without justification.** Exp 1 uses {0.1, 0.5, 1.0}, the paper summary mentions {0.0, 0.3, 0.7}, the experiment plan mentions {0.1, 0.5, 1.0} for some and 2 temperatures for others. Exp 2 uses 2 temperatures while Exp 1 uses 3. These inconsistencies make cross-experiment comparisons unreliable and suggest the \"fully crossed\" characterization is only approximate. The design is not truly balanced across experiments.\n\n- **(W8) D-study projections assume independence of item samples.** The D-study formula G = sigma_tau / (sigma_tau + sigma_delta) assumes that additional items are independently sampled from the same universe. But benchmark items are not a random sample from a well-defined universe---they are curated collections. Extrapolating from 200 stratified-sampled items to 600 or 1100 items assumes the variance structure holds for items not in the sample. For MATH (500 total items), the recommendation of 1100 items is infeasible and reveals the limitation of treating benchmark items as a random sample from an infinite universe.\n\n- **(W9) The paper omits higher-order interactions.** The code explicitly states \"Higher-order interactions (>=3-way) are absorbed into the residual.\" With 6 facets, there are 20 three-way interactions, 15 four-way, etc. The residual of 16.8% likely contains substantial structured variance. If precision x temperature x item is large (plausible given both two-way interactions are non-trivial), the attributed shares for the two-way components would be biased. The paper should at minimum discuss this limitation or fit selected three-way interactions.\n\n### Minor\n\n- **(W10) The Kruskal-Wallis test (H=47.3, p<0.001) cited for cross-benchmark differences is underspecified.** What is the test comparing? Variance component estimates across benchmarks? With only 5 benchmarks and point estimates, the degrees of freedom and interpretation are unclear.\n\n- **(W11) No correction for multiple comparisons.** Multiple permutation tests and bootstrap CIs are computed without any family-wise error rate correction (e.g., Bonferroni, Holm).\n\n- **(W12) The \"10x more cost-effective\" headline claim conflates marginal and average returns.** The 10.2:1 ratio compares marginal G gains per unit cost, but the cost metric treats one additional item the same as one additional prompt. In practice, additional prompts require human design effort while additional items can be sampled automatically. The cost comparison should distinguish compute cost from human annotation cost.\n\n## Questions for Authors\n\n1. Why is \"model\" not a facet in the G-study? If models are pooled, how much of the 58.4% item_id variance is actually model x item interaction? Can you provide the per-model G-study results as the primary analysis?\n\n2. The code uses ANOVA-based Henderson Method I estimation, but the paper claims REML. Which method was actually used for the reported results? If ANOVA-based, have you verified that the balanced-design assumption holds exactly (i.e., every cell has exactly the same number of observations)?\n\n3. What happens to the variance decomposition when you use text_exact_match instead of binary correct? Decision D002 in your project files describes this as producing a radically different structure. Why was this analysis excluded from the paper?\n\n4. The separability threshold of 0.5% appears to match the observed result exactly. Was this threshold set before or after seeing the data? What would the conclusion be at a 1% threshold? At 0.1%?\n\n5. For the MATH D-study recommendation of 1100 items: MATH has only 500 items total. How should practitioners interpret a recommendation that exceeds the benchmark size? Does this invalidate the D-study framework for small benchmarks?\n\n6. Can you provide bootstrap CIs for the separability claim (total direct infra x method interaction)? The 0.5% point estimate needs uncertainty quantification to be interpretable.\n\n7. How sensitive are the variance component estimates to the exclusion of three-way interactions? Have you tested a model with, e.g., precision x temperature x item included?\n\n8. The paper mentions temperature {0.0, 0.3, 0.7} in the summary but {0.1, 0.5, 1.0} in the tex file. Which values were actually used, and does including T=0.0 (deterministic) vs T=0.1 (near-deterministic) materially change the temperature variance component?\n\n## Score and Recommendation\n\n**Score: 4 (Borderline Reject)**\n\n**Confidence: High**\n\n**Recommendation: Borderline Reject**\n\nThe paper tackles an important problem with impressive experimental scale and provides useful practical contributions (engine confound identification, D-study budgets). However, the methodological concerns are substantive: (1) the treatment of model as pooled rather than as a G-theory facet fundamentally confounds the headline variance decomposition; (2) the mismatch between claimed (REML) and implemented (ANOVA) estimation methods undermines methodological credibility; (3) incomplete uncertainty quantification (CIs missing from most tables, especially the separability claim); and (4) the single-metric presentation omits a known sensitivity that changes the core finding. These are not cosmetic issues---they affect the validity of the three central claims. If the authors can address W1 (model as facet), W4 (REML vs ANOVA), W3 (CIs throughout), and W6 (dual metric), the paper would be substantially strengthened and could merit acceptance. In its current form, the ambitious scope is undermined by methodological gaps that a psychometrics-savvy reviewer would flag immediately.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d791cb4a-880c-460c-9412-d3102d36c978",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPS5K1FPH3w6HxZZUqp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b838821-a1e4-460c-a5d0-7647ed22b113",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNwG2GALpMGWAVoy1YEhMS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 74114,
      "output_tokens": 3345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 754
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3345,
          "cache_read_input_tokens": 74114,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 754,
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

_source line 50 · 2026-05-20T19:41:05.978Z_

<details><summary>↩ Tool result · `toolu_01C6nhefC7jffGb4pAAJQR9A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/review_report.md\", \"dream_id\": \"dream_20260520T190053\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b838821-a1e4-460c-a5d0-7647ed22b113",
  "isSidechain": true,
  "promptId": "fa6378cd-1bec-48a8-a6a4-0315da7f8a97",
  "agentId": "ab95321e8cc70eb32",
  "type": "user",
  "uuid": "ee2dbf85-8f91-4783-91ff-a52211c55f7f",
  "sourceToolAssistantUUID": "1b838821-a1e4-460c-a5d0-7647ed22b113",
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

_source line 51 · 2026-05-20T19:41:17.708Z_

Review submitted successfully. Here is the summary:

---

**Score: 4 / 6 (Borderline Reject) | Confidence: High**

The review identifies 4 major weaknesses, 5 moderate, and 3 minor issues. The most critical findings:

**Major issues:**
1. **Model pooled instead of treated as a G-theory facet** -- the 58.4% item_id figure is confounded with model x item interaction. This is a fundamental design flaw for a G-theory paper.
2. **Separability threshold (0.5%) is arbitrary and matches the observed result exactly** -- appears post-hoc.
3. **Bootstrap CIs missing from most tables** -- especially critical for the separability claim.
4. **Code implements ANOVA-based Henderson Method I, but paper claims REML** -- a methodological misrepresentation discovered by reading `variance_decomposition.py`.

**Moderate issues:**
- Only 2 GPU types with partial crossing (1 df for hardware main effect)
- Binary response metric inflates item variance; the dual-metric analysis from D002 was dropped from the paper
- Temperature levels differ across experiments without justification
- D-study extrapolation assumes infinite item universe (MATH recommendation of 1100 items exceeds benchmark size of 500)
- All 3-way+ interactions absorbed into residual (16.8%) without discussion

**What would move this to Accept:** Fix model-as-facet treatment, correctly describe the estimation method (or implement actual REML), provide CIs on all variance component tables, and include the dual-metric analysis.

Report saved to `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee2dbf85-8f91-4783-91ff-a52211c55f7f",
  "isSidechain": true,
  "agentId": "ab95321e8cc70eb32",
  "requestId": "req_011CbEPZGZNseKKqB6nLCf5k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e474dac4-7a5d-404e-960f-35bbbe441d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "73f25614-6311-4958-8c3c-0f90d7450270",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5Qft4uqTV66JwbRC9xMTy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3475,
      "cache_read_input_tokens": 74868,
      "output_tokens": 428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3475
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 428,
          "cache_read_input_tokens": 74868,
          "cache_creation_input_tokens": 3475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3475,
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
