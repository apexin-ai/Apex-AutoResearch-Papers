# Experiment: exp_a3_ace05_re — Relation Extraction Self-Consistency Diagnostic

## Objective

Validate that the SC diagnostic cascade (degeneracy → agreement → LP-quality gap) generalizes from NER to Relation Extraction. RE is the closest structured prediction extension: same span-based output, but with entity pairs + relation types instead of single entity spans.

## Data Source

### Primary: SciERC (test split)

- **Why SciERC, not ACE05**: ACE05 requires LDC license (restricted access, no public download). SciERC is publicly available, already integrated in the pipeline (`data_utils.load_scierc()`), and has both entity and relation annotations.
- **Dataset**: SciERC test set (~551 sentences from scientific abstracts)
- **Entity types** (6): Generic, Material, Method, Metric, OtherScientificTerm, Task
- **Relation types** (7): COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR
- **Format**: DyGIE++ JSON → converted to UIE format via `_parse_scierc_sentence()`
- **Download**: `bash scripts/data/get_scierc.sh` from DyGIE++ repo, or already present on server

### Filtering

Only instances with ≥1 gold relation are included in RE evaluation (skip relation-free sentences). Expected: ~200–300 instances after filtering.

## Model

- **Base**: Qwen2.5-7B-Instruct (same as NER experiments for controlled comparison)
- **Prompt**: Few-shot RE prompt with schema hint
- **Constrained decoding**: XGrammar with UIE_JSON_SCHEMA (already supports relations field)

## Sampling Configuration

| Parameter | Value |
|-----------|-------|
| N (samples) | 8 |
| Temperature | 1.0 |
| max_tokens | 1024 |
| use_grammar | True |
| collect_logprobs | True |
| subtask | "re" |

Greedy baseline: T=0, N=1 (automatic via `run_sampling_pipeline`).

## Prompt Template

Uses `build_uie_prompt(text, subtask="re", schema_hint=SCIERC_SCHEMA_HINT)` which produces:

```
Extract all relations (head entity, relation type, tail entity) from the following text.
Output a JSON object with the fields: entities, relations, events.

Text: {text}
Schema: Entity types: Generic, Material, Method, Metric, OtherScientificTerm, Task
Relation types: COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR

Output format: {"entities": [], "relations": [{"head": "...", "tail": "...", "type": "...", "head_start": <int>, "head_end": <int>, "tail_start": <int>, "tail_end": <int>}], "events": []}
```

Alternative: `use_train_format=True` for the train-aligned template (extracts entities + relations jointly).

## Output JSON Schema

Same as `UIE_JSON_SCHEMA` in sampling.py. Relation fields:

```json
{
  "head": "entity text",
  "tail": "entity text", 
  "type": "USED-FOR",
  "head_start": 10,
  "head_end": 25,
  "tail_start": 30,
  "tail_end": 45
}
```

## Evaluation Metrics

### Primary: Relation Strict Match F1

`relation_strict_match()` in evaluation.py — (head_start, head_end, tail_start, tail_end, type) must all match exactly. Micro-averaged P/R/F1.

### SC Diagnostic Metrics (per-instance)

1. **Degeneracy**: All N samples produce identical relation sets → `is_degenerate_re()`
2. **Fleiss' Kappa (surface)**: `fleiss_kappa_surface(samples, subtask="re")` using (head, tail, type) surface keys
3. **Structural Soft Jaccard**: `structural_consistency_soft_jaccard(samples, subtask="re")` with `_re_soft_jaccard_pair()` — head/tail span overlap × type match via Hungarian matching
4. **Oracle Best-of-N**: `oracle_best_of_n(samples, gold, subtask="re")`
5. **LP-weighted construction**: Adapted from NER consensus_construct to aggregate relation triples

### SC Failure Mode Diagnostics (F1–F4)

| Mode | Definition (RE adaptation) |
|------|---------------------------|
| F1: Degeneracy | All 8 samples produce identical relation sets |
| F2: Low agreement | Fleiss' κ < 0.3 AND non-degenerate |
| F3: High agreement, low quality | κ ≥ 0.3 but greedy F1 < 0.3 |
| F4: LP-quality gap | construction_F1 − greedy_F1 < −0.05 (LP hurts) |

## Pipeline Reuse

| Component | Reuse | Notes |
|-----------|-------|-------|
| VLLMSampler | 100% | No changes needed |
| XGrammar schema | 100% | UIE_JSON_SCHEMA already has relations |
| build_uie_prompt | 100% | subtask="re" template exists |
| parse_extraction_output | 100% | _validate_relations() exists |
| realign_spans | 100% | Handles relation head/tail spans |
| run_sampling_pipeline | 100% | Pass subtask="re" |
| fleiss_kappa_surface | 100% | RE surface keys implemented |
| structural_consistency_soft_jaccard | 100% | _re_soft_jaccard_pair() exists |
| oracle_best_of_n | 100% | Uses per_instance_f1 with subtask="re" |
| relation_strict_match | 100% | Already in evaluation.py |
| consensus_construct | ~30% | NER-specific, needs RE adaptation |
| is_degenerate | ~30% | NER-specific, needs RE adaptation |
| bootstrap test | ~50% | Needs RE-specific key extraction |

## GPU Requirements

- **Model**: Qwen2.5-7B-Instruct → ~15 GB VRAM
- **Server**: autodl-5090 (single GPU sufficient)
- **Estimated time**: ~15 min for 300 instances × 8 samples with vLLM batched inference
- **Disk**: <100 MB for output JSONL

## Dependencies

```
vllm, transformers, xgrammar, torch
numpy, scipy, datasets (for SciERC loading)
```

All already installed on autodl-5090 from NER experiments.
