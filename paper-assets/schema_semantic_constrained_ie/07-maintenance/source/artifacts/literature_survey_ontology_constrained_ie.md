# Literature Survey: Schema/Ontology-Guided Information Extraction with LLMs (2023-2026)

> Compiled: 2026-05-13 | For: OntoCoDec project novelty assessment

## Executive Summary

**Core novelty question**: Has anyone done "compile ontology → decoding-time semantic constraints" for IE before?

**Answer**: **No one has done the full OntoCoDec pipeline** (ontology → compiled domain/range constraints → token-level logits masking during IE generation). However, several papers occupy adjacent spaces that must be cited and differentiated:

1. **Ontology-constrained beam search for summarization** exists (EKAW2024), but targets clinical summarization, not IE, and uses beam reranking rather than logits masking.
2. **SciDC** (2026) converts scientific knowledge to decoding rules, but targets scientific reasoning tasks, not IE schemas with domain/range constraints.
3. **Grammar-constrained decoding for IE** exists (Frontiers 2024), but enforces syntactic structure (JSON/CFG), not semantic type constraints.
4. **Code-style schema encoding** (KnowCoder, GoLLIE, CodeIE) encodes schemas as Python classes, but enforces constraints at training time, not decoding time.
5. **Post-processing validation** (OntoLogX, RELATE, ODKE+) applies ontology checks after generation, not during.

**OntoCoDec's novelty**: The specific combination of (a) compiling IE ontology domain/range constraints into (b) a LogitsProcessor that enforces semantic type validity (c) at decoding time, token by token, is novel.

---

## Category 1: Schema-in-Prompt Approaches

### GoLLIE (ICLR 2024)
- **Method**: Fine-tunes Code-Llama to follow annotation guidelines encoded as Python class definitions with docstrings. Schema = Python dataclass with type hints and natural language descriptions.
- **Schema use**: PROMPT + TRAINING. Guidelines are part of the prompt; model is fine-tuned to follow them.
- **Constraint enforcement**: None at decoding time. Relies on training to learn schema compliance.
- **Relevance to OntoCoDec**: GoLLIE shows code-style schema representation improves zero-shot IE. OntoCoDec goes further by enforcing constraints at decoding time rather than hoping the model learned them.
- **URL**: https://arxiv.org/abs/2310.03668

### KnowCoder (ACL 2024)
- **Method**: Encodes 29K+ entity types and 876 relation types from Wikidata as Python classes with inheritance. Fine-tunes LLM on code-generation formulation of IE.
- **Schema use**: TRAINING. Schema encoded as code; model trained to generate class instantiations.
- **Constraint enforcement**: Training-time only. No decoding constraints. Type hierarchy encoded via Python inheritance but not enforced during generation.
- **Relevance to OntoCoDec**: KnowCoder's schema library could be a source of ontology constraints for OntoCoDec's compiler. The key difference: KnowCoder trusts the model to learn constraints; OntoCoDec enforces them.
- **URL**: https://arxiv.org/abs/2403.07969

### CodeIE (ACL 2023)
- **Method**: Recasts IE as code generation. Entity types and relation schemas encoded as Python type hints; uses Code-LLMs (Codex) for few-shot extraction.
- **Schema use**: PROMPT. Schema encoded as code-style prompt with type annotations.
- **Constraint enforcement**: None. Relies on code LLM's understanding of type hints.
- **URL**: https://arxiv.org/abs/2305.05711

### Code4Struct (ACL 2023)
- **Method**: Event argument extraction via code generation. Event schemas = Python classes with type annotations and inheritance.
- **Schema use**: PROMPT. Python class definitions serve as schema specification.
- **Constraint enforcement**: None at decoding time. Notes that PL features like type annotation could "add constraints" but does not implement this.
- **Relevance**: Explicitly identifies the opportunity that OntoCoDec seizes — using type systems as constraints — but does not implement it.
- **URL**: https://arxiv.org/abs/2210.12810

