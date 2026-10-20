# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus: **novelty and related work**. ## Venue Scoring (ARR/EM

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9e8704ac8b240d35.jsonl`
- **Structured JSON:** [`ed56f8ff2c7a464de9d7.json`](../../sessions/ed/ed56f8ff2c7a464de9d7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

67 recorded events

### User

_source line 1 · 2026-05-14T21:26:47.149Z_

You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus: **novelty and related work**.

## Venue Scoring (ARR/EMNLP 2026)
- Soundness (1-5): 5=Excellent, 4=Strong (sufficient support for all claims), 3=Acceptable (sufficient for main claims), 2=Weak, 1=Poor
- Excitement (1-5): 5=Highly Exciting, 4=Exciting, 3=Borderline, 2=Mediocre, 1=Not exciting
- Overall (1-5): 5=Strong accept, 4=Accept, 3=Borderline, 2=Reject, 1=Strong reject
- Confidence (1-5): 5=Absolutely certain, 4=Quite sure, 3=Fairly confident, 2=Willing to defend, 1=Not confident

## Paper Summary

**Title:** OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints

**Problem:** LLMs applied to information extraction (IE) systematically violate ontology constraints — 15.4% of triples violate domain/range type constraints on SciERC, 18.7% on DocRED. Prompt-level intervention (schema-informed prompting) reduces violations overall but is per-relation unreliable (Evaluate-for *increases* by 5.8pp).

**Core Idea:** Compile IE ontology schemas O = (T, R, dom, ran) into two composable constraint layers applied during autoregressive decoding:
1. **Grammar layer** (XGrammar CFG): JSON structure + entity type vocabulary + relation name vocabulary. Purely local constraints.
2. **Semantic layer** (TypeConstraintProcessor + entity registry + logit masking): domain/range constraints. Prefix-decidable with state.
3. Composition via bitwise AND: M_final = M_grammar ∧ M_semantic. Enabling dependency: grammar ensures vocabulary validity so semantic can look up rules.
4. Decidability taxonomy: (a) purely local → grammar, (b) prefix-decidable with state → semantic, (c) truly non-local (cross-field consistency) → inherent limitation.

**Claims:**
1. Violation landscape study: DR violations are non-trivial (15-19%), driven by constraint tightness not ontology size.
2. Prompt-level intervention is insufficient (per-relation unreliable).
3. OntoCoDec achieves 94% DR reduction on SciERC (15.37→0.93%) at zero F1 cost, with honest CF trade-off.
4. Cross-model generalization (zero code modification): DR reductions 44.7-99.4% across 2×2 matrix.
5. Dual-factor model: DR reduction effectiveness = f(constraint tightness × model RV baseline).
6. Decidability taxonomy classifying constraint types by amenability to autoregressive enforcement.

**Results highlights:**
- 2×2 matrix: Qwen3-8B + Llama-3.1-8B × SciERC + DocRED
- ET and RV eliminated entirely (→0%) in all cells
- DR reduction: 99.4% (Llama-SciERC) to 44.7% (Qwen-DocRED)
- F1 neutral on SciERC (p>0.5), significant positive on DocRED (p&lt;0.001)
- CF elevated (6.5-12.0%) as inherent limitation, analyzed via EVR subtyping
- Post-hoc filtering comparison: higher F1 but loses 48.1% DocRED triples, 127 TPs lost

**Related Work (as presented in paper, §6):**
- LLM-Based IE: Zero/few-shot IE with LLMs; systematic ontology constraint violation study is novel.
- Constrained Decoding: XGrammar etc. enforce structural constraints (JSON, type safety). OntoCoDec extends to semantic constraints requiring cross-field state.
- Schema-Guided Generation: Prompt-based constraint provision. Paper shows this is insufficient per-instance.
- Post-Hoc Validation: Filtering/correction after generation. Paper provides empirical comparison showing information loss.
- Type-Constrained KG Completion: Discrete symbol prediction, not applicable to autoregressive text generation.

**References cited (10 total):**
- Luo et al. (SciERC, ACL 2023)
- Yao et al. (DocRED, ACL 2019)
- Dong et al. (XGrammar, 2024)
- Wei et al. (Zero-shot IE with ChatGPT, 2023)
- Li et al. (CRANE: Correcting LLM outputs via constrained re-generation, 2024)
- Qwen Team (Qwen3 technical report, 2025)
- Touvron et al. (Llama, arXiv 2023)
- Wadhwa et al. (Revisiting RE in LLM era, ACL 2023)
- Josifoski et al. (Exploiting asymmetry for synthetic training data, EMNLP 2023)
- Wang et al. (Grammar-aligned decoding, 2024)

**Limitations stated:** CF not solved, 2×2 scope, zero-shot only, fallback degradation on high-tightness ontologies.

## Experiment Design Coverage
The paper covers all planned experiments from the design document except P017 (S2 pilot, engineering checkpoint, correctly omitted) and P020 (killed). Coverage is complete.

## Your Review Task

Provide a structured review focused on **novelty, positioning, and related work**:

1. **Summary** (2-3 sentences)
2. **Strengths** (bullet points, focus on novelty of contributions, positioning relative to prior work, significance of findings, decidability taxonomy, cross-field analysis)
3. **Weaknesses** (bullet points, focus on novelty concerns, missing related work, overclaiming, positioning gaps, limited scope of comparison)
4. **Questions to Authors** (specific, about novelty claims, missing comparisons, framing)
5. **Minor Issues** (related work coverage, citation completeness, framing)
6. **Scores**: Soundness (1-5), Excitement (1-5), Overall (1-5), Confidence (1-5)

Key things to evaluate:
- Is the violation landscape study genuinely the "first systematic study"? Are there prior works characterizing constraint violations in LLM IE?
- Is extending grammar-constrained decoding to semantic constraints with state novel enough for EMNLP?
- The decidability taxonomy (a/b/c) — is this a genuine conceptual contribution or taxonomy for taxonomy's sake?
- Related work section is very brief (5 paragraphs, 10 references). Is this sufficient for a top venue?
- How does this relate to structured prediction literature, neuro-symbolic methods, type systems in NLP?
- The "enabling dependency" concept — is this novel or well-known in constraint composition?
- Post-hoc comparison is against naive filtering only. What about constrained re-generation (CRANE is cited but not compared)?

Be rigorous but fair. EMNLP values both empirical and conceptual contributions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "a38448a0-7376-4a8b-875e-d5225f8e1e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T21:26:47.152Z_

```json
{
  "parentUuid": "a38448a0-7376-4a8b-875e-d5225f8e1e6c",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
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
  "uuid": "073a390b-b2ef-4826-9e65-47f4c93ebdab",
  "timestamp": "2026-05-14T21:26:47.152Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T21:26:51.758Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "073a390b-b2ef-4826-9e65-47f4c93ebdab",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AmDCVadXpxmaqTonXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb8b6c9c-d289-4886-b3d6-66f82a53f789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jhf5yTxY8VqGUXVnVbxHC4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7588,
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

_source line 4 · 2026-05-14T21:26:52.761Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01M9dDqZVnQWaCJDNjqKduP5`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_dream_review_report,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb8b6c9c-d289-4886-b3d6-66f82a53f789",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AmDCVadXpxmaqTonXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02ee04fc-149c-41e4-830a-21e39117f61c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jhf5yTxY8VqGUXVnVbxHC4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 8252,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 142,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7588,
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

_source line 5 · 2026-05-14T21:26:52.766Z_

<details><summary>↩ Tool result · `toolu_01M9dDqZVnQWaCJDNjqKduP5`</summary>

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
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
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
  "parentUuid": "02ee04fc-149c-41e4-830a-21e39117f61c",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "2542af0e-73d7-4681-9e47-d3e153121ce7",
  "sourceToolAssistantUUID": "02ee04fc-149c-41e4-830a-21e39117f61c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T21:26:55.697Z_



I'll read the paper and supporting project files to conduct a thorough novelty-focused review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2542af0e-73d7-4681-9e47-d3e153121ce7",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AmdRGmPKz7t2kpq5hC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df712d7a-5379-4de5-807e-1cc1ca80016b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YRx2BLPJTVkQdfhiXg6DZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 15840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 7 · 2026-05-14T21:26:56.775Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VMKFxKFWWE8CbbXQHoazKX`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df712d7a-5379-4de5-807e-1cc1ca80016b",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AmdRGmPKz7t2kpq5hC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3eba1182-e04d-4a92-95f2-21ca08809fce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YRx2BLPJTVkQdfhiXg6DZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 15840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 8 · 2026-05-14T21:26:56.794Z_

<details><summary>↩ Tool result · `toolu_01VMKFxKFWWE8CbbXQHoazKX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **llama_docred_full_s1** (success): Llama-3.1-8B-Instruct + Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上的效果。与 Qwen3-8B DocRED full_s1 (DR 10.19%) 对比，验证约束解码在不同模型+复杂 schema 上的泛化性。\\n  [llama_docred_full_s1_analysis](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/llama_docred_full_s1/report/llama_docred_full_s1_analysis.md)\\n- **llama_docred_unconstrained** (success): Llama-3.1-8B-Instruct 在 DocRED unconstrained baseline。与 Qwen3-8B DocRED unconstrained 对比 violation 分布。验证不同模型在复杂 schema (96 relations) 上的 violation 模式差异。\\n- **phase2_docred_grammar_only** (success): Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\\n\\n## 趋势\\n成功 19 / 负向 0 / 失败 0 / 共 20\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-16980: 无 GPU 信息\\n\\n## 告警\\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\\n\", \"total_chars\": 1036, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eba1182-e04d-4a92-95f2-21ca08809fce",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "7c39d44a-319b-49f2-bf02-a61c34a0dd0d",
  "sourceToolAssistantUUID": "3eba1182-e04d-4a92-95f2-21ca08809fce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T21:26:57.176Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014zYBAxeNpQ7VzAHMHdGL4Z`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c39d44a-319b-49f2-bf02-a61c34a0dd0d",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AmdRGmPKz7t2kpq5hC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ab8c6b2-2e9c-4426-b917-b0a4a3f15c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YRx2BLPJTVkQdfhiXg6DZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 15840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 10 · 2026-05-14T21:26:57.186Z_

<details><summary>↩ Tool result · `toolu_014zYBAxeNpQ7VzAHMHdGL4Z`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ab8c6b2-2e9c-4426-b917-b0a4a3f15c6e",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "59f2b8ea-fb66-4e00-8d49-13a4eaa375c5",
  "sourceToolAssistantUUID": "9ab8c6b2-2e9c-4426-b917-b0a4a3f15c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:26:57.691Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LriZfQvXYvNQt8Z2tFUnp6`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59f2b8ea-fb66-4e00-8d49-13a4eaa375c5",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AmdRGmPKz7t2kpq5hC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f176c461-4cfc-4396-b0a7-3f19ae9b7829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YRx2BLPJTVkQdfhiXg6DZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2016,
      "cache_read_input_tokens": 15840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2016,
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

_source line 12 · 2026-05-14T21:26:57.706Z_

<details><summary>↩ Tool result · `toolu_01LriZfQvXYvNQt8Z2tFUnp6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md\", \"content\": \"# OntoCoDec — Paper Framing\\n\\n## Target Venue\\nEMNLP 2026 (ARR submission May 25, 2026)\\n\\n## Title\\nOntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\\n(Note: \\\"Guaranteed\\\" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. \\\"Near-Complete\\\" is honest and defensible.)\\n\\n## Core Insight\\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\\n\\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\\n\\n## Core Claims\\n\\n### Claim 1 (Empirical): Violation Landscape\\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\\n\\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\\n\\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\\n\\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\\n\\n### Claim 2 (Empirical): Prompt Insufficiency\\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\\n\\n**Narrative**: This is NOT about \\\"5.78% barely above 5%\\\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\\n\\n### Claim 3 (Methodological): Composable Constraint Framework\\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\\n\\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \\\"synergistic\\\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\\n\\nThe two layers compose via bitwise AND of token masks. Recommended framing: \\\"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\\\"\\n\\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\\nWhen $M_{semantic} \\\\cap M_{grammar} = \\\\emptyset$, the system falls back to grammar-only control.\\n\\n**关键量化数据（Reviewer 从日志挖掘）**:\\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\\n- DocRED fallback 频率是 SciERC 的 **5.3×**\\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\\n\\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\\n\\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \\\"Constraint Coverage\\\" 指标（semantic masking 实际生效的 token 比例）。这把 \\\"10.19% DR 残余\\\" 从弱点变成可量化分析的 finding。Frame as \\\"engineering robustness\\\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\\n\\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\\n\\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\\n\\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\\n\\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\\n\\n## Anticipated Reviewer Concerns\\n\\n### C1: \\\"5.78% is barely above 5% — threshold is arbitrary\\\"\\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\\n\\n### C2: \\\"Why not just post-hoc filter?\\\"\\n**Response (D013, 实验结果已出)**:\\n\\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\\n\\n**论文 framing（不以 F1 论高低，多维对比）**:\\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\\n4. **Precision trade-off（诚实承认）**: \\\"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\\\"\\n\\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\\n\\n**Reviewer 补充发现（D013 后）**:\\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\\\"prevent vs detect\\\" 核心论据的具体数据。\\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\\n\\n### C3: \\\"Bitwise AND of two masks is not novel\\\"\\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\\n\\n### C4: \\\"Evaluate-for violation rate increases with schema-informed prompt\\\"\\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\\\"Method X evaluates for Task Y\\\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \\\"harder instances\\\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\\n\\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\\n\\n### C5: \\\"Only tested on one model (Qwen3-8B)\\\"\\n**Response**: Cross-model validation DONE. Llama-3.1-8B 零代码修改：\\n- SciERC: DR 13.34%→0.08% (↓99.4%), F1-neutral (-0.14pp)\\n- DocRED unconstrained: DR 26.15%, RV 16.03%, R-F1 5.98% (parse failures 6.8% vs Qwen 1.2%)\\n- DocRED full_s1: 🔄 ETA ~20:19 UTC\\n\\n**Cross-model claim 指导（Reviewer 专项评估）**:\\n- ✅ 可声明：\\\"OntoCoDec generalizes across model families without code modification\\\"（程序性事实，铁证）\\n- ❌ 不可声明：\\\"consistently achieves the same reduction rate\\\"（仅 2 模型，不足以量化声明）\\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\\n\\n### C6: \\\"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\\\"\\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **D012 Bootstrap CI (10000×, v2 fix) 结果**:\\n- SciERC: Rel F1 +0.13pp (p=0.58), Ent F1 -0.03pp (p=0.53) → **F1-neutral**\\n- DocRED: Rel F1 +0.50pp (p<0.001, CI [+0.23, +0.81]), Ent F1 +1.23pp (p<0.001, CI [+0.94, +1.55]) → **双双显著提升**\\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\\n- Frame as: \\\"Constraint enforcement preserves or improves extraction quality: F1-neutral on SciERC; statistically significant Rel F1 and Entity F1 improvement on DocRED (p<0.001).\\\"\\n- 不升级为 core claim，但如实报告 significance + 机制归因。Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.\\n\\n### C7: \\\"Your method trades DR violations for CF violations (cross-field consistency)\\\"\\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\\n\\n**CF 子类型分析（根因已确认）**：\\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\\n\\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\\n\\n**论证层次**：\\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\\n\\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \\\"CF 是 semantic type enforcement 的系统性副作用\\\" 提供干净的消融证据。\\n\\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\\n\\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\\n\\n### C8: \\\"Absolute F1 is too low (~8%) — results are not meaningful\\\"\\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \\\"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\\\"\\n\\n## Paper Structure (Draft)\\n1. Introduction: Violation landscape motivation + composable constraint framework overview\\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\\n5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based\\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)\\n7. Conclusion\\n\\n## Claim Calibration (per Reviewer assessment)\\n\\n**Safe to claim (sufficient evidence from Phase 2)**:\\n- \\\"First systematic study of ontology constraint violations in LLM-based IE\\\"\\n- \\\"Violation rate correlates with constraint tightness, not ontology size\\\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\\n- \\\"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\\\" ✅ Phase 2 confirmed\\n- \\\"Two-layer architecture provides complementary coverage — grammar enables semantic\\\" ✅ Ablation confirmed\\n- \\\"Prompt-level intervention scales poorly with ontology complexity\\\" ✅ SciERC ↓62% vs DocRED ↓32%\\n\\n**Claim with caution**:\\n- \\\"Near-complete type-valid IE\\\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \\\"Near-Complete\\\"\\n- \\\"Principled framework applicable to arbitrary IE ontologies\\\" — validated on 2 datasets + 1 model only\\n- \\\"F1 improvement\\\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\\n- \\\"CF reveals type system ambiguity\\\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\\\"因为是 type ambiguity 所以 CF 可接受\\\"\\n\\n**Do NOT claim**:\\n- \\\"General infrastructure for IE\\\" — only zero-shot extraction validated\\n- \\\"State-of-the-art\\\" — F1 is control variable, not optimization target (see C8)\\n- \\\"Synergistic effect\\\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\\n- \\\"S2 solves CF\\\" or \\\"S2 mitigates Structure Snowballing\\\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\\n- \\\"Pilot50 DR=0%\\\" — small-sample artifact, full S2 has DR=0.97%\\n- \\\"Grammar-first invariant\\\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\\n- \\\"Robust dual-layer composition across schema complexities\\\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\\n\\n## Risk Ranking (ordered by reject probability)\\n\\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\\n3. **Novelty perception** (MEDIUM): \\\"PLDI'25 for code → OntoCoDec for IE\\\" attack line. Must argue IE constraint structure differs fundamentally.\\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\\n\\n## Critical Path to EMNLP Submission (May 25)\\n\\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\\n- **May 14-15**: Llama DocRED 2 组实验 ✅ + Checker 修正 ✅ + post-hoc baseline ✅ + bootstrap CI ✅ + related work ✅\\n- **May 14-15**: D014 tightness claim 修订 + §5 cross-model subsection + abstract/conclusion 修正 (Agent 执行中)\\n- **May 15-17**: 全文校对 + Discussion 整合 + 最终数字确认\\n- **May 19**: 内部稿 → submit_paper_to_review\\n- **May 19-24**: Review 修改 + 最终提交\\n\\n**当前瓶颈**: D014 论文修订（tightness claim + cross-model subsection + E-F1 claim limitation）\\n\\n## Status\\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\\n- Related work: ✅ 42 bib entries, 4 additions merged\\n- Dream 6/6 actions: ✅ All complete\\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\\n- D014 tightness revision: 🔄 Agent executing (tightness × RV baseline dual-factor)\\n\", \"total_chars\": 20047, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f176c461-4cfc-4396-b0a7-3f19ae9b7829",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "610f9d73-6589-4f23-ab5a-75ba47c8eca0",
  "sourceToolAssistantUUID": "f176c461-4cfc-4396-b0a7-3f19ae9b7829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:27:01.284Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013ysJPswivg6AXteQcaQN7i`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "610f9d73-6589-4f23-ab5a-75ba47c8eca0",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Amzexw4wubLM3Hcy1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e20bc8bc-2d25-4568-9747-45da21a3b381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoE5ZjaUrgCw9dx51UXR7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9048,
      "cache_read_input_tokens": 17856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 14 · 2026-05-14T21:27:01.297Z_

<details><summary>↩ Tool result · `toolu_013ysJPswivg6AXteQcaQN7i`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e20bc8bc-2d25-4568-9747-45da21a3b381",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "fec0306e-e220-4c00-9e62-72da47c4bcec",
  "sourceToolAssistantUUID": "e20bc8bc-2d25-4568-9747-45da21a3b381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T21:27:02.234Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KpMAHQM8BjMAjdmJTfGL2N`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fec0306e-e220-4c00-9e62-72da47c4bcec",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Amzexw4wubLM3Hcy1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34184adc-4586-45a0-a05c-56c763ce869e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoE5ZjaUrgCw9dx51UXR7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9048,
      "cache_read_input_tokens": 17856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 16 · 2026-05-14T21:27:02.249Z_

<details><summary>↩ Tool result · `toolu_01KpMAHQM8BjMAjdmJTfGL2N`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ROADMAP.md\", \"content\": \"# OntoCoDec — Research Dashboard\\n\\n> 最后更新: 2026-05-14 20:43 UTC | 更新原因: 修正 Llama unconstrained DR 数据错误 (18.36%→26.07%) + 核心方向描述加 model-dependent + 补全近期任务\\n\\n## 核心方向\\n两层约束解码（grammar + semantic）近完全消除 LLM-based IE 的本体类型违规，F1 impact model-dependent: neutral (SciERC) to positive (DocRED Qwen, +0.50pp p<0.001)。详见 paper_framing.md。\\n\\n## 当前阶段\\nResearch — **全部 20 个实验完成**（19 success, 1 killed）。进入论文修订收尾。目标 May 19 内部稿 → May 25 EMNLP ARR。\\n\\n## 实验完成度\\n- 总计: 20 个实验，19 success，1 killed，0 RUNNING\\n- SciERC 5-way ablation (Qwen): ✅\\n- DocRED 4-way ablation (Qwen): ✅\\n- Llama SciERC cross-model: ✅ (DR↓99.4%)\\n- Llama DocRED cross-model: ✅ (unconstrained DR=26.07%, full_s1 DR=2.55%, DR↓90.2%)\\n- Phase 0 violation landscape: ✅ SciERC + DocRED\\n- Post-hoc baseline: ✅ (D013 multi-dimensional framing)\\n- Bootstrap CI (D012): ✅ (entity filter bug fixed + re-verified)\\n- D011 ET fix (v2 checker): ✅ 全量重跑完成\\n\\n## 关键决策摘要\\n- D014: Tightness scaling → 双因素 (tightness × model RV baseline)\\n- D013: Post-hoc framing → 不争 F1，多维对比 (recall + coverage + operational)\\n- D012: Bootstrap CI → SciERC neutral (p=0.58), DocRED significant (+0.50pp, p<0.001)\\n\\n## 活跃工作流 (May 14 ~21:30 UTC)\\n\\n### GPU 实验\\n（无 — 全部完成）\\n\\n### Agent 工作\\n- D014 修订指令在队列中等待执行（§5 tightness rewrite + cross-model subsection + abstract/conclusion + limitations + placeholders）\\n- 前置 worker callbacks 处理中\\n\\n## 近期任务\\n- [ ] D014 §5 tightness claim 修订（tightness × RV baseline 双因素）— Agent 队列中\\n- [ ] Abstract/Conclusion E-F1 claim limitation（Qwen-specific）— Agent 队列中\\n- [ ] §5 Cross-model subsection（2×2 matrix table + narrative）— Agent 队列中\\n- [ ] Limitations expansion（CF 12.02% + parse failures 6.8%→9.1% + scope）— Agent 队列中\\n- [ ] [LLAMA-DOCRED-TBD] placeholder filling — Agent 队列中\\n- [ ] Discussion 段落更新（加入 Llama DocRED 数据）\\n- [ ] Bibliography 最终编译检查\\n- [ ] main.tex 集成 + 全文数字一致性终审\\n- [ ] May 19: 内部稿 → submit_paper_to_review\\n\\n## GPU 预算\\nwestd-16980: cuda:0 + cuda:1 分配给本项目。当前空闲（全部实验已完成）。\\n\\n## Dream 后行动完成度 (6/6 ✅)\\n1. Post-hoc baseline — ✅ D013\\n2. Bootstrap CI — ✅ D012 (entity filter fix verified)\\n3. Related work 20+ refs — ✅ 42 entries merged\\n4. PICARD detailed comparison — ✅\\n5. CF/F1 discussion — ✅ discussion_paragraphs.tex\\n6. Variance estimates — ✅ bootstrap CI\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-14 | Tightness scaling claim 修订：从单因素(tightness)改为双因素(ti | llama_docred_full_s1, llama_docred_unconstrained, phase2_docred_full_s1 |\\n| D013 | 2026-05-14 | Post-hoc baseline framing: 不以 F1 论高低，多维对比 (recall  | phase2_scierc_unconstrained, phase2_scierc_full_s1, phase2_docred_unconstrained, phase2_docred_full_s1 |\\n| D012 | 2026-05-14 | Bootstrap CI framing: 选 (B) 逐数据集报告 F1 significance | phase2_docred_full_s1, phase2_scierc_full_s1 |\\n| D011 | 2026-05-14 | 推翻之前 ET 计数口径决定——修正 ET triple-counting，每个 entity 只计 | phase2_docred_unconstrained, phase2_docred_semantic_only |\\n| D010 | 2026-05-14 | Dream 三档 Weak Reject (3/6) → 制定 6 项结构性补强计划：post-ho | llama_docred_full_s1, llama_docred_unconstrained, llama_scierc_full_s1 |\\n| D009 | 2026-05-14 | Llama-3.1-8B cross-model 验证升级为 should-have，SciERC- | phase2_scierc_full_s1, phase2_scierc_unconstrained |\\n| D008 | 2026-05-14 | 补跑 DocRED semantic_only 完成跨数据集全消融；论文写作提前至 DocRED 分 | phase2_docred_grammar_only, phase2_docred_full_s1, phase2_scierc_semantic_only |\\n| D007 | 2026-05-14 | S2 降级为架构 ablation，S1 为主推策略；标题去掉 \\\"Guaranteed\\\" 改 \\\"Ne | phase2_scierc_full_s2, phase2_scierc_full_s1 |\\n| D006 | 2026-05-14 | Phase 2 SciERC 核心结果确认：Full S1 DR -94% 且 F1 无损，CF v | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1, mvp_phase0_docred_schema |\\n| D005 | 2026-05-14 | Phase 2 SciERC 核心结果确认：Full S1 DR↓94% F1无损，CF viola | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1 |\\n\\n\\n\\n\", \"total_chars\": 3780, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34184adc-4586-45a0-a05c-56c763ce869e",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "1619b376-d3c4-4ab2-ad15-9e396beb72ee",
  "sourceToolAssistantUUID": "34184adc-4586-45a0-a05c-56c763ce869e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T21:27:03.300Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BHqkYQj9TkwqPgULjJomJ7`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1619b376-d3c4-4ab2-ad15-9e396beb72ee",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Amzexw4wubLM3Hcy1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd8f6995-3864-4e6a-b4b2-4e98d68f350f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoE5ZjaUrgCw9dx51UXR7J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9048,
      "cache_read_input_tokens": 17856,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 17856,
          "cache_creation_input_tokens": 9048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9048,
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

_source line 18 · 2026-05-14T21:27:03.319Z_

<details><summary>↩ Tool result · `toolu_01BHqkYQj9TkwqPgULjJomJ7`</summary>

```text
artifacts/_project/paper/paper_tables_draft.tex
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/section7_conclusion_550cbf.tex
artifacts/_project/paper/section2_background.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/section6_relwork_additions.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/discussion_paragraphs.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/dream_reports/dream_20260514T205155/best/paper.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/section7_conclusion.tex
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/dream_reports/dream_20260514T205155/median/paper.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/dream_reports/dream_20260514T205155/worst/paper.tex
artifacts/_project/paper/appendix_related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd8f6995-3864-4e6a-b4b2-4e98d68f350f",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "ffb11312-b51b-45dd-9c03-1f956f7dcd23",
  "sourceToolAssistantUUID": "dd8f6995-3864-4e6a-b4b2-4e98d68f350f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T21:27:06.278Z_

Let me read the actual paper sections to understand the full manuscript.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffb11312-b51b-45dd-9c03-1f956f7dcd23",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AnQQDRSpsepQnddHLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d31bfa5-436f-4007-a1ec-d8409a57dabb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cmnjjum7xbFj2mAWgGSFdv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 26904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3038,
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

_source line 20 · 2026-05-14T21:27:06.762Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PaRwGwnY3Da7v58hQXzNoL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d31bfa5-436f-4007-a1ec-d8409a57dabb",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AnQQDRSpsepQnddHLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e23860f8-f6d8-43d5-a4de-75a90a387d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cmnjjum7xbFj2mAWgGSFdv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 26904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3038,
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

_source line 21 · 2026-05-14T21:27:06.767Z_

<details><summary>↩ Tool result · `toolu_01PaRwGwnY3Da7v58hQXzNoL`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Near-Complete Type-Valid Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Violation Landscape ===
35	\input{section3_violation_landscape}
36	
37	% === §4 Method ===
38	\input{section3_method_draft}
39	
40	% === §5 Constraint Composition ===
41	\section{Constraint Composition}
42	\label{sec:composition}
43	\input{section4_composition_draft}
44	
45	% === §6 Experiments ===
46	\section{Experiments}
47	\label{sec:experiments}
48	\input{section5_scierc_draft}
49	\input{section5_docred_draft}
50	\input{section5_crossmodel_draft}
51	
52	% === §7 Related Work ===
53	\input{section6_related_work}
54	
55	% === §8 Discussion and Conclusion ===
56	\section{Discussion and Conclusion}
57	\label{sec:discussion}
58	\input{discussion_paragraphs}
59	\input{section7_conclusion}
60	
61	% === Bibliography ===
62	\bibliography{relwork_new_entries}
63	
64	\end{document}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e23860f8-f6d8-43d5-a4de-75a90a387d67",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "4b28dc03-ecfd-4af7-a879-061b90c782a4",
  "sourceToolAssistantUUID": "e23860f8-f6d8-43d5-a4de-75a90a387d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T21:27:07.234Z_

<details open><summary>🔧 Tool call — Read · `toolu_0119yn4hVbvWhwkL3pqoFqNe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b28dc03-ecfd-4af7-a879-061b90c782a4",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AnQQDRSpsepQnddHLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "696e8f77-9c77-4771-9b20-8b6bd658ab5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cmnjjum7xbFj2mAWgGSFdv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 26904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3038,
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

_source line 23 · 2026-05-14T21:27:07.240Z_

<details><summary>↩ Tool result · `toolu_0119yn4hVbvWhwkL3pqoFqNe`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for structured generation.
15	However, all of these methods operate exclusively at the syntactic level---they ensure format validity (e.g., well-formed JSON, valid enum values) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.
16	This syntactic-only limitation motivates OntoCoDec's semantic extension: our grammar layer builds on XGrammar for structural (JSON schema and enum) constraints, while a second semantic layer enforces relational type constraints that are inherently beyond the expressive power of context-free grammars.
17	
18	% ===========================================================================
19	% Paradigm 1.5: Semantic Constrained Decoding for Code
20	% ===========================================================================
21	\paragraph{Semantic Constrained Decoding for Code.}
22	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness, demonstrating that richer-than-CFG constraints can be compiled into token-level filtering.
23	In the text-to-SQL domain, PICARD~\cite{scholak2021picard} maintains an incremental SQL parsing state that rejects tokens violating syntax or referencing non-existent database columns at each decoding step, achieving state-of-the-art results on Spider and CoSQL without modifying model weights.
24	While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema---database table and column names known before decoding begins.
25	In contrast, OntoCoDec's entity registry is populated \emph{during} generation as entity spans are extracted from free text, requiring constraint sets that evolve with the decoding prefix---a fundamental distinction between querying a known schema and extracting from unstructured text.
26	Synchromesh~\cite{synchromesh_iclr2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs without fine-tuning, establishing that semantic constraints can be expressed as dynamic token masks conditioned on the generation prefix.
27	MGD~\cite{mgd_neurips2023} uses static-analysis monitors to perform incremental type checking at decode time, enabling SantaCoder-1.1B to outperform text-davinci-003 on repository-level code completion by ensuring that every generated identifier is type-correct with respect to the surrounding code context.
28	Most recently, \citet{pldi2025_type_constrained_codegen} compile full type systems---including generic types and subtyping---into prefix automata for token-level logits masking, reducing compilation errors by over 50\%.
29	This last system is the closest mechanistic analog to OntoCoDec, applying the same ``type system $\to$ automaton $\to$ logits mask'' pipeline, though in a fundamentally different domain.
30	The key technical difference lies in the constraint structure: programming-language type systems feature deep subtyping hierarchies and parametric polymorphism, whereas IE ontology axioms specify flat domain/range sets---a relation $R$ accepts head entities from set $\mathcal{D}(R)$ and tail entities from set $\mathcal{R}(R)$, with no subtype chains.
31	Conversely, IE introduces a challenge absent in code generation: the constraint target (entity type) must be inferred from free-text spans rather than read from declared type annotations, requiring a stateful entity registry that tracks extracted types during autoregressive generation.
32	These methods collectively demonstrate that semantic (type) constraints at decode time are both feasible and highly effective, but exclusively in the code domain where type systems are formally specified.
33	OntoCoDec is the first to \emph{automatically compile} IE ontology axioms---including domain/range constraints---into token-level decoding masks for information extraction, migrating the type-constrained decoding paradigm from code generation to IE.
34	
35	% ===========================================================================
36	% Paradigm 2: Vocabulary/Type-Constrained Generation
37	% ===========================================================================
38	\paragraph{Vocabulary and Type-Constrained Generation.}
39	The idea of enforcing entity-type compatibility constraints for information extraction dates back to pre-neural methods.
40	\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints---e.g., \textsc{Emp-Org} only between \textsc{Per} and \textsc{Org} entities---establishing the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.
41	In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, restricting each decoding step to tokens consistent with valid entity names from a predefined catalog.
42	GenIE~\cite{josifoski2022genie} extends this approach to end-to-end information extraction with state-based constraints that enforce valid triple structures, achieving strong performance on closed-world knowledge base population, though it requires task-specific fine-tuning on the target schema.
43	AdaKGC~\cite{adakgc_emnlp2023} introduces schema-constrained dynamic decoding with trie-based prefix trees that adapt to the target schema, enforcing that generated entity and relation names belong to a predefined inventory---a vocabulary-level constraint that ensures name validity but does not verify type compatibility between a relation and its arguments.
44	GCD~\cite{geng2023gcd} provides a unified grammar-constrained decoding framework for structured NLP tasks including IE, introducing input-dependent grammars that adapt constraints based on the source text---the closest precursor to OntoCoDec in applying logits masking to IE, though limited to syntactic constraints.
45	NeuroLogic Decoding~\cite{lu2021neurologic} expresses lexical inclusion and exclusion constraints as predicate logic formulas enforced during beam search, offering a general mechanism for token-level control that can encode vocabulary membership but not relational type rules.
46	These approaches constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation.
47	OntoCoDec's semantic layer enforces relational constraints---e.g., that the head entity of relation $R$ must belong to type set $\mathcal{D}(R)$---which cannot be expressed as static vocabulary restrictions because the valid set depends on the relation type generated earlier in the same sequence.
48	While Roth \& Yih's ILP formulation shares the same type-compatibility motivation, it operates as a post-hoc reranker over discrete candidates; OntoCoDec integrates enforcement directly into autoregressive decoding, preventing violations rather than filtering them.
49	
50	% ===========================================================================
51	% Paradigm 3: Structural Constraints for IE
52	% ===========================================================================
53	\paragraph{Structural Constraints via Training and Prompting.}
54	An orthogonal approach encodes IE output structure through model training or prompt design rather than decoding-time enforcement, relying on learned representations to produce schema-compliant outputs.
55	UIE~\cite{lu2022uie} defines a Structured Extraction Language and trains a unified text-to-structure model across 13 IE datasets, relying on large-scale pre-training to internalize output format constraints.
56	GoLLIE~\cite{sainz2024gollie} expresses annotation guidelines as Python dataclass definitions and fine-tunes Code-LLaMA to generate typed code, achieving strong zero-shot transfer to unseen IE schemas by leveraging the implicit type structure of programming languages.
57	KnowCoder~\cite{knowcoder_acl2024} takes this further by encoding 29K entity types from Wikidata as a Python class hierarchy, training a Code-LLM to generate structured extraction code that implicitly respects type inheritance---the most comprehensive schema-as-code approach to date.
58	CodeIE~\cite{li2023codeie} similarly reformulates IE as code generation, leveraging the structural regularity of programming languages to reduce output format errors.
59	ADELIE~\cite{qi2024adelie} uses SFT and DPO to align LLMs on IE tasks, achieving state-of-the-art results among open-source models while preserving general capabilities, though compliance with ontological constraints remains a learned soft preference rather than a guarantee.
60	In the supervised setting, joint entity-relation architectures such as SpERT~\cite{eberts2020spert} and PFN~\cite{yan2021pfn} enforce type consistency implicitly through shared representations: SpERT classifies entity spans and relation pairs in a single BERT pass with span-level negative sampling, while PFN decomposes feature encoding into entity-specific, relation-specific, and shared partitions via gating mechanisms.
61	These models achieve strong performance but are limited to fixed, predefined schemas and cannot generalize to unseen ontologies without retraining---precisely the zero-shot, ontology-portable scenario that OntoCoDec targets.
62	EnriCo~\cite{zaratiana2024enrico} applies Answer Set Programming (ASP) constraints during decoding of joint entity-relation extraction models, enforcing structural type compatibility at generation time---a decoding-time approach, though with model-specific, manually authored constraints rather than ontology-driven compilation.
63	Training-based methods provide \emph{soft} structural guidance---the model learns to prefer valid outputs but cannot guarantee compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.
64	Importantly, training-based and decoding-time approaches are complementary rather than competing: a system like GoLLIE could be combined with OntoCoDec's constraint layers, using fine-tuning to maximize the probability of valid outputs while decoding-time enforcement eliminates residual violations.
65	OntoCoDec provides \emph{hard} decoding-time enforcement that is training-free, automatically compiled from ontology schemas, and composable with any of these training-based approaches.
66	
67	% ===========================================================================
68	% Paradigm 4: Type-Checking / Ontology Validation
69	% ===========================================================================
70	\paragraph{Post-hoc Ontology Validation.}
71	Rather than constraining generation, several methods validate LLM outputs against ontological rules after generation, applying a detect-then-fix paradigm.
72	ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale---but constraint adherence relies on prompt-level guidance, not enforcement, leaving residual violations unaddressed.
73	SPIRES/OntoGPT~\cite{spires_2024} provides an ontology-based extraction framework that grounds LLM outputs against OBO ontologies post-generation, validating extracted entities and relations through ontology lookup and correcting mismatches in a second pass---representing the prompt-then-validate paradigm in the biomedical domain.
74	OntoLogX~\cite{ontologx_2025} applies SHACL validation to LLM-generated knowledge graphs, iteratively re-prompting the LLM to correct constraint violations and reducing them by approximately 10$\times$ across multiple correction rounds---demonstrating the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
75	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB, though their constrained inference operates over a discrete candidate set rather than during autoregressive generation.
76	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating RDF triple insertions against RDFS domain/range constraints, where each validation step requires a separate LLM call---effective but computationally expensive at scale.
77	RELATE~\cite{olasunkanmi2025relate} addresses the alignment gap between LLM-extracted biomedical relations and standardized ontology predicates through a three-stage pipeline: ontology preprocessing with predicate embeddings, similarity-based retrieval via SapBERT, and LLM-based reranking with negation handling, achieving 94\% accuracy@10 on ChemProt.
78	While RELATE demonstrates effective ontology grounding for relation extraction, its constraints are applied \emph{post-extraction} through retrieval and reranking rather than during generation, and it requires domain-specific embedding models trained on biomedical corpora.
79	OntoCoDec enforces ontology constraints \emph{during} autoregressive decoding and requires no additional trained components beyond the base LLM.
80	Concurrently, \citet{zhou2026ontologytools} compile OWL ontologies into executable tool interfaces within The World Avatar framework, requiring LLM agents to invoke ontology-aware tools that enforce semantic constraints during knowledge graph construction from scientific text.
81	This ``ontology-to-tools'' approach shares OntoCoDec's philosophy of compiling formal ontological knowledge into runtime enforcement mechanisms, but operates at the tool-call level (constraining which API functions the agent invokes) rather than at the token level (constraining which tokens the decoder produces), and requires an agentic multi-step workflow rather than single-pass autoregressive generation.
82	\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms---a middle ground between unconstrained generation and hard enforcement that reduces but cannot eliminate violations.
83	Post-hoc validation detects violations after generation, requiring rejection or correction cycles that waste compute---in our setting, 15.37\% of generated triples contain domain/range violations under unconstrained decoding, representing substantial wasted generation effort.
84	OntoCoDec \emph{prevents} violations during decoding, redirecting probability mass to valid alternatives rather than discarding invalid outputs, with only marginal overhead from logits masking compared to the cost of regenerating or correcting violated triples.
85	Soft-constraint approaches such as ontology-weighted beam scoring reduce violation frequency but cannot eliminate it, whereas OntoCoDec achieves near-complete to substantial elimination (DR$\downarrow$94\% on SciERC, $\downarrow$45\% on DocRED).
86	
87	% ===========================================================================
88	% Paradigm 5: Constrained Decoding Quality Concerns
89	% ===========================================================================
90	\paragraph{Quality Impact of Constrained Decoding.}
91	A growing body of work raises concerns that constrained decoding degrades LLM generation quality, particularly for reasoning-intensive tasks where format enforcement interferes with chain-of-thought processes.
92	\citet{tam2024letmespeak} conduct a comprehensive evaluation showing that rigid format constraints (JSON, XML) harm performance on math and multi-hop QA benchmarks but \emph{benefit} classification-style tasks such as slot filling---a distinction directly relevant to IE, which is fundamentally an extraction (classification-like) task rather than a reasoning task.
93	CRANE~\cite{banerjee2025crane} provides theoretical analysis of why restricting outputs to narrow grammars suppresses chain-of-thought reasoning by eliminating intermediate reasoning tokens, and proposes an alternating strategy between unconstrained reasoning phases and constrained output phases to mitigate this effect.
94	\citet{schall2025hiddencost} conduct a systematic study across 11 models and multiple benchmarks, finding 10--30\% semantic correctness degradation on reasoning tasks under structural constraints, with larger models showing greater absolute degradation.
95	\citet{zhou2026snowballing} identify ``structure snowballing''---a failure mode where format compliance cognitive load traps models in repetitive structural patterns rather than improving reasoning during self-correction iterations.
96	These findings establish a legitimate concern for constrained decoding in reasoning-heavy applications.
97	However, information extraction occupies a fundamentally different regime: the model extracts entities and relations from input text rather than generating novel reasoning chains, and \citet{tam2024letmespeak}'s own results show that extraction-style tasks are robust to---or even benefit from---format constraints.
98	OntoCoDec addresses this concern empirically: domain/range violations decrease by 94\% on SciERC (15.37\%$\to$0.93\%) and 45\% on DocRED, with \emph{zero} F1 degradation on SciERC (R-F1 8.36\% vs.\ 8.23\% unconstrained, $+$0.13pp, not statistically significant).
99	Critically, OntoCoDec's constraints target only type tokens (entity types, relation labels), leaving free-text spans---entity surface forms and their boundaries---entirely unconstrained, which minimizes the distribution distortion that causes quality degradation in reasoning tasks.
100	A two-pass variant (S2), explored in ablation (Section~5), separates extraction and constraint enforcement into distinct passes, analogous to CRANE's alternating strategy; however, our primary single-pass approach already avoids reasoning interference by constraining only type tokens while leaving free-text spans unconstrained.
101	
102	% ===========================================================================
103	% Our Approach
104	% ===========================================================================
105	\paragraph{Our Approach.}
106	OntoCoDec occupies a unique position in this landscape: it is the first system to \emph{automatically compile} IE ontology schemas---including domain/range axioms---into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement without manually authored rules.
107	Unlike vocabulary-constrained methods that restrict individual tokens to a fixed set, OntoCoDec enforces \emph{cross-field relational constraints} through a stateful entity registry that tracks extracted types during autoregressive generation, enabling dynamic constraint evaluation that depends on previously decoded content.
108	This approach is orthogonal to supervised IE methods and applicable to any autoregressive LM without model modification or additional training.
109	Unlike training-based IE systems, OntoCoDec is training-free and achieves near-complete to substantial elimination of type violations at inference time (DR$\downarrow$94\% on SciERC, $\downarrow$45\% on DocRED); unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives with zero quality cost on SciERC (R-F1 8.36\% vs.\ 8.23\% unconstrained).
110	The two constraint layers---grammar (structural) and semantic (relational)---compose via bitwise AND with an enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "696e8f77-9c77-4771-9b20-8b6bd658ab5d",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "1aac854e-f950-40e6-a4f5-8530153502ca",
  "sourceToolAssistantUUID": "696e8f77-9c77-4771-9b20-8b6bd658ab5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T21:27:07.628Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PQVZLnSzMJ2fvWRaGw3yyT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aac854e-f950-40e6-a4f5-8530153502ca",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AnQQDRSpsepQnddHLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d0448e3-5adf-4247-97d3-ade8693067ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cmnjjum7xbFj2mAWgGSFdv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 26904,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3038
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 26904,
          "cache_creation_input_tokens": 3038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3038,
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

_source line 25 · 2026-05-14T21:27:07.634Z_

<details><summary>↩ Tool result · `toolu_01PQVZLnSzMJ2fvWRaGw3yyT`</summary>

```text
1	% Section 1: Introduction for OntoCoDec paper
2	% Target: EMNLP 2026 (ARR submission May 25, 2026)
3	
4	\section{Introduction}
5	\label{sec:introduction}
6	
7	Large language models are increasingly deployed for information extraction in zero-shot and few-shot settings, bypassing the need for task-specific training data~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}.
8	However, when an LLM generates relation triples $(h, r, t)$, neither the head entity $h$ nor the tail entity $t$ is guaranteed to carry an entity type consistent with the domain and range constraints that the target ontology prescribes for relation $r$.
9	We refer to such outputs as \emph{domain/range violations}---structurally well-formed triples that are nonetheless invalid under the ontology's type signature.
10	In a systematic study across two standard IE benchmarks, we find that these violations are pervasive: 15.4\% of generated triples on SciERC~\cite{luan2018scierc} and 18.7\% on DocRED~\cite{yao2019docred} violate domain/range constraints when no enforcement mechanism is applied.
11	Crucially, violations are not uniformly distributed across relation types.
12	Relations with tight type constraints---few valid entity-type pairs---exhibit far higher violation rates (\textsc{Compare}: 42.4\%, \textsc{Feature-of}: 33.5\%), while loosely constrained relations remain nearly violation-free (\textsc{Used-for}: 0.8\%).
13	This pattern holds across datasets of vastly different ontology sizes (7 vs.\ 96 relation types), indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
14	For downstream applications such as knowledge graph construction, ontology-grounded reasoning, and safety-critical extraction in biomedical or legal domains, such systematic type invalidity is unacceptable.
15	
16	Existing approaches address this problem at different levels but leave a fundamental gap.
17	Schema-informed prompting---explicitly describing domain/range constraints in the prompt---reduces violations by 62\% on average, yet leaves residual rates above 5\% and is unreliable at the per-relation level: for \textsc{Evaluate-for}, violations actually increase by 5.8 percentage points, revealing a \emph{prior-constraint conflict} where prompt-level signals interfere with the model's learned type associations.
18	Grammar-constrained decoding frameworks such as XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, and LMQL~\cite{beurer-kellner2023lmql} guarantee syntactic well-formedness (e.g., valid JSON) and can restrict output vocabularies, but do not encode cross-field semantic constraints such as ``if $r$ = \textsc{Feature-of}, then $h$ must be a \textsc{Method} or \textsc{OtherScientificTerm}.''
19	Post-hoc validation can filter invalid triples but wastes 14--15\% of generation compute on outputs that are discarded, cannot redirect probability mass toward valid alternatives during decoding, and is incompatible with streaming extraction scenarios.
20	Training-based approaches~\cite{sainz2024gollie,lu2022uie} incorporate schema knowledge through fine-tuning, but require task-specific training data and provide only soft guidance---they reduce but cannot eliminate violations.
21	
22	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that automatically compiles an IE ontology schema into two composable layers of decoding-time constraints.
23	The \emph{grammar layer} translates the ontology's entity types, relation types, and output structure into a context-free grammar via XGrammar, enforcing JSON well-formedness and vocabulary validity at every generated token.
24	The \emph{semantic layer} implements a \texttt{TypeConstraintProcessor} that maintains a stateful entity registry during generation: as entities and their types are decoded, the registry records each assignment, and when a relation's arguments are generated, dynamic logit masking restricts the output to entity types compatible with the relation's domain/range specification.
25	The two layers compose via bitwise AND of their token masks, with an \emph{enabling dependency}: the grammar layer guarantees that every generated relation type belongs to the valid vocabulary, which in turn enables the semantic layer to look up and enforce domain/range rules for that type.
26	This architecture is training-free and designed to be model-agnostic.
27	On SciERC, OntoCoDec reduces domain/range violations from 15.37\% to 0.93\% ($\downarrow$94\%) while remaining F1-neutral (relation F1 $+$0.13pp, within noise).
28	
29	Our contributions are as follows:
30	\begin{enumerate}
31	    \item We present the first systematic quantification of ontology constraint violations in LLM-based IE, revealing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
32	    \item We introduce OntoCoDec, a framework that compiles IE ontology domain/range constraints into semantic decoding-time constraints---the first method to enforce cross-field type validity during autoregressive generation for IE.
33	    \item We provide a decidability taxonomy of IE ontology constraints (purely local, prefix-decidable with state, truly non-local) and formalize the enabling dependency between grammar and semantic layers.
34	    \item We validate OntoCoDec on SciERC and DocRED, demonstrating near-complete violation elimination (DR 15.4\%$\rightarrow$0.93\%, $\downarrow$94\%) at zero F1 cost, with cross-dataset generalization.
35	\end{enumerate}
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d0448e3-5adf-4247-97d3-ade8693067ed",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "4b60e684-28c2-42ab-b46c-48645a06b03a",
  "sourceToolAssistantUUID": "6d0448e3-5adf-4247-97d3-ade8693067ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T21:27:12.153Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HnkrJtX9fGqsZJLb4QKF5Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b60e684-28c2-42ab-b46c-48645a06b03a",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AnixvR4so6GoaDvibd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ef755b3-eaeb-47f0-ba10-0b5a5beda750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmfV5A8fixkpj7MMWuozn7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7478,
      "cache_read_input_tokens": 29942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 27 · 2026-05-14T21:27:12.158Z_

<details><summary>↩ Tool result · `toolu_01HnkrJtX9fGqsZJLb4QKF5Q`</summary>

```text
1	\begin{abstract}
2	LLM-based information extraction systems produce systematic ontology constraint violations during autoregressive generation.
3	On SciERC (7 relation types), 15.37\% of extracted triples violate domain/range type constraints; on DocRED (96 relation types), 18.46\%.
4	Violation rates are governed by \emph{constraint tightness} ($\bar{\tau}$, the fraction of type-pair space ruled out per relation): DocRED ($\bar{\tau}{=}0.842$, mean 5.68 valid pairs) and SciERC ($\bar{\tau}{=}0.333$, mean 24 valid pairs) exhibit comparable violation rates despite a 14$\times$ difference in ontology size.
5	%
6	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable decoding constraint layers:
7	(1)~a \emph{grammar layer} (XGrammar CFG) enforcing JSON structural validity and restricting entity-type and relation vocabularies to schema-defined values (ET, RV\,$\to$\,0\%); and
8	(2)~a \emph{semantic layer} (TypeConstraintProcessor) enforcing domain/range constraints via a stateful entity registry and dynamic logit masking.
9	The grammar layer is an enabling prerequisite; the two compose via bitwise AND on token-level masks.
10	%
11	On SciERC, \textsc{OntoCoDec} reduces domain/range violations by 94\% (15.37\%\,$\to$\,0.93\%) while maintaining extraction F1 ({+}0.13pp, $p{=}0.58$, not significant).
12	On DocRED, violations decrease by 45\% (18.46\%\,$\to$\,10.21\%) with significant gains in relation F1 ({+}0.50pp, $p{<}0.001$) and entity F1 ({+}1.23pp, $p{<}0.001$) for Qwen3-8B; Llama-3.1-8B shows substantial violation reduction (DR$\downarrow$90.2\%) with F1-neutral impact. % exp_ids: phase2_docred_full, llama_docred_full_s1, llama_docred_unconstrained
13	Results are validated across two models (Qwen3-8B, Llama-3.1-8B-Instruct) and two datasets.
14	Compared with post-hoc filtering, decoding-time enforcement preserves true positives and eliminates entity-type violations that post-hoc methods cannot address.
15	\end{abstract}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ef755b3-eaeb-47f0-ba10-0b5a5beda750",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "76150928-1327-4397-a64f-8dbdecca2cb9",
  "sourceToolAssistantUUID": "6ef755b3-eaeb-47f0-ba10-0b5a5beda750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T21:27:13.111Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uu1y49CG7soWVhY1ha4c5d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76150928-1327-4397-a64f-8dbdecca2cb9",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AnixvR4so6GoaDvibd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4afc15dd-06ca-4de9-9bb7-710fd6319dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmfV5A8fixkpj7MMWuozn7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7478,
      "cache_read_input_tokens": 29942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 29 · 2026-05-14T21:27:13.116Z_

<details><summary>↩ Tool result · `toolu_01Uu1y49CG7soWVhY1ha4c5d`</summary>

```text
1	\section{Violation Landscape}
2	\label{sec:violation_landscape}
3	
4	Before presenting our constrained decoding framework, we first quantify how frequently LLMs violate ontological constraints during information extraction.
5	This analysis serves two purposes: it establishes the practical severity of unconstrained generation and identifies which constraint categories demand enforcement at decoding time versus those addressable through prompting alone.
6	
7	\subsection{Experimental Setup}
8	\label{sec:violation_setup}
9	
10	We evaluate a strong open-weight model, Qwen3-8B~\cite{qwen2025qwen3}, under zero-shot greedy decoding on two IE benchmarks that differ substantially in ontological complexity:
11	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relation types, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents, 96 relation types, avg.\ 5.68 valid type pairs per relation).
12	Both datasets ship with typed entity and relation schemas, enabling automatic constraint checking.
13	
14	We measure four categories of ontological violation:
15	\begin{itemize}[nosep,leftmargin=*]
16	    \item \textbf{Domain/Range (DR):} a predicted triple $(h,r,t)$ satisfies $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$, where $\sigma(r)$ is the set of valid subject--object type pairs for relation $r$.
17	    \item \textbf{Relation Vocabulary (RV):} the predicted relation type $r \notin \mathcal{R}$.
18	    \item \textbf{Entity Type (ET):} the predicted entity type $e \notin \mathcal{E}$.
19	    \item \textbf{Cross-Field Consistency (CF):} the same entity span is assigned different types across distinct triples within one instance.
20	\end{itemize}
21	
22	\subsection{Violation Distribution}
23	\label{sec:violation_distribution}
24	
25	Table~\ref{tab:prompt_comparison} reports violation rates on both benchmarks.
26	On SciERC (1{,}724 predicted triples, 2{,}474 entities), domain/range violations affect 15.37\% of triples, while RV, ET, and CF violations are comparatively rare at 1.39\%, 0.40\%, and 0.08\%, respectively.
27	On DocRED (16{,}540 triples, 19{,}099 entities), DR violations reach 18.70\%---comparable to SciERC despite DocRED's ontology being 14$\times$ larger.
28	This parity suggests that DR violation rates are driven primarily by \emph{constraint tightness} (valid type pairs per relation) rather than ontology size: DocRED averages only 5.68 valid pairs per relation versus SciERC's 26.1.
29	
30	RV violations on DocRED are dramatically higher (28.90\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to faithfully reproduce a target vocabulary from a single in-context specification.
31	ET violations follow a similar trend (7.50\% vs.\ 0.40\%).
32	CF violations remain negligible on both datasets (0.08\%), suggesting that within-instance type coherence is largely maintained even without explicit enforcement.
33	
34	\begin{table}[t]
35	\centering
36	\caption{Ontological violation rates (\%) under unconstrained and schema-informed prompting on SciERC and DocRED (Qwen3-8B, zero-shot). Schema-informed prompting reduces violations but fails to eliminate them, particularly on the larger DocRED ontology.}
37	\label{tab:prompt_comparison}
38	\resizebox{\columnwidth}{!}{%
39	\begin{tabular}{ll cccc}
40	\toprule
41	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
42	\midrule
43	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
44	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
45	\midrule
46	\multirow{2}{*}{DocRED} & Unconstrained & 18.7 & 28.9 & 7.5 & 0.1 \\
47	 & Schema-informed & 12.8 & 18.4 & 0.6 & 0.2 \\
48	\bottomrule
49	\end{tabular}%
50	}
51	\vspace{2pt}
52	{\footnotesize
53	\textit{Exp IDs:}
54	\texttt{mvp\_phase0\_violation\_rate},
55	\texttt{mvp\_phase0\_scierc\_schema},
56	\texttt{mvp\_phase0\_violation\_rate\_docred},
57	\texttt{mvp\_phase0\_docred\_schema}.
58	}
59	\end{table}
60	
61	\subsection{Per-Relation Analysis}
62	\label{sec:per_relation}
63	
64	Figure~\ref{fig:per_relation_dr} breaks down DR violation rates by relation type on SciERC.
65	Violation rates vary by over 40 percentage points across relations:
66	\textsc{Compare} exhibits the highest rate at 42.4\% (28/66 triples), followed by \textsc{Feature-of} at 33.5\% (163/486), \textsc{Part-of} at 25.0\% (18/72), and \textsc{Evaluate-for} at 24.1\% (32/133).
67	At the other extreme, \textsc{Used-for} violates at only 0.76\% (6/787) and \textsc{Conjunction} at 0\% (0/32).
68	
69	This distribution correlates with constraint tightness: \textsc{Compare} permits only a few valid type pairs in the SciERC schema, leaving minimal room for type substitution, whereas \textsc{Used-for} and \textsc{Conjunction} accept a broad range of subject--object type combinations.
70	The pattern implies that violations are not random generation noise but systematic failures to satisfy narrow type constraints---precisely the setting where decoding-time enforcement is most needed.
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
75	\caption{Per-relation domain/range violation rates on SciERC. Violation rates vary by over 40 percentage points across relation types, correlating with constraint tightness.}
76	\label{fig:per_relation_dr}
77	\end{figure}
78	
79	\subsection{Prompt Insufficiency}
80	\label{sec:prompt_insufficiency}
81	
82	A natural question is whether explicitly stating domain/range constraints in the prompt suffices to eliminate violations.
83	We test \emph{schema-informed prompting}, which augments the extraction prompt with the full list of valid type pairs for each relation.
84	
85	On SciERC, schema-informed prompting reduces DR violations from 15.37\% to 5.78\% (a 62.4\% relative reduction) and lowers RV from 1.39\% to 0.30\% and ET from 0.40\% to 0\% (Table~\ref{tab:prompt_comparison}).
86	On DocRED, the reduction is weaker: DR drops from 18.70\% to 12.84\% ($-$31.3\%), RV from 28.90\% to 18.40\%, and ET from 7.50\% to 0.61\%.
87	McNemar's test confirms that all four violation-category improvements are statistically significant ($p < 0.01$) on both datasets.
88	
89	However, aggregate improvements mask per-relation instability.
90	On SciERC, schema-informed prompting reduces DR for \textsc{Feature-of} by 22.3 percentage points and \textsc{Part-of} by 22.5~pp, but \emph{increases} DR for \textsc{Evaluate-for} by 5.8~pp (Figure~\ref{fig:per_relation_dr}).
91	This reversal---where adding constraint information to the prompt worsens compliance on a specific relation---demonstrates that prompt-based approaches lack the guarantee of monotonic improvement across all constraint categories.
92	
93	Two findings emerge from this analysis.
94	First, prompt-based schema enforcement scales poorly with ontological complexity: the relative DR reduction on DocRED (31.3\%) is roughly half that on SciERC (62.4\%), and RV violations remain at 18.40\% even after prompting.
95	Second, even on the simpler SciERC ontology, prompt interventions are unreliable at the per-relation level.
96	These limitations motivate a decoding-time mechanism that enforces constraints \emph{by construction} rather than by instruction, which we present in Section~\ref{sec:method}.
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4afc15dd-06ca-4de9-9bb7-710fd6319dd5",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "69f902f6-c0aa-47ef-ae18-ed55af5c6e1a",
  "sourceToolAssistantUUID": "4afc15dd-06ca-4de9-9bb7-710fd6319dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T21:27:13.484Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YNHH2pb6ESiwvuCk9dN6LR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69f902f6-c0aa-47ef-ae18-ed55af5c6e1a",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AnixvR4so6GoaDvibd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05246c1b-c3a2-4930-a7b2-be1389791efa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmfV5A8fixkpj7MMWuozn7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7478,
      "cache_read_input_tokens": 29942,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7478
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 29942,
          "cache_creation_input_tokens": 7478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7478,
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

_source line 31 · 2026-05-14T21:27:13.495Z_

<details><summary>↩ Tool result · `toolu_01YNHH2pb6ESiwvuCk9dN6LR`</summary>

```text
1	% Section 3 — Method (Draft)
2	% OntoCoDec: Near-Complete Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
10	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and the two decoding strategies (\S\ref{sec:strategies}).
11	Formal analysis of constraint composition and the grammar-first invariant is deferred to Section~\ref{sec:composition}.
12	
13	
14	\subsection{Problem Formulation}
15	\label{sec:formulation}
16	
17	\paragraph{IE as structured generation.}
18	Given an input text $x$, a language model generates a structured JSON output $y$ encoding the extracted information:
19	%
20	\begin{equation}\label{eq:output-schema}
21	\resizebox{.88\columnwidth}{!}{$\displaystyle
22	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
23	$}
24	\end{equation}
25	%
26	where each entity has a name $n_i$ and type $\tau_i$, and each relation triple specifies a head entity $h_j$, tail entity $t_j$, relation type $r_j$, and the corresponding head and tail entity types $\tau^h_j$ and $\tau^t_j$.
27	
28	\paragraph{Ontology schema.}
29	An ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \operatorname{dom}, \operatorname{range})$ defines the set of entity types $\mathcal{E}$, the set of relation types $\mathcal{R}$, and two functions $\operatorname{dom}: \mathcal{R} \to 2^{\mathcal{E}}$ and $\operatorname{range}: \mathcal{R} \to 2^{\mathcal{E}}$ that specify, for each relation, the entity types permitted as head and tail respectively.
30	
31	\paragraph{Ontology compliance.}
32	A relation triple $(h, r, t)$ with $\operatorname{type}(h) = \tau^h$ and $\operatorname{type}(t) = \tau^t$ is \emph{type-valid} with respect to $\mathcal{O}$ if and only if:
33	%
34	\begin{equation}\label{eq:type-valid}
35	  \tau^h \in \operatorname{dom}(r) \;\wedge\; \tau^t \in \operatorname{range}(r).
36	\end{equation}
37	%
38	We define the \emph{domain/range violation rate} (DR) as the fraction of generated triples that fail Eq.~\eqref{eq:type-valid}.
39	
40	\paragraph{Objective.}
41	We seek a decoding strategy that maximizes $P(y \mid x)$ subject to ontology compliance: all generated triples should be type-valid under $\mathcal{O}$, and the output $y$ must be structurally well-formed JSON conforming to the schema in Eq.~\eqref{eq:output-schema}.
42	
43	\paragraph{Constraint decidability.}
44	Not all ontology constraints are enforceable at every point during left-to-right generation.
45	We distinguish three classes by \emph{prefix-decidability}---i.e., when sufficient information becomes available in the generated prefix:
46	%
47	\begin{enumerate}[leftmargin=*,nosep]
48	  \item \textbf{Local constraints} depend only on the current token position.
49	    Entity-type membership ($\tau_i \in \mathcal{E}$) and relation-vocabulary membership ($r_j \in \mathcal{R}$) are local: each candidate token can be checked against the ontology vocabulary independently.
50	  \item \textbf{Prefix-decidable constraints} depend on the current token plus previously generated context.
51	    Domain/range constraints are prefix-decidable: once the head entity, its type, and the relation type have been generated, the set of valid tail types is fully determined.
52	  \item \textbf{Non-local constraints} depend on information not yet generated.
53	    Forward coreference---where a later entity mention determines the type of an earlier one---is inherently non-local and falls outside the scope of single-pass autoregressive decoding.
54	\end{enumerate}
55	%
56	OntoCoDec's two-layer design covers the first two classes: the grammar layer handles local constraints, and the semantic layer handles prefix-decidable constraints.
57	We revisit this taxonomy in Section~\ref{sec:composition} to formalize constraint composition properties.
58	
59	
60	\subsection{Grammar Layer}
61	\label{sec:grammar}
62	
63	The grammar layer compiles the ontology schema $\mathcal{O}$ into a context-free grammar (CFG) that is enforced at every decoding step via logit masking.
64	This compilation proceeds in two stages.
65	
66	\paragraph{Schema-to-grammar compilation.}
67	Given $\mathcal{O}$, we first generate a JSON Schema that encodes the output structure in Eq.~\eqref{eq:output-schema}, with \texttt{enum} constraints restricting entity types to $\mathcal{E}$, relation types to $\mathcal{R}$, and head/tail types to $\mathcal{E}$.
68	The JSON Schema is then compiled into an EBNF grammar using XGrammar~\cite{dong2025xgrammar}, which converts the schema into a pushdown automaton that tracks JSON nesting, field names, string boundaries, and enum membership.
69	
70	\paragraph{Logit masking.}
71	At each decoding step $t$, the grammar processor computes the set of grammar-valid tokens $G(t) \subseteq V$ based on the automaton state, and masks all tokens outside $G(t)$ by setting their logits to $-\infty$.
72	This enforces three categories of constraints simultaneously:
73	(i)~\emph{structural validity}---the output is always well-formed JSON with correct field names and nesting;
74	(ii)~\emph{relation vocabulary membership}---$r_j \in \mathcal{R}$ for all generated relations; and
75	(iii)~\emph{entity type membership}---$\tau_i \in \mathcal{E}$ for all generated entity types.
76	
77	\paragraph{What grammar does not enforce.}
78	The grammar layer does not encode domain/range constraints ($\operatorname{dom}$, $\operatorname{range}$), because these depend on the specific entity types appearing in each triple---information that is only available during generation.
79	This is precisely the gap that the semantic layer fills.
80	
81	\paragraph{Empirical profile.}
82	On SciERC, grammar-only constraints eliminate relation vocabulary violations entirely (1.39\%\,$\to$\,0\%) and entity type violations entirely (0.40\%\,$\to$\,0\%), with no measurable F1 impact (R-F1 8.23, E-F1 30.98 vs.\ unconstrained R-F1 8.23, E-F1 31.01).
83	Domain/range violations remain effectively unchanged (15.37\%\,$\to$\,14.84\%), confirming that grammar constraints enforce structural but not semantic validity.
84	
85	
86	\subsection{Semantic Layer}
87	\label{sec:semantic}
88	
89	The semantic layer enforces domain/range type constraints through a stateful logits processor that maintains an entity registry during generation.
90	
91	\subsubsection{Entity Registry}
92	\label{sec:entity-registry}
93	
94	As the model generates the entity list portion of the output, the semantic layer builds an \emph{entity registry} $\mathcal{D}: \text{name} \to \text{type}$ that maps each entity mention to its declared type.
95	This registry is populated incrementally: when the model completes an entity entry $\{n_i, \tau_i\}$, the pair $(n_i, \tau_i)$ is added to $\mathcal{D}$.
96	The registry is then consulted during relation generation to look up the declared types of head and tail entities.
97	
98	\subsubsection{Position Detection}
99	\label{sec:position-detection}
100	
101	At each decoding step $t$, the processor determines which field is currently being generated by pattern-matching on the decoded text prefix.
102	We define a set of field positions $\mathcal{F} = \{\textsc{EntityType},$ $\textsc{RelationType},$ $\textsc{HeadType},$ $\textsc{TailType},$ $\textsc{FreeText}\}$.
103	The detector examines the trailing context of the decoded output to identify the active field based on JSON key patterns (e.g., the token sequence following \texttt{"head\_type":} indicates a \textsc{HeadType} position).
104	Only at type-bearing positions (\textsc{HeadType}, \textsc{TailType}) does the semantic layer activate its constraint masks.
105	
106	\subsubsection{Dynamic Masking}
107	\label{sec:dynamic-masking}
108	
109	When a type-bearing position is detected, the processor computes a semantic mask $S(t) \subseteq V$ that restricts generation to type-valid tokens.
110	The masking rules differ by position:
111	
112	\paragraph{Head type masking.}
113	At a \textsc{HeadType} position within a relation triple, the processor considers two information sources: the entity registry $\mathcal{D}$ and the current relation type $r_j$ (if already generated).
114	If $h_j \in \mathcal{D}$ and the registered type $\mathcal{D}[h_j] \in \operatorname{dom}(r_j)$, the mask allows only that type: $S(t) = \{\operatorname{tok}(\mathcal{D}[h_j])\}$, ensuring consistency with both the entity list and domain constraints.
115	Otherwise, if $r_j$ is known, the mask falls back to all domain-valid head types: $S(t) = \{\operatorname{tok}(\tau) : \tau \in \operatorname{dom}(r_j)\}$.
116	If $r_j$ is not yet available, no semantic mask is applied and the grammar layer's entity-type membership constraint remains the sole guard.
117	
118	\paragraph{Tail type masking.}
119	At a \textsc{TailType} position, the processor has access to the current relation type $r_j$ and head type $\tau^h_j$ from the already-generated prefix.
120	It computes the set of valid tail types as $\operatorname{range}(r_j)$ and, if the tail entity $t_j$ is found in $\mathcal{D}$, further restricts to the registered type if it is domain/range-valid.
121	This implements the core prefix-decidable constraint: once $(h_j, r_j, \tau^h_j)$ are known, the valid $\tau^t_j$ values are fully determined by $\operatorname{range}(r_j)$.
122	
123	\paragraph{Implementation.}
124	Each type $\tau \in \mathcal{E}$ is mapped to the token ID of its first subword token under the model's tokenizer.
125	We pre-verify that these first-token IDs are unique across all entity types, which holds for both SciERC (6 types) and DocRED (6 types) with the Qwen3-8B tokenizer.
126	The semantic mask is applied by setting the logits of disallowed first-token IDs to $-\infty$.
127	
128	\subsubsection{Grammar-Semantic Interaction}
129	\label{sec:interaction}
130	
131	The semantic mask $S(t)$ is combined with the grammar mask $G(t)$ via conjunction:
132	%
133	\begin{equation}\label{eq:mask-conjunction}
134	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
135	\end{equation}
136	%
137	so a token is permitted only if it satisfies both structural and type-level constraints.
138	This conjunction embodies an \emph{enabling dependency}: the semantic layer's constraint lookup requires the relation type to be a valid member of $\mathcal{R}$---a property guaranteed only when the grammar layer is active.
139	Without grammar enforcement, the model may generate out-of-vocabulary relation types for which no $\operatorname{dom}$/$\operatorname{range}$ rules exist, rendering semantic masking ineffective.
140	Empirically, semantic-only constraints reduce DR by only 24\% (15.37\%\,$\to$\,11.65\%) and fail to eliminate RV (1.51\%) or ET (0.40\%) violations, whereas the full combination achieves 94\% DR reduction.
141	
142	When $S(t) \cap G(t) = \emptyset$---the semantic layer would mask out all grammar-valid tokens---the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.
143	This \emph{grammar-first invariant} reflects a deliberate priority ordering: structural integrity is a hard constraint, while a type violation is a soft error detectable by downstream validation.
144	We formalize this invariant and analyze constraint composition in detail in Section~\ref{sec:composition}.
145	
146	
147	\subsection{Decoding Strategies}
148	\label{sec:strategies}
149	
150	We consider two decoding strategies that differ in how entity and relation generation are orchestrated.
151	
152	\paragraph{S1: Single-pass decoding.}
153	Both constraint layers are active throughout a single generation pass.
154	The entity registry is populated as entities are generated and is immediately available for relation-level type checking within the same pass.
155	This is the simpler and recommended strategy.
156	
157	\paragraph{S2: Two-pass decoding.}\label{sec:s2}
158	In the first pass, the model generates only the entity list under grammar-only constraints.
159	The extracted entities are then used to compile an input-dependent grammar that additionally constrains head and tail entity names to match declared entities.
160	In the second pass, the model generates relations under this tighter grammar plus semantic constraints.
161	The two-pass separation aims to provide a more complete entity registry before relation generation begins, potentially improving type consistency.
162	
163	\paragraph{Comparison.}
164	On SciERC, S1 and S2 achieve comparable DR reduction (0.93\% vs.\ 0.97\%) but S1 yields higher relation F1 (8.36 vs.\ 8.03) and generates more triples (1,729 vs.\ 1,644).
165	S2 does not resolve the cross-field consistency trade-off introduced by semantic enforcement (CF 8.03\% vs.\ 9.90\% for S1, both elevated from 0.08\% unconstrained).
166	We adopt S1 as the primary configuration; S2 is retained as an ablation variant.
167	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05246c1b-c3a2-4930-a7b2-be1389791efa",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "e9e1184b-9f22-411c-90d6-fad71691cd75",
  "sourceToolAssistantUUID": "05246c1b-c3a2-4930-a7b2-be1389791efa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T21:27:18.792Z_

<details open><summary>🔧 Tool call — Read · `toolu_018htimAfkT6QdYjANoNtwW2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9e1184b-9f22-411c-90d6-fad71691cd75",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AoA7WrDSuG7Q7toNmV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5efc1266-2138-4896-b4d9-136336c02e0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RM5tnsngfJTLaXxDcpiVca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7460,
      "cache_read_input_tokens": 37420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7460,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 33 · 2026-05-14T21:27:18.797Z_

<details><summary>↩ Tool result · `toolu_018htimAfkT6QdYjANoNtwW2`</summary>

```text
1	% Section 5: Constraint Composition (§5 in main.tex)
2	% Draft — OntoCoDec Framework
3	
4	At each decoding step $t$, both layers produce a binary token mask over the vocabulary $V$.
5	Let $G(t) \subseteq V$ denote the set of tokens permitted by the grammar layer (valid JSON structure and ontology-vocabulary membership),
6	and $S(t) \subseteq V$ the set permitted by the semantic layer (domain/range type compliance given the current entity registry state).
7	The final mask is their conjunction:
8	%
9	\begin{equation}\label{eq:composition}
10	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
11	\end{equation}
12	%
13	so that a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
14	The conjunction is asymmetric in an important sense: the semantic layer operates \emph{strictly within} the grammar-valid set, i.e., $S(t)$ is defined only over $G(t)$.
15	This reflects the enabling dependency described in \S\ref{sec:method}: grammar validity is a precondition for semantic enforcement, because the semantic layer must identify the current relation type to look up its domain/range rules—an operation that is only well-defined when the relation type belongs to the ontology vocabulary.
16	
17	\paragraph{Grammar-First Fallback.}
18	
19	The conjunction in Eq.~\eqref{eq:composition} requires the precondition $S(t) \cap G(t) \neq \emptyset$: at least one token must be simultaneously grammar-valid and semantically valid.
20	When this precondition is violated—which can occur under tight ontology constraints where the allowed entity types for a relation do not overlap with the grammar-valid tokens at a particular position—na\"{\i}ve application of the semantic mask sets all grammar-valid tokens to $-\infty$ while grammar-invalid tokens retain finite (though heavily penalized) logits.
21	The resulting argmax selects a grammar-invalid token, breaking JSON structure.
22	We enforce a \emph{grammar-first fallback rule}: before applying the semantic mask, we verify that at least one semantically allowed type token has a logit above a grammar-validity threshold $\tau_g = -10^{8}$.
23	If $S(t) \cap G(t) = \emptyset$, semantic masking is skipped entirely, and the grammar layer alone controls token selection.
24	This reflects a deliberate priority ordering: structural integrity (grammar) is a hard constraint, while a type violation is a soft error detectable by downstream validation.
25	
26	
27	\paragraph{Constraint Tightness.}
28	
29	We quantify the restrictiveness of semantic constraints with a per-relation \emph{tightness} measure.
30	For a relation $r \in \mathcal{R}$, let $\mathcal{V}(r)$ denote the set of entity type pairs $(\tau^h, \tau^t)$ observed in the training ontology for relation $r$, and let $\mathcal{T}$ denote the full entity type vocabulary.
31	We define the tightness of $r$ as:
32	%
33	\begin{equation}\label{eq:tightness}
34	  \tau(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
35	\end{equation}
36	%
37	where $\mathcal{V}(r) \subseteq \operatorname{dom}(r) \times \operatorname{range}(r)$ and $\tau(r) \in [0, 1]$: $\tau = 1$ indicates that $r$ admits no valid type pair (a degenerate case), while $\tau = 0$ means all type combinations are permitted and the semantic mask imposes no additional restriction beyond grammar.
38	Observed pairs are typically a strict subset of $\operatorname{dom}(r) \times \operatorname{range}(r)$: for example, SciERC's \textsc{Used-for} relation has $|\operatorname{dom}| = |\operatorname{range}| = 6$ entity types, yielding a Cartesian product of 36, but only 35 pairs are attested in the data (\emph{Metric}$\times$\emph{Metric} is unobserved).
39	The mean tightness $\bar{\tau} = \frac{1}{|\mathcal{R}|}\sum_{r \in \mathcal{R}} \tau(r)$ characterizes the overall restrictiveness of an ontology's type constraints.
40	Intuitively, tighter constraints cause the semantic mask $S(t)$ to eliminate a larger fraction of grammar-valid tokens at type-bearing positions, increasing the probability that $S(t) \cap G(t) = \emptyset$ and triggering the grammar-first fallback.
41	Consequently, ontologies with high mean tightness retain higher residual domain/range violation rates despite full constraint enforcement.
42	Section~\ref{sec:docred-results} demonstrates this empirically: DocRED ($\bar{\tau} = 0.842$, 5.68 valid pairs per relation) achieves 45--90\% DR reduction across models, whereas SciERC ($\bar{\tau} = 0.333$, 24 valid pairs per relation) achieves 94--99\%, with the residual modulated by model-specific baseline violation rates (Section~\ref{sec:cross-model}).
43	
44	
45	\paragraph{Decidability Taxonomy.}
46	
47	Not all ontology constraints can be enforced at the same point during autoregressive generation.
48	We classify them by \emph{when} sufficient information becomes available:
49	%
50	\begin{enumerate}[leftmargin=*,nosep]
51	  \item \textbf{Local constraints} require only the current token. Entity-type and relation-vocabulary membership fall in this class: each candidate token can be checked against the ontology vocabulary independently, which the grammar layer handles via CFG and enum rules.
52	  \item \textbf{Prefix-decidable constraints} require the current token plus previously generated context. Domain/range constraints are prefix-decidable: once the head entity type and relation type have been generated, the valid tail entity types are fully determined. The semantic layer implements this via a stateful entity registry that tracks decoded types and activates the appropriate logit mask at each type-bearing position.
53	  \item \textbf{Non-local constraints} require information not yet generated. Forward coreference—where a later mention determines the type of an earlier one—is inherently non-local and falls outside the scope of single-pass left-to-right decoding.
54	\end{enumerate}
55	%
56	OntoCoDec's two-layer design covers the first two classes: grammar for local, semantic for prefix-decidable. The non-local class motivates the two-pass strategy (S2, \S\ref{sec:s2}), which partially addresses cross-field consistency by separating entity extraction from relation generation, though it does not fully resolve forward coreference (\S\ref{sec:limitations}).
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5efc1266-2138-4896-b4d9-136336c02e0f",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "63affbdd-d08a-4549-b03c-7958c32fe7ad",
  "sourceToolAssistantUUID": "5efc1266-2138-4896-b4d9-136336c02e0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T21:27:19.795Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QoTxAvXV1fEVPVuxSVLYQj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63affbdd-d08a-4549-b03c-7958c32fe7ad",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AoA7WrDSuG7Q7toNmV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1318704-2e5b-45ec-bcd5-59c6a47d02ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RM5tnsngfJTLaXxDcpiVca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7460,
      "cache_read_input_tokens": 37420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7460,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 35 · 2026-05-14T21:27:19.801Z_

<details><summary>↩ Tool result · `toolu_01QoTxAvXV1fEVPVuxSVLYQj`</summary>

```text
1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Results on SciERC}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\begin{tabular}{@{}l rrrrr rr@{}}
24	\toprule
25	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
26	& \multicolumn{2}{c}{\textbf{F1}} \\
27	\cmidrule(lr){2-6} \cmidrule(l){7-8}
28	\textbf{Mode}
29	  & DR\,$\downarrow$ & $\Delta$DR
30	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
31	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
32	\midrule
33	Unconstrained
34	  & 15.37 & ---
35	  & 1.39  & 0.40
36	  & 0.08
37	  & 8.23  & 31.01 \\
38	Grammar
39	  & 14.84 & $\downarrow$3\%
40	  & \textbf{0} & \textbf{0}
41	  & 0.08
42	  & 8.23  & 30.98 \\
43	Semantic
44	  & 11.65 & $\downarrow$24\%
45	  & 1.51  & 0.40
46	  & 2.71
47	  & 8.15  & 31.01 \\
48	Full (S1)
49	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
50	  & \textbf{0} & \textbf{0}
51	  & 9.90
52	  & \textbf{8.36} & 30.98 \\
53	Full (S2)
54	  & 0.97  & $\downarrow$94\%
55	  & \textbf{0} & \textbf{0}
56	  & 8.03
57	  & 8.03  & \textbf{31.90} \\
58	\bottomrule
59	\end{tabular}
60	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
61	DR: domain/range violation rate;
62	RV: relation vocabulary violation rate;
63	ET: entity type violation rate;
64	CF: cross-field consistency violation rate.
65	$\Delta$DR: relative DR reduction vs.\ the unconstrained baseline.
66	$\downarrow$\,/\,$\uparrow$: lower\,/\,higher is better.
67	Best per column in \textbf{bold} (CF excluded---see text).
68	F1 scores are multiplied by 100.
69	Statistical significance assessed via bootstrap resampling (10{,}000 iterations).}
70	\label{tab:scierc-ablation}
71	\end{table}
72	
73	% ──────────────────────────────────────────
74	%  (a) Core result
75	% ──────────────────────────────────────────
76	\paragraph{Core result: near-complete DR elimination at zero F1 cost.}
77	The full two-layer constraint configuration (S1) reduces domain/range
78	violations from 15.37\% to 0.93\%, a 94\% relative reduction,
79	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
80	while relation F1 moves from 8.23 to 8.36 ($+$0.13\,pp; bootstrap 95\% CI [$-$0.24, $+$0.58]\,pp, $p = 0.58$, 10{,}000 iterations).
81	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
82	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
83	The difference is not statistically significant ($p = 0.58$), confirming
84	that constraint enforcement is F1-neutral on this dataset.
85	At the per-relation level, violations drop from 42.42\% to 2.82\% on
86	\textsc{Compare}, from 33.54\% to 1.21\% on \textsc{Feature-of}, and
87	reach 0\% on four of seven relation types
88	(\textsc{Conjunction}, \textsc{Hyponym-of}, \textsc{Part-of},
89	\textsc{Used-for}).
90	% phase2_scierc_full_s1 per_relation_dr: Compare=0.0282,
91	%   Feature-of=0.0121, Hyponym-of=0, Part-of=0, Used-for=0, Conjunction=0
92	However, full constraint enforcement elevates cross-field consistency
93	violations from 0.08\% to 9.90\%;
94	% phase2_scierc_unconstrained: CF=0.0008; phase2_scierc_full_s1: CF=0.099
95	we analyze this trade-off in Section~\ref{sec:discussion}.
96	
97	% ──────────────────────────────────────────
98	%  (b) Grammar layer
99	% ──────────────────────────────────────────
100	\paragraph{Grammar layer: cost-free structural guarantees.}
101	Grammar-only constraints completely eliminate both relation vocabulary
102	violations (1.39\%\,$\to$\,0\%) and entity type violations
103	(0.40\%\,$\to$\,0\%), with no measurable impact on F1
104	(R-F1 8.23, E-F1 30.98).
105	% phase2_scierc_grammar_only: RV=0, ET=0, R-F1=0.0823, E-F1=0.3098
106	Domain/range violations remain effectively unchanged
107	(15.37\%\,$\to$\,14.84\%, $-$0.53\,pp), confirming that grammar
108	constraints enforce output structure---valid JSON, correct relation
109	vocabulary, valid entity types---but do not address cross-field
110	semantic constraints.
111	% phase2_scierc_grammar_only: DR=0.1484
112	The grammar layer thus provides two categories of violation elimination
113	at zero cost, establishing the structural preconditions on which the
114	semantic layer depends.
115	
116	% ──────────────────────────────────────────
117	%  (c) Enabling dependency
118	% ──────────────────────────────────────────
119	\paragraph{Enabling dependency: grammar enables semantic enforcement.}
120	Applying semantic constraints alone reduces DR by only 24\%
121	(15.37\%\,$\to$\,11.65\%) and, critically, cannot eliminate
122	relation vocabulary violations (RV\,=\,1.51\%) or entity type
123	violations (ET\,=\,0.40\%).
124	% phase2_scierc_semantic_only: DR=0.1165, RV=0.0151, ET=0.004
125	When the grammar layer is added (Full S1), DR drops a further 92\%
126	relative to the semantic-only configuration
127	(11.65\%\,$\to$\,0.93\%).
128	% phase2_scierc_full_s1: DR=0.0093; delta=(11.65-0.93)/11.65=0.920
129	This demonstrates an \emph{enabling dependency} rather than mere
130	additivity: without grammar-enforced vocabulary constraints, the
131	semantic layer encounters out-of-vocabulary relation types for which
132	no domain/range rules exist, rendering its type checking ineffective.
133	The two layers are therefore complementary with a prerequisite
134	structure---grammar must be active for semantic constraints to reach
135	their full enforcement capacity.
136	
137	% ──────────────────────────────────────────
138	%  (d) S1 vs S2
139	% ──────────────────────────────────────────
140	\paragraph{S1 vs.\ S2: single-pass suffices.}
141	The two-pass strategy (S2) achieves comparable DR
142	(0.97\% vs.\ 0.93\%) but lower relation F1
143	(8.03 vs.\ 8.36, $-$0.33\,pp) and generates fewer relation triples
144	(1{,}644 vs.\ 1{,}729).
145	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, triples=1644
146	% phase2_scierc_full_s1: DR=0.0093, R-F1=0.0836, triples=1729
147	S2 shows a modestly lower CF rate (8.03\% vs.\ 9.90\%), but both
148	configurations exhibit substantially elevated CF relative to the
149	unconstrained baseline (0.08\%), indicating that two-pass decoding
150	does not resolve the cross-field consistency trade-off
151	(Section~\ref{sec:discussion}).
152	% phase2_scierc_full_s2: CF=0.0803; phase2_scierc_full_s1: CF=0.099
153	The two-pass separation offers no clear advantage over single-pass
154	enforcement; we adopt S1 as the primary configuration for its
155	simplicity and marginally stronger extraction performance.
156	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1318704-2e5b-45ec-bcd5-59c6a47d02ed",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "5d550bc5-51ab-4434-9045-8be27fecb517",
  "sourceToolAssistantUUID": "d1318704-2e5b-45ec-bcd5-59c6a47d02ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T21:27:20.070Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K4g3XL5f7N7bL6S2fv8KNg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d550bc5-51ab-4434-9045-8be27fecb517",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AoA7WrDSuG7Q7toNmV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7368528c-4468-45d3-a30b-80850dd3e5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RM5tnsngfJTLaXxDcpiVca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7460,
      "cache_read_input_tokens": 37420,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7460
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 37420,
          "cache_creation_input_tokens": 7460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7460,
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

_source line 37 · 2026-05-14T21:27:20.076Z_

<details><summary>↩ Tool result · `toolu_01K4g3XL5f7N7bL6S2fv8KNg`</summary>

```text
1	% Section 5 — DocRED Results (Draft)
2	% Data source: Phase 2 DocRED registry experiments (checker_version: fixed_20260514)
3	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
4	%          phase2_docred_semantic_only, phase2_docred_full_s1
5	% All numbers verified against registry 2026-05-14.
6	% F1 computed via all_set method with name→Wikidata PID normalization.
7	
8	\subsection{Cross-Dataset Validation on DocRED}
9	\label{sec:docred-results}
10	
11	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED,
12	a document-level relation extraction benchmark with 96 Wikidata relation
13	types---14$\times$ the ontology size of SciERC
14	(Section~\ref{sec:scierc-results}).
15	All experiments use Qwen3-8B in a zero-shot setting on 998 test documents
16	with identical prompts and decoding parameters.
17	Relation F1 is computed via name-to-Wikidata-PID normalization:
18	each predicted relation name is mapped to its canonical PID before
19	matching against gold annotations, and predictions that cannot be mapped
20	to any valid PID are counted as false positives.
21	
22	% ──────────────────────────────────────────
23	%  Table: DocRED four-way ablation
24	% ──────────────────────────────────────────
25	\begin{table}[t]
26	\centering
27	\small
28	\setlength{\tabcolsep}{3.6pt}
29	\begin{tabular}{@{}l rrrrr rr@{}}
30	\toprule
31	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
32	& \multicolumn{2}{c}{\textbf{F1}} \\
33	\cmidrule(lr){2-6} \cmidrule(l){7-8}
34	\textbf{Mode}
35	  & DR\,$\downarrow$ & $\Delta$DR
36	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
37	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
38	\midrule
39	Unconstrained
40	  & 18.46 & ---
41	  & 29.66 & 2.48
42	  & 0.10
43	  & 7.74  & 58.15 \\
44	Grammar
45	  & 26.17 & $\uparrow$42\%
46	  & \textbf{0.03} & \textbf{0}
47	  & 0.07
48	  & \textbf{8.31}  & \textbf{59.38} \\
49	Semantic
50	  & 13.84 & $\downarrow$25\%
51	  & 29.87 & 4.22
52	  & 1.05
53	  & 7.70  & 57.81 \\
54	Full (S1)
55	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
56	  & \textbf{0.03} & \textbf{0}
57	  & 2.57
58	  & 8.23  & 59.37 \\
59	\bottomrule
60	\end{tabular}
61	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
62	DR: domain/range violation rate;
63	RV: relation vocabulary violation rate;
64	ET: entity type violation rate;
65	CF: cross-field consistency violation rate.
66	$\Delta$DR: relative change vs.\ the unconstrained baseline
67	($\uparrow$: increase; $\downarrow$: decrease).
68	Best per column in \textbf{bold} (CF excluded---see text).
69	F1 scores are multiplied by 100.
70	Entity type violation rates reflect per-unique-entity counting (checker v2).
71	Statistical significance assessed via bootstrap resampling (10{,}000 iterations).}
72	\label{tab:docred-ablation}
73	\end{table}
74	
75	% ──────────────────────────────────────────
76	%  (a) Core result
77	% ──────────────────────────────────────────
78	\paragraph{Core result: DR halved with preserved or improved F1.}
79	The full two-layer configuration reduces domain/range violations from
80	18.46\% to 10.21\%, a 45\% relative reduction, while simultaneously
81	eliminating entity type violations (2.48\%\,$\to$\,0\%) and
82	near-eliminating relation vocabulary violations
83	(29.66\%\,$\to$\,0.03\%).
84	% phase2_docred_unconstrained: DR=0.1846, ET=0.0248, RV=0.2966
85	% phase2_docred_full_s1: DR=0.1021, ET=0, RV=0.0003
86	Relation F1 moves from 7.74 to 8.23 ($+$0.50\,pp; bootstrap 95\% CI [$+$0.23, $+$0.81]\,pp, $p < 0.001$, 10{,}000 iterations).
87	Entity F1 also improves significantly, from 58.15 to 59.37 ($+$1.23\,pp; bootstrap 95\% CI [$+$0.94, $+$1.55]\,pp, $p < 0.001$), driven entirely by the grammar layer's elimination of non-standard entity types (grammar-only Entity F1\,=\,59.38\%, indistinguishable from full S1's 59.37\%, $p = 0.66$).
88	% phase2_docred_unconstrained: R-F1=0.0774, E-F1=0.5815
89	% phase2_docred_full_s1: R-F1=0.0823, E-F1=0.5937
90	% bootstrap: delta=+0.50pp, CI=[+0.23,+0.81], p<0.001
91	% bootstrap: E-F1 delta=+1.23pp, CI=[+0.94,+1.55], p<0.001
92	% grammar_only E-F1=59.38 vs full_s1 E-F1=59.37, bootstrap p=0.66
93	The relation F1 improvement is statistically significant, attributable
94	to grammar-layer elimination of 5{,}189 out-of-vocabulary relation
95	predictions that are counted as false positives under the all-valid-set
96	protocol (Section~\ref{sec:discussion}).
97	Cross-field consistency violations increase modestly from 0.10\% to
98	2.57\%, substantially lower than the 9.90\% observed on SciERC;
99	% phase2_docred_unconstrained: CF=0.0010; phase2_docred_full_s1: CF=0.0257
100	we discuss this trade-off in Section~\ref{sec:discussion}.
101	
102	% ──────────────────────────────────────────
103	%  (b) Grammar layer
104	% ──────────────────────────────────────────
105	\paragraph{Grammar layer: structural guarantees generalize, but surface latent violations.}
106	Grammar-only constraints generalize to DocRED's 96-relation ontology,
107	eliminating entity type violations (2.48\%\,$\to$\,0\%) and
108	near-eliminating relation vocabulary violations
109	(29.66\%\,$\to$\,0.03\%).
110	% phase2_docred_grammar_only: ET=0, RV=0.0003
111	However, domain/range violations \emph{increase} from 18.46\% to
112	26.17\% (+42\% relative).
113	% phase2_docred_grammar_only: DR=0.2617
114	This counter-intuitive result has a structural explanation.
115	In the unconstrained baseline, 29.66\% of triples contain
116	out-of-vocabulary relation names and are classified as RV violations;
117	because no schema entry exists for an invalid relation name,
118	these triples \emph{cannot} be evaluated against domain/range rules
119	and are therefore absent from the DR count.
120	When grammar constraints force all relation names into the valid
121	vocabulary, these formerly RV-classified triples receive valid
122	relation names---but the associated entity types frequently violate
123	the domain/range rules of the assigned relation, surfacing as new
124	DR violations.
125	The grammar layer thus \emph{reveals} latent type incompatibilities
126	rather than creating them, directly motivating the semantic layer:
127	without domain/range enforcement, grammar alone makes the type
128	violation landscape worse, not better.
129	
130	% ──────────────────────────────────────────
131	%  (c) Enabling dependency
132	% ──────────────────────────────────────────
133	\paragraph{Enabling dependency confirmed across datasets.}
134	Semantic constraints alone reduce DR by 25\%
135	(18.46\%\,$\to$\,13.84\%) but cannot eliminate relation vocabulary
136	violations (RV\,=\,29.87\%) or entity type violations
137	(ET\,=\,4.22\%).
138	% phase2_docred_semantic_only: DR=0.1384, RV=0.2987, ET=0.0422
139	The elevated ET under semantic-only decoding (4.22\% vs.\ 2.48\%
140	unconstrained) reflects a genuine trajectory perturbation:
141	constrained logit masking shifts the generation distribution,
142	causing the model to produce more non-standard entity types
143	(e.g., \textsc{Work}, \textsc{Event}, \textsc{Ethnic\_Group})
144	that fall outside DocRED's canonical six-type vocabulary.
145	% Top non-standard types: WORK (823), EVENT (743), ETHNIC_GROUP (137)
146	We discuss this side effect in the limitations.
147	Combining both layers (Full S1) reduces DR a further 26\% relative to
148	the semantic-only configuration (13.84\%\,$\to$\,10.21\%),
149	% phase2_docred_full_s1: DR=0.1021; delta=(13.84-10.21)/13.84=0.262
150	replicating the enabling dependency observed on SciERC:
151	without grammar-enforced vocabulary constraints, the semantic layer
152	encounters out-of-vocabulary relation types for which no domain/range
153	rules exist, limiting its enforcement capacity.
154	The consistency of this pattern across two datasets with substantially
155	different ontology sizes (7 vs.\ 96 relation types) and violation
156	profiles (SciERC RV\,=\,1.39\% vs.\ DocRED RV\,=\,29.66\%) confirms
157	that the grammar$\to$semantic enabling dependency is a general
158	architectural property of the framework, not an artifact of a
159	particular schema.
160	
161	% ──────────────────────────────────────────
162	%  (d) Comparison with post-hoc filtering
163	% ──────────────────────────────────────────
164	\paragraph{Comparison with post-hoc filtering.}
165	An alternative to decoding-time constraint enforcement is post-hoc filtering:
166	generating triples without constraints and discarding those that violate
167	schema rules afterward.
168	% posthoc_report_docred: filtering applied to phase2_docred_unconstrained
169	On DocRED, post-hoc filtering removes 8{,}419 of 17{,}497 triples
170	(48.1\% rejection rate), including 5{,}189 out-of-vocabulary predictions,
171	692 entity type violations, and 2{,}538 domain/range violations.
172	% posthoc_docred: removed_rv=5189, removed_et=692, removed_dr=2538
173	This raises precision from 6.55\% to 11.22\% but reduces recall from
174	9.46\% to 8.40\%, as 127 gold-standard triples are discarded along with
175	the violations (relation F1: 7.74\,$\to$\,9.61).
176	% posthoc_docred: P_before=0.0655, P_after=0.1122, R_before=0.0946, R_after=0.0840
177	% posthoc_docred: F1_before=0.0774, F1_after=0.0961, tp_before=1137, tp_after=1010
178	On SciERC, the pattern is analogous: 16.8\% of triples are rejected, recall
179	drops from 11.40\% to 10.68\%, and 7 gold-standard triples are lost.
180	% posthoc_scierc: rejection_rate=0.1676, R_before=0.114, R_after=0.1068
181	% posthoc_scierc: tp_before=111, tp_after=104
182	OntoCoDec avoids this coverage--precision trade-off by guiding generation
183	toward schema-compliant triples rather than discarding non-compliant ones,
184	and operates as a single decoding pass without a separate filtering stage.
185	
186	% ──────────────────────────────────────────
187	%  (e) Constraint tightness scaling
188	% ──────────────────────────────────────────
189	\paragraph{Constraint tightness governs enforcement ceiling.}
190	The residual DR on DocRED (10.21\%) substantially exceeds that of
191	SciERC (0.93\%, Section~\ref{sec:scierc-results}).
192	This gap is explained by per-relation \emph{constraint tightness}:
193	DocRED relations admit on average only 5.68 valid entity type pairs
194	(mean tightness\,=\,0.842, i.e., 84.2\% of entity type pairs violate
195	domain/range rules), compared to 24 valid pairs on SciERC
196	(tightness\,=\,0.333).
197	% DocRED: avg_valid_pairs=5.68, avg_tightness=0.842
198	% SciERC: avg_valid_pairs=24, avg_tightness=0.333
199	With tighter per-relation constraints, the semantic layer's logit mask
200	eliminates a larger fraction of candidate tokens at each decoding step,
201	increasing the probability that the intersection of grammar and
202	semantic masks yields a narrow or empty candidate set.
203	In the limiting case, the system falls back to grammar-only constraints,
204	preserving structural validity but forgoing domain/range enforcement
205	for that token position.
206	For example, P1198 (\textsc{unemployment\_rate}) triggers fallback on
207	83\% of decoded triples due to its extremely tight constraint set,
208	while P171 (\textsc{parent\_taxon}) falls back at 78\%.
209	% docred_fallback: P1198=83%, P171=78% (tight constraints)
210	In contrast, relations with looser constraints such as P127
211	(\textsc{owned\_by}) and P170 (\textsc{creator}) exhibit 0\% fallback.
212	% docred_fallback: P127=0%, P170=0% (loose constraints)
213	The aggregate triple-level fallback rate (10.2\%; 1{,}770 of 17{,}341
214	triples) closely tracks the residual DR rate (10.21\%), confirming
215	that each residual violation corresponds to exactly one fallback event.
216	% docred_fallback: 1770/17341=10.2%; phase2_docred_full_s1: DR=0.1021
217	Conversely, SciERC's looser constraints leave more valid alternatives
218	for the model to redirect probability mass toward, enabling
219	near-complete DR elimination.
220	Among the factors governing residual DR, constraint tightness interacts
221	with the model's baseline violation profile.
222	Qwen3-8B's high relation vocabulary violation rate (RV\,=\,29.66\%)
223	means that grammar-layer enforcement surfaces numerous latent DR
224	violations when OOV relation names are forced into the valid vocabulary
225	(Section~\ref{sec:docred-results}, grammar paragraph), yielding
226	residual DR of 10.21\%.
227	Llama-3.1-8B's lower RV (16.03\%) limits this surfacing effect,
228	achieving residual DR of 2.55\%---a 90.2\% relative reduction on the
229	same ontology where Qwen achieves 44.7\%.
230	% Qwen DocRED: RV=0.2966, DR_full=0.1021, DR_reduction=44.7%
231	% Llama DocRED: RV=0.1603, DR_full=0.0255, DR_reduction=90.2%
232	Constraint tightness thus sets an upper bound on enforcement difficulty,
233	but the realized residual DR depends additionally on the fraction of
234	triples that receive valid relation names in the first place.
235	The grammar-only configuration achieves marginally higher relation F1
236	(8.31 vs.\ 8.23); this 0.08\,pp difference is not statistically
237	significant (bootstrap $p = 0.14$) and likely reflects minor
238	distributional shifts from semantic logit masking.
239	% grammar_only: R-F1=8.31; full_s1: R-F1=8.23; bootstrap p=0.14
240	This represents, to our knowledge, the first empirical characterization
241	of how ontology constraint properties modulate decoding-time enforcement
242	effectiveness; we develop this analysis further in
243	Section~\ref{sec:discussion}.
244	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7368528c-4468-45d3-a30b-80850dd3e5c1",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "34fe44e2-3034-4729-8ce6-6fa28243d5e5",
  "sourceToolAssistantUUID": "7368528c-4468-45d3-a30b-80850dd3e5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T21:27:24.999Z_

