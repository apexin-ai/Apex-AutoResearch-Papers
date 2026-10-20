# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **Methods and Experiments**. ## Target Venue Cal

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 1
- **Tool calls:** 33
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-abaa6e03a45e8148b.jsonl`
- **Structured JSON:** [`0979feaf229a3d1fbc45.json`](../../sessions/09/0979feaf229a3d1fbc45.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

77 recorded events

### User

_source line 1 · 2026-05-22T06:25:30.402Z_

You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **Methods and Experiments**. 

## Target Venue Calibration
ARR Overall Assessment scale (1-5, half-point):
- 5 = Consider for Award (top 2.5%)
- 4 = Conference accept
- 3 = Findings accept
- 2 = Resubmit next cycle
- 1 = Do not resubmit

ACL/EMNLP Main acceptance rate ~21%. Be calibrated accordingly.

## Paper Summary

**Title**: OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints

The paper addresses ontology constraint violations in LLM-based structured IE (relation extraction and event extraction). LLMs generating structured output (JSON) systematically violate ontology type constraints—e.g., producing entity types that don't match a relation's domain/range specification. The authors propose OntoCoDec, a two-layer constrained decoding framework:

1. **Grammar layer**: Compiles ontology type vocabulary into a CFG via XGrammar, constraining every generated type token to be ontology-valid.
2. **Semantic layer**: Maintains a stateful entity registry during generation, dynamically masking logits to enforce context-sensitive domain/range (RE) or role/argument-type (EE) constraints.

The two layers compose via bitwise AND of token masks, with graceful degradation: when the intersection is empty (high constraint tightness), the system falls back to grammar-only control.

**Key contributions**:
1. Systematic violation landscape study quantifying ontology constraint violations across models, datasets, and constraint types
2. Composable constraint compilation framework (grammar + semantic layers)
3. Extensive validation: 2 IE tasks × 3 datasets × 4 models × 2 training regimes

## Paper Content Details

### Section 3: Violation Landscape
- 3 models (Qwen3-8B, Llama-3.1-8B, Mistral-7B) on SciERC (7 relations, 6 entity types) and DocRED (96 relations, 6 entity types)
- Per-triple DR rates: 13.3% (Llama SciERC) to 57.4% (Mistral DocRED)
- Violations concentrate on relations with tight constraints (Feature-of: 33.5%, Compare: 42.4%)
- Constraint tightness τ̄ (ratio of valid type pairs to all possible pairs) explains variation better than ontology size
- Prompt-level intervention reduces DR by 32-62% but can't eliminate; for some relations (Evaluate-for), prompt *increases* violations from 24.1% to 29.9%

### Section 4: OntoCoDec Framework
- Grammar compiler: ontology O → EBNF grammar G with type-vocabulary constraints
- For RE: entity_type ::= e1 | e2 | ... | e|E|, relation_name ::= r1 | ... | r|R|
- For EE: additionally constrains event types and argument roles per event type (context-sensitive → needs semantic layer)
- Semantic layer: stateful entity registry R_t, mask function M_semantic(s_t, R_t) = 1[token ∈ valid_types(r, position)] if in type field, else 1^|V|
- Composition: M_final(t) = M_grammar(s_t) ∧ M_semantic(s_t, R_t)
- Fallback when intersection empty: M_fallback(t) = M_grammar(s_t)
- S1 (single-pass) strategy chosen over S2 (two-pass); ablation showed no significant difference
- Beam search (k=4) for partial CF mitigation

### Section 5: Experiments

**Table 1 (RE Zero-Shot)**:
- Qwen SciERC: DR 15.37→0.93, RV 1.39→0, ET 0.40→0, CF 0.08→9.90, R-F1 8.23→8.36, E-F1 31.01→30.98
- Qwen DocRED: DR 18.46→10.21, RV 29.66→0.03, ET 2.48→0, CF 0.10→2.57, R-F1 7.74→8.23, E-F1 58.15→59.37
- Llama SciERC: DR 13.34→0.08, RV 0.55→0, ET 0→0, CF 0.24→6.56, R-F1 2.68→2.54, E-F1 23.56→23.49
- Llama DocRED: DR 26.07→2.55, RV 16.03→0, ET 0.13→0, CF 0.17→12.02, R-F1 5.98→6.27, E-F1 55.65→55.01
- Mistral SciERC: DR 56.94→13.40, RV 0→0, ET 1.50→0, CF 56.87→1.27, R-F1 3.66→3.67, E-F1 27.28→27.46
- Mistral DocRED: DR 57.42→33.20, RV 42.35→0, ET 7.58→0, CF 24.78→0.19, R-F1 4.34→5.52, E-F1 48.51→50.59
- Llama 70B SciERC: DR 6.50→0, RV 0.60→0, R-F1 11.22→11.24
- Llama 70B DocRED: DR 15.00→0, RV 7.80→0, R-F1 13.03→13.07

**Table 2 (LoRA Fine-Tuned + Constrained)**:
- Qwen 8B SciERC: DR 1.95→0, R-F1 43.86→43.77 (Δ=-0.09)
- Llama 8B SciERC: DR 1.11→0.09, R-F1 45.45→45.47 (Δ=+0.02)
- Llama 70B SciERC: DR 0.80→0.05, R-F1 48.20→48.30 (Δ=+0.10)
- Similar patterns on DocRED

**Table 3 (WikiEvents EE Zero-Shot)**:
- All 3 models: EV→0%, RoV→0% under S1
- Entity F1 jumps from 0% to 11.7-17.6% (format compliance restoration)
- Trigger F1 improves +1.5 to +1.8pp
- AC residual: 1.3-3.8%
- Grammar-only ablation: EV→0 but RoV persists (64-77%), proving semantic layer necessity

**Table 4 (Grammar-Only Ablation, all 3 models)**:
- Confirms grammar necessary but insufficient for EE
- AC surfacing pattern (0→9.5-13.8%) consistent with RE latent violation surfacing

**Table 5 (Post-hoc Filtering)**:
- RE: 16.8-73.7% discard
- EE: 99.6-100% discard → completely non-viable

**Table 6 (EE FT Composability)**:
- Qwen FT: RoV 38.3→0, AC 2.7→0, Arg-F1 7.9→8.2
- Llama FT: RoV 8.8→0, AC 3.5→0.8, Arg-F1 10.0→8.9

**Table 7 (Latency)**:
- 10-18% overhead across all configurations

**Section 5.7 Error Analysis**:
- AC residuals: 6/8 from semantic confusion (SideOfConflict vs SentencedPerson), 2 from BPE tokenizer collisions
- CF root causes: 7/10 from entity type ambiguity, 3 from event structural complexity
- 5 "constraint save" cases identified

**Limitations**:
- CF consistency (1.3-21.1%), inherent to per-relation/per-event enforcement
- Constrained-format sensitivity: parse rate drops 4-8pp on some models
- Ontology coverage: only explicit type constraints tested

## Experiment Design Context (from review_context.yaml)
The planned experiments include 45 configurations across 4 models, 3 datasets, 2 tasks, 2 scales, 2 training regimes. Key experiments in the plan that ARE covered in the paper:
- RE ZS (all models × 2 datasets) ✓
- 70B scale generalization (ZS) ✓
- LoRA FT + constrained (including 70B) ✓
- WikiEvents EE ZS (all 3 models) ✓
- Grammar-only ablation (all 3 models) ✓
- Post-hoc filtering comparison ✓
- EE FT composability ✓
- Latency overhead ✓
- Error analysis ✓

Experiments mentioned in plan but NOT clearly in paper:
- Bootstrap CI for EE metrics (mentioned briefly as "p < 0.001" and "p ≤ 0.05" inline but no CI table)
- Prompt sensitivity ablation (briefly mentioned in §3 as motivation but no dedicated table)
- Beam sweep details (only beam-4 latency in Table 7)
- Seed variance (not mentioned)

## Your Task

Provide a detailed review focusing on:

1. **Soundness** (1-5): Is the methodology technically correct? Are the experimental claims supported by evidence?
2. **Reproducibility** (1-5): Could someone reproduce this work from the paper alone?
3. **Strengths** (bulleted)
4. **Weaknesses** (bulleted, with severity: major/minor)
5. **Questions for authors**
6. **Missing experiments or analysis**
7. **Overall Assessment** (1-5, half-point scale per ARR)

Be rigorous but fair. Calibrate to EMNLP acceptance rate (~21% main, ~40% including Findings). Think about what a top-venue reviewer would flag.

Key things to scrutinize:
- Residual DR on Qwen DocRED (10.21%) and Mistral (13.40% SciERC, 33.20% DocRED) — is the method effective enough?
- CF trade-off: violations increase significantly (0.08%→9.90% on Qwen SciERC) — is this adequately addressed?
- The "violation elimination" framing when DR is not actually 0 for many configurations
- Statistical significance: only bootstrap CIs for R-F1; violation rate changes not tested
- The 70B results use AWQ-INT4 quantization — does this confound the scale comparison?
- Parse rate drops under constrained decoding
- Lack of comparison with existing constrained generation methods (CRANE, TypeDecoding, SynCode) in experiments

Format your response as a structured review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "eb58f808-28a0-4c88-b212-c34d0ad62767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T06:25:30.408Z_

```json
{
  "parentUuid": "eb58f808-28a0-4c88-b212-c34d0ad62767",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
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
  "uuid": "e0e7f8a8-c53e-4536-9139-5a018ed81c97",
  "timestamp": "2026-05-22T06:25:30.408Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-22T06:25:33.160Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0e7f8a8-c53e-4536-9139-5a018ed81c97",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WJinPrSymBjvJtLDW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fc10760-afeb-4ec4-b811-9c482976a655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Myr6MJZirHNTdRDt4hcSLs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17656,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17656,
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

_source line 4 · 2026-05-22T06:25:33.549Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JxAzJjaF93ja2M14ac9kfX`</summary>

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
  "parentUuid": "1fc10760-afeb-4ec4-b811-9c482976a655",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WJinPrSymBjvJtLDW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db2f50be-13ef-4b3d-80cc-a48b2c1d7813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Myr6MJZirHNTdRDt4hcSLs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17656,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17656
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17656,
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

_source line 5 · 2026-05-22T06:25:33.554Z_

<details><summary>↩ Tool result · `toolu_01JxAzJjaF93ja2M14ac9kfX`</summary>

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
  "parentUuid": "db2f50be-13ef-4b3d-80cc-a48b2c1d7813",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "c53e2b03-8363-437f-b517-805eae594c9a",
  "sourceToolAssistantUUID": "db2f50be-13ef-4b3d-80cc-a48b2c1d7813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T06:25:35.994Z_



Let me read the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c53e2b03-8363-437f-b517-805eae594c9a",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WYRYShtivDytNSLFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3868fa1b-614a-4324-a0a6-24f3342fedc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6UK8eMPgoR2BuhvqWum2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 17656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-22T06:25:37.490Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SFfv6AaVtaAqBTHfV95mEM`</summary>

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
  "parentUuid": "3868fa1b-614a-4324-a0a6-24f3342fedc2",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WYRYShtivDytNSLFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba818efc-ef38-4598-bc6d-9179ccf8a5fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6UK8eMPgoR2BuhvqWum2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 17656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 8 · 2026-05-22T06:25:37.505Z_

<details><summary>↩ Tool result · `toolu_01SFfv6AaVtaAqBTHfV95mEM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval_70b_lora_docred_200_s1_constrained | 70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve DR→0% while maintaining R-F1 comparable to unconstrained, confirming scale-independent constraint composability on DocRED at 70B scale | — | — | — |\\n| eval_70b_lora_scierc_s1_constrained | 70B LoRA SciERC with Full S1 constrained decoding will achieve DR→0% while maintaining R-F1 comparable to unconstrained (44.73), confirming scale-independent constraint effectiveness at 70B with fine-tuning | — | — | — |\\n| eval_70b_lora_docred_200_unconstrained | 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale | — | — | — |\\n\\n## 待处理\\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\\n- p1_llama_ee_ft（准备中）\\n\\n## 近期结论\\n- **eval_70b_lora_scierc_unconstrained** (success): 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models (Qwen FT R-F1=47.15, Llama FT R-F1=46.13) on SciERC unconstrained extraction due to larger model capacity ← 基于 r16_70b_lora_scierc\\n- **r16_70b_docred_zs_s1** (success): Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets\\n- **d066_sweep_llama_beam8_unc** (success): d066 DocRED beam sweep sub-task: Llama beam8 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment. ← 基于 d066_beam_sweep\\n\\n## 趋势\\n成功 111 / 负向 7 / 失败 11 / 共 133\\nCF_pct: 0 ↓（近 3 次 success）\\nDR_pct: 1.5 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-16980: 无 GPU 信息\\nwestd-21461: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\\n- w1_cf_fallback_docred: 已被终止 — unknown\\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown\\n- p8b_docred_latency: 训练失败 — unknown\\n- p1_ee_ft_composability: 训练失败 — unknown\\n- p1_ee_ft_composability_r2: 训练失败 — unknown\\n- p1_ee_ft_composability_r3: 训练失败 — unknown\\n- p1_ee_ft_composability_r4: 训练失败 — unknown\\n- p1_ee_ft_llama: 训练失败 — unknown\\n- d064_docred_full_beam: 训练失败 — unknown\\n- d066_docred_beam_sweep: 训练失败 — unknown\\n- d065_qwen_greedy_4096: 训练失败 — unknown\\n- d066_sweep_llama_scierc_beam1_unc: 训练失败 — unknown\\n\", \"total_chars\": 2778, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba818efc-ef38-4598-bc6d-9179ccf8a5fb",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "cc555ebc-06ab-43d1-836e-5b8273c0710b",
  "sourceToolAssistantUUID": "ba818efc-ef38-4598-bc6d-9179ccf8a5fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T06:25:37.925Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0141xVraeSDNH9w7pe9UXExC`</summary>

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
  "parentUuid": "cc555ebc-06ab-43d1-836e-5b8273c0710b",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WYRYShtivDytNSLFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abc627c4-7448-40ef-8963-2de1fa43aa30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6UK8eMPgoR2BuhvqWum2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 17656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 10 · 2026-05-22T06:25:37.935Z_

<details><summary>↩ Tool result · `toolu_0141xVraeSDNH9w7pe9UXExC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ROADMAP.md\", \"content\": \"# schema_semantic_constrained_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-21 03:37 UTC | 更新原因: D081 combined plan: D079 trie + D080 GoLLIE/triple/deployment + D081 user 5-point evaluation\\n\\n## 核心方向\\nOntoCoDec: 两层约束解码（grammar + semantic）将 IE schema 翻译为 token-level constraints，消除 LLM-based IE 的 type violations。**目标: EMNLP 2026 ARR May 25 提交**。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: D079+D080+D081 综合执行中 — **提交前最后一轮**\\n\\n**审稿轨迹**: R12 (3.5) → R13 (3.0) → R14 (3.5) → R15 (3.0) → R16 (3.0)\\n振荡模式：3.0-3.5 交替，结构性天花板约 3.5\\n\\n**并行工作流**:\\n- Trie baseline (P0): westd-21461 cuda:1 — SciERC 4 configs GCD-equivalent 对比\\n- GoLLIE head-to-head (P0): westd-16980 cuda:1 — 同模型 code-style prompt 对比\\n- Beam 998-doc (P0): 两台 cuda:0 — full DocRED CF 缓解证据\\n- Triple validity (P1): valid-triple precision + error propagation 分析\\n- Paper Agent: deployment-grade Abstract + DocRED data leakage 澄清\\n- R16 text modifications (MF2/MF3/W1-W6/M1-M7): 已完成\\n\\n**R15→R16 已确认的改善（保持）**:\\n- ✅ §5 显式 BoostCD/GCD 对比段落\\n- ✅ \\\"formal guarantees\\\" → \\\"enforcement mechanisms\\\"\\n- ✅ κ̄ 移出 contributions enumerate\\n- ✅ ≤ 8 页（Regression Checklist 10/10 PASS）\\n- ✅ Fallback causal tracing (100% DR from fallback)\\n- ✅ 跨语言限制 in Limitations\\n\\n## 近期任务\\n- [ ] P0: 确认 trie baseline Worker 状态 + 结果提取\\n- [ ] P0: GoLLIE SciERC head-to-head 实验\\n- [ ] P0: Beam 998-doc 结果提取 (Llama + Qwen)\\n- [ ] P1: Triple validity — valid-triple precision + error propagation\\n- [ ] P1: Paper Agent deployment-grade + DocRED leakage 澄清\\n- [ ] P2: WikiEvents 官方 test split 大小核实\\n- [ ] P2: 70B LoRA SciERC（条件启动：trie 完成后）\\n- [ ] Phase 2: 全部实验数据集成到论文\\n- [ ] Regression Checklist + R17 审稿\\n- [ ] May 25 EMNLP ARR 提交\\n\\n## GPU 预算\\nwestd-16980 cuda:0,1 + westd-21461 cuda:0,1 (4× RTX PRO 6000 96GB)\\n当前占用：beam 998-doc ×2 GPU + trie baseline 1 GPU + GoLLIE 1 GPU = 4/4 满载\\n\\n## 时间线\\n- **May 21 (now)**: D079-D081 全部 dispatch — 4 GPU 满载并行\\n- **May 22 AM**: Trie + beam + GoLLIE 结果到齐 → 数据集成\\n- **May 22 PM**: R17 审稿（目标 3.5）\\n- **May 23-24**: 最终修复 + 提交前 24h 冻结\\n- **May 25**: EMNLP 2026 ARR 提交\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D084 | 2026-05-22 | D084: 撤回 D083，恢复使用 70B DocRED ZS 数据（DR 14.98%→0%,  | r16_70b_docred_zs_s1 |\\n| D083 | 2026-05-22 | D083: 放弃 70B DocRED ZS 重跑，从论文移除该数据点。70B feasibilit | r16_70b_docred_zs_s1, r16_70b_lora_scierc, r16_70b_lora_docred |\\n| D082 | 2026-05-22 | D082: 70B LoRA DocRED 推理改用 200-doc 子集 + DocRED ZS  | r16_70b_lora_docred, r16_70b_docred_zs_s1 |\\n| D081 | 2026-05-21 | D081: 评估用户 5 项补充建议——downstream KG 扩展 Task E、beam=C | — |\\n| D080 | 2026-05-21 | D080: 采纳用户 3 项审稿建议——GoLLIE head-to-head + 下游 tripl | — |\\n| D079 | 2026-05-21 | D079: R16 Action Matrix——MF1 trie-based GCD-equiva | — |\\n| D078 | 2026-05-21 | D078: R15 Action Matrix 定稿——MF1 §5 显式对比, MF2 guara | — |\\n| D077 | 2026-05-20 | R14 Action Matrix 定稿——Grammar-only ablation refram | — |\\n| D076 | 2026-05-20 | R13 Action Matrix 定稿——全文 Claim Calibration Pass +  | — |\\n| D075 | 2026-05-20 | D075: SF2 BoostCD 不做实验对比——任务不匹配（Closed IE on Wiki- | — |\\n\\n\", \"total_chars\": 2946, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abc627c4-7448-40ef-8963-2de1fa43aa30",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "dc394e68-f7a6-4c9c-b8c9-ff78b4e8bf23",
  "sourceToolAssistantUUID": "abc627c4-7448-40ef-8963-2de1fa43aa30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T06:25:38.564Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HPaL6D83XHQHf3nBeMHioY`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc394e68-f7a6-4c9c-b8c9-ff78b4e8bf23",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WYRYShtivDytNSLFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7574710d-26da-4145-8ab6-4073f48c67f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6UK8eMPgoR2BuhvqWum2D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 17656,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 17656,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
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

_source line 12 · 2026-05-22T06:25:38.580Z_

<details><summary>↩ Tool result · `toolu_01HPaL6D83XHQHf3nBeMHioY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"content\": \"# Memory — schema_semantic_constrained_ie\\n\\n## 70B LoRA 推理状态 (2026-05-22 05:25 UTC)\\n\\n### westd-16980\\n- cuda:0: SciERC 70B LoRA S1 constrained — 34/551 (6.2%), ~9s/sample, ETA ~14:40 UTC\\n  - SciERC unconstrained 已完成 (551 lines, `/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl`)\\n- cuda:1: DocRED 70B LoRA unconstrained — 117/200 (58.5%), ~87s/sample, ETA ~15:22 UTC\\n  - 完成后还需跑 DocRED S1 constrained (~200 samples, 可能需 3-5 小时)\\n\\n### westd-21461\\n- cuda:0,1: 完全空闲\\n- 有 70B AWQ INT4 模型，但**无 70B LoRA checkpoint**（只有 8B merged checkpoints）\\n- 70B LoRA checkpoints 在 westd-16980: `/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146`, `/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663`\\n- 环境就绪: torch 2.8, transformers 5.8.1, peft 0.19.1, xgrammar 0.1.33\\n- 磁盘: 75G 可用 (autodl-tmp)\\n\\n### 关键路径分析\\n- Paper L19 XX.XX 占位符需要 4 组数据: SciERC unc/S1 + DocRED unc/S1\\n- SciERC pair: unc ✅ + S1 running (~78 min) → 最快 ~14:40 UTC 可用\\n- DocRED pair: unc running (~120 min) + S1 还没开始 → 如果串行，S1 最快 ~20:00 UTC\\n- 如果把 70B LoRA DocRED checkpoint 拷到 westd-21461 并行跑 S1 → 可提前 ~5 小时\\n\\n## DocRED 评估注意事项\\n- violation_checker.py 对 DocRED 的 R-F1 计算有 schema mismatch（模型输出自然语言 relation names，gold 用 P-codes）\\n- 正确评估用 eval_d064.py 或需要在 violation_checker.py 加 name→P-code 映射\\n- r16_70b_docred_zs_s1 已用 eval_d064.py 修正: R-F1=13.05\\n\\n## PEFT AWQ 兼容性\\n- 70B AWQ INT4 + LoRA 需要 monkey-patch: `peft.import_utils.is_gptqmodel_available = lambda: False`\\n- 否则 PEFT 误检测 GPTQModel 导致加载失败\\n\\n## Monitor 脚本 mode 参数\\n- `--mode full_s1` 是正确的（不是 `--mode s1`）\\n- westd-16980 上的 monitor 脚本因为用了错误 mode 导致自动启动失败，已由 Worker 手动修正\\n\", \"total_chars\": 1602, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7574710d-26da-4145-8ab6-4073f48c67f6",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "e54bf464-c451-45c9-bf69-afe04de8bd8b",
  "sourceToolAssistantUUID": "7574710d-26da-4145-8ab6-4073f48c67f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T06:25:41.683Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RZnANBm7NLeYmqigrwBBe7`</summary>

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
  "parentUuid": "e54bf464-c451-45c9-bf69-afe04de8bd8b",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WueyqfzDFXUHPrLpu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c6b8b5a-ef59-4d79-a2ec-59546bdb9dcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Etr7ajUN3FjSDFLhQHoLg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4732,
      "cache_read_input_tokens": 19104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4732,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 14 · 2026-05-22T06:25:41.706Z_

<details><summary>↩ Tool result · `toolu_01RZnANBm7NLeYmqigrwBBe7`</summary>

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
  "parentUuid": "3c6b8b5a-ef59-4d79-a2ec-59546bdb9dcc",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "ea247bf6-7bc7-4c04-a1b6-abf3478a43ed",
  "sourceToolAssistantUUID": "3c6b8b5a-ef59-4d79-a2ec-59546bdb9dcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T06:25:42.120Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015UW9xCuBFoN2ZMKeZoAR8v`</summary>

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
  "parentUuid": "ea247bf6-7bc7-4c04-a1b6-abf3478a43ed",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WueyqfzDFXUHPrLpu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed9753bb-ec37-4bde-97a4-e3087c2bce0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Etr7ajUN3FjSDFLhQHoLg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4732,
      "cache_read_input_tokens": 19104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4732,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 16 · 2026-05-22T06:25:42.131Z_

<details><summary>↩ Tool result · `toolu_015UW9xCuBFoN2ZMKeZoAR8v`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md\", \"content\": \"# OntoCoDec — Paper Framing\\n\\n## Target Venue\\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\\n\\n## Title\\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\\n(D015: \\\"Near-Complete\\\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\\n\\n**D040 Story 升级方向**: 从 \\\"IE-specific constrained decoding\\\" → \\\"universal ontology-constrained structured generation framework\\\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\\n\\n## Core Insight\\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\\n\\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\\n\\n## Core Claims\\n\\n### Claim 1 (Empirical): Violation Landscape\\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\\n\\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\\n\\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\\n\\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\\n\\n### Claim 2 (Empirical): Prompt Insufficiency\\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\\n\\n**Narrative**: This is NOT about \\\"5.78% barely above 5%\\\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\\n\\n### Claim 3 (Methodological): Composable Constraint Framework\\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\\n\\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \\\"synergistic\\\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\\n\\nThe two layers compose via bitwise AND of token masks. Recommended framing: \\\"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\\\"\\n\\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\\nWhen $M_{semantic} \\\\cap M_{grammar} = \\\\emptyset$, the system falls back to grammar-only control.\\n\\n**关键量化数据（Reviewer 从日志挖掘）**:\\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\\n- DocRED fallback 频率是 SciERC 的 **5.3×**\\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\\n\\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\\n\\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \\\"Constraint Coverage\\\" 指标（semantic masking 实际生效的 token 比例）。这把 \\\"10.19% DR 残余\\\" 从弱点变成可量化分析的 finding。Frame as \\\"engineering robustness\\\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\\n\\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\\n\\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\\n\\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\\n\\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\\n\\n### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)\\n**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)\\n\\nOntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.\\n\\n**Cross-task framing (Reviewer 评估 confirmed)**:\\n- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 \\\"more complex ontology → more critical constraint enforcement\\\" claim\\n- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。\\n- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints\\n- **\\\"Practical value\\\" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效\\n\\n**WikiEvents specifics** (DARPA KAIROS ontology):\\n- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）\\n- 245 组显式 (event_type, role) → allowed_entity_types 约束\\n- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints\\n- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值\\n- 99.98% 数据满足约束 → 约束定义是真实有效的\\n- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）\\n\\n**数据集选择理由**（MAVEN/RAMS 排除）：\\n- MAVEN (168 types): 无 argument extraction，不适用\\n- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束\\n- RAMS (139 types): 仅 cardinality 约束，无 entity type binding\\n- ACE05 (33 types): LDC 付费，采购周期来不及\\n- **WikiEvents 是唯一同时满足 \\\"免费 + 有显式 role→entity_type 约束\\\" 的数据集**\\n\\n**Violation 分类** (5 类，从 RE 的 4 类扩展):\\n- ET (Entity Type): entity type 不在 ontology 合法类型列表中\\n- EV (Event Vocabulary): event type 不在 ontology 定义中\\n- RoV (Role Vocabulary): argument role 不在该 event type 定义中\\n- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）\\n- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type\\n\\n**Full results (246 docs, v3 final — collision fix + exact-match fix)**:\\n\\n| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |\\n|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|\\n| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |\\n| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |\\n| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |\\n| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |\\n| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |\\n| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |\\n| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |\\n\\n**Grammar-only ablation (Mistral v3, all 3 models)**:\\n- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context\\n- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)\\n- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient\\n\\n**Post-hoc filtering comparison (devastating)**:\\n- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation\\n- Llama: 5,053→3 arguments (99.9% discarded)\\n- Mistral: 6,034→0 arguments (100% discarded)\\n- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)\\n\\n**BPE collision diagnostic (confirmed 2026-05-18)**:\\n- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens\\n- Llama (BPE, ~128K vocab): **0 collision groups** — same\\n- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')\\n- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision\\n\\n**关键 findings**:\\n- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求\\n- EV 显著（10-37%）→ grammar 层直接消除\\n- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions\\n- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP\\n- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing\\n\\n**Story upgrade**: WikiEvents results confirm paper narrative: \\\"universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints\\\". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.\\n\\n**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.\\n\\n**Remaining risk**:\\n- CF 15-21% higher than RE → continues CF tradeoff framing\\n- 70B experiment timeline tight (need results by May 20 for paper integration)\\n\\n## Anticipated Reviewer Concerns\\n\\n### C1: \\\"5.78% is barely above 5% — threshold is arbitrary\\\"\\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\\n\\n### C2: \\\"Why not just post-hoc filter?\\\"\\n**Response (D013, 实验结果已出)**:\\n\\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\\n\\n**论文 framing（不以 F1 论高低，多维对比）**:\\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\\n4. **Precision trade-off（诚实承认）**: \\\"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\\\"\\n\\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\\n\\n**Reviewer 补充发现（D013 后）**:\\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\\\"prevent vs detect\\\" 核心论据的具体数据。\\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\\n\\n### C3: \\\"Bitwise AND of two masks is not novel\\\"\\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\\n\\n### C4: \\\"Evaluate-for violation rate increases with schema-informed prompt\\\"\\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\\\"Method X evaluates for Task Y\\\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \\\"harder instances\\\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\\n\\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\\n\\n### C5: \\\"Only tested on one model (Qwen3-8B)\\\"\\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\\n\\n**Cross-model claim 指导（Reviewer 专项评估）**:\\n- ✅ 可声明：\\\"OntoCoDec generalizes across model families without code modification\\\"（程序性事实，铁证）\\n- ❌ 不可声明：\\\"consistently achieves the same reduction rate\\\"（仅 2 模型，不足以量化声明）\\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\\n\\n### C6: \\\"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\\\"\\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\\n\\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\\n\\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\\n- Frame as: \\\"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\\\"\\n- 不升级为 core claim，但如实报告。\\n\\n### C7: \\\"Your method trades DR violations for CF violations (cross-field consistency)\\\"\\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\\n\\n**CF 子类型分析（根因已确认）**：\\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\\n\\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\\n\\n**论证层次**：\\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\\n\\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \\\"CF 是 semantic type enforcement 的系统性副作用\\\" 提供干净的消融证据。\\n\\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\\n\\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\\n\\n### C8: \\\"Absolute F1 is too low (~8%) — results are not meaningful\\\"\\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \\\"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\\\"\\n\\n## Paper Structure (Draft — D040 updated)\\n1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)\\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\\n5. Experiments:\\n   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)\\n   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)\\n   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)\\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods\\n7. Conclusion: Framework generality across IE tasks\\n\\n## Claim Calibration (per Reviewer assessment)\\n\\n**Safe to claim (sufficient evidence from Phase 2)**:\\n- \\\"First systematic study of ontology constraint violations in LLM-based IE\\\"\\n- \\\"Violation rate correlates with constraint tightness, not ontology size\\\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\\n- \\\"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\\\" ✅ Phase 2 confirmed\\n- \\\"Two-layer architecture provides complementary coverage — grammar enables semantic\\\" ✅ Ablation confirmed\\n- \\\"Prompt-level intervention scales poorly with ontology complexity\\\" ✅ SciERC ↓62% vs DocRED ↓32%\\n\\n**Claim with caution**:\\n- \\\"Near-complete type-valid IE\\\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \\\"Near-Complete\\\"\\n- \\\"Principled framework applicable to arbitrary IE ontologies\\\" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending\\n- \\\"F1 improvement\\\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\\n- \\\"CF reveals type system ambiguity\\\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\\\"因为是 type ambiguity 所以 CF 可接受\\\"\\n\\n**Do NOT claim**:\\n- \\\"General infrastructure for IE\\\" — only zero-shot extraction validated\\n- \\\"State-of-the-art\\\" — F1 is control variable, not optimization target (see C8)\\n- \\\"Synergistic effect\\\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\\n- \\\"S2 solves CF\\\" or \\\"S2 mitigates Structure Snowballing\\\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\\n- \\\"Pilot50 DR=0%\\\" — small-sample artifact, full S2 has DR=0.97%\\n- \\\"Grammar-first invariant\\\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\\n- \\\"Robust dual-layer composition across schema complexities\\\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\\n\\n## Risk Ranking (ordered by reject probability)\\n\\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\\n3. **Novelty perception** (MEDIUM): \\\"PLDI'25 for code → OntoCoDec for IE\\\" attack line. Must argue IE constraint structure differs fundamentally.\\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\\n\\n## Critical Path to EMNLP Submission (May 25)\\n\\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\\n- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅\\n- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破\\n- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量\\n- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写\\n- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review\\n- **May 20-24**: Review 修改 + 最终提交\\n\\n**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。\\n\\n## Status\\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\\n- Related work: ✅ 42 bib entries, 4 additions merged\\n- Dream 6/6 actions: ✅ All complete\\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\\n- Paper compilation: ✅ 8 pages正文 + appendix\\n- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified\\n- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)\\n- Doc length breakdown: ✅ Complete (appendix written)\\n- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动\\n\", \"total_chars\": 26924, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed9753bb-ec37-4bde-97a4-e3087c2bce0f",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "072aa53e-6861-497f-aaec-f90c30618218",
  "sourceToolAssistantUUID": "ed9753bb-ec37-4bde-97a4-e3087c2bce0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T06:25:42.792Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013VsisyRZPyzqNXwTKiUNpY`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "072aa53e-6861-497f-aaec-f90c30618218",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8WueyqfzDFXUHPrLpu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df2b47fa-c6a4-46fe-b0b2-92ac37a51367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Etr7ajUN3FjSDFLhQHoLg1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4732,
      "cache_read_input_tokens": 19104,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4732
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 19104,
          "cache_creation_input_tokens": 4732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4732,
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

_source line 18 · 2026-05-22T06:25:43.169Z_

<details><summary>↩ Tool result · `toolu_013VsisyRZPyzqNXwTKiUNpY`</summary>

```text
Error: result (60,879 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32/tool-results/mcp-agent-ml-research-read_project_file-1779431143154.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32/tool-results/mcp-agent-ml-research-read_project_file-1779431143154.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df2b47fa-c6a4-46fe-b0b2-92ac37a51367",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "719b8b0e-57fe-4f6f-9194-44110c349464",
  "sourceToolAssistantUUID": "df2b47fa-c6a4-46fe-b0b2-92ac37a51367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-22T06:25:45.933Z_

Let me read the memory file and the main paper tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "719b8b0e-57fe-4f6f-9194-44110c349464",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8XFHSBrCFmMKQjrVCi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5920011a-e240-4256-bd17-1020db81fccf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RL7nB97nmEMRcCeTTJLwQ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12758,
      "cache_read_input_tokens": 23836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12758,
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

_source line 20 · 2026-05-22T06:25:46.807Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EF4xX8RadvfXqpHaYB2Vhe`</summary>

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
  "parentUuid": "5920011a-e240-4256-bd17-1020db81fccf",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8XFHSBrCFmMKQjrVCi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d4f00a9-a42c-47b5-a9e1-44aa08b0298a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RL7nB97nmEMRcCeTTJLwQ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12758,
      "cache_read_input_tokens": 23836,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12758
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 23836,
          "cache_creation_input_tokens": 12758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12758,
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

_source line 21 · 2026-05-22T06:25:46.818Z_

<details><summary>↩ Tool result · `toolu_01EF4xX8RadvfXqpHaYB2Vhe`</summary>

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
  "parentUuid": "1d4f00a9-a42c-47b5-a9e1-44aa08b0298a",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "0bf022c9-3b9a-4c0f-8ea1-d56e3313c0ca",
  "sourceToolAssistantUUID": "1d4f00a9-a42c-47b5-a9e1-44aa08b0298a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T06:25:50.103Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DRgFLjY8ad3Z7eJ1b6RKh8`</summary>

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
  "parentUuid": "0bf022c9-3b9a-4c0f-8ea1-d56e3313c0ca",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8XWvH6sexRQJRHcywp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a2ffe06-68e1-4a04-ba2b-48570e73b0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sJiXF9fTJd41rypDmVdoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 36594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2737,
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

_source line 23 · 2026-05-22T06:25:50.109Z_

<details><summary>↩ Tool result · `toolu_01DRgFLjY8ad3Z7eJ1b6RKh8`</summary>

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
  "parentUuid": "4a2ffe06-68e1-4a04-ba2b-48570e73b0a3",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "47f10b35-a7ab-40b5-9565-758e15c4ec26",
  "sourceToolAssistantUUID": "4a2ffe06-68e1-4a04-ba2b-48570e73b0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T06:25:51.618Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XRr3tkJWPHuuxySTi5ahRJ`</summary>

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
  "parentUuid": "47f10b35-a7ab-40b5-9565-758e15c4ec26",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8XWvH6sexRQJRHcywp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cd11c35-3b2d-4a1b-9c41-2c3a6d51a9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sJiXF9fTJd41rypDmVdoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 36594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2737,
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

_source line 25 · 2026-05-22T06:25:51.624Z_

<details><summary>↩ Tool result · `toolu_01XRr3tkJWPHuuxySTi5ahRJ`</summary>

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
  "parentUuid": "8cd11c35-3b2d-4a1b-9c41-2c3a6d51a9c3",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "8bdfc508-2a87-42d5-8842-b7a8434b2304",
  "sourceToolAssistantUUID": "8cd11c35-3b2d-4a1b-9c41-2c3a6d51a9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T06:25:51.824Z_

<details open><summary>🔧 Tool call — Read · `toolu_011iosirh8NMvP3hTXTJYHNi`</summary>

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
  "parentUuid": "8bdfc508-2a87-42d5-8842-b7a8434b2304",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8XWvH6sexRQJRHcywp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8dd6301-3a5c-4579-b8e2-be62cd8b2b8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sJiXF9fTJd41rypDmVdoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 36594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2737,
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

_source line 27 · 2026-05-22T06:25:51.834Z_

<details><summary>↩ Tool result · `toolu_011iosirh8NMvP3hTXTJYHNi`</summary>

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
  "parentUuid": "a8dd6301-3a5c-4579-b8e2-be62cd8b2b8a",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "0061687a-98e0-49cf-ba0d-936b92514904",
  "sourceToolAssistantUUID": "a8dd6301-3a5c-4579-b8e2-be62cd8b2b8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T06:25:51.976Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MSVAn4dcqLg2Td1tVb8HgS`</summary>

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
  "parentUuid": "0061687a-98e0-49cf-ba0d-936b92514904",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8XWvH6sexRQJRHcywp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc8f1fd7-369d-45d0-9629-5c6fdab198f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sJiXF9fTJd41rypDmVdoy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2737,
      "cache_read_input_tokens": 36594,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2737
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 36594,
          "cache_creation_input_tokens": 2737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2737,
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

_source line 29 · 2026-05-22T06:25:51.982Z_

<details><summary>↩ Tool result · `toolu_01MSVAn4dcqLg2Td1tVb8HgS`</summary>

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
  "parentUuid": "fc8f1fd7-369d-45d0-9629-5c6fdab198f1",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "9d3246e2-e98e-4ffa-886e-faa543fa6c51",
  "sourceToolAssistantUUID": "fc8f1fd7-369d-45d0-9629-5c6fdab198f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T06:25:56.267Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XrwhqFV4w2XhcKFB38sUHp`</summary>

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
  "parentUuid": "9d3246e2-e98e-4ffa-886e-faa543fa6c51",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Xu7WsD6HPQ8HZ6Vs2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "630e650e-e536-4d67-a270-60dcfc7d7fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpjAA2FkEkf4GdrnSqixW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6101,
      "cache_read_input_tokens": 39331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6101,
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

_source line 31 · 2026-05-22T06:25:56.277Z_

<details><summary>↩ Tool result · `toolu_01XrwhqFV4w2XhcKFB38sUHp`</summary>

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
  "parentUuid": "630e650e-e536-4d67-a270-60dcfc7d7fe4",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "ca2499b9-d0ea-4e3c-937b-961db4c23c01",
  "sourceToolAssistantUUID": "630e650e-e536-4d67-a270-60dcfc7d7fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T06:25:57.722Z_

<details open><summary>🔧 Tool call — Read · `toolu_011Vsoap9TSdsgo11MSJompF`</summary>

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
  "parentUuid": "ca2499b9-d0ea-4e3c-937b-961db4c23c01",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Xu7WsD6HPQ8HZ6Vs2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08214c07-9f8b-47a9-8fa4-f214554b4531",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpjAA2FkEkf4GdrnSqixW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6101,
      "cache_read_input_tokens": 39331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6101,
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

_source line 33 · 2026-05-22T06:25:57.726Z_

<details><summary>↩ Tool result · `toolu_011Vsoap9TSdsgo11MSJompF`</summary>

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
  "parentUuid": "08214c07-9f8b-47a9-8fa4-f214554b4531",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "7fcd94ca-c997-431c-8861-22ee612778bb",
  "sourceToolAssistantUUID": "08214c07-9f8b-47a9-8fa4-f214554b4531",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T06:25:57.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qsvt3Cu64PVd4JyFiwmiG5`</summary>

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
  "parentUuid": "7fcd94ca-c997-431c-8861-22ee612778bb",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Xu7WsD6HPQ8HZ6Vs2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10228498-cb1b-4ff9-bcb9-6b0f3ad10cbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpjAA2FkEkf4GdrnSqixW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6101,
      "cache_read_input_tokens": 39331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6101,
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

_source line 35 · 2026-05-22T06:25:57.760Z_

<details><summary>↩ Tool result · `toolu_01Qsvt3Cu64PVd4JyFiwmiG5`</summary>

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
  "parentUuid": "10228498-cb1b-4ff9-bcb9-6b0f3ad10cbb",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "22588304-2b17-4d98-bfbd-2ea975290e18",
  "sourceToolAssistantUUID": "10228498-cb1b-4ff9-bcb9-6b0f3ad10cbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T06:26:03.637Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AJJsf83jxmXkP5UiK2nEGP`</summary>

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
  "parentUuid": "22588304-2b17-4d98-bfbd-2ea975290e18",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8YSLj3p1noq4GQ7sxG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b65c76b-af13-4a0e-a6c6-3d5c1b1e6420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxRoKv8nMCceXHEZbon56r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
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

_source line 37 · 2026-05-22T06:26:03.654Z_

<details><summary>↩ Tool result · `toolu_01AJJsf83jxmXkP5UiK2nEGP`</summary>

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
  "parentUuid": "7b65c76b-af13-4a0e-a6c6-3d5c1b1e6420",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "67952e68-6672-4cdd-bf36-d304c18162a2",
  "sourceToolAssistantUUID": "7b65c76b-af13-4a0e-a6c6-3d5c1b1e6420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T06:26:04.658Z_

<details open><summary>🔧 Tool call — Read · `toolu_014REYruoXfjWa16PLxo8HyH`</summary>

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
  "parentUuid": "67952e68-6672-4cdd-bf36-d304c18162a2",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8YSLj3p1noq4GQ7sxG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55327af8-1f3c-4daa-8e42-45162a97fbb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxRoKv8nMCceXHEZbon56r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
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

_source line 39 · 2026-05-22T06:26:04.663Z_

<details><summary>↩ Tool result · `toolu_014REYruoXfjWa16PLxo8HyH`</summary>

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
  "parentUuid": "55327af8-1f3c-4daa-8e42-45162a97fbb5",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "6b55806f-688e-4538-813b-7f3eb1d34fbb",
  "sourceToolAssistantUUID": "55327af8-1f3c-4daa-8e42-45162a97fbb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T06:26:05.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GyJZSoD7TYshNiYU4NMTsA`</summary>

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
  "parentUuid": "6b55806f-688e-4538-813b-7f3eb1d34fbb",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8YSLj3p1noq4GQ7sxG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4456c28d-9600-47b2-bf04-ef599bd41ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxRoKv8nMCceXHEZbon56r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5524,
      "cache_read_input_tokens": 45432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5524,
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

_source line 41 · 2026-05-22T06:26:05.050Z_

<details><summary>↩ Tool result · `toolu_01GyJZSoD7TYshNiYU4NMTsA`</summary>

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
  "parentUuid": "4456c28d-9600-47b2-bf04-ef599bd41ef5",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "2e310bde-9a35-40cc-9b3b-57dbe32dc790",
  "sourceToolAssistantUUID": "4456c28d-9600-47b2-bf04-ef599bd41ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T06:26:09.338Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V31EQev4A2PLDweHgkwXTu`</summary>

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
  "parentUuid": "2e310bde-9a35-40cc-9b3b-57dbe32dc790",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Ys51p2LvN31fSiqHY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2be553c8-7799-4d74-90da-9187eea56e50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6Rkwz518tMcVRacbZbBWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5513,
      "cache_read_input_tokens": 50956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5513,
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

_source line 43 · 2026-05-22T06:26:09.343Z_

<details><summary>↩ Tool result · `toolu_01V31EQev4A2PLDweHgkwXTu`</summary>

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
  "parentUuid": "2be553c8-7799-4d74-90da-9187eea56e50",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "ee13e670-5b57-4440-9b7c-bfcf98259781",
  "sourceToolAssistantUUID": "2be553c8-7799-4d74-90da-9187eea56e50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-22T06:26:09.703Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YEDGinqbWXmzQDxWxxG7qf`</summary>

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
  "parentUuid": "ee13e670-5b57-4440-9b7c-bfcf98259781",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Ys51p2LvN31fSiqHY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08824bf8-558d-45dc-8ee6-a0aa1f313912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6Rkwz518tMcVRacbZbBWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5513,
      "cache_read_input_tokens": 50956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5513,
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

_source line 45 · 2026-05-22T06:26:09.714Z_

<details><summary>↩ Tool result · `toolu_01YEDGinqbWXmzQDxWxxG7qf`</summary>

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
  "parentUuid": "08824bf8-558d-45dc-8ee6-a0aa1f313912",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "9c959052-6db1-4e91-8ddd-bb8b1dd4bb3d",
  "sourceToolAssistantUUID": "08824bf8-558d-45dc-8ee6-a0aa1f313912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-22T06:26:10.411Z_

<details open><summary>🔧 Tool call — Read · `toolu_014PZtN9orW3v8FMyTrjvoQw`</summary>

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
  "parentUuid": "9c959052-6db1-4e91-8ddd-bb8b1dd4bb3d",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Ys51p2LvN31fSiqHY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eccb499-805e-488f-b0a0-18dd8a1f1f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6Rkwz518tMcVRacbZbBWx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5513,
      "cache_read_input_tokens": 50956,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5513
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 50956,
          "cache_creation_input_tokens": 5513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5513,
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

_source line 47 · 2026-05-22T06:26:10.420Z_

<details><summary>↩ Tool result · `toolu_014PZtN9orW3v8FMyTrjvoQw`</summary>

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
  "parentUuid": "1eccb499-805e-488f-b0a0-18dd8a1f1f84",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "25c70617-fa0a-45a9-a791-417f20782a6c",
  "sourceToolAssistantUUID": "1eccb499-805e-488f-b0a0-18dd8a1f1f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-22T06:26:14.641Z_

Now let me read the remaining appendix sections that are most relevant to my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25c70617-fa0a-45a9-a791-417f20782a6c",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8ZG5s1PQe584hoftfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e1562ca-ef11-4de0-92f4-4df31cf791d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCm9Hx1ZmDFvRjKNWCmWnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2536,
      "cache_read_input_tokens": 56469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2536,
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

_source line 49 · 2026-05-22T06:26:15.248Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GbKBoptYdjFxvqLweaUdtT`</summary>

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
  "parentUuid": "5e1562ca-ef11-4de0-92f4-4df31cf791d5",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8ZG5s1PQe584hoftfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbd8ff69-8edd-4daa-b901-c0ee4a8ed2b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCm9Hx1ZmDFvRjKNWCmWnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2536,
      "cache_read_input_tokens": 56469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2536,
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

_source line 50 · 2026-05-22T06:26:15.254Z_

<details><summary>↩ Tool result · `toolu_01GbKBoptYdjFxvqLweaUdtT`</summary>

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
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC (Qwen3-8B, zero-shot greedy), lower on DocRED due to amortization over longer sequences; under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	
20	\paragraph{Greedy decoding determinism.}
21	\label{app:greedy-determinism}
22	% exp_id: d067_seed_variance
23	All main results use greedy decoding (temperature$\,{=}\,$0, argmax token selection).
24	Argmax is deterministic: the random seed controls \texttt{torch.manual\_seed} for sampling and dropout, neither of which is active during greedy inference.
25	We verify this with three seeds (42, 123, 456) across two LoRA fine-tuned models on all 551 SciERC documents.
26	Seeds 123 and 456, evaluated on the same GPU, produce byte-identical outputs for both Qwen3-8B and Llama-3.1-8B.
27	The residual variance in Table~\ref{tab:seed-variance} stems entirely from cross-hardware floating-point divergence: seed 42 was evaluated on a different server with a different CUDA driver version.
28	Even under this conservative upper bound, $\sigma(\text{E-F1}) \leq 0.16$\,pp, $\sigma(\text{R-F1}) \leq 0.43$\,pp, and $\sigma(\text{DR\%}) \leq 0.08$\,pp.
29	The constrained decoding DR\% reduction ($-$2.06\,pp for Qwen, $-$1.01\,pp for Llama) exceeds this variance by ${>}12\times$ (signal-to-noise ratio ${>}$\,12), confirming that observed improvements reflect genuine method effects rather than run-to-run noise.
30	We therefore report single-run results without error bars; bootstrap confidence intervals (10{,}000 iterations) are provided for F1 metrics.
31	
32	\begin{table}[h]
33	\centering
34	\caption{Cross-seed variance for LoRA fine-tuned models on SciERC (551 documents, greedy decoding, seeds 42/123/456). Values: mean $\pm$ population $\sigma$ across three seeds. Seeds 123 and 456 produce identical outputs on the same GPU; all observed $\sigma$ reflects cross-server floating-point divergence.}
35	\label{tab:seed-variance}
36	\small
37	\resizebox{\columnwidth}{!}{%
38	\begin{tabular}{@{}lllccc@{}}
39	\toprule
40	Model & Dataset & Mode & E-F1 & R-F1 & DR\% \\
41	\midrule
42	Qwen3-8B & SciERC & Unc & $66.94 \pm 0.08$ & $43.25 \pm 0.43$ & $2.06 \pm 0.08$ \\
43	Qwen3-8B & SciERC & Con & $66.94 \pm 0.08$ & $43.22 \pm 0.39$ & $0.00 \pm 0.00$ \\
44	Llama-3.1-8B & SciERC & Unc & $67.99 \pm 0.16$ & $45.38 \pm 0.05$ & $1.04 \pm 0.05$ \\
45	Llama-3.1-8B & SciERC & Con & $67.99 \pm 0.16$ & $45.40 \pm 0.05$ & $0.03 \pm 0.04$ \\
46	\bottomrule
47	\end{tabular}}
48	\end{table}
49	
50	\paragraph{Beam search non-determinism.}
51	Greedy decoding is deterministic (\S\ref{app:greedy-determinism} above).
52	Beam search ($k{\geq}2$) introduces non-determinism from GPU floating-point accumulation order; we report single-run results.
53	Based on the greedy cross-hardware variance ($\sigma < 0.5$\,pp, Table~\ref{tab:seed-variance}), beam search variance is expected to be of similar magnitude.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbd8ff69-8edd-4daa-b901-c0ee4a8ed2b4",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "8547e1b7-31b8-4626-8306-18f050dda5f2",
  "sourceToolAssistantUUID": "cbd8ff69-8edd-4daa-b901-c0ee4a8ed2b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T06:26:15.558Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KhKdjUuuiFcyZnNP2zFp3Z`</summary>

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
  "parentUuid": "8547e1b7-31b8-4626-8306-18f050dda5f2",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8ZG5s1PQe584hoftfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b861e4b-8c82-4d54-a0ea-5f49d087a57a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCm9Hx1ZmDFvRjKNWCmWnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2536,
      "cache_read_input_tokens": 56469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2536,
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

_source line 52 · 2026-05-22T06:26:15.564Z_

<details><summary>↩ Tool result · `toolu_01KhKdjUuuiFcyZnNP2zFp3Z`</summary>

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
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints (zero-shot).
23	SciERC: 551 documents; DocRED: matched 50-document subsets (same documents for greedy and beam); full 998-doc DocRED results in Table~\ref{tab:beam-docred-998-zs}.
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{@{}llcccccc@{}}
28	\toprule
29	\textbf{Model / Dataset} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
30	\midrule
31	\multirow{2}{*}{Qwen3-8B / SciERC (551)}
32	  & Greedy      & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
33	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.53} & 32.00 & 8.56 \\
34	\midrule
35	\multirow{2}{*}{Qwen3-8B / DocRED (50)}
36	  & Greedy      & 0 & 0 & 8.69 & 2.08 & 59.08 & 8.33 \\
37	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.55} & 58.64 & 9.37 \\
38	\midrule
39	\multirow{2}{*}{Llama-3.1-8B / SciERC (551)}
40	  & Greedy      & 0 & 0 & 0.08 & 6.56 & 23.49 & 2.54 \\
41	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.93} & 25.04 & 3.33 \\
42	\midrule
43	\multirow{2}{*}{Llama-3.1-8B / DocRED (50)}
44	  & Greedy      & 0 & 0 & 1.58 & 6.85 & 55.35 & 6.12 \\
45	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.94} & 55.62 & 9.47 \\
46	\midrule
47	\multirow{2}{*}{Mistral-7B / SciERC (551)}
48	  & Greedy      & 0 & 0 & 13.40 & 1.27 & 27.46 & 3.67 \\
49	  & Beam ($k{=}4$) & 0 & 0 & 13.79 & \textbf{0.57} & 26.66 & 4.37 \\
50	\midrule
51	\multirow{2}{*}{Mistral-7B / DocRED (50)}
52	  & Greedy      & 0 & 0 & 28.37 & 0.34 & 51.60 & 4.19 \\
53	  & Beam ($k{=}4$) & 0 & 0 & \textbf{21.37} & \textbf{0.19} & 51.78 & 5.70 \\
54	\bottomrule
55	\end{tabular}}
56	\end{table}
57	
58	\paragraph{Discussion.}
59	For calibrated models (Qwen3-8B, Llama-3.1-8B), beam search achieves DR=0\% across all four model-dataset combinations (both SciERC with 7 entity types, 551 documents, and DocRED with 96 relation types, 50 documents), regardless of schema complexity.
60	On SciERC, beam search eliminates DR for both Qwen (0.93\%\,$\to$\,0\%) and Llama (0.08\%\,$\to$\,0\%), and substantially reduces CF (Qwen: 9.90\%\,$\to$\,0.53\%; Llama: 6.56\%\,$\to$\,0.93\%).
61	On DocRED (matched 50-document subsets), beam search eliminates DR for both Qwen (8.69\%\,$\to$\,0\%) and Llama (1.58\%\,$\to$\,0\%), with CF reductions of 74\% and 86\% respectively.
62	Llama DocRED shows the largest R-F1 gain ($+$3.4\,pp), consistent with beam search recovering valid type assignments that greedy decoding missed due to constraint fallback.
63	The CF reduction is an indirect effect: beam search reduces constraint-fallback frequency by exploring alternative token sequences that satisfy both grammar and semantic masks simultaneously, avoiding the fallback-to-grammar path that produces cross-field inconsistencies under greedy decoding.
64	
65	Mistral-7B-v0.3 constitutes a boundary condition on both datasets.
66	On SciERC (7 entity types), beam search does not reduce DR (13.4\%\,$\to$\,13.8\%), though CF drops by 55\% relative (1.27\%\,$\to$\,0.57\%) and R-F1 improves by $+$0.7\,pp; the unchanged DR confirms that all residual violations stem from entity type misclassification, not constraint-search failure.
67	On DocRED (96 relation types), beam search reduces DR by 25\% relative (28.4\%\,$\to$\,21.4\%): the more complex schema introduces constraint-search failures that beam exploration resolves, but the entity misclassification component remains.
68	This contrast reveals that beam search resolves constraint-search failure (where greedy decoding encounters $G(t) \cap S(t) = \emptyset$ conflicts) but cannot overcome fundamental model calibration limitations in entity typing.
69	
70	\paragraph{Beam width ablation.}
71	Table~\ref{tab:beam-ablation} varies beam width $k \in \{1,2,4,8\}$ on Qwen3-8B / SciERC (551 documents) under full S1 constraints.
72	
73	\begin{table}[h]
74	\centering
75	\small
76	\caption{Effect of beam width on constraint satisfaction and extraction quality (Qwen3-8B, SciERC, 551 documents, full S1 constraints). $k{=}1$ corresponds to greedy decoding.}
77	\label{tab:beam-ablation}
78	\begin{tabular}{@{}rcccc@{}}
79	\toprule
80	$k$ & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
81	\midrule
82	1 (greedy) & 0.93 & 9.90 & 30.98 & 8.36 \\
83	2          & 0.35 & 4.12 & 31.54 & \textbf{8.75} \\
84	4          & \textbf{0}    & 0.53 & 32.00 & 8.56 \\
85	8          & \textbf{0}    & \textbf{0.08} & \textbf{32.18} & 8.39 \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	DR elimination at $k{\geq}4$ confirms that constraint-search failure is resolved with moderate exploration width.
91	CF continues to decrease with larger beam (0.08\% at $k{=}8$, only 2 residual violations), while entity extraction quality improves monotonically.
92	$k{=}4$ represents the optimal cost-effectiveness trade-off: it eliminates all DR violations at roughly half the compute cost of $k{=}8$.
93	
94	\paragraph{Beam width--latency Pareto analysis (LoRA).}
95	% exp_id: d066_beam_sweep
96	Figure~\ref{fig:beam-pareto} and Table~\ref{tab:beam-sweep} extend the beam width analysis to LoRA fine-tuning, where the constrained--unconstrained interaction shifts qualitatively: LoRA + S1 already achieves DR=0\% at $k{=}1$ (greedy), so beam search targets CF reduction rather than DR elimination (contrast: zero-shot requires $k{\geq}4$ for DR=0\%).
97	Among constrained configurations, $k{=}2$ is Pareto optimal (R-F1 44.60, CF 0.11\%, 1.39$\times$ latency); $k{\geq}4$ yields diminishing F1 returns with increasing latency (1.63--2.03$\times$).
98	
99	\begin{figure*}[ht]
100	\centering
101	\includegraphics[width=\textwidth]{figures/beam_pareto.pdf}
102	\caption{Beam width vs.\ R-F1 under LoRA fine-tuning. Left: SciERC (Qwen3-8B solid, Llama-3.1-8B dashed; 551 docs). Right: DocRED (Llama-3.1-8B, 200 docs). Bubble area $\propto$ total violation rate (DR+CF+RV); green rings mark zero-violation configurations. Star: Pareto-optimal ($k{=}2$).}
103	\label{fig:beam-pareto}
104	\end{figure*}
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Beam width sweep on SciERC (Qwen3-8B LoRA, 551 documents). \textsc{unc}: unconstrained; \textsc{con}: schema-constrained. Latency relative to $k{=}1$ unconstrained. Highlighted row: Pareto-optimal configuration.}
110	\label{tab:beam-sweep}
111	\resizebox{\columnwidth}{!}{%
112	\begin{tabular}{@{}cl cccc cc@{}}
113	\toprule
114	$k$ & Mode & E-F1 & R-F1 & DR (\%) & CF (\%) & Latency (s) & Rel.\ Lat. \\
115	\midrule
116	\multirow{2}{*}{1}
117	 & \textsc{unc} & 66.88 & 42.95 & 2.11 & 0    & 2.494 & 1.00$\times$ \\
118	 & \textsc{con} & 66.88 & 42.95 & \textbf{0} & 0.50 & 2.932 & 1.18$\times$ \\
119	\midrule
120	\multirow{2}{*}{2}
121	 & \textsc{unc} & 67.79 & 44.75 & 1.54 & 0    & 2.954 & 1.18$\times$ \\
122	 & \cellcolor{blue!8}\textsc{con} & \cellcolor{blue!8}67.71 & \cellcolor{blue!8}\textbf{44.60} & \cellcolor{blue!8}\textbf{0} & \cellcolor{blue!8}0.11 & \cellcolor{blue!8}3.463 & \cellcolor{blue!8}1.39$\times$ \\
123	\midrule
124	\multirow{2}{*}{4}
125	 & \textsc{unc} & 67.49 & 43.72 & 1.89 & 0    & 3.485 & 1.40$\times$ \\
126	 & \textsc{con} & 67.22 & 43.60 & \textbf{0} & 0    & 4.069 & 1.63$\times$ \\
127	\midrule
128	\multirow{2}{*}{8}
129	 & \textsc{unc} & 66.40 & 43.17 & 1.77 & 0    & 4.194 & 1.68$\times$ \\
130	 & \textsc{con} & 66.36 & 43.65 & \textbf{0} & 0    & 5.058 & 2.03$\times$ \\
131	\bottomrule
132	\end{tabular}}
133	\end{table}
134	
135	\paragraph{Composability with fine-tuning.}
136	Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with full S1 constraints already achieves DR=0\% but retains CF=1.18\% (21 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.
137	Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=43.60; changes within $\pm$0.5\,pp).
138	Llama-3.1-8B (LoRA, SciERC) with full S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) with R-F1=46.18; the zero-violation result thus generalizes across calibrated model families.
139	% exp_id: q1_llama_ft_beam_scierc
140	The three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.
141	
142	The initial 50-document DocRED subset (Table~\ref{tab:beam-search}) was subsequently validated on the full 998-document set (Table~\ref{tab:beam-docred-998-zs}): both models achieve DR${=}$0\%, confirming subset representativeness.
143	Llama shows the larger improvement (CF 8.54\%\,$\to$\,1.00\%, 88\% reduction; R-F1 $+$2.6\,pp), consistent with beam search resolving constraint-search failures that greedy decoding cannot.
144	
145	\begin{table}[h]
146	\centering
147	\small
148	\caption{Zero-shot beam search ($k{=}4$) under full S1 constraints on the full DocRED dev set (998 documents).
149	ET/RV/DR/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.}
150	\label{tab:beam-docred-998-zs}
151	\begin{tabular}{@{}lcccccc@{}}
152	\toprule
153	\textbf{Model} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
154	\midrule
155	Qwen3-8B  & 0 & 0 & \textbf{0} & 4.94 & 58.19 & 8.72 \\
156	Llama-3.1-8B & 0 & 0 & \textbf{0} & 1.00 & 57.81 & 8.83 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	Table~\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\bar{\kappa}$ regime.
162	Parse failure rates under LoRA beam-4 range from 1.3\% to 2.9\%, lower than the zero-shot rate.
163	
164	\begin{table}[h]
165	\centering
166	\small
167	\caption{LoRA greedy vs.\ beam search ($k{=}4$) on DocRED (998 dev documents) under full S1 constraints.
168	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field violation rates (\%); PF = parse failure rate (\%); F1 $\times$ 100.}
169	\label{tab:beam-docred-lora}
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{@{}llccccccc@{}}
172	\toprule
173	\textbf{Model} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ & PF \\
174	\midrule
175	\multirow{2}{*}{Qwen3-8B}
176	  & Greedy con & 0 & 0 & 0 & 0.22 & 81.87 & 40.79 & 7.8 \\ % d065_qwen_greedy_4096_r2
177	  & Beam-4 con & 0 & \textbf{0} & \textbf{0} & 0.01 & 84.00 & 44.46 & 2.9 \\
178	\midrule
179	\multirow{2}{*}{Llama-3.1-8B}
180	  & Greedy con & 0 & 0 & 0 & 0.26 & 84.71 & 44.70 & 2.6 \\ % d065: 4096 context
181	  & Beam-4 con & 0 & 0 & 0 & \textbf{0} & \textbf{85.23} & \textbf{47.17} & \textbf{1.3} \\
182	\bottomrule
183	\end{tabular}}
184	\end{table}
185	
186	Llama-3.1-8B achieves zero violations across all four metrics (ET, RV, DR, CF = 0\%) on DocRED with LoRA + beam-4, extending the zero-violation result from SciERC to the high-$\bar{\kappa}$ regime.
187	Qwen3-8B achieves DR=0\% with near-zero CF (0.01\%); R-F1 is preserved ($\pm$0.06\,pp).
188	Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
189	
190	\paragraph{Latency overhead.}
191	Table~\ref{tab:beam-latency} reports wall-clock latency for greedy and beam search ($k{=}4$) under LoRA fine-tuning.
192	
193	\begin{table}[h]
194	\centering
195	\small
196	\begin{tabular}{@{}lrr@{}}
197	\toprule
198	\textbf{Condition} & \textbf{s/doc} & \textbf{Overhead} \\
199	\midrule
200	Greedy unconstrained   & 2.612 & 1.00$\times$ \\
201	Greedy constrained (S1)& 2.873 & 1.10$\times$ \\
202	Beam-4 unconstrained   & 3.446 & 1.32$\times$ \\
203	Beam-4 constrained (S1)& 4.013 & 1.54$\times$ \\
204	\bottomrule
205	\end{tabular}
206	\caption{Latency per document (SciERC, 551 docs, Qwen3-8B LoRA FT, RTX PRO 6000 Blackwell). Overhead relative to greedy unconstrained.}
207	\label{tab:beam-latency}
208	\end{table}
209	
210	Beam search itself adds 32\% latency (4 beams); constraint overhead increases from 10\% (greedy) to 17\% (beam) because each beam independently maintains grammar and semantic state.
211	The total 1.54$\times$ overhead is acceptable for offline batch IE; \texttt{early\_stopping} limits additional compute to partial-sequence exploration.
212	
213	We also explored a type-consensus constraint that forces identical entity types across all relations within a document.
214	However, CF violations occur precisely where the consensus type conflicts with domain-range constraints, creating a fundamental CF$\leftrightarrow$DR trade-off.
215	With DR-aware enforcement (skipping consensus when it would violate domain-range), the layer becomes a no-op (100\% skip rate on 551 SciERC documents and 50 DocRED documents).
216	This confirms that beam search resolves the CF$\leftrightarrow$DR tension through a fundamentally different mechanism: token-level exploration of paths satisfying both constraints simultaneously.
217	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b861e4b-8c82-4d54-a0ea-5f49d087a57a",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "3da07e1c-88ed-4452-b2d6-78b4d22e82b8",
  "sourceToolAssistantUUID": "7b861e4b-8c82-4d54-a0ea-5f49d087a57a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T06:26:16.408Z_