### SPIRES / OntoGPT (Bioinformatics 2024)
- **Method**: Structured Prompt Interrogation and Recursive Extraction of Semantics. Uses user-defined LinkML schemas to structure prompts. Recursively queries GPT to fill nested schema templates. Post-hoc grounds entities to ontology identifiers.
- **Schema use**: PROMPT + POST-PROCESSING. Schema structures the prompt; ontology grounding happens after extraction.
- **Constraint enforcement**: Post-hoc grounding only. No decoding-time constraints. Schema guides prompt structure but does not constrain token generation.
- **Relevance**: SPIRES is the closest "ontology-guided IE" system but enforces nothing at decoding time. Violations are caught (or missed) in post-processing.
- **URL**: https://arxiv.org/abs/2304.02711

### InstructUIE (2023)
- **Method**: Multi-task instruction tuning on 32 IE datasets. Schema encoded as task instructions in natural language.
- **Schema use**: PROMPT (instructions). No formal ontology.
- **URL**: https://github.com/BeyonderXX/InstructUIE

---

## Category 2: Ontology-Guided IE Systems

### ODKE+ (Apple, 2025)
- **Method**: Production-grade system extracting facts from 9M+ Wikipedia pages. Dynamically generates ontology snippets per entity type. Hybrid pattern + LLM extraction. Lightweight LLM-based grounder validates extractions.
- **Schema use**: PROMPT (dynamic ontology snippets) + POST-PROCESSING (grounder + corroborator).
- **Constraint enforcement**: Post-processing validation. No decoding-time constraints.
- **Scale**: 195 predicates, 19M facts, 98.8% precision.
- **URL**: https://arxiv.org/abs/2509.04696

### RELATE (2025)
- **Method**: Biomedical relation extraction with ontology constraint mapping. Three-stage pipeline: (1) ontology preprocessing with predicate embeddings, (2) SapBERT similarity retrieval, (3) LLM reranking.
- **Schema use**: POST-PROCESSING. Maps free-text relations to ontology predicates after extraction.
- **Constraint enforcement**: Post-hoc mapping, not decoding-time. Ontology constraints applied to filter/map results, not to guide generation.
- **URL**: https://arxiv.org/abs/2509.19057

### OntoLogX (2025)
- **Method**: Ontology-guided KG extraction from cybersecurity logs. Uses RAG + function-calling to produce structured output. SHACL validation for post-hoc constraint checking.
- **Schema use**: PROMPT (ontology in RAG context) + POST-PROCESSING (SHACL validation).
- **Constraint enforcement**: Post-hoc SHACL validation. Iterative correction reduces violations by ~10x, but this is generate-then-fix, not constrained generation.
- **Key insight**: SHACL violations include property cardinalities, type consistency, required fields — exactly the kinds of constraints OntoCoDec would enforce at decoding time.
- **URL**: https://arxiv.org/abs/2510.01409

### OneKE (WWW 2025)
- **Method**: Dockerized schema-guided LLM agent system. Three agents: Schema Agent (schema analysis), Extraction Agent (LLM extraction), Reflection Agent (error debugging).
- **Schema use**: PROMPT (schema guides extraction) + POST-PROCESSING (reflection agent).
- **Constraint enforcement**: Agent-based iterative correction, not decoding-time.
- **URL**: https://arxiv.org/abs/2412.20005

### StructSense (2025)
- **Method**: Multi-agent framework with ontology integration. Four agents: extractor, alignment, judge, feedback. Guides extraction with domain ontologies.
- **Schema use**: PROMPT + POST-PROCESSING (multi-agent loop).
- **Constraint enforcement**: Agent-based validation, not decoding-time.
- **URL**: https://arxiv.org/abs/2507.03674

### Ontology-grounded KG Construction under Wikidata schema (KDD Workshop 2024)
- **Method**: CQ generation → relation extraction → ontology matching → KG construction. Grounds output to Wikidata relations.
- **Schema use**: POST-PROCESSING (ontology matching after extraction).
- **URL**: https://arxiv.org/abs/2412.20942

---

## Category 3: Constrained Decoding for IE (Syntactic, not Semantic)

