# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus is **novelty/originality** and **related work adequ

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 72
- **Recorded user turns:** 2
- **Tool calls:** 30
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-adceaffc762c94987.jsonl`
- **Structured JSON:** [`823abbfd50b0efea23e2.json`](../../sessions/82/823abbfd50b0efea23e2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

70 recorded events

### User

_source line 1 · 2026-05-22T06:34:48.112Z_

You are Reviewer 2 (R2) for an EMNLP 2026 ARR submission. Your focus is **novelty/originality** and **related work adequacy**. Review blindly — do not assume any outcome quality.

## Venue Calibration (EMNLP 2026 ARR)
- 5 = Award consideration (top 2.5%)
- 4 = Conference accept (~21% acceptance)
- 3 = Findings accept
- 2 = Major revision needed
- 1 = Do not resubmit

Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)

## Paper Summary

**Title:** OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints

**Core idea:** LLM-based IE systems systematically violate ontology type constraints (13-57% domain/range violations). OntoCoDec compiles ontology schemas into two composable constraint layers for autoregressive decoding: (1) grammar layer via CFG/XGrammar enforcing structural/vocabulary constraints, (2) semantic layer with stateful entity registry + dynamic logit masking for cross-field domain/range constraints. Layers compose via bitwise AND with graceful degradation to grammar-only when intersection is empty.

**Datasets:** SciERC (RE, 7 rel types, 551 test), DocRED (RE, 96 rel types, 998 test docs), WikiEvents (EE, 56 event types, 80 arg roles, 246 test docs)
**Models:** Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B (AWQ-INT4)

## Method Description (Section 2)

**Problem Formulation (2.1):** Ontology O = (E, R, C) with entity types, relation/event types, constraints. Next-token distribution masked: p(y_t|y<t, d) ∝ p_θ(y_t|y<t, d) · 1[y_t ∈ M(t, y<t)]

**Grammar Layer (2.2):** Compiles type vocabularies + JSON structure into CFG, enforced via XGrammar. Eliminates vocabulary violations and entity type violations. Cannot enforce context-dependent constraints.

**Semantic Layer (2.3):** Stateful entity registry R_t = {(e_i, τ_i)} tracking entity-to-type mappings during generation. Dynamic logit masking at type-token positions based on domain/range rules.

**Constraint Composition (2.4):** M(t, y<t) = M_G(t) ∩ M_S(t, y<t). Graceful degradation to grammar-only when intersection empty. Enabling dependency: grammar ensures valid relation types so semantic layer can look up rules. Decidability taxonomy: (a) local → grammar, (b) prefix-decidable with state → semantic, (c) truly non-local → out of scope.

## Related Work (Section 5)

Three subsections:
1. **Constrained Decoding for Structured Generation:** Willard & Louf 2023, XGrammar (Dong et al. 2024), CRANE (Li et al. 2024), Scholak et al. 2021 (PICARD), Poesia et al. 2022 (Synchromesh). Differentiation: OntoCoDec targets IE ontology constraints requiring cross-field state tracking.

2. **Structured IE with LLMs:** CodeIE (Li et al. 2023), GoLLIE (Sainz et al. 2024), general prompt-based approaches. Differentiation: these rely on prompting, not decoding-time constraint enforcement.

3. **Ontology-Aware IE:** Traditional systems (Li & Ji 2014, Wadden et al. 2019), recent prompt-based (Xu et al. 2023, Wadhwa et al. 2023). Claim: "first to compile ontology schemas directly into decoder constraints."

4. **Structure Snowballing:** Zhang et al. 2024. Addressed by fallback mechanism.

## Key Results (for context)

- ZS RE: DR reduction 44.9-99.4%, F1 neutral
- 70B: DR→0% (unique complete elimination)
- LoRA FT: R-F1 43-46%, near-zero violations
- EE: EV→0%, RoV→0% across all models; Arg F1≈0 in ZS but FT+OntoCoDec preserves Arg F1
- Post-hoc filtering non-viable for EE (99.6-100% rejection)
- Ablation: grammar-only can't eliminate RoV; semantic layer is sole defense
- Latency: 10-13% overhead, sub-linear ontology scaling

## Your Review Task

Produce a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Novelty Assessment** (score 1-5 with detailed justification):
   - How novel is the two-layer grammar+semantic approach? Is this "well-executed engineering over XGrammar" or a genuine conceptual advance?
   - Is the claim of "first systematic integration of ontology-aware semantic constraints with grammar-constrained decoding for IE" warranted?
   - What is the delta over simply using XGrammar for JSON schema + post-hoc validation?
   - How does this compare to CRANE's type-checking approach?
   - Is the "enabling dependency" insight (grammar enables semantic layer) a real contribution or obvious once stated?
   - Is the decidability taxonomy a contribution?
3. **Related Work Assessment**:
   - Are there missing key references? Consider:
     - SGLang constrained decoding (Zheng et al. 2024)
     - Guidance (Microsoft)
     - GENRE (De Cao et al. 2021) for constrained entity generation
     - UIE (Lu et al. 2022) unified IE
     - InstructUIE (Wang et al. 2023)
     - USM (Lou et al. 2023) or other unified schema methods
     - Any ontology-constrained generation work in knowledge graph completion
   - Is the positioning against prior work fair?
   - Does the paper adequately differentiate from prompt-based schema enforcement (GoLLIE)?
4. **Excitement** (score 1-5 with justification):
   - Would this work change how the community approaches IE?
   - Is the problem significant enough?
   - Are the results exciting or expected?
5. **Soundness** (score 1-5, brief — since R1 covers this in depth)
6. **Reproducibility** (score 1-5, brief)
7. **Weaknesses** (bulleted, specific, focus on novelty/positioning gaps)
8. **Questions for Authors** (3-5 specific questions)
9. **Overall Assessment** (score on ARR 1-5 scale with 0.5 increments, with justification)

Be rigorous but fair. Calibrate to EMNLP 2026 standards (~21% main acceptance).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "f6b2fafa-d5b6-4362-b158-5062eae6f256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T06:34:48.117Z_

```json
{
  "parentUuid": "f6b2fafa-d5b6-4362-b158-5062eae6f256",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
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
  "uuid": "829ed004-517e-4962-ae47-8abc23b9a309",
  "timestamp": "2026-05-22T06:34:48.117Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-22T06:34:50.780Z_



I'll start by reading the paper and related materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "829ed004-517e-4962-ae47-8abc23b9a309",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9DREb5KpteveNTWX5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a093c713-dc1a-4b9c-b488-85946abfb7c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zePriTAMWRTB9qLT2Ne2f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8311,
      "cache_read_input_tokens": 7333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8311,
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

_source line 4 · 2026-05-22T06:34:51.716Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QgKiTfKkpGrCcrS3uydEG2`</summary>

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
  "parentUuid": "a093c713-dc1a-4b9c-b488-85946abfb7c9",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9DREb5KpteveNTWX5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00e2a213-3c06-4071-8bcc-ca18c9add026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zePriTAMWRTB9qLT2Ne2f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8311,
      "cache_read_input_tokens": 7333,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8311
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 123,
          "cache_read_input_tokens": 7333,
          "cache_creation_input_tokens": 8311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8311,
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

_source line 5 · 2026-05-22T06:34:51.719Z_

<details><summary>↩ Tool result · `toolu_01QgKiTfKkpGrCcrS3uydEG2`</summary>

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
  "parentUuid": "00e2a213-3c06-4071-8bcc-ca18c9add026",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "8b853481-812d-4f03-99bc-16e1b6cacd0e",
  "sourceToolAssistantUUID": "00e2a213-3c06-4071-8bcc-ca18c9add026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T06:34:54.727Z_



Let me read the paper and supporting materials thoroughly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b853481-812d-4f03-99bc-16e1b6cacd0e",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9Dggmp7BdcQNVokQRt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bd2c882-8c16-408e-a05b-71614f7137e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQCSSp4PLWeJzXVdFUWjmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-22T06:34:55.618Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GeaAhzexodZ5VbqhfFkgHw`</summary>

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
  "parentUuid": "5bd2c882-8c16-408e-a05b-71614f7137e4",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9Dggmp7BdcQNVokQRt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b82bee9-6c95-40dd-bf8d-03e2aa5b978a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQCSSp4PLWeJzXVdFUWjmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 8 · 2026-05-22T06:34:55.641Z_

<details><summary>↩ Tool result · `toolu_01GeaAhzexodZ5VbqhfFkgHw`</summary>

```text
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
artifacts/_project/paper/section6_relwork_additions.tex
artifacts/_project/paper/discussion_paragraphs.tex
artifacts/dream_reports/dream_20260514T205155/best/paper.tex
artifacts/dream_reports/dream_20260514T205155/median/paper.tex
artifacts/dream_reports/dream_20260514T205155/worst/paper.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
artifacts/dream_reports/dream_20260516T021434/best/paper.tex
artifacts/dream_reports/dream_20260516T021434/median/paper.tex
artifacts/dream_reports/dream_20260516T021434/worst/paper.tex
artifacts/dream_reports/dream_20260516T173022/best/paper.tex
artifacts/dream_reports/dream_20260516T173022/median/paper.tex
artifacts/_project/paper/paper_tables_draft.tex
artifacts/appendix_sampling_table.tex
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/p3_case_studies.tex
artifacts/_project/paper/p3_case_studies_861a0d.tex
artifacts/p3_case_studies.tex
artifacts/dream_reports/dream_20260518T162745/best/paper.tex
artifacts/dream_reports/dream_20260518T162745/median/paper.tex
artifacts/dream_reports/dream_20260518T162745/worst/paper.tex
artifacts/_project/paper/appendix_full_ft.tex
artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/appendix_scalability.tex
artifacts/_project/paper/case_study_kappa_dr.tex
artifacts/figures/case_study_kappa_dr.tex
artifacts/d066_beam_sweep/beam_sweep_table.tex
artifacts/d066_beam_sweep/beam_docred_sweep_table.tex
artifacts/_project/paper/appendix_pumping_lemma.tex
artifacts/_project/paper/section2_background.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/_project/paper/appendix_related_work.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/section5_wikievents_draft.tex
artifacts/_project/paper/appendix_kappa_case_study.tex
artifacts/_project/paper/appendix_tcr.tex
artifacts/_project/paper/appendix_sampling_table.tex
artifacts/_project/paper/appendix_prompt_sensitivity.tex
artifacts/_project/paper/appendix_doc_length.tex
artifacts/_project/paper/appendix_case_studies.tex
artifacts/_project/paper/fig1_framework.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/_project/paper/checklist.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section7_conclusion_compressed.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_beam_search.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/appendix_reproducibility.tex
artifacts/_project/paper/section5_runtime.tex
artifacts/dream_reports/dream_20260522T052642/best/paper.tex
artifacts/dream_reports/dream_20260522T052642/median/paper.tex
artifacts/dream_reports/dream_20260522T052642/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b82bee9-6c95-40dd-bf8d-03e2aa5b978a",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "0970d385-7b3c-4394-9b13-86c8e409ff7d",
  "sourceToolAssistantUUID": "0b82bee9-6c95-40dd-bf8d-03e2aa5b978a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T06:34:56.045Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HyEMpD4x5ZjkSLtwt82Sdj`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0970d385-7b3c-4394-9b13-86c8e409ff7d",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9Dggmp7BdcQNVokQRt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58f2cb9c-20a8-4caf-afe3-e1a578eaa568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQCSSp4PLWeJzXVdFUWjmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 10 · 2026-05-22T06:34:56.067Z_

<details><summary>↩ Tool result · `toolu_01HyEMpD4x5ZjkSLtwt82Sdj`</summary>

```text
figures/paper/fig1_overview.pdf
artifacts/_project/chart/fig1_overview.pdf
figures/paper/fig2_per_relation_dr.pdf
artifacts/_project/chart/fig2_per_relation_dr.pdf
figures/paper/fig3_ablation_layers.pdf
artifacts/dream_reports/dream_20260514T094226/best/paper.pdf
artifacts/dream_reports/dream_20260514T094226/median/paper.pdf
artifacts/dream_reports/dream_20260514T094226/worst/paper.pdf
artifacts/dream_reports/dream_20260514T205155/best/paper.pdf
artifacts/_project/paper/figures/fig2_per_relation_dr.pdf
artifacts/dream_reports/dream_20260514T205155/median/paper.pdf
artifacts/dream_reports/dream_20260514T205155/worst/paper.pdf
artifacts/_project/chart/dual_factor_scatter.pdf
artifacts/_project/paper/figures/dual_factor_scatter.pdf
artifacts/dual_factor_analysis/dual_factor_scatter.pdf
artifacts/dream_reports/dream_20260516T021434/best/paper.pdf
artifacts/dream_reports/dream_20260516T021434/median/paper.pdf
artifacts/dream_reports/dream_20260516T021434/worst/paper.pdf
artifacts/dream_reports/dream_20260516T173022/best/paper.pdf
artifacts/dream_reports/dream_20260516T173022/median/paper.pdf
artifacts/dream_reports/dream_20260518T162745/best/paper.pdf
artifacts/dream_reports/dream_20260518T162745/median/paper.pdf
artifacts/dream_reports/dream_20260518T162745/worst/paper.pdf
artifacts/_project/paper/ontocodec_paper_r9_final.pdf
artifacts/ontocodec_paper_r9_final.pdf
artifacts/_project/paper/ontocodec_paper_r10_final.pdf
artifacts/ontocodec_paper_r10_final.pdf
artifacts/figures/scaling_analysis.pdf
artifacts/figures/kappa_vs_dr_scatter.pdf
artifacts/d066_beam_sweep/figures/beam_pareto.pdf
artifacts/d066/chart/beam_pareto.pdf
artifacts/d066_beam_sweep/beam_pareto.pdf
artifacts/d066_beam_sweep/chart/beam_pareto.pdf
artifacts/_project/paper/figures/beam_pareto.pdf
artifacts/_project/paper/figures/fig1_framework_v1_backup.pdf
artifacts/_project/paper/figures/fig1_framework.pdf
artifacts/_project/paper/main.pdf
artifacts/dream_reports/dream_20260522T052642/best/paper.pdf
artifacts/dream_reports/dream_20260522T052642/median/paper.pdf
artifacts/dream_reports/dream_20260522T052642/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58f2cb9c-20a8-4caf-afe3-e1a578eaa568",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "98ac2777-6f08-4526-a237-d3fb7b3bdf51",
  "sourceToolAssistantUUID": "58f2cb9c-20a8-4caf-afe3-e1a578eaa568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T06:34:57.050Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015J4W3xY6iV8Cvzwcpumrgv`</summary>

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
  "parentUuid": "98ac2777-6f08-4526-a237-d3fb7b3bdf51",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9Dggmp7BdcQNVokQRt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7ae6a21-8382-4de7-b05e-2749e06a6e7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQCSSp4PLWeJzXVdFUWjmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 12 · 2026-05-22T06:34:57.061Z_

<details><summary>↩ Tool result · `toolu_015J4W3xY6iV8Cvzwcpumrgv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T12:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"grammar_constrained\\\"\\n    name: \\\"Grammar-Constrained Decoding\\\"\\n    narrative: \\\"Token-level structural constraints via CFG/PDA for LLM generation\\\"\\n  - key: \\\"semantic_constrained\\\"\\n    name: \\\"Semantic-Aware Constrained Decoding\\\"\\n    narrative: \\\"Beyond grammar — enforcing semantic validity during generation\\\"\\n  - key: \\\"schema_ie\\\"\\n    name: \\\"Schema-Guided Information Extraction\\\"\\n    narrative: \\\"Leveraging ontology/schema to guide LLM-based IE\\\"\\n  - key: \\\"quality_impact\\\"\\n    name: \\\"Constraint Quality Impact Analysis\\\"\\n    narrative: \\\"Studies on how constrained decoding affects output quality\\\"\\n\\npapers:\\n  dong2025xgrammar:\\n    title: \\\"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\\\"\\n    authors: [\\\"Dong, Y.\\\"]\\n    year: 2025\\n    venue: \\\"MLSys\\\"\\n    url: \\\"https://arxiv.org/abs/2411.15100\\\"\\n    bibtex_key: \\\"dong2025xgrammar\\\"\\n    category: \\\"grammar_constrained\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Foundation of grammar constraint layer; XGrammar is directly used in OntoCoDec's Level 1 constraints\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  sainz2024gollie:\\n    title: \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction Modeling\\\"\\n    authors: [\\\"Sainz, O.\\\"]\\n    year: 2024\\n    venue: \\\"ICLR\\\"\\n    url: \\\"https://arxiv.org/abs/2310.03668\\\"\\n    bibtex_key: \\\"sainz2024gollie\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Schema-guided IE with LLMs via code-style guidelines; competing approach using prompt-level schema enforcement\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  scholak2021picard:\\n    title: \\\"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models\\\"\\n    authors: [\\\"Scholak, T.\\\", \\\"Schucher, N.\\\", \\\"Bahdanau, D.\\\"]\\n    year: 2021\\n    venue: \\\"EMNLP\\\"\\n    url: \\\"https://arxiv.org/abs/2109.05093\\\"\\n    bibtex_key: \\\"scholak2021picard\\\"\\n    category: \\\"semantic_constrained\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Semantic constrained decoding for SQL; closest methodological parallel — incremental parsing with semantic validity checks\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  geng2023gcd:\\n    title: \\\"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\\\"\\n    authors: [\\\"Geng, S.\\\"]\\n    year: 2023\\n    venue: \\\"EMNLP\\\"\\n    url: \\\"https://arxiv.org/abs/2305.13971\\\"\\n    bibtex_key: \\\"geng2023gcd\\\"\\n    category: \\\"grammar_constrained\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Grammar-constrained decoding applied to NLP tasks; directly comparable zero-shot approach\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  sakota2025boostcd:\\n    title: \\\"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction\\\"\\n    authors: [\\\"Sakota, M.\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    url: \\\"https://arxiv.org/abs/2506.14901\\\"\\n    bibtex_key: \\\"sakota2025boostcd\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Most direct competitor — constrained decoding for IE with quality-constraint tradeoff analysis\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  li2024knowcoder:\\n    title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\"\\n    authors: [\\\"Li, Z.\\\"]\\n    year: 2024\\n    venue: \\\"ACL\\\"\\n    url: \\\"https://arxiv.org/abs/2403.07969\\\"\\n    bibtex_key: \\\"li2024knowcoder\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Schema-aware IE via code representation; encodes ontology into code structure for universal IE\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  ugare2025itergen:\\n    title: \\\"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking\\\"\\n    authors: [\\\"Ugare, S.\\\"]\\n    year: 2025\\n    venue: \\\"ICLR\\\"\\n    url: \\\"https://arxiv.org/abs/2410.07295\\\"\\n    bibtex_key: \\\"ugare2025itergen\\\"\\n    category: \\\"semantic_constrained\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Semantic-aware structured generation with backtracking; addresses same problem of grammar insufficiency for semantic constraints\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  josifoski2022genie:\\n    title: \\\"GenIE: Generative Information Extraction\\\"\\n    authors: [\\\"Josifoski, M.\\\"]\\n    year: 2022\\n    venue: \\\"NAACL\\\"\\n    url: \\\"https://arxiv.org/abs/2112.08340\\\"\\n    bibtex_key: \\\"josifoski2022genie\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Generative IE with trie-based prefix constrained decoding; early work on constraint-guided IE generation\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  li2023codeie:\\n    title: \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\"\\n    authors: [\\\"Li, P.\\\"]\\n    year: 2023\\n    venue: \\\"ACL\\\"\\n    url: \\\"https://arxiv.org/abs/2305.05711\\\"\\n    bibtex_key: \\\"li2023codeie\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Code generation approach to IE; leverages code structure for implicit schema compliance\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  banerjee2025crane:\\n    title: \\\"CRANE: Reasoning with Constrained LLM Generation\\\"\\n    authors: [\\\"Banerjee, P.\\\"]\\n    year: 2025\\n    venue: \\\"ICML\\\"\\n    url: \\\"https://arxiv.org/abs/2502.09061\\\"\\n    bibtex_key: \\\"banerjee2025crane\\\"\\n    category: \\\"quality_impact\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Studies quality impact of constrained decoding on reasoning; relevant to F1 impact analysis\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\", \"total_chars\": 5828, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7ae6a21-8382-4de7-b05e-2749e06a6e7c",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "1e8d1127-da9e-4a47-913c-70c9a6c30aa3",
  "sourceToolAssistantUUID": "e7ae6a21-8382-4de7-b05e-2749e06a6e7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T06:34:57.498Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Mf4QsjLn7DCowhhuimL3SU`</summary>

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
  "parentUuid": "1e8d1127-da9e-4a47-913c-70c9a6c30aa3",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9Dggmp7BdcQNVokQRt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a39af6f-4d29-4a59-b44c-dbee4d78466b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQCSSp4PLWeJzXVdFUWjmV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15644,
      "output_tokens": 381,
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
          "output_tokens": 381,
          "cache_read_input_tokens": 15644,
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

_source line 14 · 2026-05-22T06:34:57.506Z_

<details><summary>↩ Tool result · `toolu_01Mf4QsjLn7DCowhhuimL3SU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a39af6f-4d29-4a59-b44c-dbee4d78466b",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "c1e199fa-719b-4f16-9840-0be18806b2de",
  "sourceToolAssistantUUID": "6a39af6f-4d29-4a59-b44c-dbee4d78466b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T06:35:01.160Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WmJ68GSbrBzfAqS6Gc26oz`</summary>

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
  "parentUuid": "c1e199fa-719b-4f16-9840-0be18806b2de",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9E7TnQihzSaoDF9AHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94185431-2846-4829-b333-0daa286a6266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bDCcJt57AGQkF3YxhKcz7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5012,
      "cache_read_input_tokens": 17090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5012,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 16 · 2026-05-22T06:35:01.164Z_

<details><summary>↩ Tool result · `toolu_01WmJ68GSbrBzfAqS6Gc26oz`</summary>

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
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
74	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp). CF$\leftrightarrow$DR thus represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
75	Global entity-level type consensus during decoding offers the most direct path to resolving CF violations.
76	CF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated.
77	Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
78	Residual DR under fine-tuning (36 violations across all fine-tuned settings, both models and both datasets) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors correctly caught by constraints (28\%); Llama DocRED alone accounts for 33 of 36 residual violations (92\%), reflecting weaker entity typing (Appendix~\ref{app:residual-dr-analysis}).
79	Schema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations; larger training sets or manual constraint table completion can reduce this gap.
80	
81	\paragraph{Evaluation coverage.}
82	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
83	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated on 8B-class (two models, full datasets) and 70B-class models (one model; SciERC full, DocRED 200-document subset).
84	Scaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
85	Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.09\%, R-F1 within $\pm$0.6\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
86	WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).
87	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC (551 documents) and DocRED (998 documents) test sets across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
88	
89	\paragraph{Engineering considerations.}
90	Scalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\% inference overhead and sub-second compilation ($<$0.5\,s; Appendix~\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.
91	Our approach requires access to model logits for token-level masking, which excludes API-only models (e.g., GPT-4, Claude) where only output text is available; extending to API-only settings would require alternative enforcement mechanisms such as constrained sampling APIs or output reranking.
92	Continuation masking assumes each entity type name maps to a distinguishable token prefix sequence.
93	This assumption holds for our evaluation ontologies but may be challenged by ontologies with morphologically similar type names (e.g., \texttt{Protein} vs.\ \texttt{Protein\_Complex} vs.\ \texttt{Protein\_Domain}); when type names share a common prefix longer than one token, masking granularity depends on the tokenizer's subword segmentation.
94	Our evaluation is limited to English-language datasets; the continuation masking mechanism may behave differently for languages without whitespace-delimited tokenization (e.g., Chinese, Japanese), which we leave to future work.
95	Fine-tuning composability was validated exclusively with LoRA; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\ 43.77 on SciERC) but confirms that constraints remain effective (DR 2.74\%\,$\to$\,0\%; Appendix~\ref{app:full-ft}); other fine-tuning methods may exhibit different constraint interaction patterns and warrant further investigation.
96	
97	
98	% === Ethics Statement ===
99	\section*{Ethics Statement}
100	
101	This work uses publicly available benchmark datasets (SciERC, DocRED, and WikiEvents) with no personally identifiable information.
102	No human subjects were involved in the experiments.
103	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
104	Code and data will be released upon acceptance.
105	
106	% === ARR Responsible NLP Research Checklist ===
107	\input{checklist}
108	
109	% === Bibliography ===
110	\bibliography{relwork_new_entries}
111	
112	% === Appendix ===
113	\appendix
114	
115	\input{appendix_prompts}
116	\input{appendix_related_work}
117	\input{appendix_discussion}
118	\input{appendix_llama_per_relation}
119	\input{appendix_sampling_table}
120	\input{appendix_beam_search}
121	\input{appendix_reproducibility}
122	\input{appendix_doc_length}
123	\input{appendix_prompt_sensitivity}
124	\input{appendix_case_studies}
125	\input{appendix_scalability}
126	\input{appendix_full_ft}
127	\input{appendix_tcr}
128	\input{appendix_kappa_case_study}
129	\input{appendix_pumping_lemma}
130	
131	\end{document}
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94185431-2846-4829-b333-0daa286a6266",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "b69f0505-6048-428d-a8e9-3f15174d9a7c",
  "sourceToolAssistantUUID": "94185431-2846-4829-b333-0daa286a6266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T06:35:01.677Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PZxFbxt4GuFFQ4Sbkv6Co2`</summary>

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
  "parentUuid": "b69f0505-6048-428d-a8e9-3f15174d9a7c",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9E7TnQihzSaoDF9AHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85a4eb0b-cdf0-47ac-80f9-c765198f91bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bDCcJt57AGQkF3YxhKcz7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5012,
      "cache_read_input_tokens": 17090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5012,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 18 · 2026-05-22T06:35:01.683Z_

