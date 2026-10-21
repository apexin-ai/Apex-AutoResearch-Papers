# α=0.50 seed=43 Analysis Report

## Gen0 → Gen10 Metrics

| Metric | gen0 | gen10 | drift% |
|--------|------|-------|--------|
| token_entropy | 3.2342 | 2.6707 | -17.42% |
| ECE | 0.0108 | 0.0971 | +798.8% |
| perplexity | 26.949 | 32.633 | +21.09% |
| distinct_1 | 0.0983 | 0.0624 | -36.53% |
| distinct_2 | 0.5132 | 0.2617 | -49.01% |
| distinct_3 | 0.8057 | 0.4122 | -48.84% |
| effective_rank | 46.613 | 59.425 | +27.49% |
| mauve | 0.0335 | 0.0228 | -31.99% |

## Cross-Seed Comparison (α=0.50: s43 vs s42)

| Metric | s43 gen10 | s42 gen10 | rel. diff | s43 drift | s42 drift |
|--------|-----------|-----------|-----------|-----------|-----------|
| entropy | 2.6707 | 2.632 | +1.5% | -17.4% | -18.6% |
| ECE | 0.0971 | 0.102 | -4.8% | +799% | +843% |
| ppl | 32.633 | 32.64 | -0.02% | +21.1% | +21.1% |
| d1 | 0.0624 | 0.062 | +0.7% | -36.5% | -37.3% |
| d2 | 0.2617 | 0.251 | +4.3% | -49.0% | -51.5% |
| d3 | 0.4122 | 0.387 | +6.5% | -48.8% | -52.4% |

Cross-seed consistency: **excellent**. Gen10 absolute values within 1-7%, drift directions and magnitudes tightly aligned.

## Cross-Alpha Comparison (seed=43: α=0.50 vs α=0.25)

| Metric | a050 drift | a025 drift | regime difference |
|--------|------------|------------|-------------------|
| entropy | -17.4% | -5.0% | 3.5x more loss at α=0.50 |
| ECE | +799% | +99% | 8x more calibration collapse |
| ppl | +21.1% | -18.7% | **direction flip** |
| d1 | -36.5% | -40.5% | slightly less at α=0.50 |
| d2 | -49.0% | -56.4% | slightly less at α=0.50 |
| d3 | -48.8% | -58.7% | slightly less at α=0.50 |

Key finding: ppl direction flips between α=0.25 (improves) and α=0.50 (degrades), confirming regime-dependent behavior (Claim 2).
