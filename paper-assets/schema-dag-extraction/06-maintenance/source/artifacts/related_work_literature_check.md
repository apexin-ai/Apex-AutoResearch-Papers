# Related Work Literature Check (2024-2025)
Searched: 2026-05-22

## Potentially Missing Papers

### 1. Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts (Golde et al., 2025)
- **Venue:** NAACL 2025 (Long Paper)
- **Citations:** ~5-10 (recent, Dec 2024 preprint)
- **Relevance:** Proposes "Familiarity" metric measuring semantic similarity between entity types across train/eval datasets to quantify label shift difficulty. Conceptually very close to our "type confusability" — both use type-level semantic similarity as a predictor of zero-shot NER difficulty. They focus on train-eval overlap while we focus on within-schema inter-type similarity, but a reviewer will expect this citation.
- **Recommended action:** Add to Related Work §"Schema complexity" paragraph
- **Suggested insertion point:** After Ashok & Lipton 2023 discussion of entity type difficulty, add: "More recently, Golde et al. (2025) propose a 'Familiarity' metric quantifying semantic similarity between entity types to predict zero-shot NER transfer difficulty, complementing our within-schema confusability measure."
- **ArXiv:** 2412.10121

### 2. LLM4RE: A Data-centric Feasibility Study for Relation Extraction (Swarup et al., 2025)
- **Venue:** COLING 2025 (Main)
- **Citations:** ~10-15
- **Relevance:** 2100+ experiments on 5 LLMs showing they are not robust to complex data characteristics in RE. Directly relevant as empirical evidence that RE difficulty stems from data/schema characteristics, not just model capability. Companion paper "MaxRE" (Swarup et al., IEEE Access 2024) extends this to 15 RE algorithms and 7 datasets.
- **Recommended action:** Add to Related Work §"Zero-shot IE with LLMs" paragraph
- **Suggested insertion point:** After Wadhwa et al. 2023 / Xu et al. 2024 discussion, add: "Swarup et al. (2025) conduct a data-centric feasibility analysis showing LLMs are not robust to complex relational data characteristics across 2100+ experiments, motivating our controlled study of specific schema factors."
- **ArXiv:** 2409.04934

### 3. Pointing out the Shortcomings of RE Models with Semantically Motivated Adversarials (Nolano et al., 2024)
- **Venue:** LREC-COLING 2024
- **Citations:** ~10-15
- **Relevance:** Shows RE model performance drops -48.5% F1 when entity mentions are replaced with semantically similar adversarial substitutions. Demonstrates that semantic confusability at the entity level (not just type level) degrades RE performance — directly supporting our type confusability hypothesis from a complementary angle.
- **Recommended action:** Add to Related Work §"Schema complexity" or §"Type confusability" paragraph
- **Suggested insertion point:** After introducing the type confusability concept, add: "Nolano et al. (2024) demonstrate a complementary finding: RE models suffer catastrophic performance drops (-48.5% F1) under semantically motivated adversarial entity replacements, suggesting that surface-form similarity between entities exacerbates extraction difficulty."
- **ArXiv:** 2402.19076

### 4. GLiREL: Generalist Model for Zero-Shot Relation Extraction (Boylan et al., 2025)
- **Venue:** NAACL 2025 (Long Paper)
- **Citations:** ~10-15
- **Relevance:** Addresses the scalability bottleneck where existing zero-shot RE models suffer from processing each (entity-pair, label) combination separately — performance/efficiency degrades with type count. Achieves SOTA on FewRel/WikiZSL. Relevant as evidence that type count creates computational and modeling challenges in zero-shot RE.
- **Recommended action:** Consider adding to Related Work §"Zero-shot IE" — borderline
- **Suggested insertion point:** Near GLiNER/NuNER mention if present: "GLiREL (Boylan et al., 2025) addresses the scalability limitation of zero-shot RE models whose computational cost grows quadratically with the number of candidate relation types."
- **ArXiv:** 2501.03172

## No Action Needed

| Paper | Reason |
|-------|--------|
| PARSE (EMNLP 2025 Industry) | Schema optimization for extraction reliability; focuses on engineering fixes rather than analyzing complexity factors. Tangentially related but not core. |
| How Good are LLMs at RE under Low-Resource (2024) | Focus is cross-lingual low-resource RE, not schema complexity. |
| Show Less, Instruct More / SLIMER (2024) | About enriching prompts with type definitions for zero-shot NER. Related to GoLLIE approach already cited. |
| Label-Guided ICL for NER / DEER (2025) | Leverages label statistics for demonstration selection; not about type count/confusability effects. |
| Million-Label NER / GLiNER bi-encoder (2026) | Too recent (Feb 2026); shows label count scalability problem but published after typical citation window. |
| Understanding LLM Performance Degradation in Multi-Instance (2026) | Too recent (Mar 2026); about multi-document processing, not IE type count. |
| Finite Sample Corrections for TOST (Boulaguiem 2024) | Statistical methodology paper (α-TOST correction). Relevant if we want to cite improved TOST methods, but our use of standard TOST is already well-grounded with Cohen 1988 / Schuirmann 1987. |

## Summary
- **4 papers found potentially missing**
- **Recommended additions (priority order):**
  1. Golde et al. 2025 (Familiarity) — strongest match, directly measures type semantic similarity as difficulty predictor
  2. Swarup et al. 2025 (LLM4RE) — large-scale empirical evidence of LLM RE fragility to data characteristics
  3. Nolano et al. 2024 — adversarial evidence for semantic confusability degrading RE
  4. Boylan et al. 2025 (GLiREL) — borderline, type count scalability in zero-shot RE
- **Critical addition:** Golde et al. 2025 is the most likely to be flagged by a reviewer as missing, given its direct conceptual overlap with type confusability.
