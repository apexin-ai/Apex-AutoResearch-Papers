# Literature Survey: Constrained Decoding for Information Extraction (2022-2026)

Survey date: 2026-05-13

---

## Category A: Grammar-Constrained Decoding Directly Applied to IE Tasks

### A1. Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning
- **Authors**: Saibo Geng, Martin Josifoski, Maxime Peyrard, Robert West
- **Venue**: EMNLP 2023
- **ArXiv**: 2305.13971
- **Core method**: Uses context-free grammars (via Grammatical Framework) to constrain LLM decoding for structured NLP tasks. Introduces **input-dependent grammars** that adapt the grammar to each input.
- **IE tasks**: NER, relation extraction, entity disambiguation, constituency parsing
- **Semantic constraints**: No. Purely syntactic (CFG-level). Ensures valid output structure but not ontological validity of extracted content.
- **Key result**: GCD-enhanced LLMs substantially outperform unconstrained LLMs and even beat task-specific finetuned models.
- **Relevance**: **HIGH** — Most direct precursor. Demonstrates GCD for IE but stops at syntactic validity. Our work extends to semantic (type) constraints.
- **Code**: https://github.com/epfl-dlab/GCD

### A2. iNERD: Informed Named Entity Recognition Decoding for Generative Language Models
- **Authors**: Deussel, Hillebrand, et al.
- **Venue**: IEEE SLT 2024 (arXiv 2308.07791, Aug 2023)
- **Core method**: Treats NER as generative process; uses informed decoding that masks impossible tokens based on NER structure constraints during prediction.
- **IE tasks**: NER only
- **Semantic constraints**: Partial — masks tokens that are structurally impossible for NER (e.g., entity type vocabulary), but does not enforce ontological constraints like domain/range.
- **Key result**: Eliminates hallucinated entity types, improves NER performance across 5 LLMs on 8 datasets.
- **Relevance**: **HIGH** — Shows token masking for IE-specific constraints works. But constraints are NER-structural, not ontology-semantic.

### A3. Grammar-Constrained Decoding for Structured IE with Fine-tuned Models (Clinical Trial Abstracts)
- **Authors**: (Frontiers in AI, 2024)
- **Venue**: Frontiers in Artificial Intelligence, Jan 2025 (published online)
- **Core method**: Investigates grammar-constrained decoding impact on fine-tuned generative models for structured information extraction from clinical trial abstracts.
- **IE tasks**: Structured extraction from clinical text (PICO elements)
- **Semantic constraints**: No. Focuses on ensuring well-formedness of output structure via grammar rules.
- **Key result**: Grammar constraints ensure valid output format even in low-resource settings; investigates trade-off between format compliance and extraction accuracy.
- **Relevance**: MEDIUM — Domain-specific application of GCD to IE, but no semantic constraints.

### A4. Generative Biomedical Event Extraction with Constrained Decoding Strategy
- **Authors**: (IEEE/ACM Trans. Comp. Bio. Bioinformatics, 2024)
- **Venue**: IEEE/ACM TCBB, 2024
- **Core method**: T5-based seq2seq model with trie-based constrained decoding for biomedical event extraction. Uses curriculum learning.
- **IE tasks**: Biomedical event extraction (Genia 2011, Genia 2013)
- **Semantic constraints**: Partial — the trie constrains argument roles to valid options, which is a form of schema-level constraint beyond pure syntax.
- **Key result**: Outperforms extraction-based approaches; avoids cascading errors of pipeline systems.
- **Relevance**: MEDIUM-HIGH — Trie-constrained decoding for event extraction with role constraints is conceptually related to our type constraints.

### A5. An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction (ATG)
- **Authors**: Zaratiana, Tomeh, et al.
- **Venue**: AAAI 2024
- **ArXiv**: 2401.01326
- **Core method**: Encoder-decoder with pointing mechanism on dynamic vocabulary of spans and relation types. Decoder transitions through states with constraints (no relation before entities, no repeated spans, head != tail).
- **IE tasks**: Joint entity and relation extraction (CoNLL04, SciERC, ACE05)
- **Semantic constraints**: Minimal — structural constraints on generation order, but no type-compatibility checking.
- **Relevance**: MEDIUM — Constrained generation for RE but constraints are structural/ordering, not ontological.

### A6. CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors
- **Authors**: Peng Li, Tianxiang Sun, et al.
- **Venue**: ACL 2023
- **ArXiv**: 2305.05711
- **Core method**: Recasts IE structured output as Python code (dicts, lists); uses Code-LLMs (Codex) with code-style prompts.
- **IE tasks**: NER, relation extraction (7 benchmarks)
- **Semantic constraints**: No. Code structure provides implicit constraints but no ontology-level enforcement during decoding.
- **Relevance**: MEDIUM — Alternative approach to structured IE output; Python type hints could potentially encode ontological constraints but this is not explored.

