# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review standard: top ML v

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4f148f2fd0307ae6.jsonl`
- **Structured JSON:** [`5119cc27444e3ed0e371.json`](../../sessions/51/5119cc27444e3ed0e371.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-20T23:40:55.371Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review standard: top ML venue, acceptance rate ~25%, 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

## Paper Summary
Title: "Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics"

The paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure (numerical precision, hardware) with methodology (prompt, seed, temperature, ordering) and measurement (item selection) facets across 5 benchmarks (MMLU, ARC, GSM8K, HellaSwag, MATH), 4 7-9B models + 2 14B models, and 2 GPU types, totaling 3M+ observations. Three claims: (1) item dominance is benchmark-conditional (48% knowledge → 28% proof reasoning) forming a 3-tier clustering; (2) infra×method separability holds on knowledge benchmarks (<0.5%) but breaks on math-generation (3%); (3) reproducibility budgets are metric-dependent (G=0.37 binary vs G=0.97 text-match).

## Paper Structure (10 pages)
- Pages 1-2: Abstract, Intro, Related Work (4 subsections: variance sources, G-theory in NLP, item-level/efficient benchmarking, training instability)
- Page 3: Framework (G-theory basics with Eq 1-2, Experimental Design listing 9 experiments)
- Page 4-8: Results (12 subsections with 15 tables)
- Page 9: Discussion (5 paragraphs + Limitations), Conclusion
- Page 10: References (15 entries)

## Related Work as Presented
The paper cites:
- Yuan et al. (2025): Up to 9% accuracy from precision — paper extends with item-level G-theory breakdown
- Mizrahi et al. (2024, Brittlebench): ~50% variance from prompts — paper crosses prompts with infrastructure
- Lu et al. (2022), Pezeshkpour & Hruschka (2024): Seed/ordering effects — paper includes both as facets
- Biderman et al. (2024): Reproducibility lessons — positioned as motivation
- Bouthillier et al. (2021): ANOVA for ML benchmarks — paper extends to G-theory
- Mesting (2026): G-theory for LLM eval, 5 methodology facets, single benchmark (MMLU) — paper adds infrastructure crossing + multi-benchmark
- IRT: Lalor et al. (2019), Rodriguez et al. (2021), Vania et al. (2021), Polo et al. (2024, tinyBenchmarks), Perlitz et al. (2023) — positioned as complementary
- Training: Dodge et al. (2020), Sellam et al. (2022, MultiBERTs), Henderson et al. (2018), Dehghani et al. (2021, Benchmark Lottery) — fine-tuning G-study extends this

## Key Claims to Assess for Novelty
1. "First multi-benchmark G-theory analysis of LLM evaluation" — Is this truly novel vs. Mesting (2026) and Bouthillier et al. (2021)?
2. "Infrastructure×methodology crossing in unified design" — Has this been done before?
3. "Task-type clustering / benchmark-conditional variance structure" — How novel vs. existing benchmark comparison work?
4. "Model-as-facet revealing 16-22% model×item" — Standard in G-theory but novel in LLM context?
5. "Metric-dependent reproducibility budgets via D-study" — Novel contribution or straightforward application?
6. "Fine-tuning variance decomposition with G-theory" — Novel vs. Dodge et al., Sellam et al.?

## Your Review Focus Areas
1. **Novelty assessment**: Is the contribution primarily methodological (applying G-theory to new setting), empirical (new findings), or both? Is this sufficient for a top venue?
2. **Related work completeness**: Are there missing references? Is the positioning accurate?
3. **Contribution clarity**: Are the three claimed contributions well-differentiated from prior work?
4. **Framing and narrative**: Is the "benchmark-conditional variance structure" framing compelling? Is the three-tier clustering well-motivated or post-hoc?
5. **Broader impact**: Does the paper advance the field meaningfully? Will practitioners actually use D-study projections?
6. **Writing quality**: Is the paper well-organized for its density (15 tables in 10 pages)? Is the narrative coherent?

## Output Format
Structure your review as:
```
## R2 Review: Novelty & Related Work

### Summary
[2-3 sentences]

### Strengths
[Numbered list, be specific]

### Weaknesses
[Numbered list, be specific with page/section references]

### Questions for Authors
[Numbered list]

### Minor Issues
[Numbered list]

### Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "9128e7b0-dd8a-403d-be8e-3e63fff13b3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T23:40:55.374Z_

```json
{
  "parentUuid": "9128e7b0-dd8a-403d-be8e-3e63fff13b3f",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
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
  "uuid": "1e01374e-78d1-4242-80f8-8043e5291618",
  "timestamp": "2026-05-20T23:40:55.374Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T23:40:59.995Z_



I'll start by loading the project files to read the actual paper and related materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e01374e-78d1-4242-80f8-8043e5291618",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhqyU3UG8FCH1MH7vtJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52d350cf-00e5-4769-a528-cba787626e8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RYrWxdHjjmoenLhx8oxzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7383,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7383,
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

_source line 4 · 2026-05-20T23:41:01.958Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018QiLivReNYswza8tpNnGQN`</summary>

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
  "parentUuid": "52d350cf-00e5-4769-a528-cba787626e8e",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhqyU3UG8FCH1MH7vtJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "558ed8b8-98c9-4fab-8269-7e5e91995774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RYrWxdHjjmoenLhx8oxzw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7383,
      "cache_read_input_tokens": 8250,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 140,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7383,
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

_source line 5 · 2026-05-20T23:41:01.960Z_

<details><summary>↩ Tool result · `toolu_018QiLivReNYswza8tpNnGQN`</summary>

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
  "parentUuid": "558ed8b8-98c9-4fab-8269-7e5e91995774",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "1fc796c5-eafe-42f9-bb8f-144857fadab0",
  "sourceToolAssistantUUID": "558ed8b8-98c9-4fab-8269-7e5e91995774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T23:41:04.709Z_



Let me read the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fc796c5-eafe-42f9-bb8f-144857fadab0",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhrTaUMzhePjugfRr6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4482e90a-0480-421d-aa58-5c7a8fa8adcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvceDcVGQXmr5JkC1gNtfd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 15633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2059,
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