<details open><summary>🔧 Tool call — Read · `toolu_016vPQpfNhruxYXH5veN5xj6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34fe44e2-3034-4729-8ce6-6fa28243d5e5",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Aoe9Uxxi9cWgP3ybT3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f698141-92ba-4618-ba05-de3eb4fc2116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNpuunNFE5xHHYtRXoYMVU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9694,
      "cache_read_input_tokens": 44880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9694,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 39 · 2026-05-14T21:27:25.005Z_

<details><summary>↩ Tool result · `toolu_016vPQpfNhruxYXH5veN5xj6`</summary>

```text
1	% Section 5 — Cross-Model Validation (Draft)
2	% Data source: Phase 2 registry experiments, Qwen3-8B + Llama-3.1-8B
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
4	%          phase2_docred_unconstrained, phase2_docred_full_s1,
5	%          llama_scierc_unconstrained, llama_scierc_full_s1,
6	%          llama_docred_unconstrained, llama_docred_full_s1
7	% All numbers verified against registry 2026-05-14.
8	
9	\subsection{Cross-Model Validation}
10	\label{sec:cross-model}
11	
12	To verify that our constraint framework generalizes beyond a single LLM,
13	we replicate the full two-layer (S1) configuration with
14	Llama-3.1-8B-Instruct under identical prompts, decoding parameters,
15	and evaluation protocol.
16	Table~\ref{tab:cross-model} summarizes results alongside Qwen3-8B.
17	
18	% ──────────────────────────────────────────
19	%  Table: Cross-model comparison
20	% ──────────────────────────────────────────
21	\begin{table}[t]
22	\centering
23	\small
24	\setlength{\tabcolsep}{3.4pt}
25	\begin{tabular}{@{}ll rrrr rr@{}}
26	\toprule
27	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
28	& \multicolumn{2}{c}{\textbf{F1}} \\
29	\cmidrule(lr){3-6} \cmidrule(l){7-8}
30	\textbf{Dataset} & \textbf{Model}
31	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel. & Ent. \\
33	\midrule
34	\multirow{4}{*}{SciERC}
35	  & Qwen (U)  & 15.37 & 1.39 & 0.40 & 0.08 & 8.23 & 31.01 \\
36	  & Qwen (S1) &  0.93 & 0    & 0    & 9.90 & 8.36 & 30.98 \\
37	  \cmidrule(l){2-8}
38	  & Llama (U)  & 13.34 & 0.55 & 0    & 0.24 & 2.68 & 23.56 \\
39	  & Llama (S1) &  0.08 & 0    & 0    & 6.56 & 2.54 & 23.49 \\
40	% phase2_scierc_unconstrained: DR=0.1537, RV=0.0139, ET=0.0040, CF=0.0008, R-F1=0.0823, E-F1=0.3101
41	% phase2_scierc_full_s1: DR=0.0093, RV=0, ET=0, CF=0.0990, R-F1=0.0836, E-F1=0.3098
42	% llama_scierc_unconstrained: DR=0.1334, RV=0.0055, ET=0, CF=0.0024, R-F1=0.0268, E-F1=0.2356
43	% llama_scierc_full_s1: DR=0.0008, RV=0, ET=0, CF=0.0656, R-F1=0.0254, E-F1=0.2349
44	\midrule
45	\multirow{4}{*}{DocRED}
46	  & Qwen (U)  & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 & 58.15 \\
47	  & Qwen (S1) & 10.21 &  0.03 & 0    & 2.57 & 8.23 & 59.37 \\
48	  \cmidrule(l){2-8}
49	  & Llama (U)  & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 & 55.65 \\
50	  & Llama (S1) &  2.55 &  0    & 0    & 12.02 & 6.27 & 55.01 \\
51	% phase2_docred_unconstrained: DR=0.1846, RV=0.2966, ET=0.0248, CF=0.0010, R-F1=0.0774, E-F1=0.5815
52	% phase2_docred_full_s1: DR=0.1021, RV=0.0003, ET=0, CF=0.0257, R-F1=0.0823, E-F1=0.5937
53	% llama_docred_unconstrained: DR=0.2607, RV=0.1603, ET=0.0013, CF=0.0017, R-F1=0.0598, E-F1=0.5565
54	% llama_docred_full_s1: DR=0.0255, RV=0, ET=0, CF=0.1202, R-F1=0.0627, E-F1=0.5501
55	\bottomrule
56	\end{tabular}
57	\caption{Cross-model validation (Qwen3-8B vs.\ Llama-3.1-8B-Instruct).
58	U: unconstrained baseline; S1: full two-layer constraints.
59	DR/RV/ET/CF defined as in Table~\ref{tab:scierc-ablation}.
60	F1 scores are multiplied by 100.
61	Parse failures (U$\to$S1): Qwen SciERC 0$\to$0, Llama SciERC 1$\to$0,
62	Qwen DocRED 12$\to$11, Llama DocRED 68$\to$91.}
63	\label{tab:cross-model}
64	\end{table}
65	
66	% ──────────────────────────────────────────
67	%  (a) Grammar layer: model-agnostic
68	% ──────────────────────────────────────────
69	\paragraph{Grammar-layer guarantees are model-agnostic.}
70	RV and ET violations are eliminated or near-eliminated ($\leq$0.03\%)
71	under S1 for both models on both datasets.
72	% Qwen SciERC S1: RV=0, ET=0; Llama SciERC S1: RV=0, ET=0
73	% Qwen DocRED S1: RV=0.03%, ET=0; Llama DocRED S1: RV=0, ET=0
74	This confirms that the grammar layer's structural enforcement---relation
75	vocabulary restriction and entity type validation---operates on the
76	constrained decoding mechanism itself and does not depend on
77	model-specific generation patterns.
78	
79	% ──────────────────────────────────────────
80	%  (b) Semantic layer: DR reduction across models
81	% ──────────────────────────────────────────
82	\paragraph{Semantic-layer DR reduction generalizes across models.}
83	Domain/range violations decrease under S1 for both models on both
84	datasets:
85	SciERC DR drops 94\% for Qwen (15.37\%\,$\to$\,0.93\%) and
86	99.4\% for Llama (13.34\%\,$\to$\,0.08\%);
87	% Qwen: (15.37-0.93)/15.37=0.939; Llama: (13.34-0.08)/13.34=0.994
88	DocRED DR drops 45\% for Qwen (18.46\%\,$\to$\,10.21\%) and
89	90.2\% for Llama (26.07\%\,$\to$\,2.55\%).
90	% Qwen: (18.46-10.21)/18.46=0.447; Llama: (26.07-2.55)/26.07=0.902
91	In both cases, relation F1 is preserved or marginally improves
92	(Qwen R-F1: +0.13/+0.50\,pp; Llama R-F1: $-$0.14/+0.29\,pp),
93	% phase2_scierc: Qwen 8.23→8.36; Llama 2.68→2.54
94	% phase2_docred: Qwen 7.74→8.23; Llama 5.98→6.27
95	indicating that constraint enforcement redirects probability mass
96	toward schema-compliant outputs without degrading extraction quality.
97	Entity F1 is preserved or improved for Qwen3-8B ($-$0.03/$+$1.22\,pp)
98	but shows a minor decline for Llama-3.1-8B on DocRED ($-$0.64\,pp),
99	attributable in part to increased parse failures
100	(68\,$\to$\,91) under constrained decoding.
101	% llama_docred_unconstrained: E-F1=55.65, parse_fail=68
102	% llama_docred_full_s1: E-F1=55.01, parse_fail=91
103	
104	% ──────────────────────────────────────────
105	%  (c) Llama vs Qwen DR reduction asymmetry
106	% ──────────────────────────────────────────
107	\paragraph{Llama achieves higher DR reduction than Qwen.}
108	Llama's relative DR reduction exceeds Qwen's on both datasets
109	(SciERC: 99.4\% vs.\ 94\%; DocRED: 90.2\% vs.\ 45\%).
110	This asymmetry reflects the interaction between constraint tightness
111	and model-specific violation profiles: Qwen's higher baseline RV
112	(29.66\% vs.\ 16.03\%) causes grammar-layer enforcement to surface
113	more latent DR violations, raising residual DR despite identical
114	ontology constraints (see tightness paragraph,
115	Section~\ref{sec:docred-results}).
116	% Qwen DocRED: RV=0.2966, DR_full=0.1021, DR_reduction=44.7%
117	% Llama DocRED: RV=0.1603, DR_full=0.0255, DR_reduction=90.2%
118	Notably, Llama's absolute IE quality is lower than Qwen's
119	(R-F1 $\approx$ 2.5--6.3 vs.\ 8.2--8.4; E-F1 lower by 2--8\,pp),
120	but this does not diminish the validity of the compliance comparison:
121	constraint enforcement is evaluated on the model's own output
122	distribution, and the consistent violation reduction pattern across
123	two models with different capability levels strengthens the
124	model-agnostic claim.
125	
126	% ──────────────────────────────────────────
127	%  (d) CF trade-off
128	% ──────────────────────────────────────────
129	\paragraph{CF trade-off persists across models.}
130	Cross-field consistency violations increase under S1 for both models
131	(Qwen: 0.08\%\,$\to$\,9.90\% on SciERC, 0.10\%\,$\to$\,2.57\% on
132	DocRED; Llama: 0.24\%\,$\to$\,6.56\% on SciERC,
133	0.17\%\,$\to$\,12.02\% on DocRED).
134	% phase2_scierc: Qwen CF 0.08→9.90; Llama CF 0.24→6.56
135	% phase2_docred: Qwen CF 0.10→2.57; Llama CF 0.17→12.02
136	Llama exhibits the highest CF rate (12.02\% on DocRED), consistent with
137	its lower baseline generation quality producing more cases where
138	constrained field corrections create inter-field inconsistencies.
139	This cross-model pattern confirms that CF elevation is a systematic
140	property of the current constraint architecture rather than a
141	model-specific artifact, motivating a joint cross-field enforcement
142	mechanism as future work (Section~\ref{sec:discussion}).
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f698141-92ba-4618-ba05-de3eb4fc2116",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "b82c0270-63a9-4b53-9e7d-6bd0c66ccdd2",
  "sourceToolAssistantUUID": "2f698141-92ba-4618-ba05-de3eb4fc2116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T21:27:25.954Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SuviAWDHKLPRja6Rhfos3j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b82c0270-63a9-4b53-9e7d-6bd0c66ccdd2",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Aoe9Uxxi9cWgP3ybT3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dcaf883-5cd6-4a8b-baec-09e112fac9fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNpuunNFE5xHHYtRXoYMVU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9694,
      "cache_read_input_tokens": 44880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9694,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 41 · 2026-05-14T21:27:25.966Z_