### Grammar-Constrained Decoding for Clinical Trial IE (Frontiers in AI, 2024)
- **Method**: Uses context-free grammars to constrain Flan-T5/Longformer output during structured IE from clinical trial abstracts (C-TrO ontology).
- **Schema use**: DECODING. Grammar derived from ontology structure.
- **Constraint enforcement**: CFG-based constrained decoding — ensures structural validity (slot names, nesting), NOT semantic validity (type constraints, domain/range).
- **Key distinction from OntoCoDec**: This enforces *syntactic* structure (valid JSON fields matching ontology slots). OntoCoDec enforces *semantic* constraints (if relation=X, then head_type must be in domain(X)).
- **URL**: https://www.frontiersin.org/articles/10.3389/frai.2024.1406857

### SLOT (EMNLP Industry 2025)
- **Method**: Fine-tuned lightweight LM as post-processing layer to structure LLM output. Achieves 99.5% schema accuracy with constrained decoding.
- **Schema use**: POST-PROCESSING + DECODING. Constrained decoding applied to the restructuring model, not the extraction model.
- **Constraint enforcement**: Syntactic schema conformance (JSON structure), not semantic constraints.
- **URL**: https://aclanthology.org/2025.emnlp-industry.32/

### DLISC (2025)
- **Method**: Dual-LoRA with Incremental Schema Caching for on-device LLMs. Two-stage: schema identification LoRA + extraction LoRA.
- **Schema use**: TRAINING (LoRA adapters) + PROMPT (selected schemas).
- **Constraint enforcement**: Training-time schema awareness. No decoding-time semantic constraints.
- **URL**: https://arxiv.org/abs/2505.14992

### PARSE (2025)
- **Method**: LLM-driven schema optimization. Autonomously optimizes JSON schemas for LLM consumption. 64.7% improvement on SWDE.
- **Schema use**: PROMPT (optimized schema descriptions).
- **Constraint enforcement**: Schema optimization, not decoding-time enforcement.
- **URL**: https://arxiv.org/abs/2510.08623

### Schema as Parameterized Tools (SPT, 2025)
- **Method**: Treats schemas as tools for LLM tool-calling. Schema retrieval + filling + generation. Unifies closed, open, and on-demand IE.
- **Schema use**: PROMPT (schemas as tool definitions). 
- **Constraint enforcement**: Tool-calling format constrains output structure, not semantic validity.
- **URL**: https://arxiv.org/abs/2506.01276

---

## Category 4: Ontology-Constrained Decoding (Closest Competitors)

### Ontology-Constrained Generation of Clinical Summaries (EKAW 2024) ⚠️ CLOSEST
- **Method**: Ontology-guided constrained beam search for clinical summarization. Extracts medical concepts from EHRs, then generates summaries with beam search biased toward ontology-aligned content.
- **Schema use**: DECODING. Ontology used to compute hierarchy, property, and similarity scores that bias beam search.
- **Constraint enforcement**: Beam search reranking based on ontology alignment. NOT token-level logits masking. Soft preference, not hard constraint.
- **Key distinction from OntoCoDec**: (1) Task is summarization, not IE. (2) Constraints are soft (beam score bias), not hard (logits masking). (3) No domain/range enforcement for relation extraction. (4) No compilation step from ontology to FSM/grammar.
- **URL**: https://arxiv.org/abs/2411.15666

### SciDC (2026) ⚠️ VERY RELEVANT
- **Method**: Uses strong LLMs to convert flexible scientific knowledge into multi-layered standardized rules, then constrains generation with these rules. Applied to formulation design, tumor diagnosis, retrosynthesis.
- **Schema use**: DECODING. Knowledge → rules → generation constraints.
- **Constraint enforcement**: Decoding-time rule enforcement. 12% accuracy improvement.
- **Key distinction from OntoCoDec**: (1) Domain is scientific reasoning, not IE. (2) Rules are derived from scientific knowledge, not IE ontology schemas. (3) No domain/range type constraints for relation extraction. (4) Rule format is different from FSM/grammar compilation.
- **URL**: https://arxiv.org/abs/2604.06603