<details open><summary>🔧 Tool call — Read · `toolu_011bmu2T16EVaLqK3taFoMYz`</summary>

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
  "parentUuid": "3da07e1c-88ed-4452-b2d6-78b4d22e82b8",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8ZG5s1PQe584hoftfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "262f67a7-82f6-4188-b914-4eb1b02e39f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCm9Hx1ZmDFvRjKNWCmWnF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2536,
      "cache_read_input_tokens": 56469,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2536
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 56469,
          "cache_creation_input_tokens": 2536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2536,
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

_source line 54 · 2026-05-22T06:26:16.800Z_

<details><summary>↩ Tool result · `toolu_011bmu2T16EVaLqK3taFoMYz`</summary>

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
  "parentUuid": "262f67a7-82f6-4188-b914-4eb1b02e39f8",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "01316b38-63d0-4047-819e-df596fa550f9",
  "sourceToolAssistantUUID": "262f67a7-82f6-4188-b914-4eb1b02e39f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-22T06:26:19.820Z_

Now let me read the remaining key appendix files for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01316b38-63d0-4047-819e-df596fa550f9",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Zj7ZQgrW8ecMdA5Cs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9094eeb-3c58-4842-a6b1-d2b61a6084a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmhVzG5Qq2MkbWAAeAuSwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23518,
      "cache_read_input_tokens": 59005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23518,
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

