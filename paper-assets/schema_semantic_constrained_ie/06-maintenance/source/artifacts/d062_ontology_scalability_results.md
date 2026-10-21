# d062: Ontology Scalability Benchmark Results

**Date**: 2026-05-19
**Server**: westd-16980 (2x NVIDIA RTX PRO 6000 Blackwell, 96GB each)
**Model**: Qwen3-8B (base, bfloat16, cuda:0)
**Script**: `/root/schema_semantic_constrained_ie/scripts/ontology_scalability_benchmark.py`

## Table 1: Compilation Benchmark

| Ontology Scale | Entity Types | Relations | Constraint Pairs | Grammar Compile (s) | Semantic Compile (s) | Prefix Map Entries | Total Compile (s) |
|---|---|---|---|---|---|---|---|
| Small (SciERC) | 6 | 7 | 168 | 0.333 +/- 0.030 | 0.0004 +/- 0.0001 | 13 | 0.334 +/- 0.029 |
| Medium (DocRED) | 6 | 96 | 545 | 0.319 +/- 0.007 | 0.0016 +/- 0.0001 | 102 | 0.322 +/- 0.007 |
| Large (synthetic) | 100 | 500 | 6,130 | 0.332 +/- 0.006 | 0.0085 +/- 0.0001 | 600 | 0.345 +/- 0.006 |
| XLarge (synthetic) | 200 | 1,000 | 12,349 | 0.365 +/- 0.003 | 0.0171 +/- 0.0003 | 1,200 | 0.420 +/- 0.059 |

## Table 2: Inference Overhead (full_s1 mode, 10 docs, max_new_tokens=256)

| Ontology Scale | Entity Types | Relations | Unconstrained (s/doc) | Constrained (s/doc) | Overhead |
|---|---|---|---|---|---|
| Small (SciERC) | 6 | 7 | 4.187 | 4.285 | 1.02x |
| Medium (DocRED) | 6 | 96 | 4.147 | 4.272 | 1.03x |
| Large (synthetic) | 100 | 500 | 4.283 | 4.403 | 1.03x |
| XLarge (synthetic) | 200 | 1,000 | 4.285 | 4.401 | 1.03x |

## Scaling Analysis

### Compilation Time

1. **Grammar compilation (XGrammar CFG)** is the dominant cost and scales sub-linearly with ontology size: 0.319s (7 relations) to 0.365s (1000 relations), only a 1.14x increase for a 143x increase in relation count. XGrammar's JSON schema compiler handles large enum lists efficiently.

2. **Semantic constraint compilation** (first-token mapping) scales linearly with ontology size but remains negligible: 0.0004s (13 entries) to 0.017s (1200 entries). Even at 200 entity types + 1000 relations, semantic compilation takes only 17ms.

3. **Total compile time** stays under 0.5s even for the XLarge ontology (200 entities, 1000 relations, 12349 constraint pairs). Compilation is a one-time cost per ontology, amortized over all inference calls.

4. **Prefix map entries** scale linearly: entity_types + relation_types. At XLarge, 1200 entries use negligible memory.

### Inference Overhead

1. **Constraint overhead is constant at ~2-3% across all ontology scales**. Moving from 6 entity types / 7 relations to 200 entity types / 1000 relations adds no measurable additional per-token cost.

2. The per-token masking operation (TypeConstraintProcessor) only checks the active constraint context (current relation type's domain/range), not the full ontology. This explains the flat overhead profile.

3. XGrammar's grammar-based structural enforcement operates via pre-compiled bitmasks, which have O(1) per-token cost regardless of grammar complexity.

4. **Zero failures** across all scales: constrained generation completed successfully for all 10 docs at every ontology size, including XLarge (200 types, 1000 relations).

## Conclusions

1. **OntoCoDec scales efficiently to ontologies with 200+ entity types and 1000+ relations.** Total compile time stays under 0.5s and inference overhead remains at ~3% regardless of ontology scale.

2. The architecture's key scalability advantage: XGrammar handles structural constraints via pre-compiled bitmasks (O(1) per token), while the TypeConstraintProcessor only evaluates domain/range constraints for the active relation type, not the full constraint space.

3. **The claim "scalability to ontologies with hundreds of entity types has not been validated" in Limitations can now be addressed** with this empirical evidence. The first-token mapping approach requires unique first tokens per entity/relation type, which was achieved for 200 entity types using a diverse vocabulary.

4. **Practical limit**: The first-token uniqueness requirement may become a bottleneck beyond ~200 entity types for tokenizers with limited unique first-token coverage. This is a tokenizer-dependent limit, not an algorithmic one.

## Synthetic Ontology Details

- **Large (100/500)**: 100 entity types from diverse English words (Person, Location, Organization, ...), 500 relations with 2-5 random head/tail type constraints each, yielding 6,130 total constraint pairs.
- **XLarge (200/1000)**: 200 entity types, 1000 relations with 2-5 random head/tail type constraints each, yielding 12,349 total constraint pairs.
- Synthetic ontology files saved at `/root/schema_semantic_constrained_ie/data/synthetic/ontology_{large_100,xlarge_200}.json`
