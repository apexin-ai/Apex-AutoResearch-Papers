# Research conversation: You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Wea

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a43169a44fe76dba5.jsonl`
- **Structured JSON:** [`1b1a4fe4b57d8b6f548f.json`](../../sessions/1b/1b1a4fe4b57d8b6f548f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

73 recorded events

### User

_source line 1 · 2026-05-18T17:13:02.402Z_

You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **Novelty/Contribution** and **Related Work/Positioning**.

## Paper Summary

**Title**: "OntoCoDec: Universal Ontology-Constrained Structured Generation for Information Extraction"

**Core Contribution**: A framework that compiles IE ontology schemas into two composable decoding-time constraint layers:
1. Grammar layer (CFG via XGrammar) for structural validity + vocabulary membership
2. Semantic layer (stateful entity registry + dynamic logit masking) for cross-field type constraints (domain/range for RE, role-argument type for EE)

The key insight is the "enabling dependency": grammar is a prerequisite for semantic (semantic layer can't look up constraints for OOV relation/event type names).

**Claimed Contributions** (from Introduction):
1. Systematic violation landscape study quantifying ontology constraint violations across models, datasets, and IE tasks, establishing that violation rates are driven by constraint tightness rather than ontology size
2. A composable constraint framework with enabling dependency between grammar and semantic layers (semantic-only: 24% DR reduction vs full system: 94%)
3. Cross-task generalization: RE → EE with zero architectural modification, RoV 64-89% → 0%
4. Cross-scale evidence: 70B model still violates at 6.5-11%, OntoCoDec achieves 89-100% reduction

**Related Work Coverage** (Section 7, ~1 page):
- **Constrained Decoding for Structured Generation**: XGrammar, Outlines, LMQL — guarantee syntactic validity but not semantic constraints. SynCode extends to programming languages. Paper positions OntoCoDec as adding semantic layer on top.
- **Type-Aware IE**: Training-time approaches (entity typing losses, relation-aware representations, RAP). TANL, UIE, InstructUIE — embed type awareness in model. Paper claims these can't guarantee compliance at inference time.
- **LLM-Based IE**: GPT-RE, Code4Struct, GoLLIE, CodeIE — structured output for IE. Paper claims OntoCoDec is complementary.
- **Event Extraction**: Text2Event, DEGREE, CEDAR. KAIROS ontology's 245 constraints noted.
- **Quality Assurance for Generated Structures**: Post-hoc filtering. Paper shows this is non-viable for EE (99.6-100% discard).

**Background** (Section 2):
- Grammar-Constrained Decoding: XGrammar, CFG limitations (stateless → can't enforce cross-field)
- IE Ontology Structure: formal definitions of entity types E, relations R, event types V, argument roles A, type constraints
- Violation Taxonomy: DR, RV, ET, CF (for RE); EV, RoV, AC (for EE)

**Experimental scope**: 2 tasks (RE, EE), 4 models (3×8B + 1×70B), 3 datasets (SciERC, DocRED, WikiEvents), 4 configurations (unconstrained, grammar-only, semantic-only, full S1)

**Key experimental findings**:
- Violation rates: DR 6.5-26%, RoV 64-89% across models
- Full system: DR reduction 44-100%, RV/ET/EV/RoV→0%
- Post-hoc filtering non-viable for EE (99.6-100% discard)
- F1 neutral or slightly improved
- CF tradeoff: 0→9.9% (SciERC), up to 21.1% (EE)
- Latency overhead: 13-20%

**Analytical contributions**:
- Enabling dependency (grammar→semantic asymmetry)
- Tightness × RV baseline interaction model
- Latent violation surfacing effect (grammar-only DocRED DR increases from 18.46 to 26.17%)
- Fallback frequency as constraint coverage metric
- CF as inherent limitation of per-relation independent enforcement
- Decidability taxonomy (purely local, prefix-decidable with state, truly non-local)

## Your Review Task

Write a detailed review focusing on:

1. **Novelty Assessment**:
   - How novel is the two-layer (grammar + semantic) architecture? Is it a natural extension of existing constrained decoding, or a genuine contribution?
   - Is the "enabling dependency" insight genuinely surprising or obvious in retrospect?
   - How significant is the violation landscape study as a standalone contribution?
   - Is the "universal/task-agnostic" claim justified? (Only RE and EE tested)
   - Is the decidability taxonomy (§4.5) a meaningful conceptual contribution?

2. **Related Work Positioning**:
   - Are there important missing references? Consider:
     - Structured prediction / constrained decoding literature (e.g., PICARD for SQL, Synchromesh)
     - Schema-guided dialogue / schema-linking work
     - Ontology-aware NER/RE systems
     - Knowledge graph completion with type constraints
     - Other stateful constrained decoding approaches
   - Is the differentiation from existing work clear and fair?
   - Is the Related Work comprehensive enough for a top venue?

3. **Claim-Evidence Alignment**:
   - Does each claimed contribution have adequate experimental support?
   - Are claims appropriately scoped (not overclaimed)?
   - "Universal" in the title — justified?

4. **Significance and Impact**:
   - Who would use this? How practical is it?
   - Does this advance the field meaningfully?
   - Is this primarily an engineering contribution or does it provide scientific insights?

5. **Writing Quality**:
   - Is the paper well-structured?
   - Are concepts clearly defined?
   - Is the narrative coherent?

## Output Format

```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentence summary of the paper]

### Strengths
[Numbered list, 4-6 items]

### Weaknesses
[Numbered list, 4-6 items]

### Questions for Authors
[Numbered list, 3-5 items]

### Minor Issues
[Bulleted list]

### Preliminary Score: X/6
### Confidence: X/5
### Justification: [2-3 sentences]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "dda45dff-8c08-4c97-89a9-1280d4c7f1b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T17:13:02.405Z_

```json
{
  "parentUuid": "dda45dff-8c08-4c97-89a9-1280d4c7f1b9",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
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
  "uuid": "2b377085-c735-4021-809b-a4d256e0a484",
  "timestamp": "2026-05-18T17:13:02.405Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T17:13:05.137Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b377085-c735-4021-809b-a4d256e0a484",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQebG1NgiJGkEVn8zXh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c585cbc-7094-41f0-857c-0f236870c232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFuNnQLL9JwTResYLfHkak",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8940,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8940,
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

_source line 4 · 2026-05-18T17:13:06.771Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JheSutTJjbFe4BDMEz5mk9`</summary>

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
  "parentUuid": "2c585cbc-7094-41f0-857c-0f236870c232",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQebG1NgiJGkEVn8zXh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d348ad9-35b8-4494-8e67-9f0b4bf29f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFuNnQLL9JwTResYLfHkak",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8940,
      "cache_read_input_tokens": 8252,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8940
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 8940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8940,
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

_source line 5 · 2026-05-18T17:13:06.775Z_

<details><summary>↩ Tool result · `toolu_01JheSutTJjbFe4BDMEz5mk9`</summary>

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
  "parentUuid": "1d348ad9-35b8-4494-8e67-9f0b4bf29f06",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "592d0b5e-72fa-49f5-bb6d-37b39e468c96",
  "sourceToolAssistantUUID": "1d348ad9-35b8-4494-8e67-9f0b4bf29f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T17:13:09.674Z_



I'll read the paper and project files systematically to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "592d0b5e-72fa-49f5-bb6d-37b39e468c96",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQev1NySxVc6hkVptqE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f0c8111-5231-4cae-9c40-db12e516ade0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114sZzGy7EVPcVGNSvT1VZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-18T17:13:10.156Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01PS9gwSp68p3JA7hSeZV592`</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f0c8111-5231-4cae-9c40-db12e516ade0",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQev1NySxVc6hkVptqE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "883b79a6-071c-4d93-9c7e-e2ec6f8434f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114sZzGy7EVPcVGNSvT1VZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 8 · 2026-05-18T17:13:10.439Z_

<details><summary>↩ Tool result · `toolu_01PS9gwSp68p3JA7hSeZV592`</summary>

```text
{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (88 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| w9_qwen_docred_zs_sampling_r2 | Continuation of w9 DocRED sampling from doc 106, testing OntoCoDec full_s1 with temperature sampling (T=0.7) on remaining 892 DocRED documents | — | — | — |\n| p8b_docred_latency | OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper | — | — | — |\n| 70b_docred_constrained | 70B AWQ-INT4 model with OntoCoDec constrained decoding on DocRED will achieve 0% ET/RV violations while maintaining F1, demonstrating cross-dataset scalability | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **w9_qwen_docred_zs_sampling** (failed): Temperature sampling (T=0.7, top_p=0.9) with OntoCoDec full_s1 on Qwen3-8B DocRED will maintain low violation rates while exploring output diversity on cross-sentence RE with 96 relation types\n- **w9_qwen_scierc_zs_sampling** (success): Temperature sampling (T=0.7, top_p=0.9) with OntoCoDec full_s1 on Qwen3-8B SciERC will maintain low violation rates while potentially improving F1 through output diversity compared to greedy decoding\n  [w9_scierc_sampling_analysis](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/w9_qwen_scierc_zs_sampling/report/w9_scierc_sampling_analysis.md)\n- **p8_latency_overhead** (success): OntoCoDec constrained decoding overhead on Qwen3-8B SciERC is moderate (<2x), demonstrating practical deployability\n\n## 趋势\n成功 75 / 负向 4 / 失败 1 / 共 84\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\nwestd-21461: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\n- w1_cf_fallback_docred: 已被终止 — unknown\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "883b79a6-071c-4d93-9c7e-e2ec6f8434f8",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "0869df39-54ca-4edc-bbb3-b2caa66fb740",
  "sourceToolAssistantUUID": "883b79a6-071c-4d93-9c7e-e2ec6f8434f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T17:13:11.564Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015UkdEKjYSz9rDgQzpx8rTU`</summary>

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
  "parentUuid": "0869df39-54ca-4edc-bbb3-b2caa66fb740",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQev1NySxVc6hkVptqE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ae6ea14-00d4-413f-92ae-fca1e1739faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114sZzGy7EVPcVGNSvT1VZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 10 · 2026-05-18T17:13:11.586Z_

<details><summary>↩ Tool result · `toolu_015UkdEKjYSz9rDgQzpx8rTU`</summary>

```text
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/section7_conclusion_550cbf.tex
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
artifacts/_project/paper/section7_conclusion.tex
artifacts/dream_reports/dream_20260516T021434/best/paper.tex
artifacts/dream_reports/dream_20260516T021434/median/paper.tex
artifacts/dream_reports/dream_20260516T021434/worst/paper.tex
artifacts/dream_reports/dream_20260516T173022/best/paper.tex
artifacts/dream_reports/dream_20260516T173022/median/paper.tex
artifacts/_project/paper/paper_tables_draft.tex
artifacts/appendix_sampling_table.tex
artifacts/_project/paper/appendix_sampling_table.tex
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/appendix_related_work.tex
artifacts/_project/paper/section2_background.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/appendix_doc_length.tex
artifacts/_project/paper/appendix_prompt_sensitivity.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/_project/paper/section5_wikievents_draft.tex
artifacts/_project/paper/section7_conclusion_compressed.tex
artifacts/_project/paper/appendix_beam_search.tex
artifacts/_project/paper/p3_case_studies.tex
artifacts/_project/paper/p3_case_studies_861a0d.tex
artifacts/p3_case_studies.tex
artifacts/_project/paper/appendix_reproducibility.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_case_studies.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/dream_reports/dream_20260518T162745/best/paper.tex
artifacts/dream_reports/dream_20260518T162745/median/paper.tex
artifacts/dream_reports/dream_20260518T162745/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ae6ea14-00d4-413f-92ae-fca1e1739faa",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "5227d7a4-31db-4169-9c8e-0bfe0deb6b8f",
  "sourceToolAssistantUUID": "7ae6ea14-00d4-413f-92ae-fca1e1739faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T17:13:12.382Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Jmpm7TmzwFuqYShKb5d3Uk`</summary>

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
  "parentUuid": "5227d7a4-31db-4169-9c8e-0bfe0deb6b8f",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQev1NySxVc6hkVptqE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a5e8687-23a8-4ee0-b773-08a0fad4e9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114sZzGy7EVPcVGNSvT1VZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17192,
      "output_tokens": 269,
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
          "output_tokens": 269,
          "cache_read_input_tokens": 17192,
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

_source line 12 · 2026-05-18T17:13:12.392Z_

<details><summary>↩ Tool result · `toolu_01Jmpm7TmzwFuqYShKb5d3Uk`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a5e8687-23a8-4ee0-b773-08a0fad4e9dd",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "bdfe373b-7e90-4298-b992-31bbf5ffa623",
  "sourceToolAssistantUUID": "6a5e8687-23a8-4ee0-b773-08a0fad4e9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T17:13:24.856Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3hxYHr96uXcDJNkyeqRJd`</summary>

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
  "parentUuid": "bdfe373b-7e90-4298-b992-31bbf5ffa623",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQfL8T5a91GCxvqef4r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2ec79d4-8de8-417e-8646-4d5a4acf8d80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcYgnLDVYy34bTBax45PjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 18639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2526,
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

_source line 14 · 2026-05-18T17:13:24.862Z_

<details><summary>↩ Tool result · `toolu_01Q3hxYHr96uXcDJNkyeqRJd`</summary>

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
17	\usepackage{pifont}
18	
19	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	% === Abstract ===
27	\input{abstract}
28	
29	% === §1 Introduction ===
30	\input{section1_introduction_draft}
31	
32	% === §2 Background ===
33	\input{section2_background}
34	
35	% === §3 Method ===
36	\input{section3_method_draft}
37	
38	% === §4 Constraint Composition ===
39	\section{Constraint Composition}
40	\label{sec:composition}
41	\input{section4_composition_draft}
42	
43	% === §5 Experiments ===
44	\section{Experiments}
45	\label{sec:experiments}
46	
47	\subsection{Violation Landscape}
48	\input{section3_violation_landscape}
49	
50	\input{section5_scierc_draft}
51	\input{section5_docred_draft}
52	\input{section5_crossmodel_draft}
53	\input{section5_wikievents_draft}
54	\input{section5_runtime}
55	
56	% === §6 Related Work ===
57	\input{section6_related_work}
58	
59	% === §7 Discussion and Conclusion ===
60	\section{Discussion and Conclusion}
61	\label{sec:discussion}
62	\input{section7_conclusion_compressed}
63	
64	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
65	\clearpage
66	\section*{Limitations}
67	
68	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp). CF$\leftrightarrow$DR thus represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
70	Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
71	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
72	Composability with fine-tuned models is validated on both SciERC and DocRED with Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,0.20\%, R-F1 change within $\pm$0.6\,pp), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
73	The continuation masking approach (\S\ref{sec:dynamic-masking}) handles multi-token type names and prefix-shared types on the ontologies tested (6--27 entity types); scalability to ontologies with hundreds of entity types has not been validated, and the prefix-map size may grow substantially.
74	Global entity-level type consensus during decoding offers the most direct path to resolving CF violations.
75	All models tested are 7--8B-parameter class; scaling behavior to larger (70B+) or smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
76	CF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated.
77	Residual DR under fine-tuning (36 violations across all fine-tuned settings, both models and both datasets) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors correctly caught by constraints (28\%); Llama DocRED alone accounts for 33 of 36 residual violations (92\%), reflecting weaker entity typing (Appendix~\ref{app:residual-dr-analysis}).
78	Schema coverage gaps (one-third of residual violations) are irreducible by decoding-time constraints alone (training-set frequency coverage); complementary approaches such as global type consensus or post-hoc correction may address this limitation.
79	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and a DocRED subset across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
80	Validation with fine-tuned models, larger scales, and non-English ontologies remains to be explored.
81	
82	% === Ethics Statement ===
83	\section*{Ethics Statement}
84	
85	This work uses publicly available benchmark datasets (SciERC and DocRED) with no personally identifiable information.
86	No human subjects were involved in the experiments.
87	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
88	Code and data will be released upon acceptance.
89	
90	% === Bibliography ===
91	\bibliography{relwork_new_entries}
92	
93	% === Appendix ===
94	\appendix
95	
96	\input{appendix_prompts}
97	\input{appendix_related_work}
98	\input{appendix_discussion}
99	\input{appendix_llama_per_relation}
100	\input{appendix_sampling_table}
101	\input{appendix_beam_search}
102	\input{appendix_reproducibility}
103	\input{appendix_doc_length}
104	\input{appendix_prompt_sensitivity}
105	\input{appendix_case_studies}
106	
107	\end{document}
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2ec79d4-8de8-417e-8646-4d5a4acf8d80",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "f3f825e3-e0b2-40eb-84cd-9990af75ae05",
  "sourceToolAssistantUUID": "b2ec79d4-8de8-417e-8646-4d5a4acf8d80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T17:13:25.275Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tj9Z4icveuP1FGVmdYPCvq`</summary>

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
  "parentUuid": "f3f825e3-e0b2-40eb-84cd-9990af75ae05",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQfL8T5a91GCxvqef4r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cda5bf70-1eff-4ba5-ad3a-0c2707f99c15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcYgnLDVYy34bTBax45PjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 18639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2526,
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