_source line 56 · 2026-05-22T06:26:21.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VRASkPt8jCRPYSqjDESVqH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9094eeb-3c58-4842-a6b1-d2b61a6084a6",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Zj7ZQgrW8ecMdA5Cs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edec8a9a-32d8-45ab-aa84-bb644a41fea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmhVzG5Qq2MkbWAAeAuSwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23518,
      "cache_read_input_tokens": 59005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23518,
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

_source line 57 · 2026-05-22T06:26:21.716Z_

<details><summary>↩ Tool result · `toolu_01VRASkPt8jCRPYSqjDESVqH`</summary>

```text
1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Full constraint compilation (schema parsing + grammar build) scales sub-linearly (0.32\,s to 0.42\,s for 7$\to$1{,}000 relations; Table~\ref{tab:scalability}); within this, the XGrammar automaton accounts for $\sim$0.044\,s and semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edec8a9a-32d8-45ab-aa84-bb644a41fea0",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "10ebad1a-eb50-410b-b9e5-addf3d520f2e",
  "sourceToolAssistantUUID": "edec8a9a-32d8-45ab-aa84-bb644a41fea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-22T06:26:22.187Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HDPnFhJikddJrq6gsn5q97`</summary>

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
  "parentUuid": "10ebad1a-eb50-410b-b9e5-addf3d520f2e",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Zj7ZQgrW8ecMdA5Cs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e51bed18-0139-4198-a036-f70731c72a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmhVzG5Qq2MkbWAAeAuSwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23518,
      "cache_read_input_tokens": 59005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23518,
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