### A7. GoLLIE: Annotation Guidelines improve Zero-Shot Information Extraction
- **Authors**: Sainz et al. (HiTZ Center)
- **Venue**: ICLR 2024
- **ArXiv**: 2310.03668
- **Core method**: Fine-tunes Code-LLama to follow annotation guidelines defined as Python classes. Type constraints (str, list, Optional) defined in schema.
- **IE tasks**: NER, RE, event extraction (zero-shot generalization)
- **Semantic constraints**: Partial — Python type annotations serve as soft constraints during generation. However, these are format-level types (str, list), not ontological types (e.g., Person can only be head of "born_in" → Location).
- **Relevance**: MEDIUM-HIGH — Schema-as-code approach. Close in spirit but constraints are format-level, not ontology-level.

---

## Category B: Constrained Decoding Frameworks/Engines (Tooling Layer)

### B1. XGrammar: Flexible and Efficient Structured Generation Engine
- **Authors**: Dong, Ruan, et al. (MLC-AI)
- **Venue**: Preprint, Nov 2024 (arXiv 2411.15100)
- **Core method**: CFG-based constrained decoding with context-independent/dependent token split for efficiency. Supports JSON Schema, regex, custom CFG.
- **Semantic constraints**: No. Pure syntactic grammar enforcement.
- **Key result**: Up to 100x speedup over traditional grammar-constrained methods.
- **Relevance**: **HIGH as infrastructure** — This is the tool we use for the grammar layer in our system. Our semantic constraints sit on top of XGrammar.

### B2. Outlines (dottxt)
- **Venue**: Open-source library (2023-)
- **Core method**: Pioneered grammar-based constrained generation for HuggingFace models. JSON Schema, regex, CFG/EBNF.
- **Semantic constraints**: No.
- **Relevance**: Infrastructure layer. Outlines was the first widely-adopted tool; XGrammar succeeds it in performance.

### B3. LMQL: Language Model Query Language
- **Authors**: Beurer-Kellner et al. (ETH Zurich SRI Lab)
- **Venue**: PLDI 2023
- **Core method**: SQL-like query language for LLM interaction with constraints (regex, data types, choice sets). Novel evaluation semantics for character-to-token constraint translation.
- **Semantic constraints**: Partial — supports data type constraints (INT, FLOAT) and choice constraints, but not ontological/relational constraints.
- **Key result**: 75-85% fewer billable tokens vs unconstrained decoding.
- **Relevance**: LOW-MEDIUM — Different paradigm (query language vs grammar). Could theoretically express type constraints but not designed for IE ontology enforcement.

### B4. JsonFormer
- **Venue**: Open-source (2023)
- **Core method**: Generates only content tokens; fills in structure tokens deterministically based on JSON Schema. Works with HuggingFace pipelines.
- **Semantic constraints**: No. Schema compliance only.
- **Relevance**: LOW — Simple tool, limited expressiveness compared to grammar-based approaches.

### B5. Guidance (Microsoft)
- **Venue**: Open-source library (2023-)
- **Core method**: Constrained decoding framework supporting regex, CFG, JSON Schema. Integrated into vLLM/SGLang via llguidance backend.
- **Semantic constraints**: No.
- **Relevance**: Infrastructure layer.

### B6. llama.cpp GBNF Grammars
- **Venue**: Open-source
- **Core method**: GBNF grammar format for constrained generation in llama.cpp inference engine.
- **Semantic constraints**: No.
- **Relevance**: Infrastructure layer.

---

## Category C: Semantic-Level Constrained Decoding (Beyond Syntax — Not IE-Specific)

### C1. Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context
- **Authors**: Agrawal et al. (Microsoft)
- **Venue**: NeurIPS 2023
- **Core method**: Uses static analysis monitors during decoding to enforce type-checking, argument validity, and stateful API protocols in code generation.
- **Semantic constraints**: **YES** — Enforces type correctness, argument count, API protocol ordering. This is genuine semantic constraint enforcement at decode time.
- **Key result**: SantaCoder-1.1B + MGD outperforms text-davinci-003. Generalizes to Java, C#, Rust.
- **Relevance**: **CRITICAL REFERENCE** — Most analogous to our approach. They do type-checking during decoding for code; we do type-checking during decoding for IE. Key difference: their "ontology" is a programming language type system; ours is a domain ontology.
- **Code**: https://github.com/microsoft/monitors4codegen