<details><summary>↩ Tool result · `toolu_01SuviAWDHKLPRja6Rhfos3j`</summary>

```text
1	% Discussion paragraphs for §7
2	% Three standalone paragraphs: (1) Low F1 practical significance,
3	% (2) CF severity argument, (3) F1 significance difference explanation.
4	% All quantitative claims traced to registry exp_ids.
5	
6	%%% Paragraph 1: Low F1 Practical Significance %%%
7	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
8	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
9	
10	\paragraph{Practical Significance of Zero-Shot F1.}
11	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
12	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
13	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
14	When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
15	% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
16	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
17	The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
18	
19	%%% Paragraph 2: CF Severity Argument %%%
20	% exp_ids: phase2_scierc_full_s1 (CF=9.90%), phase2_scierc_grammar_only (CF=0.08%),
21	%          phase2_docred_full_s1 (CF=2.57%)
22	
23	\paragraph{Severity of Cross-Field Violations.}
24	Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
25	DR violations are therefore hard constraints.
26	Cross-field consistency (CF) violations are qualitatively different: each individual triple remains type-valid with respect to its own relation's domain/range rules; only cross-triple consistency is broken when the same entity receives different types across relations.
27	The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245~affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
28	% exp_id: phase2_scierc_full_s1
29	Ablation evidence cleanly attributes CF to the semantic layer: grammar-only decoding yields CF\,=\,0.08\%, matching the unconstrained baseline, while the full system reaches 9.90\% on SciERC and 2.57\% on DocRED
30	(Qwen3-8B; Llama-3.1-8B exhibits 12.02\% on DocRED, the highest across all configurations).
31	% exp_ids: phase2_scierc_grammar_only, phase2_docred_full_s1
32	% llama_docred_full_s1: CF=0.1202
33	This arises from per-relation independent enforcement, where each relation's constraint mask is computed without access to type decisions made for other relations.
34	A natural extension is a global entity-level type consensus pass that resolves entity types before relation-specific enforcement.
35	
36	%%% Paragraph 3: F1 Significance Difference Explanation %%%
37	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
38	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
39	
40	\paragraph{Dataset-Dependent F1 Impact.}
41	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$, 95\% CI [$+$0.23, $+$0.81]) and SciERC ($+$0.13\,pp, $p = 0.58$, 95\% CI [$-$0.24, $+$0.58]) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary (OOV) relation names.
42	% exp_id: d012_bootstrap_ci
43	Under the all-valid-set evaluation protocol, a predicted triple whose relation name does not appear in the ontology is counted as a false positive.
44	The DocRED baseline exhibits a relation-vocabulary (RV) violation rate of 29.66\%---5{,}189 predictions with OOV relation names---all of which become false positives under this protocol.
45	% exp_id: phase0_docred_unconstrained
46	The grammar layer eliminates these OOV predictions, removing a substantial source of false positives and yielding a statistically significant precision gain.
47	On SciERC, the baseline RV rate is only 1.39\% (24~OOV predictions), too few to produce a detectable F1 effect.
48	% exp_id: phase0_scierc_unconstrained
49	The F1 improvement on DocRED is thus a direct, mechanistically transparent consequence of vocabulary enforcement at scale, not an artifact of constraint-induced distribution shift.
50	Llama-3.1-8B's lower baseline RV (16.03\% vs.\ Qwen's 29.66\%)
51	results in fewer OOV predictions eliminated by the grammar layer,
52	yielding a smaller but directionally consistent R-F1 improvement
53	($+$0.29\,pp vs.\ $+$0.50\,pp), confirming that the magnitude of
54	F1 gain is proportional to the baseline OOV rate.
55	% llama_docred_unconstrained: RV=0.1603, R-F1=5.98
56	% llama_docred_full_s1: RV=0, R-F1=6.27, delta=+0.29pp
57	% qwen_docred: RV=0.2966, R-F1 delta=+0.50pp
58	
59	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
60	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
61	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
62	
63	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
64	Post-hoc filtering---generating triples without constraints, then removing schema-violating predictions---yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
65	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
66	However, this precision gain comes at substantial cost.
67	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions), reducing recall from 9.46\% to 8.40\%.
68	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
69	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
70	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
71	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
72	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dcaf883-5cd6-4a8b-baec-09e112fac9fe",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "53197e39-7de1-4c41-80ae-fbf8e6515568",
  "sourceToolAssistantUUID": "2dcaf883-5cd6-4a8b-baec-09e112fac9fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T21:27:26.310Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UGAdDGVwfLR5h78Wh2HMNM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53197e39-7de1-4c41-80ae-fbf8e6515568",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Aoe9Uxxi9cWgP3ybT3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c0f06fd-721f-4cdc-ba86-df680e48f791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNpuunNFE5xHHYtRXoYMVU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9694,
      "cache_read_input_tokens": 44880,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 44880,
          "cache_creation_input_tokens": 9694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9694,
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

_source line 43 · 2026-05-14T21:27:26.316Z_

<details><summary>↩ Tool result · `toolu_01UGAdDGVwfLR5h78Wh2HMNM`</summary>

```text
1	% Section 7 — Conclusion
2	% Data source: Phase 2 SciERC registry experiments + Phase 0 DocRED
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
4	%          phase0_scierc_unconstrained, phase0_docred_unconstrained
5	% All numbers verified against registry 2026-05-14.
6	
7	We presented OntoCoDec, a framework that automatically compiles IE ontology schemas into token-level decoding constraints to enforce type validity at generation time.
8	Our work makes three contributions.
9	
10	First, we conducted the first systematic study of ontological constraint violations in LLM-based IE (\S\ref{sec:violation_landscape}).
11	Across two benchmarks with substantially different ontology sizes---SciERC (7~relations) and DocRED (96~relations)---we found that domain/range violation rates are comparable (15.37\% vs.\ 18.46\%), % exp_ids: phase0_scierc_unconstrained, phase0_docred_unconstrained
12	indicating that violation severity is driven by \emph{constraint tightness} $\bar{\tau}$ rather than ontology scale.
13	SciERC ($\bar{\tau}{=}0.333$, mean 24 valid type pairs per relation) and DocRED ($\bar{\tau}{=}0.842$, mean 5.68) exhibit comparable violation rates despite a 14$\times$ difference in ontology size, and within each model, DR reduction scales inversely with $\bar{\tau}$: 94--99\% on SciERC ($\bar{\tau}{=}0.333$) vs.\ 45--90\% on DocRED ($\bar{\tau}{=}0.842$), with the residual modulated by model-specific baseline violation rates (Section~\ref{sec:cross-model}).
14	% Qwen: SciERC DR↓94%, DocRED DR↓45%; Llama: SciERC DR↓99%, DocRED DR↓90%
15	
16	Second, we introduced a two-layer constraint architecture that decomposes ontological enforcement into complementary mechanisms:
17	a \emph{grammar layer} (XGrammar CFG) that eliminates structural violations (RV, ET\,$\to$\,0\%) and a \emph{semantic layer} (TypeConstraintProcessor with a stateful entity registry) that enforces domain/range constraints at the token level. % exp_id: phase2_scierc_grammar_only
18	The grammar layer serves as an enabling prerequisite for the semantic layer; the two compose via bitwise AND over candidate token sets.
19	
20	Third, we validated OntoCoDec empirically.
21	On SciERC, the full system reduces domain/range violations from 15.37\% to 0.93\%---a 94\% relative reduction---while completely eliminating RV and ET violations, with no significant impact on relation F1 ($+$0.13 percentage points, $p > 0.05$). % exp_id: phase2_scierc_full_s1
22	On DocRED, the full system reduces domain/range violations from 18.46\% to 10.21\%---a 45\% relative reduction---while eliminating RV and ET violations entirely, with statistically significant gains in relation F1 ($+$0.50pp, $p{<}0.001$) and entity F1 ($+$1.23pp, $p{<}0.001$) for Qwen3-8B. Llama-3.1-8B achieves substantial DR reduction (90.2\%, 26.07\%\,$\to$\,2.55\%) with F1-neutral impact. % exp_ids: phase2_docred_full, llama_docred_full_s1, llama_docred_unconstrained
23	Compared with post-hoc filtering, decoding-time enforcement preserves true positives and eliminates entity-type violations that post-hoc methods cannot address.
24	
25	\paragraph{Limitations.}\label{sec:limitations}
26	Several limitations qualify these findings.
27	The semantic layer introduces cross-field consistency (CF) violations: CF rises from 0.08\% under unconstrained decoding to 9.90\% with full constraints. % exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1
28	This is a systematic consequence of per-relation independent type enforcement---when the same entity appears across multiple triples, each relation's domain/range constraint may assign it a different type, producing entity-versus-relation type drift.
29	The grammar layer alone does not elevate CF (0.08\%, matching the unconstrained baseline), confirming that CF is entirely attributable to the semantic layer. % exp_id: phase2_scierc_grammar_only
30	Resolving this cross-relation type coherence problem is an open challenge, not a trivial implementation fix.
31	Cross-field consistency violations increase with constraint strength and vary across models: CF reaches 12.02\% for Llama-3.1-8B on DocRED under full constraints, compared with 2.57\% for Qwen3-8B on the same dataset, suggesting that per-relation independent enforcement interacts with model-specific generation patterns. % exp_ids: llama_docred_full_s1, phase2_docred_full
32	Constrained decoding can increase parse failure rates for some model-dataset combinations: Llama-3.1-8B on DocRED shows 91 parse failures under full constraints versus 68 unconstrained (9.1\% vs.\ 6.8\%), likely due to max-token truncation of longer constrained outputs. All F1 metrics are computed over successfully parsed documents only. % exp_ids: llama_docred_full_s1, llama_docred_unconstrained
33	Beyond CF, experiments use two models (Qwen3-8B and Llama-3.1-8B-Instruct), confirming that constraint enforcement generalizes across model families: Llama-3.1-8B on DocRED achieves a 90.2\% DR reduction (26.07\%\,$\to$\,2.55\%) without any code modification.
34	% llama_docred_unconstrained: DR=26.07%; llama_docred_full_s1: DR=2.55%
35	Results are reported for two models and two datasets under zero-shot prompting only, and integration with fine-tuned models has not been explored.
36	
37	\paragraph{Future Work.}
38	We identify four directions.
39	(1)~Extension to larger models (quantized 70B-class) to further verify model-agnostic generalization across scales.
40	(2)~Global entity-level type consensus during decoding---maintaining a shared entity registry across all relations within an instance---to resolve CF violations.
41	(3)~Integration with fine-tuned models, combining constraint-aware training objectives with decoding-time enforcement.
42	(4)~Extension to non-English ontologies to evaluate cross-lingual applicability.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c0f06fd-721f-4cdc-ba86-df680e48f791",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "02518a57-c0ee-4a4a-945f-fc59b4b2c73f",
  "sourceToolAssistantUUID": "2c0f06fd-721f-4cdc-ba86-df680e48f791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T21:27:29.413Z_