_source line 16 · 2026-05-18T17:13:25.296Z_

<details><summary>↩ Tool result · `toolu_01Tj9Z4icveuP1FGVmdYPCvq`</summary>

```text
1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) guaranteeing JSON structural validity and entity/relation vocabulary membership (virtually eliminating entity type and relation vocabulary violations); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	%
6	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), comparable rates governed by \emph{constraint tightness} rather than ontology scale.
7	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost (DocRED: $+$0.50\,pp, $p{<}0.001$; \S\ref{sec:cross-model}).
8	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
9	Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with relation F1 within $\pm$0.6\,pp, a near-lossless composition.
10	With beam search ($k{=}4$), the full stack eliminates all four violation types under fine-tuned beam decoding (SciERC, both Qwen3-8B and Llama-3.1-8B) while preserving extraction quality (R-F1 44.23 and 46.11, respectively); in zero-shot beam decoding, DR reaches 0\% for calibrated models on both RE datasets.
11	The framework generalizes to event extraction (WikiEvents: 56 event types, 80 roles) without architectural modification and eliminates event-vocabulary and role-vocabulary violations ($\to$ 0\%); where unconstrained outputs are severely off-schema, format compliance additionally enables entity extraction (Entity F1: 0\%\,$\to$\,12--18\%).
12	Per-slot enforcement introduces a cross-field consistency trade-off (up to 12\% in zero-shot, resolved to $\leq$1.2\% by fine-tuning).
13	OntoCoDec demonstrates that ontology schemas can be compiled into decoding-time guarantees, bridging the gap between flexible generative extraction and the type-safety requirements of downstream knowledge systems.
14	\end{abstract}
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cda5bf70-1eff-4ba5-ad3a-0c2707f99c15",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "02078a9b-c793-45eb-abaa-dad5aeb39045",
  "sourceToolAssistantUUID": "cda5bf70-1eff-4ba5-ad3a-0c2707f99c15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T17:13:25.678Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nrnmp14auCtuCke7ts7pEr`</summary>

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
  "parentUuid": "02078a9b-c793-45eb-abaa-dad5aeb39045",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQfL8T5a91GCxvqef4r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72739330-7058-4923-b130-396d606412b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcYgnLDVYy34bTBax45PjQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 18639,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 18639,
          "cache_creation_input_tokens": 2526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2526,
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

_source line 18 · 2026-05-18T17:13:25.700Z_

<details><summary>↩ Tool result · `toolu_01Nrnmp14auCtuCke7ts7pEr`</summary>

```text
1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	For downstream systems in safety-critical domains (biomedical entity extraction, legal document analysis), statistical reduction of violations is insufficient; type-safety guarantees are needed to prevent error propagation into knowledge graphs and decision-support pipelines.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
16	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
17	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
18	
19	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
20	Our two-layer architecture reflects the observation that structural violations (malformed output, unknown types) and semantic violations (type-constraint breaches) require fundamentally different enforcement mechanisms.
21	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
22	The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records type assignments; when relation arguments are generated, dynamic logit masking restricts output to types compatible with the relation's domain/range specification.
23	The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, so the semantic layer can look up domain/range rules.
24	Unlike type-constrained code generation where types are statically declared, IE requires a dynamic entity registry built during generation, with constraint targets that depend on the co-occurring relation.
25	On SciERC, OntoCoDec reduces DR violations from 15.37\% to 0.93\% ($\downarrow$94\%) while remaining F1-neutral ($+$0.13\,pp).
26	
27	Our contributions:
28	\begin{enumerate}
29	    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), violation rates are driven by constraint tightness rather than ontology size, and prompt-level intervention is per-relation unreliable.
30	    \item OntoCoDec, a two-layer compiled constraint framework that is the first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE.
31	    Unlike type-constrained decoding in code generation, where output types are statically determined by the grammar, IE requires stateful cross-field constraints because entity type validity depends on the co-occurring relation within each triple.
32	    \item Empirical validation on 3 models $\times$ 3 datasets (2 RE + 1 EE): DR $\downarrow$76--99\% on SciERC and $\downarrow$42--90\% on DocRED with significant R-F1 gains (Qwen $p{<}0.001$, Llama $p{=}0.013$); cross-task generalization to WikiEvents (vocabulary violations $\to$\,0\%; Entity F1 0\%\,$\to$\,12--18\%); composability with LoRA (DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost).
33	    \item Characterization of the CF$\leftrightarrow$DR trade-off inherent in per-slot enforcement (resolved by fine-tuning to CF\,$\leq$\,1.2\%); beam search ($k{=}4$) as an orthogonal path that eliminates all four violation types under fine-tuned beam decoding (SciERC, both Qwen3-8B and Llama-3.1-8B) and reduces DR to 0\% for calibrated models in zero-shot settings.
34	\end{enumerate}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72739330-7058-4923-b130-396d606412b4",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "8fcbe721-3d32-403b-8768-6e5a77e52837",
  "sourceToolAssistantUUID": "72739330-7058-4923-b130-396d606412b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T17:13:30.005Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NTQEerU7FfUUBzHLvHBmzd`</summary>

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
  "parentUuid": "8fcbe721-3d32-403b-8768-6e5a77e52837",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQgKciw18rjxEJRQLiA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70bc9748-8463-4c80-913e-3e7b83a2920c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7qT46tWp1QLxFFGumw36R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4339,
      "cache_read_input_tokens": 21165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4339,
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

_source line 20 · 2026-05-18T17:13:30.041Z_

<details><summary>↩ Tool result · `toolu_01NTQEerU7FfUUBzHLvHBmzd`</summary>

```text
1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is available in the decoded prefix.
22	This requires that each entity type name maps to a unique first subword token (\S\ref{sec:semantic}, Implementation), a design assumption verified for all tested configurations.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70bc9748-8463-4c80-913e-3e7b83a2920c",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "19b8b6cb-b593-494c-842a-6fd1bf766753",
  "sourceToolAssistantUUID": "70bc9748-8463-4c80-913e-3e7b83a2920c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T17:13:30.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y7JobX4LeAVTTZnTcFb7zn`</summary>

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
  "parentUuid": "19b8b6cb-b593-494c-842a-6fd1bf766753",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQgKciw18rjxEJRQLiA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b21a5565-27fe-46d8-afd4-96bc90d33349",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7qT46tWp1QLxFFGumw36R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4339,
      "cache_read_input_tokens": 21165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4339,
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

_source line 22 · 2026-05-18T17:13:30.944Z_

<details><summary>↩ Tool result · `toolu_01Y7JobX4LeAVTTZnTcFb7zn`</summary>

```text
1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering ensures that the relation type $r_j$ is known before entity type fields are generated, which enables domain and range lookups in sequential masking (\S\ref{sec:dynamic-masking}).
30	
31	\paragraph{Ontology compliance.}
32	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,\, (\tau^h, \tau^t) \in \sigma(r)\}$ for domain-valid head types and $\operatorname{range}(r, \tau^h) = \{\tau^t : (\tau^h, \tau^t) \in \sigma(r)\}$ for the conditional range given head type $\tau^h$.
33	Our enforcement target is \emph{pair-based} type validity: $(\tau^h, \tau^t) \in \sigma(r)$ for every triple.
34	The decoder enforces this sequentially: $\tau^h \in \operatorname{dom}(r)$ at head position, then $\tau^t \in \operatorname{range}(r, \tau^h)$ at tail position. This is equivalent to the full pair check and strictly stronger than independent domain/range enforcement, because most relations have non-rectangular type signatures ($\sigma(r) \subsetneq \operatorname{dom}(r) \times \operatorname{range}(r)$ for all 7 SciERC and 73/96 DocRED relations; see \S\ref{sec:rectangularity}).\footnote{An independent check ($\tau^h \in \operatorname{dom}(r) \wedge \tau^t \in \operatorname{range}(r)$) would over-permit type pairs by $1.50\times$ on SciERC and $1.58\times$ on DocRED, corresponding to 33.3\% and 36.8\% spurious type pairs.}
35	Our goal is maximizing $P(y \mid x)$ subject to all triples being type-valid and $y$ being well-formed JSON conforming to Eq.~\eqref{eq:output-schema}.
36	
37	
38	\subsection{Grammar Layer}
39	\label{sec:grammar}
40	
41	The grammar layer compiles $\mathcal{O}$ into a context-free grammar (CFG) enforced at every decoding step via logit masking.
42	This compilation proceeds in two stages.
43	
44	\paragraph{Schema-to-grammar compilation.}
45	We generate a JSON Schema encoding the structure in Eq.~\eqref{eq:output-schema} with \texttt{enum} constraints restricting entity types to $\mathcal{E}$ and relation types to $\mathcal{R}$.
46	This schema is compiled into an EBNF grammar via XGrammar~\cite{dong2025xgrammar}, producing a pushdown automaton tracking JSON structure and enum membership.
47	
48	\paragraph{Logit masking.}
49	At step $t$, the automaton computes grammar-valid tokens $G(t) \subseteq V$; all others receive logits $-\infty$.
50	This simultaneously enforces: (i)~structural validity (well-formed JSON), (ii)~relation vocabulary membership ($r_j \in \mathcal{R}$), and (iii)~entity type membership ($\tau_i \in \mathcal{E}$).
51	Domain/range constraints are \emph{not} enforced, as they depend on entity types within each triple; this gap is filled by the semantic layer.
52	
53	\paragraph{Empirical profile.}
54	On SciERC, grammar constraints eliminate relation vocabulary violations entirely (1.39\%\,$\to$\,0\%) and entity type violations entirely (0.40\%\,$\to$\,0\%), with no measurable F1 impact.
55	Domain/range violations remain effectively unchanged (15.37\%\,$\to$\,14.84\%). This confirms that grammar constraints enforce structural but not semantic validity.
56	
57	
58	\subsection{Semantic Layer}
59	\label{sec:semantic}
60	
61	The semantic layer enforces domain/range constraints through a stateful logits processor maintaining an entity registry during generation.
62	
63	\subsubsection{Entity Registry}
64	\label{sec:entity-registry}
65	
66	As the model generates the entity list, the semantic layer builds a registry $\mathcal{D}: \text{name} \to \text{type}$ mapping each entity to its declared type.
67	This registry is populated incrementally: when the model completes an entry $\{n_i, \tau_i\}$, the pair $(n_i, \tau_i)$ is added to $\mathcal{D}$.
68	The registry is then consulted during relation generation to look up the declared types of head and tail entities.
69	
70	\subsubsection{Position Detection}
71	\label{sec:position-detection}
72	
73	At each step $t$, the processor determines which field is currently being generated by pattern-matching on the decoded prefix.
74	We define five field positions (\textsc{EntityType}, \textsc{RelationType}, \textsc{HeadType}, \textsc{TailType}, and \textsc{FreeText}), identified via JSON key patterns (e.g., tokens following \texttt{"head\_type":} indicate \textsc{HeadType}).
75	Semantic masks activate only at type-bearing positions (\textsc{HeadType}, \textsc{TailType}).
76	
77	\subsubsection{Dynamic Masking}
78	\label{sec:dynamic-masking}
79	
80	At type-bearing positions, the processor computes a semantic mask $S(t) \subseteq V$ restricting generation to type-valid tokens.
81	
82	\paragraph{Head type masking.}
83	At a \textsc{HeadType} position, the processor considers the entity registry $\mathcal{D}$ and the current relation type $r_j$ (if already generated).
84	If $h_j \in \mathcal{D}$ and $\mathcal{D}[h_j] \in \operatorname{dom}(r_j)$, the mask allows only that registered type: $S(t) = \{\operatorname{tok}(\mathcal{D}[h_j])\}$, ensuring consistency with both the entity list and domain constraints.
85	Otherwise, if $r_j$ is known, the mask falls back to all domain-valid types: $S(t) = \{\operatorname{tok}(\tau) : \tau \in \operatorname{dom}(r_j)\}$.
86	If $r_j$ is unavailable, no semantic mask is applied.
87	
88	\paragraph{Tail type masking.}
89	At a \textsc{TailType} position, the head type $\tau^h_j$ is already determined from the decoded prefix.
90	The processor computes $\operatorname{range}(r_j, \tau^h_j)$, the valid tail types conditioned on the generated head type (\S\ref{sec:formulation}).
91	If $t_j \in \mathcal{D}$, the mask further restricts to the registered type when it belongs to this set.
92	This sequential check ($\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$) achieves exact pair-based enforcement, strictly tighter than an independent range check $\tau^t \in \operatorname{range}(r)$.
93	
94	\paragraph{Tokenizer-agnostic type masking.}
95	Each type name $\tau \in \mathcal{E}$ must be mapped to token IDs for logit masking.
96	A naive approach maps $\tau$ to its first subword token and sets disallowed IDs to $-\infty$, but this fails in two scenarios:
97	(1)~SentencePiece tokenizers produce context-dependent tokenizations where the same string yields different token IDs depending on preceding context (e.g., after a JSON delimiter), and
98	(2)~ontologies with prefix-shared type names (e.g., \textsc{Sen}, \textsc{Sid}, \textsc{Side} in WikiEvents) map to the same first token, making single-token disambiguation impossible.
99	We resolve both with \emph{continuation masking}: at compile time, we scan the full vocabulary to build a prefix map identifying, for each type name, all tokens whose decoded text is a valid prefix.
100	At decode time, the semantic mask allows any token that continues a partially-generated type name, disambiguating over multiple steps.
101	This is tokenizer-agnostic, handling byte-level BPE (Qwen, Llama) and SentencePiece (Mistral) without tokenizer-specific logic.
102	
103	\subsubsection{Grammar-Semantic Interaction}
104	\label{sec:interaction}
105	
106	The final mask is the conjunction of $G(t)$ and $S(t)$, permitting only tokens satisfying both layers (formalized in \S\ref{sec:composition}).
107	This embodies an \emph{enabling dependency}: semantic lookup requires relation types to be valid members of $\mathcal{R}$, guaranteed only by the grammar layer.
108	Without grammar enforcement, the model may generate out-of-vocabulary relation types for which no $\sigma(r)$ rules exist.
109	Empirically, semantic-only constraints reduce DR by only 24\% (15.37\%\,$\to$\,11.65\%) while failing to eliminate vocabulary violations; the full combination achieves 94\% DR reduction.
110	When $S(t) \cap G(t) = \emptyset$ (the semantic layer would mask out all grammar-valid tokens), the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.
111	This \emph{grammar-first invariant} reflects a deliberate priority ordering: structural integrity is a hard constraint, while type violations are soft errors detectable by downstream validation.
112	
113	
114	\subsection{Decoding Strategies}
115	\label{sec:strategies}
116	
117	\paragraph{S1: Single-pass decoding.}
118	Both constraint layers are active throughout a single generation pass.
119	The entity registry is populated as entities are generated and immediately available for relation-level type checking.
120	This is the simpler and recommended strategy. It achieves strong constraint enforcement with higher relation F1 than the two-pass alternative.
121	
122	\paragraph{S2: Two-pass decoding.}\label{sec:s2}
123	The first pass generates only entities under grammar constraints; the extracted entities compile an input-dependent grammar that additionally constrains head and tail names to match declared entities.
124	The second pass generates relations under this tighter grammar plus semantic constraints.
125	Detailed comparison is provided in the appendix.
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b21a5565-27fe-46d8-afd4-96bc90d33349",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "ebf1f95e-629b-42f7-804a-41459475b355",
  "sourceToolAssistantUUID": "b21a5565-27fe-46d8-afd4-96bc90d33349",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T17:13:31.228Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L8souPCGj7CrKRX2DFc7a1`</summary>

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
  "parentUuid": "ebf1f95e-629b-42f7-804a-41459475b355",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQgKciw18rjxEJRQLiA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4903c4a5-e9db-4a6b-9463-babe0938394d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7qT46tWp1QLxFFGumw36R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4339,
      "cache_read_input_tokens": 21165,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4339
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 21165,
          "cache_creation_input_tokens": 4339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4339,
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

_source line 24 · 2026-05-18T17:13:31.238Z_