### Dialogue Ontology Relation Extraction via Constrained CoT Decoding (SIGDIAL 2024)
- **Method**: Adapts Chain-of-Thought decoding for ontology relation extraction in task-oriented dialogue. Constrains decoding to ontology terms. Multiple branches + confidence threshold.
- **Schema use**: DECODING. Constrains vocabulary to ontology terms.
- **Constraint enforcement**: Vocabulary restriction to ontology terms during decoding. Does NOT enforce domain/range constraints on relations.
- **Key distinction from OntoCoDec**: Constrains the vocabulary (which relation names are valid), not the semantic types (which entity type combinations are valid for a given relation).
- **URL**: https://arxiv.org/abs/2408.02361

### Evo-DKD (2025)
- **Method**: Dual-decoder for ontology evolution. One decoder proposes ontology edits; another generates justifications. Attention-based gating coordinates.
- **Schema use**: DECODING (dual-decoder architecture). But task is ontology evolution, not IE.
- **Relevance**: Tangential. Uses ontology in decoding but for a different task entirely.
- **URL**: https://arxiv.org/abs/2507.21438

### Conversational Control with Ontologies (2026)
- **Method**: Ontological definitions of conversational aspects used as constraints before LoRA fine-tuning.
- **Schema use**: TRAINING (ontology-informed LoRA).
- **Constraint enforcement**: Training-time, not decoding-time.
- **URL**: https://arxiv.org/abs/2604.04450

---

## Category 5: Type-Constrained Decoding (Non-IE, but Technically Closest)

### Type-Constrained Code Generation (PLDI 2025) ⚠️ TECHNICALLY CLOSEST
- **Method**: Compiles type systems (simply-typed lambda calculus, extended to TypeScript) into prefix automata that constrain code generation to well-typed programs. Reduces compilation errors by >50%.
- **Schema use**: DECODING. Type system → automaton → logits masking.
- **Constraint enforcement**: Hard constraint at token level via automata. Exactly the mechanism OntoCoDec uses, but for programming language types, not IE ontology types.
- **Key distinction from OntoCoDec**: (1) Domain is code generation, not IE. (2) Type system is programming language types, not ontology domain/range. (3) No relation extraction context. But the technical approach (type system → automaton → constrained decoding) is analogous.
- **MUST CITE**: This is the closest technical analog. OntoCoDec can be framed as "doing for IE ontology types what Type-Constrained Code Generation does for programming language types."
- **URL**: https://arxiv.org/abs/2504.09246

### CRANE (ICML 2025)
- **Method**: Reasoning-augmented constrained decoding. Alternates between unconstrained reasoning and constrained output. Shows strict grammar constraints can hurt reasoning.
- **Relevance**: Important methodological insight for OntoCoDec — may need to allow unconstrained reasoning before constraining the structured output portion.
- **URL**: https://arxiv.org/abs/2502.09061

### Automata-Based Constraints for LM Decoding (2024)
- **Method**: General framework for compiling constraints into automata for LLM decoding. Regular languages and context-free languages.
- **Relevance**: Infrastructure that OntoCoDec builds on.
- **URL**: https://arxiv.org/abs/2407.08103

### XGrammar (2024-2025)
- **Method**: Pushdown automaton for grammar-constrained decoding. Compiles JSON schemas to token masks. ~7000x faster than prior approaches.
- **Relevance**: OntoCoDec uses XGrammar as infrastructure, adding semantic constraints on top.
- **URL**: XGrammar GitHub

---

## Category 6: Logical Rule Constraints for IE

### Ru-LLM: Logical Rule-Constrained LLMs for DocRE (NLPCC 2025)
- **Method**: Mines logical rules from training data via frequent pattern mining + MCTS. Rules injected into LLM prompts for document-level relation extraction.
- **Schema use**: PROMPT. Logical rules added to prompt, not enforced at decoding time.
- **Constraint enforcement**: Prompt-based, not decoding-time. Rules guide reasoning but don't prevent violations.
- **Key distinction from OntoCoDec**: Rules are statistical patterns, not ontology axioms. Enforcement is soft (prompt), not hard (logits masking).
- **URL**: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11