### C2. Synchromesh: Reliable Code Generation from Pre-trained Language Models
- **Authors**: Poesia, Polozov, et al.
- **Venue**: NeurIPS 2022 (arXiv 2201.11227)
- **Core method**: Constrained Semantic Decoding (CSD) — enforces syntax, typing, and scoping constraints simultaneously during code generation. Target Similarity Tuning for example selection.
- **Semantic constraints**: **YES** — Type-checking and scope validation at decode time.
- **Key result**: Reduces SQL and DSL errors via rich constraint enforcement without fine-tuning.
- **Relevance**: **CRITICAL REFERENCE** — Pioneer of semantic constraints in decoding. Our work can be framed as "Synchromesh for IE" — bringing CSD from code to information extraction.

### C3. IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking
- **Authors**: Ugare et al.
- **Venue**: ICLR 2025
- **ArXiv**: 2410.07295
- **Core method**: First framework combining grammar-guided generation with backtracking. Allows forward/backward navigation by grammar symbols. Semantic checks trigger backtracking when violations detected.
- **Semantic constraints**: **YES** — Semantic checks (privacy leakage, SQL validity) can trigger regeneration via backtracking.
- **Key result**: 18.5% improvement over SOTA grammar-guided generation; reduces privacy leaks from 51.4% to 0%.
- **Relevance**: **HIGH** — Backtracking mechanism for semantic violations is complementary to our approach. We could potentially use backtracking when grammar ∧ semantic mask produces empty set.

### C4. CRANE: Reasoning with Constrained LLM Generation
- **Authors**: Banerjee et al.
- **Venue**: ICML 2025
- **ArXiv**: 2502.09061
- **Core method**: Balances constraint enforcement with reasoning flexibility. Augments grammar with additional rules to preserve reasoning capability. Handles both syntactic (CFG) and semantic constraints (valid variables).
- **Semantic constraints**: **YES** — Ensures generated expressions contain only valid problem-defined variables (a semantic property).
- **Key result**: Up to 10% improvement on symbolic reasoning (GSM-symbolic, FOLIO).
- **Relevance**: MEDIUM — Addresses the fundamental tension between constraint strictness and generation quality, relevant to our approach.

### C5. Syntactic and Semantic Control of LLMs via Sequential Monte Carlo
- **Authors**: Loula, LeBrun, et al.
- **Venue**: ICLR 2025 (Oral)
- **ArXiv**: 2504.13139
- **Core method**: SMC-based framework for controlled LLM generation. Flexibly incorporates domain-specific syntactic and semantic constraints. Efficiently reallocates computation during generation.
- **Semantic constraints**: **YES** — Supports arbitrary semantic constraints as probabilistic conditioning.
- **Key result**: Small open-source models outperform 8x larger models on code gen, text-to-SQL, molecule synthesis.
- **Relevance**: MEDIUM-HIGH — Elegant theoretical framework. Could be an alternative to our token masking approach, but SMC is computationally heavier.

### C6. Grammar-Aligned Decoding (GAD)
- **Authors**: Park, Wang, Berg-Kirkpatrick, et al.
- **Venue**: NeurIPS 2024
- **ArXiv**: 2405.21047
- **Core method**: ASAp algorithm — guarantees grammatical output while matching the LLM's conditional distribution. Addresses distortion problem of naive grammar-constrained decoding.
- **Semantic constraints**: No. Focuses on preserving distribution quality under syntactic constraints.
- **Key result**: Higher-likelihood outputs than existing GCD techniques while maintaining constraints.
- **Relevance**: MEDIUM — Addresses a problem we also face: naive token masking can distort generation quality. ASAp could improve our semantic masking quality.

### C7. Relation-Constrained Decoding for Text Generation (RESEAL)
- **Authors**: (NeurIPS 2022)
- **Core method**: Ensures output contains given word pairs with specified relations (syntactic or factual). RESEAL algorithm uses relation-guided probability surgery and beam allocation.
- **Semantic constraints**: **Partial** — Enforces relational constraints between words (dependency relations, KG relations), but for text generation, not extraction.
- **Relevance**: MEDIUM — Conceptually related (relation constraints during decoding) but for generation, not extraction.

---

## Category D: Ontology-Constrained IE (Post-Processing, Not Decode-Time)

### D1. RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints
- **Authors**: Olasunkanmi et al.
- **Venue**: ArXiv 2509.19057 (Nov 2025)
- **Core method**: Three-stage pipeline: (1) ontology preprocessing with predicate embeddings, (2) similarity-based retrieval with SapBERT, (3) LLM-based reranking with negation handling. Maps extracted relations to standardized ontology predicates.
- **Semantic constraints**: **YES but post-hoc** — Ontology alignment happens after extraction, not during decoding.
- **Relevance**: HIGH as comparison — Shows the need for ontology compliance in IE but addresses it via post-processing. Our approach integrates constraints into decoding.

