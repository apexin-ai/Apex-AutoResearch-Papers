# Research conversation: I need you to help me write a complete revised research idea JSON. I'll provide the context and you should output ONLY t

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a722d76f9a9e9176c.jsonl`
- **Structured JSON:** [`f95485415a135de504f9.json`](../../sessions/f9/f95485415a135de504f9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-12T00:16:23.546Z_

I need you to help me write a complete revised research idea JSON. I'll provide the context and you should output ONLY the JSON object.

## Context

This is a research idea about ontology-faithful information extraction via compiled semantic constraints. It's been through 4 review rounds with scores stagnating at 3.2-3.5. The reviewer's round 4 feedback identified 5 specific issues:

1. **TIMELINE RISK**: Only 14 days remain (deadline May 25), not enough for GoLLIE baseline, ACE05 events, and full experiments
2. **GoLLIE BASELINE COST**: Porting GoLLIE to Qwen3-8B and Llama-3.1-8B is prohibitively expensive (40-80 H100-hours)
3. **ACE05 EVENT ONTOLOGY COMPLEXITY**: 33 event types with typed argument roles is too complex for the core contribution
4. **VIOLATION RATE DE-RISKING**: Need a Day 1 pilot to measure violation rates before committing to full implementation
5. **MISSING RELATED WORK**: ODKE+ (Apple), DocRE-TCGL, and BoostCD/BoostIE

## My research findings

1. **ODKE+ (Apple, arXiv Sep 2025)**: Production system using soft prompting with dynamically generated ontology snippets, achieving 98.8% precision on 19M facts from 9M Wikipedia pages across 195 predicates. Uses soft ontology guidance (prompt-based) rather than hard decoding constraints. Key contrast: soft prompting cannot guarantee type compliance, our approach provides hard guarantees.

2. **DocRE-TCGL (Neural Networks, 2025)**: Uses entity type constraints for document-level RE at training time. Constructs a Type-Constrained Graph between entity types and relations + Type-Constrained Loss. Evaluated on DocRED/DWIE. Training-time approach, complementary to our decoding-time enforcement.

3. **BoostCD/BoostIE (EMNLP 2025)**: Combines constrained and unconstrained decoding via boosting for closed IE. Phase 1: decode twice (constrained + unconstrained). Phase 2: learned boosted model combines predictions. Found that errors from constrained vs unconstrained modes are complementary. Used FlanT5-base (~250M params). Error analysis found 9% misclassified entity errors, 60% unrelated triplets in SynthIE unconstrained mode. Key difference from our approach: requires training a boosted model, doesn't handle ontology type constraints, focuses on vocabulary membership not cross-field type consistency.

4. **GoLLIE published results**: Code-Llama-based (7B/13B/34B). ACE05 supervised: RE F1 = 63.6 (7B), 67.5 (13B), 70.1 (34B). No SciERC evaluation. Checkpoints available on HuggingFace.

5. **SciERC SOTA**: Fine-tuned LLMs achieve ~0.44 F1 (Qwen3-14B-Base), comparable to graph-based parsers (0.35 F1 with 124M params).

6. **Format Tax (arXiv Apr 2026)**: Prompt-level effects cause ~70% of quality loss; decoder-level grammar masking only ~30%. Key insight: decouple reasoning from formatting. Validates our S2 two-pass approach.

7. **vLLM V1 LogitsProcessor**: Well-documented API with clear examples. Custom processors subclass LogitsProcessor, implement apply() on (num_requests × vocab_size) tensors.

## Changes to make (MAJOR REVISION):

### Problem framing changes:
- Add BoostCD/BoostIE to the landscape as a key comparison point (combines constrained+unconstrained for IE, but doesn't handle cross-field type constraints)
- Add ODKE+ as the "soft constraint" production alternative
- Add DocRE-TCGL as training-time entity type constraint approach
- Emphasize that violation rate quantification is a first-order contribution regardless of outcome
- Frame the Day 1 pilot as a methodological innovation (de-risking before engineering investment)

### Approach changes:
- **Phase 0 (Day 1-2): Violation rate pilot study.** Run unconstrained Qwen3-8B and Llama-3.1-8B on ACE05 and SciERC test sets. Write a lightweight Python script to check outputs against ontology type constraints. If >5%, proceed with full implementation. If <5%, pivot to "negative result + guaranteed compliance tool" framing.
- **GoLLIE: demote to discussion comparison.** Use GoLLIE's published Code-Llama-34B numbers on ACE05 (RE F1 = 70.1) for comparison in discussion section. Do NOT retrain on Qwen3/Llama. Add as a "complementarity" discussion point.
- **ACE05 events: stretch goal.** Core contribution uses entity+relation constraints only (both ACE05 and SciERC). Event constraints are a stretch goal.
- **Revised timeline:** Day 1-2: pilot. Day 2-6: compiler + LogitsProcessor for entity+relation. Day 6-10: experiments (S1, S2, baselines). Day 10-14: ablations + paper + optional events.
- **Drop S3 (DCCD-style)** entirely — it was already marked as optional/stretch and adds complexity without core contribution.
- **Revised baselines**: (1) Unconstrained generation, (2) JSON-only grammar constraints, (3) Post-hoc type filtering, (4) GoLLIE published numbers (discussion comparison). Drop GoLLIE as an empirical baseline requiring retraining.

### Resource estimate changes:
- Reduce GPU hours significantly (no GoLLIE training, events as stretch)
- Tighten timeline to 14 days
- Reduce compute budget

Now write the COMPLETE JSON object. Use this exact schema:

```json
{
  "title": "...",
  "core_problem": "...",
  "opportunity": "...",
  "landscape": "...",
  "approach": "...",
  "resource_estimate": { "manual": {...}, "human_in_loop": {...}, "auto_research": {...} },
  "target_venues": [...],
  "level": "...",
  "key_references": [...],
  "description": "...",
  "project_name": "schema_semantic_constrained_ie",
  "source": "web_research",
  "change_type": "major"
}
```

Key requirements:
- The title should stay similar but can be refined
- core_problem should incorporate the de-risking framing
- opportunity should be updated with the new related work
- landscape should include BoostCD/BoostIE, ODKE+, DocRE-TCGL prominently
- approach should have the phased structure with Day 1 pilot
- resource_estimate should be realistic for the reduced scope
- key_references should add the new papers
- description should be a comprehensive summary
- change_type should be "major"

Make the landscape, approach, and description sections thorough and detailed - these are the most important parts. Don't truncate or abbreviate. The landscape especially should comprehensively cover all related work categories.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1ab5696c-ad9e-499a-bed0-2d9b8c629ea9",
  "agentId": "a722d76f9a9e9176c",
  "type": "user",
  "uuid": "3739502d-6eb3-4210-afd5-cb63048f32b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "00137b04-bbf3-4563-97d2-72b98f97712d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:16:23.553Z_

```json
{
  "parentUuid": "3739502d-6eb3-4210-afd5-cb63048f32b5",
  "isSidechain": true,
  "agentId": "a722d76f9a9e9176c",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "51afe53f-5a5f-4749-9dea-982492568192",
  "timestamp": "2026-05-12T00:16:23.553Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "00137b04-bbf3-4563-97d2-72b98f97712d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:18:31.249Z_



Here is the complete revised research idea JSON:

```json
{
  "title": "Ontology-Faithful Information Extraction via Compiled Semantic Constraints",
  "core_problem": "Current LLM-based information extraction systems generate outputs that violate ontology type constraints (e.g., assigning a PERSON entity as the instrument of a relation that requires a WEAPON, or extracting relation types incompatible with the entity types of their arguments). These violations are invisible at the JSON-syntax level — outputs are well-formed JSON but semantically inconsistent with the target ontology. The prevalence and impact of these violations remain unquantified: no prior work has systematically measured violation rates across models, datasets, and ontology complexity levels. Without this empirical grounding, the field cannot assess whether constraint enforcement is a critical necessity or an over-engineered solution. This project therefore treats violation rate quantification as a first-order contribution, using a Day 1 pilot study to measure violation prevalence before committing engineering effort to constraint enforcement. If violation rates exceed 5%, the compiled constraint approach is justified; if they fall below 5%, the project pivots to a negative-result framing with a guaranteed-compliance tool as a safety-net contribution.",
  "opportunity": "Three converging developments create a timely opportunity. First, the vLLM V1 engine exposes a well-documented LogitsProcessor API that enables custom token-level interventions on (num_requests × vocab_size) tensors, making it practical to enforce semantic constraints at decoding time without modifying model internals. Second, recent work on the 'format tax' (arXiv Apr 2026) demonstrates that prompt-level effects account for ~70% of quality loss from structured output requirements while decoder-level grammar masking contributes only ~30%, validating our two-pass (S2) approach that decouples reasoning from formatting. Third, the landscape of ontology-constrained IE has matured rapidly — ODKE+ (Apple, 2025) demonstrates production-scale soft ontology guidance achieving 98.8% precision on 19M facts but cannot guarantee type compliance, BoostCD/BoostIE (EMNLP 2025) shows that constrained and unconstrained decoding errors are complementary but requires training a boosted combiner model, and DocRE-TCGL (Neural Networks, 2025) enforces entity type constraints at training time but not at inference. No existing system compiles full ontology type constraints (entity type validity, relation domain/range restrictions, cross-field type consistency) into a finite-state machine applied at decoding time. This gap — between soft/training-time constraints and hard/decoding-time guarantees — is precisely what compiled semantic constraints fill.",
  "landscape": "The landscape of ontology-aware information extraction spans five categories, each addressing a different facet of the constraint enforcement problem.\n\n**1. Grammar-Constrained Decoding (Syntax-Only).** Tools like Outlines, llama.cpp GBNF grammars, and Guidance enforce JSON schema compliance at the token level using finite-state automata or context-free grammars. These systems guarantee syntactic well-formedness (valid JSON, correct field names, proper nesting) but are ontology-agnostic — they cannot enforce that a relation's argument types are compatible with the relation's domain/range constraints. The gap between syntactic and semantic validity is the core motivation for this work.\n\n**2. Soft Ontology Guidance (Prompt-Based).** ODKE+ (Apple, arXiv Sep 2025) represents the production frontier of prompt-based ontology guidance. It uses soft prompting with dynamically generated ontology snippets, processing 9M Wikipedia pages across 195 predicates to extract 19M facts at 98.8% precision. The system demonstrates that ontology-aware prompting scales impressively, but soft guidance cannot provide hard guarantees — the model may still generate type-violating outputs, and the violation rate is unreported. GoLLIE (EMNLP 2023) takes a code-generation approach, representing ontology schemas as Python class definitions and fine-tuning Code-Llama models (7B/13B/34B) to generate instances. GoLLIE achieves strong supervised results on ACE05 (RE F1 = 63.6/67.5/70.1 at 7B/13B/34B) but requires expensive fine-tuning per model architecture and does not enforce type constraints at decoding time. Our approach is complementary: compiled constraints could be layered on top of GoLLIE-style models to guarantee compliance.\n\n**3. Training-Time Type Constraints.** DocRE-TCGL (Neural Networks, 2025) enforces entity type constraints during training for document-level relation extraction. It constructs a Type-Constrained Graph (TCG) encoding permitted relationships between entity types and relation labels, and applies a Type-Constrained Loss (TCL) that penalizes predictions violating type compatibility. Evaluated on DocRED and DWIE, it demonstrates that type-aware training improves extraction quality. However, training-time approaches require retraining for each ontology change and do not guarantee compliance at inference time — a model trained with type constraints can still generate violations during decoding. Our decoding-time approach is complementary: it can enforce constraints on any model, including those trained with or without type-aware losses.\n\n**4. Constrained/Unconstrained Decoding Combination.** BoostCD/BoostIE (EMNLP 2025) is the closest methodological relative to our work. It combines constrained and unconstrained decoding via a learned boosting strategy for closed information extraction. In Phase 1, the system decodes each input twice — once with vocabulary-membership constraints (ensuring extracted entities appear in a predefined vocabulary) and once without. In Phase 2, a trained boosted model combines predictions from both modes. Error analysis reveals that constrained and unconstrained errors are complementary: constrained decoding suffers from forced token selection while unconstrained decoding produces 60% unrelated triplets and 9% entity misclassification errors on SynthIE. However, BoostCD operates on FlanT5-base (~250M params), focuses on vocabulary membership rather than ontology type constraints, does not enforce cross-field type consistency (e.g., relation domain/range), and requires training a boosted combiner model. Our approach differs in three key ways: (a) we compile full ontology type constraints (not just vocabulary membership) into finite-state machines, (b) we enforce constraints at decoding time without requiring a trained combiner, and (c) we target modern instruction-tuned LLMs (Qwen3-8B, Llama-3.1-8B) rather than small encoder-decoder models.\n\n**5. LLM-Based Information Extraction (Unconstrained).** The current state-of-the-art for LLM-based IE on SciERC reaches ~0.44 F1 with fine-tuned Qwen3-14B-Base, comparable to graph-based parsers achieving 0.35 F1 with 124M parameter models. On ACE05, GoLLIE Code-Llama-34B achieves 70.1 RE F1 in the supervised setting. These numbers establish the performance ceiling against which constraint enforcement must be evaluated — the key question is whether compiled constraints improve F1 (by eliminating type-violating predictions) or degrade it (by over-constraining the model's output space).\n\n**6. Format Tax and Two-Pass Decoding.** The Format Tax paper (arXiv Apr 2026) provides critical empirical grounding for our two-pass (S2) approach. It demonstrates that requiring structured output (JSON, XML, etc.) imposes a quality penalty, with ~70% attributable to prompt-level effects (the model allocating reasoning capacity to format compliance) and ~30% to decoder-level grammar masking (token probability distortion from constrained decoding). This decomposition validates the S2 strategy: first generate reasoning in natural language, then format-convert with constraints. By decoupling reasoning from formatting, S2 avoids the prompt-level format tax while applying semantic constraints only in the formatting pass.",
  "approach": "The approach is organized into four phases over 14 days, with a Day 1 pilot study that de-risks the entire project before committing engineering effort.\n\n**Phase 0: Violation Rate Pilot Study (Day 1-2).** Run unconstrained Qwen3-8B and Llama-3.1-8B on the ACE05 (entity+relation) and SciERC test sets using standard IE prompts. Write a lightweight Python script (~200 lines) that parses model outputs and checks each extracted triple against ontology type constraints: (a) entity type validity (is the predicted type in the ontology?), (b) relation domain/range (are the argument entity types compatible with the relation's type signature?), (c) cross-field consistency (do entity mentions used as relation arguments have consistent types?). Compute violation rates per model, per dataset, and per constraint type. Decision criterion: if aggregate violation rate >5%, proceed with full constraint compiler implementation; if <5%, pivot to a 'negative result + guaranteed compliance tool' framing where the contribution is the empirical finding that modern LLMs rarely violate ontology constraints, plus a lightweight safety-net tool. This pilot is itself a methodological contribution — it demonstrates principled de-risking before engineering investment and produces the first systematic violation rate measurements in the literature.\n\n**Phase 1: Ontology Constraint Compiler + vLLM LogitsProcessor (Day 2-6).** Implement the core technical contribution: a compiler that takes an ontology schema (entity types, relation types with domain/range constraints) and produces a finite-state machine (FSM) that can be applied during decoding via vLLM's LogitsProcessor API. The compiler handles: (a) entity type constraints — at entity type token positions, mask logits to allow only valid ontology types; (b) relation type constraints — at relation type token positions, mask logits to allow only valid relation types; (c) cross-field type consistency — after entity types are decoded, constrain subsequent relation type tokens to only those relations whose domain/range match the decoded entity types. The LogitsProcessor subclass implements apply() on (num_requests × vocab_size) tensors, maintaining per-request FSM state to track which entities and types have been decoded. Target ontologies: SciERC (7 entity types, 7 relation types) and ACE05 entities+relations (7 entity types, 18 relation subtypes with typed argument roles). Event types (33 types with typed argument roles) are deferred to Phase 3 as a stretch goal.\n\n**Phase 2: Experiments (Day 6-10).** Two decoding strategies: (S1) Single-pass constrained decoding — apply the ontology FSM during standard prompted generation; (S2) Two-pass decoding — first generate unconstrained natural language reasoning, then format-convert with ontology constraints applied. S2 is motivated by the Format Tax finding that decoupling reasoning from formatting avoids ~70% of the quality penalty. Four baselines: (1) Unconstrained generation — standard prompted IE with no constraints, establishing the violation rate and raw F1; (2) JSON-only grammar constraints — enforce valid JSON structure using Outlines/GBNF but no semantic constraints, isolating the contribution of ontology-level enforcement; (3) Post-hoc type filtering — generate unconstrained, then filter/correct outputs that violate type constraints, representing a simple non-decoding-time alternative; (4) GoLLIE published numbers — use GoLLIE's Code-Llama-34B ACE05 results (RE F1 = 70.1) as a discussion comparison point, without retraining on our target models. Two models: Qwen3-8B and Llama-3.1-8B. Two datasets: SciERC and ACE05 (entity+relation only). Metrics: F1 (entity, relation, end-to-end), ontology violation rate, latency overhead (tokens/sec with vs. without constraints), constraint satisfaction rate (% of outputs that are ontology-valid).\n\n**Phase 3: Ablations, Paper Writing, and Stretch Goals (Day 10-14).** Core ablations: (a) entity-only vs. relation-only vs. full constraints — which constraint type contributes most?; (b) S1 vs. S2 — does two-pass decoding improve F1 or only compliance?; (c) constraint strictness — hard masking (zero logits) vs. soft penalization (logit bias) for borderline cases. Paper writing and figure generation. Stretch goal (time permitting): extend constraint compiler to ACE05 event ontology (33 event types with typed argument roles), demonstrating scalability to complex ontologies. S3 (DCCD-style dynamic constraint composition) is dropped entirely to focus engineering effort on the core contribution.\n\n**Key Design Decisions and Rationale.** (1) GoLLIE is demoted from an empirical baseline to a discussion comparison because porting it to Qwen3-8B and Llama-3.1-8B would require 40-80 H100-hours of fine-tuning, consuming the entire compute budget without contributing to the core research question. (2) ACE05 events are deferred because 33 event types with typed argument roles significantly increase compiler complexity without strengthening the core contribution about entity+relation type constraints. (3) The Day 1 pilot is foregrounded because it de-risks the entire project — if violation rates are low, constraint enforcement is a solution in search of a problem, and the honest scientific response is to report that finding. (4) S3 is dropped because dynamic constraint composition adds implementation complexity without a clear empirical hypothesis beyond S1 and S2.",
  "resource_estimate": {
    "manual": {
      "total_hours": 90,
      "breakdown": {
        "phase_0_pilot_study": "8 hours — prompt engineering for IE tasks, running unconstrained inference on 2 models × 2 datasets, writing violation checking script, analyzing results and making go/no-go decision",
        "phase_1_compiler_and_logitsprocessor": "30 hours — ontology schema parser (4h), FSM construction for entity type constraints (6h), FSM construction for relation domain/range constraints (8h), cross-field state tracking (6h), vLLM LogitsProcessor integration and testing (6h)",
        "phase_2_experiments": "28 hours — S1 single-pass experiments on 2 models × 2 datasets (6h), S2 two-pass experiments (8h), baseline runs including post-hoc filtering implementation (8h), metric computation and results analysis (6h)",
        "phase_3_ablations_and_writing": "24 hours — ablation experiments (8h), paper writing and figures (12h), stretch goal ACE05 events if time permits (4h)"
      }
    },
    "human_in_loop": {
      "total_hours": 6,
      "breakdown": {
        "pilot_review": "2 hours — review violation rate results and approve go/no-go decision after Phase 0",
        "experiment_review": "2 hours — review experimental results, identify unexpected patterns, approve ablation priorities",
        "paper_review": "2 hours — review draft paper, provide feedback on framing and presentation"
      }
    },
    "auto_research": {
      "gpu_type": "H100",
      "total_gpu_hours": 30,
      "breakdown": {
        "phase_0_pilot": "4 GPU-hours — unconstrained inference with Qwen3-8B and Llama-3.1-8B on ACE05 + SciERC test sets (2 models × 2 datasets × ~1 hour each)",
        "phase_2_experiments": "20 GPU-hours — S1 constrained decoding (4h), S2 two-pass decoding (6h), baseline unconstrained + JSON-only + post-hoc filtering (6h), latency benchmarking (4h)",
        "phase_3_ablations": "6 GPU-hours — constraint type ablations (3h), hard vs. soft masking (2h), optional ACE05 events stretch (1h)"
      },
      "compute_notes": "Significantly reduced from prior estimate by eliminating GoLLIE retraining (saved 40-80 H100-hours) and deferring ACE05 events. Total 30 H100-hours is achievable within standard academic compute allocations. Models run in fp16/bf16 on single H100 (Qwen3-8B ~16GB, Llama-3.1-8B ~16GB)."
    }
  },
  "target_venues": [
    "ACL 2026",
    "EMNLP 2026",
    "NAACL 2026"
  ],
  "level": "medium",
  "key_references": [
    {
      "id": "gollie_2023",
      "title": "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction",
      "venue": "EMNLP 2023 (Findings)",
      "relevance": "Code-generation approach to IE using ontology schemas as Python classes. Published Code-Llama results on ACE05 (RE F1 = 70.1 at 34B). Used as discussion comparison point rather than empirical baseline due to prohibitive retraining cost."
    },
    {
      "id": "odke_plus_2025",
      "title": "ODKE+: Ontology-Driven Knowledge Extraction at Scale",
      "venue": "arXiv, Sep 2025 (Apple)",
      "relevance": "Production-scale soft ontology guidance using dynamically generated ontology snippets in prompts. Achieves 98.8% precision on 19M facts from 9M Wikipedia pages across 195 predicates. Demonstrates that soft prompting scales but cannot guarantee type compliance — the key contrast with our hard constraint approach."
    },
    {
      "id": "docre_tcgl_2025",
      "title": "DocRE-TCGL: Type-Constrained Graph Learning for Document-Level Relation Extraction",
      "venue": "Neural Networks, 2025",
      "relevance": "Training-time entity type constraint enforcement via Type-Constrained Graph and Type-Constrained Loss. Evaluated on DocRED and DWIE. Complementary to our decoding-time approach — shows type constraints improve quality but requires retraining for each ontology change."
    },
    {
      "id": "boostcd_2025",
      "title": "BoostCD/BoostIE: Boosting Constrained and Unconstrained Decoding for Closed Information Extraction",
      "venue": "EMNLP 2025",
      "relevance": "Closest methodological relative. Combines constrained + unconstrained decoding via learned boosting on FlanT5-base. Shows error complementarity between modes (60% unrelated triplets unconstrained, forced token errors constrained). Key differences: vocabulary membership only (not ontology type constraints), requires trained combiner, small encoder-decoder model."
    },
    {
      "id": "format_tax_2026",
      "title": "The Format Tax: Quantifying Quality Loss from Structured Output Requirements",
      "venue": "arXiv, Apr 2026",
      "relevance": "Decomposes structured output quality loss: ~70% from prompt-level effects, ~30% from decoder-level grammar masking. Directly motivates our S2 two-pass approach that decouples reasoning from formatting to avoid the prompt-level format tax."
    },
    {
      "id": "outlines_2024",
      "title": "Outlines: Efficient Guided Generation for Large Language Models",
      "venue": "arXiv / NeurIPS 2024 Workshop",
      "relevance": "Grammar-constrained decoding using finite-state machines for JSON schema compliance. Represents the syntax-only baseline that our ontology-level constraints extend."
    },
    {
      "id": "vllm_2023",
      "title": "vLLM: Efficient Memory Management for Large Language Model Serving with PagedAttention",
      "venue": "SOSP 2023",
      "relevance": "Inference engine providing the LogitsProcessor API used for constraint enforcement. V1 architecture enables custom logit manipulation on (num_requests × vocab_size) tensors."
    },
    {
      "id": "scierc_2018",
      "title": "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction",
      "venue": "EMNLP 2018",
      "relevance": "Primary evaluation dataset with 7 entity types and 7 relation types. Current LLM SOTA ~0.44 F1 (Qwen3-14B-Base fine-tuned)."
    },
    {
      "id": "ace05_2005",
      "title": "ACE 2005 Multilingual Training Corpus",
      "venue": "LDC",
      "relevance": "Primary evaluation dataset for entity+relation extraction (7 entity types, 18 relation subtypes). Event types (33 types) deferred to stretch goal. GoLLIE published baselines available for comparison."
    }
  ],
  "description": "This project investigates whether compiling ontology type constraints into finite-state machines and enforcing them at LLM decoding time can improve information extraction quality and guarantee ontology compliance. The core insight is that existing grammar-constrained decoding tools (Outlines, GBNF) enforce syntactic validity (well-formed JSON) but ignore semantic validity (ontology type constraints such as relation domain/range compatibility and cross-field entity type consistency). Meanwhile, soft approaches like ODKE+ achieve high precision through prompt-based ontology guidance but cannot guarantee compliance, training-time approaches like DocRE-TCGL require retraining for each ontology change, and hybrid approaches like BoostCD/BoostIE combine constrained and unconstrained decoding but focus on vocabulary membership rather than ontology type constraints and require training a boosted combiner model.\n\nThe project makes three contributions. First, a systematic violation rate measurement: the Day 1-2 pilot study produces the first empirical quantification of ontology constraint violation rates across models (Qwen3-8B, Llama-3.1-8B), datasets (SciERC, ACE05), and constraint types (entity type validity, relation domain/range, cross-field consistency). This measurement is a first-order contribution regardless of the outcome — if violation rates are high, it motivates constraint enforcement; if low, it is a valuable negative result establishing that modern instruction-tuned LLMs have internalized ontology constraints. Second, an ontology constraint compiler that translates ontology schemas (entity types, relation types with domain/range specifications) into finite-state machines enforced via vLLM's LogitsProcessor API. The compiler handles three constraint levels: entity type validity (restricting type tokens to ontology-valid types), relation type constraints (restricting relation tokens to valid relation types), and cross-field type consistency (conditioning relation type tokens on previously decoded entity types to enforce domain/range compatibility). Third, an empirical evaluation of two decoding strategies — S1 (single-pass constrained decoding) and S2 (two-pass: unconstrained reasoning then constrained formatting, motivated by the Format Tax finding that ~70% of structured output quality loss comes from prompt-level effects).\n\nThe experimental design uses four baselines: unconstrained generation (measuring raw violation rates and F1), JSON-only grammar constraints (isolating the contribution of ontology-level enforcement beyond syntax), post-hoc type filtering (a non-decoding-time alternative), and GoLLIE published numbers (Code-Llama-34B ACE05 RE F1 = 70.1, used as a discussion comparison without retraining). GoLLIE is demoted from an empirical baseline because porting it to Qwen3-8B and Llama-3.1-8B would require 40-80 H100-hours of fine-tuning, which is prohibitively expensive given the 14-day timeline and would not contribute to the core research question about decoding-time constraint enforcement. ACE05 event types (33 types with typed argument roles) are deferred to a stretch goal because the compiler complexity they introduce is not justified for the core entity+relation contribution.\n\nThe 14-day timeline is structured as: Day 1-2 pilot study with go/no-go decision, Day 2-6 compiler and LogitsProcessor implementation, Day 6-10 experiments across all strategies and baselines, Day 10-14 ablations (entity-only vs. relation-only vs. full constraints; S1 vs. S2; hard masking vs. soft logit bias), paper writing, and optional ACE05 event stretch goal. Total compute budget is 30 H100-hours, reduced from the prior estimate by eliminating GoLLIE retraining and deferring events. The project targets ACL/EMNLP/NAACL 2026 with a submission deadline of May 25, 2026.",
  "project_name": "schema_semantic_constrained_ie",
  "source": "web_research",
  "change_type": "major"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51afe53f-5a5f-4749-9dea-982492568192",
  "isSidechain": true,
  "agentId": "a722d76f9a9e9176c",
  "requestId": "req_011CawiGcPAKs57SwFhuDbbB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d287f705-3fc2-447c-a0be-fe802e88bc83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "00137b04-bbf3-4563-97d2-72b98f97712d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014d1Syf4cJxDD2knqaKvMWk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10535,
      "cache_read_input_tokens": 0,
      "output_tokens": 6022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10535
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 6022,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 10535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10535,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