### LogiRE / JMRL (EMNLP 2021, ACL 2024)
- **Method**: Learns logical rules for document-level RE. End-to-end joint learning of model + rules.
- **Schema use**: TRAINING. Rules learned during training.
- **Constraint enforcement**: Training-time regularization, not decoding-time enforcement.
- **URL**: https://arxiv.org/abs/2111.05407

---

## Category 7: Domain-Specific Schema for IE

### Biomedical: Ontology-Conformal NER (Scientific Reports 2025)
- **Method**: Assesses LLM ontology-conformal NER in materials mechanics domain. Fine-tuned models (MatSciBERT, DeBERTa) significantly outperform GPT-4 ICL.
- **URL**: https://www.nature.com/articles/s41598-025-03619-y

### GLiNER2 (2025)
- **Method**: Schema-driven multi-task IE system. Declarative schema definitions with multiple field types.
- **Schema use**: PROMPT (declarative schema). No decoding constraints.
- **URL**: https://arxiv.org/abs/2507.18546

### ToNER (LREC 2024)
- **Method**: Type-oriented NER with generative LM. Uses type matching to identify likely entity types, then fine-tunes for extraction.
- **Schema use**: TRAINING. Type-aware fine-tuning.
- **URL**: https://aclanthology.org/2024.lrec-main.1412/

---

## Taxonomy of How Ontology/Schema is Used

| Method | Prompt | Training | Decoding (Syntactic) | Decoding (Semantic) | Post-Processing |
|--------|--------|----------|---------------------|--------------------|-----------------| 
| GoLLIE | ✓ | ✓ | | | |
| KnowCoder | ✓ | ✓ | | | |
| CodeIE | ✓ | | | | |
| SPIRES | ✓ | | | | ✓ |
| ODKE+ | ✓ | | | | ✓ |
| OntoLogX | ✓ | | | | ✓ (SHACL) |
| OneKE | ✓ | | | | ✓ (Agent) |
| Grammar-CD (C-TrO) | | ✓ | ✓ (CFG) | | |
| SLOT | | ✓ | ✓ (JSON) | | |
| EKAW2024 | ✓ | | | ✓ (soft beam) | |
| SciDC | | | | ✓ (rules) | |
| Dialogue Ontology RE | | ✓ | ✓ (vocab) | | |
| Type-Constrained CG | | | | ✓ (types→FSM) | |
| **OntoCoDec (ours)** | | | **✓ (JSON)** | **✓ (domain/range→mask)** | |

---

## Category 8: Traditional Constraint Methods (ILP/CRF, pre-LLM)

### Roth & Yih (AAAI 2004 / MIT Press 2007)
- **Method**: Pioneering ILP for joint NER+RE. Trains separate entity/relation classifiers, then uses Integer Linear Programming at inference to enforce global consistency: e.g., EMP-ORG relation only valid between PER and ORG entities.
- **Schema use**: INFERENCE. Type compatibility encoded as ILP constraints.
- **Constraint enforcement**: Hard constraints at inference time via ILP solver. Not token-level; operates on classifier outputs.
- **Relevance**: Foundational. First to formalize type constraints for joint IE. OntoCoDec brings this idea to the LLM era with token-level enforcement.

### Li & Ji (AIJ 2014) — Encoding Implicit Relation Requirements
- **Method**: Mines type and cardinality constraints from data, encodes them as ILP constraints (hard/soft) for joint entity-relation extraction.
- **Schema use**: INFERENCE. Implicit type/cardinality requirements compiled into ILP.
- **Constraint enforcement**: ILP hard/soft constraints at inference time.
- **Relevance**: Directly analogous motivation — compile type constraints into inference-time enforcement. OntoCoDec does the same for autoregressive LLMs.

---

## Category 9: Training-Time Type Constraint Encoding

