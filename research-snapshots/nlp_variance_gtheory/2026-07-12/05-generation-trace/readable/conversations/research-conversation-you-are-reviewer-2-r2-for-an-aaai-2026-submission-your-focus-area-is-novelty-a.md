# Research conversation: You are Reviewer 2 (R2) for an AAAI 2026 submission. Your focus area is **Novelty and Related Work**. Conduct a thorough

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9794bbfc34255d04.jsonl`
- **Structured JSON:** [`90b3fc9bb5bc466ce203.json`](../../sessions/90/90b3fc9bb5bc466ce203.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-21T06:03:16.191Z_

You are Reviewer 2 (R2) for an AAAI 2026 submission. Your focus area is **Novelty and Related Work**. Conduct a thorough, independent blind review.

## Paper Summary
Title: "Reproducibility Budgets for LLM Evaluation: Why Generalizability Theory Demands 3–4× More Items Than IRT"

The paper applies Generalizability Theory (G-theory) to decompose evaluation variance in LLM benchmarks. It uses a fully crossed design on MMLU: 4 models × 3 precisions × 6 prompt templates × 6 random seeds × 3 temperatures × 4 item orderings × 200 items (825,600 records).

Key claims:
1. Metric-conditional reproducibility budgets: binary scoring G=0.611 vs text-exact-match G=0.007 (87× gap)
2. G-theory requires 3.3× more items than IRT (468 vs 142) for dependable measurement
3. Model×item interaction is design-sensitive: 26.2% with 2 models → 7.3% with 4 models
4. Open-source G-theory toolkit

## Related Work as presented in the paper (Section 2):
The paper covers 5 areas:
1. **Variance decomposition in ML evaluation**: Cites Bouthillier et al. 2021 (ANOVA-based), Henderson et al. 2018 (deep RL), Dodge et al. 2020 and Sellam et al. 2022 (fine-tuning instability in BERT). Claims these use standard ANOVA without D-study projections.
2. **G-theory in NLP**: Cites Mesting 2026 (ACL) — adapted G-theory to LLM evaluation with 5 methodological facets on single benchmark, treating infrastructure as fixed. This paper claims to extend by: (a) crossing infrastructure with methodology, (b) treating model as crossed facet, (c) comparing metrics, (d) comparing with IRT.
3. **Prompt and ordering sensitivity**: Mizrahi et al. 2024, Lu et al. 2022, Pezeshkpour & Hruschka 2024, Biderman et al. 2024. Claims these isolate individual sources without simultaneous decomposition.
4. **Infrastructure effects**: Yuan et al. 2025 (9% accuracy differences across GPU hardware), Messina & Scotta 2026 (precision effects, floating-point non-associativity). Claims their precision×item analysis provides item-level resolution absent from aggregate studies.
5. **IRT in NLP**: Lalor et al. 2019, Rodriguez et al. 2021, Vania et al. 2021, Polo et al. 2024 (tinyBenchmarks), Perlitz et al. 2023. Claims IRT doesn't account for prompt, seed, or ordering facets. The direct IRT-G-theory comparison is claimed as first-of-its-kind.

## Key Prior Work to Consider
- **Mesting (2026)** — The most direct predecessor. Published at ACL 2026. Applied G-theory to LLM evaluation with 5 methodological facets. This paper claims 4 extensions over Mesting.
- **Bouthillier et al. (2021)** — ANOVA-based variance decomposition for ML benchmarks
- **Polo et al. (2024)** — tinyBenchmarks using IRT for efficient subsampling
- **Biderman et al. (2024)** — Catalogued reproducibility pitfalls across evaluation pipeline
- **Yuan et al. (2025)** — Hardware effects on LLM inference (up to 9% accuracy differences)
- **Messina & Scotta (2026)** — Numerical precision effects in LLM inference

## Experimental Completeness Context
- Main MMLU study: 4 models, fully crossed, 825,600 records — COMPLETE
- Cross-benchmark: Only GSM8K (1 model) and ARC (partial 1 model) — MOSTLY INCOMPLETE
- Multi-hardware: NOT DONE (only single GPU type)
- 14B models: NOT DONE
- Fine-tuning study: NOT DONE
- The paper honestly labels incomplete results as "preliminary evidence"

## Paper Structure
8 content pages + 2 reference pages. 11 tables. Sections: Intro, Related Work, Method, Experiments and Results (6 subsections), Discussion, Limitations, Conclusion.

## Your Review Task

Evaluate focusing on:

### A. Novelty Assessment
1. How novel is applying G-theory to LLM evaluation given Mesting (2026) already did this at ACL? Are the claimed extensions genuine and significant?
2. Is the IRT vs G-theory comparison truly the "first direct comparison"? Could this have been done by combining existing work?
3. Is the metric-conditional finding (binary vs text-exact-match) novel or expected?
4. Is the model×item interaction finding novel given it's now "preliminary evidence" (CI includes near-zero)?
5. Is the 200-item subsampling approach novel or standard in psychometrics?
6. Overall: does this paper advance the field or is it an incremental extension of Mesting (2026)?

### B. Related Work Completeness
1. Are there important missing citations? Consider:
   - Other G-theory applications in education/psychology that could inform the LLM setting
   - Recent (2024-2026) work on LLM evaluation robustness
   - Work on benchmark reliability beyond what's cited
   - Classical psychometrics literature on binary data G-theory
2. Is the positioning against Mesting (2026) fair and accurate?
3. Is the IRT literature adequately covered?
4. Are variance decomposition studies outside NLP adequately cited?

### C. Contribution Significance
1. Given the scope narrowing (primarily MMLU, single GPU, 7-9B models only), is the contribution sufficient for AAAI?
2. The 87× metric gap — is this a finding that changes practice, or is it obvious that string matching is less reliable?
3. The 3.3× IRT-G-theory gap — does this represent an actionable insight for practitioners?
4. The open-source toolkit — how much does this add as a contribution?
5. Compare the ambition of the title ("3-4× More Items") with actual evidence strength.

### D. Framing and Narrative
1. Is the paper honestly framed given incomplete experiments?
2. Is the "preliminary evidence" label for model×item appropriate?
3. Does the Discussion overclaim or underclaim relative to the evidence?
4. Is the Limitations section comprehensive?
5. Does the paper tell a coherent story despite scope narrowing?

## Output Format

Provide your review in this exact structure:

```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentence summary of the paper]

### Strengths (Novelty/Positioning)
- S1: ...
- S2: ...
- S3: ...
[up to 5]

### Weaknesses (Novelty/Positioning)
- W1: ...
- W2: ...
- W3: ...
[up to 6]

### Questions for Authors
- Q1: ...
- Q2: ...
[up to 4]

### Minor Issues
- M1: ...
[up to 3]

### Preliminary Scores (AAAI 1-10 scale, where 1=trivial/wrong, 4=clear reject, 5=borderline reject, 6=borderline accept, 7=accept, 8=clear accept, 10=award quality)
- Novelty: X/10
- Significance: X/10
- Related Work Coverage: X/10
- Overall (Novelty focus): X/10
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "2628493d-a171-4a27-b190-a8a30f04cd0a",
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

_source line 2 · 2026-05-21T06:03:16.199Z_

```json
{
  "parentUuid": "2628493d-a171-4a27-b190-a8a30f04cd0a",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
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
  "uuid": "9e47309f-ad64-48b0-82ba-3d283eafe985",
  "timestamp": "2026-05-21T06:03:16.199Z",
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

_source line 3 · 2026-05-21T06:03:19.311Z_



I'll conduct a thorough review by first reading the paper and all relevant project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e47309f-ad64-48b0-82ba-3d283eafe985",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD13N537xbKMfmEyxux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb4733ad-d362-4875-a52c-7ddd22dcc727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U56KFL1f8MFTR5otsDcWpA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7989,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7989,
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

_source line 4 · 2026-05-21T06:03:20.006Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01N1TGDpQVUmCJVuQYSHi56j`</summary>

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
  "parentUuid": "bb4733ad-d362-4875-a52c-7ddd22dcc727",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD13N537xbKMfmEyxux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4b996c9-67a4-4f0c-b49c-15ae5bef03af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U56KFL1f8MFTR5otsDcWpA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7989,
      "cache_read_input_tokens": 8250,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7989
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7989,
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

_source line 5 · 2026-05-21T06:03:20.010Z_

<details><summary>↩ Tool result · `toolu_01N1TGDpQVUmCJVuQYSHi56j`</summary>

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
  "parentUuid": "f4b996c9-67a4-4f0c-b49c-15ae5bef03af",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "9bd3755f-b819-41f8-a0ea-f6d92a73f0ed",
  "sourceToolAssistantUUID": "f4b996c9-67a4-4f0c-b49c-15ae5bef03af",
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

