# Literature Survey: Evidence Generation Overhead in Relation Extraction

**Context**: SFT model generating relation triples + evidence sentences yields rel_f1=0.4057; generating triples only yields rel_f1=0.4893 (+20.6%). This survey contextualizes this evidence generation overhead.

---

## 1. Multi-task Learning Overhead in IE

- **[An Overview of Multi-Task Learning in Deep Neural Networks](https://arxiv.org/abs/1706.05098)** (Ruder, arXiv 2017) — Foundational MTL survey establishing that auxiliary tasks can cause *negative transfer* when task gradients conflict, with one task dominating and degrading others. Directly frames our evidence-as-auxiliary-task degradation.

- **[ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/60f9118a849e8e9a0c67e2a36ad80ebf-Abstract-Conference.html)** (Jiang et al., NeurIPS 2023) — Shows auxiliary tasks frequently cause negative transfer due to gradient conflicts; proposes periodic forking/merging to filter detrimental updates. Confirms that even "helpful" auxiliary tasks can hurt the primary objective.

- **[An Empirical Study of Pipeline vs. Joint approaches to Entity and Relation Extraction](https://aclanthology.org/2022.aacl-short.55/)** (Giorgi et al., AACL 2022) — Finds that with proper span representations, pipeline models can match or exceed joint models; joint approaches with shared encoders may harm accuracy because NER and RE require different feature spaces. Supports decoupling argument.

- **[Do the Benefits of Joint Models for Relation Extraction Extend to Document-level Tasks?](https://aclanthology.org/2023.ijcnlp-short.6/)** (Saini et al., IJCNLP-AACL 2023) — Directly shows joint models' advantage over pipeline disappears at document level — pipeline models outperform joint models on DocRE. Highly relevant: joint modeling overhead amplifies with longer documents.

- **[Mitigating Negative Transfer in Multi-Task Learning with Exponential Moving Average Loss Weighting Strategies](https://arxiv.org/abs/2211.12999)** (Phan et al., AAAI 2023 Student Abstract) — Demonstrates that in MTL a subset of tasks can dominate training, degrading non-dominant tasks. Loss weighting mitigates but does not eliminate the problem.

## 2. Evidence/Rationale Generation Cost

- **[Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse](https://arxiv.org/abs/2410.21333)** (Liu et al., ICML 2025) — CoT prompting causes up to 36.3% absolute performance drop on tasks where deliberation is counterproductive. Demonstrates that forcing models to generate intermediate reasoning can actively harm task performance — analogous to our evidence generation overhead.

- **[On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://arxiv.org/abs/2411.15382)** (Lobo et al., arXiv 2024) — SFT/QLoRA fine-tuning degrades CoT faithfulness by 13–18 pp in smaller models and generally reduces CoT reasoning performance. Shows fine-tuning for rationale generation creates a tension between explanation quality and task accuracy.

- **[Token-Budget-Aware LLM Reasoning](https://aclanthology.org/2025.findings-acl.1274/)** (ACL Findings 2025) — Demonstrates that reasoning tokens compete with answer tokens for output budget; achieves comparable accuracy with 67% fewer output tokens. Directly relevant: evidence tokens consume budget that could serve relation extraction.

- **[LLM-Driven Information Extraction: The Output Token Limitation Issue](https://atlassc.net/2026/01/15/the-asymmetry-of-generative-intelligence)** (AtlasSC, 2026) — Identifies a fundamental constraint: practitioners must choose between depth of reasoning (CoT tokens) and breadth of extraction (JSON payload). As output grows, attention to source text diminishes. Precisely our triples-vs-evidence token competition.

## 3. Decoupling in Structured Prediction

- **[Revisiting Relation Extraction in the era of Large Language Models](https://aclanthology.org/2023.acl-long.868/)** (Wadhwa et al., ACL 2023) — Treats RE as seq2seq generation; finds few-shot GPT-3 matches fully supervised models. Establishes that generative RE is viable but output format design critically affects performance.

- **[GenRES: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models](https://aclanthology.org/2024.naacl-long.155/)** (Jiang et al., NAACL 2024) — Shows prompting LLMs with fixed relation/entity sets causes hallucinations; output structure matters. Reinforces that generation format (with or without evidence) has non-trivial impact on extraction quality.

- **[A Survey of Generative Information Extraction](https://aclanthology.org/2025.coling-main.324/)** (COLING 2025) — Comprehensive survey of generative IE; discusses linearization strategies for structured output and the overhead of generating auxiliary information alongside core extractions.

- **[Large Language Models for Generative Information Extraction: A Survey](https://arxiv.org/abs/2312.17617)** (Xu et al., Frontiers of Computer Science 2024) — Notes that generative IE reformulates extraction as seq2seq, but output token limits create fundamental bottleneck — models can read entire documents but can only write limited structured output, making token allocation critical.

## 4. DocRE Methods and Evidence Handling

- **[DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction](https://aclanthology.org/2023.eacl-main.145/)** (Ma et al., EACL 2023) — Uses evidence as attention supervision signal (not generated output); avoids the generation overhead by treating evidence as an internal mechanism rather than explicit output. Evidence improves RE when used to *guide* the model, not as a generation target.

- **[Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion](https://aclanthology.org/2022.findings-acl.23/)** (Xie et al., ACL Findings 2022) — Jointly trains lightweight evidence extractor with RE model but fuses predictions at *inference* rather than generating evidence in the same output sequence. Decoupled design avoids token competition; improves RE by +1.37 Ign F1 on DocRED.

- **[Entity and Evidence Guided Relation Extraction for DocRED](https://arxiv.org/abs/2008.12283)** (Huang et al., arXiv 2020) — Early work using evidence sentences to guide entity-pair representations. Evidence is used as an attention mask, not generated — avoids the generation cost entirely.

- **[SIRE: Separate Intra- and Inter-sentential Reasoning for Document-level Relation Extraction](https://aclanthology.org/2021.findings-acl.47/)** (Zeng et al., ACL Findings 2021) — Separates intra- and inter-sentential reasoning into distinct representation pathways. Implicitly handles evidence by architectural separation rather than explicit prediction, avoiding the joint generation overhead.

---

## Synthesis

The literature reveals a consistent pattern: **auxiliary generation tasks impose a non-trivial cost on the primary task, especially in sequence-to-sequence settings.** Three mechanisms explain this:

1. **Gradient conflict / negative transfer** (Ruder 2017; ForkMerge, NeurIPS 2023): When evidence and relation extraction share model capacity, their gradients can conflict, with evidence generation dominating and degrading RE performance.

2. **Token budget competition** (Token-Budget-Aware 2025; AtlasSC 2026): In generative models, evidence tokens directly compete with relation tokens for output sequence capacity. Longer evidence outputs reduce the model's ability to attend back to source text for accurate extraction.

3. **Deliberation overhead** (Mind Your Step, ICML 2025; Lobo et al. 2024): Forcing explicit intermediate reasoning can actively hurt performance when the task benefits more from pattern recognition than from step-by-step justification.

Critically, **existing DocRE methods (DREEAM, Eider, SIRE) avoid this overhead by design** — they use evidence as internal attention signals or separate lightweight modules, never as co-generated output in the same sequence. No prior work has quantified the cost of jointly *generating* evidence and relations in a single autoregressive output, which is exactly what our no-evidence ablation (+20.6% rel_f1) measures. This positions our finding as the first empirical evidence that evidence generation in generative DocRE creates a substantial task interference, providing strong motivation for decoupled architectures that separate evidence reasoning from relation prediction.
