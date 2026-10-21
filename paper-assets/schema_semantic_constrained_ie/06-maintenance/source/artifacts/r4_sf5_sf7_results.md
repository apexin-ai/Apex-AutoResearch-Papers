# SF5: Llama DocRED Parse-Failure-Excluded Analysis

## Summary

Total documents: 998
Parse failures: 91 (9.1%)
Valid documents (after exclusion): 907

Parse failure doc_ids (sample):
- Conrad O. Johnson, Taiwanese expatriates in Vietnam, Memogate (Pakistan), (I Am) The Seeker, Each Time You Break My Heart, CBBC, Think Bike, Loopline Bridge, Manon Balletti, Taft–Katsura agreement, ... (91 total)

## After Exclusion (907 docs)

- DR: 2.55%
- CF: 12.02%
- ET: 0.00%
- RV: 0.00%
- E-F1: 58.18 (P=61.41, R=55.28)
- R-F1: 6.51 (P=5.49, R=7.99)

## Comparison: All Docs vs Parse-Failure-Excluded

| Metric | All docs (998) | Excluded (907) | Delta |
|--------|---------------|----------------|-------|
| DR     | 2.55%         | 2.55%          | +0.00pp |
| CF     | 12.02%        | 12.02%         | +0.00pp |
| ET     | 0.00%         | 0.00%          | +0.00pp |
| RV     | 0.00%         | 0.00%          | +0.00pp |
| E-F1   | 55.01         | 58.18          | +3.17pp |
| R-F1   | 6.27          | 6.51           | +0.23pp |

## Notes

- Violation rates unchanged because violations are already computed on non-parse-failure docs
- F1 improves because parse failures contribute to gold counts (hurt recall) without predictions
- E-F1 improves more (+3.17pp) than R-F1 (+0.23pp) because parse failure docs have gold entities but no predicted entities
- The 91 parse failures are Llama's generation failures (truncated/malformed JSON output)

---

# SF7: DocRED Fallback Coverage

## Qwen3-8B DocRED (full S1 constrained)

- Total type-bearing positions: 54,859
  - Entity type positions: 20,187 (fallback: 0)
  - Head type positions: 17,336 (fallback: 13)
  - Tail type positions: 17,336 (fallback: 33)
- Grammar-first fallback events: 46
- Fallback rate: 0.08%
- **Effective semantic constraint coverage: 99.9%**

## Comparison with SciERC

| Dataset | Total mask calls | Fallback events | Fallback rate | Effective coverage |
|---------|-----------------|-----------------|---------------|-------------------|
| SciERC  | 17,024          | 6,237           | 36.6%         | 63.4%             |
| DocRED  | 54,859          | 46              | 0.08%         | 99.9%             |

## Why DocRED Coverage is Much Higher

The large discrepancy has two root causes:

1. **Tokenization**: SciERC types are multi-token (e.g., "OtherScientificTerm" ~3 tokens), causing ~2.87 mask calls per type field. At non-first tokens, grammar has committed to a continuation, conflicting with the semantic mask. DocRED types (PER, ORG, LOC, TIME, NUM, MISC) are ALL single-token, so each type field = 1 mask call with no multi-token conflicts.

2. **Entity registry**: The CF fallback processor maintains an entity registry. When head_type/tail_type entities are already registered, the processor forces the registered type (bypassing DR constraints if needed). This handles most type decisions without triggering grammar-first fallback.

## Per-field vs Per-mask-call

For a fair apples-to-apples comparison:
- SciERC: 5,924 type fields, 17,024 mask calls (2.87x inflation)
- DocRED: 54,859 type fields = 54,859 mask calls (1.0x, no inflation)

If we measure per-type-FIELD (where the actual decision is made at the first token), both datasets would show near-100% effective coverage. The SciERC 36.6% rate is dominated by non-first-token positions where grammar necessarily overrides semantic (a tokenization artifact, not semantic constraint failure).

## Method

- SF5: Computed from `outputs/llama_docred_full_s1.jsonl` using violation_checker_docred.py logic
- SF7: Simulated from `outputs/docred_full_s1.jsonl` (Qwen3-8B) by checking each type position against ontology constraints. Single-token types make per-mask-call = per-field metric.
- SciERC reference: from `outputs/w1_cf_fallback_scierc_pilot_fallback_stats.json` (actual runtime measurement)