<details><summary>↩ Tool result · `toolu_01L8souPCGj7CrKRX2DFc7a1`</summary>

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
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern (tightness $\times$ baseline model violation rate) is consistent with the cross-dataset results: for calibrated models (Qwen, Llama), SciERC ($\bar{\kappa}{=}0.333$, 24 valid pairs/relation) achieves 94--99\% DR reduction, while DocRED ($\bar{\kappa}{=}0.842$, 5.68 pairs) achieves 45--90\%; including Mistral (whose high baseline ET shifts the regime), the full range across all three models is 42--99\% (\S\ref{sec:cross-model}; quantitative analysis in Appendix~\ref{app:dual-factor}).
29	This pattern is observed across four model-dataset configurations; additional settings would be needed to establish statistical robustness.
30	
31	\paragraph{Non-Rectangularity and Sequential Masking.}
32	\label{sec:rectangularity}
33	% Data source: artifacts/rebuttal/w2_rectangularity_report.md
34	Sequential masking ($\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$) is necessary because real ontology type signatures are non-rectangular: 0/7 SciERC and only 23/96 DocRED relations satisfy $\sigma(r) = \operatorname{dom}(r) \times \operatorname{range}(r)$.
35	Independent enforcement would admit 33--37\% spurious type pairs; on SciERC, 100\% of residual DR under S1 are pairs that pass independent checks but violate $\sigma(r)$.
36	
37	\paragraph{Decidability Taxonomy.}
38	We classify constraints by when sufficient information becomes available: \emph{local} (current token only, e.g., vocabulary membership; grammar layer), \emph{prefix-decidable} (decoded prefix, e.g., domain/range; semantic layer), and \emph{non-local} (forward coreference; outside single-pass decoding, partially addressed by S2, \S\ref{sec:s2}).
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4903c4a5-e9db-4a6b-9463-babe0938394d",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "05dcc1f2-3728-4799-a28a-924c6f6b61dc",
  "sourceToolAssistantUUID": "4903c4a5-e9db-4a6b-9463-babe0938394d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T17:13:36.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EV7PkEoXCU1uaEk1zTgyPT`</summary>

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
  "parentUuid": "05dcc1f2-3728-4799-a28a-924c6f6b61dc",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQginVg1FsdcFaimHFx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "302c27ce-4eec-4cfa-8bdf-27a0a3c1b969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdSJq5AyNVryMaAtXAGXmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5676,
      "cache_read_input_tokens": 25504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 26 · 2026-05-18T17:13:36.092Z_

<details><summary>↩ Tool result · `toolu_01EV7PkEoXCU1uaEk1zTgyPT`</summary>

```text
1	% §5.1 Experimental Setup and Violation Landscape (compressed)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	\paragraph{Setup.}
8	We evaluate on two IE benchmarks:
9	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs/relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, avg.\ 5.68 valid pairs).
10	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}.
11	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
12	Violation rates are computed over successfully parsed documents; including failures as zero-violation instances adjusts rates by at most 0.23\,pp.
13	
14	\paragraph{Baseline violations and motivation.}
15	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED, comparable rates despite 14$\times$ ontology size difference; severity is driven by \emph{constraint tightness} rather than scale.
16	Per-relation rates vary by over 40\,pp (Appendix~\ref{app:per-relation-landscape}), correlating with tightness $\kappa(r)$.
17	RV on DocRED reaches 29.66\%: large vocabularies exceed prompt-based reproduction capacity.
18	Schema-informed prompting reduces DR by 62\% on SciERC but only 30\% on DocRED and is per-relation unreliable (DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp). These limitations motivate decoding-time enforcement.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "302c27ce-4eec-4cfa-8bdf-27a0a3c1b969",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "58031e51-689d-4a35-a078-f6687c90c3c0",
  "sourceToolAssistantUUID": "302c27ce-4eec-4cfa-8bdf-27a0a3c1b969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T17:13:36.530Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KcwEFcySVEoQEY5Z6dTEfH`</summary>

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
  "parentUuid": "58031e51-689d-4a35-a078-f6687c90c3c0",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQginVg1FsdcFaimHFx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e856b782-544f-4576-815c-328846c9653e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdSJq5AyNVryMaAtXAGXmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5676,
      "cache_read_input_tokens": 25504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 28 · 2026-05-18T17:13:36.540Z_

<details><summary>↩ Tool result · `toolu_01KcwEFcySVEoQEY5Z6dTEfH`</summary>

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
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Best per column in \textbf{bold} (CF excluded).
60	F1 $\times$100. Bootstrap: 10{,}000 iterations.}
61	\label{tab:scierc-ablation}
62	\end{table}
63	
64	% ──────────────────────────────────────────
65	%  (a) Core result
66	% ──────────────────────────────────────────
67	\paragraph{Core result: DR elimination at zero F1 cost.}
68	The full two-layer constraint configuration (S1) reduces domain/range
69	violations from 15.37\% to 0.93\%, a 94\% relative reduction,
70	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
71	while relation F1 moves from 8.23 to 8.36 ($+$0.13\,pp; bootstrap 95\% CI [$-$0.24, $+$0.58]\,pp, $p = 0.58$, 10{,}000 iterations).
72	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
73	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
74	The difference is not statistically significant ($p = 0.58$); constraint enforcement is F1-neutral on this dataset.
75	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains from aggressive violation removal (SciERC: 8.63 vs.\ 8.36; DocRED: 9.61 vs.\ 8.23), but at the cost of discarding up to 48\% of predictions including true positives (Appendix~\ref{app:posthoc-extended}); OntoCoDec preserves recall by enforcing constraints during generation.
76	Per-relation DR drops to $\leq$2.82\% on all types, reaching 0\% on four of seven (Appendix~\ref{app:per-relation-landscape}).
77	However, constraint enforcement elevates CF from 0.08\% to 9.90\% (\S\ref{sec:discussion}).
78	
79	% ──────────────────────────────────────────
80	%  (b) Grammar layer
81	% ──────────────────────────────────────────
82	\paragraph{Grammar layer: cost-free structural guarantees.}
83	Grammar-only constraints eliminate RV (1.39\%\,$\to$\,0\%) and ET (0.40\%\,$\to$\,0\%) with no F1 impact, while DR remains unchanged (15.37\%\,$\to$\,14.84\%).
84	This configuration represents the capability ceiling of grammar-based constrained decoding~\cite{geng2023gcd}, which enforces JSON structure and vocabulary membership but cannot reason about cross-field semantic constraints.
85	% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
86	
87	% ──────────────────────────────────────────
88	%  (c) Enabling dependency
89	% ──────────────────────────────────────────
90	\paragraph{Enabling dependency.}
91	Semantic-only reduces DR by only 24\% (11.65\%) and cannot eliminate RV (1.51\%) or ET (0.40\%), which establishes the \emph{enabling dependency}: without grammar-enforced vocabulary, the semantic layer encounters OOV types with no domain/range rules.
92	Adding the grammar layer yields a further 92\% reduction (11.65\%\,$\to$\,0.93\%).
93	
94	% ──────────────────────────────────────────
95	%  (d) S1 vs S2
96	% ──────────────────────────────────────────
97	\paragraph{S1 vs.\ S2.}
98	S2 achieves comparable DR (0.97\%) but lower R-F1 (8.03 vs.\ 8.36) with fewer triples (1{,}644 vs.\ 1{,}729) and does not resolve the CF trade-off (8.03\% vs.\ 9.90\%); we adopt S1 as the primary configuration.
99	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644
100	
101	% ──────────────────────────────────────────
102	%  (e) Composability with Fine-Tuning
103	%  exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
104	% ──────────────────────────────────────────
105	\paragraph{Composability with fine-tuning.}
106	\label{sec:composability}
107	Table~\ref{tab:composability} tests composability across zero-shot vs.\ LoRA $\times$ unconstrained vs.\ S1 for Qwen3-8B and Llama-3.1-8B.
108	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
109	%          w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
110	%          llama_scierc_unconstrained, llama_scierc_full_s1,
111	%          w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval
112	
113	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations on tight-constraint relations (Table~\ref{tab:composability}).
114	Adding S1 eliminates these: Qwen DR 1.95\%\,$\to$\,0\% ($-$0.09\,pp R-F1), Llama DR 1.11\%\,$\to$\,0.09\% ($+$0.02\,pp).
115	On DocRED, the same pattern holds: Qwen DR 0.76\%\,$\to$\,0.01\% ($-$0.30\,pp), Llama DR 0.49\%\,$\to$\,0.20\% ($+$0.51\,pp).
116	% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23
117	
118	Across all settings, fine-tuned + S1 yields DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp, which supports orthogonal composability.
119	Post-fine-tuning, grammar is a no-op; the semantic layer alone reduces DR by 39--72\% (Appendix~\ref{app:ft-ablation}).
120	CF interference drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned), tracing to \textsc{Generic}$\leftrightarrow$X schema ambiguity (Appendix~\ref{app:cf-distribution}).
121	Beam search ($k{=}4$) eliminates residual DR and reduces CF to $<$1\% for both Qwen and Llama (Appendix~\ref{app:beam-search}).
122	
123	\begin{table}[t]
124	\centering
125	\small
126	\setlength{\tabcolsep}{3pt}
127	\resizebox{\columnwidth}{!}{%
128	\begin{tabular}{@{}lll rrrr r@{}}
129	\toprule
130	\textbf{Model} & \textbf{Setting} & \textbf{Mode}
131	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
132	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
133	  & \textbf{$\Delta$DR} \\
134	\midrule
135	\multirow{4}{*}{Qwen3-8B}
136	  & \multirow{2}{*}{Zero-shot}
137	    & Unconstr.\ & 15.37 & 0.08 & 8.23  & 31.01 & --- \\
138	  & & Full S1    &  0.93 & 9.90 & 8.36  & 30.98 & $\downarrow$94\% \\
139	\cmidrule(l){2-8}
140	  & \multirow{2}{*}{LoRA}
141	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
142	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
143	\midrule
144	\multirow{4}{*}{Llama-3.1-8B}
145	  & \multirow{2}{*}{Zero-shot}
146	    & Unconstr.\ & 13.34 & 0.24 & 2.68  & 23.56 & --- \\
147	  & & Full S1    &  0.08 & 6.56 & 2.54  & 23.49 & $\downarrow$99\% \\
148	\cmidrule(l){2-8}
149	  & \multirow{2}{*}{LoRA}
150	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
151	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
152	\bottomrule
153	\end{tabular}}%
154	\caption{Composability on SciERC (551 docs): zero-shot vs.\ LoRA $\times$ unconstrained vs.\ S1.
155	Adding S1 to LoRA: DR\,$\leq$\,0.09\%, R-F1 within $\pm$0.1\,pp.
156	DocRED: Qwen DR $-$99\%, Llama DR $-$59\%.
157	F1\,$\times$100.}
158	\label{tab:composability}
159	\end{table}
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e856b782-544f-4576-815c-328846c9653e",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "41d133dc-29b4-4b27-bcc0-7ab0ebdcc47c",
  "sourceToolAssistantUUID": "e856b782-544f-4576-815c-328846c9653e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T17:13:37.134Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NvpgA5qK85pQAacXYbJqMN`</summary>

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
  "parentUuid": "41d133dc-29b4-4b27-bcc0-7ab0ebdcc47c",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQginVg1FsdcFaimHFx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "883f0598-c55d-4580-8786-6189a719ee20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdSJq5AyNVryMaAtXAGXmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5676,
      "cache_read_input_tokens": 25504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5676,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 30 · 2026-05-18T17:13:37.139Z_

<details><summary>↩ Tool result · `toolu_01NvpgA5qK85pQAacXYbJqMN`</summary>

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
19	\begin{tabular}{@{}l rrrrr rr@{}}
20	\toprule
21	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-6} \cmidrule(l){7-8}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Best per column in \textbf{bold} (CF excluded).
54	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
55	\label{tab:docred-ablation}
56	\end{table}
57	
58	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
59	\paragraph{Core result.}
60	Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET ($\to$\,0\%), and near-eliminates RV (29.66\%\,$\to$\,0.03\%).\footnote{The residual 0.03\% RV traces to a rare XGrammar automaton edge case where subword tokens from different enum entries combine into chimeric values (e.g., \texttt{member} + \texttt{icipant\_of} from \texttt{member\_of} and \texttt{participant\_of}). This is not a fundamental limitation of the approach.}
61	R-F1 improves from 7.74 to 8.23 ($+$0.50\,pp; $p < 0.001$), attributable to elimination of 5{,}189 OOV relation predictions.
62	CF increases modestly (0.10\%\,$\to$\,2.57\%), consistent with the CF$\leftrightarrow$DR trade-off (\S\ref{sec:discussion}).
63	
64	% exp_ids: phase2_docred_grammar_only
65	\paragraph{Grammar layer surfaces latent violations.}
66	Grammar-only constraints eliminate RV and ET but \emph{increase} DR to 26.17\% ($+$42\%): the baseline's 29.66\% OOV triples cannot be evaluated for DR; grammar enforcement assigns valid relation names whose domain/range rules the associated types frequently violate, \emph{revealing} latent incompatibilities that motivate the semantic layer.
67	
68	% exp_ids: phase2_docred_semantic_only, phase2_docred_full_s1
69	\paragraph{Enabling dependency and tightness ceiling.}
70	Semantic-only reduces DR by 25\% but cannot eliminate RV (29.87\%) or prevent ET increases (2.48\%\,$\to$\,4.22\%), which replicates SciERC's enabling dependency.
71	Residual DR (10.21\%) exceeds SciERC's (0.93\%) due to higher constraint tightness ($\bar{\kappa}{=}0.842$ vs.\ 0.333): residual DR of 10.21\% implies effective semantic coverage of approximately 90\%, consistent with tight constraints forcing frequent grammar-first fallback (Appendix~\ref{app:fallback-coverage}).
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "883f0598-c55d-4580-8786-6189a719ee20",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "3ce470eb-8034-4f17-9ddd-97a937bf83e7",
  "sourceToolAssistantUUID": "883f0598-c55d-4580-8786-6189a719ee20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T17:13:41.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_011itX7PWJP18CW3gALw5W4p`</summary>

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
  "parentUuid": "3ce470eb-8034-4f17-9ddd-97a937bf83e7",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQh9yZztMuDFy7XYaLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa664b66-f459-4b35-beeb-ef3292fe0468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUR7A1bRAFyLvqju5psVCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6326,
      "cache_read_input_tokens": 31180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6326,
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

_source line 32 · 2026-05-18T17:13:41.246Z_

<details><summary>↩ Tool result · `toolu_011itX7PWJP18CW3gALw5W4p`</summary>

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
10	Table~\ref{tab:cross-model} replicates full S1 with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts and evaluation.
11	Mistral serves as a third zero-shot verification point; composability evaluation (\S\ref{sec:composability}) uses LoRA, available only for Qwen and Llama.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr r@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \textbf{R-F1} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-7}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & $\uparrow$ \\
26	\midrule
27	\multirow{6}{*}{SciERC}
28	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
29	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
30	  \cmidrule(l){2-7}
31	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
32	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
33	  \cmidrule(l){2-7}
34	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
35	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
36	\midrule
37	\multirow{6}{*}{DocRED}
38	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
39	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
40	  \cmidrule(l){2-7}
41	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
42	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
43	  \cmidrule(l){2-7}
44	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
45	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
46	\bottomrule
47	\end{tabular}}%
48	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
49	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
50	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
51	F1 $\times$100.}
52	\label{tab:cross-model}
53	\end{table}
54	
55	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
56	\paragraph{Results.}
57	RV and ET are eliminated ($\leq$0.03\%) for all models on both datasets.
58	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in five of six settings (DocRED: Qwen $+$0.50\,pp, $p{<}0.001$; Llama $+$0.29\,pp, $p{=}0.013$).
59	Cross-model DR asymmetry reflects baseline RV: Llama's lower RV (16.03\% vs.\ 29.66\%) limits latent violation surfacing, yielding 2.55\% residual DR vs.\ 10.21\%.
60	CF direction depends on baseline calibration: S1 introduces CF for calibrated models (up to 12.02\%; \S\ref{sec:discussion}), while reducing CF for poorly-calibrated Mistral (56.87\%\,$\to$\,1.27\%).
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa664b66-f459-4b35-beeb-ef3292fe0468",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "8fd661a7-391a-447b-958d-408c9cb83a51",
  "sourceToolAssistantUUID": "fa664b66-f459-4b35-beeb-ef3292fe0468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T17:13:42.101Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WHa3REtMF4VTGogvcS5unf`</summary>

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
  "parentUuid": "8fd661a7-391a-447b-958d-408c9cb83a51",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQh9yZztMuDFy7XYaLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6777f46c-6831-4e5b-a7b7-ab94725a70c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUR7A1bRAFyLvqju5psVCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6326,
      "cache_read_input_tokens": 31180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6326,
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

_source line 34 · 2026-05-18T17:13:42.106Z_