<details><summary>↩ Tool result · `toolu_01PZxFbxt4GuFFQ4Sbkv6Co2`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata, but IE type environments accumulate dynamically (\S\ref{sec:composition}).
9	
10	\paragraph{Schema-aware IE.}
11	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
12	GoLLIE and KnowCoder embed schema knowledge via code-style prompts, achieving structural compliance without runtime semantic enforcement.
13	On SciERC, GoLLIE-7B achieves zero DR violations via its Python dataclass output format but at severe coverage cost: E-F1${=}$9.17, R-F1${=}$0.0, with 46\% of documents producing empty output; OntoCoDec with LoRA (Llama-3.1-8B) achieves R-F1${=}$45.47 with DR${=}$0.09\%, surpassing KnowCoder-7B's supervised R-F1${=}$40.0~\cite{knowcoder_acl2024}.
14	The two paradigms are complementary: GoLLIE constrains output format (structural compliance), while OntoCoDec constrains content generation (semantic compliance).
15	
16	\paragraph{Constraint enforcement in IE.}
17	\citet{roth_yih_2004} and \citet{riedel2010modeling} formulated hard type constraints via ILP; post-hoc validation~\cite{khorshidi2025odke,spires_2024,ontologx_2025} detects violations after generation; EnriCo~\cite{zaratiana2024enrico}, IterGen~\cite{ugare2025itergen}, and DCCD~\cite{dccd2026} enforce constraints via ASP, backtracking, or draft-conditioning.
18	Grammar-only enforcement (GCD~\cite{geng2023gcd}, BoostCD~\cite{boostcd2025}) achieves only partial DR reduction (\S\ref{sec:constrained-baselines}).
19	OntoCoDec uses forward-only token masking at $O(|V|)$ per step; extraction tasks are robust to format constraints~\cite{tam2024letmespeak} despite reasoning degradation in other domains~\cite{banerjee2025crane,formattax2026}.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85a4eb0b-cdf0-47ac-80f9-c765198f91bd",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "3948dbc8-c42c-4c1a-b7df-a235f0d2577a",
  "sourceToolAssistantUUID": "85a4eb0b-cdf0-47ac-80f9-c765198f91bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T06:35:01.710Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UhPyEe85sT9cGvJdMTG3cB`</summary>

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
  "parentUuid": "3948dbc8-c42c-4c1a-b7df-a235f0d2577a",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9E7TnQihzSaoDF9AHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f85bc6b-0ff9-4e0c-a702-73fa92e8ddc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bDCcJt57AGQkF3YxhKcz7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5012,
      "cache_read_input_tokens": 17090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5012,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 20 · 2026-05-22T06:35:01.715Z_

<details><summary>↩ Tool result · `toolu_01UhPyEe85sT9cGvJdMTG3cB`</summary>

```text
1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement; no method provides both semantic awareness and hard constraint enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ontology constraints into context-free grammars (JSON structure, vocabulary membership) via XGrammar; the \emph{semantic layer} interprets type constraints at runtime via dynamic logit masking over an entity registry, with an \emph{empirical enabling dependency} between layers.
19	OntoCoDec compiles constraints automatically from IE ontologies, requires no constraint-specific training, and is applicable to autoregressive LMs with logits access; we validate on three English datasets (up to 96 relation types), five models (7--70B), and three tokenizer families (Llama, Qwen, Mistral).
20	DR enforcement is precision-preserving but introduces CF side-effects (\S\ref{sec:scierc-results}); fine-tuning resolves most CF ($\leq$1.3\%).
21	LoRA + greedy S1 near-eliminates DR ($\leq$0.09\%) with R-F1 within $\pm$0.6\,pp and $+$10\% latency; beam S1 ($k{=}4$) eliminates DR on both datasets (1.54$\times$ latency).
22	Zero-shot evaluation on 7--8B models with 70B results confirms DR drops by 76--99\% for models with well-calibrated type predictions (excluding Mistral-7B due to atypical entity typing interaction; \S\ref{sec:cross-model}).
23	
24	We make a systematic engineering contribution with theoretical grounding:
25	\begin{enumerate}[leftmargin=*,itemsep=2pt]
26	    \item A two-layer constrained decoding framework: we formalize a well-known intuition that cross-field type constraints require runtime state beyond context-free expressiveness (Proposition~1), yielding pair-based sequential enforcement at each level (\S\ref{sec:decidability}). Constraints compile automatically from IE ontologies, validated on schemas of varying restrictiveness with up to 96 relation types.
27	    \item A comprehensive evaluation of type constraint enforcement across 3 IE datasets, 5 models (7--70B), and 2 tasks: (a)~for RE, the five-way ablation confirms that neither layer alone achieves $>$24\% DR reduction while their composition yields 92--100\% DR reduction in fine-tuned settings; zero-shot effectiveness is dataset-dependent (45--99\%), with entity type errors accounting for most residual DR in complex schemas (\S\ref{sec:docred-results}); (b)~event extraction results on WikiEvents provide initial evidence for applicability beyond RE, covering 245 constraints across three tokenizer families (\S\ref{sec:wikievents}).
28	\end{enumerate}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f85bc6b-0ff9-4e0c-a702-73fa92e8ddc9",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "b4a30945-2139-4fb4-8e34-e9b06cb4e86d",
  "sourceToolAssistantUUID": "6f85bc6b-0ff9-4e0c-a702-73fa92e8ddc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T06:35:05.865Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hn9jB2NrL6WgYnunMsCUpw`</summary>

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
  "parentUuid": "b4a30945-2139-4fb4-8e34-e9b06cb4e86d",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9ERkd1nK7RbvaAoRKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a968c6c-c7df-419a-bcc1-c93f10a4b4ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4yf5wtPqKnGiXWRzu2kdc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5012,
      "cache_read_input_tokens": 22102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5012,
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

_source line 22 · 2026-05-22T06:35:05.870Z_

<details><summary>↩ Tool result · `toolu_01Hn9jB2NrL6WgYnunMsCUpw`</summary>

```text
1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types, followed by a relation referencing head $e_k$ for arbitrary $k \leq n$.
32	A PDA's LIFO stack cannot retrieve position $k < n$ without destroying entries above it; since both $n$ and $k$ are independently unbounded, no PDA can enforce this constraint.
33	OntoCoDec's semantic layer addresses this with a runtime entity registry $\mathcal{D}$ (a finite map enabling random-access type lookups).
34	For finite entity sets, the valid language is technically regular but the corresponding DFA requires $O(|\mathcal{E}|^{|\text{entities}|})$ states---exceeding $10^{17}$ for DocRED (7 entity types, 20+ entities per document)---making direct DFA construction infeasible and motivating the grammar-based approach (Appendix~\ref{app:pumping-lemma}).\hfill$\square$
35	
36	\noindent\textbf{Corollary} (empirical enabling dependency: a constraint whose satisfaction is a prerequisite for evaluating subsequent constraints)\textbf{.} The empirical enabling dependency is necessary: the grammar layer alone cannot enforce domain/range constraints (Proposition~1), while the semantic layer alone achieves only 24\% DR reduction without grammar-enforced vocabulary membership (\S\ref{sec:scierc-results}, Table~\ref{tab:scierc-ablation}).
37	\smallskip
38	
39	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}); formal analysis of constraint composition is in Section~\ref{sec:composition}.
40	
41	
42	\subsection{Problem Formulation}
43	\label{sec:formulation}
44	
45	\paragraph{IE as structured generation.}
46	Given an input text $x$, a language model generates a structured JSON output $y$:
47	%
48	\begin{equation}\label{eq:output-schema}
49	\resizebox{.88\columnwidth}{!}{$\displaystyle
50	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
51	$}
52	\end{equation}
53	%
54	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
55	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation, ensuring the relation type $r_j$ is known before entity type fields and enabling sequential domain/range lookups (\S\ref{sec:dynamic-masking}).
56	The grammar structurally enforces entity-before-relation ordering (100\% preservation across all configurations), ensuring the entity registry (\S\ref{sec:entity-registry}) is populated before relation-level type constraints are evaluated; unregistered entities trigger domain-only filtering.
57	
58	\paragraph{Ontology compliance.}
59	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,\, (\tau^h, \tau^t) \in \sigma(r)\}$ for domain-valid head types and $\operatorname{range}(r, \tau^h) = \{\tau^t : (\tau^h, \tau^t) \in \sigma(r)\}$ for the conditional range given head type $\tau^h$.
60	Our enforcement target is \emph{pair-based} type validity: $(\tau^h, \tau^t) \in \sigma(r)$ for every triple.
61	The decoder enforces this sequentially: $\tau^h \in \operatorname{dom}(r)$ at head position, then $\tau^t \in \operatorname{range}(r, \tau^h)$ at tail position, achieving best-effort pair-based enforcement (pair validity ensured when no fallback is triggered; domain-only filtering otherwise) strictly stronger than independent domain/range checks (which over-permit 33--37\% spurious pairs on SciERC/DocRED; \S\ref{sec:rectangularity}).
62	
63	
64	\subsection{Grammar Layer}
65	\label{sec:grammar}
66	
67	A JSON Schema encoding Eq.~\eqref{eq:output-schema} with \texttt{enum} constraints ($\mathcal{E}$, $\mathcal{R}$) is compiled into a pushdown automaton via XGrammar~\cite{dong2025xgrammar}.
68	At step $t$, grammar-valid tokens $G(t) \subseteq V$ pass; all others receive logits $-\infty$, enforcing structural validity, vocabulary membership ($r_j \in \mathcal{R}$, $\tau_i \in \mathcal{E}$), but not domain/range constraints (which depend on entity types within each triple).
69	
70	\subsection{Semantic Layer}
71	\label{sec:semantic}
72	
73	The semantic layer enforces domain/range constraints through a stateful logits processor maintaining an entity registry during generation.
74	
75	\paragraph{Entity registry.}
76	\label{sec:entity-registry}
77	The semantic layer builds a registry $\mathcal{D}: \text{name} \to \text{type}$ incrementally during entity generation: each completed entry $\{n_i, \tau_i\}$ adds $(n_i, \tau_i)$ to $\mathcal{D}$, which is consulted during relation generation for type lookups.
78	At each step $t$, the processor pattern-matches the decoded prefix to identify the current field position; semantic masks activate only at type-bearing positions (\textsc{HeadType}, \textsc{TailType}).
79	\label{sec:position-detection}
80	
81	\paragraph{Dynamic masking.}
82	\label{sec:dynamic-masking}
83	At type-bearing positions, the processor computes a semantic mask $S(t) \subseteq V$.
84	At a \textsc{HeadType} position, if $h_j \in \mathcal{D}$ and $\mathcal{D}[h_j] \in \operatorname{dom}(r_j)$, the mask allows only the registered type; otherwise it falls back to all domain-valid types $\operatorname{dom}(r_j)$.
85	At a \textsc{TailType} position, the mask restricts to $\operatorname{range}(r_j, \tau^h_j)$ conditioned on the already-determined head type, further narrowing to the registered type when $t_j \in \mathcal{D}$.
86	This sequential check achieves best-effort pair-based enforcement (\S\ref{sec:formulation}), strictly tighter than independent domain/range checking; ``best-effort'' reflects the grammar-first fallback (\S\ref{sec:composition}), which prioritizes JSON integrity over type validity when constraints conflict.
87	
88	\paragraph{Tokenizer-agnostic type masking.}
89	We use \emph{continuation masking} to handle context-dependent tokenizations and prefix-shared types (e.g., \textsc{Sen}/\textsc{Sid}/\textsc{Side} in WikiEvents): a compile-time prefix map identifies valid continuations for each type name, disambiguating over multiple steps across byte-level BPE (Qwen, Llama) and SentencePiece (Mistral).
90	
91	\paragraph{Grammar-semantic interaction.}
92	\label{sec:interaction}
93	The final mask is $G(t) \cap S(t)$; when empty, grammar-first fallback applies (\S\ref{sec:composition}), embodying the empirical enabling dependency: semantic constraints reduce DR by only 24\% without grammar-enforced vocabulary.
94	
95	
96	\subsection{Decoding Strategies}
97	\label{sec:strategies}
98	
99	\paragraph{S1 (joint extraction): Single-pass decoding.}
100	Both layers are active throughout generation; the entity registry populates during entity decoding and is immediately available for relation-level type checking.
101	
102	\paragraph{S2 (two-pass pipeline): Two-pass decoding.}\label{sec:s2}
103	A first pass extracts entities; these compile an input-dependent grammar for the second pass.
104	S1 achieves higher R-F1 at comparable DR (\S\ref{sec:scierc-results}) and is the primary configuration.
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a968c6c-c7df-419a-bcc1-c93f10a4b4ef",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "4a44e79e-2484-44dd-9e22-205a75395dbc",
  "sourceToolAssistantUUID": "4a968c6c-c7df-419a-bcc1-c93f10a4b4ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T06:35:06.270Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WRNoRTkAfpVsesb6V3mQ5y`</summary>

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
  "parentUuid": "4a44e79e-2484-44dd-9e22-205a75395dbc",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9ERkd1nK7RbvaAoRKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6a3e682-8c1e-46bf-b09d-cf0ec6be203c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4yf5wtPqKnGiXWRzu2kdc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5012,
      "cache_read_input_tokens": 22102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5012,
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