_source line 59 · 2026-05-22T06:26:22.206Z_

<details><summary>↩ Tool result · `toolu_01HDPnFhJikddJrq6gsn5q97`</summary>

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
  "parentUuid": "e51bed18-0139-4198-a036-f70731c72a92",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "3c1e79a8-a5fc-41a3-bd35-c94287012e24",
  "sourceToolAssistantUUID": "e51bed18-0139-4198-a036-f70731c72a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-22T06:26:22.801Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bw3r8Z59SjwVKmhYEHzgFb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c1e79a8-a5fc-41a3-bd35-c94287012e24",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8Zj7ZQgrW8ecMdA5Cs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "980ae0f4-18c4-4c25-a084-3dcf4f0f49ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmhVzG5Qq2MkbWAAeAuSwD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23518,
      "cache_read_input_tokens": 59005,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 59005,
          "cache_creation_input_tokens": 23518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23518,
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

_source line 61 · 2026-05-22T06:26:22.807Z_

<details><summary>↩ Tool result · `toolu_01Bw3r8Z59SjwVKmhYEHzgFb`</summary>

```text
1	% Appendix: Post-hoc Type Consistency Resolution (TCR)
2	% exp_ids: d065_tcr_pilot (all 10 configs)
3	
4	\section{Post-hoc Type Consistency Resolution}
5	\label{app:tcr}
6	
7	S1 enforces domain/range constraints per-triple but does not enforce global entity type consensus, leaving residual CF violations where the same entity receives different types across triples.
8	We evaluate a post-hoc resolution step (TCR): for each entity with conflicting type assignments, TCR selects the type that maximizes satisfaction count across all relations referencing that entity, subject to domain/range constraints.
9	Unlike naive majority voting (which ignores relational constraints and increases DR), TCR is constraint-aware: candidate types are scored by how many of the entity's relational contexts they satisfy.
10	TCR runs after S1 decoding completes and has access to the full document context.
11	
12	% ──────────────────────────────────────────
13	%  Table: TCR results on SciERC
14	% ──────────────────────────────────────────
15	\begin{table}[h]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rr rr r r@{}}
20	\toprule
21	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
22	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
23	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
24	\midrule
25	\multirow{3}{*}{Zero-shot}
26	  & Qwen    & 9.75 & \textbf{0} & 0.93  & 1.21  & $-$1.29 & 2.04 \\
27	  & Llama   & 6.40 & \textbf{0} & 0.08  & 0.30  & $-$1.78 & 1.85 \\
28	  & Mistral & 0.67 & \textbf{0} & 13.36 & 12.87 & $+$0.05 & 0 \\
29	\midrule
30	\multirow{2}{*}{LoRA}
31	  & Qwen    & 1.19 & \textbf{0} & 0     & 0     & $-$0.75 & 0 \\
32	  & Llama   & 0.46 & \textbf{0} & 0.09  & 0.09  & $-$0.18 & 0 \\
33	\bottomrule
34	\end{tabular}}
35	\caption{TCR on SciERC ($\bar{\kappa}{=}0.333$, 551 docs).
36	Pre/Post: before/after TCR.
37	$\Delta$E-F1: entity F1 change (F1$\times$100).
38	Fund.: percentage of conflicting entities where no single type satisfies all relational constraints (fundamental conflicts).
39	TCR eliminates all CF with DR increases $\leq$0.28\,pp; fundamental conflicts are 0--2\%.}
40	\label{tab:tcr-scierc}
41	\end{table}
42	
43	% ──────────────────────────────────────────
44	%  Table: TCR results on DocRED
45	% ──────────────────────────────────────────
46	\begin{table}[h]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{@{}ll rr rr r r@{}}
51	\toprule
52	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
53	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
54	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
55	\midrule
56	\multirow{3}{*}{Zero-shot}
57	  & Qwen    & 13.11 & \textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\
58	  & Llama   & 23.71 & \textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\
59	  & 70B     & 11.61 & \textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\
60	\midrule
61	\multirow{2}{*}{LoRA}
62	  & Qwen    &  0.42 & \textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\
63	  & Llama   &  0.36 & \textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\
64	\bottomrule
65	\end{tabular}}
66	\caption{TCR on DocRED ($\bar{\kappa}{=}0.842$, 998 docs).
67	Under zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\,pp for Llama) and E-F1 drops (up to $-$5.98\,pp for 70B).
68	Fundamental conflict rates are 12--23\%, an order of magnitude higher than SciERC.
69	Under LoRA, low baseline CF (0.36--0.42\%) limits both TCR impact and DR cost.}
70	\label{tab:tcr-docred}
71	\end{table}
72	
73	\paragraph{Analysis.}
74	TCR effectiveness correlates inversely with schema constraint tightness $\bar{\kappa}$.
75	On SciERC ($\bar{\kappa}{=}0.333$), fundamental conflicts constitute 0--2\% of type disagreements: most conflicts are resolvable because the loose schema admits many valid type pairs, and TCR can find a type satisfying all relational contexts.
76	DR increases are bounded ($\leq$0.28\,pp), and E-F1 cost is modest ($\leq$1.78\,pp in zero-shot, $\leq$0.75\,pp under LoRA).
77	On DocRED ($\bar{\kappa}{=}0.842$), 13--23\% of conflicts are fundamental: the tight schema renders most type pairs invalid, so unifying an entity's type across all its relational contexts inevitably violates some domain/range constraints.
78	This produces severe DR regressions under zero-shot (Llama: 2.55\%$\to$11.93\%; 70B: 0\%$\to$4.20\%), where baseline CF is high enough that many entities require resolution.
79	Under LoRA, baseline CF is already low (0.36--0.42\%), limiting both the scope for TCR improvement and the DR cost.
80	
81	This $\bar{\kappa}$-dependent boundary is consistent with the constraint tightness analysis in \S\ref{sec:composition}: $\bar{\kappa}$ characterizes not only the decoding-time DR residual regime but also the feasibility of post-hoc type resolution.
82	Beam search (\S\ref{sec:beam-results}) resolves CF and DR simultaneously across all $\bar{\kappa}$ values (SciERC and DocRED (998 docs): DR$\to$0\% for calibrated models), making it the preferred approach for high-tightness schemas.
83	TCR is a zero-cost complement for low-tightness schemas where beam search latency (1.54$\times$) is undesirable.
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "980ae0f4-18c4-4c25-a084-3dcf4f0f49ea",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "30c37e96-cc20-462b-bc44-52b15aa11548",
  "sourceToolAssistantUUID": "980ae0f4-18c4-4c25-a084-3dcf4f0f49ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-22T06:26:26.232Z_

Now let me read the last few relevant files including the paper_checklist and the latest dream review report to check calibration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30c37e96-cc20-462b-bc44-52b15aa11548",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8aAxZuWa3tuvuAhniK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f354b97a-fbca-4b9f-8828-1fcab1a02d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKfPeuqeVz6wZ7RCmp9Z74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5354,
      "cache_read_input_tokens": 82523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5354,
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

_source line 63 · 2026-05-22T06:26:28.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HGgZhaSNf5UEdkkWosSSzV`</summary>

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
  "parentUuid": "f354b97a-fbca-4b9f-8828-1fcab1a02d72",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8aAxZuWa3tuvuAhniK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c29aba18-17db-41d9-91b8-c25c2866ad7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKfPeuqeVz6wZ7RCmp9Z74",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5354,
      "cache_read_input_tokens": 82523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5354,
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

_source line 64 · 2026-05-22T06:26:28.608Z_

<details><summary>↩ Tool result · `toolu_01HGgZhaSNf5UEdkkWosSSzV`</summary>

```text
1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{llcccccc}
13	\toprule
14	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
15	\midrule
16	\multirow{2}{*}{Default}
17	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
18	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
19	\midrule
20	\multirow{2}{*}{Minimal}
21	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
22	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
23	\midrule
24	\multirow{2}{*}{Detailed}
25	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
26	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (ET and RV drop to 0\%) for all three prompt variants. Domain-range violations are reduced by 94.0\%--94.6\%, with a standard deviation of only 0.3 percentage points across prompts. Meanwhile, F1 scores remain effectively unchanged: the largest shift is 0.13 percentage points (R-F1, Default prompt), so constraint enforcement does not degrade extraction quality.
32	
33	Notably, prompt variation has a measurable effect on baseline (unconstrained) violation rates, with DR ranging from 11.1\% (Detailed) to 16.9\% (Minimal). Under constrained decoding, this range narrows to 0.64\%--0.93\%, a 20$\times$ reduction in cross-prompt variance. This convergence is expected: because OntoCoDec enforces constraints at the token level during decoding, it operates independently of prompt content. The consistent reduction rates across diverse prompt styles confirm that the mechanism is orthogonal to prompting and generalizes without prompt-specific tuning.
34	Schema-informed prompting results serve as an upper bound on zero-shot prompt-level intervention; training-based approaches (e.g., GoLLIE) achieve compliance through code-generation format but with different coverage trade-offs (\S\ref{sec:related_work}).
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c29aba18-17db-41d9-91b8-c25c2866ad7b",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "d8ee92ce-89d5-49be-b209-cf3b27cdcd3a",
  "sourceToolAssistantUUID": "c29aba18-17db-41d9-91b8-c25c2866ad7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-22T06:26:29.184Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TW9vjcNDM37mFzzHabnBmU`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8ee92ce-89d5-49be-b209-cf3b27cdcd3a",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8aAxZuWa3tuvuAhniK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ab63b49-2c1b-43b4-9703-8f4b7674f5d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKfPeuqeVz6wZ7RCmp9Z74",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5354,
      "cache_read_input_tokens": 82523,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 82523,
          "cache_creation_input_tokens": 5354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5354,
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

_source line 66 · 2026-05-22T06:26:29.192Z_

<details><summary>↩ Tool result · `toolu_01TW9vjcNDM37mFzzHabnBmU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ab63b49-2c1b-43b4-9703-8f4b7674f5d9",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "3d651f3a-83ad-4a46-b599-4c6520e47e27",
  "sourceToolAssistantUUID": "5ab63b49-2c1b-43b4-9703-8f4b7674f5d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-22T06:26:32.233Z_

Let me also read the latest dream review to check calibration against prior internal reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d651f3a-83ad-4a46-b599-4c6520e47e27",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8aeKN2EB1atXwLEQGh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c861c045-eb70-43d5-b5ae-1ffa4ec72734",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LiuY47YZPfdyCKSPDmuaP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 87877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 68 · 2026-05-22T06:26:33.597Z_

<details open><summary>🔧 Tool call — Read · `toolu_0125QhtqHSKRmmRU4UVuh9Ja`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c861c045-eb70-43d5-b5ae-1ffa4ec72734",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8aeKN2EB1atXwLEQGh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "579846cd-13df-4867-ac42-f6f695d9b33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LiuY47YZPfdyCKSPDmuaP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 87877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 69 · 2026-05-22T06:26:33.607Z_

<details><summary>↩ Tool result · `toolu_0125QhtqHSKRmmRU4UVuh9Ja`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[T1]{fontenc}
3	\usepackage[utf8]{inputenc}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{multirow}
11	\usepackage{xcolor}
12	\usepackage{url}
13	\usepackage{hyperref}
14	\usepackage[margin=1in]{geometry}
15	\usepackage{enumitem}
16	\usepackage{tabularx}
17	\usepackage{array}
18	
19	\newcommand{\sys}{OntoCoDec}
20	\newcommand{\dmark}{\dag}
21	
22	\title{\sys{}: Type-Valid Information Extraction via Compiled Ontology Constraints}
23	
24	\author{Anonymous}
25	\date{}
26	
27	\begin{document}
28	\maketitle
29	
30	%-----------------------------------------------------------------------
31	\begin{abstract}
32	%-----------------------------------------------------------------------
33	Large language models applied to structured information extraction (IE) produce systematic ontology constraint violations---generating relation triples or event arguments whose entity types violate the schema's domain/range specifications.
34	We present \textbf{\sys{}}, a framework that automatically compiles IE ontology schemas into two composable constraint layers enforced during decoding: (1)~a \emph{grammar layer} that restricts the output vocabulary to ontology-valid type names via context-free grammars, and (2)~a \emph{semantic layer} that dynamically masks logits to enforce cross-field domain/range constraints using a stateful entity registry.
35	The two layers compose via bitwise AND of token masks with an enabling dependency: the grammar layer ensures structural validity, enabling the semantic layer to enforce type-level rules.
36	
37	We first present a systematic \emph{violation landscape} study across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) on two relation extraction datasets (SciERC, DocRED), revealing per-triple violation rates of 13--57\%.
38	\sys{} eliminates domain/range violations by 90--100\% with neutral F1 impact ($|\Delta\text{R-F1}| \leq 0.30$pp).
39	Scaling to Llama-3.1-70B confirms model-scale-invariant behavior: DR$\to$0\% on both datasets.
40	LoRA fine-tuned models retain 0.4--2.0\% residual violations that \sys{} further reduces to $\leq$0.21\%, demonstrating composability with parameter-efficient training.
41	Cross-task generalization to event extraction on WikiEvents (56 event types, 80 argument roles) shows that \sys{} eliminates event vocabulary and role vocabulary violations entirely (EV/RoV$\to$0\%) across all three models, while post-hoc filtering discards 99.6--100\% of arguments.
42	All constraint overhead is 10--18\% wall-clock time with no additional pipeline stages.
43	\end{abstract}
44	
45	%-----------------------------------------------------------------------
46	\section{Introduction}
47	\label{sec:intro}
48	%-----------------------------------------------------------------------
49	
50	Structured information extraction (IE) with large language models (LLMs) frames tasks such as relation extraction (RE) and event extraction (EE) as conditional text generation: given a document and an ontology schema, the model produces structured output (e.g., JSON) containing extracted entities, relations, or events.
51	A critical but under-studied failure mode of this paradigm is \emph{ontology constraint violation}---the model generates structurally valid output that nonetheless violates the schema's type specifications.
52	For example, a relation extraction system may output the triple \texttt{(``gradient descent'':Method, Used-for, ``accuracy'':Metric)} when the ontology specifies that the object of \texttt{Used-for} must be of type \texttt{Task}, not \texttt{Metric}.
53	
54	These violations are not rare edge cases.
55	Our systematic measurement across three model families and two RE datasets reveals per-triple violation rates of 13--57\%, with violations concentrating on relation types with tight domain/range constraints (e.g., \texttt{Feature-of}: 33.5\%, \texttt{Compare}: 42.4\%) rather than distributing uniformly.
56	Prompt-level intervention---explicitly describing constraints in the prompt---reduces overall violations by 32--62\% but cannot eliminate them, and for specific relation types can even \emph{increase} violation rates due to prior-constraint conflict.
57	
58	We propose \sys{} (\textbf{Onto}logy-\textbf{Co}nstrained \textbf{Dec}oding), a framework that automatically compiles IE ontology schemas into decoding-time constraints.
59	The framework comprises two composable layers:
60	\begin{enumerate}[nosep,leftmargin=*]
61	\item A \textbf{grammar layer} that compiles the ontology's type vocabulary into a context-free grammar (CFG) via XGrammar, constraining every generated type token to be ontology-valid.
62	\item A \textbf{semantic layer} that maintains a stateful entity registry during generation and dynamically masks logits to enforce domain/range (or role/argument-type) constraints that are context-sensitive and cannot be expressed by CFGs.
63	\end{enumerate}
64	The two layers compose via bitwise AND of their token masks, with an \emph{enabling dependency}: the grammar layer guarantees that every generated type is in the valid vocabulary, which is a prerequisite for the semantic layer to look up and enforce the corresponding constraints.
65	When the intersection is empty (high constraint tightness), the system degrades gracefully to grammar-only control, maintaining structural validity as a guaranteed floor.
66	
67	We validate \sys{} on two IE tasks spanning three levels of ontology complexity:
68	(1)~relation extraction on SciERC (7 relations) and DocRED (96 relations), and
69	(2)~event extraction on WikiEvents (56 event types $\times$ 80 argument roles $\times$ 27 entity types).
70	Across four model scales (7B--70B), two training regimes (zero-shot and LoRA fine-tuned), and all three datasets, \sys{} consistently eliminates vocabulary and structural violations to near-zero while maintaining F1-neutral or F1-positive impact.
71	
72	Our contributions are:
73	\begin{enumerate}[nosep,leftmargin=*]
74	\item A systematic \textbf{violation landscape study} quantifying ontology constraint violations across models, datasets, and constraint types---the first such measurement for LLM-based IE.
75	\item A \textbf{composable constraint compilation framework} that automatically translates ontology schemas into grammar and semantic decoding constraints, requiring zero task-specific code.
76	\item Extensive validation across \textbf{2 IE tasks $\times$ 3 datasets $\times$ 4 models $\times$ 2 training regimes}, demonstrating model-agnostic, scale-invariant, and task-generalizable violation elimination.
77	\end{enumerate}
78	
79	%-----------------------------------------------------------------------
80	\section{Background}
81	\label{sec:background}
82	%-----------------------------------------------------------------------
83	
84	\paragraph{Grammar-Constrained Decoding.}
85	Grammar-constrained decoding restricts LLM output to strings accepted by a formal grammar (typically a CFG or regular expression) by masking logits at each decoding step.
86	XGrammar~\cite{dong2024xgrammar} provides an efficient implementation that precomputes token masks from EBNF grammars.
87	This approach guarantees structural validity (e.g., well-formed JSON) but cannot express context-sensitive constraints such as ``the entity type in position $i$ must be compatible with the relation type generated at position $j$.''
88	
89	\paragraph{IE Ontology Constraints.}
90	An IE ontology $\mathcal{O}$ defines a set of entity types $\mathcal{E}$, relation types $\mathcal{R}$ (for RE) or event types $\mathcal{V}$ with argument roles $\mathcal{A}$ (for EE), and type constraints.
91	For RE, constraints take the form $r \in \mathcal{R}: \text{domain}(r) \subseteq \mathcal{E}, \text{range}(r) \subseteq \mathcal{E}$.
92	For EE, constraints specify which entity types are allowed for each (event\_type, role) pair: $\text{allowed}(v, a) \subseteq \mathcal{E}$ for $v \in \mathcal{V}, a \in \mathcal{A}_v$.
93	These constraints are \emph{context-sensitive}: the valid set of types at one position depends on values generated at other positions.
94	
95	\paragraph{Violation Taxonomy.}
96	We classify ontology violations into five types:
97	\begin{itemize}[nosep,leftmargin=*]
98	\item \textbf{DR} (Domain/Range): Entity type violates the relation's domain or range specification.
99	\item \textbf{RV} (Relation Vocabulary): Relation name not in the ontology.
100	\item \textbf{ET} (Entity Type): Entity type not in the ontology's type set.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "579846cd-13df-4867-ac42-f6f695d9b33c",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "cb303af2-b7b4-4a72-b5ff-58b110ffff57",
  "sourceToolAssistantUUID": "579846cd-13df-4867-ac42-f6f695d9b33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-22T06:26:33.902Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01P7QDhKt9J71wv57khdM8bp`</summary>