Now let me read the bibliography and the appendix related work to check reference coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02518a57-c0ee-4a4a-945f-fc59b4b2c73f",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Ap7HPAuVcLQTnfGrBu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0e56c72-56b5-4723-93f8-92bf6a0215c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9ru88FMPpjwEiRs94VuB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7773,
      "cache_read_input_tokens": 54574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7773,
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

_source line 45 · 2026-05-14T21:27:31.278Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cf4N4HK5AeeYuh1HiESv82`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e56c72-56b5-4723-93f8-92bf6a0215c4",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Ap7HPAuVcLQTnfGrBu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4178b3e4-cf3b-4aa3-962a-00a72ccb2733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9ru88FMPpjwEiRs94VuB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7773,
      "cache_read_input_tokens": 54574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7773,
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

_source line 46 · 2026-05-14T21:27:31.284Z_

<details><summary>↩ Tool result · `toolu_01Cf4N4HK5AeeYuh1HiESv82`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for structured generation.
15	However, all of these methods operate exclusively at the syntactic level---they ensure format validity (e.g., well-formed JSON, valid enum values) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.
16	This syntactic-only limitation motivates OntoCoDec's semantic extension: our grammar layer builds on XGrammar for structural (JSON schema and enum) constraints, while a second semantic layer enforces relational type constraints that are inherently beyond the expressive power of context-free grammars.
17	
18	% ===========================================================================
19	% Paradigm 1.5: Semantic Constrained Decoding for Code
20	% ===========================================================================
21	\paragraph{Semantic Constrained Decoding for Code.}
22	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness, demonstrating that richer-than-CFG constraints can be compiled into token-level filtering.
23	In the text-to-SQL domain, PICARD~\cite{scholak2021picard} maintains an incremental SQL parsing state that rejects tokens violating syntax or referencing non-existent database columns at each decoding step, achieving state-of-the-art results on Spider and CoSQL without modifying model weights.
24	While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema---database table and column names known before decoding begins.
25	In contrast, OntoCoDec's entity registry is populated \emph{during} generation as entity spans are extracted from free text, requiring constraint sets that evolve with the decoding prefix---a fundamental distinction between querying a known schema and extracting from unstructured text.
26	Synchromesh~\cite{synchromesh_iclr2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs without fine-tuning, establishing that semantic constraints can be expressed as dynamic token masks conditioned on the generation prefix.
27	MGD~\cite{mgd_neurips2023} uses static-analysis monitors to perform incremental type checking at decode time, enabling SantaCoder-1.1B to outperform text-davinci-003 on repository-level code completion by ensuring that every generated identifier is type-correct with respect to the surrounding code context.
28	Most recently, \citet{pldi2025_type_constrained_codegen} compile full type systems---including generic types and subtyping---into prefix automata for token-level logits masking, reducing compilation errors by over 50\%.
29	This last system is the closest mechanistic analog to OntoCoDec, applying the same ``type system $\to$ automaton $\to$ logits mask'' pipeline, though in a fundamentally different domain.
30	The key technical difference lies in the constraint structure: programming-language type systems feature deep subtyping hierarchies and parametric polymorphism, whereas IE ontology axioms specify flat domain/range sets---a relation $R$ accepts head entities from set $\mathcal{D}(R)$ and tail entities from set $\mathcal{R}(R)$, with no subtype chains.
31	Conversely, IE introduces a challenge absent in code generation: the constraint target (entity type) must be inferred from free-text spans rather than read from declared type annotations, requiring a stateful entity registry that tracks extracted types during autoregressive generation.
32	These methods collectively demonstrate that semantic (type) constraints at decode time are both feasible and highly effective, but exclusively in the code domain where type systems are formally specified.
33	OntoCoDec is the first to \emph{automatically compile} IE ontology axioms---including domain/range constraints---into token-level decoding masks for information extraction, migrating the type-constrained decoding paradigm from code generation to IE.
34	
35	% ===========================================================================
36	% Paradigm 2: Vocabulary/Type-Constrained Generation
37	% ===========================================================================
38	\paragraph{Vocabulary and Type-Constrained Generation.}
39	The idea of enforcing entity-type compatibility constraints for information extraction dates back to pre-neural methods.
40	\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints---e.g., \textsc{Emp-Org} only between \textsc{Per} and \textsc{Org} entities---establishing the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.
41	In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, restricting each decoding step to tokens consistent with valid entity names from a predefined catalog.
42	GenIE~\cite{josifoski2022genie} extends this approach to end-to-end information extraction with state-based constraints that enforce valid triple structures, achieving strong performance on closed-world knowledge base population, though it requires task-specific fine-tuning on the target schema.
43	AdaKGC~\cite{adakgc_emnlp2023} introduces schema-constrained dynamic decoding with trie-based prefix trees that adapt to the target schema, enforcing that generated entity and relation names belong to a predefined inventory---a vocabulary-level constraint that ensures name validity but does not verify type compatibility between a relation and its arguments.
44	GCD~\cite{geng2023gcd} provides a unified grammar-constrained decoding framework for structured NLP tasks including IE, introducing input-dependent grammars that adapt constraints based on the source text---the closest precursor to OntoCoDec in applying logits masking to IE, though limited to syntactic constraints.
45	NeuroLogic Decoding~\cite{lu2021neurologic} expresses lexical inclusion and exclusion constraints as predicate logic formulas enforced during beam search, offering a general mechanism for token-level control that can encode vocabulary membership but not relational type rules.
46	These approaches constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation.
47	OntoCoDec's semantic layer enforces relational constraints---e.g., that the head entity of relation $R$ must belong to type set $\mathcal{D}(R)$---which cannot be expressed as static vocabulary restrictions because the valid set depends on the relation type generated earlier in the same sequence.
48	While Roth \& Yih's ILP formulation shares the same type-compatibility motivation, it operates as a post-hoc reranker over discrete candidates; OntoCoDec integrates enforcement directly into autoregressive decoding, preventing violations rather than filtering them.
49	
50	% ===========================================================================
51	% Paradigm 3: Structural Constraints for IE
52	% ===========================================================================
53	\paragraph{Structural Constraints via Training and Prompting.}
54	An orthogonal approach encodes IE output structure through model training or prompt design rather than decoding-time enforcement, relying on learned representations to produce schema-compliant outputs.
55	UIE~\cite{lu2022uie} defines a Structured Extraction Language and trains a unified text-to-structure model across 13 IE datasets, relying on large-scale pre-training to internalize output format constraints.
56	GoLLIE~\cite{sainz2024gollie} expresses annotation guidelines as Python dataclass definitions and fine-tunes Code-LLaMA to generate typed code, achieving strong zero-shot transfer to unseen IE schemas by leveraging the implicit type structure of programming languages.
57	KnowCoder~\cite{knowcoder_acl2024} takes this further by encoding 29K entity types from Wikidata as a Python class hierarchy, training a Code-LLM to generate structured extraction code that implicitly respects type inheritance---the most comprehensive schema-as-code approach to date.
58	CodeIE~\cite{li2023codeie} similarly reformulates IE as code generation, leveraging the structural regularity of programming languages to reduce output format errors.
59	ADELIE~\cite{qi2024adelie} uses SFT and DPO to align LLMs on IE tasks, achieving state-of-the-art results among open-source models while preserving general capabilities, though compliance with ontological constraints remains a learned soft preference rather than a guarantee.
60	In the supervised setting, joint entity-relation architectures such as SpERT~\cite{eberts2020spert} and PFN~\cite{yan2021pfn} enforce type consistency implicitly through shared representations: SpERT classifies entity spans and relation pairs in a single BERT pass with span-level negative sampling, while PFN decomposes feature encoding into entity-specific, relation-specific, and shared partitions via gating mechanisms.
61	These models achieve strong performance but are limited to fixed, predefined schemas and cannot generalize to unseen ontologies without retraining---precisely the zero-shot, ontology-portable scenario that OntoCoDec targets.
62	EnriCo~\cite{zaratiana2024enrico} applies Answer Set Programming (ASP) constraints during decoding of joint entity-relation extraction models, enforcing structural type compatibility at generation time---a decoding-time approach, though with model-specific, manually authored constraints rather than ontology-driven compilation.
63	Training-based methods provide \emph{soft} structural guidance---the model learns to prefer valid outputs but cannot guarantee compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.
64	Importantly, training-based and decoding-time approaches are complementary rather than competing: a system like GoLLIE could be combined with OntoCoDec's constraint layers, using fine-tuning to maximize the probability of valid outputs while decoding-time enforcement eliminates residual violations.
65	OntoCoDec provides \emph{hard} decoding-time enforcement that is training-free, automatically compiled from ontology schemas, and composable with any of these training-based approaches.
66	
67	% ===========================================================================
68	% Paradigm 4: Type-Checking / Ontology Validation
69	% ===========================================================================
70	\paragraph{Post-hoc Ontology Validation.}
71	Rather than constraining generation, several methods validate LLM outputs against ontological rules after generation, applying a detect-then-fix paradigm.
72	ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale---but constraint adherence relies on prompt-level guidance, not enforcement, leaving residual violations unaddressed.
73	SPIRES/OntoGPT~\cite{spires_2024} provides an ontology-based extraction framework that grounds LLM outputs against OBO ontologies post-generation, validating extracted entities and relations through ontology lookup and correcting mismatches in a second pass---representing the prompt-then-validate paradigm in the biomedical domain.
74	OntoLogX~\cite{ontologx_2025} applies SHACL validation to LLM-generated knowledge graphs, iteratively re-prompting the LLM to correct constraint violations and reducing them by approximately 10$\times$ across multiple correction rounds---demonstrating the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
75	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB, though their constrained inference operates over a discrete candidate set rather than during autoregressive generation.
76	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating RDF triple insertions against RDFS domain/range constraints, where each validation step requires a separate LLM call---effective but computationally expensive at scale.
77	RELATE~\cite{olasunkanmi2025relate} addresses the alignment gap between LLM-extracted biomedical relations and standardized ontology predicates through a three-stage pipeline: ontology preprocessing with predicate embeddings, similarity-based retrieval via SapBERT, and LLM-based reranking with negation handling, achieving 94\% accuracy@10 on ChemProt.
78	While RELATE demonstrates effective ontology grounding for relation extraction, its constraints are applied \emph{post-extraction} through retrieval and reranking rather than during generation, and it requires domain-specific embedding models trained on biomedical corpora.
79	OntoCoDec enforces ontology constraints \emph{during} autoregressive decoding and requires no additional trained components beyond the base LLM.
80	Concurrently, \citet{zhou2026ontologytools} compile OWL ontologies into executable tool interfaces within The World Avatar framework, requiring LLM agents to invoke ontology-aware tools that enforce semantic constraints during knowledge graph construction from scientific text.
81	This ``ontology-to-tools'' approach shares OntoCoDec's philosophy of compiling formal ontological knowledge into runtime enforcement mechanisms, but operates at the tool-call level (constraining which API functions the agent invokes) rather than at the token level (constraining which tokens the decoder produces), and requires an agentic multi-step workflow rather than single-pass autoregressive generation.
82	\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms---a middle ground between unconstrained generation and hard enforcement that reduces but cannot eliminate violations.
83	Post-hoc validation detects violations after generation, requiring rejection or correction cycles that waste compute---in our setting, 15.37\% of generated triples contain domain/range violations under unconstrained decoding, representing substantial wasted generation effort.
84	OntoCoDec \emph{prevents} violations during decoding, redirecting probability mass to valid alternatives rather than discarding invalid outputs, with only marginal overhead from logits masking compared to the cost of regenerating or correcting violated triples.
85	Soft-constraint approaches such as ontology-weighted beam scoring reduce violation frequency but cannot eliminate it, whereas OntoCoDec achieves near-complete to substantial elimination (DR$\downarrow$94\% on SciERC, $\downarrow$45\% on DocRED).
86	
87	% ===========================================================================
88	% Paradigm 5: Constrained Decoding Quality Concerns
89	% ===========================================================================
90	\paragraph{Quality Impact of Constrained Decoding.}
91	A growing body of work raises concerns that constrained decoding degrades LLM generation quality, particularly for reasoning-intensive tasks where format enforcement interferes with chain-of-thought processes.
92	\citet{tam2024letmespeak} conduct a comprehensive evaluation showing that rigid format constraints (JSON, XML) harm performance on math and multi-hop QA benchmarks but \emph{benefit} classification-style tasks such as slot filling---a distinction directly relevant to IE, which is fundamentally an extraction (classification-like) task rather than a reasoning task.
93	CRANE~\cite{banerjee2025crane} provides theoretical analysis of why restricting outputs to narrow grammars suppresses chain-of-thought reasoning by eliminating intermediate reasoning tokens, and proposes an alternating strategy between unconstrained reasoning phases and constrained output phases to mitigate this effect.
94	\citet{schall2025hiddencost} conduct a systematic study across 11 models and multiple benchmarks, finding 10--30\% semantic correctness degradation on reasoning tasks under structural constraints, with larger models showing greater absolute degradation.
95	\citet{zhou2026snowballing} identify ``structure snowballing''---a failure mode where format compliance cognitive load traps models in repetitive structural patterns rather than improving reasoning during self-correction iterations.
96	These findings establish a legitimate concern for constrained decoding in reasoning-heavy applications.
97	However, information extraction occupies a fundamentally different regime: the model extracts entities and relations from input text rather than generating novel reasoning chains, and \citet{tam2024letmespeak}'s own results show that extraction-style tasks are robust to---or even benefit from---format constraints.
98	OntoCoDec addresses this concern empirically: domain/range violations decrease by 94\% on SciERC (15.37\%$\to$0.93\%) and 45\% on DocRED, with \emph{zero} F1 degradation on SciERC (R-F1 8.36\% vs.\ 8.23\% unconstrained, $+$0.13pp, not statistically significant).
99	Critically, OntoCoDec's constraints target only type tokens (entity types, relation labels), leaving free-text spans---entity surface forms and their boundaries---entirely unconstrained, which minimizes the distribution distortion that causes quality degradation in reasoning tasks.
100	A two-pass variant (S2), explored in ablation (Section~5), separates extraction and constraint enforcement into distinct passes, analogous to CRANE's alternating strategy; however, our primary single-pass approach already avoids reasoning interference by constraining only type tokens while leaving free-text spans unconstrained.
101	
102	% ===========================================================================
103	% Our Approach
104	% ===========================================================================
105	\paragraph{Our Approach.}
106	OntoCoDec occupies a unique position in this landscape: it is the first system to \emph{automatically compile} IE ontology schemas---including domain/range axioms---into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement without manually authored rules.
107	Unlike vocabulary-constrained methods that restrict individual tokens to a fixed set, OntoCoDec enforces \emph{cross-field relational constraints} through a stateful entity registry that tracks extracted types during autoregressive generation, enabling dynamic constraint evaluation that depends on previously decoded content.
108	This approach is orthogonal to supervised IE methods and applicable to any autoregressive LM without model modification or additional training.
109	Unlike training-based IE systems, OntoCoDec is training-free and achieves near-complete to substantial elimination of type violations at inference time (DR$\downarrow$94\% on SciERC, $\downarrow$45\% on DocRED); unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives with zero quality cost on SciERC (R-F1 8.36\% vs.\ 8.23\% unconstrained).
110	The two constraint layers---grammar (structural) and semantic (relational)---compose via bitwise AND with an enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4178b3e4-cf3b-4aa3-962a-00a72ccb2733",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "b9e6a594-8cda-4acd-bef8-a007ca56eea9",
  "sourceToolAssistantUUID": "4178b3e4-cf3b-4aa3-962a-00a72ccb2733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T21:27:32.250Z_

<details open><summary>🔧 Tool call — Read · `toolu_0159UfSipymiSsayMzKRLN8E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9e6a594-8cda-4acd-bef8-a007ca56eea9",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Ap7HPAuVcLQTnfGrBu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf1d1223-f56d-4fd6-91fd-596d5a39e007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9ru88FMPpjwEiRs94VuB7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7773,
      "cache_read_input_tokens": 54574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7773,
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