### KnowPrompt (WWW 2022)
- **Method**: Injects entity type knowledge into prompt-tuning for relation extraction. Virtual type words initialized with aggregated entity-type embeddings. Synergistic optimization with structural constraints between entities/relations.
- **Schema use**: TRAINING. Type knowledge encoded in learnable virtual words.
- **Constraint enforcement**: Training-time structural constraint optimization. No decoding-time enforcement.
- **Relevance**: Shows value of type knowledge for RE; OntoCoDec enforces these constraints at decoding time instead.
- **URL**: https://arxiv.org/abs/2104.07650

### Type-Constrained Negative Sampling for KGE (2022-2023)
- **TaKE (Scientific Reports 2023)**: Type-augmented KGE framework. Maps entities into two vector spaces (relation-entity triples + relation-type triples). Type compatibility function constrains entity type features.
- **ETF (Applied Intelligence 2022)**: Entity embedding = entity-specific + constraint-specific components. Constraint embedding represents semantic constraints from linked relations.
- **STS**: Soft Type Constraint increases likelihood of selecting same-type negatives, guided by relation-specific type information.
- **Schema use**: TRAINING. Type constraints encoded in embedding loss functions.
- **Constraint enforcement**: Training-time only. Not LLM, not decoding-time.
- **Relevance**: Shows type constraints improve KG quality; motivates decoding-time enforcement for LLM-based IE.

---

## Category 10: Decoding-Time Vocabulary Restriction (Entity/Relation Names, not Type Semantics)

### GENRE (ICLR 2021) — Autoregressive Entity Retrieval
- **Method**: Generates entity names autoregressively with constrained beam search using a trie (prefix tree) built from all KB entity names. Forces output to be a valid entity identifier.
- **Schema use**: DECODING. Trie built from knowledge base entries.
- **Constraint enforcement**: Hard constraint via trie — only valid entity name prefixes allowed at each token. Vocabulary restriction, not type-semantic constraint.
- **Relevance**: Pioneer of trie-based constrained decoding for IE-adjacent tasks. Constrains "what entities exist" but not "what entity types are valid for a given relation."
- **URL**: https://arxiv.org/abs/2010.00904

### JoinER-BART (IEEE/ACM TASLP 2023)
- **Method**: Joint entity+relation extraction with BART. Constrained classifier predicts either input sentence tokens or relation names at each decoding step.
- **Schema use**: DECODING. Vocabulary restricted to input tokens + relation vocabulary.
- **Constraint enforcement**: Vocabulary restriction (structural), not type-semantic constraints.
- **URL**: https://doi.org/10.1109/TASLP.2023.3310879

### AdaKGC (EMNLP 2023 Findings) — Schema-Adaptable KGC
- **Method**: Schema-Constrained Dynamic Decoding (SDD) + Schema-Enriched Prefix Instruction (SPI). Handles evolving schemas without retraining. Trie-based constrained decoding adapts to new entity/relation types.
- **Schema use**: DECODING. Dynamic trie updated per schema.
- **Constraint enforcement**: Trie constrains vocabulary to valid schema terms. Does NOT enforce domain/range compatibility.
- **Relevance**: Closest in mechanism (trie-based schema constraint during decoding for IE), but constrains vocabulary, not type-semantic validity.
- **URL**: https://arxiv.org/abs/2305.08703

---

## Category 11: Document-Level RE with Entity Type Constraints (2024-2025)

### ETCGN (Int. J. Machine Learning & Cybernetics, 2024)
- **Method**: Entity Type-Constrained Graph Networks for document-level RE. Graph structure captures mention interactions; entity types confine scope of candidate relations.
- **Schema use**: MODEL ARCHITECTURE. Type constraints built into graph network structure.
- **Constraint enforcement**: Architectural (during training/inference), not token-level decoding constraint.
- **URL**: https://link.springer.com/article/10.1007/s13042-024-02293-2

### TyRaL (2025)
- **Method**: Type-constrained enhanced chain-like rules for end-to-end document-level RE. Transforms rule learning into parameter optimization.
- **Schema use**: TRAINING. Type-constraint rules learned end-to-end.
- **Constraint enforcement**: Rule-based during inference, but not token-level LLM decoding.
- **URL**: https://ceur-ws.org/Vol-4085/paper44.pdf