<details><summary>↩ Tool result · `toolu_01WHa3REtMF4VTGogvcS5unf`</summary>

```text
1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	To test generality beyond RE, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 argument roles, 27 entity types, 245 role$\to$type constraints; Appendix~\ref{app:wikievents}).
11	The framework requires no modification: grammar compiles event/role vocabularies into a CFG; the semantic layer enforces role-conditioned type constraints via the same registry.
12	Violations extend to Event Vocabulary (EV), Role Vocabulary (RoV), and Argument Constraint (AC, analogous to DR).
13	
14	% ──────────────────────────────────────────
15	%  Table: WikiEvents three-model comparison (v3 final)
16	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
17	% ──────────────────────────────────────────
18	\begin{table}[t]
19	\centering
20	\small
21	\setlength{\tabcolsep}{2.8pt}
22	\resizebox{\columnwidth}{!}{%
23	\begin{tabular}{@{}ll rrrr rr@{}}
24	\toprule
25	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
26	& \multicolumn{2}{c}{\textbf{F1}} \\
27	\cmidrule(lr){3-6} \cmidrule(l){7-8}
28	\textbf{Model} & \textbf{Mode}
29	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
30	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
31	\midrule
32	\multirow{3}{*}{Qwen3-8B}
33	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
34	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
35	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
36	\midrule
37	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
38	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
39	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
40	  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
41	\midrule
42	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
43	  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
44	  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
45	  & Full S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
46	\bottomrule
47	\end{tabular}}%
48	\caption{WikiEvents EE results (246 documents, zero-shot).
49	Violation rates over parsed documents.
50	---: not applicable (grammar-only has no semantic-layer metrics).
51	F1 $\times$ 100.}
52	\label{tab:wikievents}
53	\end{table}
54	
55	\paragraph{Results.}
56	Unconstrained generation produces extreme vocabulary violations (EV+RoV exceeding 85\% combined; Table~\ref{tab:wikievents}), and all models yield entity F1\,=\,0 because the parser cannot identify well-formed mentions in off-schema output.
57	Full S1 eliminates EV and RoV across all three models ($\to$\,0\%), which validates tokenizer-agnostic design across byte-level BPE (Qwen, Llama) and SentencePiece (Mistral).
58	Grammar-only ablation isolates each layer: grammar eliminates EV ($\to$\,0\%) but leaves RoV at 64--77\% because the CFG cannot constrain 80 argument roles conditioned on event context; AC rises from near-zero to 8--14\%, the same latent-violation surfacing pattern observed in DocRED (\S\ref{sec:docred-results}).
59	Full S1 then drives RoV to 0\%, which demonstrates layer complementarity.
60	Residual AC (1.3--3.8\%) traces to confusion between semantically similar entity types (e.g., SID vs.\ SEN) where grammar-first fallback permits the incorrect type; CF rises to 15--21\%, consistent with the per-slot enforcement trade-off in RE.
61	
62	Post-hoc filtering is impractical for EE: it retains only 23/5{,}467 arguments for Qwen (99.6\% discarded), 3/5{,}053 for Llama, and 0/6{,}034 for Mistral, because unconstrained models generate generic role names rather than ontology-specific ones.
63	Unlike RE, where constraints are F1-neutral, EE shows measurable gains: entity F1 rises from 0\% to 11.7--17.6\% and trigger F1 increases by $+$1.5--1.8\,pp, because grammar enforcement produces schema-valid JSON that the parser can process.
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6777f46c-6831-4e5b-a7b7-ab94725a70c2",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "cbba992f-1d78-44b6-87a8-d9c49399727a",
  "sourceToolAssistantUUID": "6777f46c-6831-4e5b-a7b7-ab94725a70c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T17:13:42.519Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UoepMXSZcYRnekUkH4mewK`</summary>

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
  "parentUuid": "cbba992f-1d78-44b6-87a8-d9c49399727a",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQh9yZztMuDFy7XYaLH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a61d209-4cf1-46a1-bb23-c4b5e0d1b7d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUR7A1bRAFyLvqju5psVCQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6326,
      "cache_read_input_tokens": 31180,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6326
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 31180,
          "cache_creation_input_tokens": 6326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6326,
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

_source line 36 · 2026-05-18T17:13:42.524Z_

<details><summary>↩ Tool result · `toolu_01UoepMXSZcYRnekUkH4mewK`</summary>

```text
1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	Full S1 adds $+$13.1\% wall-clock overhead on SciERC (Qwen3-8B, zero-shot greedy, RTX PRO 6000 Blackwell); under fine-tuning, overhead drops to $+$2.3\% (61\,ms/doc).
6	Grammar compile is a one-time 44\,ms cost.
7	Details in Appendix~\ref{app:runtime}.
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Beam search ($k{=}4$) addresses greedy decoding's two residual limitations on SciERC (551 documents): DR drops to 0\% for calibrated models (Qwen 0.93\%\,$\to$\,0\%; Llama 0.08\%\,$\to$\,0\%) and CF decreases substantially (Qwen 9.90\%\,$\to$\,0.53\%; Llama 6.56\%\,$\to$\,0.93\%).
12	Combined with LoRA, both calibrated models achieve zero violations across all four metrics on SciERC (Qwen3-8B R-F1\,=\,44.23; Llama-3.1-8B R-F1\,=\,46.11; Appendix~\ref{app:beam-search}).
13	
14	% === 70B cross-scale (PLACEHOLDER — awaiting DocRED 70B results) ===
15	%\paragraph{Cross-scale generalizability.}
16	%\label{sec:70b-results}
17	%To evaluate cross-scale generalizability, we test OntoCoDec on Llama-3.1-70B-Instruct (AWQ INT4 quantization).
18	%On SciERC, the 70B model produces fewer baseline violations than its 8B counterpart (DR 6.5\% vs.\ 13.3\%), yet violations persist; OntoCoDec eliminates them entirely (DR$\to$0\%, R-F1 $-$0.03\,pp).
19	%On DocRED, [PLACEHOLDER for 70B DocRED results].
20	%Case studies comparing 8B and 70B behavior appear in Appendix~\ref{app:case-scale}.
21	
22	Appendix~\ref{app:case-studies} presents representative case studies illustrating constraint behavior across violation types.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a61d209-4cf1-46a1-bb23-c4b5e0d1b7d3",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "efb50e30-07c2-4080-b5bc-97bdb70a7ddd",
  "sourceToolAssistantUUID": "8a61d209-4cf1-46a1-bb23-c4b5e0d1b7d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T17:13:47.482Z_

<details open><summary>🔧 Tool call — Read · `toolu_011cXWWT84f4MLcpDG9gX3jT`</summary>

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
  "parentUuid": "efb50e30-07c2-4080-b5bc-97bdb70a7ddd",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQhZ3PVyj5W2tRLuiUc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49414fd9-7b4a-4006-9560-567ba8d58b37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzBKoS616wceVNKjRptAQy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4301,
      "cache_read_input_tokens": 37506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4301,
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

_source line 38 · 2026-05-18T17:13:47.488Z_

<details><summary>↩ Tool result · `toolu_011cXWWT84f4MLcpDG9gX3jT`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar} (benchmarked in JSONSchemaBench~\cite{jsonschemabench2025}), Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} guarantee format validity but cannot enforce cross-field semantic constraints such as domain/range rules.
6	
7	\paragraph{Type-Constrained Generation for IE and Code.}
8	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, and \citet{pldi2025_type_constrained_codegen} enforce type constraints in code generation; OntoCoDec migrates this to IE.
9	GCD~\cite{geng2023gcd}, GoLLIE~\cite{sainz2024gollie}, and GUIDEX~\cite{guidex2025} constrain \emph{which tokens} appear but not \emph{which type combinations} are valid per relation.
10	DORE~\cite{vukovic2024dore} uses generate-then-select with confidence thresholds; GenIE~\cite{josifoski2022genie} constrains entities via a trie without relation-specific type enforcement; EnriCo~\cite{zaratiana2024enrico} applies ASP constraints with task-specific manually authored rules.
11	BoostCD~\cite{boostcd2025} combines constrained and unconstrained IE outputs via a trained boosting model; OntoCoDec is training-free and provides per-instance type guarantees rather than statistical improvement.
12	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie,schema_rl2025} provide only soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025,slot2025} validate or restructure outputs after generation rather than preventing violations.
13	
14	\paragraph{Quality Impact.}
15	Recent work shows constrained decoding can degrade reasoning and distort output distributions~\cite{banerjee2025crane,grammar_aligned_2024,schall2025hiddencost,formattax2026}; DCCD~\cite{dccd2026} proposes unconstrained-then-constrained correction as an alternative.
16	However, extraction tasks are robust to constraints~\cite{tam2024letmespeak}: OntoCoDec's narrow type-slot constraints yield neutral F1 on SciERC and significant improvement on DocRED ($+$0.50\,pp, $p{<}0.001$); post-hoc filtering is impractical for EE (99.6\% argument loss; extended survey in Appendix~\ref{app:related_work}).
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49414fd9-7b4a-4006-9560-567ba8d58b37",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "059bfb00-2807-4ef1-94ea-d8de58d674f1",
  "sourceToolAssistantUUID": "49414fd9-7b4a-4006-9560-567ba8d58b37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T17:13:48.586Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VN2fUfJA8E6tJWq19KYDzf`</summary>

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
  "parentUuid": "059bfb00-2807-4ef1-94ea-d8de58d674f1",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQhZ3PVyj5W2tRLuiUc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31ba1ea7-e598-4997-955d-13cdf3647583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzBKoS616wceVNKjRptAQy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4301,
      "cache_read_input_tokens": 37506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4301,
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

_source line 40 · 2026-05-18T17:13:48.591Z_

<details><summary>↩ Tool result · `toolu_01VN2fUfJA8E6tJWq19KYDzf`</summary>

```text
1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints that achieve 42--99\% DR reduction across three models $\times$ three datasets with no significant F1 cost.
5	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.20\% ($<$0.6\,pp F1 cost); beam search ($k{=}4$) further eliminates both residual DR and CF for calibrated models (\S\ref{sec:beam-results}).
6	CF remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct resolution path.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31ba1ea7-e598-4997-955d-13cdf3647583",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "572c8f7d-c2f5-4a4e-b632-8e5bf225a400",
  "sourceToolAssistantUUID": "31ba1ea7-e598-4997-955d-13cdf3647583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T17:13:48.969Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PJpN4ckBSSXNve6wqZ5abH`</summary>

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
  "parentUuid": "572c8f7d-c2f5-4a4e-b632-8e5bf225a400",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQhZ3PVyj5W2tRLuiUc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8b74984-ee9d-42fa-a3d0-ed636dae4880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzBKoS616wceVNKjRptAQy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4301,
      "cache_read_input_tokens": 37506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4301,
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

_source line 42 · 2026-05-18T17:13:48.974Z_