_source line 48 · 2026-05-14T21:27:32.258Z_

<details><summary>↩ Tool result · `toolu_0159UfSipymiSsayMzKRLN8E`</summary>

```text
1	% ============================================================
2	% Related Work Additions — compiled 2026-05-14
3	% Each block specifies its insertion point in section6_related_work.tex
4	% All citations verified via WebSearch (authors, venue, year confirmed)
5	% ============================================================
6	
7	
8	% ============================================================
9	% 1. PICARD
10	% INSERT INTO "Semantic Constrained Decoding for Code" paragraph
11	% AFTER: "...demonstrating that richer-than-CFG constraints can be
12	%         compiled into token-level filtering."  (end of line 22)
13	% BEFORE: "Synchromesh~\cite{synchromesh_iclr2022}..." (line 23)
14	% ============================================================
15	
16	In the text-to-SQL domain, PICARD~\cite{scholak2021picard} maintains an incremental SQL parsing state that rejects tokens violating syntax or referencing non-existent database columns at each decoding step, achieving state-of-the-art results on Spider and CoSQL without modifying model weights.
17	While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema---database table and column names known before decoding begins.
18	In contrast, OntoCoDec's entity registry is populated \emph{during} generation as entity spans are extracted from free text, requiring constraint sets that evolve with the decoding prefix---a fundamental distinction between querying a known schema and extracting from unstructured text.
19	
20	
21	% ============================================================
22	% 2. Joint Entity-Relation Models (SpERT, PFN)
23	% INSERT INTO "Structural Constraints via Training and Prompting" paragraph
24	% AFTER: "...though compliance with ontological constraints remains a
25	%         learned soft preference rather than a guarantee." (end of line 56,
26	%         after ADELIE sentence)
27	% BEFORE: "EnriCo~\cite{zaratiana2024enrico}..." (line 57)
28	% ============================================================
29	
30	In the supervised setting, joint entity-relation architectures such as SpERT~\cite{eberts2020spert} and PFN~\cite{yan2021pfn} enforce type consistency implicitly through shared representations: SpERT classifies entity spans and relation pairs in a single BERT pass with span-level negative sampling, while PFN decomposes feature encoding into entity-specific, relation-specific, and shared partitions via gating mechanisms.
31	These models achieve strong performance but are limited to fixed, predefined schemas and cannot generalize to unseen ontologies without retraining---precisely the zero-shot, ontology-portable scenario that OntoCoDec targets.
32	
33	
34	% ============================================================
35	% 3. RELATE
36	% INSERT INTO "Post-hoc Ontology Validation" paragraph
37	% AFTER: "...effective but computationally expensive at scale."
38	%        (end of line 71, after \citet{regino2025kgcurator} sentence)
39	% BEFORE: "\citet{ekaw2024_ontology_beam}..." (line 72)
40	% ============================================================
41	
42	RELATE~\cite{olasunkanmi2025relate} addresses the alignment gap between LLM-extracted biomedical relations and standardized ontology predicates through a three-stage pipeline: ontology preprocessing with predicate embeddings, similarity-based retrieval via SapBERT, and LLM-based reranking with negation handling, achieving 94\% accuracy@10 on ChemProt.
43	While RELATE demonstrates effective ontology grounding for relation extraction, its constraints are applied \emph{post-extraction} through retrieval and reranking rather than during generation, and it requires domain-specific embedding models trained on biomedical corpora.
44	OntoCoDec enforces ontology constraints \emph{during} autoregressive decoding and requires no additional trained components beyond the base LLM.
45	
46	
47	% ============================================================
48	% 4. Ontology-to-Tools
49	% INSERT INTO "Post-hoc Ontology Validation" paragraph
50	% AFTER: the RELATE addition above
51	% BEFORE: "\citet{ekaw2024_ontology_beam}..." (line 72)
52	% ============================================================
53	
54	Concurrently, \citet{zhou2026ontologytools} compile OWL ontologies into executable tool interfaces within The World Avatar framework, requiring LLM agents to invoke ontology-aware tools that enforce semantic constraints during knowledge graph construction from scientific text.
55	This ``ontology-to-tools'' approach shares OntoCoDec's philosophy of compiling formal ontological knowledge into runtime enforcement mechanisms, but operates at the tool-call level (constraining which API functions the agent invokes) rather than at the token level (constraining which tokens the decoder produces), and requires an agentic multi-step workflow rather than single-pass autoregressive generation.
56	
57	
58	% ============================================================
59	% 5. zhou2026snowballing AUDIT
60	% STATUS: VERIFIED — paper exists and description is accurate
61	%   Author: Hongxu Zhou
62	%   Title: "From Hallucination to Structure Snowballing:
63	%           The Alignment Tax of Constrained Decoding in LLM Reflection"
64	%   arXiv: 2604.06066, April 2026
65	%   No confirmed venue yet; treat as arXiv preprint
66	%
67	% ACTION: Remove the "% PENDING AUDIT" comment from
68	%         section6_related_work.tex line 85.
69	%         The existing description is accurate: the paper identifies
70	%         "structure snowballing" as a failure mode where format
71	%         compliance cognitive load traps models in repetitive
72	%         structural patterns during self-correction iterations.
73	%
74	% RECOMMENDED BIB ENTRY (if not already present):
75	%   @article{zhou2026snowballing,
76	%     title   = {From Hallucination to Structure Snowballing:
77	%                The Alignment Tax of Constrained Decoding in
78	%                {LLM} Reflection},
79	%     author  = {Zhou, Hongxu},
80	%     journal = {arXiv preprint arXiv:2604.06066},
81	%     year    = {2026},
82	%     url     = {https://arxiv.org/abs/2604.06066}
83	%   }
84	% ============================================================
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf1d1223-f56d-4fd6-91fd-596d5a39e007",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "eebde8b5-962f-4c6d-ad4c-292690a7a94e",
  "sourceToolAssistantUUID": "bf1d1223-f56d-4fd6-91fd-596d5a39e007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T21:27:32.828Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014wivBn6zJRWsZE2PRQYgy9`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eebde8b5-962f-4c6d-ad4c-292690a7a94e",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Ap7HPAuVcLQTnfGrBu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9888d9a4-2bc0-4e67-bca2-38be41ce7ee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9ru88FMPpjwEiRs94VuB7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7773,
      "cache_read_input_tokens": 54574,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7773
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 54574,
          "cache_creation_input_tokens": 7773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7773,
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

