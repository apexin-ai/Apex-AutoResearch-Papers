# Collapse Signal Report Summary

## Key Finding

**K=8 curation exhibits FORMAT/TEMPLATE collapse that Vendi Score cannot detect.** The collapse is primarily in opening patterns and response structure, not in content/semantic diversity.

## Experimental Setup

| Condition | Responses per Gen | Generations Compared |
|-----------|------------------|---------------------|
| K=8 single_reward curation | 16,000 | Gen0 vs Gen2 |
| Baseline (no curation) | 8,000 | Gen0 vs Gen2 |

## Vendi Score Context

- K=8 curation: 107.21 -> 107.25 (flat, +0.04)
- Baseline: 105.42 -> 108.72 (increasing, +3.30)

## Collapse Signals (Gen0 -> Gen2 deltas)

| Metric | K=8 Curation | Baseline | Interpretation |
|--------|-------------|----------|----------------|
| Trigram repetition rate | +0.118 (0.391 -> 0.509) | +0.123 (0.316 -> 0.439) | Similar increase |
| 4-gram repetition rate | +0.139 (0.233 -> 0.373) | +0.136 (0.178 -> 0.314) | Similar increase |
| Opening unique ratio | **-0.335** (0.701 -> 0.367) | -0.282 (0.794 -> 0.513) | Curation worse |
| Opening entropy (bits) | **-1.126** (13.09 -> 11.96) | -0.745 (12.43 -> 11.68) | Curation worse |
| Near-dup start rate | **50% -> 84%** | 38% -> 75% | Curation much worse |
| Global TTR | -0.011 (0.061 -> 0.050) | -0.014 (0.083 -> 0.069) | Curation slightly better |
| Per-response TTR | -0.008 (0.684 -> 0.676) | -0.023 (0.683 -> 0.660) | Curation better |

## Evidence Details

### 1. Opening Pattern Collapse (Primary Signal)

- K=8 Gen2: only **36.7% unique openings** (vs 51.3% baseline)
- Near-duplicate opening rate jumps from 50% to **84%** in K=8 curation
- Mechanism: ArmoRM implicitly favors certain opening patterns; iterative selection amplifies this into templates
- Vendi blind spot: embedding models are insensitive to surface-level formatting

### 2. Degenerate Token Repetition

- K=8 Gen2: "answer: answer: answer: answer:" is 2nd most common 4-gram (1149x)
- Baseline Gen2 is actually WORSE: "chopped chopped chopped" (1282x), "i_jump i_jump i_jump" (1008x)
- Implication: generic SFT mode collapse, not curation-specific

### 3. Length Compression (Low severity)

- K=8: mean drops 2.8 words, std drops 0.95
- Baseline: mean grows 1.0, std grows 2.8
- Absolute change small relative to mean (~160 words)

### 4. Per-response Vocabulary Stability

- Per-response TTR drops only -0.008 in curation vs -0.023 in baseline
- Curation selects higher-quality responses, preserving per-response lexical richness

## Recommended Complementary Metrics

1. **opening_entropy** - first-10-word entropy
2. **near_duplicate_start_rate** - 50-char fingerprint collision rate
3. **structural_template_frequency** - regex pattern match rates

## Conclusion

K=8 curation collapse is FORMAT/TEMPLATE collapse, not CONTENT/SEMANTIC collapse. Vendi Score correctly captures that semantic diversity is maintained but misses that surface-level generation is becoming template-bound. Opening-entropy or n-gram distinctness would catch this.
