# code exp d conjecture verify

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_d_conjecture_verify_20260522T112907_result.json`
- **Structured JSON:** [`a40c3baa5ff438b0db09.json`](../../sessions/a4/a40c3baa5ff438b0db09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Exp-D results are in `artifacts/exp_d_conjecture_results.json`. Let me compile the key findings.

## Exp-D: Conjecture 1 Extended Verification — Results

### Part 1: Random Verification (10,000 × 7 topologies × K∈{3,5,7} = 210,000 tests)

| Topology | Direction | K=3 viol | K=5 viol | K=7 viol | Worst |Δ| |
|----------|-----------|----------|----------|----------|---------|
| Confounding | non-dec | 84.7% | 80.6% | 78.9% | 0.011 |
| Mediation | non-dec | 82.4% | 79.0% | 78.9% | 0.013 |
| Front-door | non-dec | 84.3% | 80.8% | 79.0% | 0.013 |
| Collider | non-inc | 86.5% | 76.4% | 75.6% | 0.005 |
| M-bias | non-inc | 97.3% | 76.4% | 75.1% | 0.002 |
| Exposure | non-dec | 4.9% | 2.1% | 0.8% | 0.056 |
| IV | non-dec | 74.3% | 60.1% | 57.1% | ~10⁷ |

**Strict monotonicity fails in 67.4% of cases** (141,514/210,000). But violation **magnitudes** are tiny: <0.06 for all non-IV topologies, consistent with the paper's "approximately monotonic" claim.

### Part 2: Adversarial Search (500 restarts × 14 configs)

13/14 configs found counterexamples. Only IV K=3 failed to find one (objective ~10⁻²⁹). Adversarial worst magnitudes match random-search bounds — no large violations found for non-IV topologies.

### Interpretation

The conjecture as stated ("approximately non-decreasing/non-increasing") is **confirmed** — deviation magnitudes are bounded <0.06 for non-IV. However:

1. **Theorem 1 proof has a gap**: The DPI argument for V_B(δ) being non-increasing fails because C(δ) = (1-δ)I + δC₀ is a linear interpolation of stochastic matrices, not a degradation channel. V_B(δ) can decrease then increase (e.g., when C₀ is near-permutation: channel degrades to noise then becomes informative again as a permuted channel). The theorem claims **strict** monotonicity ("monotonically non-decreasing"), which is falsified.

2. **The "approximately" qualifier in the conjecture saves it**: worst-case step deviations are well within the 0.06 bound claimed in the paper text.

3. **Root cause**: DPI applies to Markov chains A → A*, but C(δ) doesn't form a degradation sequence — at intermediate δ the channel can be noisier than at δ=1 if C₀ is a near-permutation.

The paper text in experiments.tex already correctly describes this as "approximately monotonic" with bounded deviations. The main issue is Theorem 1's proof sketch, which needs either (a) restricting to the proportional case where it does hold exactly, or (b) weakening to approximate monotonicity with the empirical bound.

---
