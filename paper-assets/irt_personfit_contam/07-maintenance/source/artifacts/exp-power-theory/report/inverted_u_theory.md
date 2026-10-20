# Theoretical Explanation of the Inverted-U Detection Pattern

## Mechanism

The left-tail detection power exhibits an inverted-U as a function of contamination
fraction $\pi$ because the **sign of $\mathbb{E}[lz^*]$ reverses** at high $\pi$.

### Phase 1: Moderate contamination (small to medium $\pi$)
- Contaminated items create an **aberrant** response pattern: items the examinee would
  have failed now appear correct.
- MLE $\hat\theta$ is biased upward but cannot fully explain the inflated score.
- Result: $lz^* < 0$ (too many "unexpected" correct responses).
- Left-tail power increases with $\pi$.

### Phase 2: High contamination ($\pi \to 1$)
- Nearly all items are correct; $\hat\theta$ approaches the upper boundary.
- At high $\hat\theta$, the model **expects** nearly all items correct.
- The all-correct pattern becomes **over-consistent** rather than aberrant.
- Result: $lz^* > 0$ (pattern is more predictable than expected).
- Left-tail power **drops** as $lz^*$ moves to the right tail.

## Theoretical vs Empirical Crossover Points

The crossover $\pi^*$ where $\mathbb{E}[lz^*] = 0$:

| Benchmark | n_items | Theory $\pi^*$ | Simulation crossover |
|-----------|---------|----------------|---------------------|
| MMLU | 14,042 | 81.0% | 75–90% |
| HellaSwag | 10,042 | 82.6% | 75–90% |
| GSM8K | 1,319 | 85.0% | 75–90% |
| ARC-C | 295 | 82.1% | 75–90% |
| HumanEval | 164 | 82.4% | 75–90% |

## Left-tail Power Peak

| Benchmark | n_items | Peak $\pi$ | Peak left-tail power |
|-----------|---------|------------|---------------------|
| MMLU | 14,042 | 25% | 0.9804 |
| HellaSwag | 10,042 | 43% | 0.9207 |
| GSM8K | 1,319 | 37% | 0.8341 |
| ARC-C | 295 | 59% | 0.4196 |
| HumanEval | 164 | 53% | 0.6028 |

## Why Two-sided Detection Eliminates the Inverted-U

Two-sided detection ($|lz^*| > 1.96$) captures **both** tails:
- Left tail catches moderate contamination ($lz^* < 0$, aberrant pattern).
- Right tail catches high contamination ($lz^* > 0$, over-consistent pattern).

The right-tail power increases precisely where the left-tail power drops, so the
combined two-sided power is **monotonically increasing** (or nearly so) with $\pi$
for sufficiently large benchmarks, eliminating the inverted-U artifact.

## Implications for Practice

1. **Always use two-sided detection** ($|lz^*| > 1.96$) instead of one-sided.
2. The crossover region ($\pi^* \approx 75$–$85\%$) is relatively consistent across
   benchmarks, suggesting it is primarily driven by the contamination-to-ability
   mapping rather than item characteristics.
3. Benchmarks with more items are more robust: with $n > 1000$ items, two-sided
   power exceeds 80% across almost all contamination levels.