<details><summary>↩ Tool result · `toolu_01PJpN4ckBSSXNve6wqZ5abH`</summary>

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
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for structured generation.
15	However, all of these methods operate exclusively at the syntactic level: they ensure format validity (e.g., well-formed JSON, valid enum values) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.
16	This syntactic-only limitation motivates OntoCoDec's semantic extension: our grammar layer builds on XGrammar for structural (JSON schema and enum) constraints, while a second semantic layer enforces relational type constraints that are inherently beyond the expressive power of context-free grammars.
17	
18	% ===========================================================================
19	% Paradigm 1.5: Semantic Constrained Decoding for Code
20	% ===========================================================================
21	\paragraph{Semantic Constrained Decoding for Code.}
22	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness, demonstrating that richer-than-CFG constraints can be compiled into token-level filtering.
23	In the text-to-SQL domain, PICARD~\cite{scholak2021picard} maintains an incremental SQL parsing state that rejects tokens violating syntax or referencing non-existent database columns at each decoding step, achieving state-of-the-art results on Spider and CoSQL without modifying model weights.
24	While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema (database table and column names known before decoding begins).
25	In contrast, OntoCoDec's entity registry is populated \emph{during} generation as entity spans are extracted from free text, requiring constraint sets that evolve with the decoding prefix, a fundamental distinction between querying a known schema and extracting from unstructured text.
26	Synchromesh~\cite{synchromesh_iclr2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs without fine-tuning, establishing that semantic constraints can be expressed as dynamic token masks conditioned on the generation prefix.
27	MGD~\cite{mgd_neurips2023} uses static-analysis monitors to perform incremental type checking at decode time, enabling SantaCoder-1.1B to outperform text-davinci-003 on repository-level code completion by ensuring that every generated identifier is type-correct with respect to the surrounding code context.
28	Most recently, \citet{pldi2025_type_constrained_codegen} compile full type systems, including generic types and subtyping, into prefix automata for token-level logits masking, reducing compilation errors by over 50\%.
29	This last system is the closest mechanistic analog to OntoCoDec, applying the same ``type system $\to$ automaton $\to$ logits mask'' pipeline, though in a fundamentally different domain.
30	The key technical difference lies in the constraint structure: programming-language type systems feature deep subtyping hierarchies and parametric polymorphism, whereas IE ontology axioms specify flat domain/range sets; a relation $R$ accepts head entities from set $\mathcal{D}(R)$ and tail entities from set $\mathcal{R}(R)$, with no subtype chains.
31	Conversely, IE introduces a challenge absent in code generation: the constraint target (entity type) must be inferred from free-text spans rather than read from declared type annotations, requiring a stateful entity registry that tracks extracted types during autoregressive generation.
32	These methods collectively demonstrate that semantic (type) constraints at decode time are both feasible and highly effective, but exclusively in the code domain where type systems are formally specified.
33	OntoCoDec is the first to \emph{automatically compile} IE ontology axioms, including domain/range constraints, into token-level decoding masks for information extraction, migrating the type-constrained decoding paradigm from code generation to IE.
34	
35	% ===========================================================================
36	% Paradigm 2: Vocabulary/Type-Constrained Generation
37	% ===========================================================================
38	\paragraph{Vocabulary and Type-Constrained Generation.}
39	The idea of enforcing entity-type compatibility constraints for information extraction dates back to pre-neural methods.
40	\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints (e.g., \textsc{Emp-Org} only between \textsc{Per} and \textsc{Org} entities), establishing the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.
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
56	GoLLIE~\cite{sainz2024gollie} expresses annotation guidelines as Python dataclass definitions and fine-tunes Code-LLaMA to generate typed code, achieving strong zero-shot transfer to unseen IE schemas by leveraging the implicit type structure of programming languages.
57	KnowCoder~\cite{knowcoder_acl2024} takes this further by encoding 29K entity types from Wikidata as a Python class hierarchy, training a Code-LLM to generate structured extraction code that implicitly respects type inheritance, the most comprehensive schema-as-code approach to date.
58	CodeIE~\cite{li2023codeie} similarly reformulates IE as code generation, leveraging the structural regularity of programming languages to reduce output format errors.
59	ADELIE~\cite{qi2024adelie} uses SFT and DPO to align LLMs on IE tasks, achieving state-of-the-art results among open-source models while preserving general capabilities, though compliance with ontological constraints remains a learned soft preference rather than a guarantee.
60	In the supervised setting, joint entity-relation architectures such as SpERT~\cite{eberts2020spert} and PFN~\cite{yan2021pfn} enforce type consistency implicitly through shared representations: SpERT classifies entity spans and relation pairs in a single BERT pass with span-level negative sampling, while PFN decomposes feature encoding into entity-specific, relation-specific, and shared partitions via gating mechanisms.
61	These models achieve strong performance but are limited to fixed, predefined schemas and cannot generalize to unseen ontologies without retraining, precisely the zero-shot, ontology-portable scenario that OntoCoDec targets.
62	EnriCo~\cite{zaratiana2024enrico} applies Answer Set Programming (ASP) constraints during decoding of joint entity-relation extraction models, enforcing structural type compatibility at generation time. This is a decoding-time approach, though with model-specific, manually authored constraints rather than ontology-driven compilation.
63	Training-based methods provide \emph{soft} structural guidance: the model learns to prefer valid outputs but cannot guarantee compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.
64	Importantly, training-based and decoding-time approaches are complementary rather than competing: a system like GoLLIE could be combined with OntoCoDec's constraint layers, using fine-tuning to maximize the probability of valid outputs while decoding-time enforcement eliminates residual violations.
65	OntoCoDec provides \emph{hard} decoding-time enforcement that is training-free, automatically compiled from ontology schemas, and composable with any of these training-based approaches.
66	
67	% ===========================================================================
68	% Paradigm 4: Type-Checking / Ontology Validation
69	% ===========================================================================
70	\paragraph{Post-hoc Ontology Validation.}
71	Rather than constraining generation, several methods validate LLM outputs against ontological rules after generation, applying a detect-then-fix paradigm.
72	ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale, but constraint adherence relies on prompt-level guidance, not enforcement, leaving residual violations unaddressed.
73	SPIRES/OntoGPT~\cite{spires_2024} provides an ontology-based extraction framework that grounds LLM outputs against OBO ontologies post-generation, validating extracted entities and relations through ontology lookup and correcting mismatches in a second pass, representing the prompt-then-validate paradigm in the biomedical domain.
74	OntoLogX~\cite{ontologx_2025} applies SHACL validation to LLM-generated knowledge graphs, iteratively re-prompting the LLM to correct constraint violations and reducing them by approximately 10$\times$ across multiple correction rounds. This demonstrates the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
75	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB, though their constrained inference operates over a discrete candidate set rather than during autoregressive generation.
76	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating RDF triple insertions against RDFS domain/range constraints, where each validation step requires a separate LLM call, effective but computationally expensive at scale.
77	RELATE~\cite{olasunkanmi2025relate} addresses the alignment gap between LLM-extracted biomedical relations and standardized ontology predicates through a three-stage pipeline: ontology preprocessing with predicate embeddings, similarity-based retrieval via SapBERT, and LLM-based reranking with negation handling, achieving 94\% accuracy@10 on ChemProt.
78	While RELATE demonstrates effective ontology grounding for relation extraction, its constraints are applied \emph{post-extraction} through retrieval and reranking rather than during generation, and it requires domain-specific embedding models trained on biomedical corpora.
79	OntoCoDec enforces ontology constraints \emph{during} autoregressive decoding and requires no additional trained components beyond the base LLM.
80	Concurrently, \citet{zhou2026ontologytools} compile OWL ontologies into executable tool interfaces within The World Avatar framework, requiring LLM agents to invoke ontology-aware tools that enforce semantic constraints during knowledge graph construction from scientific text.
81	This ``ontology-to-tools'' approach shares OntoCoDec's philosophy of compiling formal ontological knowledge into runtime enforcement mechanisms, but operates at the tool-call level (constraining which API functions the agent invokes) rather than at the token level (constraining which tokens the decoder produces), and requires an agentic multi-step workflow rather than single-pass autoregressive generation.
82	\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms, a middle ground between unconstrained generation and hard enforcement that reduces but cannot eliminate violations.
83	Post-hoc validation detects violations after generation, requiring rejection or correction cycles that waste compute. In our setting, 15.37\% of generated triples contain domain/range violations under unconstrained decoding, representing substantial wasted generation effort.
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
106	OntoCoDec occupies a unique position in this landscape: it is the first system to \emph{automatically compile} IE ontology schemas, including domain/range axioms, into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement without manually authored rules.
107	Unlike vocabulary-constrained methods that restrict individual tokens to a fixed set, OntoCoDec enforces \emph{cross-field relational constraints} through a stateful entity registry that tracks extracted types during autoregressive generation, enabling dynamic constraint evaluation that depends on previously decoded content.
108	This approach is orthogonal to supervised IE methods and applicable to any autoregressive LM without model modification or additional training.
109	Unlike training-based IE systems, OntoCoDec is training-free and substantially reduces type violations at inference time (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED); unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives with significant R-F1 gains on DocRED ($p \leq 0.013$) and F1-neutral impact on SciERC.
110	The two constraint layers, grammar (structural) and semantic (relational), compose via bitwise AND with an enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8b74984-ee9d-42fa-a3d0-ed636dae4880",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "ee4f16e2-2745-439f-a800-6931d6a044d3",
  "sourceToolAssistantUUID": "c8b74984-ee9d-42fa-a3d0-ed636dae4880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T17:13:53.916Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V2nxdmzmunuQJ6TVB7zYwx`</summary>

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
  "parentUuid": "ee4f16e2-2745-439f-a800-6931d6a044d3",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQi32tNGAgbk5dbCiny",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1bdf0bc-f3e2-41cf-9320-0a5a49bdeaac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gq2pgJsDVVfLipk7bNyZ2V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6298,
      "cache_read_input_tokens": 41807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6298,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 44 · 2026-05-18T17:13:54.222Z_

<details><summary>↩ Tool result · `toolu_01V2nxdmzmunuQJ6TVB7zYwx`</summary>

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
27	\emph{Grammar-first fallback} (36.6\% of type-bearing positions on SciERC) occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations. These events account for the residual DR that persists after constraint enforcement.
28	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
29	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
30	
31	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
32	On SciERC, Llama-3.1-8B shows $f_{\text{gf}} = 36.6\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\% effective coverage.
33	On DocRED, by contrast, Qwen3-8B shows $f_{\text{gf}} = 0.08\%$ (46 of 54{,}859), yielding 99.9\% coverage.
34	The large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.
35	DocRED types (\textsc{PER}, \textsc{ORG}, \textsc{LOC}, \textsc{TIME}, \textsc{NUM}, \textsc{MISC}) are all single-token, eliminating this inflation.
36	This metric directly quantifies the enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
37	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
38	
39	%%% CF-DR Trade-off Analysis %%%
40	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
41	
42	\paragraph{CF-DR Trade-off Analysis.}
43	\label{app:cf-dr-tradeoff}
44	
45	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
46	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
47	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\begin{tabular}{@{}l rrrr@{}}
53	\toprule
54	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
55	\midrule
56	Full S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
57	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
58	\midrule
59	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
60	\bottomrule
61	\end{tabular}
62	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: grammar-first fallback rate at type-bearing positions.}
63	\label{tab:cf-dr-tradeoff}
64	\end{table}
65	
66	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
67	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
68	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
69	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
70	The grammar-first fallback is triggered at 36.64\% of type-bearing positions, indicating that this conflict is structural, not a tunable hyperparameter.
71	
72	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
73	Within this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
74	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are inversely associated (Spearman $\rho = -0.77$, $n{=}6$), with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}).
75	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
76	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
77	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
78	
79	Two complementary paths can lower CF without re-routing it to DR.
80	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
81	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
82	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
83	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
84	
85	%%% Dual-Factor Quantitative Analysis %%%
86	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
87	%          llama_scierc_full_s1, llama_docred_full_s1
88	
89	\paragraph{Dual-Factor Quantitative Analysis.}
90	\label{app:dual-factor}
91	
92	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
93	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
94	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
95	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction, confirming that when model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
96	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
97	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
98	
99	\begin{figure}[t]
100	\centering
101	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
102	\caption{Residual DR vs.\ $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ across four model$\times$dataset configurations.
103	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}
104	\label{fig:dual-factor-scatter}
105	\end{figure}
106	
107	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
108	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
109	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
110	
111	\paragraph{Dataset-Dependent F1 Impact.}
112	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
113	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
114	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
115	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp), confirming that F1 gain magnitude is proportional to baseline OOV rate.
116	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
117	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
118	
119	%%% Paragraph 1: Low F1 Practical Significance %%%
120	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
121	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
122	
123	\paragraph{Practical Significance of Zero-Shot F1.}
124	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
125	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
126	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
127	When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary: Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
128	% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
129	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
130	The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
131	
132	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
133	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
134	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
135	
136	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
137	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
138	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
139	However, this precision gain comes at substantial cost.
140	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions), reducing recall from 9.46\% to 8.40\%.
141	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
142	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
143	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
144	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
145	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
146	
147	%%% CF Violation Distribution %%%
148	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
149	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
150	
151	\paragraph{Cross-Field Violation Distribution.}
152	\label{app:cf-distribution}
153	
154	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise; no mention triggered $\geq$3 types).
155	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
156	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
157	
158	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
159	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets, confirming that CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
160	
161	\begin{table}[t]
162	\centering
163	\small
164	\begin{tabular}{@{}lr r@{}}
165	\toprule
166	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
167	\midrule
168	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
169	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
170	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
171	Method $\leftrightarrow$ Task & 20 & 8.2 \\
172	Material $\leftrightarrow$ Method & 17 & 6.9 \\
173	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
174	\midrule
175	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
176	\midrule
177	\textbf{Total} & \textbf{245} & 100.0 \\
178	\bottomrule
179	\end{tabular}
180	\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).
181	All 245 violations are pairwise conflicts.
182	Conflicts involving \textsc{Generic} account for 63.3\%.}
183	\label{tab:cf-distribution}
184	\end{table}
185	
186	%%% Per-Relation DR Elimination under Fine-Tuning %%%
187	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
188	
189	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
190	\label{app:lora-per-relation}
191	
192	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
193	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
194	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
195	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
196	
197	\begin{table}[t]
198	\centering
199	\small
200	\begin{tabular}{@{}l r rr rr@{}}
201	\toprule
202	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
203	\cmidrule(lr){3-4} \cmidrule(l){5-6}
204	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
205	\midrule
206	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
207	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
208	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
209	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
210	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
211	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
212	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
213	\bottomrule
214	\end{tabular}
215	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
216	$\kappa$: constraint tightness; $n$: predicted triple count.
217	Used-for gains one triple from Evaluate-for redirection.}
218	\label{tab:lora-per-relation}
219	\end{table}
220	
221	%%% Fine-Tuned Four-Way Ablation %%%
222	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
223	
224	\paragraph{Fine-Tuned Four-Way Ablation.}
225	\label{app:ft-ablation}
226	
227	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
228	
229	\begin{table}[t]
230	\centering
231	\small
232	\setlength{\tabcolsep}{3pt}
233	\resizebox{\columnwidth}{!}{%
234	\begin{tabular}{@{}lll rrrrr rr@{}}
235	\toprule
236	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
237	\midrule
238	\multirow{8}{*}{SciERC}
239	  & \multirow{4}{*}{Qwen3-8B}
240	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
241	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
242	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
243	  & & Full S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
244	  \cmidrule(l){2-10}
245	  & \multirow{4}{*}{Llama-3.1-8B}
246	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
247	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
248	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
249	  & & Full S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
250	\midrule
251	\multirow{8}{*}{DocRED}
252	  & \multirow{4}{*}{Qwen3-8B}
253	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
254	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
255	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
256	  & & Full S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
257	  \cmidrule(l){2-10}
258	  & \multirow{4}{*}{Llama-3.1-8B}
259	    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\
260	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
261	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
262	  & & Full S1       & \textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 85.23 & 44.23 \\
263	\bottomrule
264	\end{tabular}}%
265	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
266	DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
267	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
268	Semantic layer is the sole effective DR defense, providing 39--72\% reduction.
269	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED full vs.\ unconstrained).}
270	\label{tab:ft-ablation}
271	\end{table}
272	
273	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
274	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$72\%, Llama $-$39\%).
275	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings), confirming that even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
276	F1 cost is negligible: the maximum R-F1 decrease across all 16 model$\times$dataset$\times$mode combinations is $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained), attributable to parse failure increase (7.11\%\,$\to$\,8.52\%) rather than constraint-induced extraction degradation.
277	
278	%%% Residual DR Error Analysis (Fine-Tuned) %%%
279	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
280	
281	\paragraph{Residual DR Error Analysis.}
282	\label{app:residual-dr-analysis}
283	
284	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ full S1), only 36 domain/range violations remain.
285	Manual inspection reveals four root causes:
286	
287	\begin{enumerate}[nosep,leftmargin=*]
288	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
289	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
290	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
291	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
292	\end{enumerate}
293	
294	Two dataset-specific patterns emerge.
295	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
296	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
297	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.
298	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), confirming that the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
299	
300	%%% Post-Hoc Filtering Comparison (Extended) %%%
301	% exp_ids: posthoc_*_zs, posthoc_*_ft
302	
303	\paragraph{Post-Hoc Filtering: Extended Comparison.}
304	\label{app:posthoc-extended}
305	
306	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
307	
308	\begin{table}[t]
309	\centering
310	\small
311	\setlength{\tabcolsep}{3pt}
312	\resizebox{\columnwidth}{!}{%
313	\begin{tabular}{@{}lll rrr l@{}}
314	\toprule
315	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
316	\midrule
317	\multirow{6}{*}{ZS}
318	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
319	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
320	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
321	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
322	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
323	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
324	\midrule
325	\multirow{4}{*}{FT}
326	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
327	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
328	  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\
329	  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\
330	\bottomrule
331	\end{tabular}}%
332	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
333	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
334	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
335	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
336	F1 $\times$100.}
337	\label{tab:posthoc-extended}
338	\end{table}
339	
340	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
341	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
342	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
343	
344	%%% Zero-Shot Runtime Profiling %%%
345	
346	\paragraph{Zero-Shot Runtime Profiling.}
347	\label{app:runtime}
348	
349	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and Full S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
350	Grammar compile is a one-time 0.044\,s cost (amortized to zero).
351	Overhead magnitude varies with GPU and batch configuration; the constraint logic itself adds a fixed per-token masking cost that is independent of hardware.
352	
353	%%% FT Latency %%%
354	
355	\paragraph{Fine-Tuned Latency Profiling.}
356	\label{app:ft-latency}
357	Under LoRA fine-tuning (Qwen3-8B, SciERC, 100 documents, RTX PRO 6000), per-document inference times are: unconstrained 2.594\,s, grammar-only 2.637\,s ($+$1.7\%), semantic-only 2.625\,s ($+$1.2\%), full S1 2.655\,s ($+$2.3\%, $p{<}0.0001$ paired $t$-test).
358	The combined overhead is sub-additive (2.3\% $<$ 1.7\%$+$1.2\%) because fine-tuned models produce fewer grammar-first fallback events (the semantic mask conflicts with grammar-valid tokens less often when per-slot predictions are better calibrated), reducing the number of active masking calls per document.
359	Compared to the zero-shot regime (\S\ref{app:runtime}), absolute overhead decreases from seconds-scale to milliseconds-scale: the fine-tuned model generates shorter, more structured outputs, compressing total generation time from 4.163\,s (zero-shot) to 2.594\,s (fine-tuned) per document on the same GPU.
360	
361	%%% Fuzzy Relation Matching %%%
362	
363	\paragraph{Relation Matching Protocol.}
364	\label{app:fuzzy-matching}
365	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
366	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
367	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
368	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
369	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
370	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
371	
372	%%% Per-Relation Violation Landscape %%%
373	
374	\paragraph{Per-Relation Violation Landscape.}
375	\label{app:per-relation-landscape}
376	
377	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
378	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
379	
380	\begin{table}[t]
381	\centering
382	\small
383	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
384	\label{tab:prompt_comparison}
385	\begin{tabular}{ll cccc}
386	\toprule
387	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
388	\midrule
389	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
390	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
391	\midrule
392	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
393	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
394	\bottomrule
395	\end{tabular}
396	\end{table}
397	
398	\begin{figure}[t]
399	\centering
400	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
401	\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$.}
402	\label{fig:per_relation_dr}
403	\end{figure}
404	
405	%%% WikiEvents Extended %%%
406	
407	\paragraph{WikiEvents Dataset Details.}
408	\label{app:wikievents}
409	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
410	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
411	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
412	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1bdf0bc-f3e2-41cf-9320-0a5a49bdeaac",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "0c93eae8-e6d2-4ab9-9e81-eaa299de151a",
  "sourceToolAssistantUUID": "c1bdf0bc-f3e2-41cf-9320-0a5a49bdeaac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T17:13:54.809Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BAyACbn9zpP6sE6YgNA4uS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c93eae8-e6d2-4ab9-9e81-eaa299de151a",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQi32tNGAgbk5dbCiny",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2658113-0547-4150-b59d-60114f7aa45c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gq2pgJsDVVfLipk7bNyZ2V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6298,
      "cache_read_input_tokens": 41807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6298,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 46 · 2026-05-18T17:13:54.813Z_

<details><summary>↩ Tool result · `toolu_01BAyACbn9zpP6sE6YgNA4uS`</summary>