_source line 7 · 2026-05-20T23:41:05.163Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01HJQrMUtXsG6g8xoCUHjJUa`</summary>

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
  "parentUuid": "4482e90a-0480-421d-aa58-5c7a8fa8adcc",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhrTaUMzhePjugfRr6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d923e6a-95bd-43e9-b226-ca5ed0171db2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvceDcVGQXmr5JkC1gNtfd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 15633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2059,
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

_source line 8 · 2026-05-20T23:41:05.184Z_

<details><summary>↩ Tool result · `toolu_01HJQrMUtXsG6g8xoCUHjJUa`</summary>

```text
{"result":"# 项目 nlp_variance_gtheory 概况\n\n## 实验状态 (2 个)\n\n- **bf16_eager_disentangle**: DONE (negative) — \n- **mvp_phase_a**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\n\n## 趋势\n成功 1 / 负向 1 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32570: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d923e6a-95bd-43e9-b226-ca5ed0171db2",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "0334b915-cad5-46fb-a47e-d1502bed9d60",
  "sourceToolAssistantUUID": "7d923e6a-95bd-43e9-b226-ca5ed0171db2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T23:41:06.147Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011NLNXYqgqyTHCnC3HybsXc`</summary>

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
  "parentUuid": "0334b915-cad5-46fb-a47e-d1502bed9d60",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhrTaUMzhePjugfRr6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acdfa62b-1848-4184-b2d8-d075356d26a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvceDcVGQXmr5JkC1gNtfd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 15633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2059,
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

_source line 10 · 2026-05-20T23:41:06.155Z_

<details><summary>↩ Tool result · `toolu_011NLNXYqgqyTHCnC3HybsXc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **bf16_eager_disentangle** (negative): The 8.5pp accuracy gap between FP32 and BF16 in MVP Phase A is primarily due to engine differences (V0 enforce_eager vs V1 CUDA graph), not numerical precision. Running BF16+enforce_eager should show similar degradation to FP32. ← 基于 mvp_phase_a\\n- **mvp_phase_a** (success): G-theory can successfully decompose infrastructure (precision) × methodology (prompt, seed, ordering, temperature) crossed variance components in LLM evaluation, with at least 2 components exceeding 5% of total variance and at least 1 significant precision×methodology interaction.\\n\\n## 趋势\\n成功 1 / 负向 1 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32570: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 800, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acdfa62b-1848-4184-b2d8-d075356d26a0",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "b4d31a67-e02d-4c2f-8648-3d61f1be7583",
  "sourceToolAssistantUUID": "acdfa62b-1848-4184-b2d8-d075356d26a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:41:06.796Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SpeBAEycG5wqXGnLZ29gFo`</summary>

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
  "parentUuid": "b4d31a67-e02d-4c2f-8648-3d61f1be7583",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhrTaUMzhePjugfRr6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa6fedcb-e404-4046-ad81-8c71a4494df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvceDcVGQXmr5JkC1gNtfd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 15633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2059,
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

_source line 12 · 2026-05-20T23:41:06.804Z_

<details><summary>↩ Tool result · `toolu_01SpeBAEycG5wqXGnLZ29gFo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T14:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"gtheory_evaluation\\\"\\n    name: \\\"G-Theory & Evaluation Variance\\\"\\n    narrative: \\\"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\\\"\\n  - key: \\\"infrastructure_variance\\\"\\n    name: \\\"Infrastructure-Induced Variance\\\"\\n    narrative: \\\"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\\\"\\n  - key: \\\"prompt_sensitivity\\\"\\n    name: \\\"Prompt Sensitivity & Methodological Variance\\\"\\n    narrative: \\\"Prompt phrasing, seed, temperature, and ordering as variance sources\\\"\\n  - key: \\\"evaluation_methodology\\\"\\n    name: \\\"Evaluation Methodology\\\"\\n    narrative: \\\"Scoring artifacts, benchmark design, and evaluation protocol considerations\\\"\\n\\npapers:\\n  mesting2026hidden:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\\\"\\n    authors:\\n      - \\\"Mesting, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.11581\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  brittlebench2026:\\n    title: \\\"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.13285\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  yuan2025layercast:\\n    title: \\\"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\\\"\\n    authors:\\n      - \\\"Yuan, Z.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09501\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  messina2026background:\\n    title: \\\"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\\\"\\n    authors:\\n      - \\\"Messina, P.\\\"\\n      - \\\"Scotta, A.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.22411\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  generalizit2024:\\n    title: \\\"GeneralizIT: A Python Solution for Generalizability Theory Computations\\\"\\n    authors: []\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2411.17880\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  hua2025flaw:\\n    title: \\\"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\\\"\\n    authors:\\n      - \\\"Hua, W.\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    category: \\\"evaluation_methodology\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  thinkingmachines2025batch:\\n    title: \\\"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"Technical Report\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  kunievsky2025intent:\\n    title: \\\"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\\\"\\n    authors:\\n      - \\\"Kunievsky, D.\\\"\\n      - \\\"Evans, J.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.16584\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  bui2025seeds:\\n    title: \\\"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\\\"\\n    authors:\\n      - \\\"Bui, T.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  sameprompt2026:\\n    title: \\\"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.14349\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\", \"total_chars\": 6732, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa6fedcb-e404-4046-ad81-8c71a4494df2",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "9bd07563-57b5-4ee6-82c9-ea283886e502",
  "sourceToolAssistantUUID": "fa6fedcb-e404-4046-ad81-8c71a4494df2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T23:41:10.454Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01D58rq1sBWKCdGmNpsMds2A`</summary>

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
  "parentUuid": "9bd07563-57b5-4ee6-82c9-ea283886e502",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhrpdkMeivWPS842WPq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a58d593a-00b9-425f-a68a-cb401dd53143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3E5Z9Z4Q9fXeFwxkTxFr3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3938,
      "cache_read_input_tokens": 17692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3938,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 14 · 2026-05-20T23:41:10.466Z_

<details><summary>↩ Tool result · `toolu_01D58rq1sBWKCdGmNpsMds2A`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a58d593a-00b9-425f-a68a-cb401dd53143",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "9a44aa9e-250c-4d93-baf8-d871cbff41f9",
  "sourceToolAssistantUUID": "a58d593a-00b9-425f-a68a-cb401dd53143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T23:41:10.981Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RZndbm5XURbbYN6iytckiP`</summary>

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
  "parentUuid": "9a44aa9e-250c-4d93-baf8-d871cbff41f9",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhrpdkMeivWPS842WPq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a18b56b-f6bd-4ee3-ac34-c4cfe9cf45db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3E5Z9Z4Q9fXeFwxkTxFr3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3938,
      "cache_read_input_tokens": 17692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3938,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 16 · 2026-05-20T23:41:11.089Z_

<details><summary>↩ Tool result · `toolu_01RZndbm5XURbbYN6iytckiP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/memory.md\", \"content\": \"# Memory — nlp_variance_gtheory\\n\\n## Gated Model 约束 (2026-05-20)\\nLlama-3.1-8B-Instruct 和 gemma-2-9b-it 是 HF gated models，直接用 repo ID 加载失败。westd-32570 上通过 ModelScope 下载到本地路径（如 `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct`）。exp-001 正式运行需要 model path mapping 或 HF token。\\n\\n## 双 Metric 设计决策 (2026-05-20, D002)\\nbinary_correct 和 text_exact_match 测量正交维度（Spearman ρ = −0.21, n.s.）。前者衡量评估有效性（item 难度主导），后者衡量可复现性（prompt×item + temperature 主导）。两者必须同时保留——不能互相替代。\\n\\n## Temperature 对 text_match 的决定性影响 (2026-05-20)\\nT=0 → text_match=0.247, T=0.5 → text_match=0.019（降 92%），但 binary_correct 几乎不变。这是 G-theory 框架的关键洞察：采样随机性改变文本表述但不改变答案选择。\\n\\n## FP32 精度效应确认 (2026-05-20)\\nFP32 的 8.5pp accuracy gap 中 97.4% 是精度效应（非引擎 confound）。BF16-trained model 用 FP32 推理表现更差，可能因为权重从 BF16 加载到 FP32 时的数值行为差异。\\n\", \"total_chars\": 790, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a18b56b-f6bd-4ee3-ac34-c4cfe9cf45db",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "62a39ace-5989-4cd4-ae90-4d26e7414e38",
  "sourceToolAssistantUUID": "2a18b56b-f6bd-4ee3-ac34-c4cfe9cf45db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T23:41:11.499Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018cZFCKdkPZJABqrAngNWte`</summary>

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
  "parentUuid": "62a39ace-5989-4cd4-ae90-4d26e7414e38",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhrpdkMeivWPS842WPq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "823a68f2-7ba5-4313-9435-162180d9a0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3E5Z9Z4Q9fXeFwxkTxFr3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3938,
      "cache_read_input_tokens": 17692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3938,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 18 · 2026-05-20T23:41:11.511Z_

<details><summary>↩ Tool result · `toolu_018cZFCKdkPZJABqrAngNWte`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md\", \"content\": \"# Paper Framing — nlp_variance_gtheory\\n\\n## Target Venue\\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\\n- Extended: TACL (rolling)\\n\\n## Title\\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\\n\\n## Core Claims (3 条，可证伪)\\n\\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation (MVP: 58.4% on MMLU single-model; expected to decrease with model-as-facet reanalysis). Its magnitude is hypothesized to be benchmark-dependent — weakening on reasoning tasks where temperature/seed interactions increase — but this gradient requires exp-002 confirmation. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating whether a systematic benchmark-dependent gradient exists, and (c) deriving D-study implications specific to LLM evaluation.\\n**Fallback narratives**: (A) If gradient confirmed → \\\"benchmark-conditional variance structure\\\"; (B) If gradient not significant → \\\"item dominance is universal but magnitude varies\\\"; (C) If model-as-facet reduces item_id below 30% → pivot to \\\"model×item interaction is the dominant source\\\" — narrative direction changes substantially.\\n\\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \\\"infrastructure\\\" is currently limited to the precision facet.\\n\\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\\n\\n## Contributions (3 条，明确区分)\\n\\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\\n\\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\\n\\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\\n\\n## Story Spine\\n\\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\\n\\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\\n\\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\\n\\n**Headline result template**: \\\"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (X-Y%, benchmark-dependent [placeholder: fill after exp-001/002]), while direct infrastructure×methodology interactions are negligible. Variance structure [is/is not] benchmark-conditional [pending exp-002]. D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional.\\\"\\n\\n## Hook (Counter-Intuitive Quantified Claim)\\n\\\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\\\"\\n\\n## Narrative Strategy\\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\\n- **Tension**: \\\"No universal recipe\\\" — the field seeks standardization but variance structure varies qualitatively across task types\\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\\n- **Figure plan** (4 figures minimum):\\n  1. Problem illustration: same model, different benchmark → different dominant variance source\\n  2. G-theory facet diagram showing crossed design\\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\\n  4. D-study projection curves: G vs item count for different benchmarks\\n- **Key framing shifts from Dream feedback**:\\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\\n  - Cross-benchmark gradient is the **primary novel finding**\\n  - \\\"Fully crossed\\\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\\n\\n## Venue Fit Risks\\n- AAAI: Strong fit for \\\"evaluation methodology\\\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\\n- Reviewer concern 1: \\\"Only open-weight models, not API models\\\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\\n- Reviewer concern 2: \\\"G-theory is borrowed methodology, not novel\\\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\\n- Reviewer concern 3: \\\"Item dominance is obvious from measurement theory\\\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n1. **\\\"Only N GPU types\\\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \\\"numerical precision\\\" and frame hardware as future work.\\n2. **\\\"float32 engine confound\\\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\\n3. **\\\"Only MMLU\\\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\\n4. **\\\"Small item sample\\\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\\n5. **\\\"No training-time analysis\\\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\\n6. **\\\"Missing scale validation\\\"** → exp-005 (14B models)\\n7. **\\\"G-theory may not be right framework\\\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\\n8. **\\\"Separability claim is metric-dependent\\\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\\n9. **\\\"FP32 degradation is already known (Yuan 2025)\\\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\\n10. **\\\"Incremental over Mesting (2026)\\\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\\n11. **\\\"Model not treated as G-theory facet\\\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\\n12. **\\\"No CIs on variance components\\\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\\n13. **\\\"Missing related work — IRT, tinyBenchmarks, Bouthillier\\\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\\n14. **\\\"Diagnostic tool claim unsubstantiated\\\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \\\"empirical analysis + data release.\\\"\\n15. **\\\"Fine-tuning uses encoder-only RoBERTa\\\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\\n\\n## Design Decisions\\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \\\"reduced crossing\\\" rather than \\\"fully crossed.\\\"\\n\\n## Required Bibliography (minimum 25 references)\\nKey references to include beyond current literature_map:\\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\\n- Perlitz et al. (2023) — Efficient LLM benchmarking\\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\\n- Shavelson & Webb (1991) — G-theory primer (canonical)\\n- Brennan (2001) — G-theory textbook (canonical)\\n- Lu et al. (2022) — Option ordering effects in MC evaluation\\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\\n- Dehghani et al. (2021) — Benchmark Lottery\\n- Biderman et al. (2024) — Evaluation reproducibility lessons\\n- Vania et al. (2021) — IRT item properties in NLP\\n\", \"total_chars\": 13880, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "823a68f2-7ba5-4313-9435-162180d9a0f9",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "2c9b054f-49ea-41f8-b001-06abff86c945",
  "sourceToolAssistantUUID": "823a68f2-7ba5-4313-9435-162180d9a0f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-20T23:41:14.630Z_

Now let me read the actual paper draft and the distilled research/writing skills.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c9b054f-49ea-41f8-b001-06abff86c945",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhsAf1sngyoNyW3JAyM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b53f6de6-454b-4fa1-9db0-e2a5176c5d6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMBkW4TURmQNmTuo5rWVrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4810,
      "cache_read_input_tokens": 21630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4810,
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

_source line 20 · 2026-05-20T23:41:16.050Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HWjB4WrcJQRpwAo4Wdjp1B`</summary>

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
  "parentUuid": "b53f6de6-454b-4fa1-9db0-e2a5176c5d6a",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhsAf1sngyoNyW3JAyM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4295aa7c-bbcc-40a8-a184-0e94a8f11f8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMBkW4TURmQNmTuo5rWVrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4810,
      "cache_read_input_tokens": 21630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4810,
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

_source line 21 · 2026-05-20T23:41:16.138Z_

<details><summary>↩ Tool result · `toolu_01HWjB4WrcJQRpwAo4Wdjp1B`</summary>

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
  "parentUuid": "4295aa7c-bbcc-40a8-a184-0e94a8f11f8d",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "3ed8443a-5511-42e7-9620-b648a80ed19c",
  "sourceToolAssistantUUID": "4295aa7c-bbcc-40a8-a184-0e94a8f11f8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T23:41:17.054Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JuAsNMjw6xye6AWRuVFjHb`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ed8443a-5511-42e7-9620-b648a80ed19c",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhsAf1sngyoNyW3JAyM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80b8f818-0f36-4f11-ad2f-369238ab9985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMBkW4TURmQNmTuo5rWVrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4810,
      "cache_read_input_tokens": 21630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4810,
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

_source line 23 · 2026-05-20T23:41:17.105Z_

<details><summary>↩ Tool result · `toolu_01JuAsNMjw6xye6AWRuVFjHb`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/paper.pdf
artifacts/dream_reports/dream_20260520T190053/median/paper.pdf
artifacts/dream_reports/dream_20260520T190053/worst/paper.pdf
artifacts/dream_reports/dream_20260520T222113/best/paper.pdf
artifacts/dream_reports/dream_20260520T222113/median/paper.pdf
artifacts/dream_reports/dream_20260520T222113/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80b8f818-0f36-4f11-ad2f-369238ab9985",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "0ed6fb76-d2e1-45e1-a068-de70e4c1dfe3",
  "sourceToolAssistantUUID": "80b8f818-0f36-4f11-ad2f-369238ab9985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T23:41:17.644Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DLcJ5LZodQLUbmJi7Wyo17`</summary>

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
  "parentUuid": "0ed6fb76-d2e1-45e1-a068-de70e4c1dfe3",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhsAf1sngyoNyW3JAyM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a57ff833-91b0-47ec-b668-a924b97c5336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMBkW4TURmQNmTuo5rWVrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4810,
      "cache_read_input_tokens": 21630,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4810
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 21630,
          "cache_creation_input_tokens": 4810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4810,
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

_source line 25 · 2026-05-20T23:41:17.681Z_

<details><summary>↩ Tool result · `toolu_01DLcJ5LZodQLUbmJi7Wyo17`</summary>

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
  "parentUuid": "a57ff833-91b0-47ec-b668-a924b97c5336",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "f065dfe0-1642-422b-ab2d-9a08c8445630",
  "sourceToolAssistantUUID": "a57ff833-91b0-47ec-b668-a924b97c5336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T23:41:21.783Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DW49UywQcRWzYaYGwHTrJY`</summary>

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
  "parentUuid": "f065dfe0-1642-422b-ab2d-9a08c8445630",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhscy4D6K2zHfYdeZeT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5423cf30-2336-451f-bbb9-b0a038f11b0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGxSgPwq3Rv7dam2WBJNja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 26440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1640,
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

_source line 27 · 2026-05-20T23:41:21.788Z_

<details><summary>↩ Tool result · `toolu_01DW49UywQcRWzYaYGwHTrJY`</summary>

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
  "parentUuid": "5423cf30-2336-451f-bbb9-b0a038f11b0c",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "db5154e8-b7e3-44a9-9449-9c20ec250785",
  "sourceToolAssistantUUID": "5423cf30-2336-451f-bbb9-b0a038f11b0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T23:41:22.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fbz6qJL25QvydyE41zz2ok`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db5154e8-b7e3-44a9-9449-9c20ec250785",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhscy4D6K2zHfYdeZeT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79b4cf7e-fcb8-46bd-a0c2-76833ea0fbea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGxSgPwq3Rv7dam2WBJNja",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 26440,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 26440,
          "cache_creation_input_tokens": 1640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1640,
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

_source line 29 · 2026-05-20T23:41:22.960Z_

<details><summary>↩ Tool result · `toolu_01Fbz6qJL25QvydyE41zz2ok`</summary>

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
108	\sigma^2_{\text{total}} = \sigma^2_o + \sum_j \sigma^2_{f_j} + \sum_{j<l} \sigma^2_{f_j f_l} + \cdots + \sigma^2_{\text{residual}}
109	\end{equation}
110	
111	The \textbf{Generalizability coefficient} $G$ is the ratio of object-of-measurement variance to total variance including all error sources:
112	\begin{equation}
113	G = \frac{\sigma^2_o}{\sigma^2_o + \sum_{j} \frac{\sigma^2_{f_j}}{n_{f_j}} + \sum_{j<l}\frac{\sigma^2_{f_jf_l}}{n_{f_j}n_{f_l}} + \cdots + \frac{\sigma^2_{\text{res}}}{\prod_j n_{f_j}}}
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79b4cf7e-fcb8-46bd-a0c2-76833ea0fbea",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "7e2c625c-556d-460c-a30b-270092726ebe",
  "sourceToolAssistantUUID": "79b4cf7e-fcb8-46bd-a0c2-76833ea0fbea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T23:41:27.337Z_

<details open><summary>🔧 Tool call — Read · `toolu_017mnJpPAKv55c5Xw1zG8vCW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2c625c-556d-460c-a30b-270092726ebe",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEht1TQE1SWXLFXzZak6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6df5262-7778-4c6b-9b10-5ad38be5acd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUvqX6FamhdsA9wYHupsXN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6037,
      "cache_read_input_tokens": 28080,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 28080,
          "cache_creation_input_tokens": 6037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6037,
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

_source line 31 · 2026-05-20T23:41:27.348Z_

<details><summary>↩ Tool result · `toolu_017mnJpPAKv55c5Xw1zG8vCW`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6df5262-7778-4c6b-9b10-5ad38be5acd4",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "d3690e9d-452a-426e-840a-54550cdad75a",
  "sourceToolAssistantUUID": "f6df5262-7778-4c6b-9b10-5ad38be5acd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T23:41:31.935Z_

<details open><summary>🔧 Tool call — Read · `toolu_018XvHYYtPnXemrZzwNoCXzY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/paper.tex",
  "offset": 498,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3690e9d-452a-426e-840a-54550cdad75a",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhtLcLNrVkzSctdtLXL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdac0a7b-d7a6-48bc-af18-15fe5b7d19e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEmYvzRBCjVQacjG6EhUwC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6305,
      "cache_read_input_tokens": 34117,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6305
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 34117,
          "cache_creation_input_tokens": 6305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6305,
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

_source line 33 · 2026-05-20T23:41:31.943Z_

<details><summary>↩ Tool result · `toolu_018XvHYYtPnXemrZzwNoCXzY`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdac0a7b-d7a6-48bc-af18-15fe5b7d19e9",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "dfc59fbe-f4b5-4d11-a714-a10f34dbb2d2",
  "sourceToolAssistantUUID": "bdac0a7b-d7a6-48bc-af18-15fe5b7d19e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-20T23:41:34.909Z_

Now let me also check if there are any earlier dream review reports to understand what's already been reviewed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfc59fbe-f4b5-4d11-a714-a10f34dbb2d2",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhtg3Nj4uLafQuxbaAh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8974d653-7111-47d4-8b08-e49a5c9c34c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mATRfVeVLbvRNmmFFY318",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6437,
      "cache_read_input_tokens": 40422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6437,
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

_source line 35 · 2026-05-20T23:41:37.403Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011WepiGjVaMN3MTRTnNpQSs`</summary>

```json
{
  "pattern": "**/dream_reports/**/review_report.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8974d653-7111-47d4-8b08-e49a5c9c34c2",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhtg3Nj4uLafQuxbaAh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66751353-1320-4368-b122-9f72ad212b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mATRfVeVLbvRNmmFFY318",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6437,
      "cache_read_input_tokens": 40422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6437,
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

_source line 36 · 2026-05-20T23:41:37.419Z_

<details><summary>↩ Tool result · `toolu_011WepiGjVaMN3MTRTnNpQSs`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/median/review_report.md
artifacts/dream_reports/dream_20260520T190053/best/review_report.md
artifacts/dream_reports/dream_20260520T190053/worst/review_report.md
artifacts/dream_reports/dream_20260520T222113/median/review_report.md
artifacts/dream_reports/dream_20260520T222113/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66751353-1320-4368-b122-9f72ad212b71",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "112bfb73-7cee-422a-97f8-bce7fbb8dba8",
  "sourceToolAssistantUUID": "66751353-1320-4368-b122-9f72ad212b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T23:41:38.302Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MAoGcWnotaNPzbXXxoTEcT`</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "112bfb73-7cee-422a-97f8-bce7fbb8dba8",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhtg3Nj4uLafQuxbaAh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d770cf7c-7433-40a2-8f12-c29ebf1ab206",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mATRfVeVLbvRNmmFFY318",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6437,
      "cache_read_input_tokens": 40422,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6437
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 40422,
          "cache_creation_input_tokens": 6437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6437,
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

_source line 38 · 2026-05-20T23:41:38.311Z_

<details><summary>↩ Tool result · `toolu_01MAoGcWnotaNPzbXXxoTEcT`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d770cf7c-7433-40a2-8f12-c29ebf1ab206",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "88d11d92-f657-44f1-8d3e-8e23ebdf4bf7",
  "sourceToolAssistantUUID": "d770cf7c-7433-40a2-8f12-c29ebf1ab206",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T23:41:42.042Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RqRWCtnHWuHrDhvzW3d4KH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d11d92-f657-44f1-8d3e-8e23ebdf4bf7",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhu9D1LunRjoTLUzGGY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5dad43e8-f15f-4a61-9a41-dfe1f9f9bb14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUtNKmcZ4RLXXAhEg3ZhtJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 46859,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 462
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 46859,
          "cache_creation_input_tokens": 462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 462,
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

_source line 40 · 2026-05-20T23:41:42.047Z_

<details><summary>↩ Tool result · `toolu_01RqRWCtnHWuHrDhvzW3d4KH`</summary>

```text
1	---
2	dream_id: dream_20260520T222113
3	tier: best
4	overall_score: weak accept
5	timestamp: 2026-05-20T23:39:21.110041+00:00
6	---
7	
8	# Dream Review Report — Consolidated Roundtable
9	
10	**Paper:** Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
11	
12	**Dream ID:** 20260520T222113  
13	**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)
14	
15	---
16	
17	## Roundtable Process
18	
19	- **R1 focus:** Methodology, experimental design, statistical rigor
20	- **R2 focus:** Novelty, related work positioning, significance/impact
21	- **Step 1 (Independent):** Both reviewers scored **4/6 (Weak Accept)**, high confidence.
22	- **Steps 2–3 (Cross-sharing & Convergence):** See §7 below.
23	- **Step 4 (Synthesis):** This report.
24	
25	---
26	
27	## 1. Paper Summary
28	
29	The paper applies Generalizability Theory (G-theory) to LLM evaluation in a multi-benchmark setting. Three facet classes are crossed: measurement (item_id, 200 stratified-sampled items per benchmark), methodology (prompt template ×6, random seed ×6, temperature ×2–3, option ordering ×4), and infrastructure (numerical precision FP32/BF16/FP16/LayerCast, GPU hardware ×2). Six models (4×7–9B, 2×14B) are evaluated on five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), totaling 4M+ evaluation records. A fine-tuning G-study with RoBERTa-large on four NLU tasks adds cross-paradigm evidence.
30	
31	Three claims:
32	1. **Cross-benchmark variance gradient:** item_id dominance is benchmark-conditional — 56% on MMLU down to 21% on MATH, a 35pp monotonic gradient. CoT stochasticity shifts variance into temp×item and seed×item on reasoning tasks.
33	2. **Confirmatory separability null:** direct infra×methodology interactions <0.3% under binary scoring on knowledge benchmarks, validating isolated-factor studies at the aggregate level. Both factor types interact substantially with items.
34	3. **D-study protocol reversal:** optimal evaluation protocol reverses across task types — MMLU is item-limited (420 items for G≥0.90), GSM8K is seed-limited (10 seeds). Current practice G<0.25 everywhere.
35	
36	---
37	
38	## 2. Novelty Assessment (R2-led, R1-endorsed)
39	
40	### Claim 1 (Cross-benchmark variance gradient): **Moderate-to-high novelty.**
41	The paper's strongest contribution. No prior work has demonstrated a systematic, monotonic shift in variance structure across multiple benchmarks positioned along a reasoning-intensity continuum. The 35pp gradient (MMLU→MATH) with the CoT stochasticity mechanism unifies apparently contradictory conclusions from prior single-benchmark studies (Sclar on prompt sensitivity, Pezeshkpour on ordering, Yuan on precision). The "unifying explanation" framing is well-executed. However, item_id dominance per se is expected from measurement theory (Brennan 2001); the contribution is the quantification and the gradient, not the dominance finding itself.
42	
43	### Claim 2 (Confirmatory separability): **Low novelty, moderate utility.**
44	A confirmatory null. The infrastructure crossing — the paper's methodological advance over Mesting (2026) — yields near-nothing (<0.3% direct interactions). The nuanced decomposition into direct vs. item-conditional interactions (aggregate separability + item-level coupling) adds value but is not a primary novelty claim. R1 further notes that the separability claim is benchmark-conditional: GSM8K and MATH show 2.5–3.0% infra×method, weakening the generality.
45	
46	### Claim 3 (D-study protocol reversal): **Moderate novelty, high practical value.**
47	The facet effectiveness ratio inversion (MMLU items:seeds = 14.2:1, GSM8K = 0.8:1) is non-obvious and actionable. The D-study projection grids are the most practically useful output. The G<0.25 finding is an important indictment of current practice.
48	
49	### Collective Assessment
50	The three claims are stronger together than individually. The gradient explains the protocol reversal; the separability null validates independent factor study. The paper is best understood as a large-scale empirical study applying a well-established framework (G-theory) to a new domain (multi-benchmark LLM evaluation) and discovering a systematic empirical regularity (the gradient). This is a meaningful contribution, not a methodological breakthrough.
51	
52	### Incrementality over Mesting (2026)
53	Clear advance in three dimensions: (a) five benchmarks vs. one, (b) infrastructure crossing, (c) model as crossed facet. The infrastructure crossing yields near-null results, so (b) is confirmatory. The multi-benchmark gradient and model-as-facet analysis are genuine advances. R2 notes that the complementarity with Mesting (who found judge identity dominant at 43.8%) should be discussed more explicitly — this paper fixes the judge and reveals the structure underneath.
54	
55	---
56	
57	## 3. Methodology Assessment (R1-led, R2-endorsed)
58	
59	### 3.1 G-Theory Application
60	**Largely correct.** Model-as-facet (Section 7) properly separates model×item interaction (~10%) from item variance, addressing a key prior concern. Henderson Method III with REML sensitivity check is appropriate for the nearly-balanced crossed designs. Max divergence of ~1.4pp with preserved rankings is reassuring.
61	
62	### 3.2 Critical Methodological Concerns
63	
64	**(a) Binary data in G-theory (R1, Major).** Standard Henderson III / REML assume continuous, approximately normal responses. Binary 0/1 data violates this. Item variance is mechanically linked to item difficulty via the Bernoulli variance function p(1-p), partially inflating item_id dominance. The logprob analysis (Appendix B, item_id = 42.8%) on continuous data is methodologically cleaner and partially mitigates this, but the primary analysis is on binary data. The paper must discuss this limitation. A generalized G-theory approach (Brennan 2001, Ch. 12) or link-function-based decomposition would be more appropriate.
65	
66	**(b) Temperature and ordering as random facets (R1, Major).** With 2–3 temperature levels (specific design points, not random draws) and 4 systematic orderings (cyclic rotations of 24 possible permutations), the exchangeability assumption required for random effects is questionable. Misspecification inflates variance estimates for these facets and their interactions. The paper should either justify the random-effects assumption, treat these as fixed, or present both as sensitivity analysis.
67	
68	**(c) Asymmetric designs across benchmarks (R1, Moderate).** MMLU uses 3 precisions × 3 temperatures; other benchmarks use 2×2. FP32 is absent from non-MMLU experiments. The cross-benchmark precision gradient (MMLU 3.0% → MATH 0.5%) is confounded with different precision levels tested. A BF16/FP16-only MMLU reanalysis for cross-benchmark comparison is needed.
69	
70	**(d) Separability claim overstated (R1, Moderate).** Abstract says "<0.3% under binary scoring" but GSM8K reaches 3.0% and MATH 2.5%. A finding that holds on 3/5 benchmarks is benchmark-conditional, not general. The abstract and conclusions should lead with the conditionality.
71	
72	### 3.3 Experimental Design
73	- **MMLU G-study (1,036,800 records):** Strong. V0 enforce_eager control is excellent experimental hygiene.
74	- **Cross-benchmark (1,382,400 records):** Adequate but reduced design; asymmetry concern above.
75	- **Multi-hardware (691,200 records):** Adequate; 2 GPU types is the minimum, findings are directional.
76	- **Item resampling stability (32,400 records):** Well-designed; CV=4.1% on item_id is reassuring.
77	- **14B extension (345,600 records):** Useful but underpowered (2 models, 1 df for model effects).
78	- **Fine-tuning (1,728 runs):** Adequate for its scope but architecturally distant from the decoder inference setting. Best framed as preliminary evidence.
79	
80	### 3.4 Reproducibility Gaps
81	R1 flags: vLLM version should include commit hash (not just version number); model weight HuggingFace revision hashes needed; exact CUDA/cuDNN/driver versions should be reported; prompt template text should appear in an appendix; item sampling seeds should be released.
82	
83	---
84	
85	## 4. Related Work Assessment (R2-led)
86	
87	The bibliography has improved dramatically from earlier drafts (7→22 references). Four Related Work paragraphs are well-organized. Positioning against prior work is largely fair and accurate.
88	
89	### Missing References (R2)
90	1. **GeneralizIT (Nalisnick et al., 2024)** — G-theory software for ML. Relevant to tooling discussion.
91	2. **Kunievsky et al. (2025)** — prompt sensitivity decomposition into intent/articulation/model uncertainty. Relevant to interpreting prompt×item.
92	3. **Brittlebench (2026)** — prompt brittleness benchmark, ~50% prompt variance. Directly relevant.
93	4. **Bui et al. (2025)** — seed sensitivity in RoBERTa/Llama fine-tuning. Relevant to Section 8.2.
94	5. **ThinkingMachines (2025)** — batch invariance failure (80/1000 unique completions at T=0). Explains why seed×item is non-zero even at T=0; relevant to the vLLM batch nondeterminism concern.
95	
96	### Minor Positioning Issues
97	- The claim that prior ANOVA studies "lack D-study machinery" is technically true but slightly misleading — bootstrap approaches can achieve similar projections; G-theory's advantage is closed-form projection.
98	- Vania et al. (2021) is in the bibliography but not discussed in Related Work text.
99	
100	---
101	
102	## 5. Presentation Assessment (Joint)
103	
104	### Strengths
105	- Clean three-claim structure, well-supported throughout.
106	- "Unifying explanation" framing for the gradient is effective.
107	- Balanced Discussion with thorough Limitations paragraph.
108	- Engine confound discovery presented with appropriate before/after validation.
109	- Honest framing of infrastructure crossing as confirmatory.
110	
111	### Weaknesses
112	- **Zero figures (R2, Major).** This is a serious deficiency for a variance decomposition paper. Stacked-bar charts are an expected field idiom (Mesting 2026). The cross-benchmark gradient, D-study projections, and facet effectiveness inversion all cry out for visualization. With 19 tables and 0 figures, the paper is dense and visually monotonous. This is a competitive disadvantage at a top venue. Easily fixable.
113	- **Title promises "Evaluation Metrics" but delivers only binary scoring (R2, Moderate).** Logprob analysis is a one-paragraph appendix. Either deliver the metric-conditional analysis or adjust the title.
114	- **Fine-tuning section feels bolted on (R2, Moderate).** RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA is architecturally distant from 7–14B decoder inference. Cross-paradigm generalization is weak. Should be explicitly qualified as preliminary.
115	- **No cost analysis for recommended budgets (R2, Minor).** The D-study recommends specific allocations but does not estimate GPU-hour costs. Without cost, the budgets remain theoretical.
116	
117	---
118	
119	## 6. Scope Assessment (Joint)
120	
121	### Adequate for claimed scope
122	- 5 benchmarks spanning knowledge-to-reasoning: sufficient for the gradient claim. Non-overlapping bootstrap CIs provide statistical support.
123	- 4×7–9B models showing consistent per-model patterns: gradient is not a single-model artifact.
124	- 14B extension within the 8B range: scale invariance holds at this increment.
125	
126	### Limitations that should constrain claims
127	- **No 70B+ models.** Larger models may compress item_id through higher accuracy and reduce CoT stochasticity through stronger reasoning. Generality claims should be scoped to 7–14B.
128	- **No proprietary API models.** GPT-4/Claude/Gemini have opaque infrastructure. Separability null may not hold when infrastructure is uncontrolled. Mesting studied API models; this paper studies open-weight models. Complementarity should be discussed.
129	- **No non-English benchmarks.** Tokenization effects on item difficulty could alter cross-lingual variance structure.
130	- **No generation-based benchmarks.** All are multiple-choice or short-answer. Open-ended generation may have fundamentally different variance structures.
131	- **200-item samples.** Resampling stability tested only for MMLU. Other benchmarks lack resampling validation.
132	
133	---
134	
135	## 7. Roundtable: Convergence and Divergence
136	
137	### Full Convergence (Both Reviewers)
138	1. **Score: 4/6 (Weak Accept).** At the acceptance threshold, contingent on addressable revisions.
139	2. **Cross-benchmark gradient is the paper's strongest, most novel contribution.** Well-supported by data, non-overlapping CIs, per-model consistency.
140	3. **Separability null is confirmatory, not novel.** Honest framing is appreciated.
141	4. **D-study budgets are the most practically useful output.** Immediately actionable.
142	5. **Infrastructure crossing yields near-null results.** The claimed advance over Mesting produces confirmatory rather than discovery findings.
143	6. **Fine-tuning extension is architecturally distant.** Should be qualified as preliminary.
144	7. **Zero figures is a serious presentation weakness.** Easily fixable; would materially improve the paper.
145	8. **Scope limited to 7–14B open-weight models.** Claims should be scoped accordingly.
146	9. **Engine confound discovery is a standalone methodological contribution.** Valuable to the community.
147	
148	### Partial Convergence
149	10. **Separability conditionality (R1 raised, R2 endorsed after cross-sharing).** The abstract's "<0.3%" is accurate for knowledge benchmarks but not for GSM8K/MATH. Both reviewers agree the abstract should qualify this.
150	11. **Missing references (R2 raised, R1 endorsed).** Five missing references (GeneralizIT, Kunievsky, Brittlebench, Bui, ThinkingMachines) are relevant and should be added.
151	
152	### R1-Only Concerns (Not Contested by R2)
153	12. **Binary data in G-theory** — a critical methodological point that R2 did not independently flag but endorses as important. The paper's primary analysis uses binary data under methods assuming continuous responses. Must be discussed.
154	13. **Temperature/ordering as random facets** — 2–3 temperature levels and 4 systematic orderings are dubious as random draws. R2 did not raise this but acknowledges the statistical logic.
155	14. **Asymmetric designs across benchmarks** — FP32 absent from non-MMLU experiments confounds cross-benchmark precision comparisons.
156	
157	### R2-Only Concerns (Not Contested by R1)
158	15. **Title/metrics mismatch** — "Evaluation Metrics" in title but only binary scoring in main text. R1 did not flag this but agrees the title should match content.
159	16. **Comparison with IRT approaches** — the D-study budgets should be compared with tinyBenchmarks (Polo et al.) recommendations. What does G-theory add over IRT-based subsampling?
160	17. **Cost analysis for budgets** — GPU-hour estimates would make recommendations concrete.
161	
162	---
163	
164	## 8. Consolidated Strengths
165	
166	1. **Cross-benchmark variance gradient is a genuine, well-supported empirical contribution** that unifies contradictory prior findings. The monotonic 35pp gradient with mechanistic CoT explanation and non-overlapping bootstrap CIs is the paper's signature finding.
167	2. **Massive experimental scale** (4M+ records, 5 benchmarks, 6 models, fully crossed factorial designs). Few empirical papers in this area match the breadth.
168	3. **D-study reproducibility budgets are immediately actionable.** Specific item/prompt/seed allocations for G≥0.90, benchmark-specific, with projection grids.
169	4. **Engine confound discovery and correction** (vLLM V0 vs. V1 routing) is a standalone methodological contribution.
170	5. **Model-as-facet analysis** cleanly separates model×item interaction (~10%) and preserves the gradient after extraction.
171	6. **Honest framing throughout.** Separability as confirmatory, item dominance as psychometrically expected, gradient as directional with quantified uncertainty.
172	7. **Comprehensive robustness checks.** Item resampling stability, REML vs. Henderson III, bootstrap CIs, per-model breakdowns, 14B scale validation.
173	8. **Counter-intuitive G pattern** (knowledge benchmarks yield lower G than reasoning benchmarks) is well-explained and insightful.
174	9. **Current-practice G<0.25** is an important and alarming finding for the field.
175	
176	---
177	
178	## 9. Consolidated Weaknesses
179	
180	### Major
181	1. **Binary data in standard G-theory** without discussion of the methodological limitation. Item_id dominance is partially artifactual from the Bernoulli variance function. Must be addressed in revision.
182	2. **Zero figures in a variance decomposition paper.** 19 tables and 0 figures. Stacked-bar charts, D-study curves, and gradient visualizations are expected idioms. Serious competitive disadvantage at a top venue.
183	3. **Temperature (2–3 levels) and ordering (4 systematic rotations) as random facets** is statistically dubious. Sensitivity analysis with these as fixed effects is needed.
184	
185	### Moderate
186	4. **Asymmetric designs across benchmarks** confound cross-benchmark precision comparisons (FP32 absent from non-MMLU experiments).
187	5. **Separability claim overstated in abstract** — holds on knowledge benchmarks but GSM8K (3.0%) and MATH (2.5%) exceed the stated threshold. Should be qualified.
188	6. **Title promises "Evaluation Metrics" but delivers only binary scoring** in main text. Logprob analysis relegated to one-paragraph appendix.
189	7. **Infrastructure crossing is the claimed advance over Mesting but yields near-null results.** The main findings would emerge from a Mesting-style design with fixed infrastructure.
190	8. **No models above 14B.** Generality cannot be claimed beyond this scale range.
191	9. **Missing references:** GeneralizIT, Kunievsky et al. (2025), Brittlebench (2026), Bui et al. (2025), ThinkingMachines (2025).
192	10. **Fine-tuning extension (RoBERTa-large, encoder-only)** is architecturally distant from decoder inference. Feels appended rather than integrated.
193	
194	### Minor
195	11. No cost analysis for recommended D-study budgets.
196	12. Residual component (6–18%) is underanalyzed; higher-order interactions mentioned but not tabulated.
197	13. 14B extension is underpowered (2 models, 1 df for model effects).
198	14. Item resampling stability tested only for MMLU, not for other benchmarks.
199	15. Prompt template text not provided; reproducibility details (vLLM commit hash, model weight hashes, CUDA versions) insufficient.
200	
201	---
202	
203	## 10. Consolidated Questions for Authors
204	
205	1. **Binary data:** How do you address the assumption violation of applying Henderson III / REML to binary (0/1) responses? Have you considered generalized G-theory or a probit/logit link-function decomposition? Does item_id dominance survive under a method appropriate for binary data?
206	
207	2. **Temperature as random facet:** What justifies treating 2–3 temperature levels (specific design points: 0, 0.5, 1.0) as a random rather than fixed facet? Have you compared results with temperature as fixed?
208	
209	3. **Cross-benchmark precision confound:** Have you re-analyzed MMLU restricted to BF16/FP16 only (excluding FP32) for the cross-benchmark comparison? Does the precision gradient survive with matched precision levels?
210	
211	4. **Gradient under logprob scoring:** Does the full 5-benchmark gradient (MMLU > ARC > HellaSwag > GSM8K > MATH) hold under logprob-based scoring? If not, is the gradient partially an artifact of binary scoring thresholds?
212	
213	5. **Comparison with IRT:** How do the D-study budgets compare to Polo et al.'s tinyBenchmarks recommendations for MMLU? What does G-theory add over IRT-based efficient subsampling?
214	
215	6. **Separability scope:** How confident are you that the separability null extends to more diverse hardware (A100 vs. H100 vs. B200) where architectural differences are more substantial?
216	
217	7. **Judge variance complementarity:** Your entire variance structure sits "underneath" Mesting's judge variance (43.8%). How should practitioners interpret your budgets for LLM-as-judge evaluation? Would the gradient hold if judge were included as a facet?
218	
219	8. **Negative variance estimates:** How are negative Henderson III estimates handled (set to zero, left negative, redistributed)? This affects the separability claim where infra×method components are near zero.
220	
221	9. **D-study optimization procedure:** How were the "optimal" prompt and seed counts determined? Formal cost minimization, or chosen by inspection?
222	
223	10. **Rank instability analysis:** Have you computed what fraction of published leaderboard rankings would change under re-evaluation with different seeds/prompts? This would make G<0.25 more concrete than an abstract coefficient.
224	
225	---
226	
227	## 11. Recommended Revisions (Priority-Ordered)
228	
229	### Must-fix for acceptance
230	1. Add 3–5 figures: (a) cross-benchmark stacked-bar gradient, (b) D-study G vs. total evaluations curves, (c) facet effectiveness ratio visualization, (d) bootstrap CI forest plot.
231	2. Add a paragraph discussing binary data limitations in G-theory estimation and note that logprob scoring provides the methodologically cleaner decomposition.
232	3. Present sensitivity analysis with temperature as fixed facet.
233	4. Qualify separability claim in abstract: "<0.3% on knowledge benchmarks; rises to 2–3% on reasoning benchmarks."
234	
235	### Should-fix
236	5. Re-analyze MMLU at BF16/FP16 only for the cross-benchmark comparison table.
237	6. Add the 5 missing references (GeneralizIT, Kunievsky, Brittlebench, Bui, ThinkingMachines).
238	7. Align title with content: either deliver metric-conditional analysis or remove "Evaluation Metrics" from title.
239	8. Add prompt template text in an appendix; provide vLLM commit hash, model weight hashes.
240	
241	### Nice-to-have
242	9. Extend logprob analysis to all 5 benchmarks to test whether the gradient holds under continuous scoring.
243	10. Add cost estimates (GPU-hours) for recommended D-study budgets.
244	11. Expand higher-order interaction analysis in appendix.
245	
246	---
247	
248	## 12. Overall Assessment
249	
250	### Score: 4/6 (Weak Accept)
251	
252	### Confidence: High
253	
254	### Meta-Review Justification
255	
256	Both reviewers independently scored this paper 4/6 (Weak Accept) with high confidence, and the roundtable did not identify grounds to change this. The cross-benchmark variance gradient is a genuine novel finding: no prior work has demonstrated the systematic shift from item-dominated (knowledge tasks) to interaction-dominated (reasoning tasks) variance structure, and the 35pp gradient with non-overlapping bootstrap CIs is well-supported. The D-study reproducibility budgets fill a real practical gap, and the G<0.25 indictment of current practice is alarming and important.
257	
258	The paper is held back by addressable issues: (a) zero figures is a serious presentation weakness at a top venue; (b) binary data in standard G-theory requires explicit discussion; (c) temperature/ordering as random facets needs sensitivity analysis; and (d) the separability claim needs scoping. None of these are fatal. If the must-fix revisions are made — especially adding figures and the binary data discussion — the paper would likely move to 5/6 (Accept).
259	
260	The infrastructure crossing, positioned as the key methodological advance over Mesting, yields near-null results. This is intellectually honest (confirmatory null) but means the paper's primary novelty rests on the cross-benchmark gradient and D-study budgets rather than on the infrastructure-methodology crossing. Both reviewers agree this is sufficient for a top venue, given the scale of the empirical contribution and the practical utility of the findings.
261	
262	**Bottom line:** A well-executed, large-scale empirical study with a genuine novel finding (the gradient), actionable outputs (D-study budgets), and an important policy implication (G<0.25). At the acceptance threshold; fixable revisions would push it to a clear accept.
263	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dad43e8-f15f-4a61-9a41-dfe1f9f9bb14",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "4aa0796e-ff5a-4a2f-ae48-47160838b981",
  "sourceToolAssistantUUID": "5dad43e8-f15f-4a61-9a41-dfe1f9f9bb14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T23:41:46.030Z_

Now I have a comprehensive understanding of the paper, the prior review, and the literature. Let me now check the median tier review as well for additional context, then produce my focused R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aa0796e-ff5a-4a2f-ae48-47160838b981",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhuQy3Qg78jb9NpLw5A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03bff418-f79d-42ab-91ad-9fb45a223656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154S7K15ahtc46bK8arA1Sq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6761,
      "cache_read_input_tokens": 47321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6761,
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

_source line 42 · 2026-05-20T23:41:48.016Z_

<details open><summary>🔧 Tool call — Read · `toolu_015tEFodob6VbW4JhJ6bgCVs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/review_report.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03bff418-f79d-42ab-91ad-9fb45a223656",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhuQy3Qg78jb9NpLw5A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e6d4f85-2bb7-4edc-90c5-9c4cbaad70e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154S7K15ahtc46bK8arA1Sq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6761,
      "cache_read_input_tokens": 47321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6761,
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

_source line 43 · 2026-05-20T23:41:48.023Z_

<details><summary>↩ Tool result · `toolu_015tEFodob6VbW4JhJ6bgCVs`</summary>

```text
1	---
2	dream_id: dream_20260520T222113
3	tier: median
4	overall_score: weak accept
5	timestamp: 2026-05-20T23:36:13.189748+00:00
6	---
7	
8	---
9	dream_id: dream_20260520T222113
10	tier: median
11	overall_score: weak accept
12	timestamp: 2026-05-20T23:45:00+00:00
13	---
14	
15	# Dream Review Report — R1 (Methodology & Experimental Rigor)
16	
17	**Paper:** Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
18	
19	**Tier:** Median
20	
21	**Review mode:** R1 focus — Methodology, Experimental Design, Statistical Rigor
22	
23	---
24	
25	## 1. Paper Summary
26	
27	The paper applies Generalizability Theory (G-theory) to LLM evaluation, conducting multi-benchmark crossed-facet variance decompositions across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (4x7-9B + 2x14B), two GPU architectures, and multiple levels of precision, prompt template, seed, temperature, and answer ordering. Over 3 million evaluation records are analyzed. Three claims are made: (1) a benchmark-conditional variance gradient where item dominance ranges from 48% (MMLU) to 28% (MATH) under model-as-facet analysis; (2) infrastructure x methodology separability at the aggregate level (<0.5% on knowledge benchmarks, rising to 3% on math-generation benchmarks); (3) metric-conditional, benchmark-specific reproducibility budgets via D-study projections. Extensions cover 14B models, RoBERTa fine-tuning, LayerCast precision mitigation, and three scoring metrics.
28	
29	---
30	
31	## 2. Methodological Soundness
32	
33	### 2.1 G-Theory Framework Application
34	
35	**Largely correct, with one significant improvement over Dream #1.** The revised paper treats model as a crossed random facet (Section 4.4 / Table 5), which was the most critical methodological concern in the prior review. This properly separates model×item interaction (16-22%) from pure item variance and residual. The 4pp systematic reduction across all benchmarks is plausible and consistent with psychometric expectation when objects of measurement have heterogeneous difficulty profiles.
36	
37	**Henderson Method III vs. REML.** The paper uses Henderson Method III (expected mean squares) as primary estimation with REML as sensitivity check. This is defensible: Henderson III is unbiased for balanced designs, and the design is nearly balanced (fully crossed within each experiment). The reported max divergence of 2.1pp with preserved rank ordering is reassuring. However:
38	
39	- **Concern:** Henderson Method III can produce negative variance component estimates for near-zero components. The MATH table (Table 22 in the imagined experiments) shows a negative "other" entry (-1.5%), which is characteristic of this issue. The paper should explicitly state how negative estimates are handled (set to zero? redistributed? left as-is?). This matters for the separability claim where infra×method components are near zero — a negative estimate truncated to zero looks different from a genuinely zero estimate.
40	
41	- **Concern:** The G-theory formula presented in Equation 2 is simplified. The actual D-study formula for a multi-facet crossed design with 5+ facets involves many more terms. The paper should either present the full formula used or cite a specific implementation (e.g., GeneralizIT package). The simplified formula risks misleading readers about how D-study projections were actually computed.
42	
43	### 2.2 Crossed Random-Effects Assumptions
44	
45	**Items as random facet:** Justified. The 200 items per benchmark are sampled (stratified) from larger pools (MMLU: 14,042; ARC: 2,590; GSM8K: 1,319; HellaSwag: 10,042; MATH: 5,000). The random-facet assumption requires that observed items are exchangeable draws from a universe of admissible observations. Stratified sampling strengthens this by ensuring subject/topic coverage.
46	
47	**Model as random facet:** Partially justified. Four 7-9B models from different families (Qwen, Llama, Gemma, Mistral) are treated as exchangeable draws from the universe of "7-9B instruction-tuned LLMs." This is defensible but arguable — the model universe is not well-defined, and four models provide limited degrees of freedom for estimating model-related variance components. The 14B extension (2 models) is even more constrained. The paper should acknowledge that model-as-facet with k=4 yields imprecise estimates of model variance components and that the model universe is narrowly defined (open-weight, instruction-tuned, 7-9B).
48	
49	**Prompt as random facet:** The 6 prompt templates are described but their generation process matters for the random-effects assumption. If they were systematically designed to vary specific dimensions (e.g., formality, instruction explicitness), they may not represent random draws from a prompt universe. The paper should clarify whether prompt templates were generated to be representative (supporting random effects) or to maximize diversity (which biases variance estimates upward).
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e6d4f85-2bb7-4edc-90c5-9c4cbaad70e7",
  "isSidechain": true,
  "promptId": "4ce4be9f-1837-42a7-84fc-5f176198b944",
  "agentId": "a4f148f2fd0307ae6",
  "type": "user",
  "uuid": "e970e4a8-296d-448b-ac0d-2204a18a24f6",
  "sourceToolAssistantUUID": "1e6d4f85-2bb7-4edc-90c5-9c4cbaad70e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T23:43:24.461Z_

I now have a thorough understanding of the paper and prior reviews. Let me compose the R2 review focused on novelty and related work.

## R2 Review: Novelty & Related Work

### Summary

The paper applies Generalizability Theory (G-theory) to multi-benchmark LLM evaluation, crossing infrastructure facets (precision, hardware) with methodology facets (prompt, seed, temperature, ordering) and measurement (item) across 5 benchmarks, 6 models, and 4M+ records. The three claimed contributions are: (1) a cross-benchmark variance gradient where item dominance drops monotonically from 56% (MMLU) to 21% (MATH), (2) a confirmatory separability null for infrastructure x methodology interactions (<0.3% under binary scoring), and (3) benchmark-specific D-study reproducibility budgets revealing that current practice yields G<0.25 everywhere. The paper also includes a fine-tuning G-study with RoBERTa-large and a 14B scale validation.

### Strengths

1. **The cross-benchmark variance gradient is the paper's genuine novel contribution and it is well-executed.** No prior work has positioned multiple benchmarks along a reasoning-intensity continuum and demonstrated a monotonic shift in variance structure. The 35pp item_id gradient (MMLU 56% to MATH 21%) with non-overlapping bootstrap CIs is statistically rigorous. More importantly, the "unifying explanation" framing -- that prior single-benchmark studies (Sclar on prompts, Pezeshkpour on ordering, Yuan on precision) reached seemingly contradictory conclusions because they studied benchmarks at different positions on the gradient -- is genuinely insightful and advances the field's understanding.

2. **The facet effectiveness ratio inversion is non-obvious and actionable.** The finding that MMLU is item-limited (items:seeds = 14.2:1) while GSM8K is seed-limited (0.8:1) is not something a practitioner would predict a priori. This directly challenges the common assumption that evaluation protocols can be standardized across benchmarks. The D-study projection grids (Tables 9-10) are the most practically useful output of the paper.

3. **Honest positioning of contributions.** The paper correctly frames the separability null as confirmatory rather than as a novelty claim, acknowledges that item dominance is expected from measurement theory (Brennan 2001), and explicitly scopes the infrastructure facet to numerical precision. This intellectual honesty is uncommon and appreciated. The engine confound discovery (vLLM V0 vs V1 routing) and its correction is a standalone methodological contribution that will save other researchers from the same pitfall.

4. **Scale and thoroughness of the empirical study.** 4M+ evaluation records, 5 benchmarks, 6 models, 4 methodology facets, 2 infrastructure facets, per-model breakdowns, item resampling stability, REML sensitivity checks, bootstrap CIs, and 14B scale validation. This is a substantially more comprehensive study than Mesting (2026, single benchmark) or any prior isolated-factor study.

5. **The G<0.25 finding is an important indictment.** Framing current standard practice (1 prompt, 1 seed, <=200 items) as producing measurement reliability below the minimum threshold accepted in any measurement discipline is alarming and should motivate the community.

6. **Clear three-claim structure with well-differentiated contributions.** Each claim maps to specific tables and sections, making the paper's logic easy to follow despite its density.

### Weaknesses

1. **The infrastructure crossing -- the claimed methodological advance over Mesting (2026) -- yields near-null results, making the paper's novelty narrative somewhat hollow (Section 6, p.6-7).** The paper's introduction frames "crossing infrastructure with methodology in a unified G-theory framework" as a key gap filled. But the infrastructure x methodology interaction is <0.3%, meaning this crossing contributes essentially nothing to our understanding. The paper's three genuine findings -- the gradient, the D-study reversal, and the G<0.25 indictment -- would all emerge from a Mesting-style methodology-only design replicated across 5 benchmarks. This raises the question: is the infrastructure crossing a genuine contribution or an expensive null that consumed compute without advancing knowledge? The paper should forthrightly address this in the Discussion. The confirmatory null has value (it validates isolated-factor studies), but the paper currently oversells it relative to its import.

2. **Missing critical related work weakens the positioning (Section 2).** Several directly relevant papers are absent:
   - **Brittlebench (2026)**: Reports ~50% variance from prompt perturbations with a perturbation protocol. Directly relevant to the prompt facet and omitted from text (only Mizrahi/Sclar cited for prompt sensitivity).
   - **ThinkingMachines (2025)**: Documents 80/1000 unique completions at T=0 from batch-invariance failure in RMSNorm/GEMM/attention kernels. Directly relevant to the seed x item interaction at T=0 and to the vLLM infrastructure discussion. This reference would strengthen the mechanistic explanation for why seed effects are non-zero even at T=0.
   - **Messina & Scotta (2026)**: The "background temperature" formalization. Listed in the bibliography but cited only tangentially in the paper_framing document; the actual paper text cites them once without engaging with the T_bg framework.
   - **Kunievsky & Evans (2025)**: Alternative variance decomposition (intent/articulation/model uncertainty). Relevant as a competing framework that would enrich the Related Work discussion.
   - **GeneralizIT (2024)**: The Python G-theory software. If used, should be cited; if not, should be discussed as a tooling reference.
   - **Bui et al. (2025)**: Seed sensitivity in fine-tuning (RTES variance=18.22). Directly relevant to the fine-tuning G-study in Section 8.2.

3. **The "first multi-benchmark G-theory analysis" claim needs careful qualification (Section 1, Contributions).** Bouthillier et al. (2021) performed ANOVA-based variance decomposition across multiple ML benchmarks (ImageNet, CIFAR, etc.) with multiple facets. The paper positions this as "ANOVA, not G-theory" -- technically correct, but ANOVA and G-theory share the same variance decomposition; the difference is D-study projections. Mesting (2026) applied G-theory to LLM evaluation on one benchmark. The paper's claim is thus "first G-theory (not ANOVA) applied to LLM evaluation (not ML generally) across multiple benchmarks." This is a narrow novelty window that the paper should state more precisely. A reviewer less charitable than me would call this incremental.

4. **The three-tier benchmark clustering (knowledge / commonsense / reasoning) is post-hoc and lacks external validation (Section 5).** The gradient is presented as a monotonic continuum, but the benchmark ordering (MMLU > ARC > HellaSwag > GSM8K > MATH) was chosen by the authors, presumably after observing the results. An independent measure of "reasoning intensity" -- such as average chain-of-thought length, number of reasoning steps, or an IRT-derived difficulty parameter -- would make the continuum principled rather than constructed. Without this, the gradient could be an artifact of the specific 5 benchmarks selected, and a 6th benchmark might not fall on the line.

5. **Comparison with IRT-based approaches is superficial (Section 2, paragraph 4).** The paper claims D-study budgets are "directly comparable to IRT-based subsampling recommendations" (Polo et al., tinyBenchmarks) but never actually compares them. What does tinyBenchmarks recommend for MMLU -- and how does it differ from the G-theory prescription of 420 items? If they agree, G-theory is confirmatory; if they disagree, the paper must explain why. This is a missed opportunity to demonstrate G-theory's added value over an established, widely-adopted approach.

6. **Zero figures is a critical presentation failure for a variance decomposition paper.** 15-19 tables and no figures. Stacked-bar variance decomposition charts are the expected field idiom (Mesting 2026, Brittlebench 2026). The cross-benchmark gradient practically demands a visual: the 35pp monotonic decline would be immediately legible in a stacked-bar chart ordered by benchmark. D-study projection curves (G vs. facet sample size) would communicate the protocol reversal far more effectively than projection grids in tables. At a top venue with 25% acceptance rate, this is a significant competitive disadvantage.

7. **The fine-tuning G-study (Section 8.2) feels architecturally disjoint.** RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA is methodologically distant from 7-14B decoder inference-time evaluation. The facets differ (learning rate and data shuffle replace prompt template and temperature), the architecture differs (encoder-only vs. decoder), and the paradigm differs (training vs. inference). The finding that "item_id is rank-1 in fine-tuning too" is interesting but not surprising -- it would be surprising if item difficulty did not dominate in any measurement scenario. The cross-paradigm generalization claimed is weak and should be explicitly qualified as preliminary evidence, not as a contribution on par with the main findings.

### Questions for Authors

1. **Gradient robustness**: If you added a 6th benchmark (e.g., GPQA, TruthfulQA, or HumanEval), would it fall on the monotonic gradient line? What is your prediction, and what would it mean for the gradient claim if it did not?

2. **Gradient mechanism**: You attribute the shift to chain-of-thought stochasticity, but HellaSwag (commonsense completion) does not typically involve explicit CoT. What mechanism drives the gradient for HellaSwag specifically?

3. **IRT comparison**: For MMLU specifically, Polo et al. (2024) recommend ~100 items via IRT-based subsampling. Your D-study recommends 420 items for G>=0.90. Can you explain this 4x discrepancy? Are these answering different questions?

4. **Judge variance interaction**: Mesting (2026) found judge identity dominates at 43.8%. Your entire variance structure sits "underneath" this. If a practitioner uses LLM-as-judge evaluation, do your D-study budgets still apply, or are they overwhelmed by judge variance?

5. **Incremental over Mesting**: If Mesting had replicated their study on 5 benchmarks instead of 1, they would have discovered the same gradient (since infrastructure contributes <0.3%). What does the infrastructure crossing add beyond a confirmatory null?

6. **Counter-intuitive G pattern**: You note that knowledge benchmarks yield lower G than reasoning benchmarks (MMLU 0.36 vs GSM8K 0.55). Is this because the G coefficient is dominated by item sampling error on MMLU? If so, this is a feature of G-theory's definition rather than a property of the benchmarks themselves. Can you disentangle?

7. **Negative variance estimates**: How are Henderson III negative estimates handled for near-zero components? This directly affects the separability claim.

### Minor Issues

1. The bibliography contains 22 references. The paper_framing document targets 25+. Several of the missing references listed above would bring this closer to adequate coverage for a venue submission.

2. Vania et al. (2021) appears in the bibliography but is not discussed in the Related Work text.

3. The title includes "Evaluation Metrics" (plural) but the main analysis uses only binary correct scoring. The logprob analysis is a single paragraph in Discussion. Either deliver the metric-conditional analysis promised by the title or revise the title.

4. Table density: 15+ tables in 10 pages is extremely dense. Several tables (e.g., Tables 3 and 4 on per-model breakdowns) could be consolidated or moved to an appendix without losing main-text narrative.

5. The claim "over 4 million evaluation records" in the abstract should be verified against the sum of reported records: MMLU (1,036,800) + cross-benchmark (1,382,400) + hardware (691,200) + 14B (345,600) + fine-tuning (records unclear) + MATH (460,800) + LayerCast (172,800) = ~4.1M. The accounting is plausible but should be presented explicitly.

6. Section 3.3 mentions "V0 engine in enforce_eager mode" without defining these vLLM-specific terms for readers unfamiliar with vLLM internals.

### Score: 4/6
### Confidence: 4/5

**Rationale**: The cross-benchmark variance gradient is a genuine empirical contribution that advances the field's understanding of LLM evaluation variance. The D-study budgets are practically useful and the G<0.25 finding is important. However, the paper's claimed methodological advance over Mesting (infrastructure crossing) yields near-null results, meaning the novelty rests primarily on replicating a known methodology across more benchmarks and discovering an empirical regularity -- valuable, but not a methodological contribution. Missing related work, zero figures, a somewhat post-hoc gradient construction, and the absence of a direct IRT comparison weaken the presentation. With figures added, missing references incorporated, and the gradient externally validated, this would move to a clear 5/6. As submitted, it sits at the acceptance threshold.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e970e4a8-296d-448b-ac0d-2204a18a24f6",
  "isSidechain": true,
  "agentId": "a4f148f2fd0307ae6",
  "requestId": "req_011CbEhuuNLe7qt17RBSxRtq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5d9c7fc-26cb-437b-93cf-cf6a35a08abb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "7a1cd9cb-5673-4b3d-b760-963c998bdaf6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TUPXXpxZnS8ZTrHbnAXrH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 54082,
      "output_tokens": 3203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3203,
          "cache_read_input_tokens": 54082,
          "cache_creation_input_tokens": 1624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1624,
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
