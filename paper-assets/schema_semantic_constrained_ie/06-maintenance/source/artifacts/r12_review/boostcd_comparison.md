# BoostCD vs OntoCoDec Comparison

## Paper Info

- **Title**: Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction
- **Authors**: Marija Šakota, Robert West (EPFL & Microsoft)
- **Venue**: EMNLP 2025 Main (arXiv: 2506.14901)
- **Code**: https://github.com/epfl-dlab/BoostCD (public, conda env, HuggingFace data)

## Critical Finding: Task Mismatch

**BoostCD does NOT evaluate on SciERC or DocRED.** Reviewer 2's claim ("使用了 SciERC 和 DocRED 作为评估数据集") is factually incorrect.

BoostCD addresses **Closed Information Extraction (cIE)**: extracting (subject, relation, object) triplets where all entities and relations must exist in a predefined KB (Wikidata subset: 2.6M entities, 888 relations). This is fundamentally different from OntoCoDec's task (open-schema IE with type constraints on NER/RE).

## BoostCD Method Summary

Two-phase boosting approach:
1. **Phase 1**: Decode from base model in both constrained (KB-restricted) and unconstrained modes → two weak predictions
2. **Phase 2**: Learned autoregressive boosted model combines the two predictions into a final output

Constraint type: **KB membership constraints** (entity/relation must exist in Wikidata KB), not grammar or type-semantic constraints.

## BoostCD Results (Wiki-cIE Code, 10K test samples)

| Method | Model | Micro F1 | Macro F1 |
|--------|-------|----------|----------|
| BoostIE (constrained) | FlanT5-base (~250M) | 52.35 ± 0.63 | 48.81 ± 1.39 |
| BoostIE + DPO (constrained) | FlanT5-base (~250M) | 52.28 ± 0.59 | 48.29 ± 1.50 |
| SynthIE 400k (constrained) | FlanT5-base (~250M) | 35.30 ± 0.68 | 36.25 ± 1.12 |
| ReLiK (filtered) | ReLiK-large | 21.79 ± 0.53 | 12.92 ± 0.56 |

Human eval on 50 Wikipedia paragraphs:

| Method | Micro F1 | Macro F1 |
|--------|----------|----------|
| BoostIE + DPO | 34.93 ± 11.97 | 20.87 ± 4.13 |
| BoostIE | 19.33 ± 10.12 | 13.49 ± 2.77 |
| ReLiK | 23.99 ± 16.38 | 8.33 ± 1.35 |
| SynthIE 400k | 8.76 ± 4.96 | 5.35 ± 2.11 |

## Direct Comparison Table (Not Feasible)

| Dimension | OntoCoDec (Ours) | BoostCD |
|-----------|-----------------|---------|
| **Task** | Open-schema IE (NER + RE with type constraints) | Closed IE (KB-constrained triplet extraction) |
| **Datasets** | SciERC, DocRED, WikiEvents | Wiki-cIE Code, Wikipedia text |
| **Model** | Qwen3-8B, Llama-3.1-8B, Mistral-7B (7-8B) | FlanT5-base (~250M) |
| **Constraint Type** | Grammar (JSON structure + vocab) + Semantic (domain/range type compat.) | KB membership (entity/relation in Wikidata) |
| **Constraint Mechanism** | Compiled XGrammar + runtime dynamic masking | Constrained beam decoding + boosting |
| **Evaluation Metrics** | R-F1, NER-F1, DR%, CF%, RV%, ET% | Micro/Macro F1 (triplet matching) |
| **Setting** | Zero-shot + Fine-tuned (LoRA) | Supervised (300K training samples) |

## Feasibility of Running BoostCD on Our Setup

**Not recommended for direct comparison. Reasons:**

1. **Task incompatibility**: BoostCD does closed IE (map text → KB triplets), not NER/RE with type constraints. Running it on SciERC/DocRED would require substantial adaptation.
2. **Model size mismatch**: BoostCD uses FlanT5-base (250M), we use 7-8B models. Not an apples-to-apples comparison.
3. **Different constraint semantics**: BoostCD constrains to KB membership; OntoCoDec constrains type compatibility. These are orthogonal constraint dimensions.
4. **Code availability**: Code exists but is designed for Wiki-cIE/Wikidata pipeline. Adapting to SciERC/DocRED schema would be a non-trivial engineering effort.

## Recommended Response to Reviewer 2 (W1)

Since BoostCD does NOT evaluate on SciERC/DocRED and addresses a different task (closed IE vs. open-schema IE), a direct experimental comparison is methodologically inappropriate. The response should:

1. **Correct the factual error**: BoostCD evaluates on Wiki-cIE Code (Wikidata-based closed IE), not SciERC/DocRED.
2. **Articulate the task difference**: Closed IE (KB-membership constraints) vs. type-constrained open-schema IE (domain/range semantic constraints). The constraint types are orthogonal.
3. **Add qualitative discussion in §6**: Position BoostCD's boosting approach (combining constrained + unconstrained decoding) as complementary to OntoCoDec's compiled constraint approach. BoostCD uses constraints as a signal for boosting; OntoCoDec enforces constraints directly during decoding.
4. **Note potential complementarity**: BoostCD's boosting idea could theoretically be combined with OntoCoDec's constraint system — use OntoCoDec-constrained and unconstrained decodings as the two weak predictions for boosting.