```text
1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tabular}{@{}llcccccc@{}}
27	\toprule
28	\textbf{Model / Dataset} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
29	\midrule
30	\multirow{2}{*}{Qwen3-8B / SciERC (551)}
31	  & Greedy      & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
32	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.53} & 32.00 & 8.56 \\
33	\midrule
34	\multirow{2}{*}{Qwen3-8B / DocRED (50)}
35	  & Greedy      & 0 & 0 & 8.69 & 2.08 & 59.08 & 8.33 \\
36	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.55} & 58.64 & 9.37 \\
37	\midrule
38	\multirow{2}{*}{Llama-3.1-8B / SciERC (551)}
39	  & Greedy      & 0 & 0 & 0.08 & 6.56 & 23.49 & 2.54 \\
40	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.93} & 25.04 & 3.33 \\
41	\midrule
42	\multirow{2}{*}{Llama-3.1-8B / DocRED (50)}
43	  & Greedy      & 0 & 0 & 1.58 & 6.85 & 55.35 & 6.12 \\
44	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.94} & 55.62 & 9.47 \\
45	\midrule
46	\multirow{2}{*}{Mistral-7B / SciERC (551)}
47	  & Greedy      & 0 & 0 & 13.40 & 1.27 & 27.46 & 3.67 \\
48	  & Beam ($k{=}4$) & 0 & 0 & 13.79 & \textbf{0.57} & 26.66 & 4.37 \\
49	\midrule
50	\multirow{2}{*}{Mistral-7B / DocRED (50)}
51	  & Greedy      & 0 & 0 & 28.37 & 0.34 & 51.60 & 4.19 \\
52	  & Beam ($k{=}4$) & 0 & 0 & \textbf{21.37} & \textbf{0.19} & 51.78 & 5.70 \\
53	\bottomrule
54	\end{tabular}
55	\end{table}
56	
57	\paragraph{Discussion.}
58	For calibrated models (Qwen3-8B, Llama-3.1-8B), beam search achieves DR=0\% across all four model-dataset combinations (both SciERC with 7 entity types, 551 documents, and DocRED with 96 relation types, 50 documents), regardless of schema complexity.
59	On SciERC, beam search eliminates DR for both Qwen (0.93\%\,$\to$\,0\%) and Llama (0.08\%\,$\to$\,0\%), and substantially reduces CF (Qwen: 9.90\%\,$\to$\,0.53\%; Llama: 6.56\%\,$\to$\,0.93\%).
60	On DocRED (matched 50-document subsets), beam search eliminates DR for both Qwen (8.69\%\,$\to$\,0\%) and Llama (1.58\%\,$\to$\,0\%), with CF reductions of 74\% and 86\% respectively.
61	Llama DocRED shows the largest R-F1 gain ($+$3.4\,pp), consistent with beam search recovering valid type assignments that greedy decoding missed due to constraint fallback.
62	The CF reduction is an indirect effect: beam search reduces constraint-fallback frequency by exploring alternative token sequences that satisfy both grammar and semantic masks simultaneously, avoiding the fallback-to-grammar path that produces cross-field inconsistencies under greedy decoding.
63	
64	Mistral-7B-v0.3 constitutes a boundary condition on both datasets.
65	On SciERC (7 entity types), beam search does not reduce DR (13.4\%\,$\to$\,13.8\%), though CF drops by 55\% relative (1.27\%\,$\to$\,0.57\%) and R-F1 improves by $+$0.7\,pp; the unchanged DR confirms that all residual violations stem from entity type misclassification, not constraint-search failure.
66	On DocRED (96 relation types), beam search reduces DR by 25\% relative (28.4\%\,$\to$\,21.4\%): the more complex schema introduces constraint-search failures that beam exploration resolves, but the entity misclassification component remains.
67	This contrast reveals that beam search resolves constraint-search failure (where greedy decoding encounters $G(t) \cap S(t) = \emptyset$ conflicts) but cannot overcome fundamental model calibration limitations in entity typing.
68	
69	\paragraph{Beam width ablation.}
70	Table~\ref{tab:beam-ablation} varies beam width $k \in \{1,2,4,8\}$ on Qwen3-8B / SciERC (551 documents) under full S1 constraints.
71	
72	\begin{table}[h]
73	\centering
74	\small
75	\caption{Effect of beam width on constraint satisfaction and extraction quality (Qwen3-8B, SciERC, 551 documents, full S1 constraints). $k{=}1$ corresponds to greedy decoding.}
76	\label{tab:beam-ablation}
77	\begin{tabular}{@{}rcccc@{}}
78	\toprule
79	$k$ & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
80	\midrule
81	1 (greedy) & 0.93 & 9.90 & 30.98 & 8.36 \\
82	2          & 0.35 & 4.12 & 31.54 & \textbf{8.75} \\
83	4          & \textbf{0}    & 0.53 & 32.00 & 8.56 \\
84	8          & \textbf{0}    & \textbf{0.08} & \textbf{32.18} & 8.39 \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	DR elimination at $k{\geq}4$ confirms that constraint-search failure is resolved with moderate exploration width.
90	CF continues to decrease with larger beam (0.08\% at $k{=}8$, only 2 residual violations), while entity extraction quality improves monotonically.
91	$k{=}4$ represents the optimal cost-effectiveness trade-off: it eliminates all DR violations at roughly half the compute cost of $k{=}8$.
92	
93	\paragraph{Composability with fine-tuning.}
94	Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with full S1 constraints already achieves DR=0\% but retains CF=1.18\% (21 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.
95	Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=44.23; changes within $\pm$0.5\,pp).
96	Llama-3.1-8B (LoRA, SciERC) with full S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) with R-F1=46.11; the zero-violation result thus generalizes across calibrated model families.
97	% exp_id: q1_llama_ft_beam_scierc
98	The three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.
99	
100	Beam search on DocRED introduces a modest increase in parse failures (3/50, 6\%) compared to greedy (1.1\%), as longer beam-generated sequences occasionally produce malformed JSON in complex documents.
101	Wall-clock overhead is modest; \texttt{early\_stopping} terminates generation once all beams produce a complete sequence, limiting the additional compute to partial-sequence exploration rather than full-length replication.
102	Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
103	
104	We also explored a type-consensus constraint that forces identical entity types across all relations within a document.
105	However, CF violations occur precisely where the consensus type conflicts with domain-range constraints, creating a fundamental CF$\leftrightarrow$DR trade-off.
106	With DR-aware enforcement (skipping consensus when it would violate domain-range), the layer becomes a no-op (100\% skip rate on 551 SciERC documents and 50 DocRED documents).
107	This confirms that beam search resolves the CF$\leftrightarrow$DR tension through a fundamentally different mechanism: token-level exploration of paths satisfying both constraints simultaneously.
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2658113-0547-4150-b59d-60114f7aa45c",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "17a83bd2-a51c-425a-885c-a37bfcdc2a80",
  "sourceToolAssistantUUID": "e2658113-0547-4150-b59d-60114f7aa45c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T17:13:55.219Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bgga8o1VxPg9DJW1vHzef9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17a83bd2-a51c-425a-885c-a37bfcdc2a80",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQi32tNGAgbk5dbCiny",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03174474-f674-4fd3-9d25-63e9cfc66bed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gq2pgJsDVVfLipk7bNyZ2V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6298,
      "cache_read_input_tokens": 41807,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6298
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 41807,
          "cache_creation_input_tokens": 6298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6298,
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

_source line 48 · 2026-05-18T17:13:55.224Z_

<details><summary>↩ Tool result · `toolu_01Bgga8o1VxPg9DJW1vHzef9`</summary>

```text
1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	
10	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
11	
12	\subsection{Domain-Range Correction}
13	\label{app:case-dr}
14	
15	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
16	
17	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red} = violation; \textcolor{fixed}{green} = corrected.}
23	\label{tab:case1}
24	\begin{tabular}{@{}p{3.2cm}lll@{}}
25	\toprule
26	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
27	\midrule
28	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
29	\midrule
30	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
31	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
32	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Used-for(model approach, recover) & Method & Task & \ding{51} \\
34	\midrule
35	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
36	\midrule
37	Feature-of(recover, shapes) & Task & \textcolor{fixed}{Task} & \textcolor{fixed}{\ding{51}} \\
38	Feature-of(recover, poses) & Task & \textcolor{fixed}{Task} & \textcolor{fixed}{\ding{51}} \\
39	Used-for(model approach, recover) & Method & Task & \ding{51} \\
40	\bottomrule
41	\end{tabular}
42	\end{table}
43	
44	\subsection{Dual-Layer Vocabulary and Type Correction}
45	\label{app:case-rv-dr}
46	
47	\noindent\textbf{Input (DocRED, Qwen3-8B):} \textit{``Skai TV is a Greek free-to-air television network based in Piraeus. It is part of the Skai Group, one of the largest media groups in the country.''}
48	
49	The unconstrained model generates natural-language relation names (e.g., ``country of origin'') instead of Wikidata P-codes, triggering RV violations. The grammar layer forces valid P-codes; the semantic layer ensures type compatibility (Table~\ref{tab:case2}).
50	
51	\begin{table}[h]
52	\centering
53	\small
54	\caption{Layer~1 eliminates RV violations; Layer~2 corrects DR types on DocRED.}
55	\label{tab:case2}
56	\begin{tabular}{@{}p{4.5cm}p{1.8cm}p{1.2cm}@{}}
57	\toprule
58	\textbf{Unconstrained Output} & \textbf{Violation} & \textbf{Type} \\
59	\midrule
60	rel=``country of origin'' & Not in schema & RV \\
61	rel=``headquarters location'' & Not in schema & RV \\
62	rel=``part of'' & Not in schema & RV \\
63	rel=``location of formation'' & Not in schema & RV \\
64	\midrule
65	\textbf{OntoCoDec Output} & & \\
66	\midrule
67	rel=P495 (Skai TV, Greece) & ORG$\to$LOC & \ding{51} \\
68	rel=P159 (Skai TV, Piraeus) & ORG$\to$LOC & \ding{51} \\
69	rel=P127 (Skai TV, Skai Group) & ORG$\to$ORG & \ding{51} \\
70	rel=P17 (Piraeus, Greece) & LOC$\to$LOC & \ding{51} \\
71	\bottomrule
72	\end{tabular}
73	\end{table}
74	
75	\subsection{Scale Effect on Schema Compliance}
76	\label{app:case-scale}
77	
78	\noindent\textbf{Input (SciERC):} \textit{``This paper investigates the utility of applying standard MT evaluation methods (BLEU, NIST, WER and PER) to building classifiers to predict semantic equivalence and entailment.''}
79	
80	Both Qwen3-8B and Llama-3.1-70B-Instruct (AWQ INT4) mistype ``MT evaluation methods'' as \textsc{Method} (gold: \textsc{Metric}), but the downstream constraint behavior differs (Table~\ref{tab:case3}). The 70B model produces fewer violations (2 vs.\ 4) and chooses a different relation (Part-of vs.\ Hyponym-of), yet OntoCoDec corrects both.
81	
82	\begin{table}[h]
83	\centering
84	\small
85	\caption{8B vs.\ 70B on the same input. OntoCoDec corrects violations at both scales; CF arises when type corrections conflict with entity-list assignments.}
86	\label{tab:case3}
87	\begin{tabular}{@{}llll@{}}
88	\toprule
89	\textbf{Setting} & \textbf{Relation} & \textbf{Types} & \textbf{DR} \\
90	\midrule
91	\multicolumn{4}{@{}l}{\textit{Qwen3-8B Unconstrained}} \\
92	Hyponym-of(MT eval, BLEU) & Meth$\to$\textcolor{violation}{Metric} & \textcolor{violation}{\ding{55}} \\
93	Hyponym-of(MT eval, NIST) & Meth$\to$\textcolor{violation}{Metric} & \textcolor{violation}{\ding{55}} \\
94	Hyponym-of(MT eval, WER) & Meth$\to$\textcolor{violation}{Metric} & \textcolor{violation}{\ding{55}} \\
95	Hyponym-of(MT eval, PER) & Meth$\to$\textcolor{violation}{Metric} & \textcolor{violation}{\ding{55}} \\
96	\midrule
97	\multicolumn{4}{@{}l}{\textit{Qwen3-8B OntoCoDec}} \\
98	Hyponym-of(MT eval, BLEU) & Meth$\to$\textcolor{fixed}{Meth} & \textcolor{fixed}{\ding{51}} \\
99	Hyponym-of(MT eval, NIST) & Meth$\to$\textcolor{fixed}{Meth} & \textcolor{fixed}{\ding{51}} \\
100	\multicolumn{3}{@{}l}{\textcolor{cfwarn}{CF: BLEU typed Metric in entity list, Method in relation}} \\
101	\midrule
102	\multicolumn{4}{@{}l}{\textit{Llama-3.1-70B Unconstrained}} \\
103	Part-of(BLEU, MT eval) & Metric$\to$\textcolor{violation}{Meth} & \textcolor{violation}{\ding{55}} \\
104	Part-of(NIST, MT eval) & Metric$\to$\textcolor{violation}{Meth} & \textcolor{violation}{\ding{55}} \\
105	\midrule
106	\multicolumn{4}{@{}l}{\textit{Llama-3.1-70B OntoCoDec}} \\
107	Part-of(BLEU, MT eval) & Metric$\to$\textcolor{fixed}{Generic} & \textcolor{fixed}{\ding{51}} \\
108	Part-of(NIST, MT eval) & Metric$\to$\textcolor{fixed}{Generic} & \textcolor{fixed}{\ding{51}} \\
109	\bottomrule
110	\end{tabular}
111	\end{table}
112	
113	\subsection{Limitation: Trajectory Divergence under Constraints}
114	\label{app:case-cf}
115	
116	\noindent\textbf{Input (SciERC, Mistral-7B):} \textit{``Amorph recognizes NE items in two stages: dictionary lookup and rule application.''}
117	
118	The gold annotation types ``Amorph'' as \textsc{Method} and ``NE items'' as \textsc{OtherScientificTerm}, with Used-for(Amorph, NE items). The unconstrained model mistypes ``Amorph'' but coincidentally produces the correct relation. Under OntoCoDec, modified token probabilities alter the generation trajectory entirely, producing a different (non-gold) relation (Table~\ref{tab:case4}). This illustrates a fundamental property of autoregressive generation under modified distributions: constraint enforcement can change the entire output path, not just individual token choices.
119	
120	\begin{table}[h]
121	\centering
122	\small
123	\caption{Constrained decoding changes the generation trajectory. The unconstrained model coincidentally produced the gold triple despite type errors.}
124	\label{tab:case4}
125	\begin{tabular}{@{}p{4.2cm}ll@{}}
126	\toprule
127	\textbf{Setting} & \textbf{Output} & \textbf{Gold?} \\
128	\midrule
129	\textbf{Gold} & Used-for(Amorph\textsuperscript{Meth}, NE items\textsuperscript{OtherSci}) & -- \\
130	\midrule
131	\textbf{Unconstr.} & Used-for(Amorph\textsuperscript{OtherSci}, NE items\textsuperscript{Task}) & \textcolor{fixed}{\ding{51}} \\
132	\midrule
133	\textbf{OntoCoDec} & Used-for(Amorph\textsuperscript{OtherSci}, recognizes\textsuperscript{Gen}) & \textcolor{violation}{\ding{55}} \\
134	 & Feature-of(NE items\textsuperscript{Task}, in two stages\textsuperscript{Gen}) & \textcolor{violation}{\ding{55}} \\
135	\bottomrule
136	\end{tabular}
137	\end{table}
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03174474-f674-4fd3-9d25-63e9cfc66bed",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "75c87a4c-e537-4d63-88e2-3211a3a064f0",
  "sourceToolAssistantUUID": "03174474-f674-4fd3-9d25-63e9cfc66bed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-18T17:13:59.122Z_

Now let me read the remaining appendices and the bibliography to complete my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75c87a4c-e537-4d63-88e2-3211a3a064f0",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQiVRdotceR82GDsUmS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "704d39f0-3914-47b1-9bfd-e04eab1f9789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkaJXmV8gB23TDkX5XNQLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18759,
      "cache_read_input_tokens": 48105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18759,
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

_source line 50 · 2026-05-18T17:14:01.630Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SCgA9b5ygh8zaKCGV7vnN6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "704d39f0-3914-47b1-9bfd-e04eab1f9789",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQiVRdotceR82GDsUmS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91af8646-31da-495f-bdde-c9ea603ac4bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkaJXmV8gB23TDkX5XNQLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18759,
      "cache_read_input_tokens": 48105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18759,
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

_source line 51 · 2026-05-18T17:14:01.636Z_

<details><summary>↩ Tool result · `toolu_01SCgA9b5ygh8zaKCGV7vnN6`</summary>

