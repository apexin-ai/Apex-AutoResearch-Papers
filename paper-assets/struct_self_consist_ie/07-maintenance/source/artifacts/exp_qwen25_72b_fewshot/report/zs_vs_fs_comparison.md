# ZS vs FS Complete Comparison — Qwen2.5-72B-Instruct-AWQ

## Full Results Table

| Dataset  | Regime | N     | Degen% | LP ρ   | SJ ρ  | FK ρ  | VC ρ  | EM ρ  | Greedy F1 | Oracle F1 | LP-wt F1 | Δ (pp)  | p       |
|----------|--------|-------|--------|--------|-------|-------|-------|-------|-----------|-----------|----------|---------|---------|
| SciERC   | ZS     | 529   | 21.0%  | 0.081  | 0.217 | 0.227 | 0.277 | 0.181 | 0.399     | 0.549     | 0.415    | +1.53   | 0.008** |
| SciERC   | FS     | 529   | 16.6%  | 0.060  | 0.293 | 0.301 | 0.258 | 0.205 | 0.461     | 0.604     | 0.461    | -0.08   | 0.544   |
| CoNLL    | ZS     | 2756  | 67.7%  | -0.002 | 0.304 | 0.302 | 0.297 | 0.281 | 0.712     | 0.765     | 0.708    | -0.37   | —       |
| CoNLL    | FS     | 2756  | 70.0%  | 0.106  | 0.442 | 0.451 | 0.426 | 0.403 | 0.745     | 0.796     | 0.745    | +0.03   | 0.417   |
| FewNERD  | ZS     | 32565 | 46.2%  | 0.119  | 0.345 | 0.321 | 0.416 | 0.303 | 0.628     | 0.707     | 0.626    | -0.20   | —       |
| FewNERD  | FS     | 32565 | 45.2%  | 0.161  | 0.345 | 0.327 | 0.410 | 0.302 | 0.619     | 0.702     | 0.619    | +0.02   | 0.401   |

## FewNERD FS Bootstrap Details
- Observed diff: +0.000154 (+0.02pp)
- 95% CI: [-0.0011, +0.0014]
- p-value: 0.4005 (n.s.)
- Cohen's d: 0.0014 (negligible)
- Instance breakdown: 8.5% positive / 7.3% negative / 84.3% tied
- Non-degenerate subset: Δ=+0.02pp, p=0.4009 (also n.s.)

## Signal Quality ZS→FS Trends
| Signal | SciERC      | CoNLL             | FewNERD        |
|--------|-------------|-------------------|----------------|
| LP ρ   | 0.081→0.060 ↓ | -0.002→0.106 ↑↑ | 0.119→0.161 ↑ |
| SJ ρ   | 0.217→0.293 ↑ | 0.304→0.442 ↑↑  | 0.345→0.345 = |
| FK ρ   | 0.227→0.301 ↑ | 0.302→0.451 ↑↑  | 0.321→0.327 ↑ |
| VC ρ   | 0.277→0.258 ↓ | 0.297→0.426 ↑↑  | 0.416→0.410 ↓ |

## Dual-Gating Hypothesis Verdict

**NEGATIVE.** FewNERD FS provides the strongest test case: LP ρ=0.161 (highest across all 6 conditions) + degen=45.2% (moderate). Both gates nominally satisfied, yet construction Δ=+0.02pp (n.s., p=0.401).

LP-weighted construction succeeded only in SciERC ZS (+1.53pp, p=0.008). In all other 5 conditions, the effect is indistinguishable from zero. Dual-gating is necessary but insufficient — LP signal magnitude (~0.16 max) appears too weak for reliable per-instance sample discrimination.
