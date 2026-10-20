# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus: **Novelty and Related Work**. Score on a 6-point scale (1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-acf141a1713b1b57e.jsonl`
- **Structured JSON:** [`1f268f37bb062163fac0.json`](../../sessions/1f/1f268f37bb062163fac0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

66 recorded events

### User

_source line 1 · 2026-05-16T02:45:15.953Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus: **Novelty and Related Work**. Score on a 6-point scale (1=Strong Reject, 6=Strong Accept), targeting ~25% acceptance rate.

## Paper Summary
**Title:** OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints

The paper addresses ontology type constraint violations in LLM-based information extraction (IE). It makes three contributions:
1. **Violation landscape study**: First systematic measurement showing 15–26% of LLM-generated triples violate domain/range type constraints across 2 datasets × 2 models. Key finding: violation rate driven by constraint tightness (τ), not ontology size.
2. **OntoCoDec framework**: Two composable constraint layers for autoregressive decoding:
   - Grammar layer: CFG-based (builds on existing grammar-constrained decoding like XGrammar), enforces structural/vocabulary validity
   - Semantic layer: Novel stateful entity registry with dynamic logit masking for cross-field domain/range constraints
   - Composed via bitwise AND of token masks; graceful degradation (falls back to grammar-only when intersection is empty)
3. **Extensive evaluation**: 2 datasets (SciERC 7 relations, DocRED 96 relations) × 2 models (Qwen3-8B, Llama-3.1-8B) × multiple configs, with ablation studies and bootstrap CIs.

## Key Technical Details

**Constraint tightness τ_r = 1 - (|dom(r)| · |ran(r)|) / |E|²**: Measures how restrictive a relation's type constraints are. Higher τ → more violations.

**Grammar layer**: Compiles IE ontology into CFG enforcing (1) valid JSON structure, (2) entity types ∈ E, (3) relation names ∈ R. Standard grammar-constrained decoding applied to IE.

**Semantic layer (TypeConstraintProcessor)**: Maintains stateful entity registry during generation. When decoder reaches a type field in a triple: identifies current relation r → looks up dom(r) or ran(r) → constructs semantic mask M_semantic allowing only tokens consistent with valid types. This is the novel component.

**Composition**: M = M_grammar ∧ M_semantic. When M_grammar ∩ M_semantic = ∅ (high-tightness scenarios), falls back to M = M_grammar only.

**Decidability taxonomy (§4.4)**: Classifies IE constraints as (a) purely local (grammar layer), (b) prefix-decidable with state (semantic layer), (c) truly non-local (forward coreference — out of scope).

## Key Results
- Zero-shot: DR reduced 90-99% on SciERC, 45-90% on DocRED, at zero or positive F1 impact
- FT composability: FT handles bulk DR reduction (96-98%), OntoCoDec provides residual guarantee (additional 58-69%)
- CF trade-off: Semantic layer introduces cross-field consistency violations (up to 9.90% on SciERC zero-shot, 1.5-2.0% on DocRED FT)
- Post-hoc filtering comparison: Post-hoc rejects 48.1% of triples vs 0% for OntoCoDec

## Related Work Covered in the Paper (§7)
1. **Constrained Decoding for Structured Output**: XGrammar and related systems for JSON/code/SQL. Paper claims OntoCoDec extends with semantic layer for cross-field constraints.
2. **LLM-Based Information Extraction**: Recent zero/few-shot IE work. Paper claims violation landscape study fills a gap.
3. **Type-Constrained Knowledge Graph Completion**: KGC uses type constraints but operates over fixed entity inventories; IE requires constraint enforcement during open-ended text generation.
4. **Post-Hoc Validation**: Filtering/re-ranking after generation. Paper's experiments (§5.3) show OntoCoDec's advantage.

## Your Review Task

Evaluate the following aspects in detail:

### 1. Novelty Assessment
- How novel is the problem formulation (violation landscape study)?
- How novel is the technical approach (grammar + semantic two-layer architecture)?
- Is the grammar layer just standard grammar-constrained decoding applied to IE? What's new?
- Is the semantic layer (stateful entity registry + dynamic logit masking) a significant technical contribution?
- Is the composition mechanism (bitwise AND + graceful degradation) novel or straightforward?
- Is the constraint tightness metric (τ) a genuine contribution or obvious formalization?
- Is the decidability taxonomy (§4.4) substantive or superficial?

### 2. Positioning Against Related Work
- Is the related work coverage comprehensive? Any major missing references?
- Missing areas to consider:
  - Ontology-guided NER/RE (e.g., using ontology structure during training or inference)
  - Structured prediction with constraints (CRFs, structured perceptrons with hard constraints)
  - Neuro-symbolic IE approaches
  - Schema-guided dialogue/generation
  - Constrained beam search variants
  - Type-aware entity linking
- Does the paper clearly differentiate from KGC type constraint work?
- Is the XGrammar/grammar-constrained decoding baseline fairly represented?

### 3. Significance and Impact
- How important is the problem of type constraint violations in LLM-based IE?
- Is OntoCoDec likely to be adopted in practice?
- Does the work open new research directions?
- Is the scope (2 datasets, 2 models, 8B only) sufficient for the claims?

### 4. Clarity of Contributions
- Are the contributions clearly delineated?
- Is it clear what is new vs. what is standard?

### 5. Weaknesses from Novelty/Related Work Perspective
- Is there risk this is seen as "just applying grammar-constrained decoding to IE + adding a logit mask"?
- The CF trade-off — does it undermine the core contribution?
- Limited to closed-schema IE — how significant is this limitation?

Provide your review in this format:
```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
[Numbered list]

### Weaknesses
[Numbered list]

### Questions for Authors
[Numbered list]

### Missing Related Work
[If any]

### Detailed Assessment
[Paragraph-level analysis of novelty and positioning]

### Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "969be383-21a9-4f81-b3fe-ed11b51650d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T02:45:15.955Z_

```json
{
  "parentUuid": "969be383-21a9-4f81-b3fe-ed11b51650d6",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
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
  "uuid": "851140c1-9edb-4dfe-8495-ad7db2a40b16",
  "timestamp": "2026-05-16T02:45:15.955Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T02:45:18.804Z_



I'll start by thoroughly exploring the codebase to understand the paper, its claims, and the related work before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "851140c1-9edb-4dfe-8495-ad7db2a40b16",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UridYk8iBtaryw4Mck",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "1f0365cb-53d9-491f-acba-739410ca8806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQKDQ6UudVbt4Dj1PC5w32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10016,
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

_source line 4 · 2026-05-16T02:45:19.272Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XozBkLVL6g9gaTfZpULeB4`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f0365cb-53d9-491f-acba-739410ca8806",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UridYk8iBtaryw4Mck",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "8bf7b911-fe0c-4473-8470-bf885464e36f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQKDQ6UudVbt4Dj1PC5w32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10016,
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

_source line 5 · 2026-05-16T02:45:19.437Z_

<details><summary>↩ Tool result · `toolu_01XozBkLVL6g9gaTfZpULeB4`</summary>

```text
AGENTS.md
ROADMAP.lock
ROADMAP.md
analyze_cf_fallback.py
analyze_cf_violations.py
artifacts
checkpoints
compiler
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
logs
memory.md
paper_framing.md
registry.lock
registry.yaml
report.md
run_extraction_docred.py
scripts
study_status.lock
task_context
violation_checker.py
violation_checker_docred.py
writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bf7b911-fe0c-4473-8470-bf885464e36f",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "e1ce4841-2000-454c-a607-0d1acffc8d81",
  "sourceToolAssistantUUID": "8bf7b911-fe0c-4473-8470-bf885464e36f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T02:45:19.670Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0148xKjvxwMiK2XPrWGoxCac`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ -type f | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1ce4841-2000-454c-a607-0d1acffc8d81",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UridYk8iBtaryw4Mck",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "b0e4ae17-56ab-44d1-a5a7-71a5584ad53d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQKDQ6UudVbt4Dj1PC5w32",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 0,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10016
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 185,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 10016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10016,
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

_source line 7 · 2026-05-16T02:45:19.781Z_

<details><summary>↩ Tool result · `toolu_0148xKjvxwMiK2XPrWGoxCac`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig2_per_relation_dr.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig2_per_relation_dr.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/gen_fig2_per_relation_dr.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/gen_fig1_overview.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig3_ablation_layers.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig3_ablation_layers.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig1_overview.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper/fig1_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.registry_22drwdpt.tmp
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/compiler/ontology_compiler.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/compiler/tests/test_e2e.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/compiler/tests/__init__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/compiler/test_type_mask.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/compiler/__init__.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/compiler/type_mask_processor.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/analyze_cf_fallback.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/dream_registry.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_docred_minimal_result_20260513T214033_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_first_token_masking_20260513T193339.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_cf_fallback_logging_20260515T133411_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_ops_check_docred_eval_completion_20260515T232506.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_w5_docred_sft_data_gen_20260515T175442_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_w1_cf_registry_consistent_fallback_20260515T095943_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_write_section6_relwork_merge_20260514T183725_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_llama_docred_maxtoken_test_20260515T063113.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_w1_cf_fallback_scierc_pilot_20260515T144938_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_d009-llama-prep_20260514T083659.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_phase2_docred_semantic_only_20260514T141517.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_validate_llama_dryrun_20260514T104630.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_ops_check_full_s1_fallback_stats_20260514T042645_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_docred_lora_eval_prep_20260515T182621.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_w5_qwen_docred_lora_training_20260515T174919_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_cf_fallback_logging_20260515T133411.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_infra_gpu1_emergency_cleanup_20260513T221548_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_experiment_posthoc_filtering_baseline_20260514T181438.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_w5_docred_sft_data_gen_20260515T175442_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_w5_llama_lora_scierc_constrained_eval_20260515T180056.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_llama_docred_dr_residual_20260515T063059.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_ops_check_docred_progress_20260514T022901_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_w5_llama_lora_scierc_training_20260515T163426_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_docred_minimal_completion_20260513T213630_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_paper_section6_relwork_revision_20260514T054538.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_emergency_llama_scierc_full_s1_dedup_20260514T141055.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_diagnose_phase2_scierc_grammar_only_20260513T224135_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_llama_docred_unconstrained_20260514T194008_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_table_inconsistency_20260515T140337_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_infra_cleanup_and_verify_20260513T180057_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_llama_scierc_unconstrained_20260514T134815_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_s2_pilot_f1_investigation_20260513T234025_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_docred_minimal_result_20260513T214033.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_paper_reference_audit_relwork_20260514T054831.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_llama_lora_unconstrained_eval_monitor_20260515T172703_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_paper_section6_relwork_outline_20260514T053338.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_docred_sft_data_prep_20260515T172731_retry1.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_phase1_compiler_refinement_20260513T193848.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_review_pre_submission_checklist_20260515T062759.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_ops_cleanup_gpu1_orphans_20260513T235434.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_paper_w5_composability_w1_analytical_20260515T170813.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_ops_launch_docred_grammar_only_20260514T015357_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analyze_llama_bootstrap_ci_20260514T222348.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_paper_section2_background_20260514T061320_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_retry_phase2_scierc_full_s1_semantic_only_20260513T234912_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_ssh_docred_progress_check_20260514T061257.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_literature-docred-compare_20260514T083650.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_eval_scierc_phase2_v2_20260514T014906.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_verify_latex_compile_20260514T225756.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_fix_et_triplecount_and_rerun_all_20260514T182039_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_docred_batch_resume_20260513T191555.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_mvp_docred_20260513T173912.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analysis_w1_cf_fallback_pilot_detailed_20260515T150442_retry2.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_ops_check_full_s1_fallback_stats_20260514T042645.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_check_docred_eval_status_20260515T230147.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_analyze_docred_full_s1_fallback_20260514T083432_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_fix_llama_bootstrap_v2_20260514T224058.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_code_phase2_constrained_extraction_20260513T210741_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_knowledge_invariant_paper_notes_20260514T043434.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_research_constrained_decoding_literature_20260513T200558.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0e4ae17-56ab-44d1-a5a7-71a5584ad53d",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "00e90af0-92e8-4d3a-bf87-bacfac1d4eae",
  "sourceToolAssistantUUID": "b0e4ae17-56ab-44d1-a5a7-71a5584ad53d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T02:45:22.963Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EowcAUxxv6v78UKPtm2BfV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00e90af0-92e8-4d3a-bf87-bacfac1d4eae",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5Us18jKfU2iSZ4xgiq7",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "725beb7e-d23b-4692-8722-22d30c498787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgNFHf2jxEywLDbPLgqyNz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5596,
      "cache_read_input_tokens": 10016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5596,
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

_source line 9 · 2026-05-16T02:45:22.971Z_

<details><summary>↩ Tool result · `toolu_01EowcAUxxv6v78UKPtm2BfV`</summary>

```text
1	# Handover — 2026-05-16
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| w5_qwen_docred_lora_constrained_eval | Fine-tuned Qwen3-8B DocRED LoRA + OntoCoDec constrained eval — 验证 composability：约束解码在 fine-tuned Qwen DocRED 上是否仍能消除残余 DR 且不损 R-F1 | — | — | — |
9	| w5_llama_docred_lora_constrained_eval | Fine-tuned Llama-3.1-8B DocRED LoRA + OntoCoDec constrained eval — 验证 composability：约束解码在 fine-tuned Llama DocRED 上是否仍能消除残余 DR 且不损 R-F1 | — | — | — |
10	
11	## 待处理
12	- w1_cf_fallback_llama_scierc（准备中）
13	- w1_cf_fallback_llama_docred（准备中）
14	- w5_llama_docred_sft_data_gen: Generate Llama-3.1-8B-Instruct format DocRED SFT train/dev JSONL — prerequisite for Llama DocRED LoRA fine-tune (composability matrix Llama×DocRED cell)（准备中）
15	
16	## 近期结论
17	- **w5_qwen_docred_lora_unconstrained_eval** (success): Fine-tuned Qwen3-8B DocRED LoRA unconstrained eval — 获取 fine-tuned baseline DR/R-F1，与 constrained eval 对比计算 composability delta ← 基于 w5_qwen_docred_lora_training
18	- **w5_llama_docred_lora_unconstrained_eval** (success): Fine-tuned Llama-3.1-8B DocRED LoRA unconstrained eval — 获取 fine-tuned baseline DR/R-F1，与 constrained eval 对比计算 composability delta ← 基于 w5_llama_docred_lora_training
19	- **w5_qwen_docred_lora_training** (success): Qwen3-8B LoRA fine-tune on DocRED — 填补 Qwen DocRED composability 2×2 matrix 的 FT 行。预期：(1) LoRA 后 E-F1/R-F1 大幅提升；(2) 残余 DR > 0% 证明 OntoCoDec 在 DocRED FT 上仍有 composability 价值。
20	
21	## 趋势
22	成功 32 / 负向 1 / 失败 0 / 共 35
23	
24	## 下一步
25	（无活跃 idea，请通过 ideas.md 添加）
26	
27	## 资源状态
28	westd-16980: 无 GPU 信息
29	
30	## 告警
31	- mvp_phase0_docred_schema_r2: 已被终止 — unknown
32	- w1_cf_fallback_docred: 已被终止 — unknown
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "725beb7e-d23b-4692-8722-22d30c498787",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "02a09404-5c6b-4962-be47-58a42752c09c",
  "sourceToolAssistantUUID": "725beb7e-d23b-4692-8722-22d30c498787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T02:45:23.432Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PqfKCJoJz8Lzwhxx32w6qe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02a09404-5c6b-4962-be47-58a42752c09c",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5Us18jKfU2iSZ4xgiq7",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "ad3a5861-2fb1-4290-84ff-5bbe52df81f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgNFHf2jxEywLDbPLgqyNz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5596,
      "cache_read_input_tokens": 10016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5596,
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

_source line 11 · 2026-05-16T02:45:23.440Z_

<details><summary>↩ Tool result · `toolu_01PqfKCJoJz8Lzwhxx32w6qe`</summary>

```text
1	# OntoCoDec — Paper Framing
2	
3	## Target Venue
4	EMNLP 2026 (ARR submission May 25, 2026)
5	
6	## Title
7	OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
8	(D015: "Near-Complete" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)
9	
10	## Core Insight
11	LLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.
12	
13	**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:
14	- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)
15	- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])
16	- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。
17	- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。
18	
19	## Core Claims
20	
21	### Claim 1 (Empirical): Violation Landscape
22	LLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).
23	
24	**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.
25	
26	**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。
27	
28	**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.
29	
30	### Claim 2 (Empirical): Prompt Insufficiency
31	Schema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:
32	- Overall: 15.4% → 5.78% (-62.4%), still above 5%
33	- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)
34	- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses
35	
36	**Narrative**: This is NOT about "5.78% barely above 5%". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.
37	
38	### Claim 3 (Methodological): Composable Constraint Framework
39	OntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:
40	1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)
41	2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking
42	
43	The two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT "synergistic" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.
44	
45	The two layers compose via bitwise AND of token masks. Recommended framing: "Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor."
46	
47	**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):
48	When $M_{semantic} \cap M_{grammar} = \emptyset$, the system falls back to grammar-only control.
49	
50	**关键量化数据（Reviewer 从日志挖掘）**:
51	- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**
52	- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**
53	- DocRED fallback 频率是 SciERC 的 **5.3×**
54	- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）
55	
56	**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。
57	
58	**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 "Constraint Coverage" 指标（semantic masking 实际生效的 token 比例）。这把 "10.19% DR 残余" 从弱点变成可量化分析的 finding。Frame as "engineering robustness" in §4; fallback 频率 + tightness 作为 §5 定量分析。
59	
60	**Decidability taxonomy**: Constraints classified by prefix-decidability:
61	- (a) Purely local: entity type ∈ vocabulary (grammar layer)
62	- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)
63	- (c) Truly non-local: forward coreference — out of scope for forward-only decoding
64	
65	### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation
66	- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.
67	- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.
68	
69	**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.
70	
71	⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).
72	
73	## Anticipated Reviewer Concerns
74	
75	### C1: "5.78% is barely above 5% — threshold is arbitrary"
76	**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.
77	
78	### C2: "Why not just post-hoc filter?"
79	**Response (D013, 实验结果已出)**:
80	
81	Post-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。
82	
83	**论文 framing（不以 F1 论高低，多维对比）**:
84	1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。
85	2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。
86	3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。
87	4. **Precision trade-off（诚实承认）**: "Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters."
88	
89	数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。
90	
91	**Reviewer 补充发现（D013 后）**:
92	5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。
93	6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——"prevent vs detect" 核心论据的具体数据。
94	7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。
95	
96	### C3: "Bitwise AND of two masks is not novel"
97	**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.
98	
99	### C4: "Evaluate-for violation rate increases with schema-informed prompt"
100	**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior ("Method X evaluates for Task Y" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just "harder instances" — it's an active interference between prompt-level constraint signals and the model's learned type associations.
101	
102	**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.
103	
104	### C5: "Only tested on one model (Qwen3-8B)"
105	**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：
106	- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS
107	- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)
108	- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)
109	
110	**Cross-model claim 指导（Reviewer 专项评估）**:
111	- ✅ 可声明："OntoCoDec generalizes across model families without code modification"（程序性事实，铁证）
112	- ❌ 不可声明："consistently achieves the same reduction rate"（仅 2 模型，不足以量化声明）
113	- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。
114	- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。
115	- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。
116	- 等 llama_docred_full_s1 出来后定最终 claim 措辞。
117	
118	### C6: "Constrained decoding degrades generation quality (CRANE, Structure Snowballing)"
119	**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:
120	
121	**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).
122	**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).
123	
124	**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。
125	- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。
126	- Frame as: "On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent."
127	- 不升级为 core claim，但如实报告。
128	
129	### C7: "Your method trades DR violations for CF violations (cross-field consistency)"
130	**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:
131	
132	**CF 子类型分析（根因已确认）**：
133	- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)
134	- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)
135	- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差
136	
137	**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。
138	
139	**论证层次**：
140	1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint
141	2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference
142	3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug
143	4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)
144	
145	**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 "CF 是 semantic type enforcement 的系统性副作用" 提供干净的消融证据。
146	
147	**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。
148	
149	**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。
150	
151	### C8: "Absolute F1 is too low (~8%) — results are not meaningful"
152	**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: "We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance."
153	
154	## Paper Structure (Draft)
155	1. Introduction: Violation landscape motivation + composable constraint framework overview
156	2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure
157	3. Violation Landscape Study (Phase 0 empirics — independent contribution)
158	4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies
159	5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based
160	6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)
161	7. Conclusion
162	
163	## Claim Calibration (per Reviewer assessment)
164	
165	**Safe to claim (sufficient evidence from Phase 2)**:
166	- "First systematic study of ontology constraint violations in LLM-based IE"
167	- "Violation rate correlates with constraint tightness, not ontology size" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)
168	- "Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost" ✅ Phase 2 confirmed
169	- "Two-layer architecture provides complementary coverage — grammar enables semantic" ✅ Ablation confirmed
170	- "Prompt-level intervention scales poorly with ontology complexity" ✅ SciERC ↓62% vs DocRED ↓32%
171	
172	**Claim with caution**:
173	- "Near-complete type-valid IE" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to "Near-Complete"
174	- "Principled framework applicable to arbitrary IE ontologies" — validated on 2 datasets + 1 model only
175	- "F1 improvement" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升
176	- "CF reveals type system ambiguity" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示"因为是 type ambiguity 所以 CF 可接受"
177	
178	**Do NOT claim**:
179	- "General infrastructure for IE" — only zero-shot extraction validated
180	- "State-of-the-art" — F1 is control variable, not optimization target (see C8)
181	- "Synergistic effect" — mechanism is enabling dependency, not mutual amplification (see Claim 3)
182	- "S2 solves CF" or "S2 mitigates Structure Snowballing" — data shows S2 ≈ S1 on all metrics; position as architectural variant only
183	- "Pilot50 DR=0%" — small-sample artifact, full S2 has DR=0.97%
184	- "Grammar-first invariant" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim
185	- "Robust dual-layer composition across schema complexities" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim
186	
187	## Risk Ranking (ordered by reject probability)
188	
189	1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).
190	2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。
191	3. **Novelty perception** (MEDIUM): "PLDI'25 for code → OntoCoDec for IE" attack line. Must argue IE constraint structure differs fundamentally.
192	4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.
193	5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.
194	
195	## Critical Path to EMNLP Submission (May 25)
196	
197	- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅
198	- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)
199	- **May 14-15**: Llama DocRED 2 组实验 ✅ + Checker 修正 ✅ + post-hoc baseline ✅ + bootstrap CI ✅ + related work ✅
200	- **May 14-15**: D014 tightness claim 修订 + §5 cross-model subsection + abstract/conclusion 修正 (Agent 执行中)
201	- **May 15-17**: 全文校对 + Discussion 整合 + 最终数字确认
202	- **May 19**: 内部稿 → submit_paper_to_review
203	- **May 19-24**: Review 修改 + 最终提交
204	
205	**当前瓶颈**: 无技术 blocker。等 Reviewer 跨文件一致性审查 + 编译验证后即可 submit_paper_to_review。
206	
207	## Status
208	- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)
209	- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)
210	- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)
211	- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)
212	- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)
213	- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)
214	- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)
215	- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)
216	- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)
217	- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)
218	- Related work: ✅ 42 bib entries, 4 additions merged
219	- Dream 6/6 actions: ✅ All complete
220	- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)
221	- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)
222	- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)
223	- Paper compilation: ✅ 8 pages正文 + appendix
224	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad3a5861-2fb1-4290-84ff-5bbe52df81f6",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "529f2a21-05be-4c6e-8b8b-04686c53dbd5",
  "sourceToolAssistantUUID": "ad3a5861-2fb1-4290-84ff-5bbe52df81f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T02:45:24.051Z_