```text
1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding; constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ "relations": [\{"head": "head entity", "tail": "tail entity", "type": "relation name",} \\
40	\texttt{\ \ "head\_type": "ENTITY\_TYPE", "tail\_type": "ENTITY\_TYPE"\}]\}} \\[4pt]
41	\texttt{Output ONLY the JSON, no other text.} \\
42	\midrule
43	\textbf{DocRED --- User Prompt} \\
44	\midrule
45	\texttt{(Document text provided inline in the user message.)} \\
46	\bottomrule
47	\end{tabular}
48	\caption{Extraction prompts used in all experiments.
49	The same prompts are used for both unconstrained and constrained decoding; OntoCoDec's constraints operate at the logit level during generation.
50	Schema-informed prompts (\S\ref{sec:violation_landscape}) additionally include valid (head type, tail type) pairs per relation.}
51	\label{tab:prompts}
52	\end{table*}
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91af8646-31da-495f-bdde-c9ea603ac4bf",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "2fe31be4-397c-483b-969f-4a3d9898ecb8",
  "sourceToolAssistantUUID": "91af8646-31da-495f-bdde-c9ea603ac4bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-18T17:14:02.032Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CvuNHfzWFsLzqSFYdoFSdU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fe31be4-397c-483b-969f-4a3d9898ecb8",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQiVRdotceR82GDsUmS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77fe0140-0d6f-48cf-8ba1-2001b063b6fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkaJXmV8gB23TDkX5XNQLX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18759,
      "cache_read_input_tokens": 48105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18759,
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

_source line 53 · 2026-05-18T17:14:02.038Z_

<details><summary>↩ Tool result · `toolu_01CvuNHfzWFsLzqSFYdoFSdU`</summary>

```text
1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77fe0140-0d6f-48cf-8ba1-2001b063b6fc",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "7a69a7c0-27a2-495d-b6ea-e736a72261ed",
  "sourceToolAssistantUUID": "77fe0140-0d6f-48cf-8ba1-2001b063b6fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-18T17:14:02.530Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PEDwDhY8d2NKVdTT5F4ELu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a69a7c0-27a2-495d-b6ea-e736a72261ed",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQiVRdotceR82GDsUmS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a28f155a-23a2-4fa7-b65c-1c61224b3ae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkaJXmV8gB23TDkX5XNQLX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18759,
      "cache_read_input_tokens": 48105,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18759
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 48105,
          "cache_creation_input_tokens": 18759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18759,
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

_source line 55 · 2026-05-18T17:14:02.543Z_

<details><summary>↩ Tool result · `toolu_01PEDwDhY8d2NKVdTT5F4ELu`</summary>

```text
1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead drops to $+$2.3\% as the model produces shorter, more structured outputs (Appendix~\ref{app:ft-latency}).
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a28f155a-23a2-4fa7-b65c-1c61224b3ae2",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "43ff1ddd-e0f4-48c2-a319-e744f89b5aea",
  "sourceToolAssistantUUID": "a28f155a-23a2-4fa7-b65c-1c61224b3ae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-18T17:14:08.204Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016XBSyGekBrQrvWaiZmVqxc`</summary>

```json
{
  "pattern": "**/relwork_new_entries.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43ff1ddd-e0f4-48c2-a319-e744f89b5aea",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQj3C5p2u49Kzkd2qsr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69f405ad-2483-49e3-9e59-785324c50c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UU9aebb5VBcTtnS6wqtwkG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2399,
      "cache_read_input_tokens": 66864,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2399
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 66864,
          "cache_creation_input_tokens": 2399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2399,
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

_source line 57 · 2026-05-18T17:14:08.228Z_

<details><summary>↩ Tool result · `toolu_016XBSyGekBrQrvWaiZmVqxc`</summary>

```text
artifacts/_project/paper/relwork_new_entries.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69f405ad-2483-49e3-9e59-785324c50c97",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "3a756318-71a7-4f10-9def-08b67563944c",
  "sourceToolAssistantUUID": "69f405ad-2483-49e3-9e59-785324c50c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-18T17:14:11.074Z_

<details open><summary>🔧 Tool call — Read · `toolu_018bx9JemG8CmeKMLWWCD5YM`</summary>

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
  "parentUuid": "3a756318-71a7-4f10-9def-08b67563944c",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQjSnQgK7UXn3c3icgn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd84286d-68ac-4405-9ef3-76f1f48eaa17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012j6PsxtYibAPSK7txtt4Y8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 135,
      "cache_read_input_tokens": 69263,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 69263,
          "cache_creation_input_tokens": 135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 135,
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

_source line 59 · 2026-05-18T17:14:11.466Z_