_source line 24 · 2026-05-22T06:35:06.275Z_

<details><summary>↩ Tool result · `toolu_01WRNoRTkAfpVsesb6V3mQ5y`</summary>

```text
1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the empirical enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
17	
18	\paragraph{Constraint Tightness.}
19	\label{eq:tightness}
20	We define per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$ and the schema-level mean $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$.
21	Across three schemas---WikiEvents ($\bar{\kappa}{=}0.029$), SciERC ($\bar{\kappa}{=}0.333$), DocRED ($\bar{\kappa}{=}0.842$)---DR reduction ranges from 94--99\% (low $\bar{\kappa}$) to 42--90\% (high $\bar{\kappa}$); entity type confusability is a critical co-factor (Appendix~\ref{app:kappa-case-study},~\ref{app:tcr}).
22	
23	\paragraph{Greedy limitation and fallback cascade.}
24	\label{sec:greedy-limitation}
25	The semantic layer commits entity types greedily---an instance of Level~3 (non-local) constraints (\S\ref{sec:decidability})---so CF violations arise when the same entity receives different types across triples; beam search mitigates this in favorable configurations (\S\ref{sec:beam-results}).
26	Grammar-first fallback triggers on 0.5--5.7\% of type-bearing positions under zero-shot decoding, correlating with $\bar{\kappa}$; fine-tuning virtually eliminates fallback ($\leq$\,0.11\%), transitioning the semantic layer from primary enforcer to safety net.
27	Causal tracing confirms all residual DR occurs exclusively at fallback positions (Appendix~\ref{app:causal-tracing}).
28	
29	\paragraph{Non-rectangularity and independent enforcement.}
30	\label{sec:rectangularity}
31	Type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement is a sound over-approximation admitting 33--37\% spurious pairs; fine-tuning eliminates all residual DR (Table~\ref{tab:composability}).
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6a3e682-8c1e-46bf-b09d-cf0ec6be203c",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "875c57f6-98b8-4e4b-ba25-a78bdf22805c",
  "sourceToolAssistantUUID": "d6a3e682-8c1e-46bf-b09d-cf0ec6be203c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T06:35:06.935Z_

<details open><summary>🔧 Tool call — Read · `toolu_017yAjuaV38dbxQsxNqUduQi`</summary>

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
  "parentUuid": "875c57f6-98b8-4e4b-ba25-a78bdf22805c",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9ERkd1nK7RbvaAoRKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "425da05f-814d-434c-8ae4-276f530f2b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4yf5wtPqKnGiXWRzu2kdc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5012,
      "cache_read_input_tokens": 22102,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5012
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 22102,
          "cache_creation_input_tokens": 5012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5012,
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

_source line 26 · 2026-05-22T06:35:06.941Z_

<details><summary>↩ Tool result · `toolu_017yAjuaV38dbxQsxNqUduQi`</summary>

```text
1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas).
4	The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning on well-calibrated models, \textsc{OntoCoDec} near-eliminates DR (92--100\% reduction, $<$0.5\% true-positive loss) with negligible RE R-F1 impact ($\pm$0.6\,pp) but introduces CF violations as a trade-off ($\leq$1.3\% fine-tuned); zero-shot effectiveness varies by dataset and model calibration (45--99\% DR reduction, 0--21.1\% CF; \S\ref{sec:experiments}).
7	Beam search eliminates residual DR; CF effects are configuration-dependent, with full elimination on SciERC under LoRA (\S\ref{sec:beam-results}).
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across five autoregressive LMs (7--70B; 70B zero-shot and LoRA in \S\ref{sec:70b-results}) with logits access and three tokenizer families (up to 96 relation types).
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "425da05f-814d-434c-8ae4-276f530f2b5b",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "bd6dbe2c-bfd8-4d95-8586-5d91faf50adf",
  "sourceToolAssistantUUID": "425da05f-814d-434c-8ae4-276f530f2b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T06:35:11.356Z_

<details open><summary>🔧 Tool call — Read · `toolu_017XnGk73k3ahk37Jm5s3XGJ`</summary>

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
  "parentUuid": "bd6dbe2c-bfd8-4d95-8586-5d91faf50adf",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9EotPE4Qi41PffBt3u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77573956-c6d2-4dc3-8943-f568b7b304cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5dBekqmg42nyq9cQYtbzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4800,
      "cache_read_input_tokens": 27114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4800,
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

_source line 28 · 2026-05-22T06:35:11.359Z_

<details><summary>↩ Tool result · `toolu_017XnGk73k3ahk37Jm5s3XGJ`</summary>

```text
1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (\S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
20	
21	\paragraph{Problem Statement.}
22	\label{sec:bg:problem}
23	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
24	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is available in the decoded prefix.
25	This requires that each entity type name maps to a distinguishable token sequence (\S\ref{sec:dynamic-masking}).
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77573956-c6d2-4dc3-8943-f568b7b304cc",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "77300a02-9f4f-4f09-bbab-008cdc75c469",
  "sourceToolAssistantUUID": "77573956-c6d2-4dc3-8943-f568b7b304cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T06:35:12.159Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JmM7XQhdDptUgU4o6ywZ8o`</summary>

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
  "parentUuid": "77300a02-9f4f-4f09-bbab-008cdc75c469",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9EotPE4Qi41PffBt3u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54fb32f9-0865-408f-a5e4-79124186601b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5dBekqmg42nyq9cQYtbzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4800,
      "cache_read_input_tokens": 27114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4800,
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

_source line 30 · 2026-05-22T06:35:12.164Z_

<details><summary>↩ Tool result · `toolu_01JmM7XQhdDptUgU4o6ywZ8o`</summary>

```text
1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation burden).
60	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
61	F1 $\times$100. Bootstrap: 10{,}000 iterations.
62	CF: same entity assigned conflicting types across triples.
63	S1 = single-pass (\S\ref{sec:strategies}), S2 = two-pass (\S\ref{sec:s2}).
64	Grammar-only represents the ceiling of grammar-constrained decoding~\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}
65	\label{tab:scierc-ablation}
66	\end{table}
67	
68	% ──────────────────────────────────────────
69	%  (a) Core result
70	% ──────────────────────────────────────────
71	\paragraph{Zero-shot diagnostic.}
72	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
73	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
74	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
75	Full S1 reduces DR from 15.37\% to 0.93\% ($\downarrow$94\%) while R-F1 is unchanged (8.23\,$\to$\,8.36, $p{=}0.58$).
76	Per-relation DR drops to $\leq$2.82\%, reaching 0\% on 4/7 relations (Appendix~\ref{app:per-relation-landscape}).
77	Post-hoc filtering discards up to 48\% of predictions rather than correcting them (Appendix~\ref{app:posthoc-extended}); CF rises to 9.90\% (\S\ref{sec:discussion}).
78	
79	% ──────────────────────────────────────────
80	%  (b) Grammar layer
81	% ──────────────────────────────────────────
82	\paragraph{Layer contributions.}
83	% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
84	Grammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\%, the ceiling of grammar-based decoding~\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\%), so CF originates from the semantic layer.
85	Semantic-only reduces DR by only 24\% and cannot eliminate RV or ET; this is the \emph{empirical enabling dependency}: adding the grammar layer yields a further 92\% reduction (11.65\%\,$\to$\,0.93\%).
86	
87	
88	% ──────────────────────────────────────────
89	%  (d) S1 vs S2
90	% ──────────────────────────────────────────
91	\paragraph{S1 vs.\ S2.}
92	S2 achieves comparable DR (0.97\%) but lower R-F1 and CF; we adopt S1.
93	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644
94	
95	% ──────────────────────────────────────────
96	%  (e) Composability with Fine-Tuning
97	%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
98	%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,
99	%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,
100	%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval
101	% ──────────────────────────────────────────
102	\paragraph{Composability with fine-tuning.}
103	\label{sec:composability}
104	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.09\% with R-F1 within $\pm$0.6\,pp (removed triples are 97.6--100\% false positives).
105	CF drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned; Appendix~\ref{app:cf-distribution}); beam ($k{=}4$) with LoRA eliminates all four violation types on SciERC (R-F1 43.60, 46.18; \S\ref{sec:beam-results}).
106	
107	\begin{table}[t]
108	\centering
109	\small
110	\setlength{\tabcolsep}{3pt}
111	\resizebox{\columnwidth}{!}{%
112	\begin{tabular}{@{}lll rrrr r@{}}
113	\toprule
114	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
115	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
116	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
117	  & \textbf{$\Delta$DR} \\
118	\midrule
119	\multirow{4}{*}{Qwen3-8B}
120	  & \multirow{2}{*}{SciERC}
121	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
122	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
123	\cmidrule(l){2-8}
124	  & \multirow{2}{*}{DocRED}
125	    & Unconstr.\ &  0.56 & 0.08 & 40.89 & 82.35 & --- \\
126	  & & Full S1    & \textbf{0.00} & 0.22 & 40.79 & 81.87 & $\downarrow$100\% \\
127	\midrule
128	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
129	  & \multirow{2}{*}{SciERC}
130	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
131	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
132	\cmidrule(l){2-8}
133	  & \multirow{2}{*}{DocRED}
134	    & Unconstr.\ &  0.49 & 0.08 & 44.55 & 84.77 & --- \\
135	  & & Full S1    &  0.00 & 0.26 & 44.70 & 84.71 & $\downarrow$100\% \\
136	\bottomrule
137	\end{tabular}}%
138	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
139	F1\,$\times$100.
140	Paired bootstrap (B${=}$10{,}000, document-level): $\Delta$R-F1 between constrained and unconstrained is not significant ($p{>}0.05$; largest $|\Delta|{=}0.31$\,pp, $p{=}0.056$), while DR reduction is significant in all settings ($p{<}0.001$).
141	E-F1 includes parse-failure documents (Qwen PF: 7--8\%; Llama PF: 2--3\%).}
142	\label{tab:composability}
143	\end{table}
144	
145	% ──────────────────────────────────────────
146	%  (f) Downstream impact of DR elimination
147	%  exp_ids: task_e_lucky_violation_analysis
148	% ──────────────────────────────────────────
149	\paragraph{Downstream impact.}
150	\label{sec:downstream-impact}
151	Among constraint-removed triples, only 0.49\% match gold labels on average (``lucky violations''), confirming $<$0.5\% recall cost; on Llama SciERC all five are recovered via legal type paths (zero churn; Appendix~\ref{app:lucky-violations}).
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54fb32f9-0865-408f-a5e4-79124186601b",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "6338a042-6f8d-47e5-be7e-f6a739e39ece",
  "sourceToolAssistantUUID": "54fb32f9-0865-408f-a5e4-79124186601b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T06:35:12.387Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WSAKWWCjztFW9eVhAwXmwD`</summary>

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
  "parentUuid": "6338a042-6f8d-47e5-be7e-f6a739e39ece",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9EotPE4Qi41PffBt3u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d522fa2-1177-43f1-bd22-9cb594ff9d9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5dBekqmg42nyq9cQYtbzw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4800,
      "cache_read_input_tokens": 27114,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 27114,
          "cache_creation_input_tokens": 4800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4800,
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

_source line 32 · 2026-05-22T06:35:12.391Z_

<details><summary>↩ Tool result · `toolu_01WSAKWWCjztFW9eVhAwXmwD`</summary>

```text
1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrrr rr@{}}
20	\toprule
21	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-7} \cmidrule(l){8-9}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10  & 18.56
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07  & 26.24
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05  & 14.89
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57  & \textbf{12.78}
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Tot.\ = DR + CF (total type-violation burden).
54	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).
56	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see text).}
57	\label{tab:docred-ablation}
58	\end{table}
59	
60	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
61	\paragraph{Zero-shot diagnostic.}
62	Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET ($\to$\,0\%), and eliminates RV (29.66\%\,$\to$\,0.03\%).\footnote{The residual 0.03\% RV traces to a rare XGrammar automaton edge case where subword tokens from different enum entries combine into chimeric values (e.g., \texttt{member} + \texttt{icipant\_of} from \texttt{member\_of} and \texttt{participant\_of}). This has been reported upstream and is not a fundamental limitation of the approach.}
63	R-F1 improves from 7.74 to 8.23 ($+$0.50\,pp; $p < 0.001$), attributable to elimination of 5{,}189 OOV relation predictions.
64	CF increases from 0.10\% to 2.57\%, consistent with the CF$\leftrightarrow$DR trade-off (\S\ref{sec:discussion}).
65	Residual zero-shot DR (10.21\%) traces to grammar-first fallback under tight constraints ($\bar{\kappa}{=}0.842$; \S\ref{sec:greedy-limitation}); causal tracing confirms all residual DR occurs at fallback positions (Appendix~\ref{app:causal-tracing}).
66	
67	% exp_ids: phase2_docred_grammar_only, phase2_docred_semantic_only, phase2_docred_full_s1
68	\paragraph{Layer contributions.}
69	Grammar-only eliminates RV and ET but \emph{increases} DR to 26.17\%: vocabulary restriction makes OOV outputs evaluable, exposing latent type incompatibilities.
70	Semantic-only reduces DR by 25\% but cannot eliminate RV or ET, the same empirical enabling dependency observed on SciERC.
71	Residual DR (10.21\% vs.\ 0.93\% on SciERC) reflects high $\bar{\kappa}$ (0.842) and \textsc{Generic}$\leftrightarrow$X ambiguity; fine-tuning narrows DR to $\leq$\,0.09\% (Table~\ref{tab:composability}), with the 36 residual violations decomposing into entity type errors (39\%), schema coverage gaps (33\%), incorrect relation selection (17\%), and direction reversal (11\%; Appendix~\ref{app:residual-dr-analysis}).
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d522fa2-1177-43f1-bd22-9cb594ff9d9d",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "37e12e68-18ed-4966-a601-8490892faa34",
  "sourceToolAssistantUUID": "8d522fa2-1177-43f1-bd22-9cb594ff9d9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T06:35:17.695Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WJGYCgubmiGuK39F34Ue68`</summary>

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
  "parentUuid": "37e12e68-18ed-4966-a601-8490892faa34",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9FDCbb4xr6XATejbPq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8d1a375-bac7-4426-9873-f6c717652c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBhx4TsZRZ3mMZiZeDnkfa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6422,
      "cache_read_input_tokens": 31914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6422,
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

_source line 34 · 2026-05-22T06:35:17.703Z_

<details><summary>↩ Tool result · `toolu_01WJGYCgubmiGuK39F34Ue68`</summary>