<details open><summary>🔧 Tool call — Read · `toolu_012tLc8vyXHqyBmfBGS9FitR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "529f2a21-05be-4c6e-8b8b-04686c53dbd5",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5Us18jKfU2iSZ4xgiq7",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "e256698b-84c8-450b-865e-17d8658c3c47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgNFHf2jxEywLDbPLgqyNz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5596,
      "cache_read_input_tokens": 10016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5596,
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

_source line 13 · 2026-05-16T02:45:24.640Z_

<details><summary>↩ Tool result · `toolu_012tLc8vyXHqyBmfBGS9FitR`</summary>

```text
1	# Idea Brief: Ontology-Faithful Information Extraction via Compiled Semantic Constraints: Automatic Ontology-to-Decoder Compilation with Forward-Only Type Masking
2	
3	
4	- **Idea ID**: `idea_011`
5	- **Created**: 2026-05-13
6	- **Approved**: 2026-05-13
7	- **Source**: foreign:be-idea-gen-0509-6
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026 — tight but feasible with focused entity+relation evaluation and phased timeline), AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026 — same cycle, lower tier alternative), EMNLP 2026 Insights from Negative Results Workshop (Budapest, Oct 2026 — fallback venue if Phase 0 yields low violation rates and the negative-result paper is better suited for a specialized workshop), AAAI 2027 (expected deadline: ~August 1, 2026 — allows complete evaluation including event stretch goal, full DocRED evaluation, and deeper ablations)
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.
14	
15	Direction: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.
16	
17	Contribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.
21	2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.
22	3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.
23	
24	Look for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.
25	
26	Tag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Generation Journey
29	
30	1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.\n\nDirection: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.\n\nContribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.\n2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.\n3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.\n\nLook for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.\n\nTag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].'
31	2. **Problem Discovery** (959s) — 发现 4 个研究方向
32	   - Structural Self-Consistency Scaling for Information Extraction
33	   - Provenance-Grounded Universal Information Extraction
34	   - Schema-Semantic Constrained Decoding for Information Extraction
35	   - Process Reward Models for Stepwise IE Verification
36	3. **Method Synthesis** (618s) — 完成: "Structural Self-Consistency Scaling for Information Extraction" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026), AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026; Nov 6-10 Hengqin, China), AAAI 2027 (abstract: Jul 25, paper: Aug 1, 2026; Feb 16-23 Montréal)
37	3. **Method Synthesis** (515s) — 完成: "Provenance-Grounded Universal Information Extraction" [top-tier] → EMNLP 2026 (ARR submission deadline: May 25, 2026; commitment deadline: August 2, 2026), AAAI 2027 (expected deadline ~late July 2026, based on AAAI-26 pattern of July 25/Aug 1), ICLR 2027 (expected deadline ~September 2026, based on ICLR 2026 pattern of Sep 24)
38	3. **Method Synthesis** (490s) — 完成: "Schema-Semantic Constrained Decoding for Information Extraction" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026), AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026), AAAI 2027 (expected deadline: ~August 1, 2026)
39	3. **Method Synthesis** (659s) — 完成: "Process Reward Models for Stepwise IE Verification" [solid] → EMNLP 2026 (ARR submission May 25, 2026 — very tight, stretch goal only), AACL 2026 (ARR submission May 25, 2026, commitment Aug 26, 2026), AAAI 2027 (submission Aug 1, 2026), ICLR 2027 (submission Sep 24, 2026), NAACL 2027 (submission Oct 16, 2026)
40	
41	## Core Problem
42	
43	Do LLM-based IE systems violate ontology type constraints (relation domain/range, cross-field entity type consistency) at rates sufficient to warrant decoding-time enforcement — and if so, can we automatically compile ontology schemas into efficient decoding-time constraint specifications that enforce semantic validity without degrading extraction accuracy? The first question is empirically unanswered: no prior work has systematically measured ontology constraint violation rates in LLM-based IE. We treat this quantification as a first-order contribution, with a Day 1 pilot study that establishes violation prevalence before committing engineering effort. If violation rates are non-trivial (>5%), the compiled constraint approach is justified. If rates are low (<5%), this is an equally important negative result establishing that modern instruction-tuned LLMs have internalized ontology constraints from pretraining data, and the community should not invest in decoding-time semantic enforcement.
44	
45	## Opportunity / Why Now
46	
47	LLM-based IE systems produce structurally valid but potentially semantically invalid outputs: structural validity (valid JSON, correct field names) is now reliably enforced by grammar-constrained decoding (Outlines, XGrammar-2, default in vLLM/SGLang since 2026), but no existing system enforces semantic validity — cross-field type constraints such as relation domain/range restrictions — during autoregressive generation. For instance, an ACE05 PHYS.Located relation requires a PER/GPE Arg-1 and a FAC/LOC/GPE Arg-2; a system that assigns two ORG entities produces structurally valid but semantically invalid output. Three converging developments create a timely opportunity. First, vLLM V1's well-documented LogitsProcessor API enables custom token-level interventions on (num_requests × vocab_size) tensors, and XGrammar-2's GrammarMatcher exposes a composable `fill_next_token_bitmask()` API that returns grammar-valid token masks, enabling external code to intersect grammar masks with additional semantic masks via bitwise AND — making decoding-time semantic enforcement practical without reimplementing grammar-constrained decoding from scratch. Second, The Format Tax (arXiv Apr 2026) demonstrates that prompt-level format-requesting instructions cause an average −3.9pp accuracy drop while decoder-level grammar masking contributes only −1.6pp additional loss across reasoning benchmarks — though critically, this was evaluated only on reasoning/writing tasks (MATH-500, GPQA, ZebraLogic, WritingBench) and not on IE. The recently published Lost in Formatting (Ravikumar et al., EACL 2026) strengthens the IE-specific relevance: across 280+ experiments spanning multiple IE benchmarks and models, changing only the output format shifts F1 by over 40%, demonstrating that the format–accuracy interaction is even more pronounced for IE than for reasoning — making the choice of constraint application point (prompt-level vs. decoder-level vs. two-pass) a first-order design decision for IE systems. Third, the landscape has matured along parallel axes but left a specific gap between post-hoc and decoding-time constraint enforcement: the LLM+ASP Workflow (Tran et al., ICLP 2025) demonstrates that ASP-based post-hoc type constraint checking substantially reduces false positives in LLM-based IE (713→482 FPs on SciERC), validating that type constraints improve extraction quality — but applies them only after generation, meaning type-violating outputs are produced then discarded rather than prevented; ODKE+ (Apple, Sep 2025) achieves 98.8% precision through soft ontology-guided prompting but without guaranteed type compliance; BoostCD/BoostIE (EMNLP 2025) shows that constrained and unconstrained decoding errors are complementary for closed IE but focuses on vocabulary membership rather than ontology type constraints and requires training a boosted combiner; DocRE-TCGL (Neural Networks, 2025) enforces entity type constraints at training time but not at inference; and EnriCo (arXiv 2024) uses ASP solvers for constrained inference on discriminative models but is incompatible with autoregressive LLM generation. No existing system compiles full ontology type constraints (entity type validity, relation domain/range, cross-field type consistency) into finite-state specifications applied during autoregressive decoding. This gap — between post-hoc/soft/training-time constraints and hard decoding-time guarantees — is precisely what compiled semantic constraints fill. The LLM+ASP result is particularly motivating: it demonstrates that type constraints improve IE quality but leaves open whether enforcing them during generation (preventing violations) outperforms enforcing them after generation (filtering violations).
48	
49	The practical case for decoding-time enforcement over post-hoc filtering is strongest in three IE-specific deployment contexts. (a) **Streaming/real-time extraction pipelines** — in applications such as live news monitoring, social media analysis, or clinical decision support, extraction results are consumed as they are generated; post-hoc rejection wastes generation latency and cannot provide valid alternatives without costly re-generation, while decoding-time enforcement produces valid outputs in a single pass. (b) **Batch knowledge graph population** — when processing millions of documents (as in ODKE+'s 9M Wikipedia page pipeline), post-hoc rejection of type-violating outputs requires re-generation at ~2× cost, and for high-cardinality ontologies like DocRED's 96 Wikidata relations, the post-hoc rejection rate could be substantial (each relation has specific subject-type and value-type constraints), making decoding-time enforcement more compute-efficient at scale. (c) **Safety-critical domains** — in biomedical knowledge extraction (drug-gene interactions, adverse event detection), legal document processing, and regulatory compliance pipelines, even a single ontology-violating extraction can propagate errors through downstream reasoning systems; these domains require guaranteed type compliance rather than statistical compliance, paralleling how type-safe programming languages provide formal guarantees even when most code would run correctly without them. The quantification of violation rates, regardless of direction, is itself a first-order contribution that no prior work provides.
50	
51	## Landscape (SOTA & Limitations)
52	
53	**Grammar+semantic constraint paradigm (code generation).** Synchromesh (Poesia et al., ICLR 2022) introduced two-layer Completion Engines combining syntactic and semantic constraints for code generation (SQL, Vega-Lite, SMCalFlow). IterGen (Ugare et al., ICLR 2025) extended this with backtracking via KV cache state restoration when semantic callbacks detect violations, achieving 18.5% improvement over forward-only grammar-guided generation. Both require manual implementation of domain-specific constraint logic. Neither addresses IE ontology constraints or automatic constraint compilation from schema definitions.
54	
55	**Constrained decoding for IE (vocabulary-level).** GenIE (Josifoski et al., NAACL 2022) pioneered bi-level constrained generation for IE with structural constraints and prefix trie vocabulary constraints, but enforces only entity/relation name validity, not cross-field type consistency. Geng et al. (EMNLP 2023) demonstrated input-dependent grammars for closed IE on Wikidata. Schmidt & Cimiano (Frontiers AI 2024) applied grammar-constrained decoding to clinical IE. Lazy-k (Hemmer et al., EMNLP 2023) explored constrained decoding for token classification IE. SciDC (arXiv Apr 2026) introduced multi-layer decoding constraints for scientific domains using hand-crafted rules. Vukovic et al. (SIGDIAL 2024) adapted chain-of-thought decoding with ontology-constrained output spaces for dialogue relation extraction, using trie-based prefix matching to restrict generated relations to valid ontology terms — conceptually related to our approach but targeting task-oriented dialogue ontologies rather than IE schemas, using CoT branching rather than logit masking, and not handling cross-field type constraints (relation domain/range). None enforce cross-field type constraints (relation domain/range, event argument role-filler types).
56	
57	**Constrained+unconstrained combination for IE.** BoostCD/BoostIE (EMNLP 2025) is a key recent work combining constrained and unconstrained decoding via learned boosting for closed IE. Phase 1 decodes each input twice (constrained + unconstrained on FlanT5-base, ~250M params); Phase 2 trains an autoregressive boosted model to combine predictions, exploiting error complementarity — constrained decoding suffers from forced token selection while unconstrained produces 60% unrelated triplets and 9% entity misclassification errors. However, BoostCD (a) focuses on vocabulary membership constraints (entity must appear in a KB), not ontology type constraints (entity must match a relation's domain/range type); (b) requires training a separate boosted combiner model; (c) targets small encoder-decoder models, not modern instruction-tuned LLMs; and (d) does not automatically compile constraints from ontology definitions.
58	
59	**Post-hoc constraint checking for LLM-based IE.** The LLM+ASP Workflow (Tran et al., ICLP 2025; arXiv 2508.12611, updated Jan 2026) is the most direct post-hoc competitor to our approach. It combines LLM generation (GPT-4o) with ASP-based consistency checking for joint entity-relation extraction, using rules like ok_type(S,E,F,R) to verify that relation arguments satisfy domain/range type specifications. On SciERC with only 10% training data, it achieves 35.37% RE F1 (2.5× improvement over baseline), with the ASP checker reducing false positives from 713 to 482. Evaluated on CoNLL04, SciERC, and ADE, it demonstrates that type constraint checking substantially improves extraction quality, particularly for datasets with richer type specifications. However, LLM+ASP operates strictly post-hoc: the LLM generates unconstrained outputs, then the ASP checker filters violations. This means (a) type-violating outputs are produced then discarded rather than prevented, wasting generation compute on invalid outputs — particularly costly in batch KG population pipelines processing millions of documents; (b) the approach cannot redirect the model toward valid alternatives during generation — it can only accept or reject, whereas logit masking redistributes probability mass to type-valid alternatives; (c) it relies on GPT-4o (a closed-source ~1.76T parameter model), making cost and reproducibility concerns for batch processing; and (d) the ASP rules are manually specified per dataset rather than automatically compiled from ontology definitions. OntoCoDec addresses all four limitations: decoding-time enforcement prevents violations rather than filtering them, logit masking redirects probability mass to valid alternatives, it targets open-weight models (Qwen3-8B, Llama-3.1-8B) for reproducibility, and constraints are automatically compiled from schema definitions.
60	
61	**Constrained inference for joint IE (non-generative).** EnriCo (Zaratiana et al., arXiv Apr 2024) uses Answer Set Programming (ASP) to enforce entity type constraints for joint entity-relation extraction on discriminative span-classification models. On ACE05, constrained decoding improved relation F1 by ~1 point (69.1 vs. ~68). This is the closest prior work to our constraint enforcement goal on ACE05, but uses ASP solvers incompatible with GPU-accelerated batch serving, operates on discriminative models rather than autoregressive LLMs, and requires manual constraint specification per dataset.
62	
63	**Soft ontology guidance (prompt-based).** ODKE+ (Apple, arXiv Sep 2025) is a production-grade system that dynamically generates ontology snippets tailored to each entity type for LLM-based knowledge extraction. Processing 9M Wikipedia pages across 195 predicates, it extracts 19M facts at 98.8% precision, demonstrating impressive production scalability. However, soft prompting cannot guarantee type compliance — the model may still generate type-violating outputs. ODKE+ represents the 'soft constraint' pole: high precision via guidance, but no formal guarantee of ontology validity.
64	
65	**Training-time schema compliance.** GoLLIE (Sainz et al., ICLR 2024) fine-tunes Code-Llama to follow annotation guidelines encoded as Python class schemas, achieving strong supervised results on ACE05 (RE F1 = 63.6/67.5/70.1 at 7B/13B/34B). GoLLIE's published Code-Llama checkpoints are available on HuggingFace but are architecture-specific — porting to Qwen3-8B or Llama-3.1-8B would require 40-80 H100-hours of fine-tuning with non-trivial architecture adaptation. Whether decoding-time constraints complement or substitute GoLLIE-style training-time schema internalization is an open empirical question addressable through comparison against GoLLIE's published numbers. DocRE-TCGL (Neural Networks, 2025) enforces entity type constraints during training for document-level RE via a Type-Constrained Graph (TCG) encoding permitted entity-type/relation-type combinations and a Type-Constrained Loss (TCL). Evaluated on DocRED and DWIE, it demonstrates that type-aware training improves quality under long-tail and multi-label setups (up to +6.26%). Ru-LLM (Zhang et al., NLPCC 2025) learns logical rules via Monte Carlo Tree Search to constrain LLM reasoning for document-level RE on DocRED, demonstrating rule-based frameworks can outperform implicit reasoning approaches. SH-ETRs (Expert Systems 2025) learns soft-hard entity type rules for DocRE. All are training-time approaches that require retraining for each ontology change and do not guarantee inference-time compliance.
66	
67	**Constrained decoding quality degradation.** The Format Tax (arXiv Apr 2026) systematically decomposed constrained decoding quality loss on reasoning/writing benchmarks (MATH-500, GPQA, ZebraLogic, WritingBench): format-requesting prompts cause an average −3.9pp accuracy drop while decoder-level grammar masking contributes only −1.6pp additional loss. Critically, recent closed-weight models show near-zero format tax. However, the paper explicitly acknowledges that 'simpler extraction tasks may show smaller effects' — the transfer of these findings to IE is an unvalidated hypothesis. Lost in Formatting (Ravikumar et al., EACL 2026) provides IE-specific evidence: across 280+ experiments on multiple IE benchmarks and models, output format choice alone shifts F1 by over 40%, with no single format consistently dominating — demonstrating that the format–accuracy interaction is even more pronounced for IE than for reasoning tasks, and reinforcing that the choice of constraint application strategy (prompt-level vs. decoder-level vs. two-pass) is a first-order design decision for IE. Structure Snowballing (Zhou, arXiv Apr 2026) documented cascading formatting errors under strict structural constraints in Qwen3-8B, specifically on HotpotQA multi-hop reasoning with self-reflection: accuracy dropped from 50.0% to 38.0% (12pp) under Outlines-based constrained decoding, with 96/100 first-round self-corrections misdiagnosed as FORMATTING_MISMATCH rather than addressing actual semantic errors. The snowballing mechanism — formatting compliance consuming reasoning capacity in smaller models — is a first-order risk for OntoCoDec's S1 single-pass strategy on Qwen3-8B, though notably the effect was measured on multi-hop reasoning with iterative self-correction (a more reasoning-intensive task than single-pass IE extraction). Le (arXiv Apr 2026) found relevant cross-architecture evidence: Qwen models are more sensitive to schema-level signals than LLaMA models, suggesting snowballing severity may differ across architectures. CRANE (Banerjee et al., ICML 2025) proved that constrained decoding to restrictive grammars limits LLMs to TC⁰ complexity. DCCD (arXiv Mar 2026) demonstrated +24pp gains on GSM8K via draft-conditioned constrained decoding, but was evaluated only on reasoning benchmarks, not IE. These findings collectively motivate strategies that minimize constraint scope — our S2 applies semantic constraints only during the formatting pass — but whether the prompt-vs-decoder quality split transfers to IE is an empirical question our S1/S2 comparison directly addresses.
68	
69	**The key gap:** No existing work (1) automatically compil
70	
71	## Proposed Approach
72	
73	We develop OntoCoDec (Ontology-Compiled Decoding Constraints), an automatic ontology-to-constraint compiler with a phased execution plan that de-risks the core empirical question before committing engineering effort.
74	
75	**Phase 0: Violation Rate Pilot Study + Format Tax Measurement (Day 1-2).** Before any compiler implementation, run unconstrained Qwen3-8B and Llama-3.1-8B on ACE05 (entity+relation), SciERC, and DocRED test sets using standard IE prompts with JSON output format. Write a lightweight Python script (~200 lines) that parses model outputs and checks each extracted triple against ontology type constraints: (a) entity type validity — is each predicted entity type in the ontology vocabulary?; (b) relation domain/range — are the argument entity types compatible with the relation's type signature (e.g., ACE05 PHYS.Located requires PER/GPE Arg-1 and FAC/LOC/GPE Arg-2; DocRED's Wikidata relations have subject-type and value-type constraints retrievable via the Wikidata API)?; (c) cross-field consistency — do entity mentions used as relation arguments have consistent types across mentions? Compute violation rates per model, per dataset, and per constraint category. **Additionally, this pilot serves a dual purpose as a format tax measurement for IE:** for each model, compare extraction F1 between unconstrained generation and JSON-grammar-constrained generation (via XGrammar-2/Outlines) on the same inputs, producing the first measurement of the format tax specifically for IE tasks — answering whether the Format Tax's prompt-vs-decoder quality split (−3.9pp prompt, −1.6pp decoder on reasoning benchmarks) transfers to IE, where Lost in Formatting (EACL 2026) shows format sensitivity is even more pronounced. This takes <1.5 days of engineering and <8 H100-hours of compute. **Decision criteria:** (i) If aggregate violation rate >5%, proceed with full constraint compiler (Phase 1-3). If <5%, pivot to the concrete negative-result paper plan described below. (ii) If grammar-constrained extraction F1 drops >5pp vs. unconstrained for Qwen3-8B (consistent with the Structure Snowballing effect), designate Llama-3.1-8B as the primary model for subsequent phases, since cross-architecture evidence (Le, arXiv Apr 2026) suggests Qwen and Llama models respond differently to schema-level constraints. This pilot is itself a methodological contribution — principled de-risking before engineering investment — and produces the first systematic violation rate measurements and IE-specific format tax measurements in the literature.
76	
77	**Concrete Negative-Result Paper Plan (if violations <5%).** If the Phase 0 pilot reveals low violation rates, the project pivots immediately to a substantive negative-result paper with four components beyond bare violation rate measurement: (i) **Granular violation analysis:** Which specific relation types, entity type combinations, and input complexity levels (sentence length, entity density, relation density) trigger the violations that do occur? This distributional analysis reveals whether violations are uniformly rare or concentrated in specific hard cases — important for practitioners deciding whether to invest in constraint enforcement for their specific ontology. (ii) **Cross-model and cross-prompting sensitivity:** Do violation rates vary across model families (Qwen3 vs. Llama-3.1), model sizes (8B vs. larger via API), and prompting strategies (zero-shot vs. few-shot, JSON vs. code-style output formats)? If violation rates are consistently low across all conditions, the negative result is robust; if they spike under certain conditions, this identifies when constraint enforcement becomes necessary. (iii) **Compiler as guaranteed-compliance safety net:** Even with low violation rates, applications requiring formal guarantees (knowledge graph population for biomedical databases, legal document processing, regulatory compliance) cannot tolerate any violations. We evaluate the compiler's overhead (latency, throughput) on these low-violation scenarios, characterizing the cost of guaranteed compliance — analogous to how type systems in programming languages provide value even when most code would run correctly without them. (iv) **Comparison with post-hoc filtering:** How does the violation rate compare to LLM+ASP's post-hoc rejection rate? If both are low, this strengthens the negative result; if post-hoc filtering catches more issues (because it can also check inter-triple consistency across the full output), this informs which lightweight enforcement strategy is preferable. This plan ensures a publishable paper at EMNLP Findings or the Insights from Negative Results workshop (co-located with EMNLP 2026 in Budapest) regardless of violation rate outcome, with sufficient analytical depth for main track consideration.
78	
79	**Phase 1: Ontology Constraint Compiler + LogitsProcessor (Day 2-6).** The compiler takes a standard IE ontology schema (JSON or Python dataclass: entity type list, relation types with domain/range type signatures) and emits two constraint components: (1) An EBNF grammar enforcing JSON structural validity and type vocabulary constraints — what CFGs can express. This uses standard grammar-constrained decoding (XGrammar-2 compatible). (2) A stateful type-masking specification for cross-field constraints — what CFGs cannot express. The type-masking component maintains a running entity type registry: as entities are generated, their types are recorded; when relation argument slots are decoded, the registry dynamically restricts valid entity references to those satisfying domain/range constraints, with inheritance-aware matching (e.g., GPE satisfies LOC constraints in ACE05's type hierarchy). We implement a unified LogitsProcessor in vLLM V1 that internally composes both constraint layers: (1) calls XGrammar-2's `GrammarMatcher.fill_next_token_bitmask()` to obtain the grammar-valid token mask, preserving XGrammar-2's optimized TagDispatch mechanism and batch processing capabilities rather than reimplementing grammar-constrained decoding from scratch; (2) computes the type constraint mask from the entity registry; and (3) applies bitwise AND of both masks to the logits tensor. This composable design leverages XGrammar-2's 6-10× per-token speedup for the grammar layer while adding only the incremental cost of the type mask computation and intersection. The processor operates at (num_requests × vocab_size) tensor granularity via vLLM's standard LogitsProcessor API (validate_params, __init__, apply, update_state). **Scoping decision:** The compiler targets entity+relation constraints for ACE05 (7 entity types, 18 relation subtypes), SciERC (6 entity types, 7 relation types), and DocRED (6 entity types, 96 relation types with Wikidata-derived domain/range constraints). DocRED serves as the scalability stress test: its 96 relations produce a substantially larger constraint specification than ACE05 or SciERC, testing whether the compiler and LogitsProcessor scale to realistic ontology sizes. For DocRED, we retrieve per-relation subject-type and value-type constraints from Wikidata's property constraint system and compile them into the same finite-state specification format. ACE05 event extraction (33 event types with typed argument roles) is deferred to Phase 3 as a stretch goal because the compiler complexity (event trigger identification + argument role assignment + role-filler type matching) is disproportionate to the core contribution.
80	
81	**Phase 2: Experiments (Day 6-10).** Two decoding strategies:
82	- **(S1) Single-pass constrained decoding:** Both grammar and type masks applied throughout generation. Maximizes validity, potential accuracy cost. Serves as the direct comparison point. **Structure Snowballing risk mitigation for S1:** Since Qwen3-8B showed a 12pp accuracy drop under constrained decoding on HotpotQA reasoning tasks (Zhou, arXiv 2604.06066), S1 may exhibit similar degradation. However, the snowballing mechanism — formatting compliance consuming reasoning capacity across multi-hop self-correction — is specific to iterative reasoning; single-pass IE extraction is less reasoning-intensive but more structurally complex. Phase 0's format tax measurement directly quantifies this risk for IE before committing to full experiments. If S1 shows severe degradation on Qwen3-8B, we additionally evaluate **soft logit biasing** (adding a large negative bias, e.g., −20, to type-violating tokens rather than masking them to −∞) as a relaxed alternative that still strongly discourages violations while preserving some probability mass on borderline cases, reducing the cognitive load of hard constraints.
83	- **(S2) Two-pass extraction:** Pass 1 extracts entities with grammar constraints only (entity types are independent, no cross-field semantic masking needed). Pass 2 generates relations with an input-dependent grammar compiled from Pass 1's entity outputs — the type constraints become vocabulary constraints in the second pass (only entities matching the domain/range types for each relation are included in the grammar's entity vocabulary), eliminating stateful masking entirely. This is the most novel and IE-specific strategy: it exploits the structure of IE ontologies to convert context-sensitive constraints into context-free ones by conditioning the grammar on prior extraction results. **S2 inherently mitigates Structure Snowballing:** by applying semantic constraints only in Pass 2 (relations) and using grammar-only constraints in Pass 1 (entities), the constraint scope per pass is substantially reduced, avoiding the cascading formatting errors that snowball when all constraints are applied simultaneously. The Format Tax's finding that decoupling reasoning from formatting reduces quality loss on reasoning benchmarks motivates this strategy, and Lost in Formatting (EACL 2026) shows that format sensitivity is even more extreme for IE — making the S1/S2 comparison not just a methodological ablation but a direc
84	
85	## Resource Estimate
86	
87	- **auto_research**: {'claude_api_cost': '$120-280 (~1200-2800 Opus turns for iterative constraint refinement, experiment orchestration, failure diagnosis, and paper writing)', 'estimated_gpu_cost': '$136-238', 'gpu_hours': '~68h H100-80GB (includes additional ablation depth: constraint type isolation, hard vs. soft masking, per-relation-type analysis, DocRED scalability evaluation, cross-architecture constraint sensitivity)', 'gpu_utilization': '~75-85% — agent pipelines experiments continuously after Phase 0 go/no-go decision', 'risk_note': 'Phase 0 go/no-go decision prevents wasted compute. If violation rates <5%, total GPU usage drops to ~12h (pilot + simplified experiments for the negative-result paper). If Qwen3-8B shows severe constraint degradation, the model switch to Llama-3.1-8B adds ~2h for re-running Phase 0 baselines.', 'speed_bottleneck': 'Phase 0 pilot must complete before Phase 1 begins (de-risking gate). After that, compiler implementation is CPU-bound; GPU utilization peaks during Phase 2-3.', 'team': '0 (initial setup: schema definitions, dataset paths, evaluation scripts)', 'timeline': '10-14 days with 1 H100 GPU available'}
88	- **human_in_loop**: {'claude_api_cost': '$80-180 (~800-1800 Opus turns for compiler iteration, experiment orchestration, and paper drafting)', 'estimated_gpu_cost': '$86-150', 'gpu_hours': '~43h H100-80GB', 'gpu_utilization': '~55-65% — agent handles constraint specification generation, experiment execution, and result parsing; human reviews LogitsProcessor correctness and validates violation rate analysis', 'risk_note': 'Phase 0 pilot study serves as an explicit de-risking gate for both violation rates AND format tax. If violation rates <5%, pivot to negative-result framing within Day 2, saving ~25h of GPU compute and ~8 days of engineering. If Qwen3-8B format tax >5pp, switch primary model to Llama-3.1-8B. DocRED adds ~3h of compute for preliminary scalability evaluation.', 'team': '1 researcher, ~45min/day reviewing pilot results, LogitsProcessor state transitions, and validity-vs-F1 tradeoff analysis', 'timeline': '12-14 days'}
89	- **manual**: {'estimated_gpu_cost': '$76-133 at ~$2.00-3.50/hr H100', 'gpu_hours': '~38h H100-80GB (Phase 0: 8h pilot+format tax × 2 models × 3 datasets; Phase 2: 22h experiments across 2 strategies × 5 baselines × 2 models × 3 datasets; Phase 3: 8h ablations including hard vs. soft masking)', 'gpu_utilization': '~60-70% — reduced idle time by eliminating GoLLIE retraining and deferring events; GPU active during Phase 0 pilot, Phase 2 experiments, and Phase 3 ablations', 'team': '1 researcher with NLP + systems experience', 'timeline': '14 days (Day 1-2: pilot study + format tax measurement + go/no-go; Day 2-6: compiler + LogitsProcessor; Day 6-10: experiments; Day 10-14: ablations + paper + optional events)'}
90	
91	## Key References
92	
93	- Synchromesh: Reliable Code Generation from Pre-trained Language Models (ICLR 2022, Poesia et al.) — foundational two-layer syntactic+semantic constrained decoding via Completion Engines
94	- IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking (ICLR 2025, Ugare et al.) — grammar+semantic callback paradigm with backtracking; key comparison for forward-only vs. backtracking design choice
95	- BoostCD/BoostIE: Combining Constrained and Unconstrained Decoding via Boosting (EMNLP 2025) — closest methodological relative; combines constrained+unconstrained decoding for closed IE via learned boosting on FlanT5-base; shows error complementarity (60% unrelated triplets unconstrained, forced token errors constrained); limited to vocabulary membership, not ontology type constraints; requires trained combiner model
96	- LLM+ASP Workflow: An LLM + ASP Workflow for Joint Entity-Relation Extraction (ICLP 2025, EPTCS 439, Tran et al.; arXiv 2508.12611, updated Jan 2026) — most direct post-hoc competitor; combines GPT-4o with ASP-based consistency checking using ok_type(S,E,F,R) rules for relation domain/range verification; on SciERC achieves 35.37% RE F1 with 10% training data (2.5× over baseline), reducing FPs from 713→482; post-hoc approach (filter after generation) vs. OntoCoDec's decoding-time enforcement (prevent during generation); uses closed-source GPT-4o with manual ASP rule specification
97	- ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs (arXiv Sep 2025, Apple) — production-scale soft ontology guidance via dynamically generated ontology snippets; 98.8% precision on 19M facts from 9M Wikipedia pages across 195 predicates; represents the 'soft constraint' pole — high precision through prompt guidance but no hard guarantee of type compliance
98	- GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024, Sainz et al.) — training-time schema compliance via Python class schemas on Code-Llama; ACE05 RE F1 = 63.6/67.5/70.1 at 7B/13B/34B supervised; published checkpoints used as discussion comparison
99	- DocRE-TCGL: Document-level Relation Extraction with Entity Type Constraints (Neural Networks 2025) — training-time type constraint enforcement via Type-Constrained Graph + Type-Constrained Loss for DocRE on DocRED/DWIE; complementary to decoding-time approach
100	- Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction (NLPCC 2025, Zhang et al.) — learns logical rules via MCTS to constrain LLM reasoning for DocRE; evaluated on DocRED, DWIE, Re-DocRED; demonstrates rule-based frameworks outperform implicit reasoning
101	- Re2-DocRED: Revisiting Revisited-DocRED for Joint Entity and Relation Extraction (EACL 2026) — improved DocRED annotations via SiftingLogic with entity-level constraints; adds 29,580 verified triplets to Re-DocRED (+27%); relevant for DocRED evaluation quality
102	- EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction (arXiv Apr 2024, Zaratiana et al.) — ASP-based constrained inference on discriminative models; ~1 F1 improvement on ACE05 relations; closest prior work but non-generative and requires manual constraint specification
103	- GenIE: Generative Information Extraction (NAACL 2022, Josifoski et al.) — bi-level constrained generation with prefix trie vocabulary constraints; precursor lacking cross-field type enforcement
104	- Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding (SIGDIAL 2024, Vukovic et al.; arXiv 2408.02361) — constrains CoT decoding to ontology-valid relation labels and slot values for dialogue RE using trie-based prefix matching; validates ontology-constrained decoding for RE in task-oriented dialogue but targets dialogue ontologies rather than IE schemas, uses CoT branching rather than logit masking, and does not handle cross-field type constraints
105	- Lost in Formatting: How Output Formats Skew LLM Performance on Information Extraction (EACL 2026, Ravikumar et al.) — 280+ experiments demonstrating that output format choice alone shifts IE F1 by over 40%, with no single format consistently dominating; directly reinforces that constraint application strategy is a first-order design decision for IE, and motivates the S2 two-pass strategy
106	- The Format Tax (arXiv Apr 2026) — prompt-level effects cause avg −3.9pp accuracy drop, decoder-level masking adds only −1.6pp on reasoning/writing benchmarks (MATH-500, GPQA, ZebraLogic, WritingBench); motivates S2 two-pass strategy but explicitly not evaluated on IE — transfer is a hypothesis our S1/S2 comparison tests
107	- From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection (arXiv Apr 2026, Zhou; arXiv 2604.06066) — Qwen3-8B accuracy drops 50.0%→38.0% (12pp) under Outlines-based constrained decoding on HotpotQA; identifies the snowballing mechanism where formatting compliance consumes reasoning capacity; first-order risk for S1 single-pass strategy, mitigated by S2 two-pass and soft logit biasing
108	- Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding (arXiv Apr 2026, Le; arXiv 2604.14862) — finds Qwen models are more sensitive to schema-level signals than LLaMA models; informs cross-architecture constraint sensitivity analysis and model selection strategy
109	- CRANE: Reasoning with Constrained LLM Generation (ICML 2025, Banerjee et al.) — theoretical proof that strict grammar constraints limit LLMs to TC⁰
110	- Draft-Conditioned Constrained Decoding (arXiv Mar 2026) — projection tax analysis; +24pp on GSM8K but evaluated on reasoning only, not IE
111	- XGrammar-2: Efficient Dynamic Structured Generation Engine (arXiv Jan 2026, Li et al.) — TagDispatch mechanism; GrammarMatcher API with fill_next_token_bitmask() enabling composable mask intersection; grammar backend for OntoCoDec's structural constraint layer
112	- SH-ETRs: Learning Soft-Hard Rules with Entity Type Constraints for Document-Level RE (Expert Systems 2025) — training-time entity type rule learning
113	- Grammar-Constrained Decoding for Structured NLP Tasks (EMNLP 2023, Geng et al.) — input-dependent grammars for closed IE
114	- Lazy-k Decoding: Constrained Decoding for Information Extraction (EMNLP 2023, Hemmer et al.)
115	- RELATE: Relation Extraction with Ontology Constraints (arXiv Sep 2025) — post-processing pipeline for ontology predicate mapping
116	- Grammar-constrained decoding for structured IE with fine-tuned generative models (Frontiers AI 2024, Schmidt & Cimiano)
117	- Scientific Knowledge-driven Decoding Constraints (arXiv Apr 2026, SciDC) — hand-crafted multi-layer constraints for scientific domains
118	- Ontology-to-tools compilation for executable semantic constraint enforcement (arXiv Feb 2026) — compiles ontologies into tool interfaces; incompatible with batch serving
119	- LLMs Underperform Graph-Based Parsers on Supervised RE for Complex Graphs (arXiv Apr 2026) — SciERC SOTA: Qwen3-14B-Base ~0.44 F1 fine-tuned vs. graph parser 0.35 F1
120	
121	## Reviewer Evaluation
122	
123	**Scores**:
124	  - clarity: **{'rationale': 'Exceptionally detailed proposal with comprehensive landscape coverage spanning post-hoc (LLM+ASP), soft guidance (ODKE+), training-time (GoLLIE, DocRE-TCGL), vocabulary-level (BoostCD), and discriminative-model (EnriCo) approaches. The phased timeline, de-risking gates, negative-result pivot plan, and Structure Snowballing mitigations are all clearly specified. The S1/S2 strategy comparison and five baselines are well-motivated.', 'score': 4}**/5
125	  - feasibility: **{'rationale': 'Resource budget (~38h H100) is well within the 200h constraint. The vLLM V1 LogitsProcessor API and XGrammar-2 GrammarMatcher composability are independently verified to exist with the exact interfaces described. Phase 0 de-risking gate is well-designed. Timeline (14 days) is tight but the phased approach with clear go/no-go decisions, narrowed scope (entity+relation on ACE05+SciERC, preliminary DocRED), and GoLLIE reduced to discussion comparison make it feasible for an experienced systems+NLP researcher.', 'score': 4}**/5
126	  - impact: **{'rationale': "Five scientific contributions beyond engineering: first violation rate quantification, first decoding-time vs. post-hoc comparison for IE type constraints, first IE-specific format tax measurement, automatic 'zero-code' compiler with scalability across ontology sizes (7–96 relations), and granular constraint type ablation. The negative-result paper plan ensures publishable output regardless of violation rate outcome. The practical 'zero-code schema compliance' capability is immediately useful for IE deployment.", 'score': 4}**/5
127	  - novelty: **{'rationale': 'The automatic ontology-to-constraint compiler for IE, stateful entity registry for cross-field type constraints during decoding, S2 two-pass strategy converting context-sensitive to context-free constraints, and systematic violation rate quantification are genuinely novel. No existing work (Synchromesh, IterGen, BoostCD, LLM+ASP, ODKE+, EnriCo, SEM-CTRL) combines automatic compilation from IE ontology definitions with decoding-time enforcement of relation domain/range constraints via composable logit masking.', 'score': 4}**/5
128	
129	## Human Review Note
130	
131	## Agent 审核结果（完整三阶段 pipeline）
132	
133	**Verdict**: PASS
134	
135	**入口三重共识 (X)**: 23.0%
136	**终审自评 (Y)**: 38.0%
137	**出口三重共识 (Z)**: 33.0%
138	**Z 区间**: [28.0%, 38.0%]
139	**真实提升 (Z-X)**: +10.0 pp
140	**幻觉幅度 (Y-Z)**: +5.0 pp
141	**出口一致性**: 高
142	**出口三次评估**: [33.0, 34.0, 32.0]
143	
144	### 优化方案 / 拒绝详情
145	Now I have the full original proposal. Let me produce the final output.
146	
147	【优化方案】
148	
149	1. **[标题]** — 从 "OntoCoDec (Ontology-Compiled Decoding Constraints)" 改为 "OntoCoDec: Composable Ontology Constraints for Guaranteed Type-Valid Information Extraction"。标题前置"Composable"信号 framework 级贡献，而非仅仅是 IE 系统。 — [命中 Novelty + Significance：审稿人从标题即感知到 generalizability]
150	
151	2. **[整体结构]** — 从单段密集叙述（原始 proposal 是 2 个巨大段落 + 1 个 contribution 列表）重构为 8 个清晰章节（Introduction、Research Questions、Constraint Composition Framework、Violation Landscape Analysis、Experiments、Related Work、Contributions、Feasibility）。 — [命中 Technical Soundness：结构化呈现让 reviewer 能快速定位核心 claim 和 evidence]
152	
153	3. **[核心 framing 重构：§1 Introduction]** — 原始 proposal 以"先量 violation rate、若够高则建 compiler"为主线，定位为 IE-specific 系统。改为以"什么条件下语义约束可以与语法约束在 token 级别组合？"为主问题，OntoCoDec 作为该 framework 的 IE instantiation。点明 beyond-IE 的普适性（Text-to-SQL 外键、对话 slot-filling、代码类型约束）但不 overclaim（仅在 IE 验证）。 — [命中 Novelty + Significance：从"解决一个具体问题"升级为"提出一个通用框架并用具体问题验证"]
154	
155	4. **[新增核心理论贡献：§3.1 Decidability Taxonomy]** — 原始 proposal 完全没有对约束可组合性的形式化讨论。新增三级可判定性分类：(a) Purely local（仅依赖当前位置语法上下文）；(b) Prefix-decidable with state augmentation（需要前缀状态追踪，如 domain/range 检查、cardinality 计数）；(c) Truly non-local（需要未来 token 信息，如前向共指）。附闭包性质证明和 entropy reduction bound（H_{G+S} ≥ H_G - log(|V_G|/|V_{G∩S}|)）。 — [命中 Novelty：从"工程组合"升级为"有理论指导价值的 framework"，审稿人可查表判断自己的约束是否可 decode-time 实现]
156	
157	5. **[新增非空保证 + Fallback：§3.1]** — 原始 proposal 声称"100% type-valid output"但未讨论 grammar mask ∩ semantic mask = ∅ 的边界情况。新增充分条件 proposition（type names 可 tokenize + JSON string fields 不限制 token）+ fallback 策略（relax to grammar-only + 标记 unconstrained position）。 — [命中 Technical Soundness：堵住"guarantee 声明的漏洞"，消除 reviewer 最直接的形式化攻击点]
158	
159	6. **[新增 Constraint State Machine 形式化：§3.4]** — 原始 proposal 仅说"intersects grammar mask with type constraint mask via bitwise AND"，未解释 type constraint 如何随已解码上下文动态更新。新增 formal definition M = (S, s_0, δ, C)，包括状态空间、转移函数、约束函数的精确定义；correctness precondition chain（entity type 约束先于 relation type 约束）；以及两层 error propagation 分析（constraint-level + extraction-level）。 — [命中 Technical Soundness：这是原始 proposal 最大的技术空白，也是 reviewer 最可能追问的点]
160	
161	7. **[新增 Adaptive Constraint Scheduling：§3.3]** — 原始 proposal 仅有 hard masking vs. soft biasing 的二选一。新增第三种模式：当 top-k (k=10) logits 全在合法集内时用 soft biasing（最小干预），当 top-1 违规时切 hard masking（强干预）。配合"最小必要干预"的理论动机（最小化 expected KL divergence）。实验中以 Pareto 曲线（compliance vs. F1）作为 highlight figure。 — [命中 Novelty + Technical Soundness：预先消解"hard masking 过于粗暴"的 reviewer 质疑，同时增加方法论创新点]
162	
163	8. **[新增 Incomplete Ontology 讨论：§3.2]** — 原始 proposal 未讨论 closed-world assumption 的局限。新增：明确 OntoCoDec 采用 closed-world assumption；soft biasing 在不完整 ontology 下的天然容错性；incomplete ontology ablation（移除 10%/20% ontology 条目测 recall 影响）。 — [命中 Technical Soundness：消除"hard masking 会不会误杀合法但未登记的 type 组合"的 reviewer 质疑]
164	
165	9. **[Phase 0 重构：§4]** — 原始 proposal 将 Phase 0 定位为"go/no-go 门控（5% violation rate 阈值）"。改为 **violation landscape 分析**，包括：error budget analysis（type violation 在总 extraction error 中占比）、violation taxonomy（domain vs. range 不对称）、cross-model fingerprint（Jaccard similarity + Spearman rank correlation）、violation-frequency correlation。去掉 binary 5% 阈值叙事。 — [命中 Significance + Analysis Depth：从"工程检查点"升级为"对 LLM ontological knowledge internalization 的实证研究"，即使 violation rate 低也有独立科学价值]
166	
167	10. **[贡献列表重聚焦：§7]** — 原始 5 条贡献（violation rates / decoding vs post-hoc / compiler / format tax / ablation）→ 3 条核心贡献：(1) Composable constraint framework（taxonomy + closure + entropy bound）；(2) OntoCoDec system（compiler + state machine + adaptive scheduling）；(3) Violation landscape empirics（error budget + taxonomy + fingerprint）。Format tax 降级为 Phase 0 前提验证（不再作为独立贡献声称），ablation 归入实验设计。 — [命中 Novelty + Significance：叙事更聚焦，避免"tries to do too many things"的 reviewer 评价]
168	
169	11. **[删除 Dual-Outcome 显式叙事]** — 原始 proposal 有大段"如果 violations <5% 则 pivot to negative-result paper"的表述。完全删除。改为 framework framing 使 contribution 不依赖于 violation rate 的绝对值（framework + empirics 无论 violation rate 高低都成立）。 — [命中 Significance：消除"作者自己都不确定 contribution 在哪里"的 reviewer 感知；风险管理保留在内部决策中]
170	
171	12. **[删除具体时间线]** — 原始 proposal 的"14 天 4 阶段"全部删除，改以 compute budget（~75 H100-hours）和 scope management 说明可行性。 — [命中 Feasibility：避免 reviewer 因激进时间线质疑严谨性]
172	
173	13. **[Baseline 大幅扩展：§5.3]** — 原始 5 个 baseline（其中 2 个用 published numbers）→ 10 个 baseline，全部在相同模型/数据/prompt 上实验：新增 best-of-N reranking、self-consistency with type filtering（明确 N 值和 aggregation 策略）、prompt-based ontology injection、LoRA fine-tuned（ACE05）、OntoCoDec S1-adaptive。LLM+ASP 和 GoLLIE 降级为 contextual reference。 — [命中 Technical Soundness：消除"missing obvious baseline"的 reject 理由，特别是 prompt injection（"为什么不直接告诉模型规则？"）和 LoRA（"为什么不直接 fine-tune？"）]
174	
175	14. **[新增 Schema Portability 独立实验：§5.6]** — 原始 proposal 无此内容。新增 within-scale transfer（ACE05→SciERC）和 cross-scale transfer（ACE05→DocRED），量化"OntoCoDec 换 ontology = 0 GPU-hours vs. LoRA 换 ontology = N GPU-hours + 标注数据"。 — [命中 Significance + Practical Impact：这是 OntoCoDec 最差异化的竞争力，在真实部署中 ontology 迭代是常态]
176	
177	15. **[新增 Streaming Metrics：§5.4]** — 原始 proposal 声称 streaming 优势但无度量。新增 time-to-first-valid-extraction、streaming validity rate（任意前缀截断点的已完成 triple 是否 type-valid）、constraint overhead ratio。 — [命中 Significance：将 streaming motivation 从空谈变为实证]
178	
179	16. **[新增完整 Related Work Section：§6]** — 原始 proposal 在正文中 inline 提及了 LLM+ASP、GoLLIE 等但没有独立的 Related Work 节。新增三个子领域覆盖：(a) Constrained Decoding（PICARD、FUDGE、NeuroLogic、GenIE、SynCode、Synchromesh）；(b) Structured Output Frameworks（XGrammar、Outlines、SGLang、Guidance、LMQL）；(c) Type-Aware IE（LLM+ASP、GoLLIE、DeepStruct、USM）。明确 differentiation：OntoCoDec 处理 cross-slot dependencies（relation type validity 依赖先前生成的 entity types），这是 PICARD/GenIE/SynCode 均未覆盖的场景。 — [命中 Related Work：消除"对文献不了解"的 reviewer 评价，PICARD 和 SynCode 的遗漏在原始版本中是致命风险]
180	
181	17. **[新增 S2 Error Propagation 分析：§3.4]** — 原始 proposal 未讨论 two-pass 策略中 pass 1 错误对 pass 2 的影响。新增 extraction-level error propagation：pass 1 产生 type-valid 但 factually wrong 的实体 → pass 2 在错误 entity typing 基础上施加 relation constraints → 系统性错误传播。实验中测量 pass 2 F1 conditioned on pass 1 entity correctness。 — [命中 Technical Soundness：深化 S1 vs. S2 的比较，使之从"两种策略哪个更好"升级为"为什么一种比另一种好"]
182	
183	18. **[70B 模型加入 Phase 0：§5.2]** — 原始 proposal 仅用 8B 模型。新增 Llama-3.1-70B-4bit 用于 Phase 0 violation landscape 分析，回答"大模型是否仍需要 OntoCoDec"。 — [命中 Significance：缓解"limited generalizability to small models"的质疑]
184	
185	19. **[Compute Budget 调整：§8]** — 从 ~38 H100-hours → ~75 H100-hours，反映新增的 baselines、LoRA fine-tuning、70B inference、streaming metrics、ablations。 — [命中 Feasibility：实事求是，不低估实施成本]
186	
187	【主要风险】:
188	
189	1. **Novelty 天花板**：尽管包装和理论化已接近最优，核心 insight（前缀可判定的语义约束可通过 bitmask 交集与语法约束组合）在概念上并不困难。审稿人可能评价为 "well-formalized but the underlying idea is not surprising"。Decidability taxonomy 可能被视为"对已有实践的显式化命名"而非真正的新理论。这是 proposal 的结构性上界，无法通过进一步打磨改变。**应对**：强调 taxonomy 的实用价值（系统设计者查表决策）+ entropy bound 的理论贡献 + adaptive scheduling 的方法创新。
190	
191	2. **Type Violation 占总 Error 比例可能过低**：如果 Phase 0 的 error budget analysis 显示 type violation 仅占总 extraction error 的 2-3%，则 OntoCoDec 对 overall F1 的改善微乎其微，significance 叙事需要完全依赖"safety-critical guaranteed compliance + streaming deployment"这条线。这条线是否足以说服审稿人取决于 reviewer 对 deployment relevance 的重视程度。**应对**：error budget analysis 结果已预先纳入实验设计；如果占比低，framework contribution + violation landscape empirics 提供独立于 F1 改善的 contribution 基础。
192	
193	【实施评估】:
194	- **计算资源**: ~75 H100-GPU-hours 总计。Phase 0（含 70B 推理 + error budget）~10 hours；Phase 1（compiler + state machine 开发）主要 CPU + 单 GPU 测试；Phase 2 核心实验（3 数据集 × 2 模型 × 10 条件）~35 hours；LoRA fine-tuning + schema transfer ~12 hours；ablations（Pareto frontier、incomplete ontology、constraint tightness、error propagation）~18 hours。需要至少 1 张 H100 80GB（70B-4bit 推理需 ~40GB VRAM），推荐 2-4 张 H100 并行以缩短实验周期。
195	- **数据需求**: ACE05（LDC 付费，大多数 NLP 实验室有 license）、SciERC（公开）、DocRED（公开）。三个数据集均有标准 train/dev/test 划分和公开的 ontology 定义。无需额外数据收集。
196	- **人工介入**: 无需人工标注。Phase 0 的 violation taxonomy 分类为规则判定（非人工）。Error budget analysis 中的 error 类别分解可自动化。论文写作为标准工作量。
197	- **训练需求**: LoRA fine-tuning 仅对 Llama-3.1-8B 在 ACE05 上做一次（~5 epochs，~3-4 hours on 1×H100），不是本项目的主体工作。其余所有实验均为 inference-only（in-context learning），不涉及模型训练。
198	- **新 Benchmark**: 不需要构建新 benchmark。使用现有 ACE05/SciERC/DocRED 标准数据集。Violation landscape analysis 和 error budget analysis 基于现有数据集的标准评估。
199	- **预估周期**: 4-6 周（单人全职）。Phase 0: 1 周（含 70B 推理和分析）；Phase 1（compiler + state machine 实现 + 调试）: 1.5-2 周（这是最大的工程不确定性，特别是 vLLM LogitsProcessor 集成和 edge case 处理）；Phase 2 + ablations + schema transfer: 1-1.5 周；论文写作: 1 周（可与后期实验并行）。如 2 人协作（1 人 system 开发 + 1 人 experiments/analysis），可压缩至 3-4 周。
200	
201	
202	
203	## MVP Validation Results
204	
205	- **Date**: 2026-05-13
206	- **Hypothesis Supported**: Yes
207	
208	### Key Metrics
209	
210	SciERC domain_range_violation_rate: 15.4% (minimal), 5.78% (schema-informed); DocRED domain_range_violation_rate: 18.7% (minimal); SciERC per-relation range: 0%-42.4%; DocRED relation_vocabulary_violations: 28.9%; Schema-informed prompt reduction: -62.4% but still >5%; Evaluate-for regression: +5.8pp under schema-informed; Total triples analyzed: 18,264 (SciERC 1724+1661, DocRED 16540)
211	
212	### Summary
213	
214	Phase 0 违规率试点研究完成。在 SciERC (7 relation types) 和 DocRED (96 relation types) 两个公开数据集上，用 Qwen3-8B 做 zero-shot entity+relation extraction，测量本体类型约束违反率。三个实验完成（SciERC minimal/schema-informed, DocRED minimal），第四个（DocRED schema-informed）运行中。核心假设"LLM-based IE 系统以非平凡比率违反本体类型约束"得到强验证：SciERC 15.4%, DocRED 18.7% per-triple domain/range violation rate，远超 5% 阈值。Schema-informed prompting 将 SciERC 违规率从 15.4% 降至 5.78%（-62.4%），但仍 >5% 且部分 relation types 反而退步（Evaluate-for +5.8pp），说明 prompt 级干预不足以替代 decoding-time enforcement。
215	
216	### Recommendation
217	
218	GO — 进入 Phase 1-2 constrained decoding 实验。Phase 1 compiler 代码已就绪（36 tests 通过），Phase 2 实验脚本已写好。立即启动 SciERC grammar_only/semantic_only/full_s1 实验，S2 bug 修复后补充。目标 EMNLP 2026 ARR (5/25)。
219	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e256698b-84c8-450b-865e-17d8658c3c47",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "cf9db529-5a90-474b-8a3d-7840aae76087",
  "sourceToolAssistantUUID": "e256698b-84c8-450b-865e-17d8658c3c47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-16T02:45:27.637Z_