### SH-ETRs (Expert Systems with Applications, 2025)
- **Method**: Learning Soft-Hard rules with entity type constraints for doc-level RE.
- **Schema use**: TRAINING + INFERENCE. Entity type constraints inform both rule learning and application.
- **URL**: https://www.sciencedirect.com/science/article/abs/pii/S0957417425032750

### Document-Level RE with ETC (Neural Networks, 2025)
- **Method**: Entity Type Constraints divide relations into type-matched (valid) and type-mismatched (filterable). Type-matched relations are predicted; mismatched ones are filtered out.
- **Schema use**: MODEL. Type constraints as architectural bias.
- **Constraint enforcement**: Classification-time filtering, not generative decoding constraint.
- **URL**: https://www.sciencedirect.com/science/article/abs/pii/S0893608025013504

---

## Category 12: Other Generative IE Frameworks (Context)

### TANL (ICLR 2021) — Structured Prediction as Translation between Augmented Natural Languages
- **Method**: Frames structured prediction as translation. Augmented natural language encodes entities/relations inline with text. No explicit type constraints.
- **Schema use**: TRAINING (format convention). No constraint enforcement.
- **URL**: https://arxiv.org/abs/2101.05779

### REBEL (EMNLP 2021 Findings)
- **Method**: Seq2seq RE with BART for 200+ relation types. Linearizes triples as text sequences.
- **Schema use**: TRAINING. No decoding constraints.
- **URL**: https://aclanthology.org/2021.findings-emnlp.204/

### EnriCo (2024) — Enriched Representation and Globally Constrained Inference
- **Method**: Joint E+R extraction with attention mechanisms + constrained inference via Answer Set Programming (ASP). Decoding algorithms enforce task/dataset-specific constraints.
- **Schema use**: DECODING. ASP constraints ensure coherent structured output.
- **Constraint enforcement**: Global structural constraints (e.g., no overlapping spans), not type-semantic constraints.
- **Relevance**: Shows value of constrained inference for joint E+R. Uses ASP instead of logits masking.
- **URL**: https://arxiv.org/abs/2404.12493

### Integrated Attention with Entity Type Constraints (Applied Intelligence, 2025)
- **Method**: Entity type constraints + relation augmentation for distantly supervised RE. Types reduce weights of incorrectly labeled instances.
- **Schema use**: TRAINING. Type constraints as noise reduction mechanism.
- **URL**: https://www.sciencedirect.com/science/article/abs/pii/S0950705125020441

---

## Novelty Gap Analysis

### What OntoCoDec does that nobody else does:
1. **Compiles ontology domain/range constraints** into a LogitsProcessor that operates at the token level during autoregressive IE generation
2. **Combines syntactic constraints** (JSON grammar via XGrammar) **with semantic constraints** (type validity via custom LogitsProcessor) in a single decoding pass
3. **Targets IE specifically** — enforcing that extracted (head_type, relation, tail_type) triples satisfy ontology axioms, not just producing valid JSON
4. **Position-aware constraint activation** — constraints activate only at relevant positions in the JSON output (e.g., when generating tail_type given head_type and relation)

### What must be acknowledged as prior art:
1. **Grammar-constrained decoding for IE** exists (CFG-based), but only enforces syntactic structure
2. **Ontology-constrained beam search** exists (EKAW2024), but for summarization and as soft constraint
3. **SciDC** converts knowledge to decoding rules, but for scientific reasoning, not IE
4. **Type-constrained code generation** (PLDI 2025) uses the same technical mechanism (type system → automaton → logits mask) but for a completely different domain
5. **Post-hoc ontology validation** (SHACL, RELATE, ODKE+) is well-established but fundamentally different from prevention

### Strongest framing for novelty:
"OntoCoDec brings type-constrained generation (previously applied only to programming languages) to information extraction, by compiling IE ontology axioms into decoding-time semantic constraints that prevent — rather than detect — type violations."