### D2. ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs
- **Authors**: Khorshidi, Nikfarjam et al. (Apple)
- **Venue**: ArXiv 2509.04696 (Sep 2025)
- **Core method**: Production-grade system using ontology snippets (dynamically selected ontology subsets) as prompting context. Grounder validates facts post-extraction.
- **Semantic constraints**: **YES but prompt-level + post-hoc validation** — Ontology snippets guide prompting; a separate Grounder LLM validates. Not decode-time enforcement.
- **Key result**: 98.8% precision on 19M facts from 9M Wikipedia pages.
- **Relevance**: HIGH as comparison — Production system showing ontology-guided IE. But constraints are prompt-level and post-validation, not decode-time masking.

### D3. OntoKG: Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing
- **Authors**: (ArXiv 2604.02618, Apr 2026)
- **Core method**: Ontology-first KG construction with intrinsic-relational routing (classifies properties as node attributes vs graph edges). LLM-guided extraction with schema modules.
- **Semantic constraints**: Schema-level routing but post-extraction.
- **Relevance**: LOW-MEDIUM — Large-scale KG construction, not focused on decoding constraints.

---

## Category E: Benchmarks and Analysis

### E1. JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for LLMs
- **Authors**: (Guidance team + EPFL)
- **Venue**: ArXiv 2501.10868 (Jan 2025)
- **Core method**: 10K real-world JSON schemas evaluating constrained decoding on efficiency, coverage, quality. Tests Guidance, Outlines, llama.cpp, XGrammar, OpenAI, Gemini.
- **Key findings**: Constrained decoding speeds up generation by 50%; best framework supports 2x more schemas than worst; consistent 4% downstream improvement.
- **Relevance**: MEDIUM — Benchmark for syntactic constraint quality. Does not evaluate semantic constraints.

### E2. The Hidden Cost of Structure: How Constrained Decoding Affects LM Performance
- **Venue**: RANLP 2025
- **Key findings**: Fundamental divergence between base and instruction-tuned models under structural constraints. Successful constrained generation requires adapted prompts + few-shot examples. Constrained models show steeper gains from demonstrations.
- **Relevance**: HIGH — Warns about quality degradation from constraint enforcement. Our semantic masking must be carefully designed to avoid this.

### E3. SLOT: Structuring the Output of Large Language Models
- **Venue**: EMNLP 2025 Industry Track
- **Core method**: Fine-tuned lightweight LM as post-processing layer for structured output. Alternative to constrained decoding.
- **Key result**: Mistral-7B + constrained decoding: 99.5% schema accuracy.
- **Relevance**: LOW — Post-processing approach, alternative paradigm to our decode-time constraints.

---

## Category F: Surveys and Resource Lists

### F1. Awesome-LLM-Constrained-Decoding (GitHub)
- **Maintainer**: Saibo Geng (first author of A1)
- **URL**: https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding
- **Content**: Curated list of ~50 papers on constrained decoding, categorized and regularly updated.
- **Relevance**: Excellent reference list. Confirms no paper on ontology-semantic constrained decoding for IE.

### F2. Awesome-LLM4IE-Papers (GitHub)
- **URL**: https://github.com/quqxui/Awesome-LLM4IE-Papers
- **Content**: Papers on generative IE using LLMs.
- **Relevance**: Complementary resource for IE-specific papers.

### F3. A Survey of Generative Information Extraction (COLING 2025)
- **Venue**: COLING 2025
- **Content**: Comprehensive survey of generative approaches to IE.
- **Relevance**: Survey context.

---

## Summary: Gap Analysis

| Constraint Level | IE Application | Decode-Time Enforcement | Existing Work |
|---|---|---|---|
| Syntactic (valid JSON/format) | Yes | Yes | Geng et al. (A1), iNERD (A2), Clinical IE (A3) |
| Structural (valid schema fields) | Yes | Yes | XGrammar/Outlines + JSON Schema |
| Vocabulary (valid entity/relation types) | Yes | Yes | iNERD (A2), trie-based (A4) |
| **Semantic (domain/range type compatibility)** | **No** | **No** | **GAP — Our contribution** |
| Semantic (type checking) | Code gen only | Yes | MGD (C1), Synchromesh (C2) |
| Semantic (ontology compliance) | KG construction | Post-hoc only | RELATE (D1), ODKE+ (D2) |

**Core novelty confirmed**: No prior work enforces ontology-level semantic constraints (domain/range type checking) during the token-level decoding process for information extraction tasks. The closest analogues are Monitor-Guided Decoding and Synchromesh in code generation, and RELATE/ODKE+ in KG construction (post-processing only).
