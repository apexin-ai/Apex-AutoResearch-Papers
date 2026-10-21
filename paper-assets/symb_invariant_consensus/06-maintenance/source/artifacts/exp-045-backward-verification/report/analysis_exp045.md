# Analysis: exp-045-backward-verification

## Summary

**Conclusion: NEGATIVE.** Backward verification accuracy = 53.92%, far below SC baseline 75.00% (delta = -21.08pp). The approach catastrophically fails due to systematic True-label bias and Z3 lacking discriminative power on LLM-generated backward FOL.

## Core Metrics

| Metric | Value |
|--------|-------|
| BV accuracy | 53.92% (110/204) |
| SC baseline | 75.00% (153/204) |
| Delta | **-21.08pp** |
| Model | Qwen2.5-7B-Instruct |
| Dataset | FOLIO-204 |
| K (rounds) | 12 |
| Wall time | 1373.9s |

## Per-Label Accuracy

| Gold Label | N | BV Accuracy | Predicted as True | Predicted as False | Predicted as Unknown |
|-----------|---|------------|-------------------|-------------------|---------------------|
| True | 72 | **90.3%** | 65 | 1 | 6 |
| False | 63 | **20.6%** | 46 | 13 | 4 |
| Unknown | 69 | **46.4%** | 37 | 0 | 32 |

**Prediction distribution**: True=148, Unknown=42, False=14 (gold: True=72, False=63, Unknown=69). BV predicts "True" for 72.5% of problems vs 35.3% in gold, a massive systematic bias.

## Z3 Solver Statistics

| Metric | Supporting FOL | Contradicting FOL | Total |
|--------|---------------|-------------------|-------|
| SAT | 12,774 | 6,435 | 19,209 |
| UNSAT | 165 | 711 | 876 |
| FAIL | 40 | 31 | 71 |
| **SAT rate** | **98.4%** | **89.7%** | 95.3% |

- Overall UNSAT rate: 4.35% (876/20,156)
- Overall fail rate: 0.35% (71/20,156)
- Total Z3 checks: 20,156 across 2,448 rounds

## Score Analysis

- Gold answer has highest score in only 52.2% of rounds (near random for 3-class)
- **Score ties: 42.5%** of all rounds (1,041/2,448)
- Average score spread: 4.28
- Unanimous decisions (12/12 same answer): 92/204 (45.1%)

## Diagnosis

### Why backward verification fails

1. **Z3 has no discriminative power on LLM-generated backward FOL.** Supporting FOL is SAT 98.4% of the time; even contradicting FOL is SAT 89.7%. The LLM generates FOL expressions that are trivially satisfiable regardless of whether they truly support or contradict the candidate answer. Z3 returns SAT for nearly everything, so the score (sup_sat - con_sat) is dominated by how many FOL expressions the LLM generates, not by logical validity.

2. **True-label bias stems from the scoring mechanism.** When the LLM is asked "what premises support/contradict the conclusion being True?", it readily generates supporting FOL (easy to affirm). When asked the same for "False", it still generates expressions that Z3 satisfies, but fewer contradicting ones. The asymmetry in FOL generation volume, not logical reasoning, drives the True bias.

3. **High tie rate destroys resolution.** With 42.5% of rounds producing ties, the tiebreaking rule (likely favoring the first or most common answer) introduces additional bias rather than meaningful signal.

4. **The hypothesis that backward verification bypasses forward extraction quality is falsified.** Instead of bypassing the capability trap, BV shifts it: the LLM's backward FOL generation is just as noisy as its forward extraction, but now the noise manifests as uniformly-SAT formulas rather than incorrect constraints. The fundamental bottleneck (LLM's FOL quality) remains.

### Comparison to prior results

| Method | Accuracy | Delta vs SC |
|--------|----------|-------------|
| SC baseline (14B) | 75.49% | - |
| SICA (14B) | 75.74% | +0.25pp (n.s.) |
| Oracle gold FOL (14B) | 89.71% | +14.22pp |
| **Backward verification (7B)** | **53.92%** | **-21.08pp** |
| SC baseline (7B, this exp) | 75.00% | - |

BV is the worst-performing method tested, 21pp below its own SC baseline and 36pp below oracle.

## Key Takeaway

Backward verification does not circumvent the capability trap. The approach replaces one weak-LLM bottleneck (forward FOL extraction) with another (backward FOL generation), and the new bottleneck is actually worse because Z3 SAT/UNSAT provides almost no useful signal on the generated formulas. The direction of verification (forward vs backward) is irrelevant when the underlying FOL quality is the binding constraint.