Now let me read the actual paper sections, especially the related work section and the key technical sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf9db529-5a90-474b-8a3d-7840aae76087",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UsMnT3KKJfY7EHXE5M",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "7730d440-b736-403d-80cf-3f53eef9fcc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNEDNKhQhTLmmHPkM3Y2EP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26338,
      "cache_read_input_tokens": 15612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26338,
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

_source line 15 · 2026-05-16T02:45:29.676Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PJS9WthzucN2TCRpxSsoSV`</summary>

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
  "parentUuid": "7730d440-b736-403d-80cf-3f53eef9fcc5",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UsMnT3KKJfY7EHXE5M",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "4572347a-bca9-4fe9-a616-2a3889086e76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNEDNKhQhTLmmHPkM3Y2EP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26338,
      "cache_read_input_tokens": 15612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26338,
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

_source line 16 · 2026-05-16T02:45:29.705Z_

<details><summary>↩ Tool result · `toolu_01PJS9WthzucN2TCRpxSsoSV`</summary>

```text
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/section7_conclusion_550cbf.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
artifacts/_project/paper/section6_relwork_additions.tex
artifacts/_project/paper/discussion_paragraphs.tex
artifacts/dream_reports/dream_20260514T205155/best/paper.tex
artifacts/dream_reports/dream_20260514T205155/median/paper.tex
artifacts/dream_reports/dream_20260514T205155/worst/paper.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/section7_conclusion.tex
artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/appendix_related_work.tex
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/_project/paper/paper_tables_draft.tex
artifacts/_project/paper/section2_background.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section7_conclusion_compressed.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/main.tex
artifacts/dream_reports/dream_20260516T021434/best/paper.tex
artifacts/dream_reports/dream_20260516T021434/median/paper.tex
artifacts/dream_reports/dream_20260516T021434/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4572347a-bca9-4fe9-a616-2a3889086e76",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "f5cd9006-f971-4881-b80f-405df2eaed58",
  "sourceToolAssistantUUID": "4572347a-bca9-4fe9-a616-2a3889086e76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T02:45:29.837Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012jSuqXwAGNNMuQD8q6qJaq`</summary>

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
  "parentUuid": "f5cd9006-f971-4881-b80f-405df2eaed58",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UsMnT3KKJfY7EHXE5M",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "f77328a3-f2db-4614-80c1-1deee858b69d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNEDNKhQhTLmmHPkM3Y2EP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26338,
      "cache_read_input_tokens": 15612,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26338
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 15612,
          "cache_creation_input_tokens": 26338,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26338,
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