```json
{
  "pattern": "**/dream_20260522T052642/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb303af2-b7b4-4a72-b5ff-58b110ffff57",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8aeKN2EB1atXwLEQGh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9844cfed-df10-484c-bc16-e2fe3cf34dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012LiuY47YZPfdyCKSPDmuaP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 87877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 71 · 2026-05-22T06:26:33.920Z_

<details><summary>↩ Tool result · `toolu_01P7QDhKt9J71wv57khdM8bp`</summary>

```text
artifacts/dream_reports/dream_20260522T052642/logs/orchestrator.log
artifacts/dream_reports/dream_20260522T052642/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260522T052642/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260522T052642/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260522T052642/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260522T052642/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T052642/best/experiment_data.json
artifacts/dream_reports/dream_20260522T052642/best/paper_framing.md
artifacts/dream_reports/dream_20260522T052642/best/paper.tex
artifacts/dream_reports/dream_20260522T052642/best/paper.aux
artifacts/dream_reports/dream_20260522T052642/best/paper.out
artifacts/dream_reports/dream_20260522T052642/best/paper.pdf
artifacts/dream_reports/dream_20260522T052642/best/paper.log
artifacts/dream_reports/dream_20260522T052642/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260522T052642/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T052642/median/experiment_data.json
artifacts/dream_reports/dream_20260522T052642/median/paper_framing.md
artifacts/dream_reports/dream_20260522T052642/median/acl.sty
artifacts/dream_reports/dream_20260522T052642/median/paper.tex
artifacts/dream_reports/dream_20260522T052642/median/paper.aux
artifacts/dream_reports/dream_20260522T052642/median/paper.out
artifacts/dream_reports/dream_20260522T052642/median/paper.pdf
artifacts/dream_reports/dream_20260522T052642/median/paper.log
artifacts/dream_reports/dream_20260522T052642/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260522T052642/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260522T052642/worst/experiment_data.json
artifacts/dream_reports/dream_20260522T052642/worst/paper_framing.md
artifacts/dream_reports/dream_20260522T052642/worst/paper.tex
artifacts/dream_reports/dream_20260522T052642/worst/paper.aux
artifacts/dream_reports/dream_20260522T052642/worst/paper.out
artifacts/dream_reports/dream_20260522T052642/worst/paper.pdf
artifacts/dream_reports/dream_20260522T052642/worst/paper.log
artifacts/dream_reports/dream_20260522T052642/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260522T052642/best/review_context.yaml
artifacts/dream_reports/dream_20260522T052642/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9844cfed-df10-484c-bc16-e2fe3cf34dd1",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "5687a089-edc0-4015-b90a-bdd53bc60fb5",
  "sourceToolAssistantUUID": "9844cfed-df10-484c-bc16-e2fe3cf34dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-22T06:26:37.373Z_

Let me read the review context for the latest dream to understand what prior reviews have identified, and also check the 70B results section more carefully since it has XX.XX placeholders.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5687a089-edc0-4015-b90a-bdd53bc60fb5",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8azVoe8vMKy8hrPTFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfa8033d-a215-422c-8f53-dc9c646f5e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzzV1RJ5zhieb8nrYhj5Zb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3496,
      "cache_read_input_tokens": 89339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3496,
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

_source line 73 · 2026-05-22T06:26:38.523Z_

<details open><summary>🔧 Tool call — Read · `toolu_016uVKvcgLv7k24mVKkMHBKK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260522T052642/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfa8033d-a215-422c-8f53-dc9c646f5e41",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8azVoe8vMKy8hrPTFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10b939d6-b06c-4496-b8e1-053297bd5f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzzV1RJ5zhieb8nrYhj5Zb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3496,
      "cache_read_input_tokens": 89339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3496,
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

_source line 74 · 2026-05-22T06:26:38.744Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FadTqYQ5FsNhxHZpoK3SV9`</summary>

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
  "parentUuid": "10b939d6-b06c-4496-b8e1-053297bd5f34",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8azVoe8vMKy8hrPTFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46944d1f-3890-41a9-9061-12becbc15b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzzV1RJ5zhieb8nrYhj5Zb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3496,
      "cache_read_input_tokens": 89339,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 89339,
          "cache_creation_input_tokens": 3496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3496,
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

_source line 75 · 2026-05-22T06:26:38.788Z_

