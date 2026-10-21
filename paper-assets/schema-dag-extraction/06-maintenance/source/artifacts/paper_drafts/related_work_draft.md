# Section 2: Related Work

## 2.1 Schema Decomposition for Information Extraction

Handling large type schemas has emerged as a key challenge for LLM-based IE. Several strategies have been proposed to reduce schema complexity at inference time.

**Per-type and fixed decomposition.** UniversalNER \cite{uniner-2024} distills ChatGPT into a compact model by targeting one entity type per extraction call, reporting +7 F1 over ChatGPT on 43 datasets. While effective, per-type splitting sacrifices cross-type context and incurs $O(N)$ inference cost, with no principled criterion for when decomposition is necessary. KGGen \cite{kggen-2025} employs a two-stage pipeline --- entity extraction followed by relation extraction --- which decomposes at the *task* level rather than within the type schema. Similarly, DEE \cite{dee-2024} separates event detection from argument extraction with dynamic schema-aware retrieval, but does not address intra-task type partitioning.

**Similarity-based partitioning.** LLM-PEE \cite{llm-pee-2025} partitions massive event type schemas via similarity-based recall, assigning types to groups that reduce prompt length. This achieves +5.4\% event detection F1 over zero-shot baselines. However, LLM-PEE uses type similarity as an implicit proxy without empirically validating that similarity drives extraction errors --- the partition criterion optimizes for coverage, not confusability reduction.

**Schema rewriting and tool-based approaches.** PARSE \cite{parse-2025} uses an LLM to autonomously rewrite JSON schemas for better LLM consumption (+64.7\% on SWDE), treating schema optimization as a black-box process without modeling type interactions. SPT \cite{spt-2025} reframes schemas as parameterized tools for LLM tool-calling, offering a novel interface but not addressing why certain type configurations degrade extraction. DLISC \cite{dlisc-2025} introduces dual-LoRA with incremental schema caching for on-device efficiency, orthogonal to our focus on type confusability.

**Our distinction.** Unlike all prior decomposition methods, SDGD is grounded in an empirically validated degradation model: we first demonstrate that type confusability independently predicts extraction failure (controlling for count), then operationalize this finding into a graph-coloring-based decomposition that *provably* separates highly confusable types. No prior work explicitly isolates confusability from count as a degradation factor, nor optimizes decomposition to minimize it.


## 2.2 Confusability-Aware Approaches in NLP

The notion that semantically similar labels cause classification errors has appeared across NLP, though not in the context of training-free LLM IE schema design.

**Label confusion in training.** IEPile \cite{iepile-2024} constructs hard negative schemas --- semantically proximate type sets --- during *training* to improve a model's type discrimination ability. This confirms that confusable schemas are harder, but the intervention is at training time. Our work addresses *inference-time* confusability for training-free systems where model weights are frozen. The Familiarity metric \cite{familiarity-2025} quantifies label shift between synthetic training data and evaluation sets, revealing that zero-shot NER scores are overestimated when training labels overlap with evaluation labels. This measures *evaluation bias* from label similarity, not extraction-time confusion --- but supports our premise that type similarity is a meaningful confound.

**Multi-agent debate for type resolution.** CROSSAGENTIE \cite{crossagentie-2025} deploys cross-type debate within multi-agent systems to resolve entity-label conflicts: when an entity is assigned conflicting types by different agents, intra-group debate adjudicates. This *reactively* addresses type confusion after it occurs. CMAS-NER \cite{cmas-ner-2025} similarly uses cooperative multi-agent collective intelligence to overcome context correlation and indiscriminate demonstration problems in zero-shot NER. Our approach is *proactive*: we prevent type confusion by ensuring highly confusable types never co-occur in a single extraction call. The two strategies are complementary --- SDGD decomposition could serve as a pre-processing stage for multi-agent systems.

**Positional and attention effects.** Liu et al. \cite{lost-in-middle-2024} demonstrate that LLMs degrade when relevant information appears in the middle of long contexts, exhibiting U-shaped attention patterns. While not IE-specific, this provides additional motivation for schema decomposition: shorter prompts with fewer types reduce the risk of attention-related information loss. To our knowledge, no prior work has connected positional attention biases to IE schema prompt design.


## 2.3 LLM-Based Information Extraction

Training-free LLM IE has progressed rapidly, establishing both the opportunity and the challenge that motivate our work.

**Instruction-tuned IE models.** GoLLIE \cite{gollie-2024} demonstrates that code-style schema definitions with annotation guideline following enable strong zero-shot IE from a Code-LLaMA backbone. Code4UIE \cite{code4uie-2024} extends this to retrieval-augmented code generation for universal IE. KnowCoder \cite{knowcoder-2024} encodes schema knowledge via code structures into LLMs. These models internalize schema understanding through fine-tuning, sidestepping inference-time schema complexity. However, they require task-specific training, limiting deployment flexibility.

**Zero-shot extraction methods.** Self-improving NER \cite{self-improve-ner-2024} generates synthetic examples via LLM self-prompting, while ReasoningNER \cite{reasoning-ner-2025} applies chain-of-thought reasoning to achieve +12.3 F1 over GPT-4 in zero-shot settings. ZeroNER \cite{zeroner-2025} leverages entity type descriptions to produce LLM supervision for a BERT student model (+16\% F1 over LLMs on hard zero-shot). These methods improve extraction within a fixed schema presentation, but do not address how schema *structure* --- the composition and similarity of co-presented types --- affects quality.

**Compact and efficient models.** GLiNER \cite{gliner-2024} achieves competitive zero-shot NER with a bidirectional encoder via parallel entity extraction, and GLiNER2 \cite{gliner2-2025} extends this to multi-task IE. NuNER \cite{nuner-2024} uses contrastive pre-training on LLM-annotated data for strong few-shot performance. These non-LLM alternatives avoid schema complexity issues by design (parallel per-type extraction), but sacrifice the generality and zero-shot flexibility of LLM-based approaches.

**Surveys.** Xu et al. \cite{llm4ie-survey-2024} provide a comprehensive survey of LLM-based generative IE, covering prompting strategies, fine-tuning paradigms, and benchmarks. Our work contributes to the prompting strategy dimension by showing that *what types are co-presented* matters as much as *how they are presented*.