_source line 18 · 2026-05-16T02:45:29.854Z_

<details><summary>↩ Tool result · `toolu_012jSuqXwAGNNMuQD8q6qJaq`</summary>

```text
artifacts/dream_reports/dream_20260514T094226/median/references.bib
artifacts/_project/paper/relwork_new_entries.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f77328a3-f2db-4614-80c1-1deee858b69d",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "b8a1ef6a-ac23-4340-bbbc-301bf9225aca",
  "sourceToolAssistantUUID": "f77328a3-f2db-4614-80c1-1deee858b69d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T02:45:32.297Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S5cjjbnNz9DDLEmVMfZSGR`</summary>

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
  "parentUuid": "b8a1ef6a-ac23-4340-bbbc-301bf9225aca",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UskBLtRe2ADTc6bkPo",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "1d8ec550-356f-4c41-aa0a-3ca81959b8cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nzt6YdSpW7XNroh1wckxVU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 41950,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 41950,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 919,
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

_source line 20 · 2026-05-16T02:45:32.309Z_

<details><summary>↩ Tool result · `toolu_01S5cjjbnNz9DDLEmVMfZSGR`</summary>

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
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
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
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_runtime}
53	
54	% === §6 Related Work ===
55	\input{section6_related_work}
56	
57	% === §7 Discussion and Conclusion ===
58	\section{Discussion and Conclusion}
59	\label{sec:discussion}
60	\input{section7_conclusion_compressed}
61	
62	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
63	\clearpage
64	\section*{Limitations}
65	
66	The semantic layer introduces cross-field consistency (CF) violations (up to 12.02\%), a systematic consequence of per-relation independent enforcement.
67	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp), confirming that CF$\leftrightarrow$DR represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
68	Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
69	Results cover two 8B-class models under zero-shot prompting, where relation F1 remains around 8\% compared to $\sim$50\% for fine-tuned systems.
70	Composability with fine-tuned models is validated on SciERC with both Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,0.09\%, R-F1 loss $<$0.1\,pp), but evaluation is limited to one dataset and one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\%) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
71	The semantic layer's dynamic masking assumes each entity type maps to a unique first subword token---verified for both tokenizers on our two ontologies (6 entity types each), but ontologies with many types or multi-token type names would require prefix-tree masking, which we have not implemented.
72	Global entity-level type consensus during decoding offers the most direct path to resolving CF violations.
73	Both models tested are 8B-parameter class; scaling behavior to larger (70B+) or smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
74	CF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated.
75	Residual DR (e.g., 10.21\% for Qwen on DocRED) correlates with grammar-first fallback frequency and cannot be reduced beyond the schema constraint scope without complementary approaches such as global type consensus or post-hoc correction.
76	Validation with fine-tuned models, larger scales, and non-English ontologies remains to be explored.
77	
78	% === Ethics Statement ===
79	\section*{Ethics Statement}
80	
81	This work uses publicly available benchmark datasets (SciERC and DocRED) with no personally identifiable information.
82	No human subjects were involved in the experiments.
83	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
84	
85	% === Bibliography ===
86	\bibliography{relwork_new_entries}
87	
88	% === Appendix ===
89	\appendix
90	
91	\input{appendix_prompts}
92	\input{appendix_related_work}
93	\input{appendix_discussion}
94	\input{appendix_llama_per_relation}
95	
96	\end{document}
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d8ec550-356f-4c41-aa0a-3ca81959b8cc",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "172fbc1a-1f73-4502-9f2c-0d76e5e5f688",
  "sourceToolAssistantUUID": "1d8ec550-356f-4c41-aa0a-3ca81959b8cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T02:45:35.255Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VrECDfcXw2MyXUivoKNR9z`</summary>

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
  "parentUuid": "172fbc1a-1f73-4502-9f2c-0d76e5e5f688",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UsvmaYRSjovRG2JSA8",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "781c0c9d-c57d-4abf-b94d-70c9f4428b63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JddCPpP9yoqF61nwk2aiqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1586,
      "cache_read_input_tokens": 42869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 22 · 2026-05-16T02:45:35.260Z_

<details><summary>↩ Tool result · `toolu_01VrECDfcXw2MyXUivoKNR9z`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, Guidance~\cite{guidance2023}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, and ASAp~\cite{park2024grammar} ensure every token belongs to a grammar-valid continuation.
6	These methods operate at the syntactic level---they guarantee format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
7	
8	\paragraph{Semantic Constrained Decoding for Code.}
9	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, MGD~\cite{mgd_neurips2023}, and \citet{pldi2025_type_constrained_codegen} extend constrained decoding beyond CFG to enforce type and scope constraints in code generation.
10	OntoCoDec migrates this paradigm to information extraction.
11	
12	\paragraph{Vocabulary and Type-Constrained Generation.}
13	\citet{roth_yih_2004} establish relational type compatibility as a hard constraint via ILP, though applied post-hoc.
14	GENRE~\cite{decao2021genre}, NeuroLogic~\cite{lu2021neurologic}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear but not \emph{which type combinations} are valid per relation.
15	Training-based methods---TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, UIE~\cite{lu2022uie}, KnowCoder~\cite{knowcoder_acl2024}, CodeIE~\cite{li2023codeie}---encode IE structure through training or schema-as-code prompting but provide only \emph{soft} guidance that cannot guarantee compliance.
16	
17	\paragraph{Post-hoc Ontology Validation.}
18	ODKE+~\cite{khorshidi2025odke}, OntoGPT~\cite{spires_2024}, and OntoLogX~\cite{ontologx_2025} validate outputs against ontologies post-generation.
19	These detect-then-fix approaches waste compute on violated outputs; OntoCoDec \emph{prevents} violations during decoding.
20	
21	\paragraph{Quality Impact of Constrained Decoding.}
22	CRANE~\cite{banerjee2025crane} and \citet{schall2025hiddencost} show grammar restrictions can degrade reasoning, but \citet{tam2024letmespeak} find extraction-style tasks are robust to---or benefit from---constraints.
23	OntoCoDec confirms this: violations decrease by 94\% on SciERC with zero F1 degradation.
24	
25	An extended survey is provided in Appendix~\ref{app:related_work}.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "781c0c9d-c57d-4abf-b94d-70c9f4428b63",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "3ca705e3-bdc1-467f-af34-61f11b9bdce1",
  "sourceToolAssistantUUID": "781c0c9d-c57d-4abf-b94d-70c9f4428b63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T02:45:35.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JqoUuH8QFn5sFgPs4Aqt2A`</summary>

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
  "parentUuid": "3ca705e3-bdc1-467f-af34-61f11b9bdce1",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UsvmaYRSjovRG2JSA8",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "dff9777b-f861-4401-b526-bb1bea52bf4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JddCPpP9yoqF61nwk2aiqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1586,
      "cache_read_input_tokens": 42869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 24 · 2026-05-16T02:45:35.789Z_

<details><summary>↩ Tool result · `toolu_01JqoUuH8QFn5sFgPs4Aqt2A`</summary>

```text
1	\begin{abstract}
2	LLM-based information extraction systems can produce systematic ontology constraint violations during autoregressive generation.
3	On SciERC (7 relation types), 15.37\% of extracted triples violate domain/range type constraints; on DocRED (96 relation types), 18.46\%---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
4	%
5	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable decoding constraint layers:
6	(1)~a \emph{grammar layer} (XGrammar CFG) enforcing JSON structural validity and restricting entity/relation vocabularies to schema-defined values (ET, RV\,$\to$\,0\%); and
7	(2)~a \emph{semantic layer} enforcing domain/range constraints via a stateful entity registry and dynamic logit masking.
8	The grammar layer is an enabling prerequisite; the two compose via bitwise AND on token-level masks.
9	%
10	On SciERC, \textsc{OntoCoDec} reduces domain/range violations by 94\% (15.37\%\,$\to$\,0.93\%) while maintaining extraction F1 ({+}0.13pp, $p{=}0.58$).
11	On DocRED, violations decrease by 45--90\% depending on the model, with significant relation F1 gains for both Qwen3-8B ({+}0.50pp, $p{<}0.001$) and Llama-3.1-8B ({+}0.29pp, $p{=}0.013$; DR$\downarrow$90.2\%).
12	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1
13	Quantitative analysis reveals that residual DR varies predictably with ontology tightness $\times$ baseline violation rate ($R^2{=}0.886$; Appendix~\ref{app:dual-factor}).
14	Composed with LoRA fine-tuning on SciERC, \textsc{OntoCoDec} achieves DR\,=\,0\% at R-F1 43.77 (loss $<$0.1\,pp), confirming that fine-tuning and constrained decoding are complementary.
15	\end{abstract}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dff9777b-f861-4401-b526-bb1bea52bf4d",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "54409fc5-e09a-471c-b01e-545554026c9d",
  "sourceToolAssistantUUID": "dff9777b-f861-4401-b526-bb1bea52bf4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T02:45:36.211Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GvDJeUptrnS2HCs4jsREm1`</summary>

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
  "parentUuid": "54409fc5-e09a-471c-b01e-545554026c9d",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UsvmaYRSjovRG2JSA8",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "7b1969ee-070c-4a12-acd6-e3af47826b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JddCPpP9yoqF61nwk2aiqw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1586,
      "cache_read_input_tokens": 42869,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 42869,
          "cache_creation_input_tokens": 1586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1586,
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

_source line 26 · 2026-05-16T02:45:36.217Z_

<details><summary>↩ Tool result · `toolu_01GvDJeUptrnS2HCs4jsREm1`</summary>

```text
1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass during decoding.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
16	
17	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
18	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
19	The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records type assignments; when relation arguments are generated, dynamic logit masking restricts output to types compatible with the relation's domain/range specification.
20	The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
21	On SciERC, OntoCoDec reduces DR violations from 15.37\% to 0.93\% ($\downarrow$94\%) while remaining F1-neutral ($+$0.13\,pp).
22	
23	Our contributions:
24	\begin{enumerate}
25	    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
26	    \item OntoCoDec, a two-layer compiled constraint framework that enforces cross-field type validity during autoregressive IE---the first to automatically compile IE ontology domain/range constraints into token-level semantic masks.
27	    \item Empirical validation on 2 models $\times$ 2 datasets: DR $\downarrow$94\% on SciERC and $\downarrow$45--90\% on DocRED, with significant R-F1 gains on DocRED ($p \leq 0.013$), model-agnostic structural guarantees, and composability with fine-tuning (DR\,$\to$\,0\% at $<$0.1\,pp F1 cost).
28	\end{enumerate}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b1969ee-070c-4a12-acd6-e3af47826b35",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "48c783f5-f0d9-44c2-8be4-38ef0198b0a3",
  "sourceToolAssistantUUID": "7b1969ee-070c-4a12-acd6-e3af47826b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T02:45:39.169Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hayr1QEJo4EDRBiG2Fx3Sn`</summary>

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
  "parentUuid": "48c783f5-f0d9-44c2-8be4-38ef0198b0a3",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UtDTBDfPgNWyXj53gC",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "16a3ed44-15c7-4aba-9873-577afa4af891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRoGRnXKdwVgdhPofasYA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 44455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 28 · 2026-05-16T02:45:39.175Z_

<details><summary>↩ Tool result · `toolu_01Hayr1QEJo4EDRBiG2Fx3Sn`</summary>

```text
1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
10	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
11	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
12	
13	
14	\subsection{Problem Formulation}
15	\label{sec:formulation}
16	
17	\paragraph{IE as structured generation.}
18	Given an input text $x$, a language model generates a structured JSON output $y$:
19	%
20	\begin{equation}\label{eq:output-schema}
21	\resizebox{.88\columnwidth}{!}{$\displaystyle
22	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
23	$}
24	\end{equation}
25	%
26	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
27	
28	\paragraph{Ontology compliance.}
29	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,\, (\tau^h, \tau^t) \in \sigma(r)\}$ for domain-valid head types and $\operatorname{range}(r, \tau^h) = \{\tau^t : (\tau^h, \tau^t) \in \sigma(r)\}$ for the conditional range given head type $\tau^h$.
30	Our enforcement target is \emph{pair-based} type validity: $(\tau^h, \tau^t) \in \sigma(r)$ for every triple.
31	The decoder enforces this sequentially---$\tau^h \in \operatorname{dom}(r)$ at head position, then $\tau^t \in \operatorname{range}(r, \tau^h)$ at tail position---which is equivalent to the full pair check and strictly stronger than independent domain/range enforcement, because most relations have non-rectangular type signatures ($\sigma(r) \subsetneq \operatorname{dom}(r) \times \operatorname{range}(r)$ for all 7 SciERC and 73/96 DocRED relations; see \S\ref{sec:rectangularity}).\footnote{An independent check ($\tau^h \in \operatorname{dom}(r) \wedge \tau^t \in \operatorname{range}(r)$) would over-permit type pairs by $1.50\times$ on SciERC and $1.58\times$ on DocRED, corresponding to 33.3\% and 36.8\% spurious type pairs.}
32	Our goal is maximizing $P(y \mid x)$ subject to all triples being type-valid and $y$ being well-formed JSON conforming to Eq.~\eqref{eq:output-schema}.
33	
34	
35	\subsection{Grammar Layer}
36	\label{sec:grammar}
37	
38	The grammar layer compiles $\mathcal{O}$ into a context-free grammar (CFG) enforced at every decoding step via logit masking.
39	This compilation proceeds in two stages.
40	
41	\paragraph{Schema-to-grammar compilation.}
42	We generate a JSON Schema encoding the structure in Eq.~\eqref{eq:output-schema} with \texttt{enum} constraints restricting entity types to $\mathcal{E}$ and relation types to $\mathcal{R}$.
43	This schema is compiled into an EBNF grammar via XGrammar~\cite{dong2025xgrammar}, producing a pushdown automaton tracking JSON structure and enum membership.
44	
45	\paragraph{Logit masking.}
46	At step $t$, the automaton computes grammar-valid tokens $G(t) \subseteq V$; all others receive logits $-\infty$.
47	This simultaneously enforces: (i)~structural validity (well-formed JSON), (ii)~relation vocabulary membership ($r_j \in \mathcal{R}$), and (iii)~entity type membership ($\tau_i \in \mathcal{E}$).
48	Domain/range constraints are \emph{not} enforced, as they depend on entity types within each triple—the gap filled by the semantic layer.
49	
50	\paragraph{Empirical profile.}
51	On SciERC, grammar constraints eliminate relation vocabulary violations entirely (1.39\%\,$\to$\,0\%) and entity type violations entirely (0.40\%\,$\to$\,0\%), with no measurable F1 impact.
52	Domain/range violations remain effectively unchanged (15.37\%\,$\to$\,14.84\%), confirming that grammar constraints enforce structural but not semantic validity.
53	
54	
55	\subsection{Semantic Layer}
56	\label{sec:semantic}
57	
58	The semantic layer enforces domain/range constraints through a stateful logits processor maintaining an entity registry during generation.
59	
60	\subsubsection{Entity Registry}
61	\label{sec:entity-registry}
62	
63	As the model generates the entity list, the semantic layer builds a registry $\mathcal{D}: \text{name} \to \text{type}$ mapping each entity to its declared type.
64	This registry is populated incrementally: when the model completes an entry $\{n_i, \tau_i\}$, the pair $(n_i, \tau_i)$ is added to $\mathcal{D}$.
65	The registry is then consulted during relation generation to look up the declared types of head and tail entities.
66	
67	\subsubsection{Position Detection}
68	\label{sec:position-detection}
69	
70	At each step $t$, the processor determines which field is currently being generated by pattern-matching on the decoded prefix.
71	We define five field positions---\textsc{EntityType}, \textsc{RelationType}, \textsc{HeadType}, \textsc{TailType}, and \textsc{FreeText}---identified via JSON key patterns (e.g., tokens following \texttt{"head\_type":} indicate \textsc{HeadType}).
72	Semantic masks activate only at type-bearing positions (\textsc{HeadType}, \textsc{TailType}).
73	
74	\subsubsection{Dynamic Masking}
75	\label{sec:dynamic-masking}
76	
77	At type-bearing positions, the processor computes a semantic mask $S(t) \subseteq V$ restricting generation to type-valid tokens.
78	
79	\paragraph{Head type masking.}
80	At a \textsc{HeadType} position, the processor considers the entity registry $\mathcal{D}$ and the current relation type $r_j$ (if already generated).
81	If $h_j \in \mathcal{D}$ and $\mathcal{D}[h_j] \in \operatorname{dom}(r_j)$, the mask allows only that registered type: $S(t) = \{\operatorname{tok}(\mathcal{D}[h_j])\}$, ensuring consistency with both the entity list and domain constraints.
82	Otherwise, if $r_j$ is known, the mask falls back to all domain-valid types: $S(t) = \{\operatorname{tok}(\tau) : \tau \in \operatorname{dom}(r_j)\}$.
83	If $r_j$ is unavailable, no semantic mask is applied.
84	
85	\paragraph{Tail type masking.}
86	At a \textsc{TailType} position, the head type $\tau^h_j$ is already determined from the decoded prefix.
87	The processor computes $\operatorname{range}(r_j, \tau^h_j)$---the valid tail types conditioned on the generated head type (\S\ref{sec:formulation}).
88	If $t_j \in \mathcal{D}$, the mask further restricts to the registered type when it belongs to this set.
89	This sequential check ($\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$) achieves exact pair-based enforcement, strictly tighter than an independent range check $\tau^t \in \operatorname{range}(r)$.
90	
91	\paragraph{Implementation.}
92	Each $\tau \in \mathcal{E}$ is mapped to the token ID of its first subword token; we pre-verify uniqueness across all entity types, which holds for both SciERC (6 entity types) and DocRED (6 entity types, disjoint from SciERC's) with both the Qwen3-8B and Llama-3.1-8B tokenizers.
93	The semantic mask is applied by setting logits of disallowed first-token IDs to $-\infty$.
94	
95	\subsubsection{Grammar-Semantic Interaction}
96	\label{sec:interaction}
97	
98	The final mask is the conjunction of $G(t)$ and $S(t)$, permitting only tokens satisfying both layers (formalized in \S\ref{sec:composition}).
99	This embodies an \emph{enabling dependency}: semantic lookup requires relation types to be valid members of $\mathcal{R}$, guaranteed only by the grammar layer.
100	Without grammar enforcement, the model may generate out-of-vocabulary relation types for which no $\sigma(r)$ rules exist.
101	Empirically, semantic-only constraints reduce DR by only 24\% (15.37\%\,$\to$\,11.65\%) while failing to eliminate vocabulary violations; the full combination achieves 94\% DR reduction.
102	When $S(t) \cap G(t) = \emptyset$---the semantic layer would mask out all grammar-valid tokens---the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.
103	This \emph{grammar-first invariant} reflects a deliberate priority ordering: structural integrity is a hard constraint, while type violations are soft errors detectable by downstream validation.
104	
105	
106	\subsection{Decoding Strategies}
107	\label{sec:strategies}
108	
109	\paragraph{S1: Single-pass decoding.}
110	Both constraint layers are active throughout a single generation pass.
111	The entity registry is populated as entities are generated and immediately available for relation-level type checking.
112	This is the simpler and recommended strategy, achieving strong constraint enforcement with higher relation F1 than the two-pass alternative.
113	
114	\paragraph{S2: Two-pass decoding.}\label{sec:s2}
115	The first pass generates only entities under grammar constraints; the extracted entities compile an input-dependent grammar that additionally constrains head and tail names to match declared entities.
116	The second pass generates relations under this tighter grammar plus semantic constraints.
117	Detailed comparison is provided in the appendix.
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16a3ed44-15c7-4aba-9873-577afa4af891",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "3aa3e9a8-a688-4389-be1e-12eca75ce1aa",
  "sourceToolAssistantUUID": "16a3ed44-15c7-4aba-9873-577afa4af891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T02:45:39.518Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MsLmstHfxbqX5HauXr61Wm`</summary>

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
  "parentUuid": "3aa3e9a8-a688-4389-be1e-12eca75ce1aa",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UtDTBDfPgNWyXj53gC",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "9be71926-3f53-480c-aadd-d539e3386972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRoGRnXKdwVgdhPofasYA7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2759,
      "cache_read_input_tokens": 44455,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2759
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 44455,
          "cache_creation_input_tokens": 2759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2759,
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

_source line 30 · 2026-05-16T02:45:39.523Z_

<details><summary>↩ Tool result · `toolu_01MsLmstHfxbqX5HauXr61Wm`</summary>

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
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \tau(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
26	The mean tightness $\bar{\tau} = \frac{1}{|\mathcal{R}|}\sum_{r} \tau(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern---tightness $\times$ baseline model violation rate---is consistent with the cross-dataset results: SciERC ($\bar{\tau}{=}0.333$, 24 valid pairs/relation) achieves 94--99\% DR reduction, while DocRED ($\bar{\tau}{=}0.842$, 5.68 pairs) achieves 45--90\%, with the residual modulated by model-specific baselines (\S\ref{sec:cross-model}; quantitative analysis in Appendix~\ref{app:dual-factor}).
29	
30	\paragraph{Non-Rectangularity and Sequential Masking.}
31	\label{sec:rectangularity}
32	% Data source: artifacts/rebuttal/w2_rectangularity_report.md
33	The sequential masking strategy---$\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$---is necessary because real ontology type signatures are overwhelmingly non-rectangular: 0/7 SciERC and only 23/96 DocRED relations satisfy $\sigma(r) = \operatorname{dom}(r) \times \operatorname{range}(r)$.
34	Independent enforcement ($\tau^h \in \operatorname{dom}(r) \wedge \tau^t \in \operatorname{range}(r)$) would admit 33.3\% (SciERC) and 36.8\% (DocRED) spurious type pairs---on SciERC, 100\% of residual DR violations under full S1 are pairs that pass independent checks but violate $\sigma(r)$.
35	OntoCoDec's sequential approach achieves exact pair-based enforcement without explicit enumeration of $\sigma(r)$ at each step, exploiting the autoregressive left-to-right generation order.
36	
37	\paragraph{Decidability Taxonomy.}
38	We classify ontology constraints by when sufficient information becomes available:
39	%
40	\begin{enumerate}[leftmargin=*,nosep]
41	  \item \textbf{Local}: require only the current token (entity/relation vocabulary membership). Handled by the grammar layer.
42	  \item \textbf{Prefix-decidable}: require the decoded prefix (domain/range constraints). Handled by the semantic layer via the entity registry.
43	  \item \textbf{Non-local}: require information not yet generated (forward coreference). Outside the scope of single-pass decoding; partially addressed by the two-pass strategy (S2, \S\ref{sec:s2}).
44	\end{enumerate}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9be71926-3f53-480c-aadd-d539e3386972",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "fc8fb93f-050f-4fb6-ba60-016ea2bd023b",
  "sourceToolAssistantUUID": "9be71926-3f53-480c-aadd-d539e3386972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T02:45:44.335Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DBqo6PyKiEDS7oNQ3cpJ6R`</summary>

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
  "parentUuid": "fc8fb93f-050f-4fb6-ba60-016ea2bd023b",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UtTgvfzysHegTRcpvg",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "7606fb7b-7f8f-473d-b882-1951b8f5fcf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yzBWkHAu1kwiP6UdZyuit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 47214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4573,
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

_source line 32 · 2026-05-16T02:45:44.348Z_

<details><summary>↩ Tool result · `toolu_01DBqo6PyKiEDS7oNQ3cpJ6R`</summary>

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
85	Soft-constraint approaches such as ontology-weighted beam scoring reduce violation frequency but cannot eliminate it, whereas OntoCoDec substantially reduces violations (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED depending on model).
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
98	OntoCoDec addresses this concern empirically: domain/range violations decrease by 94\% on SciERC (15.37\%$\to$0.93\%) and 45--90\% on DocRED across two models, with F1-neutral impact on SciERC ($+$0.13pp, $p{=}0.58$) and significant R-F1 gains on DocRED ($p \leq 0.013$).
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
109	Unlike training-based IE systems, OntoCoDec is training-free and substantially reduces type violations at inference time (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED); unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives with significant R-F1 gains on DocRED ($p \leq 0.013$) and F1-neutral impact on SciERC.
110	The two constraint layers---grammar (structural) and semantic (relational)---compose via bitwise AND with an enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7606fb7b-7f8f-473d-b882-1951b8f5fcf6",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "82de82aa-1801-4b0a-8f62-f757a141ef2c",
  "sourceToolAssistantUUID": "7606fb7b-7f8f-473d-b882-1951b8f5fcf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T02:45:44.917Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KJefVu7EprigKptJRHNdj2`</summary>

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
  "parentUuid": "82de82aa-1801-4b0a-8f62-f757a141ef2c",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UtTgvfzysHegTRcpvg",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "4f2cbdbe-5c97-4060-9617-5501f6710b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yzBWkHAu1kwiP6UdZyuit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 47214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4573,
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

_source line 34 · 2026-05-16T02:45:44.923Z_

<details><summary>↩ Tool result · `toolu_01KJefVu7EprigKptJRHNdj2`</summary>

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
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{T}|^2$ where $\mathcal{T} = \mathcal{E}$ is the entity type vocabulary: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules---e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''---which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}---well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}---$(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}---at the point where a type token is generated, all information needed (relation type, entity registry) is available in the decoded prefix.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f2cbdbe-5c97-4060-9617-5501f6710b88",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "dab1b463-0518-4e59-bc9c-3137a298aacd",
  "sourceToolAssistantUUID": "4f2cbdbe-5c97-4060-9617-5501f6710b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T02:45:49.424Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WLVFhUjX249GYfWwYQ9eaV`</summary>

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
  "parentUuid": "dab1b463-0518-4e59-bc9c-3137a298aacd",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UttMk7KE9qkTcopQ2c",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "4ad08131-fc7c-4973-8722-fab58f3dc1c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxqgoyeUbry3GkvvUFdv2f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5939,
      "cache_read_input_tokens": 51787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5939,
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

_source line 36 · 2026-05-16T02:45:49.429Z_

<details><summary>↩ Tool result · `toolu_01WLVFhUjX249GYfWwYQ9eaV`</summary>