<details><summary>↩ Tool result · `toolu_016uVKvcgLv7k24mVKkMHBKK`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立——"universal ontology-constrained structured generation
2	  framework"。 Paper story: violation landscape (empirical contribution #1) → composable
3	  constraint compilation (methodological contribution #2) → RE 验证 (3 models × 2 datasets
4	  × ZS+FT) + EE 跨任务泛化 + 70B scale generalization。Claims 无需降级。Title 保留 "Type-Valid
5	  IE via Compiled Ontology Constraints"。 CF 写入 §7 limitation + beam search mitigation
6	  写入 §5.5，不影响 core claim。Conference main 稳过。 70B LoRA 结果复现 8B LoRA 的 scale-neutral
7	  模式：DR→近零、F1 中性/微正，confirming OntoCoDec 是 model-scale-invariant 的 plug-in infrastructure。
8	
9	  '
10	imagined_experiments:
11	- name: WikiEvents Qwen3-8B unconstrained
12	  plan_id: P021
13	  description: WikiEvents event extraction, Qwen3-8B, unconstrained baseline. 246
14	    docs.
15	  expected_results:
16	    parse_success_rate: 0.886
17	    ET_pct: 0
18	    EV_pct: 24.0
19	    RoV_pct: 74.9
20	    AC_pct: 0.3
21	    CF_pct: 0
22	    trigger_f1: 0.1184
23	    argument_f1: 0.0009
24	    entity_f1: 0
25	  result_rationale: 'EV=24% 来自 Qwen 对 56 类 hierarchical event type 的部分幻觉（约 1/4 输出使用非法
26	    event name）。 RoV=74.9% 是压倒性违规——80 个 argument roles conditioned on event type，zero-shot
27	    模型几乎 随机选择 role names。Entity F1=0% 因为 unconstrained 输出不符合 schema JSON 格式，parser
28	    无法 识别 entity mentions。AC 低(0.3%)因为大多数 argument 已经在 RoV 阶段被计为 invalid， 仅 role-valid
29	    的 argument 才会被检查 AC。这些 baseline 数字建立了 EE 比 RE 更严峻的 violation landscape，为 two-layer
30	    architecture 的必要性提供最强动机。
31	
32	    '
33	  tables:
34	  - name: 'Table: WikiEvents ZS Violation Rates (3 Models)'
35	    columns:
36	    - Metric
37	    - Qwen Unc.
38	    - Qwen S1
39	    - Llama Unc.
40	    - Llama S1
41	    - Mistral Unc.
42	    - Mistral S1
43	    rows:
44	    - - Parse %
45	      - '88.6'
46	      - '83.7'
47	      - '91.9'
48	      - '84.1'
49	      - '88.6'
50	      - '88.6'
51	    - - EV %
52	      - '24.0'
53	      - '0'
54	      - '10.5'
55	      - '0'
56	      - '37.3'
57	      - '0'
58	    - - RoV %
59	      - '74.9'
60	      - '0'
61	      - '88.8'
62	      - '0'
63	      - '63.9'
64	      - '0'
65	    - - AC %
66	      - '0.3'
67	      - '2.1'
68	      - '0.1'
69	      - '3.8'
70	      - '0'
71	      - '1.3'
72	    - - CF %
73	      - '0'
74	      - '21.1'
75	      - '0'
76	      - '17.2'
77	      - '0'
78	      - '14.9'
79	    - - Trigger F1
80	      - '11.8'
81	      - '13.4'
82	      - '5.7'
83	      - '7.5'
84	      - '2.4'
85	      - '3.9'
86	    - - Entity F1
87	      - '0'
88	      - '14.1'
89	      - '0'
90	      - '17.6'
91	      - '0'
92	      - '11.7'
93	  figures_description:
94	  - 'Stacked bar chart: EV+RoV+AC per model, unconstrained vs constrained。视觉上 unconstrained
95	    全是 violation（接近 100%），constrained 仅剩 AC 残余（1-4%），强烈对比。'
96	  analysis: 'WikiEvents 的 violation landscape 比 RE 严峻一个数量级：RoV 64-89% vs RE 的 RV 1-30%。
97	    这强化了 constraint decoding 在复杂 ontology 下的核心价值论证。Entity F1 从 0%→11-18% 不是 语义改进而是
98	    format compliance 恢复——grammar 产出 schema-valid JSON，parser 才能识别 entities。 三模型一致的
99	    EV/RoV→0% 确认 framework 跨任务泛化能力。
100	
101	    '
102	- name: WikiEvents Llama-3.1-8B unconstrained
103	  plan_id: P023
104	  description: WikiEvents event extraction, Llama-3.1-8B, unconstrained baseline.
105	    246 docs.
106	  expected_results:
107	    parse_success_rate: 0.919
108	    ET_pct: 0
109	    EV_pct: 10.5
110	    RoV_pct: 88.8
111	    AC_pct: 0.1
112	    CF_pct: 0
113	    trigger_f1: 0.0572
114	    argument_f1: 0
115	    entity_f1: 0
116	  result_rationale: 'Llama EV 最低(10.5%)说明其对 event type 名称的 memorization 更好（Llama 训练数据可能包含
117	    更多 KAIROS-adjacent 文本）。但 RoV 最高(88.8%)，表明即便知道正确 event type，argument role 的 per-event-type
118	    条件约束在 ZS 下几乎不可能满足。Trigger F1 5.7% 和 Arg F1 0% 确认 ZS EE 是极困难任务，F1 是控制变量而非优化目标。与
119	    Qwen 的对比（EV 24% vs 10.5%，RoV 75% vs 89%） 证明不同 model family 的 failure mode 分布不同——进一步支持
120	    model-agnostic constraint layer 的价值。
121	
122	    '
123	  tables: []
124	  figures_description: []
125	  analysis: 'Llama 的 RoV=88.8% 是所有实验中最高的单项 violation rate，形成 compelling evidence：
126	    即便是表现最好的模型（EV 仅 10.5%），在无约束下仍有近 90% 的 argument role 违规。 这个反直觉发现值得在 §5.4 重点强调。
127	
128	    '
129	- name: WikiEvents Mistral-7B unconstrained
130	  plan_id: P025
131	  description: WikiEvents event extraction, Mistral-7B-v0.3, unconstrained baseline.
132	    246 docs.
133	  expected_results:
134	    parse_success_rate: 0.789
135	    ET_pct: 0
136	    EV_pct: 37.3
137	    RoV_pct: 63.9
138	    AC_pct: 0
139	    CF_pct: 0
140	    trigger_f1: 0.0241
141	    argument_f1: 0
142	    entity_f1: 0
143	  result_rationale: 'Mistral EV 最高(37.3%)——SentencePiece tokenizer(~32K vocab) 对长
144	    hierarchical event names 的 tokenization 效率最低，更容易产生 OOV event types。RoV 相对最低(63.9%)可能是因为
145	    Mistral 输出 fewer arguments overall（质量更低但 surface-level violation 更少）。AC=0% 因为
146	    Mistral 基本不产出 entity type annotations（entity_f1=0%），没有可检查 AC 的 argument。 Parse
147	    rate 最低(78.9%)反映 SentencePiece tokenizer 在 complex JSON 生成上的劣势。
148	
149	    '
150	  tables: []
151	  figures_description: []
152	  analysis: '三模型的 violation 模式形成互补证据：Qwen 中等 EV + 高 RoV，Llama 低 EV + 极高 RoV， Mistral
153	    高 EV + 中等 RoV。每个模型的 failure mode 分布不同，但 OntoCoDec 均实现 EV/RoV→0%——证明 framework
154	    的 model-agnostic 特性。
155	
156	    '
157	- name: WikiEvents Mistral grammar_only v3
158	  plan_id: P027
159	  description: Grammar-only ablation on Mistral WikiEvents — proves semantic layer
160	    necessity for EE.
161	  expected_results:
162	    parse_success_rate: 0.886
163	    ET_pct: 0
164	    EV_pct: 0
165	    RoV_pct: 64.0
166	    AC_pct: 13.8
167	    CF_pct: 1.1
168	    entity_f1: 0.1192
169	    trigger_f1: 0.0337
170	    argument_f1: 0.0027
171	  result_rationale: 'Grammar-only 消除 EV→0%（CFG 约束 event type vocabulary 是 context-free
172	    的），但 RoV 仍有 64%——因为 argument role 的合法性取决于所在 event type（per-event-type conditional
173	    constraint）， 这是 context-sensitive 的，CFG 无法表达。AC 从 0%→13.8% 是 latent violation
174	    surfacing： grammar 强制产出有效 role names 后，这些 role 对应的 entity type 约束才能被检查，暴露 先前被
175	    RoV 掩盖的 AC violations。这与 RE 中 DocRED grammar_only DR=26.17%（latent DR surfacing）模式完全一致——是
176	    two-layer architecture 必要性的关键 ablation 证据。
177	
178	    '
179	  tables:
180	  - name: 'Table: WikiEvents Grammar-Only Ablation (Mistral)'
181	    columns:
182	    - Metric
183	    - Unconstrained
184	    - Grammar-Only
185	    - Full S1
186	    rows:
187	    - - EV %
188	      - '37.3'
189	      - '0'
190	      - '0'
191	    - - RoV %
192	      - '63.9'
193	      - '64.0'
194	      - '0'
195	    - - AC %
196	      - '0'
197	      - '13.8'
198	      - '1.3'
199	    - - CF %
200	      - '0'
201	      - '1.1'
202	      - '14.9'
203	    - - Entity F1
204	      - '0'
205	      - '11.9'
206	      - '11.7'
207	  figures_description:
208	  - 'Three-panel waterfall showing constraint layers progressively reducing violations:
209	    Unconstrained → Grammar-Only → Full S1。EV 在第一步消除，RoV 在第二步消除，AC surfacing 在第二步后暴露。'
210	  analysis: 'Grammar-only ablation 是论文最重要的 EE 证据之一。它证明：(1) grammar 层对 EE 的 EV 同样有效，(2)
211	    RoV 无法被 grammar 约束——需要 semantic layer，(3) AC surfacing 模式与 RE 中 DR surfacing 一致——同一
212	    latent violation 机制跨任务复现。结论：two-layer architecture 不是便利选择而是 necessary decomposition。
213	
214	    '
215	- name: WikiEvents EE post-hoc filtering (3 models)
216	  plan_id: P028
217	  description: Post-hoc filtering baseline for EE — demonstrates infeasibility of
218	    filter-based approach for complex IE tasks.
219	  expected_results:
220	    qwen_args_before: 5467
221	    qwen_args_after: 23
222	    qwen_discard_rate: 0.996
223	    llama_args_before: 5053
224	    llama_args_after: 3
225	    llama_discard_rate: 0.999
226	    mistral_args_before: 6034
227	    mistral_args_after: 0
228	    mistral_discard_rate: 1.0
229	  result_rationale: 'Post-hoc filtering 在 EE 上彻底失败——因为 RoV 64-89% + EV 10-37% 的累积
230	    violation rate 远超 RE 的 15-26%。RE 中 post-hoc 尚可保留 52-84% triples，但 EE 中 99.6-100%
231	    的 arguments 被丢弃。这是因为 EE 的约束层级更深（EV→RoV→AC 三级联，任何一级违规就被过滤）， 而 RE 仅有 DR 一级主要约束。Mistral
232	    100% discard 是极端案例：EV=37.3% 的 event type 已经不在 ontology 中，其下所有 arguments 自动 invalid。
233	    这个结果使 post-hoc 在 EE 场景下完全不可行——构成 decoding-time enforcement 的最强 motivation。
234	
235	    '
236	  tables:
237	  - name: 'Table: Post-hoc Filtering Feasibility (RE vs EE)'
238	    columns:
239	    - Setting
240	    - Dataset
241	    - Discard Rate %
242	    - Viable?
243	    rows:
244	    - - RE ZS
245	      - SciERC (Qwen)
246	      - '16.8'
247	      - Yes (costly)
248	    - - RE ZS
249	      - DocRED (Qwen)
250	      - '48.1'
251	      - Marginal
252	    - - RE ZS
253	      - DocRED (Mistral)
254	      - '73.7'
255	      - 'No'
256	    - - EE ZS
257	      - WikiEvents (Qwen)
258	      - '99.6'
259	      - 'No'
260	    - - EE ZS
261	      - WikiEvents (Llama)
262	      - '99.9'
263	      - 'No'
264	    - - EE ZS
265	      - WikiEvents (Mistral)
266	      - '100.0'
267	      - 'No'
268	  figures_description:
269	  - 'Bar chart: discard rate across RE/EE datasets, 按严重程度排列，显示从 16.8%→100% 的 escalation。视觉上
270	    EE 部分完全是黑色（discarded），与 RE 形成鲜明对比。'
271	  analysis: 'Post-hoc 在 EE 的 devastating failure 是论文叙事的关键转折点。RE 中 post-hoc 尚可作为 "expensive
272	    but functional" baseline，但 EE 中其彻底崩溃证明：随 ontology 复杂度增加， post-hoc 的 scalability
273	    是 O(violations^layers)——每增加一个约束层级，discard rate 指数增长。这为 decoding-time enforcement
274	    建立了不可替代的 positioning。
275	
276	    '
277	- name: 70B SciERC unconstrained + constrained
278	  plan_id: P029
279	  description: Llama-3.1-70B-Instruct AWQ-INT4 on SciERC, zero-shot. Scale dimension
280	    (8B→70B).
281	  expected_results:
282	    unconstrained:
283	      DR_pct: 6.5
284	      RV_pct: 0.6
285	      ET_pct: 0
286	      CF_pct: 0
287	      E_F1: 35.17
288	      R_F1: 11.22
289	    constrained:
290	      DR_pct: 0
291	      RV_pct: 0
292	      ET_pct: 0
293	      CF_pct: 3.66
294	      E_F1: 35.14
295	      R_F1: 11.24
296	    delta_DR_pp: -6.5
297	    delta_R_F1_pp: 0.02
298	    DR_reduction_pct: 100
299	  result_rationale: '70B ZS 在 SciERC 上实现 DR=0%（完全消除），远超 8B 的 DR≈0.08-0.93%。这是因为： (1)
300	    70B 的 baseline DR 仅 6.5%（8B 为 13-15%），更少的 violations 意味着更少的 fallback events，semantic
301	    mask 覆盖率更高；(2) SciERC 7-relation ontology 约束空间小， semantic mask 几乎不产生空交集。R_F1 delta
302	    +0.02pp 是 F1-neutral 的理想结果。 CF=3.66% 低于 8B Qwen 的 9.9%（70B 对 entity type 的一致性更好），但仍非零——
303	    确认 CF 是方法论固有限制而非小模型特有问题。
304	
305	    '
306	  tables:
307	  - name: 'Table: 70B ZS Results (SciERC + DocRED)'
308	    columns:
309	    - Dataset
310	    - Setting
311	    - DR %
312	    - RV %
313	    - ET %
314	    - CF %
315	    - R-F1 %
316	    - E-F1 %
317	    rows:
318	    - - SciERC
319	      - Unc.
320	      - '6.5'
321	      - '0.6'
322	      - '0'
323	      - '0'
324	      - '11.22'
325	      - '35.17'
326	    - - SciERC
327	      - S1
328	      - '0'
329	      - '0'
330	      - '0'
331	      - '3.66'
332	      - '11.24'
333	      - '35.14'
334	    - - DocRED
335	      - Unc.
336	      - '15.0'
337	      - '7.8'
338	      - '0.02'
339	      - '0.07'
340	      - '13.03'
341	      - '69.03'
342	    - - DocRED
343	      - S1
344	      - '0'
345	      - '0'
346	      - '0'
347	      - '7.01'
348	      - '13.07'
349	      - '69.05'
350	  figures_description: []
351	  analysis: '70B ZS 在两个 RE 数据集上均实现 DR=0%，R-F1 完全中性——这是最干净的 scale generalization 证据。与
352	    8B ZS 的 DR 0.08-10.21% 相比，70B 的更低 baseline violations 使 OntoCoDec 更容易 实现完全消除。关键
353	    insight：constraint effectiveness 与 model scale 正相关（更好的模型 → 更少 baseline violations
354	    → 更少 fallback → 更高 semantic coverage → DR→0%）。
355	
356	    '
357	- name: 70B DocRED unconstrained + constrained
358	  plan_id: P030
359	  description: Llama-3.1-70B-Instruct AWQ-INT4 on DocRED, zero-shot. Scale dimension.
360	  expected_results:
361	    unconstrained:
362	      DR_pct: 15.0
363	      RV_pct: 7.8
364	      ET_pct: 0.02
365	      CF_pct: 0.07
366	      E_F1: 69.03
367	      R_F1: 13.03
368	    constrained:
369	      DR_pct: 0
370	      RV_pct: 0
371	      ET_pct: 0
372	      CF_pct: 7.01
373	      E_F1: 69.05
374	      R_F1: 13.07
375	    delta_DR_pp: -15.0
376	    delta_R_F1_pp: 0.04
377	    DR_reduction_pct: 100
378	  result_rationale: '70B 在 DocRED 96-relation ontology 上也实现 DR=0%，是整个实验矩阵中最难的 ZS 配置
379	    （ontology 最大 × 模型最大）。8B Qwen 在 DocRED 仅达 DR↓45%（残余 10.21%），8B Llama DR↓90%（残余
380	    2.55%）——70B 一步到位 DR=0%，验证了 constraint tightness × model baseline 的 dual-factor
381	    理论：70B 的 RV=7.8%（远低于 Qwen 29.66%）意味着 grammar 层几乎不需要 强制纠正 relation names，semantic
382	    层面对的都是 legitimate relation types，constraint coverage 因此接近 100%。CF=7.01% 与 8B Llama(12.02%)
383	    和 8B Qwen(2.57%) 处于中间水平。
384	
385	    '
386	  tables: []
387	  figures_description: []
388	  analysis: '70B DocRED DR=0% 是实验矩阵中最关键的数据点之一。它解决了 paper 长期面临的 "DocRED DR 残余" 问题——不是方法论缺陷，而是小模型
389	    baseline violation rate 过高导致 fallback 频繁。R-F1 delta +0.04pp 与 SciERC 的 +0.02pp
390	    一致：scale up 后 F1 影响完全中性。
391	
392	    '
393	- name: Error analysis / case study
394	  plan_id: P031
395	  description: 10-20 representative cases from v3 EE results — AC residual analysis,
396	    CF root causes, qualitative evidence.
397	  expected_results:
398	    ac_residual_cases: 8
399	    ac_root_cause_semantic_confusion: 6
400	    ac_root_cause_bpe_collision: 2
401	    cf_root_cause_type_ambiguity: 7
402	    cf_root_cause_event_complexity: 3
403	    qualitative_constraint_save_cases: 5
404	  result_rationale: 'AC 残余（1.3-3.8%）的主要来源是语义混淆（如 SideOfConflict vs SentencedPerson，两者共享
405	    "参与冲突" 的语义空间）——这是 entity type ontology 的固有模糊性，非方法缺陷。Mistral 有 2 个 BPE collision
406	    残余案例（SID/SEN/SIDE→''S''），但 collision fix 已将 AC 从 16.6%→1.3%。 CF 根因分析将揭示 EE 的 CF
407	    比 RE 更高（15-21% vs 10%）是因为 argument structure 更复杂—— 同一 entity 可能在同一文档的不同 events
408	    中扮演不同角色（如 "Iran" 在 Attack 事件中是 Attacker(GPE) 而在 Sanction 事件中是 Target(ORG)），type
409	    assignment 本质上 event-dependent。 Qualitative "constraint save" 案例展示 OntoCoDec 将
410	    hallucinated event types 重定向到 语义最近的合法 type，保留信息提取的实质内容。
411	
412	    '
413	  tables: []
414	  figures_description:
415	  - 'Case study figure: 2-3 个并排案例，左侧 unconstrained 输出（红色标注 violations），右侧 constrained
416	    输出（绿色标注 corrections）。展示 grammar 层修正 event type + semantic 层修正 argument role 的联合效果。'
417	  analysis: 'Error analysis 为 paper 提供 qualitative depth。AC 残余的 semantic confusion
418	    根因分析 证明这不是 engineering bug 而是 ontology design limitation——future work 可通过 entity
419	    type hierarchy（如 Person 子类型细分）减少混淆。CF 的 event-dependent type assignment 分析首次系统性解释了为什么
420	    EE 的 CF 高于 RE——argument 结构复杂度是根因。
421	
422	    '
423	- name: EE FT composability
424	  plan_id: P032
425	  description: Fine-tuned model + OntoCoDec composability test on WikiEvents EE.
426	  expected_results:
427	    qwen_ft:
428	      unconstrained_parse_rate: 0.85
429	      unconstrained_trigger_f1: 0.3208
430	      unconstrained_arg_f1: 0.0785
431	      unconstrained_rov: 0.3831
432	      unconstrained_ac: 0.0268
433	      constrained_parse_rate: 0.95
434	      constrained_trigger_f1: 0.2672
435	      constrained_arg_f1: 0.0818
436	      constrained_rov: 0
437	      constrained_ac: 0
438	    llama_ft:
439	      unconstrained_trigger_f1: 0.2752
440	      unconstrained_arg_f1: 0.0998
441	      unconstrained_rov: 0.088
442	      unconstrained_ac: 0.035
443	      constrained_trigger_f1: 0.2691
444	      constrained_arg_f1: 0.0891
445	      constrained_rov: 0
446	      constrained_ac: 0.008
447	  result_rationale: 'EE FT composability 结果与 RE FT 模式一致：LoRA fine-tuning 大幅降低 baseline
448	    violations （Qwen RoV 74.9%→38.3%，Llama RoV 88.8%→8.8%），OntoCoDec 进一步消除至 0%。 关键发现：(1)
449	    Llama FT 的 RoV 降幅更大（从 88.8%→8.8%，91% 削减），说明 Llama 对 WikiEvents schema 的 LoRA 学习效率更高；(2)
450	    即便 FT 后，Qwen 仍有 38.3% RoV—— FT 无法完全解决 role constraint，OntoCoDec 仍有不可替代的价值；(3)
451	    Arg F1 在 constrained 下微升（Qwen +0.33pp, Llama 微降 -1.07pp），确认 FT+constrained 的 composability
452	    在 EE 上同样成立。
453	
454	    '
455	  tables:
456	  - name: 'Table: EE FT Composability (Qwen + Llama)'
457	    columns:
458	    - Model
459	    - Setting
460	    - RoV %
461	    - AC %
462	    - Trigger F1
463	    - Arg F1
464	    rows:
465	    - - Qwen FT
466	      - Unc.
467	      - '38.3'
468	      - '2.7'
469	      - '32.1'
470	      - '7.9'
471	    - - Qwen FT
472	      - S1
473	      - '0'
474	      - '0'
475	      - '26.7'
476	      - '8.2'
477	    - - Llama FT
478	      - Unc.
479	      - '8.8'
480	      - '3.5'
481	      - '27.5'
482	      - '10.0'
483	    - - Llama FT
484	      - S1
485	      - '0'
486	      - '0.8'
487	      - '26.9'
488	      - '8.9'
489	  figures_description: []
490	  analysis: 'EE FT composability 完成了 "ZS composability (RE) → FT composability (RE)
491	    → ZS generalization (EE) → FT composability (EE)" 的完整证据链。四个 quadrant 全部验证：OntoCoDec
492	    在任何 task × training regime 组合下都能即插即用地消除 violations。 这是 "universal framework" claim
493	    的最强支撑。
494	
495	    '
496	- name: Grammar-only cross-model validation (Qwen/Llama EE)
497	  plan_id: P033
498	  description: Grammar-only ablation on Qwen/Llama WikiEvents EE for completeness
499	    — extends Mistral-only ablation.
500	  expected_results:
501	    qwen_grammar_only:
502	      EV_pct: 0
503	      RoV_pct: 68.0
504	      AC_pct: 9.5
505	      CF_pct: 0.8
506	      entity_f1: 0.14
507	      trigger_f1: 0.12
508	    llama_grammar_only:
509	      EV_pct: 0
510	      RoV_pct: 77.0
511	      AC_pct: 12.0
512	      CF_pct: 0.5
513	      entity_f1: 0.17
514	      trigger_f1: 0.06
515	  result_rationale: '预测基于 Mistral grammar_only 模式 + cross-model violation 基线差异。Qwen
516	    grammar_only RoV≈68%（vs Mistral 64%）略高因为 Qwen unconstrained RoV=74.9% 本身更高，grammar
517	    层 不改变 role generation pattern。Llama grammar_only RoV≈77%（vs 其 unconstrained 88.8%）——
518	    grammar 层通过消除 OOV event types 间接减少了约 12pp RoV（部分 role violations 源于 hallucinated
519	    event types 下不存在的 roles）。AC surfacing pattern 在三个模型上一致： grammar_only AC=9-14%
520	    vs unconstrained AC=0-0.3%，确认 latent violation surfacing 是 model-agnostic 的架构特性。这三个模型的
521	    grammar_only 消融证据足以支持论文 §5.4 中 "grammar layer necessary but insufficient for EE"
522	    的 claim。
523	
524	    '
525	  tables:
526	  - name: 'Table: Grammar-Only Ablation Across Models (WikiEvents)'
527	    columns:
528	    - Model
529	    - EV %
530	    - RoV %
531	    - AC %
532	    - CF %
533	    rows:
534	    - - Mistral Unc.
535	      - '37.3'
536	      - '63.9'
537	      - '0'
538	      - '0'
539	    - - Mistral Grammar
540	      - '0'
541	      - '64.0'
542	      - '13.8'
543	      - '1.1'
544	    - - Mistral Full S1
545	      - '0'
546	      - '0'
547	      - '1.3'
548	      - '14.9'
549	    - - Qwen Unc.
550	      - '24.0'
551	      - '74.9'
552	      - '0.3'
553	      - '0'
554	    - - Qwen Grammar*
555	      - '0'
556	      - '68.0'
557	      - '9.5'
558	      - '0.8'
559	    - - Qwen Full S1
560	      - '0'
561	      - '0'
562	      - '2.1'
563	      - '21.1'
564	    - - Llama Unc.
565	      - '10.5'
566	      - '88.8'
567	      - '0.1'
568	      - '0'
569	    - - Llama Grammar*
570	      - '0'
571	      - '77.0'
572	      - '12.0'
573	      - '0.5'
574	    - - Llama Full S1
575	      - '0'
576	      - '0'
577	      - '3.8'
578	      - '17.2'
579	  figures_description: []
580	  analysis: 'Tier 3 优先级——Mistral grammar_only 已足够支撑论文 claim。如果 GPU 时间允许， Qwen/Llama
581	    grammar_only 为 appendix 完整性提供价值，但不影响核心叙事。 三模型一致的 AC surfacing 模式是 bonus finding。
582	
583	    '
584	- name: Bootstrap CI for EE metrics
585	  plan_id: P034
586	  description: Statistical significance testing for WikiEvents EE metric changes.
587	  expected_results:
588	    qwen_trigger_f1_delta: 1.55
589	    qwen_trigger_f1_p: 0.02
590	    qwen_entity_f1_delta: 14.09
591	    qwen_entity_f1_p: <0.001
592	    llama_trigger_f1_delta: 1.76
593	    llama_trigger_f1_p: 0.03
594	    llama_entity_f1_delta: 17.63
595	    llama_entity_f1_p: <0.001
596	    mistral_trigger_f1_delta: 1.46
597	    mistral_trigger_f1_p: 0.05
598	    mistral_entity_f1_delta: 11.71
599	    mistral_entity_f1_p: <0.001
600	  result_rationale: 'Entity F1 的 0%→11-18% 跳跃在统计上必然显著（p<0.001）——这是 floor-to-nonzero
601	    的 结构性变化，bootstrap 的每个 resample 都会反映这一模式。Trigger F1 的 +1.5-1.8pp 变化相对较小（基线 2.4-11.8%），在
602	    246 docs 样本下 p-values 预计在 0.02-0.05 范围—— borderline significant。但论文不需要 trigger
603	    F1 的显著性作为 core claim，因为 contribution 是 violation elimination 而非 F1 improvement。Entity
604	    F1 significance 足以在 appendix 中报告。
605	
606	    '
607	  tables: []
608	  figures_description: []
609	  analysis: 'Bootstrap CI 为 EE 结果提供 statistical rigor，但在 best tier 叙事下不是关键—— EV/RoV→0%
610	    的 exact match 不需要 CI，这些是确定性消除。CI 主要用于 F1 metrics， 且 Entity F1 的 floor-to-nonzero
611	    变化 trivially significant。放入 appendix。
612	
613	    '
614	- name: Latency overhead measurement
615	  plan_id: P035
616	  description: 'Wall-clock comparison: unconstrained vs constrained decoding overhead
617	    across tasks.'
618	  expected_results:
619	    re_zs_scierc_overhead_pct: 13.1
620	    re_ft_scierc_overhead_pct: 10.0
621	    re_zs_scierc_mean_s: 4.71
622	    re_ft_scierc_mean_s: 2.873
623	    ee_zs_wikievents_overhead_pct: 18.0
624	    ee_zs_wikievents_mean_s: 12.5
625	    beam4_overhead_pct: 16.5
626	    beam4_mean_s: 4.013
627	  result_rationale: 'RE ZS/FT latency已有实测数据（13.1%/10%）。EE latency预测~18%——高于 RE 的 13%
628	    因为： (1) WikiEvents ontology 更大（56 event types × 80 roles vs SciERC 7 relations），
629	    semantic mask computation 更重；(2) JSON 结构更深（events 内嵌 arguments 内嵌 entities）， 更多
630	    token positions 需要 mask 计算；(3) 但 absolute overhead 仍远低于 2× threshold， 属于 practical
631	    deployment 可接受范围。Beam search 的 16.5% constraint overhead 与 greedy 13.1% 接近——beam
632	    本身的多路扩展已 dominate latency，constraint 的增量开销 被 amortize。所有配置均在 1.2× 以下，不构成 deployment
633	    blocker。
634	
635	    '
636	  tables:
637	  - name: 'Table: Latency Overhead Summary'
638	    columns:
639	    - Setting
640	    - Unc. (s/doc)
641	    - Con. (s/doc)
642	    - Overhead %
643	    rows:
644	    - - RE ZS SciERC (8B)
645	      - '4.16'
646	      - '4.71'
647	      - '13.1'
648	    - - RE FT SciERC (8B)
649	      - '2.61'
650	      - '2.87'
651	      - '10.0'
652	    - - RE FT SciERC Beam-4 (8B)
653	      - '3.45'
654	      - '4.01'
655	      - '16.5'
656	    - - EE ZS WikiEvents (8B)*
657	      - '10.6'
658	      - '12.5'
659	      - ~18
660	  figures_description:
661	  - 'Bar chart: latency overhead percentage across settings, with 20% threshold line。所有
662	    bars 在 threshold 以下，视觉上证明 practical deployability。'
663	  analysis: 'Latency overhead 10-18% 在所有配置下均可接受。关键论点：相比 post-hoc filtering 需要额外 pipeline
664	    stage + re-extraction cycle，OntoCoDec 的 single-pass overhead 在 engineering 上更优。EE
665	    的 18% overhead 是 worst case，仍远低于 2× boundary。
666	
667	    '
668	- name: 70B LoRA SciERC unconstrained eval
669	  plan_id: R16-LoRA-SciERC-Unc
670	  description: 'Llama-3.1-70B-AWQ-INT4 LoRA fine-tuned on SciERC train set (3 epochs,
671	    checkpoint-663), unconstrained greedy eval on SciERC test (551 docs). Baseline
672	    for constrained comparison.
673	
674	    '
675	  expected_results:
676	    DR_pct: 0.8
677	    RV_pct: 0
678	    ET_pct: 0
679	    CF_pct: 0
680	    E_F1: 69.5
681	    E_P: 68.0
682	    E_R: 71.1
683	    R_F1: 48.2
684	    R_P: 44.8
685	    R_R: 52.3
686	    parse_fail_pct: 0
687	    total_samples: 551
688	  result_rationale: '8B LoRA baselines: Qwen DR=1.95%, R_F1=43.86%; Llama DR=1.11%,
689	    R_F1=45.45%。 70B LoRA 预期 DR~0.8%——低于 8B 因为 70B 的 larger capacity 使 LoRA training
690	    对 ontology constraints 的学习更充分（eval_loss 0.0611 与 8B 的 0.0586-0.0595 接近， 但 70B
691	    基座本身更强）。R_F1~48.2% 高于 8B 的 43-45%，但提升幅度不大（~3-5pp）—— SciERC 是小数据集（551 test, ~1.7K
692	    relations），LoRA 已经 saturate 了大部分 learnable signal，scale 的 marginal gain 有限。E_F1~69.5%
693	    略高于 8B 的 67-68%。 RV/ET=0% 因为 LoRA training 已完全学会 SciERC 的 7 个 relation name 和
694	    6 个 entity type。 CF=0% 与 8B unconstrained 一致（无 semantic enforcement 时 CF 来自 model
695	    自身一致性）。
696	
697	    '
698	  tables: []
699	  figures_description: []
700	  analysis: '70B LoRA unconstrained 的 DR=0.8% 确认 LoRA training 在 70B 上同样有效地降低 baseline
701	    violations（从 ZS 6.5%→LoRA 0.8%，↓88%）。R_F1 48.2% 预期为 cross-model 最高——为 "OntoCoDec
702	    composable with best available models" claim 提供 upper-bound 证据。
703	
704	    '
705	- name: 70B LoRA SciERC constrained eval (Full S1)
706	  plan_id: R16-LoRA-SciERC-S1
707	  description: 'Same 70B LoRA model, Full S1 constrained decoding on SciERC test (551
708	    docs). Best tier target: DR≤0.1%, |ΔR-F1|≤0.3pp.
709	
710	    '
711	  expected_results:
712	    DR_pct: 0.05
713	    RV_pct: 0
714	    ET_pct: 0
715	    CF_pct: 0.6
716	    E_F1: 69.5
717	    E_P: 68.0
718	    E_R: 71.1
719	    R_F1: 48.3
720	    R_P: 44.9
721	    R_R: 52.3
722	    parse_fail_pct: 0
723	    total_samples: 551
724	    delta_vs_unconstrained:
725	      DR_delta_pp: -0.75
726	      R_F1_delta_pp: 0.1
727	      E_F1_delta_pp: 0.0
728	  result_rationale: 'DR 0.8%→0.05%：70B LoRA 的 baseline DR 已极低，S1 仅需处理少量残余 violations。
729	    参考 8B patterns——Qwen LoRA DR 1.95%→0%, Llama LoRA 1.11%→0.09%。70B LoRA 的 baseline
730	    更低（0.8%），constrained 后 DR~0.05% 合理（可能有 1-2 个 edge case triple 因 fallback 未被 semantic
731	    mask 覆盖）。
732	
733	    R_F1 delta +0.1pp：与 8B Llama LoRA 的 +0.02pp 一致，在 F1-neutral 范围内。 LoRA 模型的 baseline
734	    RV 已经≈0%，grammar 层对 F1 无贡献；semantic 层的 DR reduction 也不改变 F1（正确 triples 的 type
735	    本就合法）。因此 F1 delta 应极小。
736	
737	    CF 0%→0.6%：与 8B Qwen LoRA 的 0%→1.18% 和 Llama LoRA 的 0%→0.46% 一致。 70B 的 CF 可能略低于
738	    8B Qwen 但略高于 8B Llama——取 0.6% 作为中间值。
739	
740	    这些数字完美落入 best tier ranges: DR 0.05% ∈ [0, 0.1]✓, ΔR-F1 +0.1pp ∈ [-0.3, 0.3]✓。
741	    Scale-neutral pattern confirmed：70B LoRA 复现了 8B LoRA 的 "DR→near-zero, F1-neutral"
742	    行为。
743	
744	    '
745	  tables:
746	  - name: 'Table: LoRA Constrained Decoding Across Scales (SciERC)'
747	    columns:
748	    - Model
749	    - DR Unc. %
750	    - DR S1 %
751	    - DR Red. %
752	    - R-F1 Unc.
753	    - R-F1 S1
754	    - Delta R-F1 pp
755	    rows:
756	    - - Qwen 8B
757	      - '1.95'
758	      - '0'
759	      - '100'
760	      - '43.86'
761	      - '43.77'
762	      - '-0.09'
763	    - - Llama 8B
764	      - '1.11'
765	      - '0.09'
766	      - '91.9'
767	      - '45.45'
768	      - '45.47'
769	      - '+0.02'
770	    - - Llama 70B*
771	      - '0.8'
772	      - '0.05'
773	      - '93.8'
774	      - '48.2'
775	      - '48.3'
776	      - '+0.1'
777	  figures_description:
778	  - 'Scale-neutral pattern chart: x-axis = model size (8B Qwen, 8B Llama, 70B Llama),
779	    y-axis = DR% (左轴, log scale) + R-F1 delta (右轴)。DR 在所有 scales 上→near-zero，R-F1
780	    delta 在 ±0.3pp band 内。Visual message: OntoCoDec is scale-invariant。'
781	  analysis: '70B LoRA SciERC constrained eval 是 best tier 的 make-or-break 数据点。DR≤0.1%
782	    和 |ΔR-F1|≤0.3pp 的预期基于三条证据线的收敛：(1) 8B Qwen/Llama LoRA 均在此范围内， (2) 70B ZS 已达 DR=0%，(3)
783	    eval_loss 0.0611 与 8B 可比。唯一风险是 AWQ-INT4 量化 引入微小的 logit distortion 使个别 edge case
784	    的 semantic mask 不生效——但 8B 未使用 量化也有残余 DR，故此风险不大。
785	
786	    '
787	- name: 70B LoRA DocRED unconstrained eval (200-doc)
788	  plan_id: R16-LoRA-DocRED-Unc
789	  description: 'Llama-3.1-70B-AWQ-INT4 LoRA fine-tuned on DocRED train set (3 epochs,
790	    checkpoint-1146), unconstrained greedy eval on DocRED dev 200-doc subset. Per
791	    D082 decision.
792	
793	    '
794	  expected_results:
795	    DR_pct: 0.4
796	    RV_pct: 0.05
797	    ET_pct: 0
798	    CF_pct: 0.1
799	    E_F1: 86.0
800	    E_P: 86.5
801	    E_R: 85.5
802	    R_F1: 46.5
803	    R_P: 42.0
804	    R_R: 52.0
805	    parse_fail_pct: 1.5
806	    total_samples: 200
807	  result_rationale: '8B LoRA DocRED baselines: Qwen DR=0.76%, R_F1=40.86%; Llama DR=0.49%,
808	    R_F1=43.72%。 70B LoRA 预期 DR~0.4%——略低于 8B Llama 的 0.49%，因为 70B 对 DocRED 96 relations
809	    的学习更充分（eval_loss 0.0635 vs 8B Llama 0.0624，接近但 70B 基座更强）。 R_F1~46.5% 高于 8B Llama
810	    43.72%，提升 ~3pp——与 SciERC 上的 scale gain 一致。 E_F1~86% 高于 8B Llama 83.93%，70B 对 entity
811	    mention detection 的改善更明显 （DocRED entity extraction 更复杂，benefit from larger model
812	    capacity）。 RV~0.05%（而非 0%）因为 DocRED 96 relations 中可能有 1-2 个 long-tail relation
813	    在 training data 中出现极少，70B LoRA 偶尔 hallucinate 接近但不完全匹配的 name。 200-doc subset per
814	    D082——足以建立 scale trend，不需要 998 全量。
815	
816	    '
817	  tables: []
818	  figures_description: []
819	  analysis: '200-doc subset 的统计功效：假设 DR σ≈0.3pp（基于 8B seed variance），200 docs 给出 95%
820	    CI ≈ ±0.04pp，足以确认 DR<0.5%。R_F1 的 95% CI ≈ ±1.5pp，足以区分 vs 8B baseline。Scale gain
821	    ~3pp R_F1 与 SciERC 一致——confirmation of scale trend。
822	
823	    '
824	- name: 70B LoRA DocRED constrained eval (200-doc, Full S1)
825	  plan_id: R16-LoRA-DocRED-S1
826	  description: 'Same 70B LoRA model, Full S1 constrained decoding on DocRED dev 200-doc
827	    subset. Best tier target: DR≤0.2%, |ΔR-F1|≤0.5pp.
828	
829	    '
830	  expected_results:
831	    DR_pct: 0.08
832	    RV_pct: 0
833	    ET_pct: 0
834	    CF_pct: 0.3
835	    E_F1: 86.0
836	    E_P: 86.5
837	    E_R: 85.5
838	    R_F1: 46.6
839	    R_P: 42.1
840	    R_R: 52.1
841	    parse_fail_pct: 1.5
842	    total_samples: 200
843	    delta_vs_unconstrained:
844	      DR_delta_pp: -0.32
845	      R_F1_delta_pp: 0.1
846	      E_F1_delta_pp: 0.0
847	  result_rationale: 'DR 0.4%→0.08%：DocRED 96-relation ontology 的 constraint space
848	    比 SciERC 更大， fallback frequency 相应更高（cf. 8B Qwen DocRED fallback 57次/doc vs SciERC
849	    11次/doc）。 但 70B LoRA 的 baseline RV≈0.05%（远低于 8B ZS Qwen 的 29.66%），grammar-semantic
850	    mask 交集几乎不为空，因此 fallback 率极低。预期 DR~0.08%（200 docs 上大约 1-2 个 residual violation
851	    triple），远在 best tier 0.2% 阈值内。
852	
853	    R_F1 delta +0.1pp：与 8B Llama LoRA 的 +0.06pp 一致。70B LoRA 的 RV 已极低， grammar 层几乎不改变
854	    prediction distribution；semantic 层的 DR reduction 也 不影响 F1（被纠正的 triples 大多本就是 FP）。F1
855	    delta 在 ±0.2pp 内是高置信度预期。
856	
857	    CF 0.1%→0.3%：DocRED LoRA 的 CF 整体较低（8B Llama 0.21%, Qwen 0.41%）。 70B 的 CF 预期在此范围内。CF
858	    增量 0.2pp 远小于 ZS 场景（ZS 70B CF=7.01%）—— LoRA training 显著减少了 entity type inconsistency。
859	
860	    Best tier alignment: DR 0.08% ∈ [0, 0.2]✓, ΔR-F1 +0.1pp ∈ [-0.5, 0.5]✓。 Scale-neutral
861	    pattern 在 DocRED 上同样成立。
862	
863	    '
864	  tables:
865	  - name: 'Table: LoRA Constrained Decoding Across Scales (DocRED)'
866	    columns:
867	    - Model
868	    - DR Unc. %
869	    - DR S1 %
870	    - DR Red. %
871	    - R-F1 Unc.
872	    - R-F1 S1
873	    - Delta R-F1 pp
874	    rows:
875	    - - Qwen 8B (998d)
876	      - '0.76'
877	      - '0.01'
878	      - '98.7'
879	      - '40.86'
880	      - '40.56'
881	      - '-0.30'
882	    - - Llama 8B (998d)
883	      - '0.49'
884	      - '0.21'
885	      - '57.1'
886	      - '43.72'
887	      - '43.78'
888	      - '+0.06'
889	    - - Llama 70B (200d)*
890	      - '0.4'
891	      - '0.08'
892	      - '80.0'
893	      - '46.5'
894	      - '46.6'
895	      - '+0.1'
896	  figures_description:
897	  - 'Paired bar chart: SciERC + DocRED side-by-side, 8B vs 70B LoRA, DR 和 R-F1 delta。两个数据集上
898	    70B 均在 best tier target zone 内。'
899	  analysis: '70B LoRA DocRED 是 best tier 的第二个关键数据点。200-doc subset 的选择（D082） 是 pragmatic——998-doc
900	    全量需要 ~15 小时（87s/sample × 998），200-doc 4 小时可完成。 统计功效足以确认 DR<0.2% 和 |ΔR-F1|<0.5pp。如果
901	    200-doc 结果 clean，可在 paper 中报告并注明 sample size，同时在 appendix 讨论 full-set extrapolation。
902	
903	    '
904	- name: Consolidated Results — Best Tier Paper Tables
905	  plan_id: SUMMARY
906	  description: All planned experiments consolidated into paper-ready tables.
907	  expected_results:
908	    total_experiment_configs: 45
909	    models_tested: 4
910	    datasets: 3
911	    tasks: 2
912	    scales: 2
913	    training_regimes: 2
914	  result_rationale: 'Best tier paper 需要 4 个核心 tables：(1) RE main results（3 models
915	    × 2 datasets × ZS unconstrained/constrained），(2) RE LoRA results（3 models × 2
916	    datasets，含 70B）， (3) WikiEvents EE results（3 models × unconstrained/constrained
917	    + grammar_only ablation）， (4) 70B scale generalization summary（ZS + LoRA，SciERC
918	    + DocRED）。这四个 tables 覆盖论文的全部 empirical claims。Appendix 另有 beam sweep、prompt sensitivity、
919	    latency、seed variance、post-hoc comparison 等补充 tables。
920	
921	    '
922	  tables:
923	  - name: 'Paper Table 1: RE Zero-Shot Main Results'
924	    columns:
925	    - Model
926	    - Dataset
927	    - Setting
928	    - DR %
929	    - RV %
930	    - ET %
931	    - CF %
932	    - R-F1 %
933	    - E-F1 %
934	    rows:
935	    - - Qwen 8B
936	      - SciERC
937	      - Unc.
938	      - '15.37'
939	      - '1.39'
940	      - '0.40'
941	      - '0.08'
942	      - '8.23'
943	      - '31.01'
944	    - - Qwen 8B
945	      - SciERC
946	      - Full S1
947	      - '0.93'
948	      - '0'
949	      - '0'
950	      - '9.90'
951	      - '8.36'
952	      - '30.98'
953	    - - Qwen 8B
954	      - DocRED
955	      - Unc.
956	      - '18.46'
957	      - '29.66'
958	      - '2.48'
959	      - '0.10'
960	      - '7.74'
961	      - '58.15'
962	    - - Qwen 8B
963	      - DocRED
964	      - Full S1
965	      - '10.21'
966	      - '0.03'
967	      - '0'
968	      - '2.57'
969	      - '8.23'
970	      - '59.37'
971	    - - Llama 8B
972	      - SciERC
973	      - Unc.
974	      - '13.34'
975	      - '0.55'
976	      - '0'
977	      - '0.24'
978	      - '2.68'
979	      - '23.56'
980	    - - Llama 8B
981	      - SciERC
982	      - Full S1
983	      - '0.08'
984	      - '0'
985	      - '0'
986	      - '6.56'
987	      - '2.54'
988	      - '23.49'
989	    - - Llama 8B
990	      - DocRED
991	      - Unc.
992	      - '26.07'
993	      - '16.03'
994	      - '0.13'
995	      - '0.17'
996	      - '5.98'
997	      - '55.65'
998	    - - Llama 8B
999	      - DocRED
1000	      - Full S1
1001	      - '2.55'
1002	      - '0'
1003	      - '0'
1004	      - '12.02'
1005	      - '6.27'
1006	      - '55.01'
1007	    - - Mistral 7B
1008	      - SciERC
1009	      - Unc.
1010	      - '56.94'
1011	      - '0'
1012	      - '1.50'
1013	      - '56.87'
1014	      - '3.66'
1015	      - '27.28'
1016	    - - Mistral 7B
1017	      - SciERC
1018	      - Full S1
1019	      - '13.40'
1020	      - '0'
1021	      - '0'
1022	      - '1.27'
1023	      - '3.67'
1024	      - '27.46'
1025	    - - Mistral 7B
1026	      - DocRED
1027	      - Unc.
1028	      - '57.42'
1029	      - '42.35'
1030	      - '7.58'
1031	      - '24.78'
1032	      - '4.34'
1033	      - '48.51'
1034	    - - Mistral 7B
1035	      - DocRED
1036	      - Full S1
1037	      - '33.20'
1038	      - '0'
1039	      - '0'
1040	      - '0.19'
1041	      - '5.52'
1042	      - '50.59'
1043	    - - Llama 70B
1044	      - SciERC
1045	      - Unc.
1046	      - '6.50'
1047	      - '0.60'
1048	      - '0'
1049	      - '0'
1050	      - '11.22'
1051	      - '35.17'
1052	    - - Llama 70B
1053	      - SciERC
1054	      - Full S1
1055	      - '0'
1056	      - '0'
1057	      - '0'
1058	      - '3.66'
1059	      - '11.24'
1060	      - '35.14'
1061	    - - Llama 70B
1062	      - DocRED
1063	      - Unc.
1064	      - '15.00'
1065	      - '7.80'
1066	      - '0.02'
1067	      - '0.07'
1068	      - '13.03'
1069	      - '69.03'
1070	    - - Llama 70B
1071	      - DocRED
1072	      - Full S1
1073	      - '0'
1074	      - '0'
1075	      - '0'
1076	      - '7.01'
1077	      - '13.07'
1078	      - '69.05'
1079	  - name: 'Paper Table 2: LoRA Fine-Tuned + Constrained (Scale Comparison)'
1080	    columns:
1081	    - Model
1082	    - Dataset
1083	    - N docs
1084	    - DR Unc. %
1085	    - DR S1 %
1086	    - R-F1 Unc.
1087	    - R-F1 S1
1088	    - Delta R-F1 pp
1089	    - CF S1 %
1090	    rows:
1091	    - - Qwen 8B
1092	      - SciERC
1093	      - '551'
1094	      - '1.95'
1095	      - '0'
1096	      - '43.86'
1097	      - '43.77'
1098	      - '-0.09'
1099	      - '1.18'
1100	    - - Llama 8B
1101	      - SciERC
1102	      - '551'
1103	      - '1.11'
1104	      - '0.09'
1105	      - '45.45'
1106	      - '45.47'
1107	      - '+0.02'
1108	      - '0.46'
1109	    - - Llama 70B*
1110	      - SciERC
1111	      - '551'
1112	      - '0.8'
1113	      - '0.05'
1114	      - '48.2'
1115	      - '48.3'
1116	      - '+0.1'
1117	      - '0.6'
1118	    - - Qwen 8B
1119	      - DocRED
1120	      - '998'
1121	      - '0.76'
1122	      - '0.01'
1123	      - '40.86'
1124	      - '40.56'
1125	      - '-0.30'
1126	      - '0.41'
1127	    - - Llama 8B
1128	      - DocRED
1129	      - '998'
1130	      - '0.49'
1131	      - '0.21'
1132	      - '43.72'
1133	      - '43.78'
1134	      - '+0.06'
1135	      - '0.21'
1136	    - - Llama 70B*
1137	      - DocRED
1138	      - '200'
1139	      - '0.4'
1140	      - '0.08'
1141	      - '46.5'
1142	      - '46.6'
1143	      - '+0.1'
1144	      - '0.3'
1145	  - name: 'Paper Table 3: WikiEvents Event Extraction (ZS)'
1146	    columns:
1147	    - Model
1148	    - Setting
1149	    - EV %
1150	    - RoV %
1151	    - AC %
1152	    - CF %
1153	    - Trig-F1 %
1154	    - Ent-F1 %
1155	    rows:
1156	    - - Qwen 8B
1157	      - Unc.
1158	      - '24.0'
1159	      - '74.9'
1160	      - '0.3'
1161	      - '0'
1162	      - '11.8'
1163	      - '0'
1164	    - - Qwen 8B
1165	      - Full S1
1166	      - '0'
1167	      - '0'
1168	      - '2.1'
1169	      - '21.1'
1170	      - '13.4'
1171	      - '14.1'
1172	    - - Llama 8B
1173	      - Unc.
1174	      - '10.5'
1175	      - '88.8'
1176	      - '0.1'
1177	      - '0'
1178	      - '5.7'
1179	      - '0'
1180	    - - Llama 8B
1181	      - Full S1
1182	      - '0'
1183	      - '0'
1184	      - '3.8'
1185	      - '17.2'
1186	      - '7.5'
1187	      - '17.6'
1188	    - - Mistral 7B
1189	      - Unc.
1190	      - '37.3'
1191	      - '63.9'
1192	      - '0'
1193	      - '0'
1194	      - '2.4'
1195	      - '0'
1196	    - - Mistral 7B
1197	      - Full S1
1198	      - '0'
1199	      - '0'
1200	      - '1.3'
1201	      - '14.9'
1202	      - '3.9'
1203	      - '11.7'
1204	    - - Mistral 7B
1205	      - Grammar
1206	      - '0'
1207	      - '64.0'
1208	      - '13.8'
1209	      - '1.1'
1210	      - '3.4'
1211	      - '11.9'
1212	  figures_description:
1213	  - 'Figure 1 (Intro/Method): Architecture diagram — ontology schema → compiler →
1214	    grammar CFG + semantic TypeConstraintProcessor → bitwise AND → constrained LLM
1215	    decoding。标注 enabling dependency arrow from grammar to semantic。'
1216	  - 'Figure 2 (§3 Violation Landscape): Heatmap of per-relation DR by model (SciERC
1217	    7 relations + DocRED top-10 relations)。Color intensity = violation rate，with tightness
1218	    τ̄ annotated per relation。'
1219	  - 'Figure 3 (§5 Results): DR reduction waterfall across settings (Unconstrained
1220	    → Grammar → Semantic → Full S1)，4-panel grid for SciERC/DocRED × Qwen/Llama。'
1221	  - 'Figure 4 (§5.4 EE): Stacked violation bar chart for WikiEvents (3 models × unc/grammar/S1)。Visual
1222	    dominance of RoV in unconstrained，clean elimination in Full S1。'
1223	  - 'Figure 5 (§5.5 or Appendix): Scale-neutral pattern plot — 8B vs 70B，DR and R-F1
1224	    delta，confirming model-size-invariance。'
1225	  analysis: Best tier paper 的 table/figure 密度目标是 ~1 table + ~1 figure per page (8
1226	    pages)。 4 tables + 5 figures = 9 visual elements 在 8 页正文中偏满——建议将 beam sweep 和
1227	    prompt sensitivity tables 移入 appendix，正文保留 3 tables + 4 figures。
1228	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10b939d6-b06c-4496-b8e1-053297bd5f34",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "54e918c5-48be-45de-93d5-47791e34a948",
  "sourceToolAssistantUUID": "10b939d6-b06c-4496-b8e1-053297bd5f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-22T06:26:38.800Z_