```text
1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\setlength{\tabcolsep}{3.4pt}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}ll rrrr r@{}}
18	\toprule
19	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
20	& \textbf{R-F1} \\
21	\cmidrule(lr){3-6} \cmidrule(l){7-7}
22	\textbf{Dataset} & \textbf{Model}
23	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
24	  & $\uparrow$ \\
25	\midrule
26	\multirow{6}{*}{SciERC}
27	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
28	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
29	  \cmidrule(l){2-7}
30	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
31	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
32	  \cmidrule(l){2-7}
33	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
34	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
35	\midrule
36	\multirow{6}{*}{DocRED}
37	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
38	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
39	  \cmidrule(l){2-7}
40	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
41	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
42	  \cmidrule(l){2-7}
43	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
44	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
48	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
49	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
50	F1 $\times$100.}
51	\label{tab:cross-model}
52	\end{table}
53	
54	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
55	\paragraph{Results.}
56	RV and ET reach $\leq$0.03\% for all models on both datasets.
57	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in 5/6 settings.
58	CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%; \S\ref{sec:discussion}) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%); fine-tuning resolves both (\S\ref{sec:composability}).
59	Mistral is a boundary condition: poor entity typing limits DR reduction to 42\% vs.\ 76--99\% for calibrated models.
60	
61	\paragraph{Post-hoc filtering comparison.}
62	Post-hoc filtering achieves DR${=}$0\% but with 15--74\% rejection rates (DocRED Qwen: 48\% discarded vs.\ OntoCoDec retaining all); under fine-tuning, both achieve comparable F1 (Appendix~\ref{app:posthoc-extended}).
63	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8d1a375-bac7-4426-9873-f6c717652c82",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "3727ba13-3b22-49fb-b85a-7126cef8c060",
  "sourceToolAssistantUUID": "a8d1a375-bac7-4426-9873-f6c717652c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T06:35:18.654Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SzHD5X67zvvzy4PpEemj7A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3727ba13-3b22-49fb-b85a-7126cef8c060",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9FDCbb4xr6XATejbPq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e733c373-a921-49ac-854e-c7865c89c50d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBhx4TsZRZ3mMZiZeDnkfa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6422,
      "cache_read_input_tokens": 31914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6422,
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

_source line 36 · 2026-05-22T06:35:18.671Z_

<details><summary>↩ Tool result · `toolu_01SzHD5X67zvvzy4PpEemj7A`</summary>

```text
1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Extension to Event Extraction}
8	\label{sec:wikievents}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42	  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
43	  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
44	  & Full S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{WikiEvents EE results. Zero-shot rows (n$=$246): full WikiEvents corpus; fine-tuning (\S\ref{sec:wikievents}, n$=$20): standard 194/20/20 split~\cite{li2021document}.
48	Violation rates over parsed documents.
49	\textemdash{} indicates not applicable (grammar-only has no semantic-layer metrics).
50	F1 $\times$ 100.}
51	\label{tab:wikievents}
52	\end{table}
53	
54	\paragraph{Results.}
55	Unconstrained EE produces extreme vocabulary violations (EV+RoV $>$85\%; Table~\ref{tab:wikievents}), with entity F1\,=\,0 because the parser cannot process off-schema output.
56	Full S1 eliminates EV and RoV across all models, which validates the tokenizer-agnostic design across byte-level BPE and SentencePiece.
57	Grammar-only eliminates EV but leaves RoV at 64--77\% and surfaces latent AC (8--14\%), consistent with DocRED's pattern (\S\ref{sec:docred-results}); full S1 drives RoV to 0\%.
58	Residual AC (1.3--3.8\%) traces to semantically similar types (e.g., SID vs.\ SEN).
59	CF rises to 15--21\%, exceeding RE levels (10--12\%) because EE's multi-argument structures increase entity reuse across slots.
60	Post-hoc filtering is impractical ($<$0.5\% arguments retained).
61	Unlike RE, EE shows measurable F1 gains: entity F1 0\%\,$\to$\,12--18\%, trigger F1 $+$1.5--1.8\,pp.
62	
63	% exp_ids: p1_ee_ft_qwen_wikievents_r5, p1_ee_ft_llama_wikievents_r5
64	\paragraph{Composability with fine-tuning.}
65	On the full official test split (20 documents; 194/20/20~\cite{li2021document}), LoRA + S1 eliminates RoV (Qwen 38.31\%\,$\to$\,0\%, Llama 8.8\%\,$\to$\,0\%) and reduces AC to $\leq$0.8\%, with argument F1 within $\pm$1.1\,pp; trigger F1 shifts ($-$5.4/$-$0.6\,pp) have wide CIs consistent with n${=}$20.
66	CF remains low (0.77--1.18\%); per-document variance is high (Arg-F1 std/mean ${>}$\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences.
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e733c373-a921-49ac-854e-c7865c89c50d",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "3b4dcb2c-db3f-4567-b945-d1f9bbdf0fde",
  "sourceToolAssistantUUID": "e733c373-a921-49ac-854e-c7865c89c50d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T06:35:18.998Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HLacSEWpL7iDqSHqd7C5dr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b4dcb2c-db3f-4567-b945-d1f9bbdf0fde",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9FDCbb4xr6XATejbPq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ad33b81-032e-46bd-b22b-970dbaf0b604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBhx4TsZRZ3mMZiZeDnkfa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6422,
      "cache_read_input_tokens": 31914,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6422
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 31914,
          "cache_creation_input_tokens": 6422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6422,
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

_source line 38 · 2026-05-22T06:35:19.011Z_

<details><summary>↩ Tool result · `toolu_01HLacSEWpL7iDqSHqd7C5dr`</summary>

```text
1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	Beam search ($k{=}4$)~\cite{anderson2017guided} explores paths satisfying both layers jointly.
11	With LoRA, beam S1 eliminates all four violation types on SciERC (R-F1 44--46); zero-shot beam achieves DR${=}$0\% on both datasets (998-doc DocRED; CF response is model-dependent; Appendix~\ref{app:beam-search}).
12	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
13	
14	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
15	\paragraph{70B evaluation.}
16	\label{sec:70b-results}
17	On Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on both datasets: SciERC 6.41\%\,$\to$\,0\% (R-F1 11.24, $+$0.09\,pp), DocRED 14.98\%\,$\to$\,0\% (R-F1 13.05, $+$0.04\,pp); CF rises to 3.50--7.01\% (from $\leq$0.07\%), comparable to 8B zero-shot CF.
18	% TODO: 待 70B LoRA 结果回填（SciERC 551 docs, DocRED 200-doc subset）
19	LoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\%, consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
20	
21	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
22	\paragraph{Comparison with grammar-constrained approaches.}
23	\label{sec:constrained-baselines}
24	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same class of constraints---vocabulary membership via context-free grammars---as GCD~\cite{geng2023gcd} and the grammar component of BoostCD~\cite{boostcd2025}, achieving RV/ET$\to$0\% but only 3\% DR reduction vs.\ Full S1's 94\%.
25	Without JSON structural enforcement, trie-only vocabulary constraints (GCD-equivalent) are counterproductive: DR rises to 15--96\% (vs.\ 1--15\% unconstrained) because models omit type fields or produce malformed JSON without grammar-level structure (Appendix~\ref{app:trie-baseline}), confirming both layers are necessary.
26	BoostCD's boosting of constrained and unconstrained decoding is complementary and potentially integrable with OntoCoDec's semantic layer.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ad33b81-032e-46bd-b22b-970dbaf0b604",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "55971ec6-4889-46b3-b459-4d2c2fa9eac9",
  "sourceToolAssistantUUID": "4ad33b81-032e-46bd-b22b-970dbaf0b604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T06:35:23.365Z_

<details open><summary>🔧 Tool call — Read · `toolu_014RFnjG9LhWidJDNozTsHYN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55971ec6-4889-46b3-b459-4d2c2fa9eac9",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9FhNkVTBJNXuYHJye6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22744d2d-ec72-403d-9832-654e1f0c36be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWFTXzLBK84CYmDWYFJceK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4780,
      "cache_read_input_tokens": 38336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4780,
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

_source line 40 · 2026-05-22T06:35:23.369Z_

<details><summary>↩ Tool result · `toolu_014RFnjG9LhWidJDNozTsHYN`</summary>

```text
1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec translates IE ontologies into composable token-level constraints via a two-layer architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.09\% ($<$0.5\% recall cost), CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models (7--8B; 70B LoRA in \S\ref{sec:70b-results}).
4	Triple validity analysis (\S\ref{sec:downstream-impact}) confirms 100\% schema compliance at $<$0.5\% recall cost.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22744d2d-ec72-403d-9832-654e1f0c36be",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "2cd9dfbd-8616-4269-8abc-f9beab7d7b2a",
  "sourceToolAssistantUUID": "22744d2d-ec72-403d-9832-654e1f0c36be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T06:35:24.340Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ChesKWphQ55wj6U26Bw2ti`</summary>

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
  "parentUuid": "2cd9dfbd-8616-4269-8abc-f9beab7d7b2a",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9FhNkVTBJNXuYHJye6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1bfdce8-9c36-465a-8f18-c6063e75a468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWFTXzLBK84CYmDWYFJceK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4780,
      "cache_read_input_tokens": 38336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4780,
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

_source line 42 · 2026-05-22T06:35:24.345Z_

<details><summary>↩ Tool result · `toolu_01ChesKWphQ55wj6U26Bw2ti`</summary>

```text
1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, which enables efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, and provide a robust foundation for structured generation.
15	However, all of these methods operate exclusively at the syntactic level: they ensure format validity (e.g., well-formed JSON, valid enum values) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.
16	This syntactic-only limitation motivates OntoCoDec's semantic extension: our grammar layer builds on XGrammar for structural (JSON schema and enum) constraints, while a second semantic layer enforces relational type constraints that are inherently beyond the expressive power of context-free grammars.
17	
18	% ===========================================================================
19	% Paradigm 1.5: Semantic Constrained Decoding for Code
20	% ===========================================================================
21	\paragraph{Semantic Constrained Decoding for Code.}
22	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness; this work demonstrates that richer-than-CFG constraints can be compiled into token-level filtering.
23	In the text-to-SQL domain, PICARD~\cite{scholak2021picard} maintains an incremental SQL parsing state that rejects tokens violating syntax or referencing non-existent database columns at each decoding step, achieving state-of-the-art results on Spider and CoSQL without modifying model weights.
24	While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema (database table and column names known before decoding begins).
25	In contrast, OntoCoDec's entity registry is populated \emph{during} generation as entity spans are extracted from free text; constraint sets evolve with the decoding prefix, a fundamental distinction between querying a known schema and extracting from unstructured text.
26	Synchromesh~\cite{synchromesh_iclr2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs without fine-tuning; this establishes that semantic constraints can be expressed as dynamic token masks conditioned on the generation prefix.
27	MGD~\cite{mgd_neurips2023} uses static-analysis monitors to perform incremental type checking at decode time; SantaCoder-1.1B with MGD outperforms text-davinci-003 on repository-level code completion by ensuring that every generated identifier is type-correct with respect to the surrounding code context.
28	Most recently, \citet{pldi2025_type_constrained_codegen} compile full type systems, including generic types and subtyping, into prefix automata for token-level logits masking and reduce compilation errors by over 50\%.
29	This last system is the closest mechanistic analog to OntoCoDec, applying the same ``type system $\to$ automaton $\to$ logits mask'' pipeline, though in a fundamentally different domain.
30	The key technical difference lies in the constraint structure: programming-language type systems feature deep subtyping hierarchies and parametric polymorphism, whereas IE ontology axioms specify flat domain/range sets; a relation $R$ accepts head entities from set $\mathcal{D}(R)$ and tail entities from set $\mathcal{R}(R)$, with no subtype chains.
31	Conversely, IE introduces a challenge absent in code generation: the constraint target (entity type) must be inferred from free-text spans rather than read from declared type annotations, so a stateful entity registry must track extracted types during autoregressive generation.
32	These methods collectively demonstrate that semantic (type) constraints at decode time are both feasible and highly effective, but exclusively in the code domain where type systems are formally specified.
33	OntoCoDec is the first to \emph{automatically compile} IE ontology axioms, including domain/range constraints, into token-level decoding masks for information extraction, migrating the type-constrained decoding paradigm from code generation to IE.
34	
35	% ===========================================================================
36	% Paradigm 2: Vocabulary/Type-Constrained Generation
37	% ===========================================================================
38	\paragraph{Vocabulary and Type-Constrained Generation.}
39	The idea of enforcing entity-type compatibility constraints for information extraction dates back to pre-neural methods.
40	\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints (e.g., \textsc{Emp-Org} only between \textsc{Per} and \textsc{Org} entities); this establishes the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.
41	In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, restricting each decoding step to tokens consistent with valid entity names from a predefined catalog.
42	GenIE~\cite{josifoski2022genie} extends this approach to end-to-end information extraction with state-based constraints that enforce valid triple structures, achieving strong performance on closed-world knowledge base population, though it requires task-specific fine-tuning on the target schema.
43	AdaKGC~\cite{adakgc_emnlp2023} introduces schema-constrained dynamic decoding with trie-based prefix trees that adapt to the target schema, enforcing that generated entity and relation names belong to a predefined inventory, a vocabulary-level constraint that ensures name validity but does not verify type compatibility between a relation and its arguments.
44	GCD~\cite{geng2023gcd} provides a unified grammar-constrained decoding framework for structured NLP tasks including IE, introducing input-dependent grammars that adapt constraints based on the source text. GCD is the closest precursor to OntoCoDec in applying logits masking to IE, though limited to syntactic constraints.
45	NeuroLogic Decoding~\cite{lu2021neurologic} expresses lexical inclusion and exclusion constraints as predicate logic formulas enforced during beam search, offering a general mechanism for token-level control that can encode vocabulary membership but not relational type rules.
46	These approaches constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation.
47	OntoCoDec's semantic layer enforces relational constraints (e.g., that the head entity of relation $R$ must belong to type set $\mathcal{D}(R)$) which cannot be expressed as static vocabulary restrictions because the valid set depends on the relation type generated earlier in the same sequence.
48	While Roth \& Yih's ILP formulation shares the same type-compatibility motivation, it operates as a post-hoc reranker over discrete candidates; OntoCoDec integrates enforcement directly into autoregressive decoding, preventing violations rather than filtering them.
49	
50	% ===========================================================================
51	% Paradigm 3: Structural Constraints for IE
52	% ===========================================================================
53	\paragraph{Structural Constraints via Training and Prompting.}
54	An orthogonal approach encodes IE output structure through model training or prompt design rather than decoding-time enforcement, relying on learned representations to produce schema-compliant outputs.
55	UIE~\cite{lu2022uie} defines a Structured Extraction Language and trains a unified text-to-structure model across 13 IE datasets, relying on large-scale pre-training to internalize output format constraints.
56	GoLLIE~\cite{sainz2024gollie} expresses annotation guidelines as Python dataclass definitions and fine-tunes Code-LLaMA to generate typed code, achieving strong zero-shot transfer to unseen IE schemas through the implicit type structure of programming languages.
57	KnowCoder~\cite{knowcoder_acl2024} takes this further by encoding 29K entity types from Wikidata as a Python class hierarchy, training a Code-LLM to generate structured extraction code that implicitly respects type inheritance, the most comprehensive schema-as-code approach to date.
58	CodeIE~\cite{li2023codeie} similarly reformulates IE as code generation, using the structural regularity of programming languages to reduce output format errors.
59	ADELIE~\cite{qi2024adelie} uses SFT and DPO to align LLMs on IE tasks, achieving state-of-the-art results among open-source models while preserving general capabilities, though compliance with ontological constraints remains a learned soft preference rather than a hard constraint.
60	In the supervised setting, joint entity-relation architectures such as SpERT~\cite{eberts2020spert} and PFN~\cite{yan2021pfn} enforce type consistency implicitly through shared representations: SpERT classifies entity spans and relation pairs in a single BERT pass with span-level negative sampling, while PFN decomposes feature encoding into entity-specific, relation-specific, and shared partitions via gating mechanisms.
61	These models achieve strong performance but are limited to fixed, predefined schemas and cannot generalize to unseen ontologies without retraining, precisely the ontology-portable scenario requiring no constraint-specific training that OntoCoDec targets.
62	EnriCo~\cite{zaratiana2024enrico} applies Answer Set Programming (ASP) constraints during decoding of joint entity-relation extraction models, enforcing structural type compatibility at generation time. This is a decoding-time approach, though with model-specific, manually authored constraints rather than ontology-driven compilation.
63	Training-based methods provide \emph{soft} structural guidance: the model learns to prefer valid outputs but cannot enforce compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.
64	Importantly, training-based and decoding-time approaches are complementary rather than competing: a system like GoLLIE could be combined with OntoCoDec's constraint layers, using fine-tuning to maximize the probability of valid outputs while decoding-time enforcement eliminates residual violations.
65	OntoCoDec provides \emph{hard} decoding-time enforcement that requires no constraint-specific training, is automatically compiled from IE ontologies, and composable with any of these training-based approaches.
66	
67	% ===========================================================================
68	% Paradigm 4: Type-Checking / Ontology Validation
69	% ===========================================================================
70	\paragraph{Post-hoc Ontology Validation.}
71	Rather than constraining generation, several methods validate LLM outputs against ontological rules after generation, applying a detect-then-fix paradigm.
72	ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale, but constraint adherence relies on prompt-level guidance, not enforcement, leaving residual violations unaddressed.
73	SPIRES/OntoGPT~\cite{spires_2024} provides an ontology-based extraction framework that grounds LLM outputs against OBO ontologies post-generation: it validates extracted entities and relations through ontology lookup and corrects mismatches in a second pass, the prompt-then-validate paradigm in the biomedical domain.
74	OntoLogX~\cite{ontologx_2025} applies SHACL validation to LLM-generated knowledge graphs, iteratively re-prompting the LLM to correct constraint violations and reducing them by approximately 10$\times$ across multiple correction rounds. This demonstrates the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
75	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB, though their constrained inference operates over a discrete candidate set rather than during autoregressive generation.
76	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating RDF triple insertions against RDFS domain/range constraints, where each validation step requires a separate LLM call, effective but computationally expensive at scale.
77	RELATE~\cite{olasunkanmi2025relate} addresses the alignment gap between LLM-extracted biomedical relations and standardized ontology predicates through a three-stage pipeline: ontology preprocessing with predicate embeddings, similarity-based retrieval via SapBERT, and LLM-based reranking with negation handling, achieving 94\% accuracy@10 on ChemProt.
78	While RELATE demonstrates effective ontology grounding for relation extraction, its constraints are applied \emph{post-extraction} through retrieval and reranking rather than during generation, and it requires domain-specific embedding models trained on biomedical corpora.
79	OntoCoDec enforces ontology constraints \emph{during} autoregressive decoding and requires no additional trained components beyond the base LLM.
80	Concurrently, \citet{zhou2026ontologytools} compile OWL ontologies into executable tool interfaces within The World Avatar framework; LLM agents must invoke ontology-aware tools that enforce semantic constraints during knowledge graph construction from scientific text.
81	This ``ontology-to-tools'' approach shares OntoCoDec's philosophy of compiling formal ontological knowledge into runtime enforcement mechanisms, but operates at the tool-call level (constraining which API functions the agent invokes) rather than at the token level (constraining which tokens the decoder produces), and requires an agentic multi-step workflow rather than single-pass autoregressive generation.
82	\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms, a middle ground between unconstrained generation and hard enforcement that reduces but cannot eliminate violations.
83	Post-hoc validation detects violations after generation and requires rejection or correction cycles that waste compute. In our setting, 15.37\% of generated triples contain domain/range violations under unconstrained decoding, a substantial waste of generation effort.
84	OntoCoDec \emph{prevents} violations during decoding, redirecting probability mass to valid alternatives rather than discarding invalid outputs, with only marginal overhead from logits masking compared to the cost of regenerating or correcting violated triples.
85	Soft-constraint approaches such as ontology-weighted beam scoring reduce violation frequency but cannot eliminate it, whereas OntoCoDec substantially reduces violations (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED depending on model).
86	
87	% ===========================================================================
88	% Paradigm 5: Constrained Decoding Quality Concerns
89	% ===========================================================================
90	\paragraph{Quality Impact of Constrained Decoding.}
91	A growing body of work raises concerns that constrained decoding degrades LLM generation quality, particularly for reasoning-intensive tasks where format enforcement interferes with chain-of-thought processes.
92	\citet{tam2024letmespeak} conduct a comprehensive evaluation showing that rigid format constraints (JSON, XML) harm performance on math and multi-hop QA benchmarks but \emph{benefit} classification-style tasks such as slot filling, a distinction directly relevant to IE, which is fundamentally an extraction (classification-like) task rather than a reasoning task.
93	CRANE~\cite{banerjee2025crane} provides theoretical analysis of why restricting outputs to narrow grammars suppresses chain-of-thought reasoning by eliminating intermediate reasoning tokens, and proposes an alternating strategy between unconstrained reasoning phases and constrained output phases to mitigate this effect.
94	\citet{schall2025hiddencost} conduct a systematic study across 11 models and multiple benchmarks, finding 10--30\% semantic correctness degradation on reasoning tasks under structural constraints, with larger models showing greater absolute degradation.
95	\citet{zhou2026snowballing} identify ``structure snowballing,'' a failure mode where format compliance cognitive load traps models in repetitive structural patterns rather than improving reasoning during self-correction iterations.
96	These findings establish a legitimate concern for constrained decoding in reasoning-heavy applications.
97	However, information extraction occupies a fundamentally different regime: the model extracts entities and relations from input text rather than generating novel reasoning chains, and \citet{tam2024letmespeak}'s own results show that extraction-style tasks are robust to, or even benefit from, format constraints.
98	OntoCoDec addresses this concern empirically: domain/range violations decrease by 94\% on SciERC (15.37\%$\to$0.93\%) and 45--90\% on DocRED across two models, with F1-neutral impact on SciERC ($+$0.13pp, $p{=}0.58$) and significant R-F1 gains on DocRED (Qwen $p{<}0.001$, Llama $p{=}0.013$).
99	Critically, OntoCoDec's constraints target only type tokens (entity types, relation labels), leaving free-text spans (entity surface forms and their boundaries) entirely unconstrained, which minimizes the distribution distortion that causes quality degradation in reasoning tasks.
100	A two-pass variant (S2), explored in ablation (Section~5), separates extraction and constraint enforcement into distinct passes, analogous to CRANE's alternating strategy; however, our primary single-pass approach already avoids reasoning interference by constraining only type tokens while leaving free-text spans unconstrained.
101	
102	% ===========================================================================
103	% Our Approach
104	% ===========================================================================
105	\paragraph{Our Approach.}
106	OntoCoDec occupies a unique position in this landscape: it is the first system to \emph{automatically compile} IE ontologies, including domain/range axioms, into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement without manually authored rules.
107	Unlike vocabulary-constrained methods that restrict individual tokens to a fixed set, OntoCoDec enforces \emph{cross-field relational constraints} through a stateful entity registry that tracks extracted types during autoregressive generation; constraint evaluation is dynamic and depends on previously decoded content.
108	This approach is orthogonal to supervised IE methods and applicable to autoregressive LMs with logits access without model modification or additional training (evaluated on 7B--70B models across three tokenizer families).
109	Unlike training-based IE systems, OntoCoDec requires no constraint-specific training and substantially reduces type violations at inference time (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED); unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives with significant R-F1 gains on DocRED ($p \leq 0.013$) and F1-neutral impact on SciERC.
110	The two constraint layers, grammar (structural) and semantic (relational), compose via bitwise AND with an empirical enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1bfdce8-9c36-465a-8f18-c6063e75a468",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "41d7f693-2845-4011-b2c6-a5c8ebab9dc6",
  "sourceToolAssistantUUID": "b1bfdce8-9c36-465a-8f18-c6063e75a468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T06:35:24.684Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NzdGkXvMmJ2dhY1me9UcdL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d7f693-2845-4011-b2c6-a5c8ebab9dc6",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9FhNkVTBJNXuYHJye6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "821d2b17-fa56-49b9-b35e-7d0595f23fb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWFTXzLBK84CYmDWYFJceK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4780,
      "cache_read_input_tokens": 38336,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4780
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 38336,
          "cache_creation_input_tokens": 4780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4780,
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

_source line 44 · 2026-05-22T06:35:24.688Z_

<details><summary>↩ Tool result · `toolu_01NzdGkXvMmJ2dhY1me9UcdL`</summary>

```text
1	% Appendix: Full Proof of Proposition 1
2	% Level 2 (prefix-decidable with state) constraints are not context-free.
3	
4	\section{Full Proof of Proposition 1}
5	\label{app:pumping-lemma}
6	
7	We prove that domain/range type constraints for IE with unbounded entity sets cannot be expressed by any context-free grammar, using the pumping lemma for context-free languages.
8	
9	\begin{proof}
10	Define the language $L$ of valid IE outputs over ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ with $\mathcal{E} = \{\tau_A, \tau_B\}$, $\mathcal{R} = \{r\}$, and $\sigma(r) = \{(\tau_A, \tau_A)\}$ (i.e., $r$ requires both head and tail to be type $\tau_A$).
11	
12	An output string has the form:
13	\[
14	w = e_1\, e_2\, \cdots\, e_n\;\; \texttt{REL}(h{=}e_k,\, r,\, \tau^h)
15	\]
16	where each $e_i$ is an entity with type $\tau_{a_i} \in \{\tau_A, \tau_B\}$, and $\tau^h$ is the head type field of a relation triple referencing entity $e_k$ ($1 \leq k \leq n$).
17	
18	The type-validity constraint requires $\tau^h = \tau_{a_k}$ (the head type must match the referenced entity's type) \emph{and} $\tau^h \in \operatorname{dom}(r) = \{\tau_A\}$.
19	Combined: a string $w \in L$ if and only if $\tau_{a_k} = \tau_A$.
20	
21	Now consider strings of the specific form:
22	\[
23	w_n = \underbrace{\tau_B\; \tau_B\; \cdots\; \tau_B}_{n-1}\; \tau_A\;\; \texttt{REL}(h{=}e_n,\, r,\, \tau_A)
24	\]
25	where the first $n{-}1$ entities have type $\tau_B$ and only entity $e_n$ has type $\tau_A$.
26	The relation references $e_n$, so $\tau^h = \tau_A = \tau_{a_n}$, satisfying both the registry consistency and domain constraint.
27	Thus $w_n \in L$ for all $n$.
28	
29	Assume for contradiction that $L$ is context-free.
30	By the pumping lemma, there exists a pumping length $p$ such that any $w \in L$ with $|w| \geq p$ can be written as $w = uvxyz$ where:
31	\begin{enumerate}[label=(\roman*)]
32	    \item $|vy| \geq 1$,
33	    \item $|vxy| \leq p$,
34	    \item $uv^i xy^i z \in L$ for all $i \geq 0$.
35	\end{enumerate}
36	
37	Choose $w = w_n$ with $n > p$.
38	The entity list portion $\tau_B^{n-1}\, \tau_A$ has length $n > p$, so the pumpable region $vxy$ (with $|vxy| \leq p$) must lie entirely within the entity list (it cannot span from the entity list to the relation reference, which is separated by $n - p > 0$ entity tokens from the start).
39	
40	\textbf{Case 1:} $v$ or $y$ contains entity tokens from the $\tau_B^{n-1}$ prefix.
41	Pumping up ($i = 2$): $uv^2 xy^2 z$ inserts additional $\tau_B$ entities, increasing $n$ to some $n' > n$.
42	But the relation reference still points to entity $e_n$ (at the original position), which is now at a different position in the longer entity list.
43	The entity at position $n$ in the pumped string is $\tau_B$ (since we inserted $\tau_B$ tokens before position $n$, shifting $\tau_A$ to position $n' > n$).
44	Thus $\tau^h = \tau_A \neq \tau_B = \tau_{a_n'}$, where $n'$ is the new position of entity $e_n$.
45	More precisely: the relation references a fixed entity name $e_k$, but pumping changes the entity-type binding at that name's position.
46	Since the pumped string assigns $\tau_B$ at position $k$ (which originally had $\tau_A$), the type-validity constraint $\tau^h = \tau_{a_k} \in \operatorname{dom}(r)$ is violated.
47	Hence $uv^2 xy^2 z \notin L$, contradicting condition (iii).
48	
49	\textbf{Case 2:} $v$ or $y$ contains the $\tau_A$ token at position $n$.
50	Pumping down ($i = 0$): $uxz$ removes the only $\tau_A$ entity.
51	The relation's head entity reference now points to a position that either does not exist or has type $\tau_B$.
52	In either case, $\tau^h = \tau_A \neq \tau_B$, violating type validity.
53	Hence $uxz \notin L$, contradicting condition (iii).
54	
55	In both cases, the pumping lemma is violated, so $L$ is not context-free.
56	The key insight is that type-validity requires a \emph{binding} between an entity's type (assigned at an earlier position) and the relation's type field (at a later position), with the binding target determined by the entity name.
57	Pumping disrupts this binding by changing which entity occupies a given position, while the relation reference remains fixed---a cross-position dependency that pushdown automata cannot track with their LIFO stack discipline.
58	
59	OntoCoDec's semantic layer addresses this with a runtime entity registry $\mathcal{D}$ (a finite map), operating as a deterministic stateful transducer that provides random-access type lookups, beyond the expressive power of context-free grammars.
60	\end{proof}
61	
62	\paragraph{Finite entity sets.}
63	For a finite entity set $\mathcal{E}$ with canonical identifiers, the valid language $L_{\text{valid}} = \bigcap_i L_i$ is theoretically regular (a finite intersection of regular languages).
64	However, the corresponding DFA requires $O(|\mathcal{T}|^{|\mathcal{E}|})$ states---for SciERC with 6 entity types and typical documents containing 20+ entities, this exceeds $10^{15}$ states, rendering explicit construction impractical.
65	Moreover, real IE operates over open-vocabulary text spans rather than closed identifier sets, making the general (non-regular) formulation the appropriate model.
66	Proposition~1 motivates the runtime state-tracking architecture for this general case.
67	
68	\paragraph{Position indexing vs.\ name referencing.}
69	The proof above uses position-based entity indexing ($e_k$ at position $k$) for expository clarity.
70	In OntoCoDec's actual JSON output, relation triples reference entities by name strings rather than positional indices.
71	The core argument transfers directly: validating type consistency requires a name$\to$type lookup over dynamically generated bindings, which is a random-access map operation.
72	A PDA's LIFO stack cannot perform random-access retrieval by key (it can only inspect the top element), so the non-context-free result holds regardless of whether entities are referenced by position or by name.
73	The position-based formulation is a simplification that makes the pumping argument more transparent without weakening the conclusion.
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "821d2b17-fa56-49b9-b35e-7d0595f23fb1",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "30866026-5484-429f-bc72-84986fde0b92",
  "sourceToolAssistantUUID": "821d2b17-fa56-49b9-b35e-7d0595f23fb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-22T06:35:27.593Z_

Now let me read the appendix discussion and the section on the violation landscape, as well as check for the bibliography.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30866026-5484-429f-bc72-84986fde0b92",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9G7dWZyGAShU8HufCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2e2053a-c78d-4405-8b64-551aa7c12b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsxwnQVu7Y2dJCtxQGWt8T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7606,
      "cache_read_input_tokens": 43116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7606,
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

_source line 46 · 2026-05-22T06:35:29.992Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RmpdDcpuca1XWudw3Rx2us`</summary>

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
  "parentUuid": "e2e2053a-c78d-4405-8b64-551aa7c12b45",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9G7dWZyGAShU8HufCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a574c43-f931-44c9-8920-34ac3da6f1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsxwnQVu7Y2dJCtxQGWt8T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7606,
      "cache_read_input_tokens": 43116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7606,
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

_source line 47 · 2026-05-22T06:35:29.999Z_

<details><summary>↩ Tool result · `toolu_01RmpdDcpuca1XWudw3Rx2us`</summary>

```text
1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\S\ref{sec:composability}), near-eliminating DR (DR\,$\leq$\,0.09\%) with minimal overhead; and LoRA + beam S1 (\S\ref{sec:beam-results}), achieving zero total violations on SciERC under favorable conditions (1.54$\times$ latency).
8	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe to isolate constraint effects; R-F1 2--8 reflects absent task-specific training, not method failure.
9	The deployment-relevant evaluation is the fine-tuned setting (R-F1 40--46\%), where constraints compose with parameter optimization without degrading performance.
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	All constraints are defined from schema-level supervision, independently of the evaluation split.
15	The framework handles both sources without modification.
16	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
17	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
18	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a574c43-f931-44c9-8920-34ac3da6f1fd",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "8a4ecb8b-3bff-41ea-9cf9-25b1be11ef13",
  "sourceToolAssistantUUID": "5a574c43-f931-44c9-8920-34ac3da6f1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-22T06:35:30.420Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TWSjhxZTZndkWBUrAfa1ph`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a4ecb8b-3bff-41ea-9cf9-25b1be11ef13",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9G7dWZyGAShU8HufCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81c4fa78-b56d-46fb-aa1b-e5162a4bece0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsxwnQVu7Y2dJCtxQGWt8T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7606,
      "cache_read_input_tokens": 43116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7606,
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

_source line 49 · 2026-05-22T06:35:30.762Z_

<details><summary>↩ Tool result · `toolu_01TWSjhxZTZndkWBUrAfa1ph`</summary>

```text
1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.
27	\emph{Grammar-first fallback} occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations.
28	The token-level fallback rate (36.6\% on SciERC Llama) is inflated by continuation tokens of multi-token type names (e.g., \textsc{OtherScientificTerm}, averaging 2.87 BPE tokens); at semantically meaningful first-token positions, the rate is 0.04--5.7\% (zero-shot) and drops to $\leq$\,0.11\% under fine-tuning.
29	These events account for the residual DR that persists after constraint enforcement.
30	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
31	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
32	
33	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
34	On SciERC, Llama-3.1-8B shows $f_{\text{gf}} = 36.6\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\% effective coverage.
35	On DocRED, by contrast, Qwen3-8B shows $f_{\text{gf}} = 0.08\%$ (46 of 54{,}859), yielding 99.9\% coverage.
36	The large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.
37	DocRED types (\textsc{PER}, \textsc{ORG}, \textsc{LOC}, \textsc{TIME}, \textsc{NUM}, \textsc{MISC}) are all single-token, eliminating this inflation.
38	This metric directly quantifies the empirical enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
39	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
40	
41	%%% Fallback Causal Tracing %%%
42	% exp_ids: Task C causal tracing (Qwen/Llama × ZS/FT × S1)
43	
44	\paragraph{Fallback Causal Tracing.}
45	\label{app:causal-tracing}
46	
47	To establish that grammar-first fallback is the \emph{sole} mechanism producing residual DR violations, we instrument the constraint processor to log, for each violation, whether the semantic mask was active ($S(t) \cap G(t) \neq \emptyset$) or bypassed via fallback ($S(t) \cap G(t) = \emptyset$) at the type-bearing position.
48	Table~\ref{tab:causal-tracing} reports the results across four SciERC configurations.
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\begin{tabular}{@{}ll rrr@{}}
54	\toprule
55	\textbf{Model} & \textbf{Setting} & \textbf{Fallback Rate} & \textbf{DR} & \textbf{From FB} \\
56	\midrule
57	Qwen3-8B  & FT S1 & 0/2256 (0\%)    & 0  & N/A \\
58	Qwen3-8B  & ZS S1 & 16/3458 (0.46\%) & 16 & 100\% \\
59	Llama-3.1-8B & FT S1 & 1/2162 (0.05\%) & 1  & 100\% \\
60	Llama-3.1-8B & ZS S1 & 1/2630 (0.04\%) & 1  & 100\% \\
61	\bottomrule
62	\end{tabular}
63	\caption{Fallback causal tracing on SciERC (551 documents). Fallback Rate: type-bearing positions where $S(t) \cap G(t) = \emptyset$ triggers grammar-first fallback. DR: residual domain/range violations. From FB: fraction of DR violations occurring at fallback positions. All violations occur exclusively at tail\_type positions (range constraints are tighter than domain constraints).}
64	\label{tab:causal-tracing}
65	\end{table}
66	
67	When the semantic mask is active, $\text{DR}_{\text{independent}} = 0$: the type constraint processor structurally prevents domain/range violations.
68	All 18 residual DR violations across four configurations occur exclusively at fallback positions, confirming that grammar-first fallback is a necessary condition for residual DR.
69	Fine-tuning reduces fallback to near-zero ($\leq$0.05\%), effectively eliminating the sole source of residual violations.
70	All fallback events occur at tail\_type positions, where $|\operatorname{range}(r, \tau^h)|$ is smaller than $|\operatorname{dom}(r)|$, making the intersection $S(t) \cap G(t)$ more likely to be empty.
71	
72	%%% CF-DR Trade-off Analysis %%%
73	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
74	
75	\paragraph{CF-DR Trade-off Analysis.}
76	\label{app:cf-dr-tradeoff}
77	
78	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
79	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
80	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\begin{tabular}{@{}l rrrr@{}}
86	\toprule
87	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
88	\midrule
89	Full S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
90	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
91	\midrule
92	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
93	\bottomrule
94	\end{tabular}
95	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\% for SciERC Qwen; \S\ref{sec:greedy-limitation}).}
96	\label{tab:cf-dr-tradeoff}
97	\end{table}
98	
99	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
100	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
101	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
102	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
103	The token-level grammar-first fallback is triggered at 36.64\% of type-bearing positions (0.46\% at first-token positions; \S\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.
104	
105	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
106	Within this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
107	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.
108	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
109	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
110	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
111	
112	Two complementary paths can lower CF without re-routing it to DR.
113	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
114	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
115	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
116	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
117	
118	%%% Dual-Factor Quantitative Analysis %%%
119	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
120	%          llama_scierc_full_s1, llama_docred_full_s1
121	
122	\paragraph{Dual-Factor Quantitative Analysis.}
123	\label{app:dual-factor}
124	
125	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
126	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
127	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
128	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
129	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
130	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
131	
132	\begin{figure}[t]
133	\centering
134	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
135	\caption{Residual DR vs.\ Schema Restrictiveness $\times$ Baseline Violation Rate ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$) across four model$\times$dataset configurations.
136	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}
137	\label{fig:dual-factor-scatter}
138	\end{figure}
139	
140	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
141	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
142	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
143	
144	\paragraph{Dataset-Dependent F1 Impact.}
145	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
146	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
147	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
148	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp); F1 gain magnitude is proportional to baseline OOV rate.
149	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
150	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
151	
152	%%% Paragraph 1: Low F1 Practical Significance %%%
153	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
154	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
155	
156	\paragraph{Practical Significance of Zero-Shot F1.}
157	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
158	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
159	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
160	Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
161	% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval
162	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
163	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
164	
165	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
166	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
167	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
168	
169	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
170	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
171	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
172	However, this precision gain comes at substantial cost.
173	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
174	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
175	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
176	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
177	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
178	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
179	
180	%%% CF Violation Distribution %%%
181	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
182	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
183	
184	\paragraph{Cross-Field Violation Distribution.}
185	\label{app:cf-distribution}
186	
187	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise; no mention triggered $\geq$3 types).
188	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
189	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
190	
191	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
192	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
193	
194	\begin{table}[t]
195	\centering
196	\small
197	\begin{tabular}{@{}lr r@{}}
198	\toprule
199	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
200	\midrule
201	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
202	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
203	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
204	Method $\leftrightarrow$ Task & 20 & 8.2 \\
205	Material $\leftrightarrow$ Method & 17 & 6.9 \\
206	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
207	\midrule
208	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
209	\midrule
210	\textbf{Total} & \textbf{245} & 100.0 \\
211	\bottomrule
212	\end{tabular}
213	\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).
214	All 245 violations are pairwise conflicts.
215	Conflicts involving \textsc{Generic} account for 63.3\%.}
216	\label{tab:cf-distribution}
217	\end{table}
218	
219	%%% Per-Relation DR Elimination under Fine-Tuning %%%
220	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
221	
222	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
223	\label{app:lora-per-relation}
224	
225	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
226	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
227	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
228	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
229	
230	\begin{table}[t]
231	\centering
232	\small
233	\begin{tabular}{@{}l r rr rr@{}}
234	\toprule
235	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
236	\cmidrule(lr){3-4} \cmidrule(l){5-6}
237	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
238	\midrule
239	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
240	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
241	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
242	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
243	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
244	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
245	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
246	\bottomrule
247	\end{tabular}
248	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
249	$\kappa$: constraint tightness; $n$: predicted triple count.
250	Used-for gains one triple from Evaluate-for redirection.}
251	\label{tab:lora-per-relation}
252	\end{table}
253	
254	%%% Fine-Tuned Four-Way Ablation %%%
255	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
256	
257	\paragraph{Fine-Tuned Four-Way Ablation.}
258	\label{app:ft-ablation}
259	
260	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
261	
262	\begin{table}[t]
263	\centering
264	\small
265	\setlength{\tabcolsep}{3pt}
266	\resizebox{\columnwidth}{!}{%
267	\begin{tabular}{@{}lll rrrrr rr@{}}
268	\toprule
269	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
270	\midrule
271	\multirow{8}{*}{SciERC}
272	  & \multirow{4}{*}{Qwen3-8B}
273	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
274	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
275	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
276	  & & Full S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
277	  \cmidrule(l){2-10}
278	  & \multirow{4}{*}{Llama-3.1-8B}
279	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
280	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
281	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
282	  & & Full S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
283	\midrule
284	\multirow{8}{*}{DocRED}
285	  & \multirow{4}{*}{Qwen3-8B}
286	    & Unconstrained & 0.56 & 0.27 & 0.00 & 0.08 & 7.11 & 82.35 & 40.89 \\
287	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
288	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
289	  & & Full S1       & \textbf{0.00} & 0.00 & 0.00 & 0.22 & 8.52 & 81.87 & 40.79 \\
290	  \cmidrule(l){2-10}
291	  & \multirow{4}{*}{Llama-3.1-8B}
292	    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 84.77 & 44.55 \\
293	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
294	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
295	  & & Full S1       & \textbf{0.00} & 0.00 & 0.00 & 0.26 & 2.51 & 84.71 & 44.70 \\
296	\bottomrule
297	\end{tabular}}%
298	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
299	DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
300	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
301	Semantic layer is the sole effective DR defense, providing 39--69\% reduction.
302	F1 cost is negligible: max $\Delta$R-F1 = $-$0.10\,pp (Qwen DocRED, full vs.\ unconstrained).}
303	\label{tab:ft-ablation}
304	\end{table}
305	
306	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
307	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--69\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$63\%, Llama $-$39\%).
308	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.09\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
309	F1 cost is negligible: the maximum R-F1 decrease across full S1 vs.\ unconstrained is $-$0.10\,pp (Qwen DocRED).
310	
311	%%% Residual DR Error Analysis (Fine-Tuned) %%%
312	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
313	
314	\paragraph{Residual DR Error Analysis.}
315	\label{app:residual-dr-analysis}
316	
317	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ full S1), only 36 domain/range violations remain.
318	Manual inspection reveals four root causes:
319	
320	\begin{enumerate}[nosep,leftmargin=*]
321	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
322	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
323	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
324	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
325	\end{enumerate}
326	
327	Two dataset-specific patterns emerge.
328	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
329	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
330	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.
331	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
332	
333	%%% Post-Hoc Filtering Comparison (Extended) %%%
334	% exp_ids: posthoc_*_zs, posthoc_*_ft
335	
336	\paragraph{Post-Hoc Filtering: Extended Comparison.}
337	\label{app:posthoc-extended}
338	
339	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
340	
341	\begin{table}[t]
342	\centering
343	\small
344	\setlength{\tabcolsep}{3pt}
345	\resizebox{\columnwidth}{!}{%
346	\begin{tabular}{@{}lll rrr l@{}}
347	\toprule
348	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
349	\midrule
350	\multirow{6}{*}{ZS}
351	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
352	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
353	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
354	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
355	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
356	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
357	\midrule
358	\multirow{4}{*}{FT}
359	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
360	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
361	  & Qwen    & DocRED & 1.03 & 41.11 & 40.79 & ph \\
362	  & Llama   & DocRED & 0.64 & 43.92 & 44.70 & cd \\
363	\bottomrule
364	\end{tabular}}%
365	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
366	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
367	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
368	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
369	F1 $\times$100.}
370	\label{tab:posthoc-extended}
371	\end{table}
372	
373	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
374	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
375	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
376	
377	%%% Zero-Shot Runtime Profiling %%%
378	
379	\paragraph{Zero-Shot Runtime Profiling.}
380	\label{app:runtime}
381	
382	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and Full S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
383	On DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.
384	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
385	
386	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
387	\paragraph{Fine-Tuned Latency Profiling.}
388	\label{app:ft-latency}
389	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and Full S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
390	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
391	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
392	
393	%%% Fuzzy Relation Matching %%%
394	
395	\paragraph{Relation Matching Protocol.}
396	\label{app:fuzzy-matching}
397	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
398	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
399	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
400	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
401	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
402	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
403	
404	%%% Per-Relation Violation Landscape %%%
405	
406	\paragraph{Per-Relation Violation Landscape.}
407	\label{app:per-relation-landscape}
408	
409	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
410	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
411	
412	\begin{table}[t]
413	\centering
414	\small
415	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
416	\label{tab:prompt_comparison}
417	\resizebox{\columnwidth}{!}{%
418	\begin{tabular}{ll cccc}
419	\toprule
420	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
421	\midrule
422	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
423	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
424	\midrule
425	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
426	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
427	\bottomrule
428	\end{tabular}}
429	\end{table}
430	
431	\begin{figure}[t]
432	\centering
433	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
434	\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$. Llama-3.1-8B shows similar per-relation patterns (Appendix~\ref{app:llama-per-relation}).}
435	\label{fig:per_relation_dr}
436	\end{figure}
437	
438	%%% WikiEvents Extended %%%
439	
440	\paragraph{WikiEvents Dataset Details.}
441	\label{app:wikievents}
442	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
443	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
444	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
445	
446	\paragraph{Constraint Tightness in WikiEvents.}
447	\label{app:wikievents-kappa}
448	% Data source: artifacts/w1c_wikievents_kappa_results.md
449	WikiEvents role-level tightness (with $|\mathcal{E}|{=}27$) has mean $\bar{\kappa}{=}0.82$ and median 0.89; 84\% of roles have $\kappa \geq 0.80$ (4 or fewer valid entity types out of 27).
450	The tightness-violation pattern extends to event extraction: roles with $\kappa \geq 0.90$ exhibit the highest AC rate (50\%), compared to 21\% for medium-tightness ($0.80 \leq \kappa < 0.90$) and 30\% for loose ($\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.
451	However, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\to$VEH) show 0\% AC despite $\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\to$CRM, Sentence$\to$SEN) show near-100\% AC because LLMs default to common types (PER, ORG).
452	The loose group's elevated rate (30\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\% AC, $\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.
453	
454	%%% Lucky Violation Analysis %%%
455	% exp_ids: task_e_lucky_violation_analysis
456	
457	\paragraph{Lucky Violation Analysis.}
458	\label{app:lucky-violations}
459	Table~\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.
460	A ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.
461	Across four fine-tuned configurations, lucky violations average 0.49\% of gold triples (range 0.01--0.51\%), confirming that nearly all removed DR violations are false positives.
462	On Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.
463	
464	\begin{table}[h]
465	\centering
466	\small
467	\resizebox{\columnwidth}{!}{%
468	\begin{tabular}{@{}llrrrr@{}}
469	\toprule
470	\textbf{Model} & \textbf{Dataset} & \textbf{DR (\%)} & \textbf{Lucky} & \textbf{$\Delta$Recall} & \textbf{Churn} \\
471	& & \textbf{unc$\to$con} & \textbf{(\% gold)} & \textbf{(pp)} & \textbf{(\%)} \\
472	\midrule
473	Qwen3-8B  & SciERC & 1.95$\to$0    & 4 (0.41\%) & $-$0.10 & 0.22 \\
474	Llama-8B  & SciERC & 1.11$\to$0.09 & 5 (0.51\%) & $\pm$0.00 & 0 \\
475	Qwen3-8B  & DocRED & 1.03$\to$0.01 & 1 (0.01\%) & $-$0.84 & 2.05 \\
476	Llama-8B  & DocRED & 0.64$\to$0.21 & 1 (0.01\%) & $-$0.10 & 0.86 \\
477	\midrule
478	\multicolumn{2}{@{}l}{\textit{Average}} & & \textit{0.49\%} & $-$0.26 & 0.78 \\
479	\bottomrule
480	\end{tabular}}
481	\caption{Lucky violation analysis across four LoRA fine-tuned configurations.
482	Lucky: count (and \% of gold triples) of constraint-removed violations matching gold labels.
483	$\Delta$Recall: recall change from unconstrained to constrained.
484	Churn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}
485	\label{tab:lucky-violations}
486	\end{table}
487	
488	%%% Trie-Only Baseline %%%
489	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
490	
491	\paragraph{Trie-Only Baseline (GCD-Equivalent).}
492	\label{app:trie-baseline}
493	Table~\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.
494	The trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\%, RV${=}$0\% across all configurations), functionally equivalent to GCD's~\cite{geng2023gcd} constrained decoding.
495	However, without grammar-level JSON enforcement, models systematically omit entity type fields (83\% of triples) or produce malformed JSON (0--51\% parse failure), causing DR to rise to 15--96\%---far worse than unconstrained baselines.
496	This confirms the grammar layer is a structural prerequisite: vocabulary constraints operate correctly in isolation but require JSON scaffolding to reach the positions where they apply.
497	
498	\begin{table}[h]
499	\centering
500	\small
501	\resizebox{\columnwidth}{!}{%
502	\begin{tabular}{@{}ll rrrr rr@{}}
503	\toprule
504	\textbf{Model} & \textbf{Setting}
505	  & \textbf{ET\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{DR\,$\downarrow$} & \textbf{CF}
506	  & \textbf{R-F1\,$\uparrow$} & \textbf{PF\,(\%)} \\
507	\midrule
508	\multirow{2}{*}{Qwen3-8B}
509	  & LoRA  & 0 & 0 & 95.5  & 0.09 & 42.57 & 9.1 \\
510	  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\
511	\multirow{2}{*}{Llama-8B}
512	  & LoRA  & 0 & 0 & 15.2$^\dagger$  & 0    & 41.42 & 50.8 \\
513	  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\
514	\midrule
515	\multicolumn{8}{@{}l}{\textit{Comparison with OntoCoDec S1:}} \\
516	\midrule
517	& & \multicolumn{2}{c}{\textbf{S1 DR\,(\%)}} & \textbf{Trie DR\,(\%)} & \multicolumn{2}{c}{\textbf{DR Gap (pp)}} & \\
518	\cmidrule(lr){3-4} \cmidrule(lr){5-5} \cmidrule(lr){6-7}
519	Qwen3-8B  & LoRA  & \multicolumn{2}{c}{0}    & 95.5  & \multicolumn{2}{c}{95.5}  & \\
520	Qwen3-8B  & ZS    & \multicolumn{2}{c}{0.93} & 29.3  & \multicolumn{2}{c}{28.4}  & \\
521	Llama-8B  & LoRA  & \multicolumn{2}{c}{0.09} & 15.2  & \multicolumn{2}{c}{15.1}  & \\
522	Llama-8B  & ZS    & \multicolumn{2}{c}{0.08} & 84.4  & \multicolumn{2}{c}{84.3}  & \\
523	\bottomrule
524	\end{tabular}}
525	\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.
526	Top: full trie-only metrics (ET/RV/DR/CF: violation rates \%; R-F1 $\times$100; PF: parse failure rate).
527	Trie achieves ET${=}$0\%, RV${=}$0\% but DR rises to 15--96\% because models omit type fields without structural enforcement.
528	Bottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.
529	$^\dagger$50.8\% parse failure rate.}
530	\label{tab:trie-baseline}
531	\end{table}
532	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81c4fa78-b56d-46fb-aa1b-e5162a4bece0",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "61faa52e-f63e-4b32-bc99-cc99d71373bf",
  "sourceToolAssistantUUID": "81c4fa78-b56d-46fb-aa1b-e5162a4bece0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-22T06:35:30.852Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TFSCyAS6zrNFWsfqha8uB4`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61faa52e-f63e-4b32-bc99-cc99d71373bf",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9G7dWZyGAShU8HufCe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad53e1e4-9b3f-4fc7-8b1e-1ac0a9f1ef3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsxwnQVu7Y2dJCtxQGWt8T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7606,
      "cache_read_input_tokens": 43116,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7606
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 43116,
          "cache_creation_input_tokens": 7606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7606,
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

_source line 51 · 2026-05-22T06:35:30.878Z_

<details><summary>↩ Tool result · `toolu_01TFSCyAS6zrNFWsfqha8uB4`</summary>

```text
artifacts/_project/paper/new_citations.bib
artifacts/_project/paper/relwork_new_entries.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad53e1e4-9b3f-4fc7-8b1e-1ac0a9f1ef3d",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "273ded58-3e90-4305-bca5-2a5da17414d3",
  "sourceToolAssistantUUID": "ad53e1e4-9b3f-4fc7-8b1e-1ac0a9f1ef3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-22T06:35:34.765Z_

<details open><summary>🔧 Tool call — Read · `toolu_016xiNU8u1NwDqnLZFnfZdWC`</summary>

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
  "parentUuid": "273ded58-3e90-4305-bca5-2a5da17414d3",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9GaAwXvsBsuVWdQ4uq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2669f42-fe41-4390-a15e-76b4ccbf79db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnYU34nNNzqfDTrtv1wPKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16493,
      "cache_read_input_tokens": 50722,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16493
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 50722,
          "cache_creation_input_tokens": 16493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16493,
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

_source line 53 · 2026-05-22T06:35:35.083Z_

<details><summary>↩ Tool result · `toolu_016xiNU8u1NwDqnLZFnfZdWC`</summary>

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
362	  booktitle = {Proceedings of the Workshop on Generative {AI} and Knowledge Graphs ({GenAIK}) at {COLING} 2025},
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
401	% D015 reviewer-requested references (5 entries)
402	% ============================================================
403	
404	% Confirmed via: ACL Anthology 2021.findings-emnlp.204, GitHub Babelscape/rebel
405	@inproceedings{cabot2021rebel,
406	  title     = {{REBEL}: Relation Extraction By End-to-end Language Generation},
407	  author    = {Huguet Cabot, Pere-Llu{\'\i}s and Navigli, Roberto},
408	  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2021},
409	  pages     = {2370--2381},
410	  year      = {2021},
411	  url       = {https://aclanthology.org/2021.findings-emnlp.204/}
412	}
413	
414	% ============================================================
415	% Batch 3: New entries added 2026-05-16 (3 entries, Director-requested)
416	% ============================================================
417	
418	% Confirmed via: arXiv:2403.01632, OpenReview HiUZtgAPoH, Illinois Experts page
419	% NOTE: Director specified ICML 2024 — verify volume/pages
420	@inproceedings{ugare2024syncode,
421	  title     = {{SynCode}: {LLM} Generation with Grammar Augmentation},
422	  author    = {Ugare, Shubham and Suresh, Tarun and Kang, Hangoo and Misailovic, Sasa and Singh, Gagandeep},
423	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
424	  year      = {2024},
425	  series    = {PMLR},
426	  volume    = {235},
427	  url       = {https://arxiv.org/abs/2403.01632}
428	}
429	
430	% Confirmed via: OpenReview ac93gRzxxV, ICLR 2025 poster page, arXiv:2410.07295
431	@inproceedings{ugare2025itergen,
432	  title     = {{IterGen}: Iterative Semantic-aware Structured {LLM} Generation with Backtracking},
433	  author    = {Ugare, Shubham and Suresh, Tarun and Banerjee, Debangshu and Misailovic, Sasa and Singh, Gagandeep},
434	  booktitle = {The Thirteenth International Conference on Learning Representations},
435	  year      = {2025},
436	  url       = {https://openreview.net/forum?id=ac93gRzxxV}
437	}
438	
439	% Confirmed via: ACL Anthology 2025.emnlp-main.926, arXiv:2506.14901, EPFL dlab
440	@inproceedings{boostcd2025,
441	  title     = {Combining Constrained and Unconstrained Decoding via Boosting: {BoostCD} and Its Application to Information Extraction},
442	  author    = {Sakota, Marija and Geng, Saibo and Josifoski, Martin and West, Robert},
443	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
444	  year      = {2025},
445	  url       = {https://aclanthology.org/2025.emnlp-main.926/}
446	}
447	
448	% ============================================================
449	% Dataset & model references (5 entries)
450	% ============================================================
451	
452	% Confirmed via: ACL Anthology D18-1360, arXiv:1808.09602
453	@inproceedings{luan2018scierc,
454	  title     = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
455	  author    = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
456	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
457	  pages     = {3219--3232},
458	  year      = {2018},
459	  address   = {Brussels, Belgium},
460	  url       = {https://aclanthology.org/D18-1360/}
461	}
462	
463	% Confirmed via: ACL Anthology P19-1074, arXiv:1906.06127
464	@inproceedings{yao2019docred,
465	  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
466	  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
467	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
468	  pages     = {764--777},
469	  year      = {2019},
470	  address   = {Florence, Italy},
471	  url       = {https://aclanthology.org/P19-1074/}
472	}
473	
474	% Confirmed via: arXiv:2302.10205, Semantic Scholar
475	@article{wei2023zeroshot,
476	  title   = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},
477	  author  = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},
478	  journal = {arXiv preprint arXiv:2302.10205},
479	  year    = {2023},
480	  url     = {https://arxiv.org/abs/2302.10205}
481	}
482	
483	% Confirmed via: arXiv:2505.09388, Hugging Face model cards
484	@article{qwen2025qwen3,
485	  title   = {Qwen3 Technical Report},
486	  author  = {{Qwen Team}},
487	  journal = {arXiv preprint arXiv:2505.09388},
488	  year    = {2025},
489	  url     = {https://arxiv.org/abs/2505.09388}
490	}
491	
492	% Confirmed via: NeurIPS 2024 proceedings, arXiv:2312.07104
493	@inproceedings{zheng2024sglang,
494	  title     = {{SGLang}: Efficient Execution of Structured Language Model Programs},
495	  author    = {Zheng, Lianmin and Yin, Liangsheng and Xie, Zhiqiang and Sun, Chuyue and Huang, Jeff and Yu, Cody Hao and Cao, Shiyi and Kozyrakis, Christos and Stoica, Ion and Gonzalez, Joseph E. and Barrett, Clark and Sheng, Ying},
496	  booktitle = {Advances in Neural Information Processing Systems},
497	  volume    = {37},
498	  year      = {2024},
499	  url       = {https://arxiv.org/abs/2312.07104}
500	}
501	
502	% Confirmed via: ACL Anthology 2021.naacl-main.69
503	@inproceedings{li2021document,
504	  title     = {Document-Level Event Argument Extraction by Conditional Generation},
505	  author    = {Li, Sha and Ji, Heng and Han, Jiawei},
506	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
507	  pages     = {894--908},
508	  year      = {2021},
509	  url       = {https://aclanthology.org/2021.naacl-main.69/}
510	}
511	
512	% ============================================================
513	% New citations added 2026-05-18 (literature freshness check)
514	% ============================================================
515	
516	% grammar_aligned_2024 removed: duplicate of park2024grammar (same paper)
517	
518	@article{formattax2026,
519	    author    = {Ivan Yee Lee and Loris D'Antoni and Taylor Berg-Kirkpatrick},
520	    title     = {The Format Tax},
521	    journal   = {arXiv preprint arXiv:2604.03616},
522	    year      = {2026},
523	    url       = {https://arxiv.org/abs/2604.03616},
524	}
525	
526	@article{dccd2026,
527	    author    = {Avinash Reddy and Thayne T. Walker and James S. Ide and Amrit Singh Bedi},
528	    title     = {Draft-Conditioned Constrained Decoding for Structured Generation in {LLMs}},
529	    journal   = {arXiv preprint arXiv:2603.03305},
530	    year      = {2026},
531	    url       = {https://arxiv.org/abs/2603.03305},
532	}
533	
534	@inproceedings{guidex2025,
535	    author    = {Neil De La Fuente and Oscar Sainz and Iker Garc{\'\i}a-Ferrero and Eneko Agirre},
536	    title     = {{GUIDEX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},
537	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
538	    year      = {2025},
539	    publisher = {Association for Computational Linguistics},
540	    url       = {https://aclanthology.org/2025.findings-acl.1245/},
541	}
542	
543	@article{jsonschemabench2025,
544	    author    = {Saibo Geng and Hudson Cooper and Micha{\l} Moskal and Samuel Jenkins and Julian Berman and Nathan Ranchin and Robert West and Eric Horvitz and Harsha Nori},
545	    title     = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},
546	    journal   = {arXiv preprint arXiv:2501.10868},
547	    year      = {2025},
548	    url       = {https://arxiv.org/abs/2501.10868},
549	}
550	
551	% ============================================================
552	% Round 9 SF6 references (5 entries)
553	% ============================================================
554	
555	% Confirmed via: arXiv:2304.08085
556	@article{wang2023instructuie,
557	  title     = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
558	  author    = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
559	  journal   = {arXiv preprint arXiv:2304.08085},
560	  year      = {2023},
561	  url       = {https://arxiv.org/abs/2304.08085}
562	}
563	
564	% Confirmed via: ACL Anthology 2022.findings-acl.67
565	@inproceedings{wang2022deepstruct,
566	  title     = {{DeepStruct}: Pretraining of Language Models for Structure Prediction},
567	  author    = {Wang, Chenguang and Liu, Xiao and Chen, Zui and Hong, Haoyun and Tang, Jie and Song, Dawn},
568	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
569	  pages     = {803--823},
570	  year      = {2022},
571	  doi       = {10.18653/v1/2022.findings-acl.67},
572	  url       = {https://aclanthology.org/2022.findings-acl.67}
573	}
574	
575	% Confirmed via: OpenReview r65xfUb76p, ICLR 2024
576	@inproceedings{zhou2024universalner,
577	  title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
578	  author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
579	  booktitle = {The Twelfth International Conference on Learning Representations},
580	  year      = {2024},
581	  url       = {https://openreview.net/forum?id=r65xfUb76p}
582	}
583	
584	% Confirmed via: AAAI 2023 proceedings, doi:10.1609/aaai.v37i11.26563
585	@inproceedings{lou2023usm,
586	  title     = {Universal Information Extraction as Unified Semantic Matching},
587	  author    = {Lou, Jie and Lu, Yaojie and Dai, Dai and Jia, Wei and Lin, Hongyu and Han, Xianpei and Sun, Le and Wu, Hua},
588	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
589	  volume    = {37},
590	  number    = {11},
591	  pages     = {13318--13326},
592	  year      = {2023},
593	  doi       = {10.1609/aaai.v37i11.26563},
594	  url       = {https://ojs.aaai.org/index.php/AAAI/article/view/26563}
595	}
596	
597	% Confirmed via: ACL Anthology 2023.acl-long.868
598	@inproceedings{wadhwa2023revisiting,
599	  title     = {Revisiting Relation Extraction in the era of Large Language Models},
600	  author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
601	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
602	  pages     = {15566--15589},
603	  year      = {2023},
604	  doi       = {10.18653/v1/2023.acl-long.868},
605	  url       = {https://aclanthology.org/2023.acl-long.868}
606	}
607	
608	% ============================================================
609	% R12 reviewer-requested references
610	% ============================================================
611	
612	% ============================================================
613	% R13 SF5 references (F1 anchoring)
614	% ============================================================
615	
616	
617	% Confirmed via: OpenReview, ICLR 2021
618	@inproceedings{paolini2021tanl,
619	  title     = {Structured Prediction as Translation between Augmented Natural Languages},
620	  author    = {Paolini, Giovanni and Aky{\"u}rek, Ben and Aky{\"u}rek, Ekin and O{\u{g}}uz, Barlas},
621	  booktitle = {International Conference on Learning Representations},
622	  year      = {2021},
623	  url       = {https://openreview.net/forum?id=US-TP-xnXI}
624	}
625	
626	% ============================================================
627	% R12 reviewer-requested references
628	% ============================================================
629	
630	% Confirmed via: NeurIPS 2022 proceedings, arXiv:2304.06248
631	@inproceedings{fei2022lasuie,
632	  title     = {{LasUIE}: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model},
633	  author    = {Fei, Hao and Wu, Shengqiong and Li, Jingye and Li, Bobo and Li, Fei and Qin, Libo and Zhang, Meishan and Zhang, Min and Chua, Tat-Seng},
634	  booktitle = {Advances in Neural Information Processing Systems},
635	  volume    = {35},
636	  year      = {2022},
637	  url       = {https://arxiv.org/abs/2304.06248}
638	}
639	
640	% Confirmed via: ACL Anthology, EMNLP-CoNLL 2010 (originally 2009 workshop)
641	@inproceedings{riedel2010modeling,
642	  title     = {Modeling Relations and Their Mentions without Labeled Text},
643	  author    = {Riedel, Sebastian and Yao, Limin and McCallum, Andrew},
644	  booktitle = {Joint European Conference on Machine Learning and Knowledge Discovery in Databases},
645	  pages     = {148--163},
646	  year      = {2010},
647	  publisher = {Springer}
648	}
649	
650	% Confirmed via: CVPR 2017 proceedings
651	@inproceedings{anderson2017guided,
652	  title     = {Guided Open Vocabulary Image Captioning with Constrained Beam Search},
653	  author    = {Anderson, Peter and Fernando, Basura and Johnson, Mark and Gould, Stephen},
654	  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing},
655	  pages     = {936--945},
656	  year      = {2017},
657	  publisher = {Association for Computational Linguistics}
658	}
659	
660	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2669f42-fe41-4390-a15e-76b4ccbf79db",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "762129d2-f5a3-455a-9111-5d5b84abd974",
  "sourceToolAssistantUUID": "d2669f42-fe41-4390-a15e-76b4ccbf79db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-22T06:35:38.797Z_

Now let me also read the distilled research skill to understand the landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "762129d2-f5a3-455a-9111-5d5b84abd974",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9GtdwaEn7jEmDb8F1v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffb8af18-a0b2-4553-b67f-57d2cce69270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjMP4bg9XYJ12tg3wivbpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13002,
      "cache_read_input_tokens": 67215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13002,
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

_source line 55 · 2026-05-22T06:35:40.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V7VZTE7LcfBtEuv3grPgAj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/skills/projects/schema_semantic_constrained_ie/distilled-research.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffb8af18-a0b2-4553-b67f-57d2cce69270",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9GtdwaEn7jEmDb8F1v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d52c919-84d8-4d93-8461-ae5ce29ed1db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjMP4bg9XYJ12tg3wivbpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13002,
      "cache_read_input_tokens": 67215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13002,
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

_source line 56 · 2026-05-22T06:35:40.691Z_

<details><summary>↩ Tool result · `toolu_01V7VZTE7LcfBtEuv3grPgAj`</summary>

```text
1	---
2	name: Schema-Semantic Constrained IE Research Patterns
3	description: 从10篇论文蒸馏的约束解码+结构化IE领域研究共识——实验设计、baseline选择、评估规范、方法论趋势
4	source_papers: 10 (8 deep + 2 abstract)
5	---
6	
7	## 方法论趋势
8	
9	**代码式 schema 表示取代 NL 描述**（3/10，GoLLIE/KnowCoder/CodeIE，置信度：高）
10	Python 类（继承、docstring、类型标注）编码 IE schema。GoLLIE 用 docstring 编码标注指南，KnowCoder 用类继承映射 30K+ Wikidata 类型，CodeIE 证明 Code-LLM 天然适配结构化输出。趋势：2023→2024 从 prompt 级到预训练级深化。
11	
12	**语法约束解码从 SQL 扩展到通用结构化生成**（5/10，PICARD→GCD→IterGen/CRANE/XGrammar，置信度：高）
13	演进轨迹：PICARD(2021)SQL 增量解析→GCD(2023)CFG 通用框架→IterGen(2025)回溯纠错→CRANE(2025)理论证明约束损害推理+语法增强恢复→XGrammar(2025)系统级近零开销。趋势从纯语法→语义感知→效率工程。
14	
15	**无微调推理时方法占半壁江山**（4/8深读，GCD/CodeIE/IterGen/CRANE，置信度：高）
16	few-shot + constrained decoding 与微调路线并列。CRANE 提供理论基础：有限语法将 LLM 表达限制在 TC0 复杂度类，语法增强可恢复。
17	
18	**约束-推理 tradeoff 成为核心议题**（3/10，CRANE/IterGen/BoostCD，置信度：中）
19	CRANE 理论证明严格约束损害推理，IterGen 用回溯缓解，BoostCD 用集成融合。这揭示约束解码不是免费午餐——需要机制设计来保护语义质量。
20	
21	## 实验设计共识
22	
23	**必选 Baseline**：GenIE（closed IE 标杆，3篇）、UIE/InstructUIE（通用IE，3篇）、Outlines/SGLang（约束解码系统，3篇）、LLaMA/CodeLLaMA（开源LLM，3篇）
24	
25	**必选数据集**：ACE05 NER+RE+Event（4篇）、CoNLL03 NER（3篇）、REBEL/Wiki-cIE closed IE（3篇）。约束解码系统论文额外需 JSON/SQL/XML 生成基准。
26	
27	**核心指标**：IE 任务以 micro-F1 为主（8/10），closed IE 加 macro-F1 反映长尾。约束解码论文必报 parse rate/validity rate（CRANE 100%，IterGen 验证）。系统论文报延迟（XGrammar per-token µs）。
28	
29	**消融必做维度**：①约束 vs 无约束效果对比（4/10）②核心组件逐步叠加/去除（GoLLIE p-value, XGrammar 248.6x cache 贡献）③模型尺寸 scaling（3/10）
30	
31	## 训练配方共识
32	
33	**LoRA/QLoRA 是 LLM-based IE 微调标配**（GoLLIE QLoRA 3e-4, KnowCoder LoRA rank=32 3e-4，置信度：高）
34	lr=3e-4 + cosine scheduler 是共识。A100 80GB 标配硬件。
35	
36	**XGrammar 的系统设计启示**：99% token 为 context-independent 可预计算，仅<1% 需运行时检查。160MB→0.46MB 内存压缩。GPU-CPU 重叠实现零开销。
37	
38	## 竞品 Claim 与研究空白
39	
40	**竞品**：KnowCoder（30K+类型 schema 库+两阶段训练），BoostCD（约束/无约束互补 boosting +17 F1）
41	
42	**共同局限**（≥2篇）：①闭源 API 不兼容（GCD, CRANE, CodeIE）②约束解码延迟（GCD 0.05-0.5s/token, IterGen 回溯开销, BoostCD 3次调用）③语法/schema 人工设计成本（PICARD, GCD）④训练数据质量（BoostCD 合成数据, KnowCoder 1.5B token 自动构造）
43	
44	**研究空白**：①代码 schema 表示 + 语法约束解码两条路线未融合——无论文同时使用 ②语义约束（超越语法合规）系统性方案缺失——仅 CRANE/IterGen 初步触及 ③动态 schema 适应（推理时 schema 变化）无方案 ④约束解码对 IE 特定任务（事件抽取、关系抽取）的针对性设计不足
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d52c919-84d8-4d93-8461-ae5ce29ed1db",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "081f3d63-23d7-49b4-a957-7c098c984029",
  "sourceToolAssistantUUID": "3d52c919-84d8-4d93-8461-ae5ce29ed1db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-22T06:35:41.475Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SVQNeFn9GyuQ2kUSgthnUH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "081f3d63-23d7-49b4-a957-7c098c984029",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9GtdwaEn7jEmDb8F1v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdd5e2ee-ef50-4f8d-bef7-306204db1d65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjMP4bg9XYJ12tg3wivbpU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13002,
      "cache_read_input_tokens": 67215,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13002
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 67215,
          "cache_creation_input_tokens": 13002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13002,
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

_source line 58 · 2026-05-22T06:35:41.480Z_

<details><summary>↩ Tool result · `toolu_01SVQNeFn9GyuQ2kUSgthnUH`</summary>

```text
1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=\textwidth]{figures/fig1_framework.pdf}
4	\caption{Overview of OntoCoDec. An IE ontology is compiled into two constraint layers: a grammar layer (context-free) and a semantic layer (prefix-decidable with state). At each decoding step, the final mask $M_{\text{final}}(t) = G(t) \cap S(t)$ ensures both structural and type validity; when $S(t) \cap G(t) = \emptyset$, grammar-first fallback preserves JSON integrity.}
5	\label{fig:framework}
6	\end{figure*}
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdd5e2ee-ef50-4f8d-bef7-306204db1d65",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "d3701371-63ee-40b7-8f7a-63f3c952fad4",
  "sourceToolAssistantUUID": "bdd5e2ee-ef50-4f8d-bef7-306204db1d65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-22T06:35:44.638Z_

Now I have a thorough understanding of the paper. Let me also check for some specific references that the review task asks about.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3701371-63ee-40b7-8f7a-63f3c952fad4",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9HMHpHNiwqCV8iS1j5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "266d49ee-1a8e-415b-84a4-adbde106dfd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXsL3M53re8mi4ccqn4erh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2033,
      "cache_read_input_tokens": 80217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2033,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 60 · 2026-05-22T06:35:46.991Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BFe6ttDDMJjhsig5DBzLAL`</summary>

```json
{
  "pattern": "SGLang|sglang|Guidance|microsoft.*guidance|GENRE|genre|InstructUIE|instructuie|USM|lou.*2023",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "266d49ee-1a8e-415b-84a4-adbde106dfd6",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9HMHpHNiwqCV8iS1j5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "473b4c30-3c9c-4fc2-a3e2-50827efeb7b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXsL3M53re8mi4ccqn4erh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2033,
      "cache_read_input_tokens": 80217,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2033
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 80217,
          "cache_creation_input_tokens": 2033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2033,
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

_source line 61 · 2026-05-22T06:35:47.037Z_

<details><summary>↩ Tool result · `toolu_01BFe6ttDDMJjhsig5DBzLAL`</summary>

```text
artifacts/_project/paper/main.bbl:69:  Petroni}]{decao2021genre}
artifacts/_project/paper/main.bbl:187:  Wu}]{lou2023usm}
artifacts/_project/paper/main.bbl:396:  Gui, Kang, Yang, Li, and Du}]{wang2023instructuie}
artifacts/_project/paper/main.bbl:400:\newblock \href {https://arxiv.org/abs/2304.08085} {{InstructUIE}: Multi-task
artifacts/_project/paper/main.bbl:459:  Stoica, Gonzalez, Barrett, and Sheng}]{zheng2024sglang}
artifacts/_project/paper/main.bbl:463:\newblock \href {https://arxiv.org/abs/2312.07104} {{SGLang}: Efficient
artifacts/_project/paper/section2_background.tex:18:XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
artifacts/_project/paper/section6_related_work.tex:11:GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
artifacts/_project/paper/main.aux:101:\citation{zheng2024sglang}
artifacts/_project/paper/main.aux:686:\citation{wang2023instructuie}
artifacts/_project/paper/main.aux:687:\citation{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner}
artifacts/_project/paper/main.aux:1019:\bibcite{decao2021genre}{{8}{2021}{{De~Cao et~al.}}{{De~Cao, Izacard, Riedel, and Petroni}}}
artifacts/_project/paper/main.aux:1140:\bibcite{lou2023usm}{{22}{2023}{{Lou et~al.}}{{Lou, Lu, Dai, Jia, Lin, Han, Sun, and Wu}}}
artifacts/_project/paper/main.aux:1280:\bibcite{wang2023instructuie}{{48}{2023}{{Wang et~al.}}{{Wang, Zhou, Zu, Xia, Chen, Zhang, Zheng, Ye, Zhang, Gui, Kang, Yang, Li, and Du}}}
artifacts/_project/paper/main.aux:1288:\bibcite{zheng2024sglang}{{56}{2024}{{Zheng et~al.}}{{Zheng, Yin, Xie, Sun, Huang, Yu, Cao, Kozyrakis, Stoica, Gonzalez, Barrett, and Sheng}}}
artifacts/_project/paper/main.aux:1529:\citation{decao2021genre}
artifacts/_project/paper/relwork_new_entries.bib:248:@inproceedings{decao2021genre,
artifacts/_project/paper/relwork_new_entries.bib:493:@inproceedings{zheng2024sglang,
artifacts/_project/paper/relwork_new_entries.bib:494:  title     = {{SGLang}: Efficient Execution of Structured Language Model Programs},
artifacts/_project/paper/relwork_new_entries.bib:556:@article{wang2023instructuie,
artifacts/_project/paper/relwork_new_entries.bib:557:  title     = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
artifacts/_project/paper/relwork_new_entries.bib:585:@inproceedings{lou2023usm,
artifacts/_project/paper/section6_relwork_outline.tex:46:In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, limiting each decoding step to tokens consistent with valid entity names.
artifacts/_project/paper/appendix_related_work.tex:41:In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, restricting each decoding step to tokens consistent with valid entity names from a predefined catalog.
artifacts/_project/paper/main.blg:12:Warning--can't use both volume and number fields in lou2023usm
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "473b4c30-3c9c-4fc2-a3e2-50827efeb7b0",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "b257d094-ba95-45ac-b9d7-446eec4e14a2",
  "sourceToolAssistantUUID": "473b4c30-3c9c-4fc2-a3e2-50827efeb7b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-22T06:35:52.967Z_

Good. The paper does cite SGLang, GENRE, InstructUIE, UIE, and USM. Let me now check if Microsoft's Guidance library is cited.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b257d094-ba95-45ac-b9d7-446eec4e14a2",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9HmFxynZvc2bizKXfE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c98d97e2-333c-4b27-ab38-cd12223a0edd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RxUZt61j2tQDAbtTNbfoi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 82250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 63 · 2026-05-22T06:35:53.755Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MMbxcS4qPmpbdcGXfm4CWu`</summary>

```json
{
  "pattern": "guidance|microsoft.*guidance|Guidance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c98d97e2-333c-4b27-ab38-cd12223a0edd",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9HmFxynZvc2bizKXfE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01418f6b-2bd3-41e3-9157-95c30e6593a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RxUZt61j2tQDAbtTNbfoi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 82250,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 82250,
          "cache_creation_input_tokens": 1461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1461,
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

_source line 64 · 2026-05-22T06:35:53.778Z_

<details><summary>↩ Tool result · `toolu_01MMbxcS4qPmpbdcGXfm4CWu`</summary>

```text
artifacts/_project/paper/section1_introduction_draft.tex:15:Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement; no method provides both semantic awareness and hard constraint enforcement.
artifacts/_project/paper/appendix_related_work.tex:63:Training-based methods provide \emph{soft} structural guidance: the model learns to prefer valid outputs but cannot enforce compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.
artifacts/_project/paper/appendix_related_work.tex:72:ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale, but constraint adherence relies on prompt-level guidance, not enforcement, leaving residual violations unaddressed.
artifacts/_project/paper/section6_relwork_outline.tex:79:\textbf{Distinction:} Training-based methods provide \emph{soft} structural guidance---the model learns to prefer valid outputs but offers no compliance guarantee at inference time. EnriCo's ASP constraints are hard but model-specific and require manual rule authoring. OntoCoDec provides \emph{hard} decoding-time enforcement that is training-free, automatically compiled from ontology schemas, and composable with any of these approaches.
artifacts/_project/paper/section6_relwork_outline.tex:90:ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale---but constraint adherence relies on prompt-level guidance, not enforcement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01418f6b-2bd3-41e3-9157-95c30e6593a5",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "61f0a7d9-3eea-4bdf-b730-f090e2ef5206",
  "sourceToolAssistantUUID": "01418f6b-2bd3-41e3-9157-95c30e6593a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-22T06:35:57.679Z_

Now I have all the information I need to write a thorough review. Let me also check one more detail -- the 70B LoRA results that seem to be placeholder "XX.XX" values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61f0a7d9-3eea-4bdf-b730-f090e2ef5206",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9JG73nxzzVVPsATsgd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8050813d-891d-482a-ad16-d57313e32c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SykXCDrmNxzQdyFeKBqn2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 83711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 616,
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

_source line 66 · 2026-05-22T06:35:58.301Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01ECDa4XAik2fue1ejkw4NcQ`</summary>

```json
{
  "pattern": "XX\\.XX",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8050813d-891d-482a-ad16-d57313e32c2b",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9JG73nxzzVVPsATsgd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6357137-21c0-4b75-b6f3-7ad9df2e6279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SykXCDrmNxzQdyFeKBqn2U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 616,
      "cache_read_input_tokens": 83711,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 616
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 83711,
          "cache_creation_input_tokens": 616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 616,
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

_source line 67 · 2026-05-22T06:35:58.317Z_

<details><summary>↩ Tool result · `toolu_01ECDa4XAik2fue1ejkw4NcQ`</summary>

```text
artifacts/_project/paper/section5_runtime.tex:19:LoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\%, consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6357137-21c0-4b75-b6f3-7ad9df2e6279",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "eda5064c-b2b8-4e37-9d75-c7451be1acae",
  "sourceToolAssistantUUID": "a6357137-21c0-4b75-b6f3-7ad9df2e6279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-22T06:36:01.402Z_

Now let me check the compiled PDF to verify page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda5064c-b2b8-4e37-9d75-c7451be1acae",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9JbKCs3MvzcTsw2HTf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20e26fba-0a9f-470a-ae7f-793826c57e30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuLciEnzrGqLgGRLdrkgpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 84327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 326,
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

_source line 69 · 2026-05-22T06:36:01.924Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vc3RxdgGuUfkzRqw4S1yxC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20e26fba-0a9f-470a-ae7f-793826c57e30",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9JbKCs3MvzcTsw2HTf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2f72c56-9000-4687-86ab-d417d39b30f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuLciEnzrGqLgGRLdrkgpt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 84327,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 326
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 84327,
          "cache_creation_input_tokens": 326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 326,
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

_source line 70 · 2026-05-22T06:36:02.481Z_

<details><summary>↩ Tool result · `toolu_01Vc3RxdgGuUfkzRqw4S1yxC`</summary>

```text
PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf (564.8KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2f72c56-9000-4687-86ab-d417d39b30f7",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "uuid": "e424db79-4892-428f-85d1-9dbb66ef9f4c",
  "sourceToolAssistantUUID": "b2f72c56-9000-4687-86ab-d417d39b30f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 71 · 2026-05-22T06:36:02.479Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e424db79-4892-428f-85d1-9dbb66ef9f4c",
  "isSidechain": true,
  "promptId": "b804d36f-8b07-4c90-a5a9-80fc9d96b913",
  "agentId": "adceaffc762c94987",
  "type": "user",
  "isMeta": true,
  "uuid": "0dbc0f2f-9508-4e0a-9ecf-63cc91ba2bfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-22T06:38:00.964Z_



Now I have a comprehensive understanding of the paper. Let me produce the review.

---

## Review: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**Reviewer 2 (R2) -- Focus: Novelty/Originality and Related Work Adequacy**

---

### 1. Summary

This paper presents OntoCoDec, a two-layer constrained decoding framework that compiles IE ontology schemas into token-level masks enforced during autoregressive generation. The grammar layer (via XGrammar) enforces JSON structure and vocabulary membership; the semantic layer maintains a runtime entity registry to enforce domain/range type constraints via dynamic logit masking. Evaluation spans three datasets (SciERC, DocRED, WikiEvents), five models (7B--70B), and demonstrates 92--100% DR reduction in fine-tuned settings with negligible F1 impact, at the cost of introducing cross-field (CF) type inconsistency violations.

---

### 2. Novelty Assessment: **3 / 5**

**The two-layer grammar+semantic approach: well-executed engineering with a modest conceptual contribution.**

The core idea -- combining structural CFG constraints with a stateful semantic layer that tracks an entity registry during decoding -- is a natural and reasonable engineering design, but the conceptual leap is incremental. The paper essentially answers: "what if we added a stateful logits processor on top of XGrammar?" The answer turns out to be effective, but the mechanism (a dictionary lookup that constrains type tokens based on previously decoded relation types) is straightforward once the problem is identified. The grammar layer is XGrammar off the shelf. The semantic layer is a pattern-matching state machine over the decoded prefix with domain/range lookups. The composition is bitwise AND with a fallback.

**Is the "first systematic integration" claim warranted?** Partially. The paper does a good job surveying prior work and the claim appears accurate in a narrow sense -- no prior work compiles IE ontology domain/range constraints into token-level masks specifically. However, the claim's narrowness limits its significance. PICARD (Scholak et al. 2021) does essentially the same thing for SQL (incremental semantic filtering at decode time using a schema); the difference is that IE entity types are inferred rather than declared. GenIE (Josifoski et al. 2022) uses state-based constraints for triple structure. IterGen (Ugare et al. 2025) addresses the same grammar-insufficiency-for-semantic-constraints problem with backtracking. The paper acknowledges these but the differentiation sometimes feels thin -- "our entities are inferred from text rather than read from declarations" is a valid but not deeply novel distinction.

**Delta over XGrammar + post-hoc validation:** The paper argues persuasively that post-hoc filtering is destructive (up to 48% rejection, 73.7% for Mistral DocRED) and that decoding-time enforcement is preferable. This is a real practical advantage. However, the actual mechanism is conceptually close to "XGrammar for structure + a lookup table applied at type-token positions." The 10--13% latency overhead is attractive, but one could also implement post-hoc filtering with a re-generation loop at comparable cost for the fine-tuned regime (where rejection rates are 0.6--2%).

**Comparison with CRANE:** CRANE addresses the constraint-vs-reasoning tradeoff theoretically; OntoCoDec is more applied and IE-specific. The paper correctly notes that IE is extraction (not reasoning) and thus less susceptible to quality degradation from constraints, citing Tam et al. (2024). This is a fair differentiation. OntoCoDec does not engage with CRANE's type-checking approach directly -- CRANE's alternating constrained/unconstrained phases are mentioned as analogous to S2 but not experimentally compared.

**Is the "enabling dependency" insight a contribution?** It is well-documented empirically (Table 1: semantic-only gets 24% DR reduction vs. 94% with grammar+semantic) but is somewhat obvious once stated: of course a semantic layer that filters based on relation types needs the relation types to be valid first. The paper calls this an "empirical enabling dependency" rather than claiming it as surprising, which is appropriately calibrated. The five-way ablation that demonstrates it is the real contribution -- the insight itself is expected.

**Is the decidability taxonomy a contribution?** The three-level taxonomy (context-free / prefix-decidable with state / non-local) is a useful organizational device. Proposition 1 (domain/range constraints are not context-free) is correct and the pumping lemma proof in the appendix is rigorous. However, the result is not deep -- it is well-known that context-free grammars cannot enforce arbitrary cross-serial dependencies, and the specific application to IE type constraints is a straightforward instantiation. The taxonomy provides clarity for the paper's architecture motivation but would not independently constitute a contribution.

**Bottom line:** The novelty is at the "solid applied contribution" level -- a well-engineered system that addresses a real gap (runtime semantic constraint enforcement for IE), with thorough evaluation. It is not a conceptual breakthrough. The paper is honest about this, framing the contribution as "systematic engineering contribution with theoretical grounding" (Section 1), which is accurate.

---

### 3. Related Work Assessment

**Coverage:** The related work is thorough, especially the extended appendix survey. The paper cites the key works I would expect:

- SGLang (Zheng et al. 2024) -- cited in Section 2
- GENRE (De Cao et al. 2021) -- cited in appendix related work
- UIE (Lu et al. 2022) -- cited in Section 6 and appendix
- InstructUIE (Wang et al. 2023) -- cited in Section 6
- USM (Lou et al. 2023) -- cited in Section 6
- PICARD, Synchromesh, GCD, IterGen, CRANE, BoostCD -- all cited and discussed

**Missing references:**

- **Microsoft Guidance library** -- Not cited. While Guidance is more of a software tool than a research paper, it is a widely-used system for constrained generation that supports stateful token masking and should be acknowledged as a related tool in the grammar-constrained decoding paragraph.
- **Knowledge graph completion work with ontology constraints** -- The paper focuses exclusively on IE but does not discuss ontology-constrained generation in the KG completion setting (e.g., constrained link prediction approaches that enforce type constraints). This is a minor gap given the IE focus but relevant to the broader positioning.
- **DCCD (Reddy et al. 2026)** -- Cited in Section 6 but only in passing. Given that draft-conditioned constrained decoding also addresses semantic constraints beyond grammar, a more detailed comparison would strengthen positioning.

**Is the positioning against prior work fair?**

Mostly fair, with one notable concern:

- The GoLLIE comparison (Section 6, lines 592--614) is informative but slightly misleading in its empirical framing. The paper compares GoLLIE-7B in zero-shot on SciERC (E-F1=9.17, R-F1=0.0) against OntoCoDec with LoRA fine-tuning (R-F1=45.47). This is not an apples-to-apples comparison -- GoLLIE was designed for zero-shot transfer to unseen schemas, while OntoCoDec+LoRA uses task-specific training. The paper does note "the two paradigms are complementary" but the juxtaposition of numbers creates an unfavorable impression of GoLLIE that may not be warranted. A fairer comparison would either (a) compare both in zero-shot, or (b) compare GoLLIE fine-tuned on SciERC vs. OntoCoDec+LoRA.

- The paper's claim that "no method provides both semantic awareness and hard constraint enforcement" (Section 1) is accurate for IE specifically but should acknowledge that PICARD does exactly this for text-to-SQL, and Mundler et al. (2025) do this for code generation. The paper does discuss these in the appendix but the introduction makes the claim sound broader than it is.

**Differentiation from prompt-based schema enforcement:**

The paper adequately differentiates from GoLLIE and KnowCoder by noting that prompt-based approaches provide "soft" guidance without runtime enforcement. The empirical evidence (1--2% residual DR even after fine-tuning, Table 2) supports this distinction.

---

### 4. Excitement: **2.5 / 5**

**Would this change how the community approaches IE?** Unlikely to cause a paradigm shift. The approach is useful for deployment scenarios requiring guaranteed ontology compliance, but the target audience is narrow: practitioners deploying LLM-based IE systems with strict schema requirements. The research community has largely moved toward prompt-based and training-based approaches that scale more naturally.

**Is the problem significant enough?** The problem is real -- 15--57% domain/range violations in zero-shot IE is a legitimate concern for deployment. However, fine-tuning already reduces violations to 0.5--2%, and OntoCoDec's incremental gain (to <0.09%) in the fine-tuned setting, while valuable for strict applications, is incremental. The zero-shot setting where the problem is most severe also has very low F1 (2--8%), making the violation reduction less practically meaningful.

**Are the results exciting or expected?** Largely expected. Given a correctly implemented semantic constraint layer, near-elimination of domain/range violations is the anticipated outcome. The CF tradeoff (up to 12% new violations introduced) is the most interesting finding because it reveals a fundamental tension in per-relation independent enforcement, but this is presented more as a limitation than an exciting result. The beam search result (complete violation elimination on SciERC) is encouraging but configuration-dependent.

The most interesting technical insight is that the grammar layer is a no-op for fine-tuned models (Table in Appendix C) while the semantic layer remains the sole defense -- this shifts the layer roles from "both necessary" (zero-shot) to "only semantic matters" (fine-tuned) and deserves more prominence.

---

### 5. Soundness: **4 / 5**

The experimental methodology is rigorous: paired bootstrap tests, five-way ablation, causal tracing of residual violations, three datasets, five models, two training regimes. The paper is commendably transparent about limitations (CF tradeoff, Mistral boundary case, incomplete 70B LoRA results). The constraint tightness analysis provides genuine insight into when the method works well vs. struggles.

Concerns: (a) The 70B LoRA results contain placeholders ("XX.XX") on page 8, which is a submission-readiness issue. (b) SciERC and DocRED constraints are extracted from training data rather than formal ontologies, raising questions about generalization to true ontology-constrained settings (though WikiEvents validates the formal ontology case). (c) The constraint tightness regression has only n=4 data points and p=0.058 -- the paper correctly flags this but still draws conclusions from it.

---

### 6. Reproducibility: **4 / 5**

The paper provides substantial implementation detail: JSON schema structure, field ordering, compilation pipeline, continuation masking mechanism. The constraint compilation from ontologies is described in sufficient detail for reimplementation. Hardware is specified (NVIDIA RTX PRO 6000 Blackwell Server Edition). Code release is promised upon acceptance. The appendix is exceptionally thorough. Deductions: the entity registry's pattern-matching logic for position detection (Section 3.3) could use more detail; the continuation masking compile-time prefix map is described at a high level without pseudocode.

---

### 7. Weaknesses

- **The CF tradeoff substantially undermines the practical value.** In zero-shot mode, full S1 reduces DR from 15.37% to 0.93% on SciERC but introduces 9.90% CF -- the total violation burden only drops from 15.45% to 10.83%. On DocRED, total violations drop from 18.56% to 12.78%. The method does not so much eliminate violations as convert one violation type into another. Under fine-tuning, CF is manageable (<=1.3%), but this relies on the model being well-calibrated.

- **Incomplete results in the submission.** The 70B LoRA results are placeholder "XX.XX" values (Section 5.4, line 557--561). This is a significant gap for a claimed contribution point ("70B zero-shot and LoRA in Section 5.4").

- **The novelty is primarily in integration, not in individual components.** The grammar layer is XGrammar. The semantic layer is a lookup table over a dictionary. The composition is bitwise AND. Each component is straightforward; the contribution is assembling them for IE, which is engineering-dominant.

- **Limited generalization evidence for "ontology compilation."** Two of three datasets (SciERC, DocRED) derive constraints empirically from training data, not from formal ontologies. Only WikiEvents uses a real ontology (KAIROS). The paper's framing as "ontology compilation" is somewhat aspirational given this evaluation distribution.

- **Zero-shot R-F1 of 2--8% limits interpretability of constraint effects.** At these performance levels, the models are essentially failing at the extraction task; demonstrating that constraints enforce type validity on largely incorrect extractions has limited practical value. The paper acknowledges this and positions zero-shot as a "diagnostic probe," but the paper devotes considerable space to zero-shot results.

- **No comparison with a simple "constrained re-generation" baseline.** If a generated triple violates domain/range constraints, one could mask the violating type tokens and regenerate just that triple. This would achieve similar DR reduction without the CF tradeoff. The paper compares against post-hoc filtering (rejection) but not against constrained re-generation (correction).

- **WikiEvents EE evaluation is preliminary.** Fine-tuning evaluation uses only 20 test documents with high per-document variance (Arg-F1 std/mean > 0.5). The paper acknowledges insufficient power for F1 differences but still reports numerical results that may mislead.

---

### 8. Questions for Authors

1. **CF vs. DR total violation burden:** In zero-shot SciERC, total violations (DR+CF) drop from 15.45% to 10.83% with S1. Have you considered reporting a unified "type violation rate" metric that captures both DR and CF, and if so, does OntoCoDec still show a clear win over unconstrained decoding on this metric across all settings?

2. **Constrained re-generation baseline:** Have you considered a baseline that detects DR violations after generation and re-generates only the type-bearing tokens under constraints, rather than constraining the entire generation? This could potentially avoid the CF tradeoff by allowing the model to establish entity types in the first pass and only correcting violations.

3. **Scalability of continuation masking:** The paper notes that the "first-token uniqueness requirement" may become a bottleneck beyond 200 entity types (Limitations). Can you quantify at what ontology scale this becomes a real problem? For example, KnowCoder handles 29K entity types -- is OntoCoDec fundamentally incompatible with such scales?

4. **Why not compare against IterGen?** IterGen (Ugare et al. 2025) addresses the same problem (semantic constraints beyond grammar) with backtracking. It seems like a natural experimental baseline. Is there a technical reason this comparison was omitted?

5. **Grammar-layer role inversion under fine-tuning:** The appendix ablation (Table in Appendix C) shows the grammar layer is a no-op for fine-tuned models. Does this mean a deployment using LoRA + semantic-layer-only (without grammar) would achieve the same results? If so, the "two-layer architecture" contribution is less compelling for the primary deployment setting.

---

### 9. Overall Assessment: **3.0** (Findings)

**Justification:** OntoCoDec addresses a real problem (ontology type violations in LLM-based IE) with a well-engineered solution and thorough evaluation. The experimental methodology is among the paper's strongest aspects -- the five-way ablation, causal tracing, constraint tightness analysis, and honest treatment of the CF tradeoff are all commendable.

However, the novelty is limited to assembling known components (XGrammar + dictionary-based state tracking) for a specific application. The conceptual advance beyond "add a stateful logits processor on top of grammar-constrained decoding" is modest. The CF tradeoff means that total type violations are only partially reduced in the most interesting (zero-shot) setting. The 70B LoRA placeholders indicate incomplete results. The paper would benefit from stronger baselines (constrained re-generation, IterGen comparison) and a clearer articulation of when the engineering complexity of OntoCoDec is justified over simpler alternatives (post-hoc filtering in the fine-tuned regime, where rejection rates are 0.6--2%).

The work is solid enough for Findings -- it makes a useful applied contribution with thorough evaluation -- but lacks the novelty or surprising results for main conference acceptance. The "first to compile ontology constraints into decoder masks for IE" claim, while technically accurate, describes an incremental step along a well-established trajectory (PICARD for SQL, Mundler et al. for code, now OntoCoDec for IE).

| Dimension | Score |
|-----------|-------|
| Soundness | 4 |
| Excitement | 2.5 |
| Reproducibility | 4 |
| **Overall** | **3.0** |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dbc0f2f-9508-4e0a-9ecf-63cc91ba2bfb",
  "isSidechain": true,
  "agentId": "adceaffc762c94987",
  "requestId": "req_011CbH9Ju8WcmAGgi1nGU8Jx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86ad2baa-b52c-4ff1-8780-736f6501ac6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "a39f4bf6-f98d-43c7-bbf4-41a033e3e2e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M365eor6SEPHNBzib5a3bg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10300,
      "cache_read_input_tokens": 84653,
      "output_tokens": 4158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4158,
          "cache_read_input_tokens": 84653,
          "cache_creation_input_tokens": 10300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10300,
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