```text
1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test set annotations are not publicly available; following prior work, we evaluate on the development set (998 documents).} 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	
14	\paragraph{Violation distribution.}
15	Table~\ref{tab:prompt_comparison} reports violation rates.
16	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED---comparable rates despite a 14$\times$ difference in ontology size---indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
17	RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce a target vocabulary from a single prompt.
18	Per-relation rates (Figure~\ref{fig:per_relation_dr}) vary by over 40 percentage points: \textsc{Compare} at 42.4\% vs.\ \textsc{Used-for} at 0.76\%, correlating with tightness---tight constraints (few valid type pairs) produce systematic failures.
19	
20	\begin{table}[t]
21	\centering
22	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
23	\label{tab:prompt_comparison}
24	\resizebox{\columnwidth}{!}{%
25	\begin{tabular}{ll cccc}
26	\toprule
27	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
28	\midrule
29	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
30	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
31	\midrule
32	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
33	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
34	\bottomrule
35	\end{tabular}%
36	}
37	\end{table}
38	
39	\begin{figure}[t]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
42	\caption{Per-relation DR violation rates on SciERC. Rates correlate with constraint tightness.}
43	\label{fig:per_relation_dr}
44	\end{figure}
45	
46	\paragraph{Prompt insufficiency.}
47	Schema-informed prompting---augmenting the prompt with valid type pairs---reduces DR by 62.4\% on SciERC but only 30.4\% on DocRED (Table~\ref{tab:prompt_comparison}), and is unreliable per-relation: DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp.
48	These limitations motivate decoding-time enforcement (\S\ref{sec:method}).
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ad08131-fc7c-4973-8722-fab58f3dc1c0",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "efff9526-76e5-4c16-9058-9e1b5871f0de",
  "sourceToolAssistantUUID": "4ad08131-fc7c-4973-8722-fab58f3dc1c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T02:45:50.194Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RqcTVDsfz1yWffdJyX5G2x`</summary>

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
  "parentUuid": "efff9526-76e5-4c16-9058-9e1b5871f0de",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UttMk7KE9qkTcopQ2c",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "25a49dd8-4835-406d-bf45-771409a0019a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxqgoyeUbry3GkvvUFdv2f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5939,
      "cache_read_input_tokens": 51787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5939,
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

_source line 38 · 2026-05-16T02:45:50.199Z_

<details><summary>↩ Tool result · `toolu_01RqcTVDsfz1yWffdJyX5G2x`</summary>

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
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain/range violation rate;
63	RV: relation vocabulary violation rate;
64	ET: entity type violation rate;
65	CF: cross-field consistency violation rate.
66	$\Delta$DR: relative DR reduction vs.\ the unconstrained baseline.
67	$\downarrow$\,/\,$\uparrow$: lower\,/\,higher is better.
68	Best per column in \textbf{bold} (CF excluded---see text).
69	F1 scores are multiplied by 100.
70	Statistical significance assessed via bootstrap resampling (10{,}000 iterations).}
71	\label{tab:scierc-ablation}
72	\end{table}
73	
74	% ──────────────────────────────────────────
75	%  (a) Core result
76	% ──────────────────────────────────────────
77	\paragraph{Core result: DR elimination at zero F1 cost.}
78	The full two-layer constraint configuration (S1) reduces domain/range
79	violations from 15.37\% to 0.93\%, a 94\% relative reduction,
80	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
81	while relation F1 moves from 8.23 to 8.36 ($+$0.13\,pp; bootstrap 95\% CI [$-$0.24, $+$0.58]\,pp, $p = 0.58$, 10{,}000 iterations).
82	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
83	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
84	The difference is not statistically significant ($p = 0.58$), confirming
85	that constraint enforcement is F1-neutral on this dataset.
86	At the per-relation level, violations drop from 42.42\% to 2.82\% on
87	\textsc{Compare}, from 33.54\% to 1.21\% on \textsc{Feature-of}, and
88	reach 0\% on four of seven relation types
89	(\textsc{Conjunction}, \textsc{Hyponym-of}, \textsc{Part-of},
90	\textsc{Used-for}).
91	% phase2_scierc_full_s1 per_relation_dr: Compare=0.0282,
92	%   Feature-of=0.0121, Hyponym-of=0, Part-of=0, Used-for=0, Conjunction=0
93	However, full constraint enforcement elevates cross-field consistency
94	violations from 0.08\% to 9.90\%;
95	% phase2_scierc_unconstrained: CF=0.0008; phase2_scierc_full_s1: CF=0.099
96	we analyze this trade-off in Section~\ref{sec:discussion}.
97	
98	% ──────────────────────────────────────────
99	%  (b) Grammar layer
100	% ──────────────────────────────────────────
101	\paragraph{Grammar layer: cost-free structural guarantees.}
102	Grammar-only constraints eliminate RV (1.39\%\,$\to$\,0\%) and ET (0.40\%\,$\to$\,0\%) with no F1 impact, while DR remains unchanged (15.37\%\,$\to$\,14.84\%), confirming that grammar constraints enforce structural validity but not semantic constraints.
103	% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
104	
105	% ──────────────────────────────────────────
106	%  (c) Enabling dependency
107	% ──────────────────────────────────────────
108	\paragraph{Enabling dependency.}
109	Semantic-only constraints reduce DR by only 24\% (15.37\%\,$\to$\,11.65\%) and cannot eliminate RV (1.51\%) or ET (0.40\%).
110	% phase2_scierc_semantic_only: DR=0.1165, RV=0.0151, ET=0.004
111	Adding the grammar layer yields a further 92\% relative reduction (11.65\%\,$\to$\,0.93\%), demonstrating an \emph{enabling dependency}: without grammar-enforced vocabulary, the semantic layer encounters OOV relation types with no domain/range rules.
112	% phase2_scierc_full_s1: DR=0.0093
113	
114	% ──────────────────────────────────────────
115	%  (d) S1 vs S2
116	% ──────────────────────────────────────────
117	\paragraph{S1 vs.\ S2.}
118	S2 achieves comparable DR (0.97\%) but lower R-F1 (8.03 vs.\ 8.36) with fewer triples (1{,}644 vs.\ 1{,}729) and does not resolve the CF trade-off (8.03\% vs.\ 9.90\%); we adopt S1 as the primary configuration.
119	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644
120	
121	% ──────────────────────────────────────────
122	%  (e) Composability with Fine-Tuning
123	%  exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
124	% ──────────────────────────────────────────
125	\paragraph{Composability with fine-tuning.}
126	\label{sec:composability}
127	Table~\ref{tab:composability} presents the composability matrix on SciERC for both Qwen3-8B and Llama-3.1-8B (zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1), testing whether OntoCoDec composes with task-specific fine-tuning across model families.
128	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
129	%          w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
130	%          llama_scierc_unconstrained, llama_scierc_full_s1,
131	%          w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval
132	
133	For Qwen3-8B, fine-tuning alone raises R-F1 from 8.23 to 43.86 ($+$35.63\,pp) and E-F1 from 31.01 to 67.05 ($+$36.04\,pp), while reducing DR from 15.37\% to 1.95\% (87\% relative reduction).
134	% w5_lora_scierc_unconstrained_eval: DR=0.0195, R-F1=0.4386, E-F1=0.6705
135	The residual 1.95\% DR concentrates on tight-constraint relations: \textsc{Evaluate-for} (13.13\%), \textsc{Part-of} (5.77\%), and \textsc{Compare} (5.00\%) (per-relation breakdown in Appendix~\ref{app:lora-per-relation}).
136	Adding OntoCoDec eliminates the remaining DR entirely (1.95\%\,$\to$\,0\%) with R-F1 cost of $-$0.09\,pp (43.86\,$\to$\,43.77) and unchanged E-F1 (67.05).
137	% w5_lora_scierc_constrained_eval: DR=0, R-F1=0.4377, E-F1=0.6705, CF=0.0118
138	
139	Llama-3.1-8B exhibits the same pattern.
140	Fine-tuning raises R-F1 from 2.68 to 45.45 ($+$42.77\,pp) and E-F1 from 23.56 to 67.76 ($+$44.20\,pp), while reducing DR from 13.34\% to 1.11\%.
141	% w5_llama_lora_scierc_unconstrained_eval: DR=0.0111, R-F1=0.4545, E-F1=0.6776
142	Adding OntoCoDec reduces DR by 92\% (1.11\%\,$\to$\,0.09\%) with R-F1 change of $+$0.02\,pp (45.45\,$\to$\,45.47) and unchanged E-F1 (67.76).
143	% w5_llama_lora_scierc_constrained_eval: DR=0.0009, R-F1=0.4547, E-F1=0.6776, CF=0.0046
144	
145	Across both models, fine-tuned + S1 yields DR\,$\leq$\,0.09\% with R-F1 change within $\pm$0.1\,pp, consistently validating Claim~3 on SciERC across two model families: fine-tuning and OntoCoDec compose along orthogonal axes---fine-tuning improves extraction quality, OntoCoDec guarantees ontological compliance.
146	We evaluate on one dataset and one fine-tuning method (LoRA), so we do not claim composability holds universally.
147	
148	Two secondary observations support this interpretation.
149	First, CF interference drops substantially under fine-tuning for both models: Qwen from $+$9.82\,pp to $+$1.18\,pp, Llama from $+$6.32\,pp to $+$0.46\,pp,
150	% Qwen: ZS CF delta = 9.90-0.08 = 9.82pp, FT CF delta = 1.18-0 = 1.18pp
151	% Llama: ZS CF delta = 6.56-0.24 = 6.32pp, FT CF delta = 0.46-0 = 0.46pp
152	because fine-tuned per-slot type predictions are more consistent with the entity registry;
153	for Qwen, the residual 1.18\% traces to \textsc{Generic}$\leftrightarrow$X schema-level ambiguity (Appendix~\ref{app:cf-distribution}) rather than enforcement failure.
154	Second, in the zero-shot setting, S1 R-F1 impact is negligible for both models (Qwen $+$0.13\,pp, Llama $-$0.14\,pp),
155	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
156	% llama_scierc_unconstrained: R-F1=0.0268; llama_scierc_full_s1: R-F1=0.0254
157	confirming that constraint enforcement is F1-neutral regardless of base model quality.
158	
159	\begin{table}[t]
160	\centering
161	\small
162	\setlength{\tabcolsep}{3pt}
163	\resizebox{\columnwidth}{!}{%
164	\begin{tabular}{@{}lll rrrr r@{}}
165	\toprule
166	\textbf{Model} & \textbf{Setting} & \textbf{Mode}
167	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
168	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
169	  & \textbf{$\Delta$DR} \\
170	\midrule
171	\multirow{4}{*}{Qwen3-8B}
172	  & \multirow{2}{*}{Zero-shot}
173	    & Unconstr.\ & 15.37 & 0.08 & 8.23  & 31.01 & --- \\
174	  & & Full S1    &  0.93 & 9.90 & 8.36  & 30.98 & $\downarrow$94\% \\
175	\cmidrule(l){2-8}
176	  & \multirow{2}{*}{LoRA}
177	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
178	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
179	\midrule
180	\multirow{4}{*}{Llama-3.1-8B}
181	  & \multirow{2}{*}{Zero-shot}
182	    & Unconstr.\ & 13.34 & 0.24 & 2.68  & 23.56 & --- \\
183	  & & Full S1    &  0.08 & 6.56 & 2.54  & 23.49 & $\downarrow$99\% \\
184	\cmidrule(l){2-8}
185	  & \multirow{2}{*}{LoRA}
186	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
187	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
188	\bottomrule
189	\end{tabular}}%
190	\caption{Composability matrix on SciERC (551 documents):
191	zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1
192	for Qwen3-8B and Llama-3.1-8B.
193	$\Delta$DR: relative DR reduction vs.\ the same-row unconstrained baseline.
194	For both models, fine-tuning alone leaves residual DR (1--2\%);
195	adding S1 reduces it to $\leq$\,0.09\% with R-F1 change within $\pm$0.1\,pp.
196	F1\,$\times$100.
197	Evaluation is limited to one dataset and one fine-tuning method (LoRA).}
198	\label{tab:composability}
199	\end{table}
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25a49dd8-4835-406d-bf45-771409a0019a",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "ee32d659-534d-4e8b-8cfa-d8f1cffc0064",
  "sourceToolAssistantUUID": "25a49dd8-4835-406d-bf45-771409a0019a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T02:45:54.866Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MhuLJwcedgrsydMbnZbdiv`</summary>

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
  "parentUuid": "ee32d659-534d-4e8b-8cfa-d8f1cffc0064",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UuFFr2h1iTnUvzmpSc",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "bb96546e-03e8-4c44-a37a-f5a615d05f2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9h4Si8BfA6ytzNtMrmBuy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6306,
      "cache_read_input_tokens": 57726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6306,
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

_source line 40 · 2026-05-16T02:45:54.874Z_

<details><summary>↩ Tool result · `toolu_01MhuLJwcedgrsydMbnZbdiv`</summary>

```text
1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types---14$\times$ the ontology size of SciERC.
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
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
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
60	\paragraph{Core result.}
61	Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET (2.48\%\,$\to$\,0\%), and near-eliminates RV (29.66\%\,$\to$\,0.03\%).
62	Relation F1 improves from 7.74 to 8.23 ($+$0.50\,pp; bootstrap 95\% CI [$+$0.23, $+$0.81], $p < 0.001$), attributable to grammar-layer elimination of 5{,}189 OOV relation predictions counted as false positives.
63	CF increases modestly (0.10\%\,$\to$\,2.57\%), lower than SciERC's 9.90\%.
64	
65	% exp_ids: phase2_docred_grammar_only
66	\paragraph{Grammar layer surfaces latent violations.}
67	Grammar-only constraints eliminate RV and ET but \emph{increase} DR from 18.46\% to 26.17\% ($+$42\%).
68	This counter-intuitive result has a structural explanation: the unconstrained baseline's 29.66\% OOV relation triples cannot be evaluated for DR (no schema entry exists); grammar enforcement assigns these triples valid relation names whose domain/range rules the associated entity types frequently violate.
69	The grammar layer thus \emph{reveals} latent type incompatibilities, directly motivating the semantic layer.
70	
71	% exp_ids: phase2_docred_semantic_only, phase2_docred_full_s1
72	\paragraph{Enabling dependency.}
73	Semantic-only constraints reduce DR by only 25\% (18.46\%\,$\to$\,13.84\%) while failing to eliminate RV (29.87\%) or ET (4.22\%).
74	Full S1 achieves a further 26\% relative reduction over semantic-only (13.84\%\,$\to$\,10.21\%), replicating the enabling dependency from SciERC: without grammar-enforced vocabulary, the semantic layer encounters OOV relation types for which no domain/range rules exist.
75	
76	% exp_ids: phase2_docred_full_s1, llama_docred_full_s1
77	\paragraph{Constraint tightness governs enforcement ceiling.}
78	The residual DR on DocRED (10.21\%) exceeds SciERC (0.93\%) due to per-relation \emph{constraint tightness}: DocRED relations average 5.68 valid type pairs ($\bar{\tau}{=}0.842$) vs.\ 24 on SciERC ($\bar{\tau}{=}0.333$).
79	Tighter constraints produce narrower grammar$\cap$semantic mask intersections, increasing fallback frequency---the aggregate fallback rate (10.2\%; 1{,}770/17{,}341 triples) closely tracks residual DR (10.21\%), confirming a near-bijection between fallback events and residual violations.
80	Crucially, tightness interacts with the model's baseline violation profile: Qwen's high RV (29.66\%) causes grammar enforcement to surface many latent DR violations, yielding 10.21\% residual DR; Llama's lower RV (16.03\%) limits this surfacing, achieving 2.55\% residual ($\downarrow$90.2\%) on the same ontology (\S\ref{sec:cross-model}).
81	This dual-factor pattern---tightness $\times$ baseline RV---is consistent with cross-dataset and cross-model DR reduction differences.
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb96546e-03e8-4c44-a37a-f5a615d05f2b",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "e284ea6a-e3d3-421a-a2ef-8d28cafbf7e4",
  "sourceToolAssistantUUID": "bb96546e-03e8-4c44-a37a-f5a615d05f2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T02:45:55.228Z_

<details open><summary>🔧 Tool call — Read · `toolu_013uEm6P9z3mnYNRKXuJdqCX`</summary>

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
  "parentUuid": "e284ea6a-e3d3-421a-a2ef-8d28cafbf7e4",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UuFFr2h1iTnUvzmpSc",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "99ed8b6e-d0a5-4c33-9795-dc7483d0d5a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9h4Si8BfA6ytzNtMrmBuy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6306,
      "cache_read_input_tokens": 57726,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6306
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 57726,
          "cache_creation_input_tokens": 6306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6306,
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

_source line 42 · 2026-05-16T02:45:55.234Z_

<details><summary>↩ Tool result · `toolu_013uEm6P9z3mnYNRKXuJdqCX`</summary>

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
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results alongside Qwen3-8B.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr rr@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \multicolumn{2}{c}{\textbf{F1}} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-8}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & Rel. & Ent. \\
26	\midrule
27	\multirow{4}{*}{SciERC}
28	  & Qwen (U)  & 15.37 & 1.39 & 0.40 & 0.08 & 8.23 & 31.01 \\
29	  & Qwen (S1) &  0.93 & 0    & 0    & 9.90 & 8.36 & 30.98 \\
30	  \cmidrule(l){2-8}
31	  & Llama (U)  & 13.34 & 0.55 & 0    & 0.24 & 2.68 & 23.56 \\
32	  & Llama (S1) &  0.08 & 0    & 0    & 6.56 & 2.54 & 23.49 \\
33	\midrule
34	\multirow{4}{*}{DocRED}
35	  & Qwen (U)  & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 & 58.15 \\
36	  & Qwen (S1) & 10.21 &  0.03 & 0    & 2.57 & 8.23 & 59.37 \\
37	  \cmidrule(l){2-8}
38	  & Llama (U)  & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 & 55.65 \\
39	  & Llama (S1) &  2.55 &  0    & 0    & 12.02 & 6.27 & 55.01 \\
40	\bottomrule
41	\end{tabular}}%
42	\caption{Cross-model validation. U: unconstrained; S1: full two-layer.
43	Parse failures (U$\to$S1): Qwen DocRED 12$\to$11, Llama DocRED 68$\to$91; others $\leq$1.
44	F1 $\times$100.}
45	\label{tab:cross-model}
46	\end{table}
47	
48	\paragraph{Model-agnostic structural guarantees.}
49	RV and ET violations are eliminated ($\leq$0.03\%) for both models on both datasets, confirming that grammar-layer enforcement depends on the decoding mechanism, not model-specific generation patterns.
50	
51	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1
52	\paragraph{DR reduction generalizes but varies by model.}
53	SciERC DR drops 94\% for Qwen (15.37\%\,$\to$\,0.93\%) and 99.4\% for Llama (13.34\%\,$\to$\,0.08\%); DocRED DR drops 45\% for Qwen and 90.2\% for Llama.
54	R-F1 is preserved or improves in three of four settings
55	(Qwen: $+$0.13/$+$0.50\,pp; Llama: $-$0.14/$+$0.29\,pp).
56	On DocRED, R-F1 gains are statistically significant for both models
57	(Qwen $+$0.50\,pp, $p{<}0.001$; Llama $+$0.29\,pp, $p{=}0.013$;
58	bootstrap 10{,}000 iterations).
59	The sole R-F1 decline (Llama SciERC, $-$0.14\,pp)
60	is practically negligible on a 2.68\% baseline.
61	On SciERC, Qwen's R-F1 change is not significant ($p{=}0.58$).
62	% All bootstrap CIs registry-aligned (≤0.05pp tolerance)
63	Entity F1 impact is model-dependent: Qwen DocRED improves ($+$1.22\,pp, $p{<}0.001$), while Llama DocRED shows a modest decline ($-$0.64\,pp, $p{=}0.022$), partially attributable to Llama's higher parse failure rate under constraints (91 vs.\ 68 documents); other entity F1 changes are not significant.
64	
65	\paragraph{Tightness $\times$ RV interaction is consistent with cross-model asymmetry.}
66	Llama's relative DR reduction exceeds Qwen's on both datasets.
67	This asymmetry reflects the interaction between constraint tightness and model-specific violation profiles (\S\ref{sec:docred-results}): Qwen's higher baseline RV (29.66\% vs.\ 16.03\% on DocRED) causes grammar enforcement to surface more latent DR violations---triples whose OOV relation names masked underlying type incompatibilities.
68	With Llama's lower RV, fewer triples undergo this surfacing, yielding residual DR of 2.55\% vs.\ Qwen's 10.21\% on the same ontology ($\bar{\tau}{=}0.842$).
69	This is consistent with the dual-factor pattern: constraint tightness sets the enforcement difficulty ceiling, while baseline RV modulates the realized residual DR.
70	Notably, Llama's per-relation residual DR shows no correlation with tightness (Spearman $\rho{=}0.069$, $p{=}0.52$), indicating that the constraint system is uniformly effective across relations of varying tightness once baseline RV is low (per-relation breakdown in Appendix~\ref{app:llama-per-relation}).
71	
72	\paragraph{CF trade-off.}
73	CF violations increase under S1 for both models (Qwen: 0.08\%\,$\to$\,9.90\% SciERC, 0.10\%\,$\to$\,2.57\% DocRED; Llama: 0.24\%\,$\to$\,6.56\% SciERC, 0.17\%\,$\to$\,12.02\% DocRED), confirming CF elevation as a systematic property of per-relation independent enforcement (\S\ref{sec:discussion}).
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99ed8b6e-d0a5-4c33-9795-dc7483d0d5a3",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "861807eb-428d-4bb4-9c1b-d18de74b4607",
  "sourceToolAssistantUUID": "99ed8b6e-d0a5-4c33-9795-dc7483d0d5a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T02:45:59.669Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SmhYXaDpGo6qcKBVb42q56`</summary>

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
  "parentUuid": "861807eb-428d-4bb4-9c1b-d18de74b4607",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UuchwQ7pQTEtY2BYtF",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "c8702711-6265-4730-89fc-e4cbc832eff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TkvTJht41LNZgsP8qgKSw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4250,
      "cache_read_input_tokens": 64032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4250,
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

_source line 44 · 2026-05-16T02:45:59.674Z_

<details><summary>↩ Tool result · `toolu_01SmhYXaDpGo6qcKBVb42q56`</summary>