<details><summary>↩ Tool result · `toolu_01FadTqYQ5FsNhxHZpoK3SV9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T12:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"grammar_constrained\\\"\\n    name: \\\"Grammar-Constrained Decoding\\\"\\n    narrative: \\\"Token-level structural constraints via CFG/PDA for LLM generation\\\"\\n  - key: \\\"semantic_constrained\\\"\\n    name: \\\"Semantic-Aware Constrained Decoding\\\"\\n    narrative: \\\"Beyond grammar — enforcing semantic validity during generation\\\"\\n  - key: \\\"schema_ie\\\"\\n    name: \\\"Schema-Guided Information Extraction\\\"\\n    narrative: \\\"Leveraging ontology/schema to guide LLM-based IE\\\"\\n  - key: \\\"quality_impact\\\"\\n    name: \\\"Constraint Quality Impact Analysis\\\"\\n    narrative: \\\"Studies on how constrained decoding affects output quality\\\"\\n\\npapers:\\n  dong2025xgrammar:\\n    title: \\\"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models\\\"\\n    authors: [\\\"Dong, Y.\\\"]\\n    year: 2025\\n    venue: \\\"MLSys\\\"\\n    url: \\\"https://arxiv.org/abs/2411.15100\\\"\\n    bibtex_key: \\\"dong2025xgrammar\\\"\\n    category: \\\"grammar_constrained\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Foundation of grammar constraint layer; XGrammar is directly used in OntoCoDec's Level 1 constraints\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  sainz2024gollie:\\n    title: \\\"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction Modeling\\\"\\n    authors: [\\\"Sainz, O.\\\"]\\n    year: 2024\\n    venue: \\\"ICLR\\\"\\n    url: \\\"https://arxiv.org/abs/2310.03668\\\"\\n    bibtex_key: \\\"sainz2024gollie\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Schema-guided IE with LLMs via code-style guidelines; competing approach using prompt-level schema enforcement\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  scholak2021picard:\\n    title: \\\"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models\\\"\\n    authors: [\\\"Scholak, T.\\\", \\\"Schucher, N.\\\", \\\"Bahdanau, D.\\\"]\\n    year: 2021\\n    venue: \\\"EMNLP\\\"\\n    url: \\\"https://arxiv.org/abs/2109.05093\\\"\\n    bibtex_key: \\\"scholak2021picard\\\"\\n    category: \\\"semantic_constrained\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Semantic constrained decoding for SQL; closest methodological parallel — incremental parsing with semantic validity checks\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  geng2023gcd:\\n    title: \\\"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning\\\"\\n    authors: [\\\"Geng, S.\\\"]\\n    year: 2023\\n    venue: \\\"EMNLP\\\"\\n    url: \\\"https://arxiv.org/abs/2305.13971\\\"\\n    bibtex_key: \\\"geng2023gcd\\\"\\n    category: \\\"grammar_constrained\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Grammar-constrained decoding applied to NLP tasks; directly comparable zero-shot approach\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  sakota2025boostcd:\\n    title: \\\"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction\\\"\\n    authors: [\\\"Sakota, M.\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    url: \\\"https://arxiv.org/abs/2506.14901\\\"\\n    bibtex_key: \\\"sakota2025boostcd\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Most direct competitor — constrained decoding for IE with quality-constraint tradeoff analysis\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  li2024knowcoder:\\n    title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\\\"\\n    authors: [\\\"Li, Z.\\\"]\\n    year: 2024\\n    venue: \\\"ACL\\\"\\n    url: \\\"https://arxiv.org/abs/2403.07969\\\"\\n    bibtex_key: \\\"li2024knowcoder\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Schema-aware IE via code representation; encodes ontology into code structure for universal IE\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  ugare2025itergen:\\n    title: \\\"IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking\\\"\\n    authors: [\\\"Ugare, S.\\\"]\\n    year: 2025\\n    venue: \\\"ICLR\\\"\\n    url: \\\"https://arxiv.org/abs/2410.07295\\\"\\n    bibtex_key: \\\"ugare2025itergen\\\"\\n    category: \\\"semantic_constrained\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Semantic-aware structured generation with backtracking; addresses same problem of grammar insufficiency for semantic constraints\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  josifoski2022genie:\\n    title: \\\"GenIE: Generative Information Extraction\\\"\\n    authors: [\\\"Josifoski, M.\\\"]\\n    year: 2022\\n    venue: \\\"NAACL\\\"\\n    url: \\\"https://arxiv.org/abs/2112.08340\\\"\\n    bibtex_key: \\\"josifoski2022genie\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Generative IE with trie-based prefix constrained decoding; early work on constraint-guided IE generation\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  li2023codeie:\\n    title: \\\"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\\\"\\n    authors: [\\\"Li, P.\\\"]\\n    year: 2023\\n    venue: \\\"ACL\\\"\\n    url: \\\"https://arxiv.org/abs/2305.05711\\\"\\n    bibtex_key: \\\"li2023codeie\\\"\\n    category: \\\"schema_ie\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Code generation approach to IE; leverages code structure for implicit schema compliance\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\\n  banerjee2025crane:\\n    title: \\\"CRANE: Reasoning with Constrained LLM Generation\\\"\\n    authors: [\\\"Banerjee, P.\\\"]\\n    year: 2025\\n    venue: \\\"ICML\\\"\\n    url: \\\"https://arxiv.org/abs/2502.09061\\\"\\n    bibtex_key: \\\"banerjee2025crane\\\"\\n    category: \\\"quality_impact\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Studies quality impact of constrained decoding on reasoning; relevant to F1 impact analysis\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T12:00:00Z\\\"\\n\", \"total_chars\": 5828, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46944d1f-3890-41a9-9061-12becbc15b84",
  "isSidechain": true,
  "promptId": "7f7f02bf-bfd1-4663-b51e-c5c8ba1bdd7b",
  "agentId": "abaa6e03a45e8148b",
  "type": "user",
  "uuid": "a87edf30-6051-4194-8cef-35e920eb5721",
  "sourceToolAssistantUUID": "46944d1f-3890-41a9-9061-12becbc15b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-22T06:28:35.248Z_

I have now read the complete paper (main text, all appendices, and project context). I have comprehensive knowledge of the methodology, experiments, results, and limitations. Let me now compose my review.

---

## EMNLP 2026 ARR Review -- Reviewer 1 (Methods & Experiments)

**Paper**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

---

### 1. Summary

This paper addresses ontology type constraint violations in LLM-based structured information extraction. The authors propose OntoCoDec, a two-layer constrained decoding framework: a grammar layer (compiled via XGrammar) ensures JSON structural validity and vocabulary membership, while a semantic layer maintains a runtime entity registry for dynamic logit masking of domain/range constraints. The paper includes a violation landscape study, evaluates on RE (SciERC, DocRED) and EE (WikiEvents) across 4 models (7B--70B) under zero-shot and LoRA fine-tuned settings, and provides extensive ablations including grammar-only, semantic-only, beam search, post-hoc filtering, and trie-only baselines.

---

### 2. Soundness: 3.5 / 5

The core methodology is technically correct. The two-layer decomposition is well-motivated by the decidability analysis, and the Proposition 1 proof (that domain/range constraints are not context-free) is valid. The composition via bitwise AND with grammar-first fallback is a principled design. However, several soundness issues temper my assessment:

**Positive:**
- The formal analysis of constraint decidability levels is sound and provides genuine theoretical grounding.
- The causal tracing analysis (Table in Appendix) cleanly establishes that 100% of residual DR violations occur at fallback positions -- this is an important mechanistic finding.
- The five-way ablation on SciERC cleanly isolates the contribution of each layer.
- Bootstrap confidence intervals (10,000 iterations) are provided for F1 metrics with p-values.

**Concerns:**
- The claim "92--100% DR reduction" under fine-tuning is technically correct but obscures that Llama-8B SciERC achieves only 92% (not near-100%), and more importantly, the fine-tuned Llama DocRED contributes 33 of 36 residual violations (92%). The method's effectiveness is model-dependent in ways not fully captured by the top-line claim.
- The 70B LoRA results in Section 5 contain literal "XX.XX" placeholders (`section5_runtime.tex`, line 19). This is a serious completeness issue -- either the experiments were not finished or the paper was submitted prematurely. The paper explicitly states 70B LoRA results will demonstrate "scale-independent composability" but cannot be verified from the current manuscript.
- Constraint tightness kappa-bar as a "descriptive metric" is fitted on n=4 data points with R^2=0.886 but p=0.058 (not significant). The paper acknowledges this but still devotes substantial space to the dual-factor analysis. At n=4, the linear fit is essentially unconstrained (df=2), and any two-parameter model would fit well. This finding should be presented with much greater caution.
- The constraint tables for SciERC and DocRED are derived from training-data co-occurrence statistics, not from a formal ontology. This means the "ontology" in OntoCoDec is actually an empirical approximation. The paper acknowledges 99%+ coverage but the 1% gap contributes to residual violations (33% of the 36 FT residuals are schema coverage gaps).

---

### 3. Reproducibility: 3.5 / 5

**Positive:**
- Hyperparameters are well-specified (LoRA rank, learning rate, batch size, epochs, all target modules listed).
- Hardware is identified (RTX PRO 6000 Blackwell, 98GB VRAM).
- Greedy decoding determinism is verified across seeds with explicit variance bounds.
- Software versions are listed (PyTorch 2.10, Transformers 4.57, etc.).
- Code release is promised upon acceptance.

**Concerns:**
- The constraint tables (the mapping sigma(r) for each dataset) are central to reproducibility but are not explicitly provided. Without the exact type-pair tables, a reimplementation would need to re-derive them from training data using unspecified extraction logic.
- The fuzzy relation matching protocol (token overlap >80% AND edit distance <=2) is described in the appendix but the implementation choices could affect results. The 98 additional TPs for Mistral from fuzzy matching (+0.84pp R-F1) are non-trivial.
- The WikiEvents ontology required manual additions (5 Contact subtypes + CRM entity type) beyond what the official ontology provides. These modifications are mentioned but the exact mapping is not provided.
- DocRED is evaluated on the dev set (not test set), which is standard, but the constraint table is derived from the training set of the same dataset, creating a potential information leakage concern for the fine-tuned setting (the model sees training data that also defines the constraints).

---

### 4. Strengths

- **Comprehensive experimental matrix.** The paper covers 3 datasets, 5 models (3 at 8B, 1 at 70B zero-shot, 1 at 70B LoRA), 2 tasks, 2 training regimes, with extensive ablations (five-way, grammar-only, semantic-only, trie-only, post-hoc filtering, beam search, prompt sensitivity, seed variance). This is significantly more thorough than the typical constrained decoding paper.

- **Honest and thorough treatment of CF trade-off.** The CF-DR trade-off analysis, including the CF-priority fallback ablation showing that eliminating CF re-routes violations to DR (+13.85pp), is an exemplary piece of scientific honesty. The paper does not hide this limitation and provides mechanistic explanation.

- **WikiEvents extension provides genuine generalization evidence.** The EE results on WikiEvents demonstrate the framework's applicability beyond RE, with a different constraint structure (event types, argument roles, entity types). The grammar-only ablation on EE (RoV persists at 64--77%) cleanly establishes the necessity of the semantic layer for this task.

- **Post-hoc filtering comparison is well-executed.** The 99.6--100% argument discard rate for EE post-hoc filtering is a devastating comparison that strongly motivates the decoding-time approach. The multi-dimensional comparison (recall, coverage, operational) is fairer than simple F1 comparison.

- **Causal tracing of residual violations.** The instrumented fallback analysis establishes that all residual DR occurs exclusively at grammar-first fallback positions, providing clear mechanistic understanding of the method's ceiling.

- **Beam search compatibility and full sweep.** The beam width ablation (k=1,2,4,8) with LoRA fine-tuning achieving zero violations on SciERC at k>=4 is a strong practical result. The Pareto analysis is useful for deployment guidance.

---

### 5. Weaknesses

**Major:**

- **(M1) Incomplete 70B LoRA results.** The 70B LoRA paragraph in Section 5 contains "XX.XX" placeholders for all metrics. This is one of the paper's claimed contributions ("70B LoRA in Section 5") and a key piece of the "scale-independent composability" narrative. Submitting with placeholder data is a significant issue that undermines the completeness of the evaluation. The paper cannot claim "5 models" in the experimental coverage when 20% of the scale experiments are missing.

- **(M2) Residual DR on Mistral is very high (13.4% SciERC, 33.2% DocRED).** The paper acknowledges Mistral as a "boundary condition" and excludes it from the dual-factor analysis, but this substantially weakens the "model-agnostic" framing. On DocRED, the method leaves one-third of triples violating constraints. The paper should more prominently acknowledge that for poorly-calibrated models, OntoCoDec provides limited benefit. The current framing of "76--99% DR reduction" in the cross-model section is misleading when it includes 42% reduction (Mistral DocRED from 57.42% to 33.20%).

- **(M3) CF trade-off is substantial and not adequately resolved.** Under zero-shot decoding, CF rises to 9.90% (SciERC), 12.02% (DocRED Llama), and 14.9--21.1% (WikiEvents). While the paper argues CF is a "soft" violation vs. DR's "hard" violation, this distinction is debatable: downstream KG consumers would treat entity type inconsistency as a serious data quality issue. The fine-tuned CF (<=1.3%) is acceptable, but the zero-shot CF makes the method's primary evaluation setting problematic. The fact that Total violations (DR+CF) under S1 can be comparable to or higher than unconstrained (e.g., SciERC: 10.83% vs. 15.45%) undercuts the value proposition in zero-shot.

- **(M4) No experimental comparison with the most relevant constrained generation baselines.** The paper discusses GCD, BoostCD, SynCode, CRANE, IterGen, and PICARD in related work but never experimentally compares against any of them. The trie-only ablation is positioned as "GCD-equivalent" but this is an ablation of the authors' own system, not a comparison against GCD's actual implementation. BoostCD is described as "complementary and potentially integrable" without evidence. IterGen with backtracking is arguably the most relevant semantic constraint baseline and is only cited. At minimum, a direct comparison against GCD (which is publicly available) and GoLLIE (which achieves "zero DR violations" per the related work section) would significantly strengthen the paper.

**Minor:**

- **(m1) Statistical testing is incomplete for violation rates.** Bootstrap CIs are provided for F1 metrics but not for violation rate changes. The core claims are about DR reduction, yet no significance test or CI is reported for these changes. At n=551 (SciERC) and n=998 (DocRED), the sample sizes are large enough that most changes would be significant, but this should be stated rather than assumed.

- **(m2) WikiEvents EE fine-tuning evaluation is underpowered.** The official test split has only 20 documents (194/20/20 split). The paper acknowledges "per-document variance is high (Arg-F1 std/mean > 0.5), confirming sufficient power to detect violation elimination but not small F1 differences." With n=20, the F1 shift CIs are extremely wide, making the fine-tuning composability claim for EE essentially unverifiable for performance metrics.

- **(m3) Parse rate drops under constrained decoding are not fully analyzed.** Qwen WikiEvents: 88.6% to 83.7%; Llama WikiEvents: 91.9% to 84.1%. These 5--8pp parse rate drops mean the method causes some documents to produce unparseable output. The violation rates are computed over parsed documents only, which could introduce a selection bias (the unparseable documents may have been the most constrained ones).

- **(m4) 70B uses AWQ-INT4 quantization, confounding the scale analysis.** The paper reports 70B results using AWQ-INT4 but does not discuss how quantization affects constraint enforcement. Quantized logits may have different distributional properties than full-precision logits, potentially affecting the mask intersection behavior. The 70B zero-shot results (DR=0% on both datasets) could partly reflect quantization effects on logit distributions rather than pure scale effects.

- **(m5) SciERC and DocRED constraints are empirically derived, not from formal ontologies.** This is a disconnect with the "ontology" framing. Only WikiEvents uses a formal ontology (KAIROS). The paper's title and framing emphasize "ontology constraints" but 2 of 3 datasets use data-derived constraints with 99%+ but not 100% coverage.

- **(m6) The violation landscape study (Section 3 / setup) is conducted only with Qwen3-8B for the detailed per-relation analysis.** The claim that "violation rate correlates with constraint tightness rather than ontology size" is supported by only 2 data points (SciERC vs. DocRED) for the ontology size comparison. The per-relation analysis is single-model.

---

### 6. Questions for Authors

1. **70B LoRA placeholders:** Will the 70B LoRA results be available before the review period ends? What is the estimated timeline? If these results deviate from the "scale-independent" prediction, how would the narrative change?

2. **Mistral exclusion:** You exclude Mistral from the dual-factor analysis due to "poor entity typing." Is there a principled threshold for when OntoCoDec is expected to work vs. not? The current ET>5% criterion is post-hoc. Could you provide guidance on what model characteristics predict successful constraint enforcement?

3. **GoLLIE comparison:** You report that GoLLIE-7B achieves "zero DR violations" on SciERC but with R-F1=0.0 and 46% empty output. Did you run GoLLIE yourself, or are these numbers from the original paper? A direct head-to-head on the same evaluation protocol would be informative.

4. **CF severity in practice:** You argue CF violations are "soft errors" vs. DR's "hard errors." Have you measured the downstream impact? For instance, if the extracted triples are used for KG construction, how many spurious entity type assignments propagate?

5. **Constraint table construction:** How sensitive are results to the specific training-set derived constraint table? If you used a different cutoff for rare type pairs, how would violation rates change? The 33% of residual FT violations from "schema coverage gaps" suggest this is a meaningful parameter.

6. **Parse failure selection bias:** For WikiEvents, you report violation rates over parsed documents only (83.7--88.6% parse rate under S1). What is the violation profile of the 12--16% unparseable documents? Could you provide a sensitivity analysis that assumes worst-case violations for unparseable documents?

---

### 7. Missing Experiments or Analysis

1. **Direct experimental comparison with GCD, BoostCD, or GoLLIE.** The trie-only ablation is not a substitute for running the actual baselines. GCD code is publicly available.

2. **Bootstrap CIs for violation rates.** Core claims are about DR/RV/ET reduction, but only F1 has statistical testing.

3. **Seed variance for the main results.** The seed variance analysis is only for LoRA fine-tuned SciERC (Table in Appendix). Zero-shot results, DocRED results, and WikiEvents results have no variance analysis.

4. **Cross-lingual evaluation.** The Limitations section acknowledges this gap. Given the tokenizer-dependent continuation masking mechanism, even one non-English dataset would strengthen the contribution.

5. **Ablation of constraint table coverage.** The 99%+ coverage is presented as sufficient, but an ablation showing how violation rates change with 95%, 98%, 100% coverage tables would quantify the impact of schema completeness.

6. **Analysis of parse failure content.** The 5--8pp parse rate drop under constrained decoding is concerning. An analysis of what these failures look like (truncation? malformed JSON? empty output?) would help assess whether the method is causing harm in these cases.

7. **WikiEvents Argument F1 under fine-tuning.** The paper reports violation elimination but Arg-F1 shifts within +/-1.1pp on n=20 documents. A power analysis showing what effect size is detectable at n=20 would clarify the evidential weight.

---

### 8. Overall Assessment: 3.0 (Findings)

**Rationale:**

The paper addresses a real and under-studied problem (ontology constraint violations in LLM-based IE), proposes a technically sound two-layer framework, and provides an unusually thorough experimental evaluation. The violation landscape study is a genuine empirical contribution, the ablation design is exemplary, and the honest treatment of the CF trade-off is commendable.

However, several issues prevent a Conference (4.0) recommendation:

(a) The 70B LoRA results -- a claimed contribution -- contain placeholder values, indicating incomplete experiments at submission time. This is a significant completeness gap.

(b) The lack of direct experimental comparison with existing constrained generation methods (GCD, BoostCD, GoLLIE, IterGen) is a notable omission for a methods paper. The paper positions itself relative to these approaches through discussion and ablation-as-proxy, but never runs them.

(c) The CF trade-off is substantial in the zero-shot setting (the paper's primary evaluation mode), with Total violations (DR+CF) sometimes comparable to unconstrained. The method's value proposition is clearest in the fine-tuned setting, but this is where baseline violations are already low (0.5--2%), making the marginal benefit smaller.

(d) Effectiveness is strongly model-dependent: excellent for calibrated models (Qwen, Llama), limited for Mistral. The paper's "model-agnostic" framing overstates the generality.

(e) The contribution is primarily engineering (applying known techniques -- XGrammar + logit masking -- to a new domain) rather than fundamentally novel. Proposition 1 formalizes a known intuition. The enabling dependency between layers, while clearly demonstrated, follows naturally from the decomposition.

The paper would be a solid Findings paper. To reach Conference, it would need: complete 70B results, at least one head-to-head baseline comparison, and a more calibrated set of claims that reflects the method's strong model-dependence and CF trade-off. The experimental thoroughness and honest analysis are genuine strengths that a round of revision could build on.

**Confidence:** 4/5 (high -- I read the full paper including all appendices).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87edf30-6051-4194-8cef-35e920eb5721",
  "isSidechain": true,
  "agentId": "abaa6e03a45e8148b",
  "requestId": "req_011CbH8bMGiVwYBy1C6uMbta",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dbc2956-04ad-4aa0-9f05-db6bb8f9ba39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "5cda2c76-b1bb-4b5e-b780-c4d3c1c78b32",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6CL1VRwbaNdk56HuHRa8K",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22711,
      "cache_read_input_tokens": 92835,
      "output_tokens": 4314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4314,
          "cache_read_input_tokens": 92835,
          "cache_creation_input_tokens": 22711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22711,
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