_source line 50 · 2026-05-14T21:27:32.862Z_

<details><summary>↩ Tool result · `toolu_014wivBn6zJRWsZE2PRQYgy9`</summary>

```text
artifacts/dream_reports/dream_20260514T094226/median/references.bib
artifacts/_project/paper/relwork_new_entries.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9888d9a4-2bc0-4e67-bca2-38be41ce7ee1",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "31caf0ad-0564-43e5-9e3a-58c21ac8e403",
  "sourceToolAssistantUUID": "9888d9a4-2bc0-4e67-bca2-38be41ce7ee1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T21:27:38.016Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NFLagWdqDcG5Wp1U48wqv9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31caf0ad-0564-43e5-9e3a-58c21ac8e403",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3ApatoX9jz3fPMbcP4M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f5d768d-cd82-42ab-aa5e-5a06f6085808",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUSf4Z9SjLFFM77yni2AnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7085,
      "cache_read_input_tokens": 62347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7085,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 52 · 2026-05-14T21:27:38.030Z_

<details><summary>↩ Tool result · `toolu_01NFLagWdqDcG5Wp1U48wqv9`</summary>

```text
1	% ============================================================
2	% Merged authoritative BibTeX references (9 entries)
3	% Merged 2026-05-14 from relwork_new_entries.bib + new_references.bib
4	% ============================================================
5	
6	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
7	% Venue: ICLR 2022 (cite key corrected from synchromesh_neurips2022)
8	@inproceedings{synchromesh_iclr2022,
9	  title     = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},
10	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
11	  booktitle = {International Conference on Learning Representations},
12	  year      = {2022},
13	  url       = {https://openreview.net/forum?id=KmtVD97J43e}
14	}
15	
16	% Confirmed via: NeurIPS 2023 proceedings, microsoft/monitors4codegen GitHub
17	@inproceedings{mgd_neurips2023,
18	  title     = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},
19	  author    = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},
20	  booktitle = {Advances in Neural Information Processing Systems},
21	  volume    = {36},
22	  year      = {2023},
23	  url       = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}
24	}
25	
26	% Confirmed via: ACM DL doi:10.1145/3729274, arXiv:2504.09246, SRI Lab ETH
27	@article{pldi2025_type_constrained_codegen,
28	  title     = {Type-Constrained Code Generation with Language Models},
29	  author    = {M\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},
30	  journal   = {Proceedings of the ACM on Programming Languages},
31	  volume    = {9},
32	  number    = {PLDI},
33	  year      = {2025},
34	  doi       = {10.1145/3729274},
35	  url       = {https://dl.acm.org/doi/10.1145/3729274}
36	}
37	
38	% Confirmed via: ACL Anthology W04-2401, scottyih.org
39	% WARNING: cite key suggests AAAI 2004, but actual venue is CoNLL 2004 at HLT-NAACL
40	@inproceedings{roth_yih_2004,
41	  title     = {A Linear Programming Formulation for Global Inference in Natural Language Tasks},
42	  author    = {Roth, Dan and Yih, Wen-tau},
43	  booktitle = {Proceedings of the Eighth Conference on Computational Natural Language Learning ({CoNLL}-2004) at {HLT}-{NAACL} 2004},
44	  pages     = {1--8},
45	  year      = {2004},
46	  address   = {Boston, Massachusetts, USA},
47	  url       = {https://aclanthology.org/W04-2401/}
48	}
49	
50	% Confirmed via: ACL Anthology 2023.findings-emnlp.425, zjunlp/AdaKGC GitHub
51	@inproceedings{adakgc_emnlp2023,
52	  title     = {Schema-adaptable Knowledge Graph Construction},
53	  author    = {Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang, Ningyu},
54	  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2023},
55	  pages     = {6408--6431},
56	  year      = {2023},
57	  url       = {https://aclanthology.org/2023.findings-emnlp.425/}
58	}
59	
60	% Confirmed via: ACL Anthology 2024.acl-long.475, arXiv:2403.07969
61	@inproceedings{knowcoder_acl2024,
62	  title     = {{KnowCoder}: Coding Structured Knowledge into {LLMs} for Universal Information Extraction},
63	  author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
64	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
65	  pages     = {8758--8779},
66	  year      = {2024},
67	  address   = {Bangkok, Thailand},
68	  url       = {https://aclanthology.org/2024.acl-long.475/}
69	}
70	
71	% Confirmed via: Oxford Academic Bioinformatics btae104, PubMed 38383067
72	@article{spires_2024,
73	  title     = {Structured Prompt Interrogation and Recursive Extraction of Semantics ({SPIRES}): A Method for Populating Knowledge Bases Using Zero-shot Learning},
74	  author    = {Caufield, J. Harry and Hegde, Harshad and Emonet, Vincent and Harris, Nomi L. and Joachimiak, Marcin P. and Matentzoglu, Nicolas and Kim, HyeongSik and Moxon, Sierra and Reese, Justin T. and Haendel, Melissa A. and Robinson, Peter N. and Mungall, Christopher J.},
75	  journal   = {Bioinformatics},
76	  volume    = {40},
77	  number    = {3},
78	  pages     = {btae104},
79	  year      = {2024},
80	  doi       = {10.1093/bioinformatics/btae104},
81	  url       = {https://academic.oup.com/bioinformatics/article/40/3/btae104/7612230}
82	}
83	
84	% Confirmed via: arXiv:2510.01409, Wiley Advanced Intelligent Systems doi:10.1002/aisy.202501381
85	@misc{ontologx_2025,
86	  title         = {{OntoLogX}: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models},
87	  author        = {Cotti, Luca and Drago, Idilio and Rula, Anisa and Bianchini, Devis and Cerutti, Federico},
88	  year          = {2025},
89	  eprint        = {2510.01409},
90	  archiveprefix = {arXiv},
91	  primaryclass  = {cs.AI},
92	  url           = {https://arxiv.org/abs/2510.01409}
93	}
94	
95	% Confirmed via: Springer LNCS 15370, arXiv:2411.15666, Lama-West GitHub
96	@inproceedings{ekaw2024_ontology_beam,
97	  title     = {Ontology-Constrained Generation of Domain-Specific Clinical Summaries},
98	  author    = {Mehenni, Gaya and Zouaq, Amal},
99	  booktitle = {Knowledge Engineering and Knowledge Management ({EKAW} 2024)},
100	  series    = {Lecture Notes in Computer Science},
101	  volume    = {15370},
102	  pages     = {382--398},
103	  year      = {2024},
104	  publisher = {Springer},
105	  doi       = {10.1007/978-3-031-77792-9_23}
106	}
107	
108	% ============================================================
109	% New entries added 2026-05-14 for §6 related work expansion
110	% ============================================================
111	
112	% Confirmed via: ACL Anthology 2021.emnlp-main.779, arXiv:2109.05093, GitHub ServiceNow/picard
113	@inproceedings{scholak2021picard,
114	  title     = {{PICARD}: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models},
115	  author    = {Scholak, Torsten and Schucher, Nathan and Bahdanau, Dzmitry},
116	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
117	  year      = {2021},
118	  url       = {https://aclanthology.org/2021.emnlp-main.779/}
119	}
120	
121	% Confirmed via: arXiv:2509.19057, ResearchGate, OpenReview gcG8dmAUNh
122	@article{olasunkanmi2025relate,
123	  title   = {{RELATE}: Relation Extraction in Biomedical Abstracts with {LLMs} and Ontology Constraints},
124	  author  = {Olasunkanmi, Olawumi and Satusky, Mathew and Yi, Hong and Bizon, Chris and Lee, Harlin and Ahalt, Stanley},
125	  journal = {arXiv preprint arXiv:2509.19057},
126	  year    = {2025},
127	  url     = {https://arxiv.org/abs/2509.19057}
128	}
129	
130	% Confirmed via: arXiv:2602.03439, University of Cambridge / The World Avatar project
131	@article{zhou2026ontologytools,
132	  title   = {Ontology-to-tools compilation for executable semantic constraint enforcement in {LLM} agents},
133	  author  = {Zhou, Xiaochi and Bulter, Patrick and Yang, Changxuan and Rihm, Simon D. and Angkanaporn, Thitikarn and Akroyd, Jethro and Mosbach, Sebastian and Kraft, Markus},
134	  journal = {arXiv preprint arXiv:2602.03439},
135	  year    = {2026},
136	  url     = {https://arxiv.org/abs/2602.03439}
137	}
138	
139	% Confirmed via: IOS Press ECAI 2020 FAIA vol.325, arXiv:1909.07755, GitHub lavis-nlp/spert
140	@inproceedings{eberts2020spert,
141	  title     = {Span-based Joint Entity and Relation Extraction with Transformer Pre-training},
142	  author    = {Eberts, Markus and Ulges, Adrian},
143	  booktitle = {Proceedings of the 24th European Conference on Artificial Intelligence ({ECAI} 2020)},
144	  series    = {Frontiers in Artificial Intelligence and Applications},
145	  volume    = {325},
146	  pages     = {2006--2013},
147	  year      = {2020},
148	  doi       = {10.3233/FAIA200321}
149	}
150	
151	% Confirmed via: ACL Anthology 2021.emnlp-main.17, arXiv:2108.12202
152	% NOTE: venue is EMNLP 2021 (NOT AAAI 2021)
153	@inproceedings{yan2021pfn,
154	  title     = {A Partition Filter Network for Joint Entity and Relation Extraction},
155	  author    = {Yan, Zhiheng and Zhang, Chong and Fu, Jinlan and Zhang, Qi and Wei, Zhongyu},
156	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
157	  pages     = {185--197},
158	  year      = {2021},
159	  url       = {https://aclanthology.org/2021.emnlp-main.17/}
160	}
161	
162	% Confirmed via: ACL Anthology 2021.naacl-main.5, GitHub princeton-nlp/PURE
163	@inproceedings{zhong2021frustratingly,
164	  title     = {A Frustratingly Easy Approach for Entity and Relation Extraction},
165	  author    = {Zhong, Zexuan and Chen, Danqi},
166	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
167	  pages     = {50--61},
168	  year      = {2021},
169	  address   = {Online},
170	  publisher = {Association for Computational Linguistics},
171	  url       = {https://aclanthology.org/2021.naacl-main.5}
172	}
173	
174	% Confirmed via: ACL Anthology 2022.acl-long.337, GitHub thunlp/PL-Marker
175	@inproceedings{ye2022packed,
176	  title     = {Packed Levitated Marker for Entity and Relation Extraction},
177	  author    = {Ye, Deming and Lin, Yankai and Li, Peng and Sun, Maosong},
178	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
179	  pages     = {4904--4917},
180	  year      = {2022},
181	  address   = {Dublin, Ireland},
182	  publisher = {Association for Computational Linguistics},
183	  url       = {https://aclanthology.org/2022.acl-long.337}
184	}
185	
186	% Confirmed via: arXiv:2604.06066 (previously PENDING AUDIT — now verified)
187	@article{zhou2026snowballing,
188	  title   = {From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in {LLM} Reflection},
189	  author  = {Zhou, Hongxu},
190	  journal = {arXiv preprint arXiv:2604.06066},
191	  year    = {2026},
192	  url     = {https://arxiv.org/abs/2604.06066}
193	}
194	
195	% ============================================================
196	% Batch 1: Constrained decoding + IE foundations (10 entries)
197	% ============================================================
198	
199	% Confirmed via: arXiv 2411.15100, MLSys 2025 proceedings
200	@inproceedings{dong2025xgrammar,
201	  title     = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},
202	  author    = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},
203	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
204	  year      = {2025},
205	  url       = {https://arxiv.org/abs/2411.15100}
206	}
207	
208	% Confirmed via: arXiv 2307.09702
209	@article{willard2023outlines,
210	  title   = {Efficient Guided Generation for Large Language Models},
211	  author  = {Willard, Brandon T. and Louf, R{\'e}mi},
212	  journal = {arXiv preprint arXiv:2307.09702},
213	  year    = {2023},
214	  url     = {https://arxiv.org/abs/2307.09702}
215	}
216	
217	% Confirmed via: ACM DL 10.1145/3591300, PLDI 2023
218	@inproceedings{beurer-kellner2023lmql,
219	  title     = {Prompting Is Programming: A Query Language for Large Language Models},
220	  author    = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},
221	  booktitle = {Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI)},
222	  year      = {2023},
223	  url       = {https://doi.org/10.1145/3591300}
224	}
225	
226	% Confirmed via: PMLR v235, ICML 2024
227	@inproceedings{beurer-kellner2024domino,
228	  title     = {Guiding {LLMs} The Right Way: Fast, Non-Invasive Constrained Generation},
229	  author    = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},
230	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
231	  pages     = {3658--3673},
232	  year      = {2024},
233	  series    = {PMLR},
234	  volume    = {235},
235	  url       = {https://proceedings.mlr.press/v235/beurer-kellner24a.html}
236	}
237	
238	% Confirmed via: NeurIPS 2024 proceedings, OpenReview
239	@inproceedings{park2024grammar,
240	  title     = {Grammar-Aligned Decoding},
241	  author    = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},
242	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
243	  year      = {2024},
244	  url       = {https://arxiv.org/abs/2405.21047}
245	}
246	
247	% Confirmed via: OpenReview, ICLR 2021
248	@inproceedings{decao2021genre,
249	  title     = {Autoregressive Entity Retrieval},
250	  author    = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},
251	  booktitle = {International Conference on Learning Representations (ICLR)},
252	  year      = {2021},
253	  url       = {https://openreview.net/forum?id=5k8F6UU39V}
254	}
255	
256	% Confirmed via: ACL Anthology 2022.naacl-main.342
257	@inproceedings{josifoski2022genie,
258	  title     = {{GenIE}: Generative Information Extraction},
259	  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
260	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
261	  pages     = {4626--4643},
262	  year      = {2022},
263	  url       = {https://aclanthology.org/2022.naacl-main.342/}
264	}
265	
266	% Confirmed via: ACL Anthology 2023.emnlp-main.674
267	@inproceedings{geng2023gcd,
268	  title     = {Grammar-Constrained Decoding for Structured {NLP} Tasks without Finetuning},
269	  author    = {Geng, Saibo and Josifoski, Martin and Peyrard, Maxime and West, Robert},
270	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
271	  year      = {2023},
272	  url       = {https://aclanthology.org/2023.emnlp-main.674/}
273	}
274	
275	% Confirmed via: ACL Anthology 2021.naacl-main.339
276	@inproceedings{lu2021neurologic,
277	  title     = {{NeuroLogic} Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints},
278	  author    = {Lu, Ximing and West, Peter and Zellers, Rowan and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
279	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
280	  pages     = {4288--4299},
281	  year      = {2021},
282	  url       = {https://aclanthology.org/2021.naacl-main.339/}
283	}
284	
285	% Confirmed via: ACL Anthology 2022.acl-long.395
286	@inproceedings{lu2022uie,
287	  title     = {Unified Structure Generation for Universal Information Extraction},
288	  author    = {Lu, Yaojie and Liu, Qing and Dai, Dai and Xiao, Xinyan and Lin, Hongyu and Han, Xianpei and Sun, Le and Wu, Hua},
289	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
290	  pages     = {5755--5772},
291	  year      = {2022},
292	  url       = {https://aclanthology.org/2022.acl-long.395/}
293	}
294	
295	% ============================================================
296	% Batch 2: 10 entries added 2026-05-14
297	% ============================================================
298	
299	% Confirmed via: ICLR 2024 proceedings, OpenReview Y3wpuxd7u9, arXiv:2310.03668
300	@inproceedings{sainz2024gollie,
301	  title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction Modeling},
302	  author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
303	  booktitle = {The Twelfth International Conference on Learning Representations},
304	  year      = {2024},
305	  url       = {https://openreview.net/forum?id=Y3wpuxd7u9}
306	}
307	
308	% Confirmed via: ACL Anthology 2023.acl-long.855, arXiv:2305.05711
309	@inproceedings{li2023codeie,
310	  title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
311	  author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
312	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
313	  pages     = {15339--15353},
314	  year      = {2023},
315	  address   = {Toronto, Canada},
316	  url       = {https://aclanthology.org/2023.acl-long.855/}
317	}
318	
319	% Confirmed via: ACL Anthology 2024.emnlp-main.419, arXiv:2405.05008, GitHub THU-KEG/ADELIE
320	@inproceedings{qi2024adelie,
321	  title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
322	  author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
323	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
324	  year      = {2024},
325	  address   = {Miami, Florida, USA},
326	  url       = {https://aclanthology.org/2024.emnlp-main.419/}
327	}
328	
329	% Confirmed via: arXiv:2404.12493, GitHub urchade/EnriCo
330	% NOTE: arXiv preprint; no conference publication found
331	@article{zaratiana2024enrico,
332	  title   = {{EnriCo}: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction},
333	  author  = {Zaratiana, Urchade and Tomeh, Nadi and Dauxais, Yann and Holat, Pierre and Charnois, Thierry},
334	  journal = {arXiv preprint arXiv:2404.12493},
335	  year    = {2024},
336	  url     = {https://arxiv.org/abs/2404.12493}
337	}
338	
339	% Confirmed via: arXiv:2509.04696, Apple ML Research machinelearning.apple.com/research/odke
340	% NOTE: cite key uses "odke"; actual paper title is "ODKE+"
341	@article{khorshidi2025odke,
342	  title   = {{ODKE+}: Ontology-Guided Open-Domain Knowledge Extraction with {LLMs}},
343	  author  = {Khorshidi, Samira and Nikfarjam, Azadeh and Shankar, Suprita and Sang, Yisi and Govind, Yash and Jang, Hyun and Kasgari, Ali and McClimans, Alexis and Soliman, Mohamed and Konda, Vishnu and Fakhry, Ahmed and Qi, Xiaoguang},
344	  journal = {arXiv preprint arXiv:2509.04696},
345	  year    = {2025},
346	  url     = {https://arxiv.org/abs/2509.04696}
347	}
348	
349	% Confirmed via: ACL Anthology 2023.findings-eacl.95
350	@inproceedings{upadhyay2023openie,
351	  title     = {Open Information Extraction with Entity Focused Constraints},
352	  author    = {Upadhyay, Prajna and Balalau, Oana and Manolescu, Ioana},
353	  booktitle = {Findings of the Association for Computational Linguistics: {EACL} 2023},
354	  year      = {2023},
355	  url       = {https://aclanthology.org/2023.findings-eacl.95/}
356	}
357	
358	% Confirmed via: ACL Anthology 2025.genaik-1.10, GenAIK Workshop at COLING 2025
359	@inproceedings{regino2025kgcurator,
360	  title     = {Can {LLMs} be Knowledge Graph Curators for Validating Triple Insertions?},
361	  author    = {Regino, Andr{\'e} Gomes and dos Reis, Julio Cesar},
362	  booktitle = {Proceedings of the Workshop on Generative {AI} and Knowledge Graphs ({GenAIK})},
363	  pages     = {87--99},
364	  year      = {2025},
365	  address   = {Abu Dhabi, UAE},
366	  url       = {https://aclanthology.org/2025.genaik-1.10/}
367	}
368	
369	% Confirmed via: ACL Anthology 2024.emnlp-industry.91, arXiv:2408.02442
370	@inproceedings{tam2024letmespeak,
371	  title     = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},
372	  author    = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},
373	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
374	  pages     = {1218--1236},
375	  year      = {2024},
376	  address   = {Miami, Florida, US},
377	  url       = {https://aclanthology.org/2024.emnlp-industry.91/}
378	}
379	
380	% Confirmed via: PMLR v267/banerjee25a, ICML 2025, arXiv:2502.09061
381	@inproceedings{banerjee2025crane,
382	  title     = {{CRANE}: Reasoning with Constrained {LLM} Generation},
383	  author    = {Banerjee, Debangshu and Suresh, Tarun and Ugare, Shubham and Misailovic, Sasa and Singh, Gagandeep},
384	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
385	  pages     = {2836--2857},
386	  year      = {2025},
387	  url       = {https://proceedings.mlr.press/v267/banerjee25a.html}
388	}
389	
390	% Confirmed via: ACL Anthology 2025.ranlp-1.124
391	@inproceedings{schall2025hiddencost,
392	  title     = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},
393	  author    = {Schall, Maximilian and de Melo, Gerard},
394	  booktitle = {Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing ({RANLP} 2025)},
395	  year      = {2025},
396	  address   = {Varna, Bulgaria},
397	  url       = {https://aclanthology.org/2025.ranlp-1.124/}
398	}
399	
400	% ============================================================
401	% Dataset & model references (5 entries)
402	% ============================================================
403	
404	% Confirmed via: ACL Anthology D18-1360, arXiv:1808.09602
405	@inproceedings{luan2018scierc,
406	  title     = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
407	  author    = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
408	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
409	  pages     = {3219--3232},
410	  year      = {2018},
411	  address   = {Brussels, Belgium},
412	  url       = {https://aclanthology.org/D18-1360/}
413	}
414	
415	% Confirmed via: ACL Anthology P19-1074, arXiv:1906.06127
416	@inproceedings{yao2019docred,
417	  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
418	  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
419	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
420	  pages     = {764--777},
421	  year      = {2019},
422	  address   = {Florence, Italy},
423	  url       = {https://aclanthology.org/P19-1074/}
424	}
425	
426	% Confirmed via: arXiv:2302.10205, Semantic Scholar
427	@article{wei2023zeroshot,
428	  title   = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},
429	  author  = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},
430	  journal = {arXiv preprint arXiv:2302.10205},
431	  year    = {2023},
432	  url     = {https://arxiv.org/abs/2302.10205}
433	}
434	
435	% Confirmed via: arXiv:2505.09388, Hugging Face model cards
436	@article{qwen2025qwen3,
437	  title   = {Qwen3 Technical Report},
438	  author  = {{Qwen Team}},
439	  journal = {arXiv preprint arXiv:2505.09388},
440	  year    = {2025},
441	  url     = {https://arxiv.org/abs/2505.09388}
442	}
443	
444	% Confirmed via: NeurIPS 2024 proceedings, arXiv:2312.07104
445	@inproceedings{zheng2024sglang,
446	  title     = {{SGLang}: Efficient Execution of Structured Language Model Programs},
447	  author    = {Zheng, Lianmin and Yin, Liangsheng and Xie, Zhiqiang and Sun, Chuyue and Huang, Jeff and Yu, Cody Hao and Cao, Shiyi and Kozyrakis, Christos and Stoica, Ion and Gonzalez, Joseph E. and Barrett, Clark and Sheng, Ying},
448	  booktitle = {Advances in Neural Information Processing Systems},
449	  volume    = {37},
450	  year      = {2024},
451	  url       = {https://arxiv.org/abs/2312.07104}
452	}
453	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f5d768d-cd82-42ab-aa5e-5a06f6085808",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "c57d3f2b-bb57-460d-830f-59e28d9d738d",
  "sourceToolAssistantUUID": "8f5d768d-cd82-42ab-aa5e-5a06f6085808",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T21:27:38.643Z_

<details open><summary>🔧 Tool call — Read · `toolu_016hTWo4Mb3tRKfU3F7dUuWt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57d3f2b-bb57-460d-830f-59e28d9d738d",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3ApatoX9jz3fPMbcP4M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1328af47-8fbf-48ce-8a34-9765da1d8520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUSf4Z9SjLFFM77yni2AnP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7085,
      "cache_read_input_tokens": 62347,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7085
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 62347,
          "cache_creation_input_tokens": 7085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7085,
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

_source line 54 · 2026-05-14T21:27:38.658Z_

<details><summary>↩ Tool result · `toolu_016hTWo4Mb3tRKfU3F7dUuWt`</summary>

```text
1	% Section 2: Background for OntoCoDec paper
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\subsection{IE Ontology Structure}
7	\label{sec:bg:ontology}
8	
9	An information extraction ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines a set of entity types $\mathcal{E}$, a set of relation types $\mathcal{R}$, and a domain/range mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ that specifies, for each relation type $r \in \mathcal{R}$, the set of valid (head type, tail type) pairs.
10	A triple $(h, r, t)$ is \emph{type-valid} under $\mathcal{O}$ if and only if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
11	For example, SciERC~\citep{luan2018scierc} defines $|\mathcal{E}|=6$ entity types, $|\mathcal{R}|=7$ relation types, and $|\sigma(r)|$ ranges from 17 (\textsc{Compare}) to 35 (\textsc{Used-for}) valid type pairs per relation, out of $|\mathcal{E}|^2 = 36$ possible.
12	We define the \emph{constraint tightness} of a relation $r$ as the fraction of the type-pair space it excludes: $1 - |\sigma(r)| / |\mathcal{E}|^2$.
13	Tighter constraints leave fewer valid options for the model, increasing the likelihood of violations.
14	Empirically, constraint tightness varies substantially both within and across datasets.
15	Within SciERC, the overall average of 24.0 valid pairs (out of 36) masks sharp per-relation differences: \textsc{Compare} admits only 17 pairs (tightness 0.53), while \textsc{Used-for} admits 35 (tightness 0.03).
16	DocRED~\citep{yao2019docred} exhibits far tighter constraints overall, with relations averaging only 5.68 valid pairs (out of 36; tightness 0.84), reflecting fundamentally different ontology designs.
17	
18	\subsection{Grammar-Constrained Decoding}
19	\label{sec:bg:gcd}
20	
21	In autoregressive language model generation, each token $y_t$ is sampled from $p(\cdot \mid y_{<t}, x)$ where $x$ is the input prompt.
22	Grammar-constrained decoding restricts this distribution at each step by applying a token-level mask $M_g \in \{0, 1\}^{|V|}$ that zeros out tokens incompatible with a target grammar.
23	XGrammar~\citep{dong2025xgrammar} compiles a JSON Schema into a pushdown automaton, computing the set of valid next tokens from the current automaton state at each decoding step.
24	This enables enforcement of structural constraints---valid JSON syntax, enumerated vocabularies---with negligible latency overhead by precomputing context-independent token sets and caching adaptive token sets per grammar state.
25	Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} provide similar capabilities through finite-state machine and interleaved grammar-based approaches, respectively.
26	
27	However, grammar-constrained decoding is inherently limited to constraints expressible as context-free grammars.
28	Cross-field semantic constraints---such as ``if the relation is \textsc{Feature-of}, then the head entity type must be \textsc{Method} or \textsc{OtherScientificTerm}''---depend on previously generated field values and cannot be captured by a static CFG.
29	This limitation motivates a second constraint layer that tracks generation state and enforces semantic validity dynamically.
30	
31	\subsection{Problem Statement}
32	\label{sec:bg:problem}
33	
34	Given an IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ and an autoregressive language model $\mathcal{M}$, we seek to compile $\mathcal{O}$ into decoding-time constraints $\mathcal{C}$ such that the constrained output of $\mathcal{M}$ satisfies:
35	\begin{enumerate}[label=(\alph*)]
36	    \item \textbf{Structural validity}: the output is well-formed JSON conforming to the IE schema, with all entity types $\in \mathcal{E}$ and relation types $\in \mathcal{R}$;
37	    \item \textbf{Type validity}: for every extracted triple $(h, r, t)$, the type assignment is ontology-consistent: $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
38	\end{enumerate}
39	
40	Condition (a) is context-free and directly expressible via grammar-constrained decoding.
41	Condition (b) is context-sensitive: enforcing domain/range constraints for a relation requires knowing the types of its argument entities, which are generated earlier in the sequence.
42	Crucially, however, (b) is \emph{prefix-decidable}---at the point where a relation's argument type is being generated, all information needed to evaluate the constraint (the relation type and the entity registry built from prior tokens) is available in the already-generated prefix.
43	This prefix-decidability property, combined with a stateful entity registry, makes (b) amenable to token-level enforcement during autoregressive decoding, despite being beyond the expressiveness of context-free grammars.
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1328af47-8fbf-48ce-8a34-9765da1d8520",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "eefedd56-53bd-410e-8fbd-b82bdaa7e1db",
  "sourceToolAssistantUUID": "1328af47-8fbf-48ce-8a34-9765da1d8520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-14T21:27:41.728Z_

Now let me also read the dream review reports for additional context on what prior reviewers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eefedd56-53bd-410e-8fbd-b82bdaa7e1db",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Aq1Tv9gWBozhXg65Co",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cf8aeed-f785-4300-831c-9fec210dd37a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwKZ1FM7t8eBU1EDyTZ8Z4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10898,
      "cache_read_input_tokens": 69432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10898,
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

_source line 56 · 2026-05-14T21:27:44.090Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UwJLsshd78XnkhYEWfZFbf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T205155/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cf8aeed-f785-4300-831c-9fec210dd37a",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Aq1Tv9gWBozhXg65Co",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39a2c57c-12f8-4a34-a430-070684a96749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwKZ1FM7t8eBU1EDyTZ8Z4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10898,
      "cache_read_input_tokens": 69432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10898,
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

_source line 57 · 2026-05-14T21:27:44.097Z_

<details><summary>↩ Tool result · `toolu_01UwJLsshd78XnkhYEWfZFbf`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{graphicx}
6	\usepackage{amsmath,amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{url}
11	\usepackage[margin=2.5cm]{geometry}
12	\usepackage{hyperref}
13	\usepackage{natbib}
14	\usepackage{array}
15	\usepackage{tabularx}
16	
17	\newcommand{\sys}{OntoCoDec}
18	\newcommand{\dr}{domain/range}
19	\newcommand{\rv}{relation vocabulary}
20	\newcommand{\et}{entity type}
21	\newcommand{\cf}{cross-field consistency}
22	
23	\title{\sys{}: Near-Complete Type-Valid Information Extraction\\via Compiled Ontology Constraints}
24	
25	\author{
26	  Anonymous EMNLP Submission
27	}
28	\date{}
29	
30	\begin{document}
31	\maketitle
32	
33	% ============================================================
34	\begin{abstract}
35	Large language models (LLMs) applied to information extraction (IE) produce systematic ontology constraint violations---15.4\% of extracted triples violate domain/range type constraints on SciERC and 18.7\% on DocRED. We show that these violations concentrate on relation types with tight type constraints (e.g., Compare: 42.4\%) rather than scaling with ontology size, and that prompt-level intervention, while reducing overall violations by 62\%, remains unreliable at the per-relation level, with one relation type exhibiting \emph{increased} violations.
36	
37	We present \sys{}, a framework that automatically compiles IE ontology schemas into two composable constraint layers for LLM decoding: (1) a \emph{grammar layer} enforcing JSON structure and type/relation vocabulary via context-free grammars, and (2) a \emph{semantic layer} enforcing cross-field domain/range constraints through a stateful entity registry with dynamic logit masking. The two layers compose via bitwise AND with an enabling dependency: grammar ensures vocabulary validity, enabling the semantic layer to look up and enforce domain/range rules.
38	
39	Evaluated on SciERC (7 relations) and DocRED (96 relations) with Qwen3-8B and Llama-3.1-8B, \sys{} reduces domain/range violations by 94\% on SciERC (15.4\%$\to$0.93\%) and 44.7--90.2\% on DocRED, while eliminating entity-type and relation-vocabulary violations entirely. F1 impact is neutral on SciERC ($p{=}0.58$) and significantly positive on DocRED ($+0.50$pp relation F1, $p{<}0.001$). We provide a decidability taxonomy classifying constraint types by their amenability to autoregressive enforcement and identify cross-field consistency as an inherent limitation of per-relation independent enforcement.
40	\end{abstract}
41	
42	% ============================================================
43	\section{Introduction}
44	\label{sec:intro}
45	
46	Information extraction (IE) systems built on large language models achieve impressive zero-shot performance by framing extraction as structured generation. However, when an ontology defines type constraints on relations---e.g., that \textsc{Used-for} requires a \textsc{Method} head and a \textsc{Task} tail---LLMs routinely violate these constraints in their output.
47	
48	We conduct the first systematic study of ontology constraint violations in LLM-based IE. Our violation landscape analysis across two datasets (SciERC with 7 relations, DocRED with 96) reveals two key findings: (1) domain/range violations are non-trivial (15.4\% and 18.7\% respectively) and concentrate on relation types with tight constraints rather than scaling with ontology size; (2) schema-informed prompting reduces violations by 62\% overall but is unreliable at the per-relation level---Evaluate-for violations \emph{increase} by 5.8 percentage points even when constraints are explicitly described in the prompt.
49	
50	These findings motivate \sys{}, a framework that compiles ontology schemas into decoder constraints operating at two complementary layers. The \textbf{grammar layer} uses context-free grammars (via XGrammar) to enforce JSON structure, entity type vocabulary, and relation name vocabulary---constraints that are decidable from the token prefix alone. The \textbf{semantic layer} maintains a stateful entity registry during generation and applies dynamic logit masking to enforce domain/range constraints---which require cross-field state but remain prefix-decidable given the registry.
51	
52	The two layers exhibit an \emph{enabling dependency}: grammar ensures every generated relation name belongs to the valid vocabulary, which is a prerequisite for the semantic layer to look up the corresponding domain/range rules. Without grammar, the semantic layer encounters out-of-vocabulary relation names and cannot enforce constraints (semantic-only achieves 24\% DR reduction vs.\ full system 94\%).
53	
54	We classify constraints into a decidability taxonomy: (a) purely local constraints (entity type $\in$ vocabulary), enforceable by grammar alone; (b) prefix-decidable with state (domain/range compatibility), requiring the semantic layer's entity registry; and (c) truly non-local constraints (forward coreference), which are out of scope for forward-only autoregressive decoding.
55	
56	Our contributions:
57	\begin{enumerate}
58	\item A systematic violation landscape study establishing that LLM-based IE produces non-trivial, tightness-driven ontology violations, and that prompt-level intervention is insufficient (\S\ref{sec:landscape}).
59	\item A composable two-layer constraint framework with principled decidability taxonomy, compiling ontology schemas into grammar and semantic decoder constraints (\S\ref{sec:method}).
60	\item Comprehensive experiments on 2 datasets $\times$ 2 models showing 94\% DR elimination on SciERC at zero F1 cost, with honest analysis of the cross-field consistency trade-off (\S\ref{sec:experiments}).
61	\item A cross-model generalization study demonstrating zero-code-modification transfer across model families, with a dual-factor analysis explaining DR reduction variance (\S\ref{sec:experiments}).
62	\end{enumerate}
63	
64	% ============================================================
65	\section{Background}
66	\label{sec:background}
67	
68	\paragraph{IE as Structured Generation.} Modern LLM-based IE frames extraction as generating JSON-structured output containing entity lists and relation triples. Each triple $(h, r, t)$ associates a head entity $h$ with type $\tau_h$, a relation $r$, and a tail entity $t$ with type $\tau_t$. An ontology schema $\mathcal{O}$ defines the valid entity types $\mathcal{T}$, relation types $\mathcal{R}$, and for each $r \in \mathcal{R}$, the domain $\text{dom}(r) \subseteq \mathcal{T}$ and range $\text{ran}(r) \subseteq \mathcal{T}$.
69	
70	\paragraph{Constraint Violations.} We define four violation types:
71	\begin{itemize}
72	\item \textbf{Entity type (ET)}: $\tau_h \notin \mathcal{T}$ or $\tau_t \notin \mathcal{T}$
73	\item \textbf{Relation vocabulary (RV)}: $r \notin \mathcal{R}$
74	\item \textbf{Domain/range (DR)}: $\tau_h \notin \text{dom}(r)$ or $\tau_t \notin \text{ran}(r)$
75	\item \textbf{Cross-field consistency (CF)}: same entity assigned different types across relations
76	\end{itemize}
77	
78	\paragraph{Grammar-Constrained Decoding.} Recent work on grammar-constrained decoding (e.g., XGrammar) enforces context-free grammar constraints during autoregressive generation by masking logits at each decoding step. This guarantees structural validity (e.g., valid JSON) but cannot enforce cross-field semantic constraints that depend on previously generated content.
79	
80	\paragraph{Constraint Tightness.} We define the \emph{constraint tightness} $\tau_r$ of a relation $r$ as:
81	\begin{equation}
82	\bar{\tau}_r = 1 - \frac{|\text{dom}(r)| \times |\text{ran}(r)|}{|\mathcal{T}|^2}
83	\end{equation}
84	Higher tightness means fewer valid type combinations, predicting higher violation rates.
85	
86	% ============================================================
87	\section{Violation Landscape Study}
88	\label{sec:landscape}
89	
90	We conduct a systematic study of ontology constraint violations in zero-shot LLM-based IE using Qwen3-8B on SciERC (551 abstracts, 7 relations) and DocRED (998 documents, 96 relations).
91	
92	% --- Experiment 1: SciERC minimal prompt ---
93	\subsection{SciERC Violation Profile}
94	\label{sec:scierc-violations}
95	
96	Table~\ref{tab:per-relation-dr} presents per-relation domain/range violation rates under a minimal prompt (relation list only, no constraint descriptions). The overall DR violation rate is 15.4\% (265 of 1,724 triples), but the distribution is highly non-uniform: Compare exhibits 42.4\% violations while Used-for shows only 0.8\%.
97	
98	\begin{table}[t]
99	\centering
100	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39a2c57c-12f8-4a34-a430-070684a96749",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "dc052a14-b8d9-4592-bcbc-1e617ae8f1da",
  "sourceToolAssistantUUID": "39a2c57c-12f8-4a34-a430-070684a96749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T21:27:44.809Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PSjBicQWV8oHBQYqrMN7sN`</summary>

```json
{
  "pattern": "**/dream_reports/**/review_report.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc052a14-b8d9-4592-bcbc-1e617ae8f1da",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Aq1Tv9gWBozhXg65Co",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a66fe08b-1616-46f6-808d-14408d07b96e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwKZ1FM7t8eBU1EDyTZ8Z4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10898,
      "cache_read_input_tokens": 69432,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10898
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 69432,
          "cache_creation_input_tokens": 10898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10898,
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

_source line 59 · 2026-05-14T21:27:44.826Z_

<details><summary>↩ Tool result · `toolu_01PSjBicQWV8oHBQYqrMN7sN`</summary>

```text
artifacts/dream_reports/dream_20260514T094226/median/review_report.md
artifacts/dream_reports/dream_20260514T094226/best/review_report.md
artifacts/dream_reports/dream_20260514T094226/worst/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a66fe08b-1616-46f6-808d-14408d07b96e",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "b39fc1e1-b05a-42e5-bcc3-a56465e1c41a",
  "sourceToolAssistantUUID": "a66fe08b-1616-46f6-808d-14408d07b96e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-14T21:27:47.999Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RsvmmhDTpQ3zYycXH2K82J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b39fc1e1-b05a-42e5-bcc3-a56465e1c41a",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AqTteLyfsMDKKo7rNf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee08938e-f221-495b-bf8e-e78f4faac6a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeqX6jozVCwZHCN162bP1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2880,
      "cache_read_input_tokens": 80330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2880,
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

_source line 61 · 2026-05-14T21:27:48.005Z_

<details><summary>↩ Tool result · `toolu_01RsvmmhDTpQ3zYycXH2K82J`</summary>

```text
1	---
2	dream_id: dream_20260514T094226
3	tier: best
4	overall_score: Weak Reject (3)
5	timestamp: 2026-05-14T11:02:35.235800+00:00
6	---
7	
8	# Reviewer R2 — Novelty, Significance, Related Work, Writing Quality
9	
10	## Paper: "How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation" / "OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints"
11	
12	**Note**: The "best" and "median" tier drafts differ in title and some numerical details. This review covers both, noting discrepancies where material.
13	
14	---
15	
16	## 1. Novelty Assessment
17	
18	### 1.1 Violation Landscape Study (Contribution 1)
19	**Moderate novelty.** The systematic measurement of ontology constraint violations in LLM-based IE is, to my knowledge, genuinely new — no prior work has characterized the per-relation distribution of type constraint violations in LLM-generated IE outputs. The finding that constraint tightness predicts violation rate is a useful empirical insight.
20	
21	However, measuring error rates of LLM outputs against a known schema is conceptually straightforward. The landscape study is descriptive rather than explanatory: the tightness-violation correlation is intuitive (tighter constraints leave less room for valid outputs, so violations are more likely) and does not reveal deeper mechanisms about *why* LLMs produce these violations (e.g., distributional prior conflicts, attention patterns, or training data biases). The "prior-constraint conflict" analysis for Evaluate-for is suggestive but underdeveloped.
22	
23	The landscape study spans only 2 datasets and 1-2 models, which limits its generality as a standalone empirical contribution. A landscape study claiming to characterize "how LLMs violate ontology constraints" should ideally include more diverse ontologies, model families, and scales.
24	
25	### 1.2 Grammar-Constrained Decoding for IE (Contribution 2)
26	**Low novelty.** Applying XGrammar to enforce JSON structure and vocabulary compliance is a straightforward engineering application of an existing tool. The paper itself acknowledges that grammar-constrained decoding is the "de facto standard for structured output" from LLMs. Compiling an IE ontology's entity types and relation names into a CFG and feeding it to XGrammar is exactly what the tool was designed for.
27	
28	The result (ET→0%, RV→0%) is expected by construction — this is the definition of grammar-constrained decoding. Reporting that it works is necessary for completeness but does not constitute a research contribution. The latency overhead measurement (13-14%) has some practical value.
29	
30	### 1.3 Semantic Constraint Layer (Contribution 3)
31	**Moderate novelty with significant caveats.** The stateful entity registry + dynamic logit masking for cross-field domain/range enforcement during autoregressive generation is the most novel component. The key idea — maintaining state across generation positions to enforce constraints beyond CFG expressiveness — is technically sound and fills a genuine gap.
32	
33	However:
34	- The mechanism (bitwise AND of two mask vectors) is elementary.
35	- The concept of type-constrained decoding with stateful monitors already exists in the code generation domain (Synchromesh ICLR'22, MGD NeurIPS'23, PLDI'25). The paper's own related work section acknowledges this. The transfer from code generation to IE is the claimed novelty, but the technical delta is modest — IE ontologies have flat domain/range sets (simpler than programming language type systems), and the main new challenge (inferring entity types from free text) is handled by simply recording types from the entity list, not by a novel inference mechanism.
36	- Effectiveness degrades substantially on DocRED (only 46% DR reduction vs 94% on SciERC), and the paper introduces a new class of violations (CF: 9.9% on SciERC) that did not exist in the unconstrained baseline. This trade-off weakens the practical value proposition.
37	
38	### 1.4 Overall Novelty Verdict
39	The paper's novelty is spread thin across three contributions, none of which is individually strong enough for a top venue. The landscape study is useful but shallow; the grammar layer is engineering; the semantic layer is the most novel but has limited effectiveness and introduces side effects. The "decidability taxonomy" (local / prefix-decidable / non-local) is a reasonable framing but not a deep theoretical contribution — it is a restatement of well-known properties of autoregressive generation.
40	
41	---
42	
43	## 2. Significance and Impact
44	
45	### 2.1 Who would use these findings?
46	Practitioners building LLM-based IE pipelines who need ontology compliance. The grammar layer is immediately deployable. The semantic layer requires implementing the TypeConstraintProcessor per ontology.
47	
48	### 2.2 Is the grammar layer finding actionable enough to justify publication?
49	No. "Use XGrammar to enforce JSON schema" is good engineering advice, not a research contribution. This belongs in a technical blog post or toolkit documentation, not a top-venue paper.
50	
51	### 2.3 Does the violation landscape data have reuse value?
52	Moderate. The per-relation violation data for SciERC and DocRED could inform future work on targeted constraint enforcement. However, the landscape is model-specific (Qwen3-8B) and setting-specific (zero-shot). Different models, prompt strategies, or fine-tuning would produce different violation landscapes.
53	
54	### 2.4 Is the positioning effective?
55	The paper tries to be both an empirical study and a method paper, but this dual positioning weakens both aspects. As an empirical study, it lacks breadth (2 datasets, 1-2 models). As a method paper, the method's effectiveness is partial (46% on DocRED) and introduces a new failure mode (CF violations). The paper would be stronger if it committed fully to one identity.
56	
57	### 2.5 Practical Significance Concern
58	The absolute R-F1 is ~8% across all configurations. The paper correctly notes this is a zero-shot setting and F1 is a control variable. However, this means the constraint enforcement is being evaluated on a system whose extraction quality is far below practical utility. It is unclear whether constrained decoding would provide the same benefits (or introduce the same CF trade-offs) on a fine-tuned model with R-F1 in the 40-50% range where the outputs actually matter. This limits the practical significance of the findings.
59	
60	---
61	
62	## 3. Related Work Coverage
63	
64	### 3.1 Reference Count
65	The "median" tier paper cites ~13 references; the extended related work section (section6_related_work.tex) cites ~25. The extended version is adequate; the short versions are insufficient. A paper making claims about being "the first" to do something must demonstrate thorough coverage of prior art.
66	
67	### 3.2 Missing or Underrepresented Areas
68	
69	**Structured prediction for IE (critical gap):**
70	- Roth & Yih (2004) is cited in the extended version but absent from the main drafts. This is the foundational work on enforcing type constraints in IE via ILP — the paper should explicitly position against it.
71	- Joint entity-relation extraction models (e.g., SpERT, PURE, PFN, UniRel) that implicitly enforce type constraints through shared representations are entirely absent.
72	- CasRel, TPLinker, and other structured prediction approaches for RE that handle type constraints architecturally.
73	
74	**Other constrained decoding methods:**
75	- PICARD (Scholak et al., 2021) is cited in the median bib but not discussed. PICARD does incremental parsing for SQL — a highly relevant constrained decoding approach.
76	- Guidance (Microsoft) and Instructor — practical tools for structured LLM output that compete with the grammar layer.
77	- JSON mode / structured output features built into commercial APIs (OpenAI, Anthropic) that solve the grammar-layer problem out of the box.
78	
79	**Schema-guided generation:**
80	- SGD (Schema-Guided Dialogue) and schema-guided approaches in dialogue systems.
81	- TANL (Paolini et al., 2021) — structured generation for IE.
82	
83	**KG completion with type constraints:**
84	- TransE/TransR/RotatE with type constraints are not discussed. Type-constrained KG completion (Krompass et al., 2015, mentioned in the task description but absent from the paper) is a relevant precedent.
85	
86	**Error analysis in IE:**
87	- Prior work on error analysis of IE systems (e.g., detailed error taxonomies for RE, NER error analysis) is not cited. The violation taxonomy presented is novel in the specific context of ontology constraints but should be positioned against existing error analysis frameworks.
88	
89	### 3.3 Is the positioning fair?
90	The claim "first systematic study of ontology constraint violations in LLM-based IE" appears defensible based on my knowledge. However, the claim "first to migrate type-constrained decoding from code generation to IE" (from the extended related work) may be overly strong — EnriCo (Zaratiana et al., AAAI 2024) applies ASP constraints during decoding for joint entity-relation extraction, which is a form of semantic-constrained decoding for IE, even if it uses different formalism.
91	
92	---
93	
94	## 4. Writing Quality
95	
96	### 4.1 Clarity of Exposition
97	Generally clear. The violation taxonomy (ET/RV/DR/CF) is well-defined. The enabling dependency between grammar and semantic layers is explained well. The constraint tightness definition is intuitive.
98	
99	### 4.2 Organization and Flow
100	The paper is well-organized with a logical progression from landscape study to method to experiments. The "best" tier draft has better flow than the "median" tier, with section numbering and cross-references more consistently applied.
101	
102	### 4.3 Negative Results Presentation
103	**A strength of this paper.** The honest presentation of:
104	- DocRED's attenuated results (46% vs 94%)
105	- CF violation trade-off (9.9% on SciERC)
106	- S2 offering no improvement over S1
107	- Evaluate-for regression under schema-informed prompting
108	
109	...is commendable and reflects scientific integrity. The paper does not oversell its findings.
110	
111	### 4.4 Title/Abstract Alignment
112	The "best" tier title ("Near-Complete Type-Valid IE via Compiled Ontology Constraints") overpromises slightly — "near-complete" applies to SciERC but not DocRED where 10.19% DR remains. The "median" tier title ("Type-Valid IE via Compiled Ontology Constraints") is more appropriate.
113	
114	The landscape study title variant ("How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation") better reflects the paper's actual balance of contributions but undersells the semantic layer.
115	
116	### 4.5 Specific Writing Issues
117	- The paper inconsistently uses "14%" and "62%" for latency overhead across drafts (the "best" tier says 37%, the "median" says 62% for full S1). These numbers need reconciliation.
118	- Some tables present "---" for values that should be reported (e.g., grammar-only DR on DocRED in Table 5 of the median draft).
119	- The "enabling ratio" metric (full DR reduction / semantic-only DR reduction) is introduced without adequate motivation for why this specific ratio is informative.
120	
121	---
122	
123	## 5. Weaknesses (Numbered)
124	
125	**W1 (Major): Limited experimental scope undermines generality claims.** Two datasets, one primary model (Qwen3-8B), zero-shot only. The cross-model validation with Llama-3.1-8B is SciERC-only and appears incomplete in the current drafts. For a paper claiming to present a general framework, this is insufficient. Critical missing experiments: (a) a fine-tuned model where F1 is practically meaningful; (b) at least one additional ontology domain (biomedical, financial); (c) larger models (70B+) where violation patterns may differ.
126	
127	**W2 (Major): The CF violation trade-off is inadequately addressed.** The semantic layer eliminates 94% of DR violations on SciERC but introduces 9.9% CF violations that did not exist before. The paper argues CF violations are "softer" than DR violations, but this is assertion rather than demonstrated. In a knowledge graph, an entity with inconsistent types across relations creates downstream inference failures. The net benefit calculation (DR reduction per CF increase) is not grounded in any downstream task evaluation.
128	
129	**W3 (Major): DocRED results are weak and inconsistent across drafts.** The "best" tier claims 46% DR reduction; the paper_framing.md mentions 35.5%. The grammar-only DR on DocRED *increases* from 18.7% to 26.17%, which the paper explains as a "denominator effect" — but this explanation itself reveals that the violation measurement is confounded by the constraint intervention. The tightness-violation correlation on DocRED is weak (rho=0.37 in one draft, 0.52 in another, 0.14 in the task description). These inconsistencies across drafts suggest the results are still in flux.
130	
131	**W4 (Moderate): No downstream task evaluation.** All evaluation is intrinsic (violation rates, F1 against gold labels). There is no evaluation of whether reduced violations actually improve downstream KG quality, question answering, or reasoning. The motivation section argues violations matter for "downstream knowledge graph population, reasoning engines, and regulatory compliance systems" — but this claim is never empirically validated.
132	
133	**W5 (Moderate): The decidability taxonomy is underexploited.** The three-level taxonomy (local / prefix-decidable / non-local) is presented as a contribution but only Type (a) and Type (b) constraints are addressed. Type (c) — forward coreference — is acknowledged as out of scope. The taxonomy itself is a straightforward observation about autoregressive generation and does not offer deep insight.
134	
135	**W6 (Moderate): Insufficient comparison with simpler baselines.** The paper compares against unconstrained generation and schema-informed prompting. Missing baselines: (a) post-hoc filtering (reject + regenerate invalid triples); (b) self-consistency voting across multiple samples; (c) few-shot prompting with constraint examples; (d) simple regex-based type checking during generation (without the full semantic layer machinery).
136	
137	**W7 (Minor): The paper conflates two different papers.** The "best" and "median" tier drafts present materially different numbers, framings, and even titles. The Spearman rho for tightness-DR on DocRED varies from 0.14 to 0.52 across documents. This suggests the experimental results are not yet settled, which is concerning for review.
138	
139	---
140	
141	## 6. Questions for Authors (Numbered)
142	
143	**Q1.** The DocRED Spearman rho for tightness-DR correlation is reported as 0.14 (p=0.18) in one place and 0.52 (p<0.001) in another. Which is correct? Is the discrepancy due to measuring unconstrained vs. constrained (full_s1) DR? If so, why does the correlation change so dramatically?
144	
145	**Q2.** Have you measured whether CF violations actually harm downstream tasks? The severity distinction (DR = hard, CF = soft) is intuitive but unvalidated. In what downstream application would CF violations be acceptable?
146	
147	**Q3.** What happens when this framework is applied to a fine-tuned IE model with R-F1 in the 40-50% range? Does the violation rate decrease (making constraints less necessary) or does the constraint framework still provide meaningful benefit?
148	
149	**Q4.** The grammar-only DR on DocRED *increases* (18.7% → 26.17%). You explain this as a denominator effect. But could it also reflect that grammar constraints force the model into generation patterns that produce more DR violations? Have you analyzed whether the set of DR-violating triples under grammar-only overlaps with the unconstrained set?
150	
151	**Q5.** Why is no post-hoc filtering baseline reported? The paper argues against post-hoc filtering in the introduction but never empirically compares against it. A reject-and-regenerate baseline would clarify whether the decoding-time approach offers genuine advantages beyond computational efficiency.
152	
153	**Q6.** The CF analysis attributes 85% of SciERC CF violations to "type system ambiguity." How do you distinguish genuine ambiguity from method-induced errors? Is there human annotation to validate this claim?
154	
155	**Q7.** How sensitive are the results to the output JSON format? If the entity list were generated *after* relations (or interleaved), would the semantic layer's entity registry mechanism still work?
156	
157	---
158	
159	## 7. Minor Issues
160	
161	- M1: The latency overhead numbers are inconsistent across drafts (14% vs 23% vs 37% vs 62% for various configurations). These need to be reconciled into a single coherent set.
162	- M2: Table 4 in paper_tables_draft.tex has "TBD" entries for DocRED S1, suggesting the paper is not yet complete.
163	- M3: The bib file has cite key naming issues (e.g., `synchromesh_neurips2022` is actually ICLR 2022; `roth_yih_2004` suggests AAAI but is CoNLL at HLT-NAACL).
164	- M4: The `zhou2026snowballing` reference has a "PENDING AUDIT" comment in the extended related work, suggesting unverified citations.
165	- M5: The "Conjunction" relation in SciERC has 0% DR both before and after constraints — including it in the ablation table adds noise without information.
166	- M6: No confidence intervals, bootstrap estimates, or significance tests are reported for the main DR reduction numbers. The paper correctly notes F1 differences are not significant but does not apply the same rigor to violation rate differences.
167	- M7: The paper should report wall-clock times for the full pipeline (compilation + inference), not just per-token overhead, since compilation cost matters for deployment.
168	
169	---
170	
171	## 8. Score and Justification
172	
173	**Score: 3 (Weak Reject)**
174	
175	**Justification:**
176	
177	The paper addresses a real and practical problem — LLM-based IE systems do produce ontology violations, and constrained decoding is a reasonable approach. The honest presentation of negative results (DocRED degradation, CF trade-off) is commendable.
178	
179	However, the paper falls short of the acceptance bar for a top ML venue for several reasons:
180	
181	1. **Novelty is insufficient.** The grammar layer is engineering; the semantic layer transfers an existing idea (type-constrained decoding) from code generation to IE with modest technical delta; the landscape study is descriptive but shallow.
182	
183	2. **Experimental scope is narrow.** Two datasets, one primary model, zero-shot only. The DocRED results are weak and internally inconsistent across drafts.
184	
185	3. **The CF trade-off undermines the core value proposition.** Eliminating one violation type while introducing another is a net unclear benefit without downstream evaluation.
186	
187	4. **Related work coverage is thin** in the main paper drafts (7-13 references), missing important prior work on structured prediction for IE, joint extraction models, and alternative constrained decoding methods.
188	
189	5. **No downstream evaluation.** The practical motivation (KG quality, reasoning, compliance) is never empirically validated.
190	
191	The paper could be strengthened by: (a) committing to either a thorough empirical study (more models, datasets, settings) OR a method paper with downstream evaluation; (b) addressing CF violations with a concrete solution rather than just analysis; (c) including post-hoc filtering and few-shot baselines; (d) expanding related work significantly.
192	
193	As currently positioned, the paper is a competent technical report that would be appropriate for a workshop or a systems/demo track, but does not meet the novelty and significance bar for a main conference paper at a top ML/NLP venue.
194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee08938e-f221-495b-bf8e-e78f4faac6a4",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "e2ca9abb-6f3b-4b05-bc40-cedb7d0a0727",
  "sourceToolAssistantUUID": "ee08938e-f221-495b-bf8e-e78f4faac6a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-14T21:27:48.465Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gaje9G47nM7dcoKLK5xEzG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2ca9abb-6f3b-4b05-bc40-cedb7d0a0727",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AqTteLyfsMDKKo7rNf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9114d511-6018-4552-98da-ccd06421fb1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeqX6jozVCwZHCN162bP1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2880,
      "cache_read_input_tokens": 80330,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2880
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 80330,
          "cache_creation_input_tokens": 2880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2880,
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

_source line 63 · 2026-05-14T21:27:48.498Z_

<details><summary>↩ Tool result · `toolu_01Gaje9G47nM7dcoKLK5xEzG`</summary>

```text
1	---
2	dream_id: dream_20260514T094226
3	tier: median
4	overall_score: weak reject
5	timestamp: 2026-05-14T10:57:37.487832+00:00
6	---
7	
8	# Dream Review Report: Type-Valid IE via Compiled Ontology Constraints
9	
10	**dream_id:** 20260514T094226 | **review_mode:** full | **date:** 2026-05-14
11	
12	---
13	
14	## Roundtable Summary
15	
16	Two reviewers conducted independent reviews, then cross-shared findings and converged through discussion.
17	
18	- **R1** (Methods + Experiments): **4/6 Weak Accept**, Confidence 4/5
19	- **R2** (Novelty + Related Work): **3/6 Weak Reject**, Confidence 4/5
20	- **Converged Score: 3/6 (Weak Reject)**
21	
22	---
23	
24	## Step 1: Independent Reviews
25	
26	### R1 — Methods & Experiments
27	
28	**Methods assessment:**
29	The two-layer grammar+semantic architecture is well-motivated by the decidability taxonomy (purely local / prefix-decidable / truly non-local). Layer composition via bitwise AND with graceful fallback (grammar-only when semantic mask empties all grammar-valid tokens) is correctly designed. The enabling dependency is the most interesting methodological claim, convincingly quantified via the enabling ratio (3.9× SciERC, 1.6× DocRED).
30	
31	Technical gaps: (1) The semantic layer's position detection mechanism (how it identifies when it is at a subject-type vs. object-type token position) is underspecified. (2) Hidden dependency on output ordering (entities must precede relations for the registry to work) is not discussed as a constraint on prompt design. (3) No discussion of behavior under non-greedy decoding (beam search, sampling).
32	
33	**Experiments assessment:**
34	- The 5-configuration ablation (unconstrained / grammar_only / semantic_only / full_s1 / full_s2) is clean and sufficient for decomposing each layer's contribution.
35	- Grammar layer's perfect generalization (ET/RV→0% on both datasets) is the cleanest result in the paper.
36	- SciERC evidence is strong: 94% DR reduction, F1-neutral, clear per-relation gradient.
37	- DocRED evidence is honest but attenuated: 46% DR reduction, 10.2% residual.
38	- The grammar_only DR increase on DocRED (18.7%→26.2%) is correctly explained as a denominator effect — the paper handles this well.
39	- Tightness-DR Spearman correlation (ρ=0.82 SciERC, ρ=0.37 DocRED) is appropriate. The low R² on DocRED (~14%) is acknowledged.
40	- CF analysis (Tables 7-8) with ambiguity vs. systematic error classification is thorough.
41	- Latency analysis (Table 9) is adequate — ~62% overhead for S1 is reasonable.
42	
43	**Critical concerns:**
44	1. No statistical significance testing — all results are single-seed, single-run, no bootstrap CIs. F1-neutrality (+0.13pp) is claimed without statistical backing on ~1700 triples.
45	2. Cross-model validation (Llama-3.1-8B) is missing entirely. The "model-agnostic" claim rests on N=1 model.
46	3. Missing baselines: no post-hoc filtering comparison (reject-and-regenerate), no comparison to PICARD-style incremental parsing, no few-shot evaluation.
47	4. The CF trade-off partially offsets DR gains: on SciERC, DR drops 14.5pp but CF rises 9.8pp. Net violation reduction is real but less dramatic than headline numbers suggest.
48	
49	**R1 Strengths:**
50	- Clean ablation design cleanly isolates each layer's contribution
51	- Grammar layer perfect generalization is a strong, unambiguous result
52	- Tightness-DR analysis transforms DocRED's weaker results into an analytical contribution
53	- Honest CF disclosure with root-cause analysis (ambiguity vs. systematic)
54	- DocRED denominator effect correctly explained
55	- Latency overhead (~62%) is practical
56	
57	**R1 Weaknesses:**
58	- Single model, single seed, no significance testing
59	- Missing cross-model validation undermines generalization claims
60	- No post-hoc filtering baseline for cost comparison
61	- Semantic layer position detection mechanism underspecified
62	- No few-shot or fine-tuned evaluation (violation landscape may differ substantially)
63	
64	---
65	
66	### R2 — Novelty & Related Work
67	
68	**Novelty assessment:**
69	- **Core idea (compiling ontology schemas into constrained decoding):** A natural migration of techniques well-established in code generation (Synchromesh, PICARD, GCD) to the IE domain. IE ontology constraints (flat domain/range sets over a small type inventory) are structurally simpler than programming language type systems. The transfer is largely straightforward.
70	- **Two-layer decomposition:** The grammar layer is an application of XGrammar to an IE-specific JSON schema. The semantic layer is a standard HuggingFace LogitsProcessor maintaining a dictionary with set membership lookup. Composition via bitwise AND is the obvious design. This is competent engineering, not a design innovation.
71	- **Violation landscape study (§3):** This is the paper's most novel contribution. No prior work has systematically measured per-relation distribution of ontology constraint violations in LLM-based IE or established the tightness-violation correlation. The finding that violation rates are driven by constraint tightness rather than ontology size is a genuine insight. The Evaluate-for regression under schema-informed prompting (+5.8pp) is a compelling finding.
72	- **Enabling dependency:** An empirical observation, not a design innovation. The fact that valid relation types are needed before domain/range lookup is architecturally self-evident. Quantifying the ratio (3.9× vs 1.6×) adds empirical substance but not methodological novelty.
73	- **Decidability taxonomy:** A straightforward classification that follows directly from the problem structure. Similar taxonomies exist in constrained code generation literature.
74	
75	**Related work assessment:**
76	Coverage is generally adequate but has significant gaps:
77	1. **PICARD (Scholak et al., EMNLP 2021)** — most significant omission. PICARD maintains cross-field state during SQL decoding to enforce column-type compatibility, a direct methodological parallel to OntoCoDec's entity registry. The paper cites PICARD but does not discuss the methodological similarity.
78	2. **SynCode (Ugare et al., 2024)** — grammar-augmented generation with semantic actions, directly comparable to the grammar+semantic layering.
79	3. **REBEL (Cabot & Navigli, 2021), TANL (Paolini et al., 2021)** — end-to-end RE models that implicitly learn type constraints through training. The question of whether fine-tuned models already achieve low violation rates (making decoding-time enforcement unnecessary) is unaddressed.
80	4. **Type-constrained KG embedding methods** — type constraint enforcement has been studied extensively in KG completion literature. The paper's novelty claim should be scoped to "LLM-based generative IE."
81	
82	**Positioning against GoLLIE:** Fair — correctly identifies complementarity. But critically missing: what are GoLLIE's violation rates? If fine-tuned models already achieve low DR, the motivation for decoding-time enforcement weakens.
83	
84	**Overclaiming concerns:**
85	- "First systematic quantification" should be scoped to LLM-based generative IE specifically
86	- The decidability taxonomy is presented as a contribution but is a straightforward classification
87	
88	**R2 Strengths:**
89	- Violation landscape study has independent empirical value
90	- Schema-informed prompting regression is a compelling motivation
91	- Grammar layer generalization is clean and unambiguous
92	- Proactive CF disclosure shows intellectual honesty
93	- Paper correctly positions OntoCoDec as complementary to training-based approaches
94	
95	**R2 Weaknesses:**
96	- Limited technical novelty of the framework — competent engineering integration of known techniques (XGrammar + LogitsProcessor + bitwise AND), not a research advance in constrained decoding methodology
97	- DocRED results (46% DR, 10.2% residual) undermine headline claims; the method leaves substantial violations unaddressed on realistic ontologies
98	- CF trade-off shifts violation burden rather than eliminating it; no downstream task evaluation to substantiate the hard/soft severity distinction
99	- ~8% relation F1 raises practical relevance concerns — ~92% of extracted triples are factually wrong regardless of type validity. The paper does not address this.
100	- PICARD omission is a notable related work gap for a methodologically close predecessor
101	- Narrow experimental scope: 1 model, 2 datasets, zero-shot only
102	
103	---
104	
105	## Step 2: Cross-Sharing
106	
107	**R1 response to R2's novelty concerns:**
108	R1 acknowledges that the framework components are individually known techniques, but argues that the systematic integration for IE ontology constraints — particularly the empirical discovery of the enabling dependency and its variation with ontology complexity — constitutes a meaningful systems contribution. The violation landscape study is independently valuable. However, R1 concedes that the technical novelty bar for a top venue main track is borderline.
109	
110	**R2 response to R1's experiment concerns:**
111	R2 agrees that the experimental design (5-configuration ablation) is clean, but emphasizes that experimental thoroughness cannot compensate for limited technical novelty. R2 also adopts R1's concern about missing statistical significance testing as reinforcing the "incomplete work" assessment.
112	
113	**R1 adopts R2's point on ~8% F1:**
114	R1 agrees this is an elephant in the room. The paper explicitly states F1 is for verification not SOTA claims, and argues constrained decoding is orthogonal to model quality — but the practical value proposition is weakened when the vast majority of extractions are wrong regardless of type validity. A brief discussion of how constraint enforcement interacts with model quality (does it help more or less as F1 improves?) would strengthen the paper.
115	
116	**R2 adopts R1's point on CF net effect:**
117	R2 agrees the net violation analysis (DR↓14.5pp vs CF↑9.8pp on SciERC) is important context. The paper's distinction between hard (DR) and soft (CF) violations is reasonable in principle but unvalidated empirically.
118	
119	---
120	
121	## Step 3: Convergence
122	
123	### Areas of Agreement
124	
125	1. **Violation landscape study (§3) is the paper's strongest and most novel contribution.** Both reviewers consider this independently valuable: the per-relation violation distribution, constraint tightness correlation, and prompt-intervention regression are genuine findings.
126	
127	2. **Grammar layer's perfect generalization (ET/RV→0%) is a clean, strong result.** Unambiguous, generalizes across both datasets, and represents a guaranteed structural compliance floor.
128	
129	3. **CF trade-off is a real concern.** The shift from DR violations to CF violations partially offsets gains. The hard/soft severity argument is reasonable but not empirically validated through downstream tasks.
130	
131	4. **Cross-model validation is a significant gap.** The "model-agnostic" claim on N=1 model is weak. This is the most actionable improvement for a revision.
132	
133	5. **Statistical rigor is lacking.** Single seed, single run, no confidence intervals. F1-neutrality claims need statistical backing.
134	
135	6. **DocRED results are honest but attenuated.** The paper handles this well (framing as "stress test," explaining via loose ontology structure), but 46% DR reduction with 10.2% residual limits the practical impact claim.
136	
137	### Areas of Divergence
138	
139	1. **Novelty threshold** — the primary disagreement. R1 considers the empirical contributions + engineering integration sufficient for a borderline accept (4/6). R2 considers the framework's technical novelty below the bar for a top venue main track (3/6). After cross-sharing, R1 moves closer to R2's position, acknowledging the borderline nature.
140	
141	2. **Practical relevance of ~8% F1 setting.** R2 considers this a fundamental concern; R1 considers it contextually appropriate (zero-shot setting explicitly chosen, constrained decoding is orthogonal to model quality). The converged view: the paper should explicitly discuss how constraint value scales with model quality, even if only as a discussion point.
142	
143	3. **PICARD significance.** R2 considers this a major omission; R1 considers it one of several missing baselines. Converged view: PICARD is the most methodologically relevant omission and should be discussed.
144	
145	### Converged Score Rationale
146	
147	The reviewers converge on **3/6 (Weak Reject)** for the following reasons:
148	
149	**For acceptance:**
150	- Violation landscape study is a genuine empirical contribution
151	- Grammar layer generalization is a clean, strong result
152	- Ablation design is thorough and well-executed
153	- Honest treatment of limitations (DocRED degradation, CF trade-off)
154	
155	**Against acceptance (decisive):**
156	- Framework technical novelty is below the bar — straightforward integration of XGrammar + LogitsProcessor, transferring a simpler version of what already exists in code generation (GCD, PICARD)
157	- DocRED results show the method leaves substantial violations on realistic ontologies
158	- Single model undermines generalization claims
159	- CF trade-off partially offsets gains without downstream validation
160	- ~8% F1 practical relevance concern is unaddressed
161	- Missing statistical rigor
162	
163	The violation landscape study alone would be a solid workshop or findings-track contribution. The framework, while competently engineered, does not introduce sufficient methodological novelty for a top venue main track at ~25% acceptance rate.
164	
165	---
166	
167	## Step 4: Final Consolidated Assessment
168	
169	### Overall Score: 3/6 (Weak Reject)
170	
171	### Recommendation
172	Below acceptance threshold for a top ML venue main track. The violation landscape study is the paper's strongest contribution and could stand alone as a findings/short paper. The framework is competent engineering but the technical novelty (applying known constrained decoding techniques to a simpler constraint structure than existing work handles) does not clear the bar. A revision addressing cross-model validation, statistical significance, the PICARD comparison, and downstream CF impact evaluation could strengthen the paper to borderline-accept territory.
173	
174	### Actionable Revision Suggestions (Priority Order)
175	
176	1. **Cross-model validation** — run Llama-3.1-8B on SciERC (estimated 3h GPU). This is the single highest-impact improvement.
177	2. **Statistical significance** — bootstrap CIs on F1 and DR metrics, or at minimum 3 seeds with std.
178	3. **PICARD discussion** — explicitly compare the semantic layer's entity registry to PICARD's incremental parsing state, articulate what (if anything) is new.
179	4. **Post-hoc filtering baseline** — compare OntoCoDec's 62% latency overhead to reject-and-regenerate with an unconstrained model.
180	5. **GoLLIE violation rates** — measure DR/RV/ET/CF for a fine-tuned IE model to establish whether decoding-time enforcement provides value on top of training.
181	6. **~8% F1 discussion** — explicitly address the practical relevance of type-valid but factually incorrect extractions. Discuss how constraint value may scale with model quality improvement.
182	7. **CF downstream impact** — even a small-scale experiment showing that CF violations are less harmful than DR violations to a downstream consumer (KG population, QA) would substantiate the hard/soft distinction.
183	
184	### Experiment Coverage vs. Plan
185	
186	| Planned Experiment | Status in Paper | Assessment |
187	|---|---|---|
188	| DocRED Unconstrained Baseline | Covered (Table 5) | Adequate |
189	| DocRED Semantic-only | Covered (Table 5) | Adequate |
190	| Per-relation DR + Tightness Spearman | Covered (Tables 2-3, §3.3-3.4) | Well-done |
191	| CF Composition Deep Dive | Covered (Tables 7-8, §5.5) | Thorough |
192	| Latency Comparison | Covered (Table 9, §5.6) | Adequate |
193	| Cross-model (Llama-3.1-8B) | **NOT completed** | Significant gap |
194	
195	5 of 6 planned experiments are covered. The missing cross-model validation is the most impactful gap for the paper's generalization claims.
196	
197	### Key Questions for Authors
198	
199	1. How does the semantic layer's entity registry differ technically from PICARD's incremental parsing state for SQL? What is the algorithmic contribution beyond domain transfer?
200	2. What are the violation rates for a fine-tuned IE model (GoLLIE, InstructUIE) on SciERC/DocRED? If fine-tuning already reduces DR substantially, what is the marginal value of decoding-time enforcement?
201	3. The ~8% R-F1 means ~92% of triples are factually wrong. In what practical scenario does type-valid but factually incorrect extraction provide value?
202	4. On SciERC, DR drops 14.5pp but CF rises 9.8pp. Have you measured the net impact on any downstream task?
203	5. All results use greedy decoding. How does the system behave under beam search or nucleus sampling?
204	6. The paper claims "model-agnostic by design" on N=1 model. Can you provide even preliminary Llama results to support this claim?
205	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9114d511-6018-4552-98da-ccd06421fb1e",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "d314cabb-aa45-4e2f-920f-30bf822ee9b2",
  "sourceToolAssistantUUID": "9114d511-6018-4552-98da-ccd06421fb1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-14T21:27:52.954Z_

I now have a thorough understanding of the paper, its contributions, the prior dream review feedback, and how the paper has evolved since that feedback. Let me now write my review as R2 focusing on novelty and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d314cabb-aa45-4e2f-920f-30bf822ee9b2",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AqjZDys7rTeFbmNb14",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee446880-c6ef-47f6-a969-09864e67388a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E97F9oPRY3QNZf3dxBHVnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9909,
      "cache_read_input_tokens": 83210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9909,
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

_source line 65 · 2026-05-14T21:27:53.448Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019EPzJb9hYwPjBcumoJyyD8`</summary>

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
  "parentUuid": "ee446880-c6ef-47f6-a969-09864e67388a",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3AqjZDys7rTeFbmNb14",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "194c4a01-6f83-4291-a7af-4a6bfe76f554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E97F9oPRY3QNZf3dxBHVnM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9909,
      "cache_read_input_tokens": 83210,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 83210,
          "cache_creation_input_tokens": 9909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9909,
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

_source line 66 · 2026-05-14T21:27:53.451Z_

<details><summary>↩ Tool result · `toolu_019EPzJb9hYwPjBcumoJyyD8`</summary>

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
  "parentUuid": "194c4a01-6f83-4291-a7af-4a6bfe76f554",
  "isSidechain": true,
  "promptId": "fa0f5a78-4f5f-41ab-b0ab-139961a66534",
  "agentId": "a9e8704ac8b240d35",
  "type": "user",
  "uuid": "3713df0d-32e0-43be-afb0-52e81ec933ab",
  "sourceToolAssistantUUID": "194c4a01-6f83-4291-a7af-4a6bfe76f554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-14T21:29:28.120Z_



Now I have all the information needed to write a thorough R2 review. Let me compose it.

---

## Reviewer 2 (R2): Novelty, Positioning, and Related Work

### 1. Summary

OntoCoDec compiles IE ontology schemas into two composable decoding constraint layers -- a grammar layer (XGrammar CFG for JSON structure and vocabulary membership) and a semantic layer (stateful entity registry with dynamic logit masking for domain/range constraints) -- to enforce type validity during autoregressive generation. The paper additionally contributes a violation landscape study across SciERC and DocRED showing 15-19% domain/range violation rates driven by constraint tightness, and a decidability taxonomy classifying constraint types by amenability to left-to-right enforcement. Results on a 2x2 matrix (2 models, 2 datasets) show 44.7-99.4% DR reduction with F1 neutral-to-positive impact.

### 2. Strengths

**S1: The violation landscape study is a genuine empirical contribution.** To my knowledge, no prior work has systematically characterized per-relation ontology constraint violation distributions in LLM-based IE. The finding that violation rates correlate with constraint tightness rather than ontology size (SciERC 7 relations at 15.4% DR vs. DocRED 96 relations at 18.5% DR) is a useful and non-obvious empirical insight. The Evaluate-for regression under schema-informed prompting (+5.8pp) is a particularly compelling finding that strengthens the motivation for decoding-time enforcement.

**S2: The related work section has been substantially expanded since the earlier draft.** The current version covers six well-organized paradigms with approximately 42 references: grammar-constrained decoding (XGrammar, Outlines, LMQL, DOMINO, ASAp), semantic constrained decoding for code (PICARD, Synchromesh, MGD, PLDI'25), vocabulary/type-constrained generation (Roth & Yih 2004, GENRE, GenIE, AdaKGC, GCD, NeuroLogic), structural constraints via training (UIE, GoLLIE, KnowCoder, CodeIE, ADELIE, SpERT, PFN, EnriCo), post-hoc ontology validation (ODKE+, SPIRES, OntoLogX, RELATE, ontology-to-tools, ontology beam scoring), and quality impact of constrained decoding (CRANE, Let Me Speak Freely, Hidden Cost, Structure Snowballing). This is thorough coverage for EMNLP.

**S3: The PICARD differentiation is well-articulated.** The paper correctly identifies PICARD as the closest mechanistic analog in a different domain and provides a clean technical distinction: PICARD operates over a fixed, fully enumerated schema (database columns known before decoding), whereas OntoCoDec's entity registry is populated during generation from free-text spans. This is a genuine and important difference.

**S4: Honest positioning of limitations.** The paper does not oversell. The title change from "Guaranteed" to "Near-Complete" is appropriate. The CF trade-off is disclosed proactively with ablation evidence cleanly attributing it to the semantic layer. The dual-factor model (tightness x RV baseline) explaining cross-model DR reduction variance is more insightful than a simple tightness-only narrative.

**S5: Cross-model validation addresses a critical gap from the earlier draft.** The 2x2 matrix (Qwen3-8B + Llama-3.1-8B x SciERC + DocRED) with zero code modification is a meaningful demonstration of model-agnostic design. The finding that Llama achieves 90.2% DR reduction on DocRED (where Qwen achieves only 44.7%) due to lower baseline RV is a genuinely interesting empirical observation that deepens the analysis.

**S6: The post-hoc filtering comparison is now included with multi-dimensional analysis.** The 48.1% triple rejection rate on DocRED and 127 lost true positives provide concrete evidence for the information-loss argument against post-hoc approaches.

### 3. Weaknesses

**W1 (Major): The core technical contribution -- extending grammar-constrained decoding with a stateful semantic layer -- has limited novelty.** The paper's own related work section acknowledges that type-constrained decoding with stateful monitors exists in code generation (Synchromesh ICLR'22, MGD NeurIPS'23, PLDI'25 type systems to prefix automata). The transfer to IE involves a structurally *simpler* constraint system: flat domain/range sets over a small entity type inventory (6 types in both SciERC and DocRED) versus deep subtyping hierarchies and parametric polymorphism in programming languages. The "new challenge" of inferring entity types from free text is handled by recording types from the entity list -- a dictionary lookup, not a novel inference mechanism. The composition via bitwise AND is the standard approach. While the paper argues that the IE domain introduces unique challenges (entity types inferred from free text rather than declared), the actual implementation of the entity registry is straightforward. The novelty bar for EMNLP requires more than competent domain transfer of known techniques to a simpler setting.

**W2 (Major): The decidability taxonomy (local / prefix-decidable / non-local) is presented as a contribution but offers limited conceptual depth.** This classification follows directly from the well-known properties of autoregressive left-to-right generation: some constraints depend only on the current position, some on the prefix, and some on future tokens. Similar taxonomies appear implicitly or explicitly in the constrained decoding literature for code (Synchromesh's "target constraint decoding" framework, MGD's "static analysis monitors"). The paper would benefit from either (a) formalizing this taxonomy more rigorously (e.g., relating it to formal language theory hierarchies -- which constraint classes correspond to regular, context-free, context-sensitive languages?) or (b) honestly positioning it as a useful organizational framework rather than a standalone contribution.

**W3 (Moderate): CRANE is cited but not empirically compared.** CRANE (Banerjee et al., ICML 2025) proposes constrained re-generation as an alternative to both post-hoc filtering and single-pass constrained decoding. The paper cites CRANE in the quality-impact paragraph and even notes that S2's two-pass strategy is "analogous to CRANE's alternating strategy," but does not compare against CRANE's actual constrained re-generation approach. Since the paper argues against post-hoc filtering, and CRANE occupies the space between post-hoc filtering and decoding-time enforcement, this comparison gap is notable.

**W4 (Moderate): Missing connections to the neuro-symbolic and structured prediction literature.** The paper frames the problem entirely within the constrained decoding paradigm but does not engage with:
- The broader neuro-symbolic integration literature, where enforcing logical constraints on neural outputs is a central theme (e.g., DeepProbLog, Semantic Loss, Logic Tensor Networks). OntoCoDec's approach of compiling declarative constraints into procedural enforcement is a specific instance of this broader research direction.
- Structured prediction with constraints (beyond Roth & Yih 2004), including constrained conditional models, Markov logic networks for IE, and posterior regularization approaches that enforce constraints during learning rather than decoding.
- The distinction between "hard" vs. "soft" constraint enforcement and the rich literature on when each is appropriate. The paper's grammar-first fallback is effectively a soft-constraint relaxation, but this is not connected to the formal literature on constraint relaxation.

**W5 (Moderate): The "enabling dependency" is presented with more weight than warranted.** That grammar must validate relation names before the semantic layer can look up domain/range rules is an architectural consequence of the system design (the semantic layer indexes constraints by relation name), not a deep insight about constraint composition. The empirical quantification (semantic-only achieves 24% DR reduction vs. full 94%) is useful but the finding is architecturally self-evident: if the semantic layer cannot identify the relation, it cannot enforce relation-specific constraints. Framing this as the "enabling dependency" and listing it as part of Contribution 3 inflates its significance.

**W6 (Minor): No engagement with type systems in NLP beyond the code generation domain.** Recent work on type-theoretic approaches to natural language semantics (e.g., Montague grammar, CCG type-logical grammars, type-driven incremental semantic parsing) is relevant to the general question of enforcing type constraints during language processing. While this literature operates at a different level of abstraction, acknowledging it would strengthen the paper's theoretical positioning.

**W7 (Minor): The "first systematic study" claim should be scoped more carefully.** The paper claims "the first systematic quantification of ontology constraint violations in LLM-based IE." This is likely true for the specific framing (per-relation DR distribution in zero-shot LLM IE), but error analysis and constraint violation measurement in IE systems more broadly is not new. The claim should explicitly scope to "LLM-based generative IE in the zero-shot setting" to avoid overstating.

### 4. Questions to Authors

**Q1.** The PLDI'25 type-constrained code generation system compiles "full type systems -- including generic types and subtyping -- into prefix automata for token-level logits masking." Your system compiles flat domain/range sets into logit masks. Beyond the domain difference (code vs. IE), what is the algorithmic or conceptual contribution that distinguishes OntoCoDec from applying the PLDI'25 approach to a simpler constraint structure? Is there a technical challenge in IE that required a novel solution beyond what exists in the code generation literature?

**Q2.** EnriCo (Zaratiana et al., 2024) applies ASP constraints during decoding for joint entity-relation extraction. How does OntoCoDec's approach differ from EnriCo beyond the formalism (logit masking vs. ASP)? EnriCo also enforces type compatibility at generation time -- is the claim of "first" scoped to exclude this work?

**Q3.** The entity registry is populated from the entity list that precedes relations in the JSON output. What happens if the model generates an entity in a relation that was not in the entity list? How does the system handle entity mentions with no registry entry? This seems like a fundamental ordering dependency that should be discussed as a constraint on the approach.

**Q4.** Have you considered whether the violation landscape findings generalize beyond zero-shot settings? If fine-tuned models (e.g., GoLLIE, KnowCoder) already achieve low DR rates, the practical motivation for decoding-time enforcement weakens substantially. Even a brief measurement of violation rates for a fine-tuned model would address this concern.

**Q5.** The constraint tightness formula uses observed valid type pairs |V(r)| rather than the Cartesian product |dom(r)| x |range(r)|. The paper notes these can differ (e.g., Used-for has 35/36 observed pairs vs. 36 Cartesian). How sensitive are the tightness-DR correlations to this choice? Would using the Cartesian product change the story?

### 5. Minor Issues

**M1.** The bibliography contains a few cite key inaccuracies (e.g., `roth_yih_2004` suggests AAAI but the actual venue is CoNLL-2004 at HLT-NAACL; `synchromesh_iclr2022` was previously keyed as NeurIPS). While the actual entries are correct, these could cause confusion.

**M2.** The paper does not cite TANL (Paolini et al., ICLR 2021) or REBEL (Cabot & Navigli, EMNLP 2021), both of which are prominent end-to-end RE models that generate structured triples autoregressively and implicitly handle type constraints through training. These are relevant comparisons in the "structural constraints via training" paragraph.

**M3.** The "Our Approach" summary paragraph at the end of the related work repeats the same DR reduction numbers already given in the abstract and introduction. This space would be better used to sharpen the positioning rather than repeating results.

**M4.** The paper does not discuss behavior under non-greedy decoding (beam search, nucleus sampling). Since grammar-constrained decoding interacts differently with beam search than with greedy decoding (mask intersection over beams), this should at least be acknowledged.

**M5.** The constraint tightness measure (Eq. 5) is defined using observed type pairs rather than ontology-permitted pairs. This conflates the ontology's formal constraints with the dataset's empirical distribution. A cleaner formulation would separate the two.

**M6.** SynCode (Ugare et al., 2024), which combines grammar constraints with semantic actions during generation, is absent from the related work despite being directly relevant to the grammar+semantic layering architecture.

### 6. Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 4 (Strong) | The experimental design is thorough (5-way ablation, 2x2 cross-model matrix, bootstrap CIs, post-hoc comparison). Claims are appropriately calibrated. The CF trade-off is honestly reported with clean ablation evidence. The dual-factor model is well-supported. Minor gap: no downstream task evaluation to validate the hard/soft violation severity distinction. |
| **Excitement** | 2 (Mediocre) | The violation landscape study is a useful empirical contribution, and the system works as described. However, the core technical idea -- extending grammar-constrained decoding with a stateful logits processor for cross-field constraints -- is a natural domain transfer of techniques already established in code generation (PICARD, Synchromesh, MGD, PLDI'25) to a structurally simpler constraint system. The decidability taxonomy restates known properties of autoregressive generation. The paper does not introduce a new algorithmic idea, formalism, or surprising finding that would excite the community. |
| **Overall** | 3 (Borderline) | The paper is well-executed and scientifically honest. The violation landscape study, the thorough ablation, the cross-model validation, and the dual-factor analysis are all positives. The related work has been substantially strengthened. However, the novelty of the constrained decoding framework itself is limited -- it is competent engineering that transfers known techniques to a simpler domain. For EMNLP main track, I would expect either a more novel technical contribution or a substantially broader empirical study (more models, domains, and settings). The paper is above the bar for Findings but borderline for the main conference. |
| **Confidence** | 4 (Quite sure) | I am familiar with the grammar-constrained decoding literature, type-constrained code generation, and IE methods. I have read the full paper including all sections and the bibliography. My main uncertainty is whether the community would weight the violation landscape study and the engineering contribution more favorably than I do. |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3713df0d-32e0-43be-afb0-52e81ec933ab",
  "isSidechain": true,
  "agentId": "a9e8704ac8b240d35",
  "requestId": "req_011Cb3Ar6qu3CXyfvzZQS9EV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f857104-0e87-44c5-9699-8adffe761512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "d100b6b0-1eb0-4d27-a3fa-08cfd6c31175",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrhSLwTr5EGMDvbv5Gpdz4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 93119,
      "output_tokens": 3557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3557,
          "cache_read_input_tokens": 93119,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 716,
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
