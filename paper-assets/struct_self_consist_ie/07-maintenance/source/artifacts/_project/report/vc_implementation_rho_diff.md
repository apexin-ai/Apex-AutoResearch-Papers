# VC Implementation ρ Difference: Eq.6 vs Majority Threshold

Two Voting Confidence (VC) implementations exist in the codebase:

- **Eq.6 (no threshold)**: `mean([v/N for v in counter.values()])` — averages voting rate over all unique items
- **Majority threshold**: `mean([v/N for v in counter.values() if v > N/2])` else 0.0 — only items appearing in >50% of samples

D068 unified the paper to majority threshold for Table 2.

## Spearman ρ (VC vs F1), full split (non-empty gold)

| Dataset | Model | Task | N | n | ρ\_eq6 | ρ\_majority | Δρ (eq6 − maj) |
|---------|-------|------|---|---|--------|-------------|----------------|
| SciERC | Qwen | NER | 8 | 529 | 0.3792 | 0.2524 | **+0.1268** |
| SciERC | Qwen | RE | 8 | 397 | 0.3498 | 0.3311 | **+0.0187** |
| SciERC | LLaMA | NER | 8 | 529 | 0.4053 | — | — |
| SciERC | LLaMA | RE | 8 | 397 | 0.3840 | — | — |
| CoNLL | LLaMA | NER | 8 | 2756 | 0.4256 | — | — |
| CoNLL | Qwen | NER | 16 | 2756 | 0.4286 | — | — |

"—" = samples.jsonl not available locally; majority-threshold ρ requires recomputation from raw samples.

## Methodology

- **Qwen × SciERC**: Computed from local `exp_012_rerun_1024/samples_with_logprobs.jsonl` (seed=42). NER F1 uses strict span match `(start, end, type)`. RE F1 uses `(head_start, head_end, tail_start, tail_end, type)`. Values validated against worker verification result (exact match).
- **Other configurations**: ρ\_eq6 from experiment registry (all registry entries use Eq.6 implementation, confirmed by worker verification of exp\_012).

## Key observations

1. **NER Δρ is large (+0.127)**: The majority threshold discards all items appearing in ≤4 of 8 samples. For NER, many valid but rare entity mentions get filtered out, collapsing the signal's dynamic range and reducing correlation with F1.

2. **RE Δρ is small (+0.019)**: Relations are inherently sparser — most extracted relations either appear consistently (majority) or not at all. The threshold filter removes fewer items proportionally, so the two implementations converge.

3. **Direction is consistent**: Eq.6 ≥ majority threshold in both subtasks. The no-threshold version preserves more discriminative signal from low-frequency items.

4. **Practical impact on paper claims**: The qualitative ranking VC > SJ > others holds under both implementations for NER. For RE, VC remains the top signal either way. The D068 decision to use majority threshold is conservative — it reports the weaker of the two ρ values.