<details><summary>↩ Tool result · `toolu_018bx9JemG8CmeKMLWWCD5YM`</summary>

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
401	% D015 reviewer-requested references (5 entries)
402	% ============================================================
403	
404	% Confirmed via: GitHub guidance-ai/guidance, Microsoft Research project page
405	@misc{guidance2023,
406	  title        = {Guidance: A Guidance Language for Controlling Large Language Models},
407	  author       = {Lundberg, Scott and Ribeiro, Marco Tulio},
408	  year         = {2023},
409	  url          = {https://github.com/guidance-ai/guidance},
410	  note         = {Microsoft Research}
411	}
412	
413	% Confirmed via: OpenReview US-TP-xnXI, arXiv:2101.05779, Amazon Science
414	@inproceedings{paolini2021tanl,
415	  title     = {Structured Prediction as Translation between Augmented Natural Languages},
416	  author    = {Paolini, Giovanni and Athiwaratkun, Ben and Krone, Jason and Ma, Jie and Achille, Alessandro and Anubhai, Rishita and dos Santos, Cicero Nogueira and Xiang, Bing and Soatto, Stefano},
417	  booktitle = {International Conference on Learning Representations},
418	  year      = {2021},
419	  url       = {https://openreview.net/forum?id=US-TP-xnXI}
420	}
421	
422	% Confirmed via: ACL Anthology 2021.findings-emnlp.204, GitHub Babelscape/rebel
423	@inproceedings{cabot2021rebel,
424	  title     = {{REBEL}: Relation Extraction By End-to-end Language Generation},
425	  author    = {Huguet Cabot, Pere-Llu{\'\i}s and Navigli, Roberto},
426	  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2021},
427	  pages     = {2370--2381},
428	  year      = {2021},
429	  url       = {https://aclanthology.org/2021.findings-emnlp.204/}
430	}
431	
432	% Confirmed via: IJCAI 2016 Proceedings/16/Papers/421, GitHub thunlp/TKRL
433	@inproceedings{xie2016tkrl,
434	  title     = {Representation Learning of Knowledge Graphs with Hierarchical Types},
435	  author    = {Xie, Ruobing and Liu, Zhiyuan and Sun, Maosong},
436	  booktitle = {Proceedings of the 25th International Joint Conference on Artificial Intelligence ({IJCAI})},
437	  pages     = {2965--2971},
438	  year      = {2016},
439	  url       = {https://www.ijcai.org/Proceedings/16/Papers/421.pdf}
440	}
441	
442	% ============================================================
443	% Batch 3: New entries added 2026-05-16 (3 entries, Director-requested)
444	% ============================================================
445	
446	% Confirmed via: arXiv:2403.01632, OpenReview HiUZtgAPoH, Illinois Experts page
447	% NOTE: Director specified ICML 2024 — verify volume/pages
448	@inproceedings{ugare2024syncode,
449	  title     = {{SynCode}: {LLM} Generation with Grammar Augmentation},
450	  author    = {Ugare, Shubham and Suresh, Tarun and Kang, Hangoo and Misailovic, Sasa and Singh, Gagandeep},
451	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
452	  year      = {2024},
453	  series    = {PMLR},
454	  volume    = {235},
455	  url       = {https://arxiv.org/abs/2403.01632}
456	}
457	
458	% Confirmed via: OpenReview ac93gRzxxV, ICLR 2025 poster page, arXiv:2410.07295
459	@inproceedings{ugare2025itergen,
460	  title     = {{IterGen}: Iterative Semantic-aware Structured {LLM} Generation with Backtracking},
461	  author    = {Ugare, Shubham and Suresh, Tarun and Banerjee, Debangshu and Misailovic, Sasa and Singh, Gagandeep},
462	  booktitle = {The Thirteenth International Conference on Learning Representations},
463	  year      = {2025},
464	  url       = {https://openreview.net/forum?id=ac93gRzxxV}
465	}
466	
467	% Confirmed via: ACL Anthology 2025.emnlp-main.926, arXiv:2506.14901, EPFL dlab
468	@inproceedings{boostcd2025,
469	  title     = {Combining Constrained and Unconstrained Decoding via Boosting: {BoostCD} and Its Application to Information Extraction},
470	  author    = {Sakota, Marija and Geng, Saibo and Josifoski, Martin and West, Robert},
471	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
472	  year      = {2025},
473	  url       = {https://aclanthology.org/2025.emnlp-main.926/}
474	}
475	
476	% ============================================================
477	% Dataset & model references (5 entries)
478	% ============================================================
479	
480	% Confirmed via: ACL Anthology D18-1360, arXiv:1808.09602
481	@inproceedings{luan2018scierc,
482	  title     = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
483	  author    = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
484	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
485	  pages     = {3219--3232},
486	  year      = {2018},
487	  address   = {Brussels, Belgium},
488	  url       = {https://aclanthology.org/D18-1360/}
489	}
490	
491	% Confirmed via: ACL Anthology P19-1074, arXiv:1906.06127
492	@inproceedings{yao2019docred,
493	  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
494	  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
495	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
496	  pages     = {764--777},
497	  year      = {2019},
498	  address   = {Florence, Italy},
499	  url       = {https://aclanthology.org/P19-1074/}
500	}
501	
502	% Confirmed via: arXiv:2302.10205, Semantic Scholar
503	@article{wei2023zeroshot,
504	  title   = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},
505	  author  = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},
506	  journal = {arXiv preprint arXiv:2302.10205},
507	  year    = {2023},
508	  url     = {https://arxiv.org/abs/2302.10205}
509	}
510	
511	% Confirmed via: arXiv:2505.09388, Hugging Face model cards
512	@article{qwen2025qwen3,
513	  title   = {Qwen3 Technical Report},
514	  author  = {{Qwen Team}},
515	  journal = {arXiv preprint arXiv:2505.09388},
516	  year    = {2025},
517	  url     = {https://arxiv.org/abs/2505.09388}
518	}
519	
520	% Confirmed via: NeurIPS 2024 proceedings, arXiv:2312.07104
521	@inproceedings{zheng2024sglang,
522	  title     = {{SGLang}: Efficient Execution of Structured Language Model Programs},
523	  author    = {Zheng, Lianmin and Yin, Liangsheng and Xie, Zhiqiang and Sun, Chuyue and Huang, Jeff and Yu, Cody Hao and Cao, Shiyi and Kozyrakis, Christos and Stoica, Ion and Gonzalez, Joseph E. and Barrett, Clark and Sheng, Ying},
524	  booktitle = {Advances in Neural Information Processing Systems},
525	  volume    = {37},
526	  year      = {2024},
527	  url       = {https://arxiv.org/abs/2312.07104}
528	}
529	
530	% Confirmed via: arXiv, ACL 2024
531	@inproceedings{zaratiana2023gliner,
532	  title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
533	  author    = {Zaratiana, Urchade and Ngoudi, Nadi and Aziziaden, Amir and Conf, Caleb},
534	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
535	  year      = {2024},
536	  url       = {https://arxiv.org/abs/2311.08526}
537	}
538	
539	% Confirmed via: ACL Anthology 2021.naacl-main.69
540	@inproceedings{li2021document,
541	  title     = {Document-Level Event Argument Extraction by Conditional Generation},
542	  author    = {Li, Sha and Ji, Heng and Han, Jiawei},
543	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
544	  pages     = {894--908},
545	  year      = {2021},
546	  url       = {https://aclanthology.org/2021.naacl-main.69/}
547	}
548	
549	% Confirmed via: ACL Anthology, SIGDIAL 2024
550	@inproceedings{vukovic2024dore,
551	  title     = {{DORE}: A Dataset for {Portuguese} Knowledge Graph Construction and a Reproduction of a {LLM}-based Ontology-Constrained Approach},
552	  author    = {Vukovi{\'c}, Mila and Prange, Jakob and Navigli, Roberto},
553	  booktitle = {Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL)},
554	  pages     = {291--303},
555	  year      = {2024},
556	  url       = {https://aclanthology.org/2024.sigdial-1.25/}
557	}
558	
559	% ============================================================
560	% New citations added 2026-05-18 (literature freshness check)
561	% ============================================================
562	
563	@inproceedings{grammar_aligned_2024,
564	    author    = {Kanghee Park and Jiayu Wang and Taylor Berg-Kirkpatrick and Nadia Polikarpova and Loris D'Antoni},
565	    title     = {Grammar-Aligned Decoding},
566	    booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS 2024)},
567	    year      = {2024},
568	    url       = {https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html},
569	}
570	
571	@article{formattax2026,
572	    author    = {Ivan Lee and Loris D'Antoni and Taylor Berg-Kirkpatrick},
573	    title     = {The Format Tax},
574	    journal   = {arXiv preprint arXiv:2604.03616},
575	    year      = {2026},
576	    url       = {https://arxiv.org/abs/2604.03616},
577	}
578	
579	@article{dccd2026,
580	    author    = {Avinash Reddy and Thayne T. Walker and James S. Ide and Amrit Singh Bedi},
581	    title     = {Draft-Conditioned Constrained Decoding for Structured Generation in {LLMs}},
582	    journal   = {arXiv preprint arXiv:2603.03305},
583	    year      = {2026},
584	    url       = {https://arxiv.org/abs/2603.03305},
585	}
586	
587	@inproceedings{slot2025,
588	    author    = {Zhengyuan Shen and Darren Yow-Bang Wang and Soumya Smruti Mishra and Zhichao Xu and Yifei Teng and Haibo Ding},
589	    title     = {{SLOT}: Structuring the Output of Large Language Models},
590	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
591	    year      = {2025},
592	    pages     = {472--491},
593	    publisher = {Association for Computational Linguistics},
594	    url       = {https://aclanthology.org/2025.emnlp-industry.32/},
595	}
596	
597	@inproceedings{guidex2025,
598	    author    = {Neil De La Fuente and Oscar Sainz and Iker Garc{\'\i}a-Ferrero and Eneko Agirre},
599	    title     = {{GUIDEX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},
600	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
601	    year      = {2025},
602	    publisher = {Association for Computational Linguistics},
603	    url       = {https://aclanthology.org/2025.findings-acl.1245/},
604	}
605	
606	@inproceedings{schema_rl2025,
607	    author    = {Yaxi Lu and Haolun Li and Xin Cong and Zhong Zhang and Yesai Wu and Yankai Lin and Zhiyuan Liu and Fangming Liu and Maosong Sun},
608	    title     = {Learning to Generate Structured Output with Schema Reinforcement Learning},
609	    booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},
610	    year      = {2025},
611	    pages     = {4905--4918},
612	    publisher = {Association for Computational Linguistics},
613	    url       = {https://aclanthology.org/2025.acl-long.243/},
614	}
615	
616	@article{jsonschemabench2025,
617	    author    = {Saibo Geng and Hudson Cooper and Micha{\l} Moskal and Samuel Jenkins and Julian Berman and Nathan Ranchin and Robert West and Eric Horvitz and Harsha Nori},
618	    title     = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},
619	    journal   = {arXiv preprint arXiv:2501.10868},
620	    year      = {2025},
621	    url       = {https://arxiv.org/abs/2501.10868},
622	}
623	
624	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd84286d-68ac-4405-9ef3-76f1f48eaa17",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "9a11ed72-6157-4dd5-8df2-404137632574",
  "sourceToolAssistantUUID": "fd84286d-68ac-4405-9ef3-76f1f48eaa17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-18T17:14:14.610Z_

Now let me also check the remaining appendices and the paper framing document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a11ed72-6157-4dd5-8df2-404137632574",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQjgZPaifpiSQPaUTbS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80a3389b-dbe4-47d0-b000-18d42a1e7359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQMPTFA1fKf9omCTgtCRzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 69398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12529,
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

_source line 61 · 2026-05-18T17:14:17.111Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H2ez3jMQFbECCHShy4SYwF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80a3389b-dbe4-47d0-b000-18d42a1e7359",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQjgZPaifpiSQPaUTbS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d27cbd11-0388-48c6-bc77-aa95eb071596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQMPTFA1fKf9omCTgtCRzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 69398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12529,
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

_source line 62 · 2026-05-18T17:14:17.117Z_

<details><summary>↩ Tool result · `toolu_01H2ez3jMQFbECCHShy4SYwF`</summary>

```text
1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 &  5.6 \\
43	             & Const. &   0 &    0 &  731 & 200 &  931 & 54.8 &  5.8 \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	\begin{table}[h]
49	\centering
50	\small
51	\caption{Violation reduction percentage by document length bin.}
52	\label{tab:doc-length-reduction}
53	\begin{tabular}{l rr rr}
54	\toprule
55	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{DocRED}} \\
56	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
57	\textbf{Bin} & \textbf{Viols (U$\to$C)} & \textbf{Red.\%} & \textbf{Viols (U$\to$C)} & \textbf{Red.\%} \\
58	\midrule
59	Short  & 63 $\to$ 10  & 84.1 & 2445 $\to$ 633  & 74.1 \\
60	Medium & 119 $\to$ 22 & 81.5 & 2941 $\to$ 729  & 75.2 \\
61	Long   & 118 $\to$ 24 & 79.7 & 3550 $\to$ 931  & 73.8 \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	
66	The violation reduction rate is consistent across all length bins: 80--84\% for SciERC and 74--75\% for DocRED.
67	Longer documents produce more violations in the unconstrained setting (e.g., DocRED long-bin: 3,550 vs.\ short-bin: 2,445), yet OntoCoDec achieves proportionally similar reduction, confirming that the constraint framework scales reliably with document complexity.
68	ET and RV violations are fully eliminated across all bins.
69	F1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d27cbd11-0388-48c6-bc77-aa95eb071596",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "3abe08a8-fce0-42d5-91d6-e7232f65f1c4",
  "sourceToolAssistantUUID": "d27cbd11-0388-48c6-bc77-aa95eb071596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-18T17:14:17.914Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MbwE3R9F4M9gSw9s2iYVKf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3abe08a8-fce0-42d5-91d6-e7232f65f1c4",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQjgZPaifpiSQPaUTbS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f925c5e9-10ee-4298-b5ba-435c355466bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQMPTFA1fKf9omCTgtCRzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 69398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12529,
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

_source line 64 · 2026-05-18T17:14:17.920Z_

<details><summary>↩ Tool result · `toolu_01MbwE3R9F4M9gSw9s2iYVKf`</summary>

```text
1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC. ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (ET and RV drop to 0\%) for all three prompt variants. Domain-range violations are reduced by 94.0\%--94.6\%, with a standard deviation of only 0.3 percentage points across prompts. Meanwhile, F1 scores remain effectively unchanged: the largest shift is 0.13 percentage points (R-F1, Default prompt), confirming that constraint enforcement does not degrade extraction quality.
31	
32	Notably, prompt variation has a measurable effect on baseline (unconstrained) violation rates, with DR ranging from 11.1\% (Detailed) to 16.9\% (Minimal). Under constrained decoding, this range narrows to 0.64\%--0.93\%, a 20$\times$ reduction in cross-prompt variance. This convergence is expected: because OntoCoDec enforces constraints at the token level during decoding, it operates independently of prompt content. The consistent reduction rates across diverse prompt styles confirm that the mechanism is orthogonal to prompting and generalizes without prompt-specific tuning.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f925c5e9-10ee-4298-b5ba-435c355466bf",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "bb437e7c-a182-4192-ae81-f0cbb3ea2b1c",
  "sourceToolAssistantUUID": "f925c5e9-10ee-4298-b5ba-435c355466bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-18T17:14:18.563Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RyeLq3KMurmt2YpL33bBJU`</summary>

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
  "parentUuid": "bb437e7c-a182-4192-ae81-f0cbb3ea2b1c",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQjgZPaifpiSQPaUTbS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77c6f5bf-2beb-4d46-873b-1eb30b654812",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQMPTFA1fKf9omCTgtCRzV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 69398,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12529
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 69398,
          "cache_creation_input_tokens": 12529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12529,
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

_source line 66 · 2026-05-18T17:14:18.578Z_

<details><summary>↩ Tool result · `toolu_01RyeLq3KMurmt2YpL33bBJU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77c6f5bf-2beb-4d46-873b-1eb30b654812",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "5683962d-152d-40d0-b96e-89733c0d4caa",
  "sourceToolAssistantUUID": "77c6f5bf-2beb-4d46-873b-1eb30b654812",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-18T17:14:22.742Z_

Now let me also read the appendix on Llama per-relation results for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5683962d-152d-40d0-b96e-89733c0d4caa",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQkD8uMF2uuZ8np969R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "952cd360-c790-4a86-8b64-0b654d5135af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQLmD3hw4MJZSvJQbtGfWX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3133,
      "cache_read_input_tokens": 81927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3133,
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

_source line 68 · 2026-05-18T17:14:24.527Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FCe689q6DxunzeN7anhGDF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "952cd360-c790-4a86-8b64-0b654d5135af",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQkD8uMF2uuZ8np969R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8602057-60c6-4eb5-aa60-4844ce427254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQLmD3hw4MJZSvJQbtGfWX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3133,
      "cache_read_input_tokens": 81927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3133,
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

_source line 69 · 2026-05-18T17:14:24.532Z_

<details><summary>↩ Tool result · `toolu_01FCe689q6DxunzeN7anhGDF`</summary>

```text
1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's residual DR on the same relations is markedly lower (P1198 reaches only 20.0\%) and no relation-level fallback concentration comparable to Qwen is observed.
37	% exp_ids: llama_docred_full_s1, qwen_docred_full_s1
38	The substantially lower residual DR for Llama (2.55\% vs.\ Qwen's 10.21\%) on the same ontology confirms that constraint tightness alone does not determine enforcement effectiveness: the model's baseline vocabulary compliance (RV) modulates the fraction of triples eligible for semantic-layer enforcement.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8602057-60c6-4eb5-aa60-4844ce427254",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "fffe08f8-e3fd-4916-be6b-72b5fe74e0e3",
  "sourceToolAssistantUUID": "c8602057-60c6-4eb5-aa60-4844ce427254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-18T17:14:27.578Z_

I now have a thorough understanding of the full paper. Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fffe08f8-e3fd-4916-be6b-72b5fe74e0e3",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQkeqEELcU1cGA7Gi75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc813cf1-4cf5-4efe-bdfa-48c2f8557d6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dq7AMMweTrJjQEM22jsqc9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 85060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1139,
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

_source line 71 · 2026-05-18T17:14:28.967Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TUmQTEpnuWve4L7bddbsZ5`</summary>

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
  "parentUuid": "fc813cf1-4cf5-4efe-bdfa-48c2f8557d6d",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQkeqEELcU1cGA7Gi75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4db504c-1d2d-405b-838e-bf5596dd7e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dq7AMMweTrJjQEM22jsqc9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 85060,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1139
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 85060,
          "cache_creation_input_tokens": 1139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1139,
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

_source line 72 · 2026-05-18T17:14:28.969Z_

<details><summary>↩ Tool result · `toolu_01TUmQTEpnuWve4L7bddbsZ5`</summary>

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
  "parentUuid": "c4db504c-1d2d-405b-838e-bf5596dd7e88",
  "isSidechain": true,
  "promptId": "16620f3f-acf4-4d2d-b16f-7a1caf2fd598",
  "agentId": "a43169a44fe76dba5",
  "type": "user",
  "uuid": "22b0cdc8-e3fa-4ae7-a2c7-77e03eb15ce0",
  "sourceToolAssistantUUID": "c4db504c-1d2d-405b-838e-bf5596dd7e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-18T17:15:53.123Z_



## R2 Review: Novelty and Related Work

### Summary

This paper presents OntoCoDec, a framework that compiles IE ontology schemas into two composable decoding-time constraint layers: a grammar layer (CFG via XGrammar) for structural/vocabulary validity, and a semantic layer (stateful entity registry + dynamic logit masking) for cross-field domain/range type constraints. The paper includes a violation landscape study, ablation experiments on SciERC, DocRED, and WikiEvents across three model families, and analysis of the enabling dependency between layers. DR violations are reduced by 42-99% with no significant F1 cost.

### Strengths

1. **Well-motivated problem with clear formalization.** The paper precisely defines the gap between grammar-constrained decoding (context-free) and the context-sensitive constraints required for IE ontology compliance. The constraint tightness metric, the formal ontology definition, and the violation taxonomy are cleanly presented and make the problem concrete. The distinction between local, prefix-decidable, and non-local constraints (the decidability taxonomy) is a useful conceptual lens, even if it is relatively straightforward.

2. **Thorough ablation design that isolates each layer's contribution.** The five-way ablation (unconstrained, grammar-only, semantic-only, full S1, full S2) is well-designed and directly supports the enabling dependency claim. The grammar-only row on DocRED revealing latent violations (DR rising from 18.46% to 26.17%) is a genuinely interesting finding that emerges naturally from the ablation structure.

3. **Honest treatment of limitations.** The paper does not hide the CF trade-off (up to 12% in zero-shot), the Mistral boundary condition, or the residual DR on DocRED. The CF-DR trade-off ablation in the appendix (Table showing that eliminating CF re-routes violations to DR) is admirably transparent. The dual-factor analysis explicitly notes the small sample size (n=4) and refrains from overclaiming statistical robustness.

4. **Comprehensive experimental coverage for an engineering contribution.** Three models, three datasets (two tasks), four constraint configurations, composability with LoRA, beam search, sampling, prompt sensitivity, document length analysis, and runtime profiling. The paper leaves few obvious experimental gaps within its stated scope.

5. **Cross-task generalization to EE is compelling.** Applying the same framework to WikiEvents with zero architectural modification, eliminating EV and RoV violations entirely, and demonstrating that post-hoc filtering is catastrophically impractical for EE (99.6% discard) strengthens the paper's case for generality.

6. **The related work coverage is notably comprehensive.** The paper cites and positions itself against a wide range of relevant work, including the closest mechanistic analogs in code generation (PICARD, Synchromesh, MGD, type-constrained codegen from PLDI 2025), vocabulary-constrained IE (Roth & Yih 2004, GENRE, GenIE, AdaKGC, GCD, NeuroLogic), training-based IE (UIE, GoLLIE, KnowCoder, CodeIE, ADELIE), post-hoc validation (ODKE+, SPIRES, OntoLogX), and constrained decoding quality concerns (CRANE, Let Me Speak Freely, Hidden Cost, Format Tax). The appendix related work is thorough.

### Weaknesses

1. **The core novelty is incremental relative to type-constrained code generation.** The paper itself acknowledges (Section 3, Appendix B) that the "type system to automaton to logits mask" pipeline exists in code generation (PLDI 2025, Synchromesh, MGD). The claimed distinction, that IE requires a dynamic entity registry built during generation rather than static type declarations, is valid but represents an engineering adaptation of an established paradigm, not a conceptual breakthrough. The semantic layer is essentially a stateful logits processor that maintains a lookup table and performs conditional masking. This is useful but not deeply novel. The paper would benefit from more explicitly framing the contribution as "migrating and adapting an established technique to a new domain with specific challenges" rather than implying greater novelty through the "first to automatically compile IE ontology axioms" framing.

2. **"Universal" and "task-agnostic" claims are overclaimed given the experimental scope.** The title says "Universal Ontology-Constrained Structured Generation" (note: the main.tex title actually says "Type-Constrained Information Extraction via Compiled Ontology Constraints," which is more honest). Only two IE tasks (RE, EE) are tested, both with relatively simple type constraint structures (flat domain/range sets). The paper does not test: (i) nested/hierarchical entity types (e.g., fine-grained entity typing with hundreds of types), (ii) ontologies with subtype hierarchies, (iii) n-ary relations, (iv) tasks beyond IE (e.g., schema-guided dialogue, structured summarization), or (v) ontologies at true web scale (Wikidata has 10K+ property types). The Limitations section acknowledges that scalability to "hundreds of entity types" is unverified. Two tasks do not establish universality.

3. **The violation landscape study, while useful, is not a standalone contribution at the level claimed.** The finding that "violation rates are driven by constraint tightness rather than ontology size" is demonstrated across exactly two ontologies (7 vs. 96 relations) with one primary model. The dual-factor analysis relies on four data points with R-squared=0.886 but p=0.058. This is a reasonable observation, not a robust empirical law. Claiming it as a first-listed contribution oversells it. It would be more appropriately framed as motivating analysis.

4. **The enabling dependency, while empirically validated, is architecturally obvious.** If the semantic layer needs to look up domain/range rules by relation name, and the relation name might be out-of-vocabulary without grammar enforcement, then of course the semantic layer depends on the grammar layer. The quantitative demonstration (semantic-only: 24% DR reduction vs. full: 94%) is useful empirical evidence, but the architectural insight itself follows directly from the design. Presenting this as a key finding overstates its conceptual depth.

5. **Missing positioning against IterGen (Ugare et al., ICLR 2025).** The paper cites IterGen in its bibliography but never discusses it in the related work text. IterGen introduces iterative semantic-aware structured generation with backtracking for LLMs, which is directly relevant: it is a stateful constrained decoding approach that goes beyond CFG constraints. The paper should explain how OntoCoDec differs from IterGen's approach, particularly regarding whether IterGen's backtracking mechanism could address the CF trade-off that OntoCoDec cannot resolve within single-pass decoding.

6. **The CF trade-off undermines the "guarantee" framing.** The paper repeatedly uses language like "formal guarantees" and "type-safety guarantees," but the system actually introduces up to 12% CF violations in zero-shot and up to 21% in EE. A system that eliminates one violation type while introducing another at comparable rates does not provide guarantees in the strong sense implied. The abstract says "composable token-level decoding constraints that provide formal guarantees," but the guarantee is partial: structural validity and per-triple type validity are guaranteed, but cross-triple consistency is not. This should be stated more carefully.

### Questions for Authors

1. How does OntoCoDec handle ontologies with subtype hierarchies (e.g., Person is-a Agent, Organization is-a Agent)? The current formulation assumes flat type sets. If a relation permits Agent as domain, should Person and Organization both be allowed? This is common in real-world ontologies (KAIROS, ACE, BioLink) and the paper does not address it.

2. The continuation masking approach builds a prefix map at compile time for multi-token type names. What is the compile-time and runtime complexity as the number of entity types grows? The paper notes this is unverified beyond 27 types. Have you estimated the scaling behavior analytically?

3. The paper shows beam search resolves both residual DR and CF for calibrated models. Why not make beam search the primary recommendation rather than greedy S1? The paper seems to bury what appears to be the most effective configuration (LoRA + beam + S1 achieving zero violations) in the appendix.

4. Could you clarify why Mistral-7B shows such dramatically different behavior (56.94% DR unconstrained on SciERC vs. 13-15% for the other two models)? Is this a prompt formatting issue, a fundamental calibration problem, or something else? The paper attributes it to "poor zero-shot calibration" but this deserves more analysis given that Mistral substantially changes the narrative about OntoCoDec's effectiveness.

5. The paper tests composability with LoRA fine-tuning only. Have you considered or tested composability with other training-time constraint approaches like GoLLIE's code-based schema encoding? This would strengthen the "orthogonal composability" claim.

### Minor Issues

- The title in main.tex ("Type-Constrained Information Extraction via Compiled Ontology Constraints") differs from the title in the review prompt ("OntoCoDec: Universal Ontology-Constrained Structured Generation for Information Extraction"). The former is more accurate and should be preferred.
- The abstract is 234 words but is dense with numbers. Consider reducing the quantitative detail in the abstract and focusing on the narrative arc per the writing norms.
- The 70B cross-scale paragraph in section5_runtime.tex is commented out with placeholders. If this data is not ready, the cross-scale claim in Contribution 4 of the introduction should be removed or weakened.
- Section 7 (Discussion and Conclusion) is only three sentences. This is too compressed even for a space-constrained submission. A brief discussion of implications and future directions would strengthen the paper.
- The paper mentions "WikiEvents: 56 event types, 80 roles" but the violation rates are extremely high (EV+RoV > 85% unconstrained). This suggests the zero-shot models fundamentally cannot do this task, which somewhat weakens the generalization claim since OntoCoDec is mainly fixing format rather than demonstrating semantic constraint enforcement.
- Table 3 (cross-model) could benefit from showing absolute triple counts alongside violation percentages to give readers a sense of scale.
- The fuzzy matching protocol (Appendix B) with 80% token overlap and edit distance <= 2 seems generous. How sensitive are the Mistral results to this threshold?

### Preliminary Score: 4/6
### Confidence: 4/5
### Justification

The paper addresses a real and well-defined problem, provides thorough experiments, and delivers a working system with clear practical value. The related work coverage is strong and the positioning is generally fair. However, the core technical novelty is limited: the two-layer architecture is a natural and somewhat predictable extension of existing constrained decoding techniques to IE, adapting ideas already demonstrated in code generation. The enabling dependency is architecturally obvious despite being empirically useful. The "universal" claim is not supported by two tasks, and the CF trade-off partially undermines the guarantee framing. This is a solid engineering contribution with useful empirical insights, placing it at the boundary between a Findings-level and a main-conference paper. A score of 4 (Weak Accept / Conference-level) reflects that the execution quality and experimental thoroughness compensate for the limited conceptual novelty, but the paper would need to temper its novelty claims and more honestly frame the contribution as an engineering advance to fully earn main-conference acceptance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22b0cdc8-e3fa-4ae7-a2c7-77e03eb15ce0",
  "isSidechain": true,
  "agentId": "a43169a44fe76dba5",
  "requestId": "req_011CbAQkyMTgDx6dTB1575WN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdaf138b-b33b-4672-a6c2-a0b9ac48ce4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "0eddf8e3-65e4-4850-9e66-a5c0b106b0fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsQGtkzWupDSVfr9uw7Tyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 86199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 686,
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