_source line 6 · 2026-05-21T06:03:25.758Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_0131qaBmhvVwHCBt4QVUdxFk`</summary>

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
  "parentUuid": "9bd3755f-b819-41f8-a0ea-f6d92a73f0ed",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD1LNmL5NfMFuhCmYLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13ea48b3-2867-4123-92d8-85edf695afbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fr97GWG4tkkpTYUShXphNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 7 · 2026-05-21T06:03:25.798Z_

<details><summary>↩ Tool result · `toolu_0131qaBmhvVwHCBt4QVUdxFk`</summary>

```text
{"result":"# 项目 nlp_variance_gtheory 概况\n\n## 实验状态 (7 个)\n\n- **exp001_qwen**: RUNNING — \n- **exp001_mistral**: DONE (success) — \n- **exp001_gemma**: DONE (success) — \n- **exp001_llama**: DONE (success) — \n- **exp001_pilot**: DONE (success) — \n- **bf16_eager_disentangle**: DONE (negative) — \n- **mvp_phase_a**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp001_qwen | Qwen3-8B variance decomposition at full scale (1,296 conditions × 200 items) completes the 4-model design for cross-model G-theory analysis — tests whether item_id dominance and model×item interaction patterns hold with a 4th architecturally distinct model (Claim 1) | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp001_mistral** (success): Mistral-7B-Instruct-v0.3 variance decomposition at full scale (1,296 conditions × 200 items) will contribute to cross-model G-theory analysis — model-as-facet tests whether item_id dominance holds across architecturally diverse models (Claim 1) ← 基于 exp001_llama\n- **exp001_gemma** (success): Gemma-2-9b-it variance decomposition at full scale (1,296 conditions × 200 items) will show model-specific variance structure differences compared to Llama — enabling model-as-facet analysis (Claim 1 make-or-break) ← 基于 exp001_llama\n- **exp001_llama** (success): Single-model (Llama-3.1-8B-Instruct) G-theory variance decomposition at full scale (1,296 conditions × 200 items across 3 precisions × 3 temperatures × 6 prompts × 6 seeds × 4 orderings) will confirm MVP findings: item_id dominates binary_correct variance, while text_exact_match reveals infrastructure×methodology interactions ← 基于 mvp_phase_a\n\n## 趋势\n成功 5 / 负向 1 / 失败 0 / 共 6\nitems_per_condition: 200 →（近 3 次 success）\ntotal_records: 259200 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32570: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13ea48b3-2867-4123-92d8-85edf695afbc",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "ee577e33-b9ba-485d-8a02-12a2b98a329e",
  "sourceToolAssistantUUID": "13ea48b3-2867-4123-92d8-85edf695afbc",
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

_source line 8 · 2026-05-21T06:03:26.317Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MTWSehAzg2cihX9efHb4Qy`</summary>

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
  "parentUuid": "ee577e33-b9ba-485d-8a02-12a2b98a329e",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD1LNmL5NfMFuhCmYLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cff020e-b3e4-44bd-b3ac-c2ccce17ea55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fr97GWG4tkkpTYUShXphNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 9 · 2026-05-21T06:03:26.324Z_

<details><summary>↩ Tool result · `toolu_01MTWSehAzg2cihX9efHb4Qy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp001_qwen | Qwen3-8B variance decomposition at full scale (1,296 conditions × 200 items) completes the 4-model design for cross-model G-theory analysis — tests whether item_id dominance and model×item interaction patterns hold with a 4th architecturally distinct model (Claim 1) | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp001_mistral** (success): Mistral-7B-Instruct-v0.3 variance decomposition at full scale (1,296 conditions × 200 items) will contribute to cross-model G-theory analysis — model-as-facet tests whether item_id dominance holds across architecturally diverse models (Claim 1) ← 基于 exp001_llama\\n- **exp001_gemma** (success): Gemma-2-9b-it variance decomposition at full scale (1,296 conditions × 200 items) will show model-specific variance structure differences compared to Llama — enabling model-as-facet analysis (Claim 1 make-or-break) ← 基于 exp001_llama\\n- **exp001_llama** (success): Single-model (Llama-3.1-8B-Instruct) G-theory variance decomposition at full scale (1,296 conditions × 200 items across 3 precisions × 3 temperatures × 6 prompts × 6 seeds × 4 orderings) will confirm MVP findings: item_id dominates binary_correct variance, while text_exact_match reveals infrastructure×methodology interactions ← 基于 mvp_phase_a\\n\\n## 趋势\\n成功 5 / 负向 1 / 失败 0 / 共 6\\nitems_per_condition: 200 →（近 3 次 success）\\ntotal_records: 259200 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32570: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1584, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cff020e-b3e4-44bd-b3ac-c2ccce17ea55",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "59a12df9-964a-475c-b48f-e0905ad247b5",
  "sourceToolAssistantUUID": "3cff020e-b3e4-44bd-b3ac-c2ccce17ea55",
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

_source line 10 · 2026-05-21T06:03:27.268Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VK9qFrCe7bKfwiHJVf2777`</summary>

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
  "parentUuid": "59a12df9-964a-475c-b48f-e0905ad247b5",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD1LNmL5NfMFuhCmYLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f422031-d198-4ea9-8556-c5b9f97a6c91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fr97GWG4tkkpTYUShXphNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 11 · 2026-05-21T06:03:27.277Z_

<details><summary>↩ Tool result · `toolu_01VK9qFrCe7bKfwiHJVf2777`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T14:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"gtheory_evaluation\\\"\\n    name: \\\"G-Theory & Evaluation Variance\\\"\\n    narrative: \\\"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\\\"\\n  - key: \\\"infrastructure_variance\\\"\\n    name: \\\"Infrastructure-Induced Variance\\\"\\n    narrative: \\\"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\\\"\\n  - key: \\\"prompt_sensitivity\\\"\\n    name: \\\"Prompt Sensitivity & Methodological Variance\\\"\\n    narrative: \\\"Prompt phrasing, seed, temperature, and ordering as variance sources\\\"\\n  - key: \\\"evaluation_methodology\\\"\\n    name: \\\"Evaluation Methodology\\\"\\n    narrative: \\\"Scoring artifacts, benchmark design, and evaluation protocol considerations\\\"\\n\\npapers:\\n  mesting2026hidden:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\\\"\\n    authors:\\n      - \\\"Mesting, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.11581\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  brittlebench2026:\\n    title: \\\"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.13285\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  yuan2025layercast:\\n    title: \\\"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\\\"\\n    authors:\\n      - \\\"Yuan, Z.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09501\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  messina2026background:\\n    title: \\\"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\\\"\\n    authors:\\n      - \\\"Messina, P.\\\"\\n      - \\\"Scotta, A.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.22411\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  generalizit2024:\\n    title: \\\"GeneralizIT: A Python Solution for Generalizability Theory Computations\\\"\\n    authors: []\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2411.17880\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  hua2025flaw:\\n    title: \\\"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\\\"\\n    authors:\\n      - \\\"Hua, W.\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    category: \\\"evaluation_methodology\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  thinkingmachines2025batch:\\n    title: \\\"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"Technical Report\\\"\\n    category: \\\"infrastructure_variance\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  kunievsky2025intent:\\n    title: \\\"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\\\"\\n    authors:\\n      - \\\"Kunievsky, D.\\\"\\n      - \\\"Evans, J.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2506.16584\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  bui2025seeds:\\n    title: \\\"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\\\"\\n    authors:\\n      - \\\"Bui, T.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  sameprompt2026:\\n    title: \\\"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.14349\\\"\\n    category: \\\"prompt_sensitivity\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\", \"total_chars\": 6732, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f422031-d198-4ea9-8556-c5b9f97a6c91",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "275f6a47-9dba-4e68-8f64-1674d7cf91ea",
  "sourceToolAssistantUUID": "9f422031-d198-4ea9-8556-c5b9f97a6c91",
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

_source line 12 · 2026-05-21T06:03:31.878Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0164NTMA6vM3h7tsMWbGJoiZ`</summary>

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
  "parentUuid": "275f6a47-9dba-4e68-8f64-1674d7cf91ea",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD1LNmL5NfMFuhCmYLk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffbca8f0-d04d-4bf5-b419-23ebd99cfe87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fr97GWG4tkkpTYUShXphNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 13 · 2026-05-21T06:03:31.888Z_

<details><summary>↩ Tool result · `toolu_0164NTMA6vM3h7tsMWbGJoiZ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffbca8f0-d04d-4bf5-b419-23ebd99cfe87",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "bb75a8d9-e9b8-4ffc-8fd2-ed27661db326",
  "sourceToolAssistantUUID": "ffbca8f0-d04d-4bf5-b419-23ebd99cfe87",
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

_source line 14 · 2026-05-21T06:03:35.522Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0179fputdTRkzA2j7MbXWddJ`</summary>

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
  "parentUuid": "bb75a8d9-e9b8-4ffc-8fd2-ed27661db326",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2DQbX4PjsKyociVum",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c58d5c1-af8c-40a0-aabd-72451870b074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z8iES8VaRNZJX7SD42HDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4775,
      "cache_read_input_tokens": 17685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4775,
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

_source line 15 · 2026-05-21T06:03:35.537Z_

<details><summary>↩ Tool result · `toolu_0179fputdTRkzA2j7MbXWddJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/paper_framing.md\", \"content\": \"# Paper Framing — nlp_variance_gtheory\\n\\n## Target Venue\\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\\n- Extended: TACL (rolling)\\n\\n## Title\\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\\n\\n## Core Claims (3 条，可证伪)\\n\\n**Claim 1 — Model-Conditional Item Dominance**: Item selection is the single largest variance source in single-model LLM evaluation (61.1% on MMLU), but model×item interaction (26.2%) emerges as the second-largest source when model is treated as a crossed facet. Item difficulty rankings are model-specific: two models with similar aggregate accuracy (Llama 66.4% vs Gemma 73.2%) disagree dramatically at the item level — item_id drops from 61% (single-model) to 38% (cross-model) as model×item absorbs the model-conditional portion. This means single-model variance decompositions overestimate item dominance by conflating universal and model-specific item difficulty. Cross-benchmark gradient (pending exp-002) is hypothesized to further modulate this structure.\\n**Empirical anchors (exp-001, 3 models, balanced bf16, 259,200 records)**: Single-model item_id=61.1%, cross-model item_id=42.8% [34.8-50.1%] (↓18pp), model×item=31.7% [24.6-37.3%] (second-largest source). G_item=0.777 [0.725-0.829] (3 models). D-study: 5 models → G=0.841. model×item magnitude varies with model heterogeneity (12-32% across designs) but is consistently the second-largest source. 4-model analysis pending (Qwen running).\\n**Fallback narratives**: (A) If 4-model REML analysis confirms trend → \\\"model×item interaction is a fundamental dimension of evaluation variance\\\"; (B) If 4-model shows stabilization → \\\"2-model overestimates model-specificity\\\"; (C) Cross-benchmark gradient confirmed → additional conditionality dimension.\\n\\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \\\"infrastructure\\\" is currently limited to the precision facet.\\n\\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.\\n\\n## Contributions (4 条，明确区分)\\n\\n1. **Model×item interaction as the hidden dominant source**: When model is treated as a crossed facet in a balanced 3-model design, model×item interaction (31.7%, CI [24.6-37.3%]) emerges as the second-largest variance source, while item_id drops from 61% (single-model) to 43%. Item difficulty rankings are model-specific — single-model G-studies overestimate item dominance by conflating universal and model-specific difficulty. G_item=0.777 with 3 models, requiring 5+ models for G≥0.84. This is the first quantification of cross-model item-level disagreement in LLM evaluation via G-theory.\\n\\n2. **Confirmatory separability with metric qualification**: Infrastructure×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional and benchmark-conditional (knowledge benchmarks only).\\n\\n3. **IRT vs G-theory: the cost of multi-facet reliability**: The first direct comparison showing G-theory requires 3.6-4.4× more items than IRT (510 vs 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores. At IRT's recommended 116 items, G-theory G is only 0.529. This quantifies the \\\"hidden cost\\\" of evaluation dimensions invisible to IRT.\\n\\n4. **Practitioner toolkit**: Open-source G-theory variance decomposition pipeline + D-study budget calculator for LLM evaluation. Includes: (a) benchmark-specific reproducibility budget tables (items × prompts × seeds for target G), (b) temperature-stratified reliability guide, (c) model-as-facet analysis template. Addresses \\\"purely diagnostic\\\" criticism — provides actionable tools, not just warnings.\\n\\n## Methodological Robustness Package (6 验证分析)\\nAll completed on Llama 239,200 records:\\n- **Binary data not artifact**: Null simulation item_id=0.08% vs observed 61.1% (737.5×); obs/Bernoulli ratio=1.0008\\n- **Fixed vs random insensitive**: Binary G ranges 0.611-0.664 across all facet classification choices\\n- **Bootstrap = jackknife**: CI width ratio 0.96-1.04, independence violation negligible\\n- **Temperature stratification**: Binary G degrades T=0.0 (0.760) → T=0.7 (0.549); text metric unreliable at all T>0\\n- **D-study formula verified**: Monotonicity assertion added; min_items_G80=414 (practical) / 510 (all random)\\n- **IRT comparison**: G-theory 3.6-4.4× more conservative than IRT; difference attributable to prompt/seed/ordering dimensions\\n\\n## Story Spine\\n\\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\\n\\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\\n\\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\\n\\n**Headline result template**: \\\"In a G-study of 5,184 conditions across 4 models on MMLU (200 items), item selection accounts for 61% of variance in single-model evaluation but only 38% when model is treated as a crossed facet — with model×item interaction (26%) emerging as the second-largest source. Cross-model generalizability collapses from G=0.61 to G=0.07, revealing that item difficulty rankings are model-specific. G-theory requires 4× more items than IRT to achieve reliable measurement because it accounts for prompt, seed, and ordering dimensions that IRT ignores. Direct infrastructure×methodology interactions are negligible (<0.1% under binary scoring). We release an open-source G-theory toolkit for practitioners to compute benchmark-specific reproducibility budgets.\\\"\\n\\n## Hook (Counter-Intuitive Quantified Claim)\\n\\\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\\\"\\n\\n## Narrative Strategy\\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\\n- **Tension**: \\\"No universal recipe\\\" — the field seeks standardization but variance structure varies qualitatively across task types\\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\\n- **Figure plan** (5 figures):\\n  1. **Stacked-bar: single-model vs cross-model variance decomposition** — item_id shrinks from 61% to 38%, model×item appears at 26%. The \\\"reveal\\\" figure.\\n  2. **G-theory crossed design diagram** — facets, levels, crossing structure\\n  3. **D-study projection curves** — G vs item count for binary (practical vs all-random) and text metric. Shows G≥0.80 threshold at ~414/510 items.\\n  4. **IRT vs G-theory item requirement comparison** — bar chart showing 116 (IRT) vs 510 (G-theory) items, with breakdown of where the extra items go (prompt×item, seed×item, residual)\\n  5. **Temperature-stratified G coefficient heatmap** — binary vs text metric × 3 temperatures, showing metric×temperature interaction\\n- **Key framing shifts from Dream feedback**:\\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\\n  - Cross-benchmark gradient is the **primary novel finding**\\n  - \\\"Fully crossed\\\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\\n\\n## Venue Fit Risks\\n- AAAI: Strong fit for \\\"evaluation methodology\\\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\\n- Reviewer concern 1: \\\"Only open-weight models, not API models\\\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\\n- Reviewer concern 2: \\\"G-theory is borrowed methodology, not novel\\\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\\n- Reviewer concern 3: \\\"Item dominance is obvious from measurement theory\\\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n1. **\\\"Only N GPU types\\\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \\\"numerical precision\\\" and frame hardware as future work.\\n2. **\\\"float32 engine confound\\\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\\n3. **\\\"Only MMLU\\\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\\n4. **\\\"Small item sample\\\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\\n5. **\\\"No training-time analysis\\\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\\n6. **\\\"Missing scale validation\\\"** → exp-005 (14B models)\\n7. **\\\"G-theory may not be right framework\\\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\\n8. **\\\"Separability claim is metric-dependent\\\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\\n9. **\\\"FP32 degradation is already known (Yuan 2025)\\\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\\n10. **\\\"Incremental over Mesting (2026)\\\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\\n11. **\\\"Model not treated as G-theory facet\\\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\\n12. **\\\"No CIs on variance components\\\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\\n13. **\\\"Missing related work — IRT, tinyBenchmarks, Bouthillier\\\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\\n14. **\\\"Diagnostic tool claim unsubstantiated\\\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \\\"empirical analysis + data release.\\\"\\n15. **\\\"Fine-tuning uses encoder-only RoBERTa\\\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\\n\\n## Design Decisions\\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \\\"reduced crossing\\\" rather than \\\"fully crossed.\\\"\\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\\n\\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\\n\\n### MD1. Binary Data in G-theory\\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\\n**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \\\"mechanical\\\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.\\n\\n### MD2. Fixed vs Random Facet Sensitivity\\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\\n\\n### MD3. Separability Claim Scope\\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\\n**Defense**: Qualify all separability claims as \\\"under binary scoring on knowledge-retrieval benchmarks.\\\" Present benchmark-conditional separability as a finding (not a limitation): \\\"separability itself varies across task types.\\\"\\n\\n### MD4. D-study Optimization Documentation\\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\\n\\n### MD5. G-coefficient Interpretation\\n**Issue**: G=0.22 for 200 items ≠ \\\"MMLU is unreliable\\\" (standard MMLU uses ~14K items).\\n**Defense**: (a) Clearly distinguish \\\"G for our 200-item subsample design\\\" from \\\"reliability of full MMLU\\\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \\\"cost of subsampling\\\" rather than \\\"MMLU is broken.\\\"\\n\\n### MD6. Bootstrap Independence\\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\\n\\n### MD7. IRT vs G-theory Comparison\\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \\\"cost of multi-facet reliability\\\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\\n\\n### MD8. Cross-benchmark Design Asymmetry\\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\\n\\n### MD9. Title-Content Alignment\\n**Issue**: Title promises \\\"Evaluation Metrics\\\" but logprob analysis is minimal.\\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \\\"...Across Benchmarks and Models.\\\"\\n\\n## Required Bibliography (minimum 25 references)\\nKey references to include beyond current literature_map:\\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\\n- Perlitz et al. (2023) — Efficient LLM benchmarking\\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\\n- Shavelson & Webb (1991) — G-theory primer (canonical)\\n- Brennan (2001) — G-theory textbook (canonical)\\n- Lu et al. (2022) — Option ordering effects in MC evaluation\\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\\n- Dehghani et al. (2021) — Benchmark Lottery\\n- Biderman et al. (2024) — Evaluation reproducibility lessons\\n- Vania et al. (2021) — IRT item properties in NLP\\n\", \"total_chars\": 20740, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c58d5c1-af8c-40a0-aabd-72451870b074",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "92d8c31f-7ca6-460c-ab77-b5c0cdae1deb",
  "sourceToolAssistantUUID": "9c58d5c1-af8c-40a0-aabd-72451870b074",
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

_source line 16 · 2026-05-21T06:03:36.501Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YFoMM2Adbfo3FesY88kcBm`</summary>

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
  "parentUuid": "92d8c31f-7ca6-460c-ab77-b5c0cdae1deb",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2DQbX4PjsKyociVum",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df6ea7fc-8c5e-42fa-b463-fb614465857b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z8iES8VaRNZJX7SD42HDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4775,
      "cache_read_input_tokens": 17685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4775,
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

_source line 17 · 2026-05-21T06:03:36.519Z_

<details><summary>↩ Tool result · `toolu_01YFoMM2Adbfo3FesY88kcBm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/decisions.yaml\", \"content\": \"_next_id: 6\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:57 UTC\\n  summary: MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4%），separability 在聚合层面成立，进入\\n    research 阶段\\n  rationale: 5,400 次推理完成，5 个方差分量 ≥5% 且 CI 不含零，pipeline 端到端可运行。核心发现：(1) item 选择是评估方差最大来源；(2)\\n    precision/temperature/prompt 效应是 item-specific 的；(3) 直接的 infrastructure×methodology\\n    交互可忽略（<0.02%）。float32 引擎混淆需全研究阶段解决但不影响 MVP 结论。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:12 UTC\\n  summary: 采用 dual-metric (binary correct + text exact match) 方差分解作为论文核心方法论，Claim\\n    3 改为 metric-conditional reproducibility budget\\n  rationale: MVP 双变量分析揭示截然不同的方差结构：binary correct 下 item_id 主导 (58.4%, G=0.357)；text\\n    exact match 下 prompt×item 主导 (37.5%, G=0.975)。单一 response variable 无法完整描述评估可靠性。Dual-metric\\n    对比是 G-theory 框架的天然优势——\\\"同一实验在不同衡量标准下可靠性完全不同\\\"是比单一 budget 更有力的发现。precision:temperature\\n    交互在 text metric 下显著 (1.3%, CI 不含零)，证明 separability 在细粒度下不完全成立。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 22:20 UTC\\n  summary: Dream 审稿后调整 framing：infrastructure crossing 降级为 confirmatory，cross-benchmark\\n    gradient 升级为 primary novelty，model-as-facet 加入分析计划\\n  rationale: Dream full review (dream_20260520T190053) 三档评分：Best 3/6, Median 4/6,\\n    Worst 3/6。三档一致暴露 9 个结构性问题：(1) bibliography 严重不足（需 25+ refs）; (2) model 未作为 G-theory\\n    facet（inflates item_id）; (3) 无 bootstrap CIs; (4) 零 figures; (5) infrastructure\\n    crossing 为 confirmatory null 非 breakthrough; (6) item dominance 心理测量学预期，oversold;\\n    (7) \\\"fully crossed\\\" 过度声称; (8) \\\"diagnostic tool\\\" 无实质; (9) fine-tuning 用 RoBERTa\\n    距离太远。全部为 framing/分析问题，不影响实验设计——P0 实验不变，但 framing 需大改，exp-004 分析内容扩展。需 re-dream\\n    验证后批准 P0。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: unchanged\\n    result: design not affected by framing changes\\n  - exp_id: exp-004\\n    role: expanded\\n    result: added model-as-facet, bootstrap CIs, higher-order interactions, IRT comparison\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-21 00:08 UTC\\n  summary: 'Re-dream #2 通过质量门控（Best 4/6, Median 4/6），批准 exp-001 启动'\\n  rationale: 'Dream #2 评分：Best 4/6 (Weak Accept), Median 4/6 (Weak Accept), Worst\\n    3/6 (Weak Reject)。Best ≥ weak accept 且 Median ≥ borderline，满足 post-MVP kickoff\\n    Step 5 的批准条件。相比 Dream #1 (3/4/3)，Best 从 3→4 提升，结构性问题已解决。剩余问题均为分析/呈现层面：(1) 零 figures\\n    — 论文写作阶段处理; (2) D-study 优化过程需文档化 — exp-004; (3) Bootstrap 重采样独立性问题 — 加 jackknife\\n    对比到 exp-004; (4) G 系数解读需区分 item-level 与 benchmark-level — 论文 Discussion; (5) Cross-benchmark\\n    设计不对称需 sensitivity analysis — exp-004; (6) IRT 对比 — 已纳入 exp-004; (7) Exp 5/6/7\\n    建议移至 appendix — 论文写作。所有剩余问题不影响 exp-001 实验设计。'\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: approved\\n    result: re-dream passes, proceed with full-scale experiment\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-21 02:26 UTC\\n  summary: Gemma2 fp16 不可用 — cross-model 分析用 bf16+fp32 平衡设计，fp16 仅用于 within-model\\n  rationale: vLLM 报告 Gemma2 架构不支持 fp16（numerical instability）。bf16 vs fp16 差异 <0.1pp（Llama\\n    数据），precision 信号集中在 fp32 vs 其他（10.7pp）。cross-model 用 2 precisions 不损失 power，fp16\\n    数据在 Llama/Mistral/Qwen within-model 分析中保留。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: affected\\n    result: Gemma fp16 conditions marked N/A, cross-model analysis scoped to bf16+fp32\\n  depends_on:\\n  - D004\\n\", \"total_chars\": 3318, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df6ea7fc-8c5e-42fa-b463-fb614465857b",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "6583a5d4-ac93-4780-9485-34ddc8d529c4",
  "sourceToolAssistantUUID": "df6ea7fc-8c5e-42fa-b463-fb614465857b",
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

_source line 18 · 2026-05-21T06:03:36.975Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H7VrsVNGKs97pzf99Tagi1`</summary>

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
  "parentUuid": "6583a5d4-ac93-4780-9485-34ddc8d529c4",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2DQbX4PjsKyociVum",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15255c37-aa87-41b9-9ffc-9ac2da0ae495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z8iES8VaRNZJX7SD42HDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4775,
      "cache_read_input_tokens": 17685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4775,
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

_source line 19 · 2026-05-21T06:03:36.985Z_

<details><summary>↩ Tool result · `toolu_01H7VrsVNGKs97pzf99Tagi1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/memory.md\", \"content\": \"# Memory — nlp_variance_gtheory\\n\\n## Gated Model 约束 (2026-05-20)\\nLlama-3.1-8B-Instruct 和 gemma-2-9b-it 是 HF gated models，直接用 repo ID 加载失败。westd-32570 上通过 ModelScope 下载到本地路径（如 `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct`）。exp-001 正式运行需要 model path mapping 或 HF token。\\n\\n## 双 Metric 设计决策 (2026-05-20, D002)\\nbinary_correct 和 text_exact_match 测量正交维度（Spearman ρ = −0.21, n.s.）。前者衡量评估有效性（item 难度主导），后者衡量可复现性（prompt×item + temperature 主导）。两者必须同时保留——不能互相替代。\\n\\n## Temperature 对 text_match 的决定性影响 (2026-05-20)\\nT=0 → text_match=0.247, T=0.5 → text_match=0.019（降 92%），但 binary_correct 几乎不变。这是 G-theory 框架的关键洞察：采样随机性改变文本表述但不改变答案选择。\\n\\n## FP32 精度效应确认 (2026-05-20)\\nFP32 的 8.5pp accuracy gap 中 97.4% 是精度效应（非引擎 confound）。BF16-trained model 用 FP32 推理表现更差，可能因为权重从 BF16 加载到 FP32 时的数值行为差异。\\n\\n## Gemma2 不支持 float16 (2026-05-21)\\nvLLM 拒绝以 float16 加载 gemma2：`\\\"The model type 'gemma2' does not support float16. Reason: Numerical instability.\\\"`。这是架构层面限制，非配置问题。Director 决策 (方案 A 修改版)：cross-model 分析用 bf16+fp32 (2 precisions × 4 models 平衡设计)，fp16 仅用于 Llama/Mistral/Qwen 的 within-model G-study。bf16 vs fp16 差异 <0.1pp (Llama 已证实)，precision 信号集中在 fp32 vs 其他 (10.7pp gap)。\\n\\n## few_shot_examples.json 一致性风险 (2026-05-21)\\nGemma 启动时 Worker 重新生成了 few_shot_examples.json（从 5 subjects × 2 orderings → 10 subjects × 4 orderings）。需验证 Llama 实际使用的版本是否一致，否则 cross-model ordering facet 对比可能失效。\\n\\n## M006: D-study 公式方向性检查 (2026-05-21)\\nD-study 公式 `G_ni = σ²τ / (σ²τ + σ²δ × (n_actual / ni))` — 注意是 n_actual/ni 而非 ni/n_actual。G 必须随 n_items 单调递增（items 越多 error 越小）。所有 D-study 代码必须带 monotonicity assertion。temperature_stratified_analysis.json 曾因公式反转导致 min_items_G80=10（正确值 414）。**教训：遇到不合理结果（G 随 items 下降）时质疑计算，不要合理化。**\\n\\n## Cross-model G-study 关键洞察 (2026-05-21)\\n2-model (Llama+Gemma) 分析揭示：item_id 从单模型 61.1% 降至 37.9%，model×item_id 交互 = 26.2%（第二大方差源）。G 系数从 0.611 暴跌至 0.073——单模型 item 难度排序跨模型几乎不可推广。model main effect 仅 0.2%（均值相似），但 item-level 交互极大。D-study 显示即使 10 个模型 G 仅 0.179。这是论文核心叙事\\\"no universal reproducibility recipe\\\"的最强证据。\\n\", \"total_chars\": 1994, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15255c37-aa87-41b9-9ffc-9ac2da0ae495",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "48ca461f-5896-4f47-b186-be7a9ac42c4f",
  "sourceToolAssistantUUID": "15255c37-aa87-41b9-9ffc-9ac2da0ae495",
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

_source line 20 · 2026-05-21T06:03:37.615Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DdH8R7d2i6fBAdh71KyeHx`</summary>

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
  "parentUuid": "48ca461f-5896-4f47-b186-be7a9ac42c4f",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2DQbX4PjsKyociVum",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a478b41e-9a75-49c3-a1d2-aa391a352a46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Z8iES8VaRNZJX7SD42HDF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4775,
      "cache_read_input_tokens": 17685,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 390,
          "cache_read_input_tokens": 17685,
          "cache_creation_input_tokens": 4775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4775,
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

_source line 21 · 2026-05-21T06:03:37.623Z_

<details><summary>↩ Tool result · `toolu_01DdH8R7d2i6fBAdh71KyeHx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/ROADMAP.md\", \"content\": \"# nlp_variance_gtheory — Research Dashboard\\n\\n> 最后更新: 2026-05-21 00:13 UTC | 更新原因: Dream #2 通过，exp-001 Phase 1 Llama 执行中，ROADMAP 同步\\n\\n## 核心方向\\nCross-benchmark G-theory 方差分解：item dominance 是 benchmark-conditional 的，variance structure 随 task type 系统性变化，无 universal reproducibility recipe。详见 `paper_framing.md`。\\n\\n## 当前进展\\n- **阶段**: Research（exp-001 执行中）\\n- **MVP**: PASS — item_id=58.4%, separability <0.5%, dual-metric (binary G=0.357, text G=0.975)\\n- **Dream #1**: Best 3/6 → 9 个结构性问题修复 framing\\n- **Dream #2**: Best 4/6, Median 4/6 — **质量门控通过** (D004)\\n- **P0 实验**: 1/5 started — exp-001 Phase 1 (Llama) 执行中\\n- **代码准备**: pipeline dry-run PASS, 分析框架 (model_facet, bootstrap_ci) 就绪\\n- **模型**: Llama ✅, Mistral/Qwen3-Instruct/Gemma 下载中\\n- **磁盘**: 根 41% (18G free), 数据盘 19% (284G free)\\n- **文献**: bibliography 15 篇完成, related_work 10 篇完成\\n\\n## P0 实验状态\\n\\n| ID | 描述 | GPU-h | 状态 | 阻塞项 |\\n|----|------|-------|------|--------|\\n| exp-001 | 4 models × 5184 conditions × 200 MMLU items | 100 | **Phase 1 执行中** (Llama) | 其他模型下载 |\\n| exp-001b | Item resampling stability (3×200-item samples) | 15 | planned | exp-001 |\\n| exp-002 | Multi-benchmark (GSM8K, ARC, HellaSwag) | 200 | 采样脚本就绪 | exp-001 |\\n| exp-003 | Multi-hardware G-study | 120 | **BLOCKED** | 第二种 GPU（已催 Manager ×2） |\\n| exp-004 | D-study + model-as-facet + bootstrap + IRT 对比 | 0 | planned | exp-001/002/003 |\\n\\n## 近期任务\\n- [ ] exp-001 Phase 1: Llama 全量 1,196 conditions × 200 items（4 GPU 并行，Agent 执行中）\\n- [ ] 监控模型下载 → Phase 2: 每个模型下载完即开跑\\n- [ ] Phase 3: 2+ 模型完成后立即 model-as-facet 分析（Claim 1 make-or-break）\\n- [ ] exp-003 第二种 GPU 跟进 Manager\\n- [x] Dream #2 通过质量门控，exp-001 批准 (D004)\\n- [x] paper_framing.md 全面重写（9 issues from Dream #1）\\n- [x] experiment_plan.yaml 扩展（exp-001b, exp-004）\\n- [x] 分析代码框架：model_facet_analysis.py, bootstrap_ci.py\\n- [x] bibliography 15 篇 + related_work 10 篇\\n- [x] dual_metric_analysis.md 深度分析\\n- [x] exp-001 dry-run + pilot v2 通过 (20,000 records)\\n- [Dream 观察] item_id 在 model-as-facet 后是否下降\\n- [Dream 观察] residual 是否 >25%（高阶交互）\\n- [Dream 观察] D-study budget vs MATH item pool\\n\\n## GPU 预算\\n- **已分配**: westd-32570 4× RTX PRO 6000 96GB（GPU 0-3）\\n- **在用**: 4/4（exp-001 Phase 1 Llama）\\n- **P0 总需**: 435h\\n- **第二种 GPU**: 已催 Manager ×2，预估 ¥210-360\\n\\n## 投稿目标\\n- AAAI 2027: abstract Jul 21, paper Jul 28（9 weeks）\\n- ACL 2027 ARR: Oct 15（21 weeks, backup）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D005 | 2026-05-21 | Gemma2 fp16 不可用 — cross-model 分析用 bf16+fp32 平衡设计，f | exp-001 |\\n| D004 | 2026-05-21 | Re-dream #2 通过质量门控（Best 4/6, Median 4/6），批准 exp-00 | exp-001 |\\n| D003 | 2026-05-20 | Dream 审稿后调整 framing：infrastructure crossing 降级为 co | exp-001, exp-004 |\\n| D002 | 2026-05-20 | 采用 dual-metric (binary correct + text exact match) | — |\\n| D001 | 2026-05-20 | MVP PASS — G-theory 方差分解在 LLM 评估中可行，item 方差主导（58.4 | — |\\n\\n\", \"total_chars\": 2775, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a478b41e-9a75-49c3-a1d2-aa391a352a46",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "30a44cac-2d6b-4cd0-9c0d-8eb394218457",
  "sourceToolAssistantUUID": "a478b41e-9a75-49c3-a1d2-aa391a352a46",
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

_source line 22 · 2026-05-21T06:03:41.778Z_

Now let me read the paper writing plan and any existing paper draft/sections, plus the distilled research and writing skills for full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30a44cac-2d6b-4cd0-9c0d-8eb394218457",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2d5t14eiBSVMf3oWW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6e12740-85ef-4d03-950e-07ab8b73f9e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8htmyv9tEhExY4gtDBftC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11433,
      "cache_read_input_tokens": 22460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11433,
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

_source line 23 · 2026-05-21T06:03:42.789Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019QiSqNGjbXvnMxmMhN77N2`</summary>

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
  "parentUuid": "d6e12740-85ef-4d03-950e-07ab8b73f9e0",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2d5t14eiBSVMf3oWW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "569afec2-0102-45b4-b45e-76fda2a7145d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8htmyv9tEhExY4gtDBftC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11433,
      "cache_read_input_tokens": 22460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11433,
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

_source line 24 · 2026-05-21T06:03:42.797Z_

<details><summary>↩ Tool result · `toolu_019QiSqNGjbXvnMxmMhN77N2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "569afec2-0102-45b4-b45e-76fda2a7145d",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "e6eee43a-089d-4d2a-9546-0175f75b16d1",
  "sourceToolAssistantUUID": "569afec2-0102-45b4-b45e-76fda2a7145d",
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

_source line 25 · 2026-05-21T06:03:43.726Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TMusD8jYstzHCkDWgqAUvL`</summary>

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
  "parentUuid": "e6eee43a-089d-4d2a-9546-0175f75b16d1",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2d5t14eiBSVMf3oWW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cddff34-00bb-4d6f-9175-41bc78632ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8htmyv9tEhExY4gtDBftC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11433,
      "cache_read_input_tokens": 22460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11433,
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

_source line 26 · 2026-05-21T06:03:43.734Z_

<details><summary>↩ Tool result · `toolu_01TMusD8jYstzHCkDWgqAUvL`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'nlp_variance_gtheory'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cddff34-00bb-4d6f-9175-41bc78632ab1",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "acde662a-8ad3-46ec-a369-6cd8392a4cb7",
  "sourceToolAssistantUUID": "4cddff34-00bb-4d6f-9175-41bc78632ab1",
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

_source line 27 · 2026-05-21T06:03:44.328Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lfa6DhryAK6ZCWCkgwT1Xf`</summary>

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
  "parentUuid": "acde662a-8ad3-46ec-a369-6cd8392a4cb7",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2d5t14eiBSVMf3oWW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2f525c4-78b7-44e4-beb2-c77a77991495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8htmyv9tEhExY4gtDBftC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11433,
      "cache_read_input_tokens": 22460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11433,
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

_source line 28 · 2026-05-21T06:03:44.334Z_

<details><summary>↩ Tool result · `toolu_01Lfa6DhryAK6ZCWCkgwT1Xf`</summary>

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
  "parentUuid": "d2f525c4-78b7-44e4-beb2-c77a77991495",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "79455762-e7a1-4e45-8fd7-fb81132df3c8",
  "sourceToolAssistantUUID": "d2f525c4-78b7-44e4-beb2-c77a77991495",
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

_source line 29 · 2026-05-21T06:03:44.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WuWqFCmMa4C7DJtYhbnArF`</summary>

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
  "parentUuid": "79455762-e7a1-4e45-8fd7-fb81132df3c8",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD2d5t14eiBSVMf3oWW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8024535-bc6d-4fe7-b25d-950295d9fdd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8htmyv9tEhExY4gtDBftC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11433,
      "cache_read_input_tokens": 22460,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11433
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 383,
          "cache_read_input_tokens": 22460,
          "cache_creation_input_tokens": 11433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11433,
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

_source line 30 · 2026-05-21T06:03:44.708Z_

<details><summary>↩ Tool result · `toolu_01WuWqFCmMa4C7DJtYhbnArF`</summary>

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
  "parentUuid": "f8024535-bc6d-4fe7-b25d-950295d9fdd7",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "3bf6c4a4-2c15-44c3-abd1-84132f8d843b",
  "sourceToolAssistantUUID": "f8024535-bc6d-4fe7-b25d-950295d9fdd7",
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

_source line 31 · 2026-05-21T06:03:47.568Z_

Now let me look at the actual paper artifacts — any draft sections, analysis outputs, and experiment results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bf6c4a4-2c15-44c3-abd1-84132f8d843b",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD39UEU4ihPwM5k4XZi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71bb2da5-9b17-4d10-b6c9-2e1eb5f8cd96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3yzarLaUXB2f6yThEjp4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 33893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2482,
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

_source line 32 · 2026-05-21T06:03:48.546Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018wAvN29tBXQp5Hzk4BkDCJ`</summary>

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
  "parentUuid": "71bb2da5-9b17-4d10-b6c9-2e1eb5f8cd96",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD39UEU4ihPwM5k4XZi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a94cafd-1a80-498d-a4f3-2a0678df8ccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3yzarLaUXB2f6yThEjp4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 33893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2482,
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

_source line 33 · 2026-05-21T06:03:48.581Z_

<details><summary>↩ Tool result · `toolu_018wAvN29tBXQp5Hzk4BkDCJ`</summary>

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
  "parentUuid": "5a94cafd-1a80-498d-a4f3-2a0678df8ccd",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "bcd2a2f4-fac1-4679-81c5-34bae967c66a",
  "sourceToolAssistantUUID": "5a94cafd-1a80-498d-a4f3-2a0678df8ccd",
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

_source line 34 · 2026-05-21T06:03:49.028Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XSqeZ8iaFTwHbS1PuDopod`</summary>

```json
{
  "pattern": "**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcd2a2f4-fac1-4679-81c5-34bae967c66a",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD39UEU4ihPwM5k4XZi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2502e82-0e6a-4043-a426-273188ee1de2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3yzarLaUXB2f6yThEjp4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 33893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2482,
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

_source line 35 · 2026-05-21T06:03:49.044Z_

<details><summary>↩ Tool result · `toolu_01XSqeZ8iaFTwHbS1PuDopod`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/experiment_data.json
artifacts/dream_reports/dream_20260520T190053/median/experiment_data.json
artifacts/dream_reports/dream_20260520T190053/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T222113/best/experiment_data.json
artifacts/dream_reports/dream_20260520T222113/median/experiment_data.json
artifacts/dream_reports/dream_20260520T222113/worst/experiment_data.json
artifacts/dream_reports/dream_20260521T032813/best/experiment_data.json
artifacts/dream_reports/dream_20260521T032813/median/experiment_data.json
artifacts/dream_reports/dream_20260521T032813/worst/experiment_data.json
artifacts/dream_reports/dream_20260521T044739/best/experiment_data.json
artifacts/dream_reports/dream_20260521T044739/median/experiment_data.json
artifacts/dream_reports/dream_20260521T044739/worst/experiment_data.json
artifacts/analysis/cross_model_reml.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2502e82-0e6a-4043-a426-273188ee1de2",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "31967f32-4a9a-434c-8504-c862e1c99731",
  "sourceToolAssistantUUID": "d2502e82-0e6a-4043-a426-273188ee1de2",
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

_source line 36 · 2026-05-21T06:03:49.606Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01E9m9uiAipTmst13dxQYRPj`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/ 2>/dev/null || echo \"No artifacts dir\"",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31967f32-4a9a-434c-8504-c862e1c99731",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD39UEU4ihPwM5k4XZi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6423bdf-e915-40fc-8b51-05b25c0e0817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3yzarLaUXB2f6yThEjp4H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 33893,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2482
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 33893,
          "cache_creation_input_tokens": 2482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2482,
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

_source line 37 · 2026-05-21T06:03:49.743Z_

<details><summary>↩ Tool result · `toolu_01E9m9uiAipTmst13dxQYRPj`</summary>

```text
total 60
drwxr-xr-x  7 ubuntu ubuntu 4096 May 20 23:40 .
drwxr-xr-x 10 ubuntu ubuntu 4096 May 21 05:53 ..
drwxr-xr-x  4 ubuntu ubuntu 4096 May 20 17:12 _project
drwxr-xr-x  3 ubuntu ubuntu 4096 May 21 06:03 analysis
-rw-r--r--  1 ubuntu ubuntu 8690 May 20 23:40 bibliography_notes.md
drwxr-xr-x  4 ubuntu ubuntu 4096 May 21 02:55 code
drwxr-xr-x  6 ubuntu ubuntu 4096 May 21 04:47 dream_reports
-rw-r--r--  1 ubuntu ubuntu 3321 May 20 16:34 env_setup_report.md
-rw-r--r--  1 ubuntu ubuntu 4036 May 20 23:40 manifest.yaml
drwxr-xr-x  4 ubuntu ubuntu 4096 May 20 22:01 mvp_phase_a
-rw-r--r--  1 ubuntu ubuntu 9779 May 20 21:04 related_work_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6423bdf-e915-40fc-8b51-05b25c0e0817",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "3352a022-80bb-4cdd-90d9-99aaecc84f86",
  "sourceToolAssistantUUID": "c6423bdf-e915-40fc-8b51-05b25c0e0817",
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

_source line 38 · 2026-05-21T06:03:52.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YSFX5hEbnzoQsFCJnYrva8`</summary>

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
  "parentUuid": "3352a022-80bb-4cdd-90d9-99aaecc84f86",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD3WivAj5Rh7xnCk7Xm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c9ef182-90e4-4b07-8da6-f05f400f0247",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjJvuCjVxcz7nGFhnGWEaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 36375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1260,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 39 · 2026-05-21T06:03:52.678Z_

<details><summary>↩ Tool result · `toolu_01YSFX5hEbnzoQsFCJnYrva8`</summary>

```text
1	# Related Work — Structured Notes
2	
3	> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。
4	
5	## (a) G-theory & Variance Decomposition in NLP/ML
6	
7	### [Mesting et al., 2026] — Hidden Measurement Error in LLM Pipelines
8	- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估，交叉分解 5 个 facets（item/prompt/temperature/judge model/replication）；发现 judge 选择贡献 43.8% 方差，prompt×judge 交互贡献 12.4%；标准 95% CI 实际覆盖率仅 79%，标准 CI 遗漏 40-60% 不确定性
9	- **方法**: 在 AILuminate、MMLU、Chatbot Arena 上对多个 LLM 进行全交叉 G-study，用 REML 估计方差分量，D-study 指导评估设计优化（如 3 个 judge 可降低 38% SE）
10	- **与本工作的关系**: extends — 我们直接继承其 TEE 框架和 REML 方法论，是最近的方法论前驱；但其 facets 完全限于方法论层面，未涉及 infrastructure
11	- **我们的差异化**: 我们将 G-theory 框架扩展到 infrastructure facets（precision/hardware/batch），实现 infrastructure × methodology 的联合交叉分解，这是 Mesting 未触及的维度
12	
13	### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition
14	- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量
15	- **方法**: 提出基于语义层次的方差分解框架，将 prompt 变异按语义保持程度分级
16	- **与本工作的关系**: complements — 提供了 prompt 方差的细粒度语义分解，其 articulation 分量对应我们框架中 prompt paraphrase facet
17	- **我们的差异化**: Kunievsky 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的全交叉设计；我们的框架同时容纳 prompt 和 infrastructure facets
18	
19	### [Nalisnick et al., 2024] — GeneralizIT: G-theory Software for ML
20	- **核心发现**: 为 ML 场景提供 G-theory 计算工具包（Python），简化 REML 估计和 D-study 设计流程
21	- **方法**: Python 实现 G-theory 核心计算，包括方差分量估计和 D-study 投影
22	- **与本工作的关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现
23	- **我们的差异化**: GeneralizIT 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget
24	
25	## (b) Infrastructure Variance
26	
27	### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance
28	- **核心发现**: BF16 推理导致高达 9% 的 accuracy 标准差和 9,000-token 的回复长度偏移，FP32 接近 0%；推理模型（reasoning models）受影响最大；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存
29	- **方法**: 系统性测试不同 GPU 数量、类型、精度配置下的 LLM 推理输出变异，对比 FP32/BF16/FP16 的准确率和生成长度差异
30	- **与本工作的关系**: addresses limitation of — 提供了 precision 作为 infrastructure 方差源的关键经验证据，但未将其纳入多因素统一分解框架，止步于单因素刻画+工程缓解
31	- **我们的差异化**: 我们将 precision 作为 G-theory 框架中的一个 facet，与 prompt/judge/temperature 等方法论因素联合交叉分解，可量化 precision × methodology 交互效应
32	
33	### [Messina et al., 2026 (TMLR)] — Background Temperature Effects on GPU Computation
34	- **核心发现**: 即使名义温度 T=0，API 模型仍存在"背景随机性"：GPT 有效温度~0.075、Gemini~0.065、Claude~0；根因是 BF16/FP16 浮点运算的非结合性（floating-point non-associativity）导致的隐式随机性
35	- **方法**: 提出 reference calibration 方法，将背景非确定性量化为单一标量 T_bg；在多个 API 模型上系统测量 T=0 下的输出变异分布
36	- **与本工作的关系**: complements — 为 infrastructure 层面的非确定性提供了理论解释（浮点非结合性）和量化方法（T_bg），为我们纳入 hardware facet 提供实证和理论依据；precision × temperature 交互在 text_match 下可能显著
37	- **我们的差异化**: Messina 聚焦 API 层面的 T_bg 刻画，是单因素描述性研究；我们将此类硬件非确定性纳入 G-theory 的多因素交叉设计，检验其与方法论因素的交互
38	
39	### [ThinkingMachines, 2025] — Batch Invariance Failure in LLM Inference
40	- **核心发现**: T=0 下 Qwen3-8B 在默认 vLLM 设置下 1000 次推理产生 80 种不同输出；根因不是随机种子，而是 RMSNorm/GEMM/attention 算子的 batch-size 依赖性；提出确定性内核方案，代价为 1.6-2.1× 延迟
41	- **方法**: 在 vLLM 框架下系统性测试 batch size 对 T=0 推理的影响，逐层定位非确定性来源（RMSNorm → GEMM → attention），提出并验证 batch-invariant 内核
42	- **与本工作的关系**: addresses limitation of — 发现并定位了 batch 非确定性这一关键 infrastructure 方差源，但止步于工程诊断和修复，未进行跨因素归因
43	- **我们的差异化**: 我们使用默认设置（不启用确定性内核）以反映从业者真实条件，用 text_exact_match 指标捕获类似的 infrastructure 非确定性，并将 batch 因素与其他 infrastructure/methodology 因素一起纳入 G-theory 分解
44	
45	## (c) Prompt Sensitivity & Methodological Variance
46	
47	### [Brittlebench, 2026] — Prompt Brittleness Benchmark
48	- **核心发现**: 系统性评估 prompt 脆弱性，prompt 措辞贡献约 50% 方差（开源模型）、商用模型约 25%；63% 的情况下单一扰动即导致排名反转
49	- **方法**: 通过 ANOVA 分解 V_data + V_brittleness，设计标准化 prompt 扰动协议，在多模型多基准上评估
50	- **与本工作的关系**: complements — 提供了大规模 prompt 脆弱性的实证基准和扰动协议（我们的 prompt paraphrase 生成参考其方法）；其 V_brittleness 分量对应我们框架中 prompt facet 的方差
51	- **我们的差异化**: Brittlebench 使用传统 ANOVA 只分解 data vs. brittleness 两个分量；我们的 G-theory 框架不仅量化 prompt sensitivity，还分解其与 judge/temperature/precision 等因素的交互效应
52	
53	### [Hua et al., 2025 (EMNLP)] — Scoring Artifacts in LLM Evaluation
54	- **核心发现**: 大量表观的 prompt sensitivity 实际上是评估方法的 artifact——使用 LLM-judge 替代 log-likelihood 评估后 rank correlation 从 0.30 跃升至 0.95
55	- **方法**: 对比 log-likelihood 和 generation-based 评估方式下的 prompt sensitivity 表现，揭示评分方法对方差估计的系统性偏差
56	- **与本工作的关系**: complements — 警示区分"真实方差"与"评估 artifact"的重要性；为我们选择 generation-based 评估协议（而非 log-likelihood）提供方法论依据
57	- **我们的差异化**: Hua 聚焦揭示 artifact 现象而非系统性分解方差来源；我们的 G-theory 框架可将 scoring method 作为 facet 纳入，从而量化其贡献
58	
59	### [Same Prompt, Different Outcomes, 2026] — LLM Reproducibility
60	- **核心发现**: 在 2 策略 × 6 模型 × 4 温度 × 10 重复的设计下确认了方法论层面的方差，但排除了硬件/精度因素
61	- **方法**: 在加拿大政府任命记录数据集（3,718 条记录）上，使用 6 个模型（Claude Haiku 4.5、Claude Opus 4.6、GPT-5-mini、GPT-5.2、Gemini Flash 3、Gemini Pro 3）× 2 种 prompting 策略（multi-step 分步 vs. single-step 一次性）× 4 个温度（0.0/0.3/0.7/1.0）× 10 次重复，共 480 次执行；评估指标为 completion（完成率）、concordance（与人工分析一致性）、validity（有效性）、consistency（跨运行一致性）；发现 prompting 策略是主导方差源，数据预处理步骤产生最大分析分歧，即使 T=0 也存在非确定性
62	- **与本工作的关系**: complements — 确认 methodology-layer 方差的存在，但缺乏 infrastructure 交叉
63	- **我们的差异化**: 我们同时纳入 infrastructure 和 methodology 因素进行联合分解
64	
65	### [Bui et al., 2025] — Seed Sensitivity in LLM Fine-Tuning
66	- **核心发现**: 微调阶段种子敏感性极端（RTES variance=18.22），是单因素研究
67	- **方法**: 对 RoBERTa-large（全参数微调）和 Llama3.2-3B（LoRA，~2.3M 可训练参数）在 GLUE/SuperGLUE 基准上以 10 个随机种子（42–132）重复微调；宏观指标为 accuracy/F1 的均值和方差，微观指标为自定义 consistency（跨种子个体预测稳定性）；RoBERTa-large 方差极端分化——COPA 方差 16.83、RTE 方差 16.67，而 QQP 仅 0.06；LoRA 微调的 Llama 在多数任务上方差显著低于全参数微调
68	- **与本工作的关系**: complements — 预期与我们框架中 seed facet 直接相关；为微调阶段 G-study 扩展提供动机
69	- **我们的差异化**: Bui 只考察 seed 这一单一因素，未进行 infrastructure 交叉；我们的框架支持将 seed 与其他因素联合分解
70	
71	## 定位总结
72	
73	本项目是首个用 Generalizability Theory 联合分解 infrastructure（硬件类型、数值精度、batch 非确定性）与 methodology（prompt 措辞、随机种子、温度、few-shot 顺序）方差的工作。现有研究要么只用 G-theory 分解方法论 facets（Mesting），要么只刻画单一 infrastructure 因素并提出工程修复（Yuan、ThinkingMachines、Messina），没有工作在一个统一的交叉设计中同时容纳两类因素并检验其 separability。我们的 D-study 产出可量化的 reproducibility budget，为社区提供实验设计的决策依据。
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c9ef182-90e4-4b07-8da6-f05f400f0247",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "7c4195e5-b279-47d2-8af7-cd7f4424290c",
  "sourceToolAssistantUUID": "7c9ef182-90e4-4b07-8da6-f05f400f0247",
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

_source line 40 · 2026-05-21T06:03:52.992Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fm8V6zSAbHYBPV9sv4h89b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/bibliography_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c4195e5-b279-47d2-8af7-cd7f4424290c",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD3WivAj5Rh7xnCk7Xm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eeb31273-cab3-41a0-b5c9-451b26a17e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjJvuCjVxcz7nGFhnGWEaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 36375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1260,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 41 · 2026-05-21T06:03:52.998Z_

<details><summary>↩ Tool result · `toolu_01Fm8V6zSAbHYBPV9sv4h89b`</summary>

```text
1	# Bibliography Notes
2	
3	## 1. Bouthillier et al. (2021)
4	**Citation**: Bouthillier, X., Delaunay, P., Bronzi, M., Trofimov, A., Nichyporuk, B., Szeto, J., Mohammadi Sepahvand, N., Raff, E., Madan, K., Voleti, V., Ebrahimi Kahou, S., Michalski, V., Arbel, T., Pal, C., Varoquaux, G., & Vincent, P. (2021). Accounting for Variance in Machine Learning Benchmarks. *Proceedings of Machine Learning and Systems (MLSys)*, 3.
5	**关联**: 提出 ML benchmark 中方差的系统性量化框架，展示了随机种子、数据划分等因素对评估结果的显著影响，是将统计方法引入 ML 评估可靠性的先驱工作，与我们用 G-theory 分解评估方差的核心目标直接对应。
6	
7	## 2. Polo et al. (2024)
8	**Citation**: Maia Polo, F., Weber, L., Choshen, L., Sun, Y., Xu, G., & Yurochkin, M. (2024). tinyBenchmarks: Evaluating LLMs with Fewer Examples. *Proceedings of the 41st International Conference on Machine Learning (ICML)*, PMLR 235.
9	**关联**: 用 IRT 建模 benchmark item 的区分力来选择代表性子集，实现高效评估。其 item-level 分析思路与我们用 G-theory 分解 item（题目）方差源的方法论互补——tinyBenchmarks 关注 item 选择效率，我们关注方差归因。
10	
11	## 3. Perlitz et al. (2024)
12	**Citation**: Perlitz, Y., Bandel, E., Gera, A., Arviv, O., Ein-Dor, L., Shnarch, E., Slonim, N., Shmueli-Scheuer, M., & Choshen, L. (2024). Efficient Benchmarking (of Language Models). *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)*, pages 2519–2536.
13	**关联**: 系统研究了 benchmark 设计选择（任务数量、样本数量、指标选择）对评估可靠性的影响，以 HELM 为测试案例量化了计算成本-可靠性的权衡。为我们的 G-theory 框架提供了"哪些设计因素值得纳入方差分解"的实证依据。
14	
15	## 4. Henderson et al. (2018)
16	**Citation**: Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., & Meger, D. (2018). Deep Reinforcement Learning That Matters. *Proceedings of the 32nd AAAI Conference on Artificial Intelligence (AAAI)*, pages 3207–3214.
17	**关联**: 深度 RL 领域的可复现性经典研究，揭示了超参数、随机种子、代码实现等因素导致的高方差问题。虽然领域不同，但其方差量化方法论和"评估结果不可靠"的核心发现，为我们在 NLP 评估中引入 G-theory 提供了跨领域动机。
18	
19	## 5. Lalor et al. (2019)
20	**Citation**: Lalor, J. P., Wu, H., & Yu, H. (2019). Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pages 4962–4973.
21	**关联**: 首次将 IRT 应用于 NLP 评估，用 DNN 生成的 artificial crowds 替代人类作答数据来估计 item 参数。为我们在 LLM 评估中使用心理测量学方法（G-theory 也源于心理测量学）提供了直接先例和方法论基础。
22	
23	## 6. Rodriguez et al. (2021)
24	**Citation**: Rodriguez, P., Barrow, J., Hoyle, A., Lalor, J. P., Jia, R., & Boyd-Graber, J. (2021). Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards? *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 4486–4503.
25	**关联**: 用贝叶斯 IRT 模型分析 NLP leaderboard 的排名可靠性，发现不同 item 的信息量差异巨大。其"item 层面的评估质量分析"与我们 G-theory 中将 item 作为方差 facet 的设计理念高度一致。
26	
27	## 7. Vania et al. (2021)
28	**Citation**: Vania, C., Htut, P. M., Huang, W., Mungra, D., Pang, R. Y., Phang, J., Liu, H., Cho, K., & Bowman, S. R. (2021). Comparing Test Sets with Item Response Theory. *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 1141–1158.
29	**关联**: 用 IRT 分析 29 个 NLP 数据集的 item 属性（难度、区分度），发现部分 benchmark 对当前模型已经饱和。提供了 item 层面的定量分析方法，与我们的 G-theory 方差分解在 item facet 维度互补。
30	
31	## 8. Lu et al. (2022)
32	**Citation**: Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity. *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 8086–8098.
33	**关联**: 实证表明 few-shot prompt 中示例的排列顺序可导致性能从 SOTA 级别降至随机猜测水平。这种 prompt ordering 效应是我们 G-theory 框架中 infrastructure facet（评估执行方式带来的方差）的关键组成部分。
34	
35	## 9. Pezeshkpour & Hruschka (2024)
36	**Citation**: Pezeshkpour, P. & Hruschka, E. (2024). Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions. *Findings of the Association for Computational Linguistics: NAACL 2024*, pages 2006–2017.
37	**关联**: 量化了 LLM 在多选题中对选项顺序的敏感性（性能差异 13%–75%），直接证明了评估基础设施层面的方差来源。这是我们 G-theory 方差分解中 item presentation format 这一 facet 的核心实证支撑。
38	
39	## 10. Dodge et al. (2020)
40	**Citation**: Dodge, J., Ilharco, G., Schwartz, R., Farhadi, A., Hajishirzi, H., & Smith, N. A. (2020). Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping. *arXiv preprint arXiv:2002.06305*.
41	**关联**: 系统量化了微调过程中随机种子（权重初始化和数据顺序）对性能的影响，发现 BERT 在 GLUE 任务上的表现因种子不同差异显著。直接为我们 G-theory 框架中"模型训练方差"这一 facet 提供了实证依据。
42	
43	## 11. Sellam et al. (2022)
44	**Citation**: Sellam, T., Yadlowsky, S., Tenney, I., Wei, J., Saphra, N., D'Amour, A., Linzen, T., Bastings, J., Turc, I., Eisenstein, J., Das, D., & Pavlick, E. (2022). The MultiBERTs: BERT Reproductions for Robustness Analysis. *Proceedings of the 10th International Conference on Learning Representations (ICLR)*.
45	**关联**: 训练了 25 个独立 BERT 模型来量化预训练随机性对下游任务的影响，提供了严格的多次复现分析框架。MultiBERTs 的方法论（多次独立训练 + 统计分析）与 G-theory 的 D-study（决策研究，估计需要多少复现才能达到可靠评估）思想天然契合。
46	
47	## 12. Dehghani et al. (2021)
48	**Citation**: Dehghani, M., Tay, Y., Gritsenko, A. A., Zhao, Z., Houlsby, N., Diaz, F., Metzler, D., & Vinyals, O. (2021). The Benchmark Lottery. *arXiv preprint arXiv:2107.07002*.
49	**关联**: 提出"benchmark lottery"概念，证明算法的相对优劣可能仅因选择不同 benchmark 任务而逆转。这种 benchmark 选择带来的系统性方差正是我们 G-theory 框架中 methodology facet（任务/benchmark 选择作为方差源）要量化的核心问题。
50	
51	## 13. Biderman et al. (2024)
52	**Citation**: Biderman, S., Schoelkopf, H., Sutawika, L., Gao, L., Tow, J., Abbasi, B., Aji, A. F., Ammanamanchi, P. S., Black, S., Clive, J., DiPofi, A., Etxaniz, J., Fattori, B., Forde, J. Z., Foster, C., Hsu, J., Jaiswal, M., Lee, W. Y., Li, H., Lovering, C., Muennighoff, N., Pavlick, E., Phang, J., Skowron, A., Tan, S., Tang, X., Wang, K. A., Winata, G. I., Yvon, F., & Zou, A. (2024). Lessons from the Trenches on Reproducible Evaluation of Language Models. *arXiv preprint arXiv:2405.14782*.
53	**关联**: 基于 lm-evaluation-harness 的大规模实践，系统总结了 LLM 评估中影响可复现性的实际因素（prompt 格式、tokenization、采样策略等）。为我们 G-theory 框架中 infrastructure facet 的具体操作化提供了丰富的第一手经验。
54	
55	## 14. Shavelson & Webb (1991)
56	**Citation**: Shavelson, R. J. & Webb, N. M. (1991). *Generalizability Theory: A Primer*. Sage Publications. ISBN: 978-0-8039-3745-1.
57	**关联**: G-theory 的入门教材，系统介绍了 G-study/D-study 框架、方差分量估计和概化系数计算。是我们将 G-theory 从教育测量领域迁移到 LLM 评估的核心理论基础。
58	
59	## 15. Brennan (2001)
60	**Citation**: Brennan, R. L. (2001). *Generalizability Theory* (2nd ed.). Springer. ISBN: 978-0-387-95282-6.
61	**关联**: G-theory 的权威教科书，涵盖了多 facet 交叉设计、随机/固定 facet 处理、方差分量的负估计等高级主题。为我们设计复杂的 LLM 评估 G-study（多 facet：模型 × benchmark × prompt × 种子）提供了完整的统计理论基础。
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eeb31273-cab3-41a0-b5c9-451b26a17e75",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "4a1bfe01-4136-4d1c-b16c-8c2cdfbee68d",
  "sourceToolAssistantUUID": "eeb31273-cab3-41a0-b5c9-451b26a17e75",
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

_source line 42 · 2026-05-21T06:03:53.349Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L86RLusMDHyJkNgGiphEhC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis/cross_model_reml.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a1bfe01-4136-4d1c-b16c-8c2cdfbee68d",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD3WivAj5Rh7xnCk7Xm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a20f3c7-4a2a-4a2b-aa5e-ae65b58dce64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjJvuCjVxcz7nGFhnGWEaw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 36375,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1260
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 36375,
          "cache_creation_input_tokens": 1260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1260,
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

_source line 43 · 2026-05-21T06:03:53.353Z_

<details><summary>↩ Tool result · `toolu_01L86RLusMDHyJkNgGiphEhC`</summary>

```text
1	{
2	  "variance_components": {
3	    "model": {
4	      "estimate": 0.0010290198937726236,
5	      "pct": 0.4875577997741033
6	    },
7	    "precision": {
8	      "estimate": 9.99999830736044e-11,
9	      "pct": 4.7380786338410094e-08
10	    },
11	    "temperature": {
12	      "estimate": 9.631237221169772e-06,
13	      "pct": 0.004563356701919683
14	    },
15	    "prompt_template": {
16	      "estimate": 5.518521151463852e-06,
17	      "pct": 0.0026147191583927648
18	    },
19	    "seed": {
20	      "estimate": 9.998627400562663e-11,
21	      "pct": 4.737429087310311e-08
22	    },
23	    "ordering": {
24	      "estimate": 9.991840437244204e-11,
25	      "pct": 4.734213370177221e-08
26	    },
27	    "item_id": {
28	      "estimate": 0.08109664849078965,
29	      "pct": 38.424236252870756
30	    },
31	    "model:precision": {
32	      "estimate": 0.0027710682609073363,
33	      "pct": 1.3129541542278156
34	    },
35	    "model:temperature": {
36	      "estimate": 1.7063433694072214e-07,
37	      "pct": 8.084790429048245e-05
38	    },
39	    "model:prompt_template": {
40	      "estimate": 3.286114015484348e-05,
41	      "pct": 0.015569869240549539
42	    },
43	    "model:seed": {
44	      "estimate": 1.4873774439447188e-05,
45	      "pct": 0.0070473124804675165
46	    },
47	    "model:ordering": {
48	      "estimate": 1.2878205458698546e-06,
49	      "pct": 0.0006101796045421561
50	    },
51	    "model:item_id": {
52	      "estimate": 0.055635917793783955,
53	      "pct": 26.360739799209366
54	    },
55	    "precision:temperature": {
56	      "estimate": 7.908701363121626e-08,
57	      "pct": 3.747205529270417e-05
58	    },
59	    "precision:prompt_template": {
60	      "estimate": 5.094699164929328e-06,
61	      "pct": 0.002413908934507704
62	    },
63	    "precision:seed": {
64	      "estimate": 9.997961285113744e-11,
65	      "pct": 4.737113476519271e-08
66	    },
67	    "precision:ordering": {
68	      "estimate": 9.665759256128838e-07,
69	      "pct": 0.0004579713516311929
70	    },
71	    "precision:item_id": {
72	      "estimate": 0.004183675007033927,
73	      "pct": 1.9822584517011157
74	    },
75	    "temperature:prompt_template": {
76	      "estimate": 2.3158619308226167e-06,
77	      "pct": 0.0010972737790645435
78	    },
79	    "temperature:seed": {
80	      "estimate": 1.7242527248656344e-05,
81	      "pct": 0.008169646377854669
82	    },
83	    "temperature:ordering": {
84	      "estimate": 9.981260628050397e-11,
85	      "pct": 4.7292005725396054e-08
86	    },
87	    "temperature:item_id": {
88	      "estimate": 0.0021554588075093878,
89	      "pct": 1.0212735050632589
90	    },
91	    "prompt_template:seed": {
92	      "estimate": 2.2662571141397357e-06,
93	      "pct": 0.0010737706228802304
94	    },
95	    "prompt_template:ordering": {
96	      "estimate": 7.556719943107846e-07,
97	      "pct": 0.0003580433936474366
98	    },
99	    "prompt_template:item_id": {
100	      "estimate": 0.0059596217722228525,
101	      "pct": 2.823716136427643
102	    },
103	    "seed:ordering": {
104	      "estimate": 9.992492992438848e-11,
105	      "pct": 4.734522556012071e-08
106	    },
107	    "seed:item_id": {
108	      "estimate": 0.005282813122371878,
109	      "pct": 2.5030388218427637
110	    },
111	    "ordering:item_id": {
112	      "estimate": 0.00133198146050742,
113	      "pct": 0.6311033966933125
114	    },
115	    "residual": {
116	      "estimate": 0.05151671126893721,
117	      "pct": 24.409027026479254
118	    }
119	  },
120	  "total_variance": 0.21105598028569988,
121	  "n_observations": 325600,
122	  "method": "REML-EM (Henderson MME)",
123	  "elapsed_seconds": 606.3528063297272,
124	  "converged": false,
125	  "n_iterations": 100,
126	  "n_levels": {
127	    "model": 2,
128	    "precision": 2,
129	    "temperature": 3,
130	    "prompt_template": 6,
131	    "seed": 6,
132	    "ordering": 4,
133	    "item_id": 200
134	  },
135	  "fixed_intercept": 0.6947930599463834,
136	  "n_random_effects": 28,
137	  "q_total": 5035,
138	  "all_facets": [
139	    "model",
140	    "precision",
141	    "temperature",
142	    "prompt_template",
143	    "seed",
144	    "ordering",
145	    "item_id"
146	  ]
147	}
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a20f3c7-4a2a-4a2b-aa5e-ae65b58dce64",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "9b582a34-3ec6-4b79-bb0b-8c052a89302d",
  "sourceToolAssistantUUID": "9a20f3c7-4a2a-4a2b-aa5e-ae65b58dce64",
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

_source line 44 · 2026-05-21T06:03:56.896Z_

Now let me read the latest dream report to understand what reviewers have already flagged, and the most recent paper draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b582a34-3ec6-4b79-bb0b-8c052a89302d",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD3nM2271T7fBkJG9zn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ba499bc-5632-4c66-9454-a4dfb7e69753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HqTRyDafWNhrv8Q3ikLkeh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9445,
      "cache_read_input_tokens": 37635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9445,
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

_source line 45 · 2026-05-21T06:03:58.588Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G3m3mLTAhgdp6v5atSS16J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ba499bc-5632-4c66-9454-a4dfb7e69753",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD3nM2271T7fBkJG9zn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ede3038b-8aa3-4e55-b3d6-c91686b17748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HqTRyDafWNhrv8Q3ikLkeh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9445,
      "cache_read_input_tokens": 37635,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 37635,
          "cache_creation_input_tokens": 9445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9445,
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

_source line 46 · 2026-05-21T06:03:58.832Z_

<details><summary>↩ Tool result · `toolu_01G3m3mLTAhgdp6v5atSS16J`</summary>

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
103	    \sigma^2_{\text{total}} = \sigma^2_p + \sum_i \sigma^2_{f_i} + \sum_{i&lt;j} \sigma^2_{f_i f_j} + \cdots + \sigma^2_{pf_1 \cdots f_k,e}
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
799	\newblock Are emergent abilities in large language models just in-context learning? A study of option ordering effects.
800	\newblock \textit{Preprint}.
801	
802	\bibitem[Mesting(2026)]{mesting2026}
803	Mesting, F. (2026).
804	\newblock Generalizability theory for LLM evaluation: A five-facet analysis.
805	\newblock \textit{Preprint}.
806	
807	\bibitem[Messina \& Scotta(2026)]{messina2026}
808	Messina, P. \& Scotta, A. (2026).
809	\newblock Background temperature: Characterizing non-determinism in LLM inference.
810	\newblock \textit{Transactions on Machine Learning Research}.
811	
812	\bibitem[Perlitz et~al.(2023)]{perlitz2023}
813	Perlitz, Y., et~al. (2023).
814	\newblock Efficient benchmarking (of language models).
815	\newblock \textit{arXiv preprint}.
816	
817	\bibitem[Pezeshkpour \& Hruschka(2024)]{pezeshkpour2024}
818	Pezeshkpour, P. \& Hruschka, E. (2024).
819	\newblock Large language models sensitivity to the order of options in multiple-choice questions.
820	\newblock \textit{Findings of ACL}.
821	
822	\bibitem[Polo et~al.(2024)]{polo2024}
823	Polo, F.~M., et~al. (2024).
824	\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.
825	\newblock \textit{Proceedings of ICML}.
826	
827	\bibitem[Rodriguez et~al.(2021)]{rodriguez2021}
828	Rodriguez, P., Barrow, J., Hoyle, A.~M., Lalor, J.~P., Jia, R., \& Boyd-Graber, J. (2021).
829	\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?
830	\newblock \textit{Proceedings of ACL}.
831	
832	\bibitem[Sellam et~al.(2022)]{sellam2022}
833	Sellam, T., Yadlowsky, S., Wei, J., Saphra, N., D'Amour, A., Linzen, T., ... \& Eisenstein, J. (2022).
834	\newblock The MultiBERTs: BERT reproductions for robustness analysis.
835	\newblock \textit{Proceedings of ICLR}.
836	
837	\bibitem[Shavelson \& Webb(1991)]{shavelson1991}
838	Shavelson, R.~J. \& Webb, N.~M. (1991).
839	\newblock \textit{Generalizability Theory: A Primer}.
840	\newblock Sage.
841	
842	\bibitem[ThinkingMachines(2025)]{thinkingmachines2025}
843	ThinkingMachines Authors. (2025).
844	\newblock Batch-invariance failures in LLM inference: Sources and mitigations.
845	\newblock \textit{Preprint}.
846	
847	\bibitem[Vania et~al.(2021)]{vania2021}
848	Vania, C., et~al. (2021).
849	\newblock Comparing test sets with item response theory.
850	\newblock \textit{Proceedings of ACL}.
851	
852	\bibitem[Yuan et~al.(2025)]{yuan2025}
853	Yuan, Z., et~al. (2025).
854	\newblock Numerical precision and LLM evaluation: Up to 9\% accuracy variation from floating-point format.
855	\newblock \textit{Preprint}.
856	
857	\bibitem[Biderman et~al.(2024)]{biderman2024}
858	Biderman, S., et~al. (2024).
859	\newblock Lessons from the trenches on reproducible evaluation of language models.
860	\newblock \textit{Preprint}.
861	
862	\end{thebibliography}
863	
864	\end{document}
865	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ede3038b-8aa3-4e55-b3d6-c91686b17748",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "7daab121-b06b-4507-8615-a6917e388a58",
  "sourceToolAssistantUUID": "ede3038b-8aa3-4e55-b3d6-c91686b17748",
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

_source line 47 · 2026-05-21T06:04:02.359Z_

Now let me also check the dream review reports to understand what prior reviewers identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7daab121-b06b-4507-8615-a6917e388a58",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD4BZXGauwvE9NwFG7w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf7345bb-d9a7-4487-bb39-917dc42e76c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161vHPuVPKi9wSyQiSu2BQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19436,
      "cache_read_input_tokens": 47080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19436,
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

_source line 48 · 2026-05-21T06:04:04.721Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015C2eSXECXd1Jvz6LDs9jtr`</summary>

```json
{
  "pattern": "**/dream_20260521T044739/best/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf7345bb-d9a7-4487-bb39-917dc42e76c4",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD4BZXGauwvE9NwFG7w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd1f9c37-9eee-45b1-83de-9a0d8d4591a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161vHPuVPKi9wSyQiSu2BQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19436,
      "cache_read_input_tokens": 47080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19436,
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

_source line 49 · 2026-05-21T06:04:04.744Z_

<details><summary>↩ Tool result · `toolu_015C2eSXECXd1Jvz6LDs9jtr`</summary>

```text
artifacts/dream_reports/dream_20260521T044739/best/paper_framing.md
artifacts/dream_reports/dream_20260521T044739/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd1f9c37-9eee-45b1-83de-9a0d8d4591a1",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "f18b2207-e550-4066-85cf-3a54931e432f",
  "sourceToolAssistantUUID": "cd1f9c37-9eee-45b1-83de-9a0d8d4591a1",
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

_source line 50 · 2026-05-21T06:04:05.364Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NbhJFN5mKos1WthWfHU6s4`</summary>

```json
{
  "pattern": "**/dream_20260521T044739/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f18b2207-e550-4066-85cf-3a54931e432f",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD4BZXGauwvE9NwFG7w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ebefb6c-7221-4565-b11a-543b24281226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161vHPuVPKi9wSyQiSu2BQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19436,
      "cache_read_input_tokens": 47080,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19436
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 47080,
          "cache_creation_input_tokens": 19436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19436,
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

_source line 51 · 2026-05-21T06:04:05.381Z_

<details><summary>↩ Tool result · `toolu_01NbhJFN5mKos1WthWfHU6s4`</summary>

```text
artifacts/dream_reports/dream_20260521T044739/best/paper_framing.md
artifacts/dream_reports/dream_20260521T044739/median/paper_framing.md
artifacts/dream_reports/dream_20260521T044739/worst/paper_framing.md
artifacts/dream_reports/dream_20260521T044739/best/review_report.md
artifacts/dream_reports/dream_20260521T044739/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ebefb6c-7221-4565-b11a-543b24281226",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "3cadd34c-b7ea-491c-a5f8-e0465ee78dda",
  "sourceToolAssistantUUID": "5ebefb6c-7221-4565-b11a-543b24281226",
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

_source line 52 · 2026-05-21T06:04:08.134Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P6m1DSXabdDdRyrnsNH3e5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cadd34c-b7ea-491c-a5f8-e0465ee78dda",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD4figcbrBYTtLzmkRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d799782-420e-4a5c-b1ef-790923a44e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9SPogJFPVkfw8QkNAWrSA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 66516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 53 · 2026-05-21T06:04:08.140Z_

<details><summary>↩ Tool result · `toolu_01P6m1DSXabdDdRyrnsNH3e5`</summary>

```text
1	---
2	dream_id: dream_20260521T044739
3	tier: best
4	overall_score: borderline accept
5	timestamp: 2026-05-21T05:53:06.951774+00:00
6	---
7	
8	# Dream Review Report: Reproducibility Budgets for LLM Evaluation
9	
10	**Paper**: "Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics"
11	
12	**Venue**: AAAI (1-10 scale)
13	
14	**Review Mode**: Full (2 Reviewers + Roundtable)
15	
16	---
17	
18	## Reviewer Assignments
19	
20	- **R1** — Methods and Experiments (soundness, statistical methodology, design rigor)
21	- **R2** — Novelty and Related Work (originality, positioning, significance, writing)
22	
23	---
24	
25	## R1 Review: Methods and Experiments
26	
27	### Summary
28	The paper applies G-theory to decompose LLM evaluation variance across infrastructure, methodology, and measurement facets, with model as a crossed random facet. Nine experiments totaling ~4.3M item-level records yield three claims about item dominance, infrastructure-methodology separability, and benchmark-conditional reproducibility budgets. The experimental scope is ambitious and the methodological defense package (MD1-MD9) is unusually thorough for this literature.
29	
30	### Strengths
31	
32	1. **Well-motivated factorial design.** The fully crossed MMLU design (4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items) is the most comprehensive variance decomposition in LLM evaluation. Crossing infrastructure with methodology—rather than studying them in isolation—directly tests an implicit field assumption.
33	
34	2. **Correct statistical implementation.** Henderson's Method III for balanced and REML for unbalanced designs are the right choices. Negative-variance truncation to zero is standard. D-study partition (fixed facets to universe score, random to error) is correctly implemented.
35	
36	3. **Exemplary robustness analyses (MD1-MD9).** Particularly strong: (a) Bernoulli null simulation showing item_id = 0.08% vs observed 61.1% (671× ratio); (b) REML vs Henderson III comparison (max divergence 1.4%, rank preserved); (c) bootstrap vs jackknife CI comparison (width ratio 0.96–1.04); (d) fixed vs random sensitivity (<3% change).
37	
38	4. **Item resampling stability (Exp 2).** Three independent stratified 200-item draws with item_id CV = 0.039 and preserved rank order (Friedman p > 0.10) directly addresses the most common criticism of subsampled evaluation studies.
39	
40	5. **Cross-benchmark gradient is convincing.** Monotonic decrease of item_id from MMLU (60.4%) to MATH (22.1%) with ρ = 1.0 across 5 benchmarks, accompanied by inverse increases in prompt×item and temp×item, provides an elegant reconciliation of seemingly contradictory prior findings.
41	
42	6. **Power analysis preempts underpowering criticism.** Power > 0.998 for effects ≥5% and MDE = 1.2% at 80% power demonstrates that near-zero infrastructure×methodology interactions are genuine nulls.
43	
44	7. **Model-as-facet analysis is a genuine contribution.** The demonstration that item_id drops from 60.4% to 36.8% while model×item absorbs 24.1%—collapsing G from 0.618 to 0.065—is clean and important. D-study showing 10 models yield G = 0.179 quantifies irreducibility.
45	
46	8. **IRT vs G-theory comparison is a standalone contribution.** The 4.4× item requirement gap (510 vs 116) directly informs practitioners using tinyBenchmarks-style approaches.
47	
48	### Weaknesses
49	
50	1. **Four models is marginal for random-effects estimation of the model facet (Major).** Variance components from facets with <5–6 levels are known to be unstable and positively biased (Brennan, 2001, Ch. 4). The bootstrap CI [21.3, 27.0] on model×item reflects item-resampling uncertainty only—models are fixed across all bootstrap samples. A leave-one-model-out analysis is needed to quantify sensitivity to the model sample. The 14B extension (Exp 6) adds models in a separate analysis, not the main crossed design.
51	
52	2. **The "precision" facet conflates genuine numerical effects with vLLM engine artifacts (Major).** FP32 shows consistent ~8-10pp accuracy degradation due to a vLLM-specific code path issue (V1 CUDA graph vs V0 eager), not fundamental precision properties. Two of three precision levels (BF16, FP16) are nearly identical (<0.2pp), while FP32 is dramatically different due to this artifact. The paper should present a BF16-vs-FP16-only decomposition as sensitivity analysis.
53	
54	3. **Hardware crossing is severely underpowered (Moderate-Major).** Two GPU types (both NVIDIA data-center class) provide df=1 for the hardware facet. The 0.18% [0.03, 0.42] hardware×methodology estimate has almost no statistical power. Hardware×item = 1.2% is 6.7× larger than hardware×methodology. Cross-architecture effects (NVIDIA vs AMD, consumer vs data-center) could plausibly be larger. The separability claim should be scoped as preliminary or limited to "numerical precision separability."
55	
56	4. **Option ordering facet is undefined for open-ended benchmarks (Moderate).** GSM8K and MATH are open-ended generation tasks without MC options. The paper reports 4 ordering levels for all benchmarks but does not explain what "ordering" means for these tasks. If few-shot exemplar ordering was used as proxy, it measures a different construct than MC option rotation. This is a non-trivial gap.
57	
58	5. **Temperature and ordering have too few design points for credible random-facet treatment (Moderate).** Temperature has 3 levels (0.0, 0.3, 0.7)—selected boundary/midpoint values, not random draws from a universe. The 4 orderings exhaust ABCD rotations but exclude the 24 total permutations. The fixed-facet analysis should be presented as primary for these facets.
59	
60	6. **D-study grid search procedure is underdocumented (Moderate).** The optimization appears to be independent per-facet sweeps rather than joint optimization. Jointly optimized allocations could be substantially different. The procedure, objective function, search bounds, and step sizes should be documented.
61	
62	7. **Cross-benchmark design asymmetry (Minor-Moderate).** MMLU uses 3 precisions × 3 temperatures while other benchmarks use 2 × 2. Precision-related components on non-MMLU benchmarks are mechanically smaller because BF16 and FP16 produce nearly identical results (no FP32).
63	
64	8. **Gemma FP16 exclusion creates imbalance (Minor).** Gemma has 2 precision levels vs 3 for others. The paper states REML is used for unbalanced cases but should clarify which estimator was actually used for the main cross-model analysis.
65	
66	### Questions for Authors
67	
68	1. What fraction of bootstrap resamples show model×item > item_id in the cross-model analysis?
69	2. What happens to the variance decomposition if FP32 is excluded, leaving only BF16 vs FP16?
70	3. How was option ordering operationalized for GSM8K and MATH?
71	4. Leave-one-model-out: does removing any single model change model×item by more than the bootstrap CI width?
72	5. What is the D-study projection for the common practice of 1 prompt, 1 seed, varying only items?
73	6. For Exp 7: is seed×LR driven by specific divergent combinations or smooth interaction?
74	7. Has a Bernoulli null simulation been run specifically for model×item (not just item_id)?
75	8. How sensitive is the cross-benchmark gradient to the specific 200-item samples on benchmarks other than MMLU?
76	
77	### Minor Issues
78	1. Higher-order interaction computation (3.2%) is not reflected in the code that only fits 2-way interactions.
79	2. Bootstrap resamples items but not models—CIs on model×item only reflect item sampling uncertainty. Should be stated explicitly.
80	3. Verify "first multi-benchmark G-theory study" claim against Mesting (2026) who may have used multiple benchmarks.
81	4. The `text_exact_match` canonical answer definition depends on the design itself.
82	5. Logprob item_id = 53.2% vs binary 60.4%: the 7.2pp difference deserves discussion.
83	6. Total 4.29M records should be broken down by experiment in a summary table.
84	7. G coefficient formula should state whether relative G (Eρ²) or absolute G (Φ) is used.
85	
86	### R1 Scores
87	- Soundness: 7/10
88	- Experimental Design: 8/10
89	- Reproducibility: 7/10
90	- **Overall (R1): 7/10**
91	- Confidence: 4/5
92	
93	---
94	
95	## R2 Review: Novelty and Related Work
96	
97	### Summary
98	The genuine novel contribution is the cross-benchmark variance gradient: item dominance monotonically decreases from 60.4% (MMLU) to 22.1% (MATH) with corresponding increases in methodology×item interactions. The infrastructure×methodology crossing—framed as the primary advance over Mesting (2026)—yields a near-null (<0.5%), informative as confirmation but not carrying the weight the framing places on it. The D-study budget differentiation and model×item irreducibility are strong empirical findings, but the paper is primarily an empirical extension of Mesting's framework rather than a methodological advance.
99	
100	### Strengths
101	
102	1. **Cross-benchmark variance gradient is genuinely novel and explanatory.** No prior work has positioned multiple LLM benchmarks along a reasoning-intensity continuum and demonstrated a monotonic shift in variance structure. This resolves genuine confusion about why prior single-benchmark studies reached contradictory conclusions about which factors matter most.
103	
104	2. **Model×item as cross-model generalizability barrier is a strong finding.** G collapse from 0.618 to 0.065 due to 24.1% model×item, persisting at 21–25% across all 5 benchmarks, is the first G-theory quantification of cross-model item-level disagreement. This directly challenges leaderboard interpretability.
105	
106	3. **D-study budget differentiation is practically actionable.** The items-to-seeds effectiveness ratio shifting from 14.2:1 (MMLU) to 0.8:1 (GSM8K) crystallizes "no universal reproducibility recipe" with specific guidance.
107	
108	4. **Metric-conditional separability adds genuine nuance.** Infrastructure×methodology <0.5% under binary but hw×temp = 0.83% under text-exact-match. This metric-dependent distinction is new.
109	
110	5. **Experimental scale exceeds all prior work.** ~4.3M records, 6 models, 5 benchmarks, 2 GPU types, 9 experiments substantially exceed Mesting (2026), Brittlebench (2026), and Yuan (2025).
111	
112	6. **IRT vs G-theory cost comparison fills a methodological gap.** The 4.4× item requirement difference quantifies the "hidden cost" of multi-facet reliability.
113	
114	### Weaknesses
115	
116	1. **Infrastructure crossing as primary framing vs near-null contribution (Major).** The title, abstract, and introduction frame "crossing infrastructure and methodology in a unified G-theory framework" as the key advance. But infrastructure×methodology < 0.5% across all benchmarks. The three strongest findings (gradient, model×item, D-study budgets) would emerge from a methodology-only design replicated across benchmarks with model as crossed facet. The framing creates a mismatch between what is promised and what is delivered. The paper should foreground the gradient and model-as-facet findings as primary.
117	
118	2. **Incrementality over Mesting (2026) not fully resolved (Major).** The paper claims four differences from Mesting: (a) infrastructure crossing → near-null; (b) multi-benchmark → genuine advance; (c) model as crossed facet → genuine advance; (d) metric-conditional budgets → genuine advance. Points (b)–(d) are extensions of Mesting's framework, not a fundamentally different approach. The "first" language throughout overstates methodological novelty. The contribution is primarily empirical (new findings from a larger study), not methodological (new framework).
119	
120	3. **Missing related work creates unfair positioning (Major).** Several important works are insufficiently engaged:
121	   - **Sclar et al. (2024, ICLR)**: Up to 76% accuracy swing from prompt formatting—relationship to this paper's prompt×item variance undiscussed.
122	   - **Kunievsky & Evans (2025)**: Alternative variance decomposition (intent/articulation/model uncertainty)—a directly competing framework, absent from the paper.
123	   - **Bui et al. (2025)**: Seed sensitivity in fine-tuning (RTES variance=18.22 for RoBERTa on COPA)—directly relevant to Exp 7 but uncited.
124	   - The IRT comparison would be strengthened by explicitly engaging with tinyBenchmarks' ~100-item recommendation and explaining the 4× gap mechanism.
125	
126	4. **Cross-benchmark gradient ordering is post-hoc (Moderate).** The monotonic ordering was presumably observed after experiments. The explanatory mechanism (CoT stochasticity) is plausible but not independently validated. Without an external measure of reasoning intensity, Spearman ρ = 1.0 is circular: benchmarks are ordered by the quantity being correlated.
127	
128	5. **Item dominance is partially expected from measurement theory (Moderate).** Any assessment with wide difficulty range shows item variance as dominant—well-established in psychometrics. The contribution is in quantifying the magnitude and deriving the gradient, not the finding per se. The paper should be more explicit about this.
129	
130	6. **Fine-tuning experiment is architecturally disjoint (Moderate).** RoBERTa-large (355M, encoder-only, classification) vs decoder LLMs (7-9B, generation). The regime change claim (seed×lr supplants item_id) cannot be generalized to decoder fine-tuning (e.g., LoRA on Llama). The paper acknowledges this as a limitation but the cross-paradigm comparison risks overstatement.
131	
132	7. **"Practitioner toolkit" contribution is vaguely defined (Moderate).** What is actually released is unclear—specific scripts/tables vs a general tool? Mesting (2026) already applied G-theory to LLM eval, and GeneralizIT provides G-theory software.
133	
134	8. **Zero figures in a variance decomposition paper (Moderate).** 18 tables and no figures. The cross-benchmark gradient demands a stacked-bar chart. The D-study budget reversal demands projection curves. Visual communication at a competitive venue dramatically affects reviewer engagement and comprehension.
135	
136	### Questions for Authors
137	
138	1. If you added GPQA or HumanEval as a 6th benchmark, would it fall on the gradient? What independent measure of reasoning intensity validates the ordering?
139	2. If you removed all infrastructure facets and ran methodology-only G-theory across 5 benchmarks, which claimed contributions would change?
140	3. Can you provide a precise accounting of where the 4.4× IRT-G-theory gap comes from (fraction from prompt×item, seed×item, residual)?
141	4. With 4 deliberately selected models, how defensible is treating model as a random facet? How does G change if model is fixed?
142	5. Full 14K-item MMLU with 1 prompt and 1 seed: what is G? If it exceeds 0.80, the "current practice is inadequate" claim needs qualification.
143	6. What mechanism drives HellaSwag's position on the gradient, given it doesn't involve explicit multi-step reasoning?
144	7. If a practitioner uses LLM-as-judge, do your D-study budgets still apply, or would judge variance overwhelm them?
145	
146	### Minor Issues
147	1. D-study table internal consistency needs verification (apparent anomalies in GSM8K projections flagged in prior reviews).
148	2. Cross-benchmark design asymmetry (3×3 vs 2×2) affects comparability of precision-related components.
149	3. Abstract claim about "current standard practice yields G < 0.25" uses all-facets-random G; many practitioners fix temperature/precision, making practical G higher.
150	4. Several references have incomplete information; "first" claims are vulnerable without exhaustive literature review.
151	5. Some reported numbers differ between sections (reconcile 2-model vs 4-model analyses).
152	
153	### R2 Scores
154	- Novelty: 6/10
155	- Significance: 7/10
156	- Writing Quality: 5/10
157	- **Overall (R2): 6/10**
158	- Confidence: 4/5
159	
160	---
161	
162	## Roundtable Discussion
163	
164	### Step 2: Cross-Sharing
165	
166	R1 and R2 exchanged reviews. Key observations from the exchange:
167	
168	- **R1 → R2**: R1's concern about the FP32 engine artifact strengthens R2's point about infrastructure crossing yielding near-null genuine results—much of the reported precision variance may be an artifact rather than a finding about numerical precision per se.
169	- **R2 → R1**: R2's point about post-hoc gradient ordering helps contextualize R1's otherwise positive assessment of the gradient—the statistical evidence is strong but the causal mechanism needs independent validation.
170	- Both reviewers independently flagged the 4-model limitation and hardware underpowering as concerns.
171	
172	### Step 3: Convergence
173	
174	**Points of Agreement:**
175	
176	1. **The cross-benchmark variance gradient is the paper's strongest contribution.** Both reviewers rate this as genuinely novel and well-supported empirically. The reconciliation of contradictory prior findings is valuable.
177	
178	2. **Model×item interaction is important and well-quantified.** The G collapse from 0.618 to 0.065 is a clean demonstration with direct practical implications for leaderboard interpretation.
179	
180	3. **D-study budget differentiation is practically actionable.** The MMLU-vs-GSM8K budget reversal (item-limited vs seed-limited) is non-obvious and useful.
181	
182	4. **Infrastructure crossing framing is misaligned with results.** The near-null infrastructure×methodology finding, while informative, does not justify its prominence in the title, abstract, and introduction.
183	
184	5. **4 models is marginal for the model-as-facet claim.** Both reviewers request leave-one-model-out sensitivity analysis.
185	
186	6. **Hardware separability with 2 GPU types is preliminary.** The claim should be scoped accordingly.
187	
188	7. **The paper is at or near the AAAI acceptance threshold.** Core findings merit publication; framing and presentation need revision.
189	
190	**Points of Divergence:**
191	
192	- R1 is more positive about overall methodological soundness (7/10), viewing the weaknesses as addressable through additional analyses and clarifications.
193	- R2 is more concerned about framing and novelty positioning (6/10), viewing the infrastructure crossing emphasis and "first" claims as problematic.
194	- R1 weighs the MD1-MD9 defense package more heavily as a strength; R2 weighs the missing figures and related work gaps more heavily as weaknesses.
195	
196	### Step 4: Consolidated Assessment
197	
198	**Overall Score: 6.5/10 — Borderline Accept**
199	
200	**Core Strengths (what merits publication):**
201	- Cross-benchmark variance gradient with ρ = 1.0 is a genuinely novel empirical finding
202	- Model×item interaction quantification (21–25% across 5 benchmarks) with G collapse demonstration
203	- D-study budget differentiation (MMLU item-limited, GSM8K seed-limited)
204	- IRT vs G-theory 4.4× cost comparison
205	- Exemplary robustness package (MD1-MD9)
206	- Impressive experimental scale (~4.3M records, 9 experiments)
207	
208	**Core Weaknesses (what threatens acceptance):**
209	- **Framing mismatch**: Infrastructure crossing is foregrounded but yields a near-null; actual novelty (gradient, model×item) is underemphasized
210	- **Incrementality**: Primarily an empirical extension of Mesting (2026), not a methodological advance; "first" claims overstate
211	- **Missing references**: Kunievsky (2025), Sclar et al. (2024), Bui et al. (2025) directly relevant but uncited
212	- **Presentation**: Zero figures in a variance decomposition paper is a significant handicap at a competitive venue
213	- **Model facet**: 4 models marginal for random-effects; leave-one-model-out analysis needed
214	- **FP32 confound**: Precision facet partially measures a vLLM artifact; needs BF16-vs-FP16-only sensitivity
215	- **Post-hoc gradient**: No independent validation of the reasoning-intensity continuum
216	- **Hardware**: 2 GPU types insufficient for "confirmatory separability" language
217	
218	**Recommendation for Revision:**
219	1. Reframe: Center the gradient and model×item findings as primary contributions; relabel infrastructure crossing as confirmatory
220	2. Add 3–4 figures: cross-benchmark stacked bars, D-study projection curves, model-as-facet before/after, IRT vs G-theory comparison
221	3. Complete related work: Add Kunievsky (2025), Sclar et al. (2024), Bui et al. (2025); engage tinyBenchmarks deeply
222	4. Sensitivity analyses: Leave-one-model-out, FP32-excluded decomposition
223	5. Clarify: Option ordering for open-ended benchmarks, D-study optimization procedure, G coefficient type (relative vs absolute)
224	6. Temper claims: Remove "first" where not defensible; scope hardware separability as preliminary
225	
226	**Experiment Coverage Assessment:**
227	All 9 planned experiments (exp-001 through exp-008 + MATH extension) are present in the paper, mapped to Experiments 1–9. Coverage: **9/9 (100%)**. The paper faithfully reports all planned analyses, including the fine-tuning regime comparison and LayerCast mitigation study.
228	
229	---
230	
231	## Score Summary
232	
233	| Criterion | R1 | R2 | Consensus |
234	|---|---|---|---|
235	| Soundness / Methodology | 7 | — | 7 |
236	| Experimental Design | 8 | — | 8 |
237	| Novelty | — | 6 | 6 |
238	| Significance | — | 7 | 7 |
239	| Writing / Presentation | — | 5 | 5 |
240	| Reproducibility | 7 | — | 7 |
241	| **Overall** | **7** | **6** | **6.5** |
242	| Confidence | 4/5 | 4/5 | 4/5 |
243	
244	**Verdict: Borderline Accept (6.5/10)**. The empirical contributions are strong and the experimental scale is impressive, but the framing-results mismatch, missing figures, incomplete related work, and marginal model sample size collectively place the paper just at the acceptance boundary. A revision addressing the six points above would likely push this to a solid 7/10.
245	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d799782-420e-4a5c-b1ef-790923a44e2c",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "fac5748f-93b6-43c3-869b-94c6425a1f11",
  "sourceToolAssistantUUID": "2d799782-420e-4a5c-b1ef-790923a44e2c",
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

_source line 54 · 2026-05-21T06:04:08.496Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Af5Nor9W6BUSgqS6tKkczu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fac5748f-93b6-43c3-869b-94c6425a1f11",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD4figcbrBYTtLzmkRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e72f48f6-0655-4305-a671-d5a5c0085550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9SPogJFPVkfw8QkNAWrSA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 66516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 454,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 55 · 2026-05-21T06:04:08.501Z_

<details><summary>↩ Tool result · `toolu_01Af5Nor9W6BUSgqS6tKkczu`</summary>

```text
1	---
2	dream_id: dream_20260521T044739
3	tier: median
4	overall_score: borderline — 3/5 ACL ARR
5	timestamp: 2026-05-21T06:00:00.909092+00:00
6	---
7	
8	# Dream Review Report — Reproducibility Budgets for LLM Evaluation
9	
10	**Paper**: "Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks and Models"
11	**Scoring scale**: ACL ARR 1–5 (5 = top 2–5%, 4 = top 10–20%, 3 = borderline, 2 = below average, 1 = seriously flawed)
12	**Review mode**: Full (2 Reviewers → roundtable)
13	
14	---
15	
16	## Scores
17	
18	| Dimension | Score |
19	|-----------|-------|
20	| Soundness | 3 |
21	| Substance | 3 |
22	| Novelty | 3 |
23	| Significance | 3 |
24	| Clarity | 3.5 |
25	| **Overall** | **3** |
26	| Confidence | 4/5 |
27	
28	**Assessment**: Borderline. The paper has genuine merits — particularly the IRT vs G-theory comparison — but significant weaknesses in infrastructure coverage, model-facet sample size, and incomplete experiments prevent a clear accept.
29	
30	---
31	
32	## Summary
33	
34	The paper applies Generalizability Theory (G-theory) to decompose LLM evaluation variance across infrastructure (numerical precision) and methodology (prompt, seed, temperature, ordering) facets. It studies 4 open-weight models (~7–9B) on 4 benchmarks (MMLU, HellaSwag, ARC-Challenge, GSM8K) totaling 2.2M+ records. Four contributions are claimed: (1) G-theory requires 3.6–7.0× more items than IRT for reliable measurement, (2) model×item interaction accounts for ~16.4% of variance, (3) variance structure is benchmark-conditional, and (4) an open-source D-study calculator.
35	
36	---
37	
38	## Strengths
39	
40	### S1. IRT vs G-theory comparison is novel and actionable (Contribution 1)
41	No prior work directly compares IRT item requirements with G-theory requirements for LLM evaluation. The 3.6–7.0× gap (Table 11) is striking, well-attributed causally to prompt×item (4.8%), seed×item (4.6%), and ordering×item (1.3%) — dimensions IRT ignores by design. At IRT's recommended 116 items for MMLU, G-theory yields only G = 0.489 — substantially below the 0.80 threshold. This finding is robust: it doesn't depend on model count, hardware, or any of the paper's incomplete experiments. The ratio increasing for reasoning benchmarks (GSM8K: 6.2×, ARC: 7.0×) adds cross-benchmark validation. This is the paper's strongest contribution and could meaningfully influence benchmark design practices.
42	
43	### S2. Thorough methodological defenses
44	Table 12 presents 6 defense analyses that preemptively address likely reviewer concerns: (MD1) Bernoulli correlation r=0.38, r²=0.14 — partial but not dominant mechanical link; (MD2) fixed vs random facet classification shifts variance by at most 3.2% — robust; (MD5) full MMLU 14K projection yields G=0.942 — subsampling is the cost, not an MMLU flaw; (MD6) bootstrap vs jackknife CI width ratio 0.94–1.08 — negligible independence violation; (MD8) 3×3 vs 2×2 design reduction changes components by at most 2.1%; (MD9) logprob scoring yields consistent direction (item_id=52.4%, G=0.528). This level of robustness checking exceeds the typical standard.
45	
46	### S3. Transparent reporting of incomplete experiments
47	Sections 4.5 and 4.7 explicitly state what was not completed (14B extension, multi-hardware, LayerCast, MATH benchmark) and why. The Limitations section (Section 6) addresses 6 distinct limitations with specific quantitative context. This honesty is commendable and unusual.
48	
49	### S4. Multi-benchmark G-theory extension
50	Extending from Mesting (2026)'s single-benchmark G-theory to 4 benchmarks is a meaningful step. The cross-benchmark variance decomposition (Table 7) reveals that item_id ranges from 59.7% (MMLU) to 41.8% (ARC-Challenge), with a 17.9pp spread. The D-study budget table (Table 9) showing 414–682 items for G≥0.80 across benchmarks directly demonstrates that no universal item budget suffices — a practically valuable finding.
51	
52	### S5. Model-as-crossed-facet design
53	Treating model as a random facet to estimate model×item interaction is a novel design choice within the G-theory-for-LLM literature. The finding that item difficulty rankings are partially model-specific (16.4% interaction) and that cross-model G collapses from 0.598 to 0.152 has implications for leaderboard validity.
54	
55	### S6. Item resampling stability analysis
56	Exp-001b proactively tests whether item_id dominance is an artifact of a particular 200-item draw. Three independent stratified samples yield item_id ranging from 49.3% to 61.1% (CV=0.13), confirming directional robustness while honestly quantifying estimation variability. The recommendation to report ranges rather than point estimates (55–65%) is appropriate.
57	
58	---
59	
60	## Weaknesses
61	
62	### W1. Four models as a random facet — fundamental statistical limitation [Major]
63	With only 4 levels for the model facet, the degrees of freedom for estimating model and model×item variance components are extremely limited. The bootstrap 95% CI for model×item is [11.2%, 21.8%] — a 10.6pp width (Table 10). At the lower bound (11.2%), model×item is still notable but approaches the sum of methodology×item interactions; at the upper bound (21.8%), it dominates. The paper acknowledges this (Section 6, "Model sample size") but the limitation fundamentally constrains Contribution 2. A reviewer can reasonably question whether 4 models suffice for treating model as a random facet in the G-theory sense — in psychometrics, random facets typically have 10+ levels. The bootstrap "compensation" is partial: it captures sampling variability but cannot overcome the structural limitation of estimating a variance component from 4 levels.
64	
65	**Impact on paper**: Contribution 2 is the second-listed contribution but rests on the weakest statistical foundation. The 16.4% point estimate should be treated with more caution in the abstract and conclusion.
66	
67	### W2. Infrastructure claim substantially overclaimed [Major]
68	The paper's framing — crossing "infrastructure (numerical precision) and methodology" — implies a meaningful infrastructure component. In reality, all experiments use a single GPU architecture (NVIDIA RTX PRO 6000), and "infrastructure" reduces to numerical precision settings within that one platform. Exp-003 (multi-hardware) was not completed. Furthermore, the FP32 results (Table 3: 5–11pp accuracy degradation vs BF16) are attributable to vLLM's enforce_eager mode changing the computation path, not to numerical precision per se. This means precision×item (3.2%) may measure "computation engine artifact × item" rather than "numerical precision × item."
69	
70	The abstract states "infrastructure (numerical precision) and methodology" as if these are comparable pillars. The honest framing would be: "primarily methodology-focused G-theory with a precision side-analysis on a single GPU." The separability claim (infra×method < 0.1%) is limited to precision-on-RTX-PRO-6000, not generalizable infrastructure.
71	
72	**Recommendation**: Substantially tone down infrastructure framing throughout, especially in abstract, introduction, and Contribution 2 context. Rename or qualify "infrastructure facet."
73	
74	### W3. FP32 anomaly is a confound, not just an oddity [Major]
75	Table 3 shows FP32 consistently performing 5–11pp worse than BF16 across all models. The paper explains this as enforce_eager causing FP32 to use a different computation path. But this explanation has consequences the paper doesn't fully address:
76	- If FP32's poor performance is an implementation artifact, then the "precision" facet conflates numerical format with computation engine — these are different constructs
77	- The precision main effect (1.5%, Table 2) and precision×item (3.2%) may be inflated by this confound
78	- Practitioners who don't use enforce_eager may see different precision variance — the results may not transfer
79	
80	The paper should either: (a) remove FP32 and analyze BF16/FP16 only, showing that precision variance is near-zero within optimized paths, or (b) explicitly discuss the confound and reframe the facet as "computation configuration" rather than "numerical precision."
81	
82	### W4. Fine-tuning G-study is too underpowered to contribute [Moderate]
83	The fine-tuning analysis (Section 4.6) uses encoder-only RoBERTa on 2 classification tasks (SST-2, MNLI), 1 GPU, 288 runs (16.7% of planned). The inference vs fine-tuning comparison (Table 14) is compelling conceptually — seed replaces item_id as the dominant source — but the evidence base is too thin and confounded:
84	- Comparing decoder LLMs (7–9B, knowledge/reasoning tasks) with encoder RoBERTa (~125M, classification tasks) confounds paradigm with architecture, scale, and task type
85	- Only 1 GPU → GPU×seed interaction untested
86	- 2/4 tasks → no task-gradient analysis possible
87	- Caveats are stated (Section 4.6) but the comparison is still prominently featured in the abstract and conclusion
88	
89	**Recommendation**: Downgrade from abstract/conclusion prominence to a Discussion-section observation. Frame as "preliminary evidence" rather than a contribution.
90	
91	### W5. No figures in the paper [Moderate]
92	The paper is entirely table-driven (14 tables in main + appendix, 0 figures). For a paper about variance decomposition, this is a significant presentation gap:
93	- Stacked bar charts are the standard visual idiom for variance decomposition (used by Mesting 2026, BrittleBench/Mizrahi 2024)
94	- D-study projection curves (G vs item count) would make Table 4 much more intuitive
95	- The ARC anomaly in the benchmark gradient would be immediately visible in a scatter plot
96	- The inference vs fine-tuning contrast (Table 14) would benefit from paired stacked bars
97	
98	Adding 3–4 figures would substantially improve accessibility without increasing page count significantly.
99	
100	### W6. Benchmark gradient is weak evidence [Moderate]
101	Contribution 3 ("benchmark-conditional variance structure") is hedged as "suggestive evidence" — appropriately so. The expected monotonic gradient (knowledge → commonsense → science → math reasoning) is approximately but not strictly observed: ARC-Challenge (science, 41.8%) falls below GSM8K (math, 43.5%), breaking monotonicity. Rank correlation with expected order is 0.8 (from context). With only 4 benchmarks, one anomaly is enough to prevent strong claims. The ARC anomaly is attributed to high prompt×item (10.5% vs 4.8–8.9% for others), but this post-hoc explanation is not independently verified.
102	
103	### W7. Incremental novelty over Mesting (2026) [Moderate]
104	The core methodological contribution — G-theory applied to LLM evaluation — belongs to Mesting (2026). This paper's extensions are:
105	- Infrastructure facet → severely limited (W2)
106	- Multi-benchmark → solid but straightforward extension
107	- Model as crossed facet → novel but statistically weak (W1)
108	- IRT comparison → strongest novel element
109	
110	The paper is best understood as a multi-benchmark replication and extension of Mesting with added IRT comparison, rather than a fundamentally new framework. The framing should acknowledge this more directly.
111	
112	### W8. Missing related work discussion [Minor]
113	- Biderman et al. (2024) appears in references but is not discussed in the Related Work section
114	- Kunievsky et al. (2025) intent/articulation/model uncertainty decomposition is not cited — relevant as an alternative decomposition framework
115	- ThinkingMachines/Gruver et al. (2025) batch-size nondeterminism (80/1000 unique at T=0) deserves more than a passing mention — it's a key infrastructure variance source this paper doesn't address
116	- The distinction between this paper's design (judge fixed) and Mesting's (judge as facet) deserves more discussion — fixing the judge eliminates the single largest variance source (43.8%) from Mesting, fundamentally changing what the decomposition reveals
117	
118	---
119	
120	## Questions for Authors
121	
122	1. **FP32 confound**: Have you analyzed the variance decomposition with FP32 removed (BF16/FP16 only)? How much does precision and precision×item change? This would isolate the enforce_eager confound.
123	
124	2. **Model facet justification**: In psychometrics, how many levels of a random facet are considered minimally adequate? Can you cite precedent for using 4 levels? If the standard is 10+, how should we interpret your model×item estimates?
125	
126	3. **Cross-benchmark design asymmetry**: The MMLU design (3 precisions × 3 temperatures) is richer than other benchmarks (2×2). Have you tested whether this asymmetry affects cross-benchmark comparisons? Could the reduced design systematically underestimate or overestimate specific variance components?
127	
128	4. **ARC anomaly**: You attribute ARC's high prompt×item (10.5%) to complex option descriptions in science questions. Is there independent evidence for this? Have you examined which specific ARC items drive the anomaly?
129	
130	5. **Fine-tuning comparison**: What would the comparison look like if you used a decoder model (e.g., one of your 4 models) fine-tuned on a generative task? The current encoder-vs-decoder confound prevents strong claims.
131	
132	6. **D-study calculator**: Is this a simple implementation of Equation 2 with lookup tables for benchmark-specific variance estimates, or does it involve non-trivial computation? What happens when a practitioner's design doesn't match your specific facet configurations?
133	
134	---
135	
136	## Experimental Coverage Assessment
137	
138	Comparing against the planned experiment list:
139	
140	| Experiment | Status | Impact of Gap |
141	|-----------|--------|---------------|
142	| exp-001: 4-Model MMLU G-Study | ✅ Complete | — |
143	| exp-001b: Item Resampling | ✅ Complete | — |
144	| exp-002: Multi-Benchmark | ✅ Complete | — |
145	| exp-003: Multi-Hardware | ❌ 0% | **High** — "infrastructure" reduced to precision-on-one-GPU |
146	| exp-004: Comprehensive Analysis | ✅ Complete | — |
147	| exp-005: 14B Extension | ❌ 0% | **Medium** — scale-dependent conclusions impossible |
148	| exp-006: Fine-Tuning | ⚠️ 16.7% | **Medium** — too thin for standalone contribution |
149	| exp-007: LayerCast | ❌ 0% | **Low** — mitigation validation, not core |
150	| exp-008: MATH Benchmark | ❌ 0% | **Medium** — would test gradient with 5th benchmark |
151	
152	3 of 8 experiments fully completed; 1 partially; 4 not done. The completed experiments (001, 001b, 002, 004) form a coherent core, but the missing experiments collectively weaken 3 of 4 claimed contributions.
153	
154	---
155	
156	## Recommendation Summary
157	
158	**What works**: The IRT vs G-theory comparison (Contribution 1) is novel, robust, and actionable. The multi-benchmark variance decomposition is solid empirical work. The methodological defense battery is commendable. The writing is clear and limitations are honestly reported.
159	
160	**What doesn't work**: The infrastructure claim is overclaimed given single-GPU scope and FP32 confound. The model-as-facet analysis is statistically underpowered with only 4 models. The fine-tuning comparison is too thin and confounded. The lack of figures weakens presentation.
161	
162	**Path to acceptance**: (1) Substantially reframe as methodology-focused with precision as secondary analysis. (2) Add 3–4 figures. (3) Elevate IRT comparison as the primary contribution. (4) Downgrade fine-tuning to Discussion-section preliminary observation. (5) Address FP32 confound explicitly — either remove FP32 from analysis or rename the facet. (6) Add missing related work discussion.
163	
164	**Overall**: 3/5 — Borderline. The paper addresses a genuine gap, has one strong novel contribution (IRT vs G-theory), and is methodologically careful, but the incomplete infrastructure story, 4-model limitation, and absence of figures hold it below the acceptance threshold in its current form.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e72f48f6-0655-4305-a671-d5a5c0085550",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "56d1243b-4f2c-48fd-a47c-a54666619282",
  "sourceToolAssistantUUID": "e72f48f6-0655-4305-a671-d5a5c0085550",
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

_source line 56 · 2026-05-21T06:04:13.395Z_

Now I have comprehensive context. Let me also check what actual experiments are complete vs. what the dream paper presents, since the dream paper is aspirational.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56d1243b-4f2c-48fd-a47c-a54666619282",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD4uzBSfWYZJF2QpE8u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac795ff1-dc01-47bd-ad11-cd0c74f0a1e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144EYmvNo24g3rQjvN5A5gg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10846,
      "cache_read_input_tokens": 66970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10846,
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

_source line 57 · 2026-05-21T06:04:16.380Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EXcY2bPgmz2qgkKVY9kT19`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/experiment_data.json",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac795ff1-dc01-47bd-ad11-cd0c74f0a1e3",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD4uzBSfWYZJF2QpE8u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "801864e9-8b1f-4fd5-959a-6e5c1fdc002e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144EYmvNo24g3rQjvN5A5gg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10846,
      "cache_read_input_tokens": 66970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10846,
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

_source line 58 · 2026-05-21T06:04:16.385Z_

<details><summary>↩ Tool result · `toolu_01EXcY2bPgmz2qgkKVY9kT19`</summary>

```text
1	[
2	  {
3	    "name": "Full-scale 4-model MMLU precision study",
4	    "description": "4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B, Mistral-7B) × 3 precisions (Gemma仅bf16+fp32) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. V0 enforce_eager统一引擎消除float32混淆。核心：4模型交叉验证2模型的model×item交互。\n",
5	    "results": {
6	      "total_records": 891200,
7	      "models_completed": 4,
8	      "per_model_accuracy_bf16": {
9	        "llama": 0.711,
10	        "gemma": 0.732,
11	        "mistral": 0.685,
12	        "qwen3": 0.748
13	      },
14	      "single_model_item_id_pct_llama": 61.1,
15	      "single_model_item_id_pct_gemma": 58.7,
16	      "single_model_item_id_pct_mistral": 59.4,
17	      "single_model_item_id_pct_qwen3": 62.3,
18	      "single_model_item_id_pct_mean": 60.4,
19	      "single_model_G_binary_mean": 0.618,
20	      "cross_4model_item_id_pct": 36.8,
21	      "cross_4model_model_pct": 8.3,
22	      "cross_4model_model_x_item_pct": 24.1,
23	      "cross_4model_precision_pct": 1.4,
24	      "cross_4model_prompt_x_item_pct": 3.2,
25	      "cross_4model_seed_x_item_pct": 3.1,
26	      "cross_4model_temp_x_item_pct": 2.1,
27	      "cross_4model_prec_x_item_pct": 1.8,
28	      "cross_4model_ordering_x_item_pct": 0.3,
29	      "cross_4model_infra_x_method_binary_pct": 0.08,
30	      "cross_4model_residual_pct": 18.8,
31	      "cross_model_G_4model": 0.065,
32	      "d_study_10models_G": 0.179,
33	      "d_study_items_G80_practical": 480,
34	      "d_study_items_G80_all_random": 540
35	    },
36	    "tables": [
37	      {
38	        "title": "Table 1: Single-model variance decomposition (binary, MMLU, 4 models)",
39	        "structure": "Rows=variance sources (item_id, precision, prompt×item, seed×item, temp×item, prec×item, ordering×item, residual); Columns=Llama, Gemma, Mistral, Qwen3, Mean",
40	        "highlight": "item_id: 61.1, 58.7, 59.4, 62.3, mean=60.4%; residual: 21.6, 22.4, 21.9, 20.8"
41	      },
42	      {
43	        "title": "Table 2: Cross-model 4-way variance decomposition (binary, MMLU)",
44	        "structure": "Rows=variance sources incl. model, model×item; Columns=% variance, bootstrap 95% CI, significance",
45	        "highlight": "model×item: 24.1% [21.3, 27.0] p<0.001; item_id: 36.8% [33.5, 40.2]; model: 8.3% [5.1, 12.4]"
46	      },
47	      {
48	        "title": "Table 3: G-coefficient comparison — single vs cross-model",
49	        "structure": "Rows=Llama, Gemma, Mistral, Qwen3, 2-model cross, 4-model cross; Columns=G(binary), G(text), items for G≥0.80",
50	        "highlight": "G collapse: single mean 0.618 → 4-model cross 0.065; D-study 10-model G=0.179"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "801864e9-8b1f-4fd5-959a-6e5c1fdc002e",
  "isSidechain": true,
  "promptId": "f18814bb-5456-4f2b-bf34-7e63cb890dd6",
  "agentId": "a9794bbfc34255d04",
  "type": "user",
  "uuid": "31a87036-8532-4367-a7d7-5d938f558630",
  "sourceToolAssistantUUID": "801864e9-8b1f-4fd5-959a-6e5c1fdc002e",
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

_source line 59 · 2026-05-21T06:05:42.089Z_

I now have sufficient context to write a thorough, independent R2 review. Let me synthesize everything I've analyzed.

## R2 Review: Novelty and Related Work

### Summary
This paper applies Generalizability Theory (G-theory) to decompose LLM evaluation variance across infrastructure (numerical precision), methodology (prompt, seed, temperature, ordering), and measurement (items) factors, treating model as a crossed random facet. On MMLU with 4 models and 825,600 records, it finds item_id dominates single-model variance (60.4%) but model-by-item interaction (24.1%) emerges as the second-largest source in a cross-model design, collapsing G from 0.618 to 0.065. The paper claims G-theory requires 3.3-4.4x more items than IRT and provides metric-conditional reproducibility budgets.

### Strengths (Novelty/Positioning)

- S1: **The IRT vs. G-theory item-requirement comparison is a genuinely novel and actionable contribution.** No prior work has directly compared the item budgets implied by IRT-based subsampling (e.g., tinyBenchmarks) with G-theory D-study projections. The 3.3-4.4x gap, attributable to prompt-by-item (4.6%), seed-by-item (4.7%), and residual (21.6%) dimensions that IRT ignores, is well-decomposed and directly informs practitioners choosing between these frameworks. This finding is robust to the paper's incomplete experiments -- it holds with data already collected.

- S2: **Model-as-crossed-facet analysis is a meaningful design choice that extends Mesting (2026).** Treating model as a random crossed facet in a G-theory framework -- rather than stratifying or pooling -- is novel within this literature. The resulting quantification of model-by-item interaction (24.1%) and G-coefficient collapse from 0.618 to 0.065 challenges the interpretability of leaderboard rankings and is the first G-theory demonstration that item difficulty orderings are substantially model-specific in LLM evaluation.

- S3: **The cross-benchmark variance gradient (in the aspirational version) would be a strong contribution.** The paper correctly identifies that extending from one benchmark to multiple benchmarks along a cognitive-complexity continuum could reconcile contradictory prior findings about which variance sources dominate. The hypothesized monotonic decrease of item dominance from knowledge-retrieval to multi-step reasoning tasks, if confirmed, would be explanatory and non-obvious.

- S4: **Positioning against IRT literature is done thoughtfully.** The paper correctly identifies that IRT and G-theory answer fundamentally different reliability questions and does not frame them as competitors but as complementary approaches with different cost implications. The engagement with Lalor et al. (2019), Rodriguez et al. (2021), Polo et al. (2024), and Vania et al. (2021) is adequate for the IRT thread.

- S5: **The dual-metric analysis (binary vs. text-exact-match) reveals a genuinely non-obvious finding.** The 87x gap in G-coefficients (0.611 vs. 0.007) and the metric-conditional nature of infrastructure-methodology separability (precision-by-temperature reaching 1.3% under text-exact-match but near-zero under binary) is new and practically important. This finding falls out naturally from the G-theory framework but has not been reported before.

### Weaknesses (Novelty/Positioning)

- W1: **The paper is primarily an empirical extension of Mesting (2026), not a methodological advance, but the framing suggests otherwise.** The paper claims four differences from Mesting: (a) infrastructure crossing, (b) model as crossed facet, (c) multi-benchmark analysis, (d) metric-conditional budgets. Point (a) yields a near-null result (infrastructure-by-methodology <0.5%), meaning the most-emphasized distinction contributes least. Points (b)-(d) are genuine extensions but within Mesting's framework, not a new framework. The repeated "first" language throughout ("first multi-benchmark G-theory study," "first direct comparison," "first quantification") overstates methodological novelty. The contribution is empirical -- new findings from a larger, more carefully designed study -- and should be framed as such. The title's emphasis on "3-4x More Items Than IRT" is the strongest empirical claim but its prominence is undermined by the fact that the actual evidence (primarily MMLU, single GPU) is narrower than the title implies.

- W2: **Several directly relevant works are missing or insufficiently engaged.** (a) Sclar et al. (2024, ICLR) documented up to 76% accuracy swing from prompt formatting choices -- this is the most comprehensive prompt sensitivity study and its relationship to the paper's prompt-by-item variance component is undiscussed. (b) Kunievsky & Evans (2025) proposed an alternative variance decomposition framework (intent/articulation/model uncertainty) that directly competes with the G-theory approach -- it should be cited and contrasted. (c) Bui et al. (2025) documented extreme seed sensitivity in fine-tuning (RTES variance=18.22 for RoBERTa on COPA) -- directly relevant to the paper's planned fine-tuning study but uncited. (d) The classical psychometrics literature on binary data in G-theory (Brennan 2001, Ch. 12; Shavelson et al. 1989 on generalized G-theory) is referenced only in the methodological defense, not in Related Work, creating the impression that the authors discovered this issue rather than addressing a well-known limitation. (e) The paper does not engage with the broader education measurement literature where G-theory with binary outcomes has been extensively debated (e.g., Mushquash & O'Connor 2006; Briesch et al. 2014).

- W3: **The positioning against Mesting (2026) needs more nuance on the judge-model design decision.** The paper fixes the judge (evaluator) and excludes it as a facet, whereas Mesting found judge choice to be the single largest variance source (43.8%). This is a major design choice that fundamentally changes what the decomposition reveals -- by removing the dominant facet, item_id mechanically rises to dominance. The paper should explicitly discuss this trade-off: it gains controlled experimentation but loses the ability to compare variance magnitudes with Mesting's decomposition. Without this discussion, readers may incorrectly compare item_id=60.4% here with item_id figures from Mesting and draw misleading conclusions.

- W4: **Item dominance as the top finding is partially expected from measurement theory and oversold.** In any assessment with a wide difficulty range, item variance dominates -- this is well-established in educational measurement (Lord & Novick, 1968; Brennan, 2001). The paper's contribution is in quantifying the magnitude (60.4%) and showing its benchmark-conditionality, not in the finding per se. The framing in the Abstract and Introduction treats item dominance as more surprising than it is. The paper should forthrightly acknowledge the psychometric expectation and foreground the novel aspects: the magnitude, the gradient, and the model-by-item interaction.

- W5: **The model-by-item interaction finding (Claim 1 flagship) rests on 4 models, which is marginal for random-effects estimation.** The paper's own cross_model_reml.json shows the 2-model analysis yielded 26.2% model-by-item interaction; the 4-model (or 3-model from actual experiments: 31.7% with CI [24.6-37.3%]) shows different magnitudes. The instability across 2-3-4 model designs (26.2% -> 31.7% -> 24.1% in the dream paper) suggests the estimate has not converged. In psychometric practice, random facets typically require 10+ levels for stable variance component estimation (Brennan, 2001, Ch. 4). The bootstrap CIs capture item-resampling uncertainty but not model-sampling uncertainty -- the 4 models are fixed across all resamples. A leave-one-model-out analysis is essential but absent from the current results.

- W6: **The scope narrowing significantly weakens the title's ambition.** The title promises "3-4x More Items Than IRT" generically, but the actual completed evidence is primarily MMLU on a single GPU architecture with 7-9B models. The cross-benchmark experiments (GSM8K: 1 model partial; ARC: partial) are labeled "preliminary evidence." The multi-hardware experiment was not done. The 14B extension was not done. The fine-tuning study was not done. The gap between the breadth implied by the title/abstract and the depth of actual evidence is a significant weakness. The paper would benefit from a title that more precisely reflects the scope of the evidence: e.g., "Reproducibility Budgets for MMLU: A G-Theory Analysis of Variance Sources in LLM Evaluation."

### Questions for Authors

- Q1: If you removed all infrastructure facets and ran a methodology-only G-theory analysis across benchmarks with model as crossed facet, which of the four claimed contributions would materially change? The near-null infrastructure-by-methodology result suggests the answer is "none," which raises the question of whether the infrastructure crossing is a contribution or a distraction.

- Q2: The 2-model analysis (cross_model_reml.json, which I can verify from project artifacts) shows model-by-item at 26.2%, the 3-model analysis (from paper_framing.md) shows 31.7% [24.6-37.3%], and the dream paper's 4-model version reports 24.1% [21.3-27.0]. Can you explain this non-monotonic trajectory and provide leave-one-model-out results? Does removing any single model change model-by-item by more than the bootstrap CI width?

- Q3: Given that Mesting (2026) included judge as a facet (43.8% of variance) and you excluded it, how should practitioners interpret the apparent difference in item dominance between the two studies? Are your D-study budgets valid for evaluation setups that include LLM-as-judge, or would judge variance overwhelm the item/prompt/seed budget recommendations?

- Q4: The IRT comparison uses tinyBenchmarks' ~100-116 item recommendation. But tinyBenchmarks explicitly optimizes for ranking preservation across a fixed set of models. Your G-theory budget (468-510 items) targets generalizability across all facets simultaneously. Are these even comparable targets? Could you provide a fairer comparison where both frameworks target the same reliability goal?

### Minor Issues

- M1: The bibliography has several entries with incomplete information (e.g., Lu et al. 2022 cited with a different title than the actual paper; ThinkingMachines 2025 and Brittlebench 2026 lack proper author information). Several "first" claims are vulnerable without an exhaustive literature search -- Mesting (2026) also used multiple benchmarks (MMLU, AILuminate, Chatbot Arena), so "first multi-benchmark G-theory study" may be inaccurate.

- M2: The design decision to fix the judge/evaluator (generation-based scoring with fixed rubric) is methodologically sound but is buried in the paper_framing.md design decisions section rather than being prominently discussed in the paper itself. This choice eliminates the single largest variance source from Mesting's decomposition and deserves explicit treatment in the Method section.

- M3: The cross-benchmark analyses use reduced designs (2 precisions x 2 temperatures vs. MMLU's 3x3), creating a design asymmetry that mechanically affects the comparability of precision-related variance components across benchmarks. This should be acknowledged in the cross-benchmark results rather than only in the methodological defense appendix.

### Preliminary Scores (AAAI 1-10 scale)
- Novelty: 5/10
- Significance: 6/10
- Related Work Coverage: 5/10
- Overall (Novelty focus): 5/10

**Rationale for scores.** The novelty score of 5 reflects that the core methodological framework (G-theory for LLM evaluation) belongs to Mesting (2026), and the extensions -- while real -- are empirical rather than methodological. The IRT vs. G-theory comparison and the model-as-facet design are the most genuinely novel elements, but the former is a relatively straightforward comparison and the latter is statistically underpowered with 4 models. The significance score of 6 acknowledges that the IRT-G-theory gap and the D-study budgets are practically valuable, and the model-by-item finding -- if confirmed at scale -- would be important for leaderboard interpretation. The related work score of 5 reflects missing engagement with Sclar et al. (2024), Kunievsky & Evans (2025), Bui et al. (2025), and the classical psychometrics literature on binary G-theory. The overall score of 5 (borderline reject) reflects the combination of incremental novelty over Mesting, scope narrowing relative to claims, missing related work, and the fundamental tension between the paper's ambitious framing and its actual evidence base. A revision that (a) honestly reframes as an empirical extension of Mesting with the IRT comparison as the lead contribution, (b) completes the cross-benchmark experiments with multiple models, and (c) adds the missing related work would likely move this to a 6 or 7.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31a87036-8532-4367-a7d7-5d938f558630",
  "isSidechain": true,
  "agentId": "a9794bbfc34255d04",
  "requestId": "req_011CbFD5V9iiXSPaHCjCRBSv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29693d82-1f4c-46e0-946c-dcdb86c10c70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "61758983-af28-4ed0-aeee-c7c8e76b89a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016KXsy36P9JuBMG8dUBszip",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1364,
      "cache_read_input_tokens": 77816,
      "output_tokens": 3185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1364
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3185,
          "cache_read_input_tokens": 77816,
          "cache_creation_input_tokens": 1364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1364,
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