```text
1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix B.
3	
4	\paragraph{CF Severity.}
5	% exp_ids: phase2_scierc_full_s1 (CF=9.90%), phase2_scierc_grammar_only (CF=0.08%),
6	%          phase2_docred_full_s1 (CF=2.57%), llama_docred_full_s1 (CF=12.02%)
7	Unlike DR violations (ontologically invalid triples), CF violations are qualitatively milder: each triple remains type-valid per its own relation; only cross-triple consistency is broken.
8	The dominant pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (85/245 on SciERC; Table~\ref{tab:cf-distribution})---reflects genuine type-system ambiguity, with \textsc{Generic} involved in 63.3\% of all CF violations.
9	Ablation attributes CF to the semantic layer's two mechanisms---registry override and grammar-first fallback---with model-dependent profiles (Appendix~\ref{app:discussion}).
10	% exp_ids: phase2_scierc_grammar_only, phase2_docred_full_s1, llama_docred_full_s1
11	CF fallback ablation confirms a CF$\leftrightarrow$DR tension: eliminating CF re-routes violations to DR ($+$13.85\,pp), confirming the current S1 configuration as near-optimal (Appendix~\ref{app:cf-dr-tradeoff}).
12	% exp_ids: cf_fallback_ablation_scierc
13	Fine-tuning reduces CF by 88\% ($+$9.82\,pp\,$\to$\,$+$1.18\,pp; \S\ref{sec:composability}); the residual traces to schema-level \textsc{Generic}$\leftrightarrow$X ambiguity.
14	R-F1 gains are significant on DocRED ($+$0.50\,pp, $p{<}0.001$) but not SciERC ($+$0.13\,pp, $p{=}0.58$), proportional to baseline OOV rate (Appendix~\ref{app:discussion}).
15	% exp_ids: lora_scierc_full_s1, d012_bootstrap_ci
16	
17	% Limitations and Future Work moved to \section*{Limitations} in main.tex (ARR requirement)
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8702711-6265-4730-89fc-e4cbc832eff1",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "dec272fc-9f2d-4197-a0df-b0ee73e94666",
  "sourceToolAssistantUUID": "c8702711-6265-4730-89fc-e4cbc832eff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T02:46:00.185Z_

<details open><summary>🔧 Tool call — Read · `toolu_017icFRQaHuDvUnWnamhcGV9`</summary>

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
  "parentUuid": "dec272fc-9f2d-4197-a0df-b0ee73e94666",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UuchwQ7pQTEtY2BYtF",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "df090df8-d1a8-4065-a320-22fd6eca4dd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TkvTJht41LNZgsP8qgKSw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4250,
      "cache_read_input_tokens": 64032,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4250
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 64032,
          "cache_creation_input_tokens": 4250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4250,
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

_source line 46 · 2026-05-16T02:46:00.190Z_

<details><summary>↩ Tool result · `toolu_017icFRQaHuDvUnWnamhcGV9`</summary>

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
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type---which may differ from the entity's registered type.
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
27	\emph{Grammar-first fallback} (36.6\% of type-bearing positions on SciERC) occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations---these events account for the residual DR that persists after constraint enforcement.
28	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
29	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
30	
31	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
32	On SciERC, this yields 63.4\% coverage---at 63.4\% of type-bearing positions, the semantic layer actively constrains generation.
33	This metric directly quantifies the enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
34	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
35	
36	%%% CF-DR Trade-off Analysis %%%
37	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
38	
39	\paragraph{CF-DR Trade-off Analysis.}
40	\label{app:cf-dr-tradeoff}
41	
42	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
43	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
44	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
45	
46	\begin{table}[t]
47	\centering
48	\small
49	\begin{tabular}{@{}l rrrr@{}}
50	\toprule
51	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
52	\midrule
53	Full S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
54	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
55	\midrule
56	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
57	\bottomrule
58	\end{tabular}
59	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: grammar-first fallback rate at type-bearing positions.}
60	\label{tab:cf-dr-tradeoff}
61	\end{table}
62	
63	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
64	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
65	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
66	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
67	The grammar-first fallback is triggered at 36.64\% of type-bearing positions, indicating that this conflict is structural, not a tunable hyperparameter.
68	
69	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
70	Within this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
71	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use---a distinction the per-slot decoder cannot resolve without document-level coreference.
72	
73	Two complementary paths can lower CF without re-routing it to DR.
74	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
75	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
76	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
77	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
78	
79	%%% Dual-Factor Quantitative Analysis %%%
80	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
81	%          llama_scierc_full_s1, llama_docred_full_s1
82	
83	\paragraph{Dual-Factor Quantitative Analysis.}
84	\label{app:dual-factor}
85	
86	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\tau} \times \text{RV}_{\text{baseline}}$ for all four model$\times$dataset configurations.
87	A linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$; we do not report a $p$-value given the small sample size).
88	The strong fit is consistent with the dual-factor pattern described in \S\ref{sec:composition}: configurations with higher tightness and higher baseline violation rate exhibit proportionally higher residual DR after constraint enforcement.
89	The two DocRED points (high $\bar{\tau}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\tau}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
90	
91	\begin{figure}[t]
92	\centering
93	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
94	\caption{Residual DR vs.\ $\bar{\tau} \times \text{RV}_{\text{baseline}}$ across four model$\times$dataset configurations.
95	Linear fit: $y = 0.366x - 0.138$, $R^2 = 0.886$.}
96	\label{fig:dual-factor-scatter}
97	\end{figure}
98	
99	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
100	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
101	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
102	
103	\paragraph{Dataset-Dependent F1 Impact.}
104	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
105	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
106	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
107	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp), confirming that F1 gain magnitude is proportional to baseline OOV rate.
108	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
109	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
110	
111	%%% Paragraph 1: Low F1 Practical Significance %%%
112	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
113	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
114	
115	\paragraph{Practical Significance of Zero-Shot F1.}
116	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
117	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
118	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
119	When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
120	% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
121	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
122	The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
123	
124	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
125	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
126	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
127	
128	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
129	Post-hoc filtering---generating triples without constraints, then removing schema-violating predictions---yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
130	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
131	However, this precision gain comes at substantial cost.
132	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions), reducing recall from 9.46\% to 8.40\%.
133	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
134	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
135	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
136	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
137	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
138	
139	%%% CF Violation Distribution %%%
140	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
141	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
142	
143	\paragraph{Cross-Field Violation Distribution.}
144	\label{app:cf-distribution}
145	
146	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise---no mention triggered $\geq$3 types).
147	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
148	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially---a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
149	
150	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
151	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets, confirming that CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\begin{tabular}{@{}lr r@{}}
157	\toprule
158	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
159	\midrule
160	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
161	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
162	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
163	Method $\leftrightarrow$ Task & 20 & 8.2 \\
164	Material $\leftrightarrow$ Method & 17 & 6.9 \\
165	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
166	\midrule
167	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
168	\midrule
169	\textbf{Total} & \textbf{245} & 100.0 \\
170	\bottomrule
171	\end{tabular}
172	\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).
173	All 245 violations are pairwise conflicts.
174	Conflicts involving \textsc{Generic} account for 63.3\%.}
175	\label{tab:cf-distribution}
176	\end{table}
177	
178	%%% Per-Relation DR Elimination under Fine-Tuning %%%
179	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
180	
181	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
182	\label{app:lora-per-relation}
183	
184	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
185	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\tau{=}0.361$, 13.13\%), \textsc{Part-of} ($\tau{=}0.417$, 5.77\%), and \textsc{Compare} ($\tau{=}0.528$, 5.00\%).
186	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
187	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
188	
189	\begin{table}[t]
190	\centering
191	\small
192	\begin{tabular}{@{}l r rr rr@{}}
193	\toprule
194	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
195	\cmidrule(lr){3-4} \cmidrule(l){5-6}
196	\textbf{Relation} & $\tau$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
197	\midrule
198	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
199	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
200	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
201	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
202	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
203	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
204	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
205	\bottomrule
206	\end{tabular}
207	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
208	$\tau$: constraint tightness; $n$: predicted triple count.
209	Used-for gains one triple from Evaluate-for redirection.}
210	\label{tab:lora-per-relation}
211	\end{table}
212	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df090df8-d1a8-4065-a320-22fd6eca4dd4",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "23d53c73-177d-4d39-8f99-44fbb76f990d",
  "sourceToolAssistantUUID": "df090df8-d1a8-4065-a320-22fd6eca4dd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-16T02:46:03.558Z_

Now let me look at the bibliography to understand which references are cited.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23d53c73-177d-4d39-8f99-44fbb76f990d",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5Uuyv93qKEKzFf57tJB",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "e13579d2-4250-487c-895e-2d1ac977bf43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nawAjCNKEXjQXTLuJ4YqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6854,
      "cache_read_input_tokens": 68282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6854,
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

_source line 48 · 2026-05-16T02:46:05.332Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Brkh8WDZMDDyHQAVgxUZaD`</summary>

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
  "parentUuid": "e13579d2-4250-487c-895e-2d1ac977bf43",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5Uuyv93qKEKzFf57tJB",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "2a286ef5-0e1b-4950-a869-e036074c740e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nawAjCNKEXjQXTLuJ4YqR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6854,
      "cache_read_input_tokens": 68282,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6854
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 68282,
          "cache_creation_input_tokens": 6854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6854,
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

_source line 49 · 2026-05-16T02:46:05.345Z_

<details><summary>↩ Tool result · `toolu_01Brkh8WDZMDDyHQAVgxUZaD`</summary>

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
443	% Dataset & model references (5 entries)
444	% ============================================================
445	
446	% Confirmed via: ACL Anthology D18-1360, arXiv:1808.09602
447	@inproceedings{luan2018scierc,
448	  title     = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
449	  author    = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
450	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
451	  pages     = {3219--3232},
452	  year      = {2018},
453	  address   = {Brussels, Belgium},
454	  url       = {https://aclanthology.org/D18-1360/}
455	}
456	
457	% Confirmed via: ACL Anthology P19-1074, arXiv:1906.06127
458	@inproceedings{yao2019docred,
459	  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
460	  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
461	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
462	  pages     = {764--777},
463	  year      = {2019},
464	  address   = {Florence, Italy},
465	  url       = {https://aclanthology.org/P19-1074/}
466	}
467	
468	% Confirmed via: arXiv:2302.10205, Semantic Scholar
469	@article{wei2023zeroshot,
470	  title   = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},
471	  author  = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},
472	  journal = {arXiv preprint arXiv:2302.10205},
473	  year    = {2023},
474	  url     = {https://arxiv.org/abs/2302.10205}
475	}
476	
477	% Confirmed via: arXiv:2505.09388, Hugging Face model cards
478	@article{qwen2025qwen3,
479	  title   = {Qwen3 Technical Report},
480	  author  = {{Qwen Team}},
481	  journal = {arXiv preprint arXiv:2505.09388},
482	  year    = {2025},
483	  url     = {https://arxiv.org/abs/2505.09388}
484	}
485	
486	% Confirmed via: NeurIPS 2024 proceedings, arXiv:2312.07104
487	@inproceedings{zheng2024sglang,
488	  title     = {{SGLang}: Efficient Execution of Structured Language Model Programs},
489	  author    = {Zheng, Lianmin and Yin, Liangsheng and Xie, Zhiqiang and Sun, Chuyue and Huang, Jeff and Yu, Cody Hao and Cao, Shiyi and Kozyrakis, Christos and Stoica, Ion and Gonzalez, Joseph E. and Barrett, Clark and Sheng, Ying},
490	  booktitle = {Advances in Neural Information Processing Systems},
491	  volume    = {37},
492	  year      = {2024},
493	  url       = {https://arxiv.org/abs/2312.07104}
494	}
495	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a286ef5-0e1b-4950-a869-e036074c740e",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "d2d41d13-fad1-406f-a9bf-0a0472841f5d",
  "sourceToolAssistantUUID": "2a286ef5-0e1b-4950-a869-e036074c740e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-16T02:46:09.363Z_

Now let me look at the compiler implementation to understand the technical depth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d41d13-fad1-406f-a9bf-0a0472841f5d",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UvMtUwMW2FYpa5AuVN",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "127424f2-6f6b-4126-8c6a-4d3f40be6cce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016H9VKUR9nL9uDi3zsXAQUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10060,
      "cache_read_input_tokens": 75136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10060,
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

_source line 51 · 2026-05-16T02:46:11.303Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L2rRdMoCK1NcfXUSLqfpAE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/compiler/type_mask_processor.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "127424f2-6f6b-4126-8c6a-4d3f40be6cce",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UvMtUwMW2FYpa5AuVN",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "95f35069-b083-4b65-9f29-eca7fba45041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016H9VKUR9nL9uDi3zsXAQUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10060,
      "cache_read_input_tokens": 75136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10060,
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

_source line 52 · 2026-05-16T02:46:11.316Z_

<details><summary>↩ Tool result · `toolu_01L2rRdMoCK1NcfXUSLqfpAE`</summary>

```text
1	"""LogitsProcessor for runtime domain/range type constraint enforcement.
2	
3	Layered on top of XGrammar's structural constraints:
4	- XGrammar (Layer 1): Guarantees valid JSON, entity/relation type strings from enum
5	- TypeConstraintProcessor (Layer 2): Guarantees domain/range consistency
6	
7	At each generation step:
8	1. Detect current JSON field position (entity type? relation head_type? tail_type?)
9	2. If at entity type position -> allow all entity type first tokens
10	3. If at head_type position -> mask to types valid for the current relation
11	4. If at tail_type position -> mask to types valid for (relation_type, head_type) pair
12	5. Apply mask: disallowed type tokens -> logits = -inf
13	
14	Composition:
15	    grammar_processor = xgr.contrib.hf.LogitsProcessor(compiled_grammar)
16	    type_processor = TypeConstraintProcessor(spec, tokenizer)
17	    model.generate(logits_processor=[grammar_processor, type_processor])
18	
19	Framework: HuggingFace transformers (API: __call__(input_ids, scores) -> scores)
20	Depends on: ontology_compiler.ConstraintSpec (type->token mappings + relation constraints)
21	
22	Verified first-token IDs (Qwen3-8B tokenizer, context-independent):
23	  SciERC:
24	    Task=6262, Method=3523, Material=13415, Metric=54310,
25	    OtherScientificTerm=11409, Generic=19964
26	  DocRED:
27	    PER=9654, ORG=44927, LOC=12052, TIME=18129, NUM=17488, MISC=44
28	All first tokens are unique within each dataset -> simple first-token masking
29	is sufficient, no trie-based multi-token tracking needed.
30	"""
31	
32	from __future__ import annotations
33	
34	import re
35	from dataclasses import dataclass, field
36	from enum import Enum, auto
37	from typing import Optional
38	
39	import torch
40	from transformers import LogitsProcessor, PreTrainedTokenizerBase
41	
42	from .ontology_compiler import ConstraintSpec
43	
44	
45	class FieldPosition(Enum):
46	    """Current position in the JSON output structure."""
47	    UNKNOWN = auto()
48	    ENTITY_TYPE = auto()        # Inside entity's "type" field value
49	    RELATION_TYPE = auto()      # Inside relation's "type" field value
50	    RELATION_HEAD_TYPE = auto()  # Inside relation's "head_type" field value
51	    RELATION_TAIL_TYPE = auto()  # Inside relation's "tail_type" field value
52	    FREE_TEXT = auto()           # Entity text, relation head/tail text, etc.
53	
54	
55	@dataclass
56	class EntityRegistry:
57	    """Runtime registry of generated entities and their types.
58	
59	    Tracks text->type mappings from the entities list so that when a relation
60	    references an entity by text, we know its type for domain/range checking.
61	    """
62	    entities: dict[str, str] = field(default_factory=dict)
63	
64	    def register(self, text: str, entity_type: str):
65	        self.entities[text] = entity_type
66	
67	    def get_type(self, text: str) -> Optional[str]:
68	        return self.entities.get(text)
69	
70	    def clear(self):
71	        self.entities.clear()
72	
73	
74	@dataclass
75	class GenerationState:
76	    """Tracks the state of JSON generation for constraint application."""
77	    position: FieldPosition = FieldPosition.UNKNOWN
78	    current_relation_type: Optional[str] = None
79	    current_head_type: Optional[str] = None
80	    current_head_text: Optional[str] = None
81	    current_tail_text: Optional[str] = None
82	    entity_registry: EntityRegistry = field(default_factory=EntityRegistry)
83	    in_entities_section: bool = True
84	
85	    def reset(self):
86	        self.position = FieldPosition.UNKNOWN
87	        self.current_relation_type = None
88	        self.current_head_type = None
89	        self.current_head_text = None
90	        self.current_tail_text = None
91	        self.entity_registry.clear()
92	        self.in_entities_section = True
93	
94	
95	class PositionDetector:
96	    """Detects current field position by parsing generated text.
97	
98	    Regex-based parsing of JSON text generated so far. Called at every
99	    decoding step, so only inspects the tail of the text.
100	
101	    Future optimization: use XGrammar's GrammarMatcher state for O(1) per step
102	    instead of O(n) text parsing.
103	    """
104	
105	    _RE_TAIL_TYPE = re.compile(r'"tail_type"\s*:\s*"[^"]*$')
106	    _RE_HEAD_TYPE = re.compile(r'"head_type"\s*:\s*"[^"]*$')
107	    _RE_TYPE_FIELD = re.compile(r'"type"\s*:\s*"[^"]*$')
108	
109	    _RE_ENTITY = re.compile(r'"text"\s*:\s*"([^"]+)"\s*,\s*"type"\s*:\s*"([^"]+)"')
110	
111	    _RE_REL_TYPE_VAL = re.compile(r'"type"\s*:\s*"([^"]+)"')
112	    _RE_HEAD_TYPE_VAL = re.compile(r'"head_type"\s*:\s*"([^"]+)"')
113	    _RE_HEAD_TEXT_VAL = re.compile(r'"head"\s*:\s*"([^"]+)"')
114	    _RE_TAIL_TEXT_VAL = re.compile(r'"tail"\s*:\s*"([^"]+)"')
115	    _RE_REL_START = re.compile(r'\{\s*"head"')
116	
117	    @classmethod
118	    def detect(cls, generated_text: str, state: GenerationState) -> FieldPosition:
119	        """Determine which JSON field is currently being generated.
120	
121	        Mutates state in place: updates entity registry, current relation type,
122	        current head type, etc.
123	        """
124	        if '"relations"' in generated_text:
125	            state.in_entities_section = False
126	
127	        for match in cls._RE_ENTITY.finditer(generated_text):
128	            state.entity_registry.register(match.group(1), match.group(2))
129	
130	        # Find the last relation object being generated
131	        last_rel_start = -1
132	        for m in cls._RE_REL_START.finditer(generated_text):
133	            last_rel_start = m.start()
134	
135	        if last_rel_start >= 0:
136	            partial_rel = generated_text[last_rel_start:]
137	
138	            m = cls._RE_REL_TYPE_VAL.search(partial_rel)
139	            if m:
140	                state.current_relation_type = m.group(1)
141	
142	            m = cls._RE_HEAD_TYPE_VAL.search(partial_rel)
143	            if m:
144	                state.current_head_type = m.group(1)
145	
146	            m = cls._RE_HEAD_TEXT_VAL.search(partial_rel)
147	            if m:
148	                state.current_head_text = m.group(1)
149	
150	            m = cls._RE_TAIL_TEXT_VAL.search(partial_rel)
151	            if m:
152	                state.current_tail_text = m.group(1)
153	
154	        # Determine position from last 100 chars
155	        tail = generated_text[-100:]
156	
157	        if cls._RE_TAIL_TYPE.search(tail):
158	            return FieldPosition.RELATION_TAIL_TYPE
159	
160	        if cls._RE_HEAD_TYPE.search(tail):
161	            return FieldPosition.RELATION_HEAD_TYPE
162	
163	        if cls._RE_TYPE_FIELD.search(tail):
164	            if state.in_entities_section:
165	                return FieldPosition.ENTITY_TYPE
166	            else:
167	                return FieldPosition.RELATION_TYPE
168	
169	        return FieldPosition.FREE_TEXT
170	
171	
172	class TypeConstraintProcessor(LogitsProcessor):
173	    """Enforces domain/range type constraints during autoregressive generation.
174	
175	    Constraint logic:
176	    - ENTITY_TYPE: Allow all entity type first tokens (defense-in-depth with XGrammar)
177	    - RELATION_HEAD_TYPE: Given relation R, allow types T where exists T' s.t. (T,T') in R.valid_pairs
178	    - RELATION_TAIL_TYPE: Given relation R and head H, allow types T where (H,T) in R.valid_pairs
179	      <-- THIS IS THE KEY CONSTRAINT
180	
181	    Usage:
182	        spec, compiled_grammar = compile_ontology("ontology_constraints.json", tokenizer)
183	        grammar_proc = xgr.contrib.hf.LogitsProcessor(compiled_grammar)
184	        type_proc = TypeConstraintProcessor(spec, tokenizer, prompt_length=len(input_ids[0]))
185	        output = model.generate(**inputs, logits_processor=[grammar_proc, type_proc])
186	    """
187	
188	    def __init__(
189	        self,
190	        spec: ConstraintSpec,
191	        tokenizer: PreTrainedTokenizerBase,
192	        prompt_length: int = 0,
193	    ):
194	        self.spec = spec
195	        self.tokenizer = tokenizer
196	        self.prompt_length = prompt_length
197	        self.state = GenerationState()
198	        self.detector = PositionDetector()
199	
200	        self._type_first_token, self._all_type_first_tokens = self._build_first_token_map()
201	
202	    def _build_first_token_map(self) -> tuple[dict[str, int], set[int]]:
203	        """Build entity_type -> first_token_id mapping.
204	
205	        Uses pre-computed token IDs from ConstraintSpec.entity_type_first_token
206	        (set by OntologyCompiler.compile_type_constraints) if available.
207	        Falls back to ConstraintSpec.entity_type_token_ids, then tokenizer.encode().
208	
209	        All first tokens verified unique for Qwen3-8B on both SciERC and DocRED,
210	        so simple first-token masking is sufficient (no trie needed).
211	        """
212	        type_first_token: dict[str, int] = {}
213	        all_first_tokens: set[int] = set()
214	
215	        for etype in self.spec.entity_types:
216	            # Priority: pre-compiled first token > full token list > tokenizer
217	            if etype in self.spec.entity_type_first_token:
218	                first_id = self.spec.entity_type_first_token[etype]
219	            else:
220	                token_ids = self.spec.entity_type_token_ids.get(etype)
221	                if token_ids is None:
222	                    token_ids = self.tokenizer.encode(etype, add_special_tokens=False)
223	                first_id = token_ids[0]
224	
225	            type_first_token[etype] = first_id
226	            all_first_tokens.add(first_id)
227	
228	        return type_first_token, all_first_tokens
229	
230	    def _detect_position(self, generated_text: str) -> FieldPosition:
231	        """Detect current token's semantic position in the JSON structure.
232	
233	        Delegates to PositionDetector.detect() which parses the generated text
234	        and updates self.state (relation type, head type, entity registry, etc.).
235	        """
236	        return self.detector.detect(generated_text, self.state)
237	
238	    def __call__(
239	        self,
240	        input_ids: torch.LongTensor,
241	        scores: torch.FloatTensor,
242	    ) -> torch.FloatTensor:
243	        """Apply domain/range constraints to logits.
244	
245	        Args:
246	            input_ids: [batch_size, seq_len] -- full sequence including prompt
247	            scores: [batch_size, vocab_size] -- logits for next token
248	
249	        Returns:
250	            Modified scores with disallowed type tokens set to -inf
251	        """
252	        batch_size = input_ids.shape[0]
253	
254	        for batch_idx in range(batch_size):
255	            generated_ids = input_ids[batch_idx, self.prompt_length:].tolist()
256	            generated_text = self.tokenizer.decode(
257	                generated_ids, skip_special_tokens=True
258	            )
259	
260	            position = self._detect_position(generated_text)
261	
262	            if position == FieldPosition.ENTITY_TYPE:
263	                scores[batch_idx] = self._mask_entity_type(scores[batch_idx])
264	
265	            elif position == FieldPosition.RELATION_HEAD_TYPE:
266	                scores[batch_idx] = self._mask_head_type(scores[batch_idx])
267	
268	            elif position == FieldPosition.RELATION_TAIL_TYPE:
269	                scores[batch_idx] = self._mask_tail_type(scores[batch_idx])
270	
271	        return scores
272	
273	    def _mask_entity_type(self, logits: torch.FloatTensor) -> torch.FloatTensor:
274	        """At entity type position, allow only valid entity type first tokens.
275	
276	        XGrammar's enum constraint already restricts to valid types, but this
277	        provides defense-in-depth by masking at the logit level.
278	        All entity types are allowed here (no domain/range filtering at this stage).
279	        """
280	        return self._apply_type_mask(logits, set(self.spec.entity_types))
281	
282	    def _mask_head_type(self, logits: torch.FloatTensor) -> torch.FloatTensor:
283	        """Mask entity types that cannot be head_type for the current relation.
284	
285	        Strategy: intersect entity registry type with D/R-valid types.
286	        - If entity type known AND D/R-valid → force that single type
287	        - If entity type known but NOT D/R-valid → use D/R constraint
288	        - If entity type unknown → use D/R constraint
289	        """
290	        rel_type = self.state.current_relation_type
291	        constraint = self.spec.get_constraint(rel_type) if rel_type else None
292	        allowed_dr = constraint.valid_head_types() if constraint else None
293	
294	        head_text = self.state.current_head_text
295	        if head_text:
296	            actual_type = self.state.entity_registry.get_type(head_text)
297	            if actual_type and actual_type in self._type_first_token:
298	                if allowed_dr is None or actual_type in allowed_dr:
299	                    return self._apply_type_mask(logits, {actual_type})
300	
301	        if allowed_dr is not None:
302	            return self._apply_type_mask(logits, allowed_dr)
303	        return logits
304	
305	    def _mask_tail_type(self, logits: torch.FloatTensor) -> torch.FloatTensor:
306	        """Mask entity types that cannot be tail_type for (relation, head_type).
307	
308	        Strategy: intersect entity registry type with D/R-valid types.
309	        - If entity type known AND D/R-valid → force that single type
310	        - If entity type known but NOT D/R-valid → use D/R constraint
311	        - If entity type unknown → use D/R constraint
312	        """
313	        rel_type = self.state.current_relation_type
314	        head_type = self.state.current_head_type
315	        constraint = self.spec.get_constraint(rel_type) if rel_type else None
316	
317	        if constraint is not None:
318	            if head_type is not None:
319	                allowed_dr = constraint.valid_tail_types_for_head(head_type)
320	            else:
321	                allowed_dr = constraint.valid_tail_types()
322	        else:
323	            allowed_dr = None
324	
325	        tail_text = self.state.current_tail_text
326	        if tail_text:
327	            actual_type = self.state.entity_registry.get_type(tail_text)
328	            if actual_type and actual_type in self._type_first_token:
329	                if allowed_dr is None or actual_type in allowed_dr:
330	                    return self._apply_type_mask(logits, {actual_type})
331	
332	        if allowed_dr is not None:
333	            return self._apply_type_mask(logits, allowed_dr)
334	        return logits
335	
336	    def _apply_type_mask(
337	        self,
338	        logits: torch.FloatTensor,
339	        allowed_types: set[str],
340	    ) -> torch.FloatTensor:
341	        """Set logits of disallowed type first-tokens to -inf.
342	
343	        Only masks the FIRST token of each type string. XGrammar's grammar
344	        ensures remaining tokens are forced once the first is selected.
345	
346	        First-token uniqueness verified for Qwen3-8B:
347	          SciERC: Task(6262), Method(3523), Material(13415), Metric(54310),
348	                  OtherScientificTerm(11409), Generic(19964)
349	          DocRED: PER(9654), ORG(44927), LOC(12052), TIME(18129),
350	                  NUM(17488), MISC(44)
351	        """
352	        disallowed_first_tokens = [
353	            tid for etype, tid in self._type_first_token.items()
354	            if etype not in allowed_types
355	        ]
356	
357	        if disallowed_first_tokens:
358	            logits[disallowed_first_tokens] = float("-inf")
359	
360	        return logits
361	
362	    def reset(self):
363	        """Reset state between generate() calls."""
364	        self.state.reset()
365	
366	
367	# ── Integration Helper ───────────────────────────────────────────────────
368	
369	def build_constrained_processors(
370	    constraints_path: str,
371	    tokenizer: PreTrainedTokenizerBase,
372	    prompt_length: int,
373	) -> list[LogitsProcessor]:
374	    """Build the complete LogitsProcessor stack for constrained generation.
375	
376	    Returns a list suitable for LogitsProcessorList:
377	        [xgrammar_processor, type_constraint_processor]
378	
379	    Usage:
380	        processors = build_constrained_processors(
381	            "ontology_constraints.json", tokenizer, len(input_ids[0])
382	        )
383	        output = model.generate(**inputs, logits_processor=processors)
384	    """
385	    import xgrammar as xgr
386	    from .ontology_compiler import compile_ontology
387	
388	    spec, compiled_grammar = compile_ontology(constraints_path, tokenizer)
389	
390	    processors = []
391	
392	    if compiled_grammar is not None:
393	        grammar_processor = xgr.contrib.hf.LogitsProcessor(compiled_grammar)
394	        processors.append(grammar_processor)
395	
396	    type_processor = TypeConstraintProcessor(spec, tokenizer, prompt_length)
397	    processors.append(type_processor)
398	
399	    return processors
400	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95f35069-b083-4b65-9f29-eca7fba45041",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "23b6107c-763d-4276-bc2f-d50f66a7cbb6",
  "sourceToolAssistantUUID": "95f35069-b083-4b65-9f29-eca7fba45041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T02:46:11.904Z_

<details open><summary>🔧 Tool call — Read · `toolu_0192ZBPQFuYXxcB8BTCN2AX7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/compiler/ontology_compiler.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23b6107c-763d-4276-bc2f-d50f66a7cbb6",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UvMtUwMW2FYpa5AuVN",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "7dd30f71-5eb3-4446-99c4-e917f87586d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016H9VKUR9nL9uDi3zsXAQUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10060,
      "cache_read_input_tokens": 75136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10060,
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

_source line 54 · 2026-05-16T02:46:11.909Z_

<details><summary>↩ Tool result · `toolu_0192ZBPQFuYXxcB8BTCN2AX7`</summary>

```text
1	"""Ontology Schema -> Constraint Specification Compiler.
2	
3	Compiles an IE ontology schema (entity types, relation types, domain/range pairs)
4	into two constraint artifacts:
5	  1. EBNF grammar for XGrammar — enforces valid JSON structure + type vocabulary
6	  2. TypeConstraintSpec — semantic-level constraints for the LogitsProcessor
7	
8	Input:  ontology_constraints.json (entity types, relation types, valid head/tail pairs)
9	Output: ConstraintSpec (for TypeConstraintProcessor) + CompiledGrammar (for XGrammar)
10	Depends: xgrammar, transformers (tokenizer)
11	
12	Architecture: HF transformers + XGrammar (standalone).
13	- XGrammar handles structural constraints via EBNF grammar
14	- Custom LogitsProcessor handles semantic constraints (domain/range masking)
15	- Composed via LogitsProcessorList in model.generate()
16	"""
17	
18	from __future__ import annotations
19	
20	import json
21	from dataclasses import dataclass, field
22	from pathlib import Path
23	from typing import Optional
24	
25	
26	@dataclass
27	class RelationConstraint:
28	    """Domain/range constraint for a single relation type."""
29	    relation_type: str
30	    valid_pairs: list[tuple[str, str]]  # [(head_type, tail_type), ...]
31	
32	    def valid_head_types(self) -> set[str]:
33	        return {h for h, _ in self.valid_pairs}
34	
35	    def valid_tail_types(self) -> set[str]:
36	        return {t for _, t in self.valid_pairs}
37	
38	    def valid_tail_types_for_head(self, head_type: str) -> set[str]:
39	        return {t for h, t in self.valid_pairs if h == head_type}
40	
41	    def valid_head_types_for_tail(self, tail_type: str) -> set[str]:
42	        return {h for h, t in self.valid_pairs if t == tail_type}
43	
44	
45	@dataclass
46	class ConstraintSpec:
47	    """Complete constraint specification compiled from an ontology schema.
48	
49	    Used by both the EBNF grammar generator and the TypeConstraintProcessor.
50	    """
51	    entity_types: list[str]
52	    relation_types: list[str]
53	    relation_constraints: dict[str, RelationConstraint]
54	
55	    # Token-level mappings (populated by compile_for_tokenizer)
56	    entity_type_token_ids: dict[str, list[int]] = field(default_factory=dict)
57	    relation_type_token_ids: dict[str, list[int]] = field(default_factory=dict)
58	    # First-token mapping (populated by compile_type_constraints)
59	    entity_type_first_token: dict[str, int] = field(default_factory=dict)
60	
61	    def get_constraint(self, relation_type: str) -> Optional[RelationConstraint]:
62	        return self.relation_constraints.get(relation_type)
63	
64	
65	class OntologyCompiler:
66	    """Compiles ontology_constraints.json into constraint artifacts."""
67	
68	    def __init__(self, constraints_path: str | Path):
69	        with open(constraints_path) as f:
70	            self.raw = json.load(f)
71	        self.spec = self._build_spec()
72	
73	    def _build_spec(self) -> ConstraintSpec:
74	        entity_types = self.raw["entity_types"]
75	        raw_rtypes = self.raw["relation_types"]
76	
77	        # SciERC: list of strings; DocRED: dict of code->name
78	        if isinstance(raw_rtypes, dict):
79	            relation_types = list(raw_rtypes.keys())
80	        else:
81	            relation_types = raw_rtypes
82	
83	        relation_constraints = {}
84	        for rtype, rdata in self.raw["relation_constraints"].items():
85	            relation_constraints[rtype] = RelationConstraint(
86	                relation_type=rtype,
87	                valid_pairs=[(h, t) for h, t in rdata["valid_pairs"]],
88	            )
89	
90	        return ConstraintSpec(
91	            entity_types=entity_types,
92	            relation_types=relation_types,
93	            relation_constraints=relation_constraints,
94	        )
95	
96	    # ── EBNF Grammar Generation ──────────────────────────────────────────
97	
98	    def compile_ebnf(self) -> str:
99	        """Generate EBNF grammar for XGrammar.
100	
101	        Enforces:
102	        - Valid JSON structure (object with "entities" and "relations" arrays)
103	        - Entity type must be one of the defined types (enum constraint)
104	        - Relation type must be one of the defined types (enum constraint)
105	        - head_type / tail_type must be valid entity types
106	
107	        Does NOT enforce (handled by TypeConstraintProcessor at decode time):
108	        - Domain/range consistency (head_type, tail_type must match relation's valid_pairs)
109	        - Cross-reference consistency (entity mentioned in relation must exist in entities list)
110	        """
111	        entity_type_rule = " | ".join(
112	            f'"\\\"" "{etype}" "\\\"" ' for etype in self.spec.entity_types
113	        )
114	        relation_type_rule = " | ".join(
115	            f'"\\\"" "{rtype}" "\\\"" ' for rtype in self.spec.relation_types
116	        )
117	
118	        ebnf = f'''root ::= "{{" ws entities-field "," ws relations-field ws "}}"
119	
120	entities-field ::= "\\"entities\\"" ws ":" ws "[" ws entity-list? ws "]"
121	entity-list ::= entity ("," ws entity)*
122	entity ::= "{{" ws "\\"text\\"" ws ":" ws json-string "," ws "\\"type\\"" ws ":" ws entity-type ws "}}"
123	
124	relations-field ::= "\\"relations\\"" ws ":" ws "[" ws relation-list? ws "]"
125	relation-list ::= relation ("," ws relation)*
126	relation ::= "{{" ws "\\"head\\"" ws ":" ws json-string "," ws "\\"tail\\"" ws ":" ws json-string "," ws "\\"type\\"" ws ":" ws relation-type "," ws "\\"head_type\\"" ws ":" ws entity-type "," ws "\\"tail_type\\"" ws ":" ws entity-type ws "}}"
127	
128	entity-type ::= {entity_type_rule}
129	relation-type ::= {relation_type_rule}
130	
131	json-string ::= "\\"" json-char* "\\""
132	json-char ::= [^"\\\\] | "\\\\" ["\\\\/bfnrt] | "\\\\u" [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F]
133	
134	ws ::= [ \\t\\n]*
135	'''
136	        return ebnf
137	
138	    # ── JSON Schema Generation ───────────────────────────────────────────
139	
140	    def compile_json_schema(self) -> dict:
141	        """Generate JSON Schema for XGrammar's from_json_schema.
142	
143	        XGrammar 2.0 can compile JSON Schema directly, often more
144	        efficiently. Uses enum constraints for type fields.
145	        """
146	        entity_schema = {
147	            "type": "object",
148	            "properties": {
149	                "text": {"type": "string"},
150	                "type": {"type": "string", "enum": self.spec.entity_types},
151	            },
152	            "required": ["text", "type"],
153	            "additionalProperties": False,
154	        }
155	
156	        relation_schema = {
157	            "type": "object",
158	            "properties": {
159	                "head": {"type": "string"},
160	                "tail": {"type": "string"},
161	                "type": {"type": "string", "enum": self.spec.relation_types},
162	                "head_type": {"type": "string", "enum": self.spec.entity_types},
163	                "tail_type": {"type": "string", "enum": self.spec.entity_types},
164	            },
165	            "required": ["head", "tail", "type", "head_type", "tail_type"],
166	            "additionalProperties": False,
167	        }
168	
169	        return {
170	            "type": "object",
171	            "properties": {
172	                "entities": {"type": "array", "items": entity_schema},
173	                "relations": {"type": "array", "items": relation_schema},
174	            },
175	            "required": ["entities", "relations"],
176	            "additionalProperties": False,
177	        }
178	
179	    # ── XGrammar Integration ─────────────────────────────────────────────
180	
181	    def compile_xgrammar(self, tokenizer) -> "xgrammar.CompiledGrammar":
182	        """Compile grammar for use with XGrammar's LogitsProcessor."""
183	        import xgrammar as xgr
184	
185	        tokenizer_info = xgr.TokenizerInfo.from_huggingface(
186	            tokenizer, vocab_size=tokenizer.vocab_size
187	        )
188	        compiler = xgr.GrammarCompiler(tokenizer_info)
189	
190	        schema_str = json.dumps(self.compile_json_schema())
191	        grammar = xgr.Grammar.from_json_schema(schema_str)
192	        return compiler.compile_grammar(grammar)
193	
194	    # ── Tokenizer Alignment ──────────────────────────────────────────────
195	
196	    def compile_for_tokenizer(self, tokenizer) -> ConstraintSpec:
197	        """Populate token-level mappings in the ConstraintSpec.
198	
199	        Maps each entity/relation type string to its full token ID sequence.
200	        """
201	        for etype in self.spec.entity_types:
202	            token_ids = tokenizer.encode(etype, add_special_tokens=False)
203	            self.spec.entity_type_token_ids[etype] = token_ids
204	
205	        for rtype in self.spec.relation_types:
206	            token_ids = tokenizer.encode(rtype, add_special_tokens=False)
207	            self.spec.relation_type_token_ids[rtype] = token_ids
208	
209	        return self.spec
210	
211	    # ── Type Constraint Compilation ──────────────────────────────────────
212	
213	    def compile_type_constraints(self, tokenizer) -> dict[str, int]:
214	        """Build entity_type -> first_token_id mapping from tokenizer.
215	
216	        Validates uniqueness: raises ValueError if two types share a first token.
217	        Pre-condition verified for Qwen3-8B on both SciERC and DocRED.
218	        """
219	        if not self.spec.entity_type_token_ids:
220	            self.compile_for_tokenizer(tokenizer)
221	
222	        first_tokens_seen: dict[int, str] = {}
223	
224	        for etype in self.spec.entity_types:
225	            token_ids = self.spec.entity_type_token_ids[etype]
226	            first_id = token_ids[0]
227	
228	            if first_id in first_tokens_seen:
229	                raise ValueError(
230	                    f"First-token collision: '{etype}' and "
231	                    f"'{first_tokens_seen[first_id]}' share first token ID {first_id}"
232	                )
233	            first_tokens_seen[first_id] = etype
234	            self.spec.entity_type_first_token[etype] = first_id
235	
236	        return dict(self.spec.entity_type_first_token)
237	
238	    def build_processor(
239	        self,
240	        tokenizer,
241	        prompt_length: int = 0,
242	    ) -> list:
243	        """Assemble complete LogitsProcessor stack: [XGrammar, TypeConstraint].
244	
245	        Returns list suitable for model.generate(logits_processor=...).
246	        """
247	        from .type_mask_processor import TypeConstraintProcessor
248	
249	        self.compile_type_constraints(tokenizer)
250	        compiled_grammar = self.compile_xgrammar(tokenizer)
251	
252	        import xgrammar as xgr
253	
254	        processors = []
255	        processors.append(xgr.contrib.hf.LogitsProcessor(compiled_grammar))
256	        processors.append(TypeConstraintProcessor(self.spec, tokenizer, prompt_length))
257	        return processors
258	
259	
260	# ── Convenience ──────────────────────────────────────────────────────────
261	
262	def compile_ontology(
263	    constraints_path: str | Path,
264	    tokenizer=None,
265	) -> tuple[ConstraintSpec, Optional["xgrammar.CompiledGrammar"]]:
266	    """One-call compilation: ontology JSON -> (ConstraintSpec, CompiledGrammar)."""
267	    compiler = OntologyCompiler(constraints_path)
268	    compiled_grammar = None
269	
270	    if tokenizer is not None:
271	        compiler.compile_type_constraints(tokenizer)
272	        compiled_grammar = compiler.compile_xgrammar(tokenizer)
273	
274	    return compiler.spec, compiled_grammar
275	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dd30f71-5eb3-4446-99c4-e917f87586d9",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "de7b847c-bdcd-4d25-ad8c-7797b94264b7",
  "sourceToolAssistantUUID": "7dd30f71-5eb3-4446-99c4-e917f87586d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-16T02:46:17.237Z_

Now let me check the writing plan and the dream reports for the most recent review-oriented analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de7b847c-bdcd-4d25-ad8c-7797b94264b7",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UvrqGoMDESJeB4BXoA",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "7838db41-39cc-44e8-bb54-ee345ef85b05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165wBFy5LAJPB2LyKj8ZrfA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9320,
      "cache_read_input_tokens": 85196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9320,
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

_source line 56 · 2026-05-16T02:46:19.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EoNHAMBRz6Vtysx3mXN5zv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7838db41-39cc-44e8-bb54-ee345ef85b05",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UvrqGoMDESJeB4BXoA",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "19fdb869-76be-4df9-9c11-bc9c7a23a570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165wBFy5LAJPB2LyKj8ZrfA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9320,
      "cache_read_input_tokens": 85196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9320,
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

_source line 57 · 2026-05-16T02:46:19.989Z_

<details><summary>↩ Tool result · `toolu_01EoNHAMBRz6Vtysx3mXN5zv`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{multirow}
6	\usepackage{xcolor}
7	\usepackage[hidelinks]{hyperref}
8	\usepackage[margin=1in]{geometry}
9	\usepackage{enumitem}
10	
11	\newcommand{\sys}{\textsc{OntoCoDec}}
12	\newcommand{\DR}{\textsc{dr}}
13	\newcommand{\RV}{\textsc{rv}}
14	\newcommand{\ET}{\textsc{et}}
15	\newcommand{\CF}{\textsc{cf}}
16	
17	\title{\sys{}: Type-Valid Information Extraction via\\Compiled Ontology Constraints}
18	
19	\author{Anonymous}
20	\date{}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	\begin{abstract}
27	% ============================================================
28	
29	Large language models applied to information extraction produce systematic ontology constraint violations---wrong entity types, out-of-vocabulary relations, and domain/range mismatches---at rates of 15--26\% per triple.
30	Prompt-level interventions reduce but cannot reliably eliminate these violations.
31	We present \sys{}, a framework that automatically compiles IE ontology schemas into two composable constraint layers for autoregressive decoding: a \emph{grammar layer} enforcing JSON structure and type vocabulary via context-free grammars, and a \emph{semantic layer} enforcing cross-field domain/range constraints through a stateful entity registry with dynamic logit masking.
32	The layers compose via bitwise AND of token masks with an enabling dependency: grammar ensures structural validity, which enables the semantic layer to enforce domain/range rules.
33	In zero-shot evaluation on SciERC and DocRED across two model families (Qwen3-8B, Llama-3.1-8B), \sys{} eliminates 90--99\% of domain/range violations.
34	Crucially, \sys{} is \emph{orthogonal to model improvement}: composed with LoRA fine-tuning on DocRED, it eliminates 94--100\% of residual violations with R-F1 change within $\pm$0.06 percentage points, while cross-field consistency violations collapse from 2.6--12.0\% to under 0.5\%.
35	This establishes guaranteed type-validity as a modular property that persists across training regimes.
36	
37	\end{abstract}
38	
39	% ============================================================
40	\section{Introduction}
41	\label{sec:intro}
42	% ============================================================
43	
44	Information extraction (IE) systems built on large language models (LLMs) achieve impressive coverage by framing extraction as text generation: given a document and an ontology schema describing target entity types and relation types with their domain/range constraints, the model generates structured output (e.g., JSON) listing extracted entities and relations.
45	However, the generative paradigm introduces a class of errors absent from traditional pipeline IE: \emph{ontology constraint violations}, where the model produces structurally invalid output that no correct extraction could contain.
46	
47	These violations are not rare edge cases. In our measurement across two standard IE benchmarks---SciERC (7 relation types) and DocRED (96 relation types)---and two 8B-parameter models (Qwen3-8B, Llama-3.1-8B), we find domain/range violation rates of 15--26\% per extracted triple in zero-shot settings. Violations concentrate on relation types with tight domain/range constraints rather than distributing uniformly, and comparable violation rates arise regardless of ontology size (SciERC 15.4\% vs.\ DocRED 18.7\% despite a 14$\times$ difference in relation count).
48	
49	Schema-informed prompting---explicitly describing domain/range constraints in the instruction---reduces but cannot eliminate violations. On SciERC, overall violation rate drops by 62\%, but three relation types retain double-digit violation rates. On DocRED, the reduction is only 32\%, confirming that prompt-level intervention scales poorly with ontology complexity. Worse, one SciERC relation type (\emph{Evaluate-for}) shows \emph{increased} violations under schema-informed prompting, due to conflict between the prompt-injected constraints and the model's distributional priors.
50	
51	We propose \sys{} (\textbf{Onto}logy-\textbf{Co}nstrained \textbf{Dec}oding), a framework that automatically compiles IE ontology schemas into decoder-level constraints. \sys{} consists of two composable layers:
52	\begin{enumerate}[nosep,leftmargin=*]
53	    \item A \textbf{grammar layer} that compiles ontology-derived type and relation vocabularies into a context-free grammar (CFG), enforcing valid JSON structure and ensuring every generated type/relation name belongs to the schema vocabulary.
54	    \item A \textbf{semantic layer} that maintains a stateful entity registry during generation and dynamically masks logits to enforce domain/range constraints---ensuring that each relation's argument types satisfy the ontology's type restrictions for that relation.
55	\end{enumerate}
56	The two layers compose via bitwise AND of their token masks at each decoding step, with an \emph{enabling dependency}: the grammar layer ensures every relation name is in the valid vocabulary, which is a prerequisite for the semantic layer to look up and enforce the corresponding domain/range rules.
57	
58	Our central finding is that \sys{} functions as a \emph{modular compliance layer} that is orthogonal to model improvement via fine-tuning. Applied to a zero-shot model, it eliminates 90--99\% of domain/range violations. Applied to a LoRA fine-tuned model, it eliminates 94--100\% of the smaller residual violations that fine-tuning alone cannot remove---at zero F1 cost. Fine-tuning improves extraction quality (R-F1 from $\sim$8\% to $\sim$41--44\%); \sys{} guarantees type validity. Neither intervention degrades the other. This composability resolves a practical concern: zero-shot F1 is too low for deployment, but adding fine-tuning for quality does not require abandoning constraint guarantees.
59	
60	A secondary finding is that cross-field consistency (CF) violations---where the same entity receives different types across relation contexts---collapse dramatically under fine-tuning (from 2.6--12.0\% to under 0.5\%). This reveals that CF was never an architectural limitation of \sys{}, but a consequence of applying per-relation type enforcement to a model with poorly calibrated type priors.
61	
62	\paragraph{Contributions.}
63	\begin{enumerate}[nosep,leftmargin=*]
64	    \item A systematic measurement of ontology constraint violations in LLM-based IE, revealing violation rates of 15--26\% that correlate with constraint tightness rather than ontology size.
65	    \item \sys{}, a two-layer constrained decoding framework with automatic ontology-to-constraint compilation, eliminating 90--100\% of domain/range violations across datasets and models.
66	    \item A composability analysis demonstrating that constrained decoding and fine-tuning are orthogonal: \sys{} eliminates residual violations from fine-tuned models at zero F1 cost, verified across two model families.
67	\end{enumerate}
68	
69	% ============================================================
70	\section{Background}
71	\label{sec:background}
72	% ============================================================
73	
74	\paragraph{IE as Structured Generation.}
75	Modern LLM-based IE formulates extraction as generating a JSON object containing entity and relation lists, conditioned on a document and an ontology schema. The schema defines valid entity types $\mathcal{E}$, relation types $\mathcal{R}$, and for each relation $r \in \mathcal{R}$, domain and range constraints $\text{dom}(r) \subseteq \mathcal{E}$ and $\text{ran}(r) \subseteq \mathcal{E}$ specifying which entity types may serve as subject and object.
76	
77	\paragraph{Ontology Constraint Violations.}
78	We identify four violation types in generated IE output:
79	\begin{itemize}[nosep,leftmargin=*]
80	    \item \textbf{Entity Type (\ET{})}: An entity is assigned a type not in $\mathcal{E}$.
81	    \item \textbf{Relation Vocabulary (\RV{})}: A relation uses a name not in $\mathcal{R}$.
82	    \item \textbf{Domain/Range (\DR{})}: A relation triple $(s, r, o)$ where $\text{type}(s) \notin \text{dom}(r)$ or $\text{type}(o) \notin \text{ran}(r)$.
83	    \item \textbf{Cross-Field (\CF{})}: The same entity span receives different types across its occurrences in different relation triples or between the entity list and relation triples.
84	\end{itemize}
85	\ET{} and \RV{} are vocabulary violations (token not in schema); \DR{} is a semantic violation (valid tokens in invalid combination); \CF{} is a consistency violation (valid per-triple, inconsistent globally).
86	
87	\paragraph{Grammar-Constrained Decoding.}
88	Grammar-constrained decoding restricts token generation to sequences accepted by a formal grammar. Given a CFG $G$ and the current generation prefix, only tokens leading to at least one valid completion under $G$ are permitted. Systems such as XGrammar implement this efficiently via precomputed token masks, enabling real-time enforcement during autoregressive generation. CFGs can enforce \ET{} and \RV{} constraints (valid vocabulary) but cannot express \DR{} constraints, which require cross-field state.
89	
90	% ============================================================
91	\section{\sys{} Framework}
92	\label{sec:method}
93	% ============================================================
94	
95	\sys{} takes an IE ontology schema as input and produces a constrained decoding configuration that enforces type-validity during autoregressive generation. The framework consists of two layers and a composition mechanism.
96	
97	\subsection{Grammar Layer}
98	\label{sec:grammar}
99	
100	The grammar layer compiles the ontology schema into a CFG that enforces: (1) valid JSON structure matching the expected IE output format, (2) entity type tokens restricted to $\mathcal{E}$, and (3) relation name tokens restricted to $\mathcal{R}$. Entity mention spans and other free-text fields are unconstrained.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19fdb869-76be-4df9-9c11-bc9c7a23a570",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "4a444f6c-04a0-4c65-8adb-3c79f2dd6435",
  "sourceToolAssistantUUID": "19fdb869-76be-4df9-9c11-bc9c7a23a570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-16T02:46:20.817Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JkLUgCxQ38D5Ks8nZ2XobR`</summary>

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
  "parentUuid": "4a444f6c-04a0-4c65-8adb-3c79f2dd6435",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UvrqGoMDESJeB4BXoA",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "3760bd5c-edf1-42f9-9632-4f550c87bf77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165wBFy5LAJPB2LyKj8ZrfA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9320,
      "cache_read_input_tokens": 85196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9320,
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

_source line 59 · 2026-05-16T02:46:20.830Z_

<details><summary>↩ Tool result · `toolu_01JkLUgCxQ38D5Ks8nZ2XobR`</summary>

```text
1	% Section 5 — Runtime Analysis
2	% Data source: artifacts/rebuttal/w3_runtime_report.md
3	% Per-document inference times from JSONL outputs (inference_time_seconds field).
4	% All runs on same single-GPU server (westd-16980), same vLLM/transformers stack.
5	
6	\subsection{Runtime Overhead}
7	\label{sec:runtime}
8	
9	Table~\ref{tab:runtime} reports per-document inference time for each configuration.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\setlength{\tabcolsep}{4pt}
15	\begin{tabular}{@{}lll rr@{}}
16	\toprule
17	\textbf{Model} & \textbf{Dataset} & \textbf{Mode} & \textbf{Avg (s)} & \textbf{Overhead} \\
18	\midrule
19	\multirow{3}{*}{Qwen}
20	  & \multirow{3}{*}{SciERC}
21	    & Unconstrained & 8.69 & --- \\
22	  & & Grammar       & 8.82 & $+$1.4\% \\
23	  & & Full (S1)     & 6.76 & $-$22.2\% \\
24	\cmidrule(l){2-5}
25	\multirow{2}{*}{}
26	  & \multirow{2}{*}{DocRED}
27	    & Unconstrained & 19.76 & --- \\
28	  & & Full (S1)     & 20.40 & $+$3.2\% \\
29	\midrule
30	\multirow{2}{*}{Llama}
31	  & SciERC
32	    & Unconstrained & 2.81 & --- \\
33	  & & Full (S1)     & 4.33 & $+$53.8\% \\
34	\cmidrule(l){2-5}
35	  & \multirow{2}{*}{DocRED}
36	    & Unconstrained & 18.16 & --- \\
37	  & & Full (S1)     & 20.52 & $+$13.0\% \\
38	\bottomrule
39	\end{tabular}
40	\caption{Per-document inference time (wall-clock seconds, same GPU).
41	Grammar-only overhead is $\leq$4.2\% (Qwen; Llama grammar-only not separately measured).
42	Post-hoc filtering is an $O(n)$ pass over predicted triples and adds negligible time.}
43	\label{tab:runtime}
44	\end{table}
45	
46	Overhead ranges from $-$22\% to $+$54\%, with three of four cells at $\leq$13\%; the outlier (Llama-SciERC, $+$53.8\%) is only $+$1.5\,s absolute.
47	Qwen-SciERC exhibits a \emph{speedup} ($-$22.2\%) because constrained decoding produces tighter outputs, avoiding long noisy continuations before EOS.
48	Grammar-only overhead is $\leq$4.2\% (Qwen), indicating the semantic layer's logit masking accounts for most incremental cost.
49	Llama grammar-only was not separately measured; because the grammar layer uses identical DFA construction across models, Qwen's $\leq$4.2\% provides a reasonable proxy.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3760bd5c-edf1-42f9-9632-4f550c87bf77",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "87c0b38d-2d66-4e24-ad00-ab136099d135",
  "sourceToolAssistantUUID": "3760bd5c-edf1-42f9-9632-4f550c87bf77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-16T02:46:24.113Z_

Now let me look at the decision log to understand the evolution of the project and key decisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87c0b38d-2d66-4e24-ad00-ab136099d135",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UwWVw3F8zViLDPNwh3",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "f315d44e-3873-483e-b227-7c496c2bc9e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GQMMrrfCD8wB9joSCa93h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3906,
      "cache_read_input_tokens": 94516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3906,
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

_source line 61 · 2026-05-16T02:46:24.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TbmDqNJ3hjWLHj4LfxsFDT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f315d44e-3873-483e-b227-7c496c2bc9e4",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UwWVw3F8zViLDPNwh3",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "33b7a613-d8ee-4df0-b33b-4b1dc7b4b8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GQMMrrfCD8wB9joSCa93h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3906,
      "cache_read_input_tokens": 94516,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 94516,
          "cache_creation_input_tokens": 3906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3906,
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

_source line 62 · 2026-05-16T02:46:24.988Z_

<details><summary>↩ Tool result · `toolu_01TbmDqNJ3hjWLHj4LfxsFDT`</summary>

```text
1	_next_id: 30
2	decisions:
3	- id: D001
4	  date: 2026-05-13 17:38 UTC
5	  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备
6	  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →
7	    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback
8	    思维，冲最高目标。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-13 19:14 UTC
13	  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值
14	  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate
15	    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for
16	    0.76%)，支持"特定 relation types 需要 decoding-time enforcement"的论文 claim。DocRED dry-run
17	    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认
18	    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'
19	  related_experiments:
20	  - exp_id: mvp_phase0_violation_rate
21	    role: primary
22	    result: domain_range_violation_rate=15.4%, go_nogo=GO
23	  depends_on:
24	  - D001
25	- id: D003
26	  date: 2026-05-13 21:48 UTC
27	  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验
28	  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation
29	    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1
30	    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1
31	    实验。
32	  related_experiments:
33	  - exp_id: mvp_phase0_violation_rate
34	    role: primary
35	    result: SciERC DR=15.4%, GO
36	  - exp_id: mvp_phase0_scierc_schema
37	    role: primary
38	    result: SciERC DR=5.78%, prompt insufficient
39	  - exp_id: mvp_phase0_violation_rate_docred
40	    role: primary
41	    result: DocRED DR=18.7%, GO
42	  depends_on:
43	  - D002
44	- id: D004
45	  date: 2026-05-14 01:53 UTC
46	  summary: Phase 2 SciERC 核心结果确认：grammar+semantic (full_s1) DR↓94% F1 neutral，两层约束协同效应成立
47	  rationale: _v2 干净数据 551 样本全量结果：full_s1 DR=0.93%（baseline 15.37%，↓94%），R-F1 微升 +0.0013。grammar
48	    单独消除 RV/ET，semantic 单独降 DR 24%，组合后 94%——超加性效应。论文核心 claim 站住。早期污染数据 semantic_only
49	    DR=16.43% 已修正为 11.65%。
50	  related_experiments:
51	  - exp_id: phase2_scierc_unconstrained
52	    role: baseline
53	    result: DR=15.37%
54	  - exp_id: phase2_scierc_grammar_only
55	    role: ablation
56	    result: DR=14.84%, RV/ET=0%
57	  - exp_id: phase2_scierc_semantic_only
58	    role: ablation
59	    result: DR=11.65%
60	  - exp_id: phase2_scierc_full_s1
61	    role: core_result
62	    result: DR=0.93%, F1=0.0836
63	  depends_on:
64	  - D003
65	- id: D005
66	  date: 2026-05-14 01:53 UTC
67	  summary: Phase 2 SciERC 核心结果确认：Full S1 DR↓94% F1无损，CF violation↑124x 作为已知 tradeoff
68	    待 S2 对比后决定处理策略
69	  rationale: v2 干净数据 551/551 全量验证，Reviewer PASS。Grammar+Semantic 协同效应成立，ablation story
70	    清晰。CF violation（0.08%→9.9%）是约束副作用，需等 S2 结果判断是在论文中作为 limitation 还是加 CF 约束修复。
71	  related_experiments:
72	  - exp_id: phase2_scierc_unconstrained
73	    role: baseline
74	    result: DR=15.37%, RV=1.39%, ET=0.4%, RF1=0.0823
75	  - exp_id: phase2_scierc_grammar_only
76	    role: ablation
77	    result: DR=14.84%, RV=0%, ET=0%, RF1=0.0823
78	  - exp_id: phase2_scierc_semantic_only
79	    role: ablation
80	    result: DR=11.65%, RV=1.51%, ET=0.4%, RF1=0.0815
81	  - exp_id: phase2_scierc_full_s1
82	    role: core_result
83	    result: DR=0.93%, RV=0%, ET=0%, RF1=0.0836, CF=9.9%
84	  depends_on: []
85	- id: D006
86	  date: 2026-05-14 01:54 UTC
87	  summary: Phase 2 SciERC 核心结果确认：Full S1 DR -94% 且 F1 无损，CF violation 上升为已知 limitation
88	  rationale: v2 干净数据全量（551/551）结果经 Reviewer PASS 验证：Full S1 DR 15.37%→0.93%（↓94%），R-F1
89	    +0.13pp，ET/RV→0%。Ablation story 清晰（grammar 管格式、semantic 管语义、双层协同）。CF violation
90	    从 0.08%→9.9% 是已知副作用，需在论文中正面报告并论述与 DR 的性质差异。Semantic-only DR=11.65% 说明两层是 multiplicative
91	    关系。决定推进 DocRED Phase 2 跨数据集验证 + 等 S2 对比。
92	  related_experiments:
93	  - exp_id: phase2_scierc_unconstrained
94	    role: baseline
95	    result: DR=15.37%, R-F1=0.0823
96	  - exp_id: phase2_scierc_grammar_only
97	    role: ablation
98	    result: DR=14.84%, RV/ET=0%, F1持平
99	  - exp_id: phase2_scierc_semantic_only
100	    role: ablation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33b7a613-d8ee-4df0-b33b-4b1dc7b4b8c2",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "47c22f0d-664f-4507-b737-94bba9ec9057",
  "sourceToolAssistantUUID": "33b7a613-d8ee-4df0-b33b-4b1dc7b4b8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-16T02:46:29.028Z_

I now have a thorough understanding of the paper. Let me also check if there are any additional analysis files or the dream review reports that might contain pre-submission review insights.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47c22f0d-664f-4507-b737-94bba9ec9057",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UwovvbQhoFn6dGxHkw",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "3f70bbea-0f19-4634-a841-e5c189760852",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHMurw5RQt7h8Sxn7MqNf6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2379,
      "cache_read_input_tokens": 98422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2379,
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

_source line 64 · 2026-05-16T02:46:30.107Z_

<details open><summary>🔧 Tool call — Read · `toolu_01URc43NckBUT7sv3ZQiwpuq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/median/paper.tex",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f70bbea-0f19-4634-a841-e5c189760852",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UwovvbQhoFn6dGxHkw",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "69452341-3447-447a-8734-7b75e0744c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHMurw5RQt7h8Sxn7MqNf6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2379,
      "cache_read_input_tokens": 98422,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 98422,
          "cache_creation_input_tokens": 2379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2379,
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

_source line 65 · 2026-05-16T02:46:30.117Z_

<details><summary>↩ Tool result · `toolu_01URc43NckBUT7sv3ZQiwpuq`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	\usepackage{natbib}
12	
13	\newcommand{\sys}{OntoCoDec}
14	\newcommand{\pp}{\text{pp}}
15	
16	\title{\sys{}: Type-Valid Information Extraction via Compiled Ontology Constraints}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	%==============================================================================
24	\begin{abstract}
25	%==============================================================================
26	Large language models (LLMs) applied to information extraction (IE) systematically violate ontology type constraints---generating triples where entity types fall outside the valid domain or range of the predicted relation.
27	We present the first systematic study of such violations, finding that LLM-based IE systems produce domain/range violations at rates of 15--26\% per triple, concentrated on relations with tight type constraints.
28	Schema-informed prompting reduces violations by up to 62\% but cannot eliminate them and scales poorly with ontology complexity.
29	We propose \sys{}, a framework that automatically compiles IE ontology schemas into two composable constraint layers for autoregressive decoding: (1)~a grammar layer enforcing structural and vocabulary validity via context-free grammars, and (2)~a semantic layer enforcing cross-field domain/range constraints through a stateful entity registry with dynamic logit masking.
30	The two layers compose via bitwise AND of token masks with an enabling dependency: the grammar layer ensures structural validity, enabling the semantic layer to enforce domain/range rules.
31	Evaluated on SciERC (7 relations) and DocRED (96 relations) with Qwen3-8B and Llama-3.1-8B in zero-shot settings, \sys{} eliminates 90--99\% of domain/range violations at zero or positive F1 impact.
32	In fine-tuned regimes, \sys{} composes with LoRA fine-tuning at negligible F1 cost ($\leq$0.5\pp{}), providing a residual compliance guarantee that fine-tuning alone cannot achieve.
33	\end{abstract}
34	
35	%==============================================================================
36	\section{Introduction}
37	\label{sec:intro}
38	%==============================================================================
39	
40	Information extraction (IE) aims to structure unstructured text into typed entities and relations conforming to a predefined ontology schema.
41	Recent work applies LLMs to IE in zero-shot or few-shot settings, leveraging their broad knowledge to extract structured information without task-specific training data.
42	However, LLM outputs frequently violate the ontology's type constraints: a relation such as \texttt{Feature-of} may require its head entity to be of type \texttt{Method} and its tail of type \texttt{Task}, yet LLMs routinely assign invalid types such as \texttt{OtherScientificTerm} or \texttt{Material}.
43	
44	We present the first systematic measurement of such constraint violations across two IE benchmarks of different scale: SciERC (7 relation types) and DocRED (96 relation types).
45	Our violation landscape study reveals three findings:
46	(1)~domain/range (DR) violations occur at non-trivial rates---15.4\% on SciERC and 18.5--26.1\% on DocRED depending on the model---despite correct relation names;
47	(2)~violations are \emph{not} uniformly distributed but concentrate on relations with tight type constraints (e.g., \texttt{Compare} at 42.4\%, \texttt{Feature-of} at 33.5\%), while loose-constraint relations show near-zero violation;
48	(3)~schema-informed prompting reduces overall violations by up to 62\% but is unreliable at the per-relation level, with some relations \emph{increasing} in violation rate.
49	
50	Motivated by these findings, we propose \sys{}, a framework that automatically compiles ontology schemas into decoding-time constraints.
51	\sys{} contributes:
52	\begin{itemize}
53	  \item A \textbf{violation landscape study} establishing that LLM-based IE systematically violates type constraints, with violation rate driven by constraint tightness interacting with model vocabulary compliance.
54	  \item A \textbf{composable two-layer constraint framework}: a grammar layer (CFG-based) for structural and vocabulary validity, and a semantic layer (stateful logit masking) for cross-field domain/range enforcement.
55	  \item \textbf{Extensive evaluation} on 2 datasets $\times$ 2 models $\times$ multiple configurations (zero-shot unconstrained, constrained, fine-tuned, fine-tuned+constrained, post-hoc filtering), with bootstrap confidence intervals.
56	\end{itemize}
57	
58	%==============================================================================
59	\section{Background}
60	\label{sec:background}
61	%==============================================================================
62	
63	\paragraph{Grammar-Constrained Decoding.}
64	Grammar-constrained decoding restricts an LLM's output to conform to a context-free grammar (CFG) by masking logits at each decoding step.
65	Systems such as XGrammar compile grammars into efficient token-level masks, enabling structured output (e.g., valid JSON) without fine-tuning.
66	However, CFG-expressible constraints are purely local---they cannot enforce cross-field semantic constraints such as ``if the relation is \texttt{Feature-of}, then the head entity type must be \texttt{Method}.''
67	
68	\paragraph{IE Ontology Structure.}
69	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \mathcal{C})$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and type constraints $\mathcal{C}$.
70	Each constraint $c_r \in \mathcal{C}$ specifies valid domain (head) and range (tail) entity types for relation $r$: $c_r = (\text{dom}(r) \subseteq \mathcal{E}, \text{ran}(r) \subseteq \mathcal{E})$.
71	We define the \emph{constraint tightness} $\tau_r = 1 - \frac{|\text{dom}(r)| \cdot |\text{ran}(r)|}{|\mathcal{E}|^2}$ to quantify how restrictive a relation's type constraints are.
72	
73	%==============================================================================
74	\section{Violation Landscape Study}
75	\label{sec:landscape}
76	%==============================================================================
77	
78	We measure four violation types in LLM-generated IE outputs:
79	\begin{itemize}
80	  \item \textbf{Domain/Range (DR)}: Entity type not in the valid domain or range of the predicted relation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69452341-3447-447a-8734-7b75e0744c53",
  "isSidechain": true,
  "promptId": "f8f3d660-ad25-4bf6-8c5f-89c7ddc21fe7",
  "agentId": "acf141a1713b1b57e",
  "type": "user",
  "uuid": "e3b67c6e-ae68-4e5a-939b-9a76dec3b883",
  "sourceToolAssistantUUID": "69452341-3447-447a-8734-7b75e0744c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-16T02:48:16.593Z_

I have now read through the complete paper, all supporting materials, the project framing documents, the code implementation, the related work sections (both main and appendix), and the bibliography. I have a comprehensive understanding of the paper's contributions, claims, and positioning. Let me now write the review.

## R2 Review: Novelty and Related Work

### Summary
This paper presents OntoCoDec, a two-layer constrained decoding framework that compiles IE ontology schemas into grammar-level (CFG for structural/vocabulary validity) and semantic-level (stateful entity registry with dynamic logit masking for domain/range enforcement) constraints, composed via bitwise AND of token masks. The paper also provides a systematic measurement of ontology constraint violation rates (15-26%) in LLM-based IE and introduces a constraint tightness metric to explain violation distribution. Evaluated on SciERC and DocRED across Qwen3-8B and Llama-3.1-8B, OntoCoDec achieves 45-99% DR reduction at neutral or positive F1 impact, and demonstrates composability with LoRA fine-tuning.

### Strengths

1. **Well-motivated problem formulation with novel empirical contribution.** The violation landscape study (Section 5.1) is genuinely the first systematic measurement of ontology type constraint violations in LLM-based IE. The finding that violation rates are driven by constraint tightness rather than ontology size is non-obvious and practically useful. The counter-intuitive result that schema-informed prompting can increase violations for specific relations (Evaluate-for +5.8pp) strengthens the motivation.

2. **Extensive and honest related work.** The paper covers five distinct paradigms in the extended related work (grammar-constrained decoding, semantic constrained decoding for code, vocabulary/type-constrained generation, post-hoc ontology validation, and quality impact of constrained decoding). The positioning against the code generation constrained decoding literature (Synchromesh, PICARD, MGD, PLDI'25 type-constrained codegen) is well-articulated and identifies the genuine technical distinction: IE requires a dynamically populated entity registry during generation rather than a fixed schema known prior to decoding.

3. **Clean ablation design revealing non-trivial interaction.** The enabling dependency between grammar and semantic layers is not just claimed but empirically demonstrated: semantic-only achieves only 24% DR reduction (SciERC) because it encounters out-of-vocabulary relation types with no constraint rules. The DocRED grammar-only result where DR *increases* (18.46% to 26.17%) because grammar forces OOV relations to valid names whose constraints are then violated is a genuinely insightful finding that reveals the non-trivial nature of the two-layer interaction.

4. **Proactive disclosure of CF trade-off with principled analysis.** The paper does not hide the cross-field consistency violation problem (up to 12.02% on Llama DocRED). The CF-DR trade-off analysis with an actual ablation (Table in Appendix, showing that eliminating CF re-routes violations to DR, +13.85pp) is a substantive contribution to understanding composable constraint systems. The identification of the dual mechanism (registry override vs. grammar-first fallback) adds technical depth.

5. **Composability with fine-tuning is a strong practical result.** Demonstrating that OntoCoDec achieves DR=0% when composed with LoRA fine-tuning on SciERC, at effectively zero F1 cost (-0.09pp), with CF collapsing from 9.90% to 1.18%, addresses the most natural practical objection ("just fine-tune instead"). This is validated across two model families.

6. **Pair-based sequential enforcement is technically precise.** The observation that most ontology type signatures are non-rectangular (0/7 SciERC, 73/96 DocRED), and that independent domain/range checking would over-permit 33-37% spurious type pairs, justifies the sequential head-then-tail masking strategy as genuinely tighter than the naive approach. This is a small but rigorous technical contribution.

### Weaknesses

1. **The grammar layer is entirely standard; the semantic layer is a logit mask with a hash map.** The grammar layer is direct application of XGrammar to IE schemas -- the paper acknowledges this. The semantic layer's core mechanism is a dictionary (entity name to type) populated during generation, consulted to construct a logit mask at type-bearing positions. While the engineering integration is competent, the individual technical components are each straightforward. The novelty rests on the *combination* and the *IE-specific application*, not on any individual algorithmic contribution. This places the paper in the "well-executed systems paper with empirical contribution" category rather than "technical novelty" category.

2. **The decidability taxonomy is superficial.** The three-level taxonomy (local, prefix-decidable, non-local) in Section 4 is presented as a conceptual contribution but amounts to a restatement of known formal language theory concepts (context-free vs. context-sensitive vs. truly context-dependent) applied to IE constraints. It does not include any formal proofs, complexity analysis, or surprising categorization. Calling forward coreference "non-local" and domain/range checking "prefix-decidable" is accurate but not novel -- these observations would be apparent to anyone with basic formal language theory background.

3. **Constraint tightness metric is obvious once stated.** The metric tau_r = 1 - |valid_pairs| / |E|^2 is a natural normalized measure of constraint restrictiveness. While it usefully predicts violation distribution, it is not a methodological contribution in itself -- it is essentially the complement of the fraction of the type-pair space that is valid. The dual-factor regression (tightness x baseline RV predicts residual DR with R^2=0.886) is fitted on only 4 data points, which is insufficient for any statistical claim about the relationship.

4. **Missing critical related work in structured prediction with constraints.** The paper does not discuss:
   - **CRF/structured perceptron with hard constraints** for joint NER+RE (e.g., Ratinov and Roth 2009; Finkel et al. 2005 for enforcing consistency constraints in NER; Singh et al. 2013 for joint inference with constraints). The tradition of enforcing relational type constraints in structured prediction predates LLMs and should be acknowledged.
   - **Schema-guided dialogue systems** (e.g., SGD benchmark, Rastogi et al. 2020) that enforce slot-value constraints during generation. While a different task, the mechanism of constraining generation to schema-valid values is directly relevant.
   - **BoostCD/BoostIE (EMNLP 2025)** is mentioned in the Idea Brief's landscape but conspicuously absent from the paper's related work and bibliography. This is a significant omission given that it directly addresses constrained vs. unconstrained decoding for IE and demonstrates error complementarity.
   - **SynCode (ICML 2024, Ugare et al.)** -- a grammar-augmented constrained decoding system that handles context-free and context-sensitive constraints through attribute grammars. This is mechanistically very close to OntoCoDec's approach of extending CFG constraints with semantic state.
   - **IterGen (ICLR 2025, Ugare et al.)** -- extends grammar-guided generation with semantic backtracking via KV cache restoration. This demonstrates a more sophisticated approach to handling grammar-semantic conflicts than OntoCoDec's graceful degradation (fallback to grammar-only), and should be discussed as an alternative design point.

5. **The "migration from code to IE" framing undersells the simplification.** The paper claims to "migrate the type-constrained decoding paradigm from code generation to IE" (Appendix related work). However, code type systems involve subtyping hierarchies, parametric polymorphism, scope rules, and deep inference -- while IE ontologies have flat domain/range sets with no inheritance. This migration is conceptually interesting but technically represents a substantial *simplification* of the code domain methods, not an extension. The paper does acknowledge this difference but should be more explicit that the IE instantiation is significantly less technically challenging than its code-domain inspirations.

6. **Scope is narrow despite claims of generality.** The paper evaluates on two datasets with very small type vocabularies (6 entity types each). The assumption that each entity type maps to a unique first subword token is explicitly stated as verified only for these two ontologies. For ontologies with dozens or hundreds of entity types (e.g., Wikidata's fine-grained types), this assumption would fail, requiring prefix-tree masking that "we have not implemented" (Limitations section). This significantly limits the practical applicability of the current system despite the paper's framing as an "automatic ontology-to-constraint compiler."

7. **Two 8B models only, zero-shot F1 of ~8%.** The evaluation covers only two 8B-class models. While the LoRA composability experiment raises F1 to ~44%, the core constrained decoding evaluation operates at ~8% F1 where the practical significance of constraint enforcement is questionable -- if 92% of triples are wrong anyway, the value of ensuring the remaining 8% are type-valid is limited. The paper addresses this by framing F1 as a control variable, which is fair, but the lack of evaluation on models that produce meaningful extraction quality (70B+, or fine-tuned models with >30% F1) weakens practical significance.

### Questions for Authors

1. How does the system handle ontologies with non-unique first subword tokens across entity types? The paper acknowledges this limitation but provides no solution. Has this been tested on any ontology beyond SciERC and DocRED's 6-type vocabularies?

2. The dual-factor regression (R^2=0.886) is fit on exactly 4 points. Can you provide additional data points (e.g., from different prompting strategies, additional models, or synthetic ontologies with varying tightness) to support this claimed pattern?

3. Why is BoostCD/BoostIE (EMNLP 2025) not discussed in the related work? It directly addresses the constrained decoding trade-off for IE and demonstrates complementary error modes -- a finding that directly relates to your grammar-semantic interaction analysis.

4. The CF-DR trade-off analysis shows that total violations (DR+CF) under your best configuration are 10.83% on SciERC zero-shot. Under unconstrained decoding, DR alone is 15.37% but CF is only 0.08%. How do you argue that 10.83% total violations (DR+CF) is preferable to 15.45% (DR+CF unconstrained), given that CF violations are described as "milder" and DR is reduced by 94%? Is the net violation reduction actually 15.45% to 10.83%, only a 30% relative improvement when counting both violation types?

5. How does the grammar-first fallback rate vary across relation types? You report an aggregate 10.2% fallback rate on DocRED -- is this concentrated on the same high-tightness relations, or is it spread across the ontology?

6. The paper's framing increasingly emphasizes composability with fine-tuning (especially in the "best" dream report). But the composability experiment is only on SciERC with LoRA. Can you demonstrate this on DocRED with fine-tuning, where the residual DR is much higher (10.21% for Qwen)?

### Missing Related Work

1. **BoostCD/BoostIE (Zhang et al., EMNLP 2025)**: Combines constrained and unconstrained decoding for closed IE via learned boosting. Directly relevant as it addresses error complementarity between constrained and unconstrained decoding for IE.

2. **SynCode (Ugare et al., ICML 2024)**: Uses attribute grammars with semantic augmentation for constrained generation. Mechanistically close to OntoCoDec's grammar + semantic state approach.

3. **IterGen (Ugare et al., ICLR 2025)**: Grammar-guided generation with semantic backtracking. Provides a more sophisticated alternative to the graceful degradation strategy.

4. **Classical structured prediction with constraints**: Roth and Yih (2004) is cited but the broader tradition of constrained structured prediction (CRFs with hard constraints, ILP-based joint inference for NER+RE) is not adequately covered. Work by Ratinov and Roth (2009), Singh et al. (2013) on joint constrained inference is relevant context.

5. **Schema-guided dialogue** (Rastogi et al., AAAI 2020 -- SGD dataset): Constraining generation to schema-valid slot values during dialogue is a closely related paradigm.

6. **DeepStruct (Wang et al., 2022)** and **USM (Lou et al., ACL 2023)**: Universal structured generation frameworks for IE that handle schema constraints through model architecture.

### Detailed Assessment

The paper's novelty profile is uneven. The strongest novelty claim is the violation landscape study -- this is a genuine empirical contribution that no prior work provides, and the finding about constraint tightness as the driver (rather than ontology size) is non-obvious. The constraint tightness metric itself, while simple, provides a useful predictive framework for practitioners.

The technical novelty of OntoCoDec is moderate. The grammar layer is explicitly standard (XGrammar applied to IE). The semantic layer's core mechanism -- a hash map entity registry consulted to construct logit masks at specific JSON field positions -- is sound engineering but not technically deep. The composition via bitwise AND is straightforward. The graceful degradation (fallback to grammar-only when semantic mask conflicts) is a reasonable engineering choice but not novel. The paper's claim to "migrate" type-constrained decoding from code to IE is accurate but, as noted, represents simplification rather than extension.

The decidability taxonomy adds little. Anyone familiar with formal language theory would categorize these constraints identically. The taxonomy's value is pedagogical rather than technical, and it does not yield any non-obvious design decisions -- the grammar layer handles CFG-expressible constraints and the semantic layer handles prefix-decidable ones, exactly as one would expect.

Where the paper genuinely excels is in the thoroughness of its experimental evaluation and the honesty of its analysis. The five-way ablation, cross-model validation, composability with fine-tuning, post-hoc filtering comparison, per-relation breakdown, CF-DR trade-off analysis with ablation, and bootstrap confidence intervals collectively represent a very strong empirical contribution. The finding that the grammar layer *reveals* latent violations on DocRED (DR increases from 18.46% to 26.17% under grammar-only) is a genuinely insightful observation about the interaction between structural and semantic constraint enforcement.

The related work coverage in the appendix is broad and generally well-positioned, but the omission of BoostCD/BoostIE is a notable gap given its direct relevance. The paper clearly differentiates from KGC type constraint work and from post-hoc validation approaches. The differentiation from PICARD (fixed schema vs. dynamically populated entity registry) is well-articulated.

The practical significance is limited by the narrow scope: two 6-type ontologies, two 8B models, zero-shot F1 of ~8%. The composability with fine-tuning partly addresses this, but is validated on only one dataset. The first-subword-token uniqueness assumption is a real scalability limitation. The paper is honest about these limitations but they constrain the impact of the work.

Overall, this is a well-executed empirical paper with a competent engineering contribution. The violation landscape study is the strongest novel contribution. The technical approach, while sound, does not introduce new algorithmic ideas -- it combines existing primitives (grammar-constrained decoding, logit masking, entity registry) in a straightforward way for the IE domain. The evaluation is thorough and honest. For a top venue, the novelty bar is borderline: the problem is real and the solution works, but the technical depth is limited and the scope is narrow.

### Score: 4/6
### Confidence: 4/5

A score of 4 (Borderline Accept) reflects that the paper makes a genuine empirical contribution (violation landscape study) and provides a competent, well-evaluated system (OntoCoDec) that addresses a real problem. The thorough evaluation with honest disclosure of limitations is commendable. However, the technical novelty is limited -- the individual components are standard, the composition is straightforward, and the decidability taxonomy is superficial. The missing related work (especially BoostCD/BoostIE, SynCode, and IterGen) is a concern that should be addressed. The narrow scope (two small ontologies, two 8B models) limits practical significance claims. At a venue with ~25% acceptance rate, this paper is competitive but faces risk from reviewers who prioritize algorithmic novelty over empirical thoroughness. If the authors address the missing related work and clarify the technical differentiation from SynCode/IterGen, the paper would be strengthened. The composability with fine-tuning result is the paper's strongest card for practical significance and should be more prominently featured.

### Critical Files for Implementation
- /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3b67c6e-ae68-4e5a-939b-9a76dec3b883",
  "isSidechain": true,
  "agentId": "acf141a1713b1b57e",
  "requestId": "req_011Cb5UxBuWsCEFBi34va6c9",
  "attributionAgent": "Plan",
  "type": "assistant",
  "uuid": "f8995c71-960d-4177-a360-1872800c1ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "b6ffaff3-ff01-4c89-a912-e4c7491ed48f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJMouFcXMKpjsmKXQf6RBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1993,
      "cache_read_input_tokens": 100801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1993,
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
