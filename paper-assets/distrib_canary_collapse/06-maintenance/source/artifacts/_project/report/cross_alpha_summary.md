# Cross-Alpha Comprehensive Analysis

**Date:** 2026-05-15
**Model:** EleutherAI/pythia-410m | **Data:** WikiText-103 (5k subset) | **Generations:** 10
**Alpha points:** {0.00, 0.25, 0.50, 0.75, 1.00} | **Seeds:** s42 primary + s43 multi-seed at α=0.25

---

## Table 1: Drift Summary (gen0 → gen10, % change)

| α | Seed | Token Entropy | ECE | Perplexity | Distinct-1 | Distinct-2 | Distinct-3 |
|---:|:----:|-------------:|------:|-----------:|-----------:|-----------:|-----------:|
| 0.00 | 42 | −5.1% | +51.7% | −21.7% | −13.8% | −9.8% | −4.5% |
| 0.25 | 42 | −4.1% | +79.7% | −17.2% | −40.3% | −57.1% | −59.9% |
| 0.25 | 43 | −5.0% | +98.6% | −18.7% | −40.5% | −56.4% | −58.7% |
| 0.50 | 42 | −18.6% | +842.8% | +21.1% | −37.3% | −51.5% | −52.4% |
| 0.75 | 42 | −27.7% | +1809.5% | +182.1% | −32.7% | −41.3% | −38.4% |
| 1.00 | 42-45 | −60.5% | +3762.6% | +3624.6% | −28.3% | −35.2% | −31.6% |

**Key pattern:** Calibration metrics (ECE, perplexity) degrade monotonically with α. Diversity metrics (distinct-N) show an **inverted-U**: worst collapse at α=0.25 (d3: −59.9%), attenuating toward α=1.0 (d3: −31.6%). This dissociation is a core finding.

---

## Table 2: Detectability by Alpha

| α | Perm. Granger FDR-sig (forward) | Raw p min | Consensus Robust Pairs | TY FDR-sig | Method Ablation: Naive→Robust flip rate | Qualitative |
|---:|:------:|--------:|:-------:|:------:|:------:|:--------|
| 0.00 | 0/4 | 0.051 | 0/16 | 0/8 | 100%→0% | **none** |
| 0.25 | 0/4 | 0.015 | 1/16 | 3/8† | 100%→25% | **weak** |
| 0.50 | 0/4 | 0.019 | 0/16 | 0/8 | 100%→25% | **none** |
| 0.75 | 3/4 | 0.003 | 11/16 | — | — | **strong** |
| 1.00 | 3/4 | 0.001 | 6/16 | 19/32 | 100%→75% | **moderate** |

†C001 constraint: TY results at α=0.25 are from single-seed with df_resid≈4-6; non-monotonic TY pattern (0%→62.5%→0%→59.4%) is unreliable and must not be cited in paper.

**Phase transition:** Sharp jump from 0 FDR-sig at α≤0.50 to 3/4 FDR-sig at α≥0.75. Consensus robust pairs jump from 0-1/16 to 11/16 at α=0.75.

**Method sensitivity (Claim 3):**
- Naive Pearson: 100% sig at ALL α including null control (α=0.00) — pure false positives
- After FDR-corrected permutation Granger: α=0.00 correctly drops to 0%
- Naive-vs-permutation flip rate: 50% | Naive-vs-TY flip rate: 57%
- Inter-method agreement κ = 0.185 (poor)

---

## Table 3: Cross-seed Comparison (α=0.25, s42 vs s43)

| Metric | s42 gen0 | s42 gen10 | s42 Drift% | s43 gen0 | s43 gen10 | s43 Drift% | |Δ Drift| |
|--------|--------:|--------:|---------:|--------:|--------:|---------:|--------:|
| token_entropy | 3.234 | 3.102 | −4.1% | 3.234 | 3.072 | −5.0% | 0.9 pp |
| ece | 0.0108 | 0.0194 | +79.7% | 0.0108 | 0.0215 | +98.6% | 18.9 pp |
| perplexity | 26.95 | 22.32 | −17.2% | 26.95 | 21.90 | −18.7% | 1.5 pp |
| distinct_1 | 0.0982 | 0.0586 | −40.3% | 0.0983 | 0.0585 | −40.5% | 0.2 pp |
| distinct_2 | 0.5178 | 0.2219 | −57.1% | 0.5132 | 0.2236 | −56.4% | 0.7 pp |
| distinct_3 | 0.8127 | 0.3263 | −59.9% | 0.8057 | 0.3330 | −58.7% | 1.2 pp |
| effective_rank | 46.61 | 45.30 | −2.8% | 46.61 | 45.37 | −2.7% | 0.1 pp |
| mauve | 0.0341 | 0.0163 | −52.2% | 0.0335 | 0.0187 | −44.2% | 8.0 pp |

**Verdict:** Diversity drift is highly reproducible (d1: 0.2pp, d2: 0.7pp, d3: 1.2pp difference). Calibration drift (ECE) shows larger seed variance (18.9pp) but same qualitative direction. MAUVE shows the most seed sensitivity (8.0pp), consistent with known MAUVE variance issues.

---

## Table 4: Granger Causality Detail (Permutation, FDR-corrected, forward direction)

| Direction | α=0.00 | α=0.25 | α=0.50 | α=0.75 | α=1.00 |
|-----------|-------:|-------:|-------:|-------:|-------:|
| entropy→d1 | .129 | .067 | .186 | **.054** | **.048*** |
| entropy→d2 | .179 | .172 | .186 | **.048*** | .054 |
| ECE→d1 | .974 | .409 | .076 | **.046*** | **.024*** |
| ECE→d2 | .622 | .186 | .129 | **.046*** | **.046*** |

Values are p_fdr. * = FDR-sig at q<0.05. Bold = p_fdr < 0.06.

---

## Table 5: Consensus Classification Summary (5-method agreement)

| α | Robust/16 | Threshold | Key robust pairs |
|---:|:--------:|:---------:|:-----------------|
| 0.00 | 0/16 | ≥4/5 methods | none |
| 0.25 | 1/16 | ≥4/5 methods | entropy→d1 (4/5) |
| 0.50 | 0/16 | ≥4/5 methods | none (max 3/5) |
| 0.75 | 11/16 | ≥4/5 methods | entropy→{d1,d2,d3,ppl}, ECE→{d1,d2,d3,ppl}, erank→{d1,d2,d3} |
| 1.00 | 6/16 | ≥4/5 + ≥3/4 seeds | entropy→{d1,d2,d3}, ECE→{d1,d2,d3} |

Regime-dependent pairs: 11/16 (69%). Stable pairs: 5/16 (self_bleu→all, erank→ppl).

---

## Key Findings

1. **Regime map with sharp phase transition (Claim 2):** Detectability undergoes a step-change between α=0.50 and α=0.75. At α≤0.50, zero FDR-significant Granger pairs and 0-1/16 consensus robust pairs. At α=0.75, this jumps to 3/4 FDR-sig and 11/16 consensus robust — the strongest detectability across all tested alphas, even exceeding α=1.0 (6/16 robust under the stricter 4-seed consensus threshold).

2. **Diversity-calibration dissociation:** Diversity metrics collapse hardest at low contamination (α=0.25: d2 −57.1%, d3 −59.9%) and attenuate with increasing α (α=1.0: d2 −35.2%, d3 −31.6%). Calibration metrics (ECE, perplexity) degrade monotonically with α (ECE: +51.7% → +3762.6%). This dissociation means diversity collapse alone is not a reliable indicator of contamination severity.

3. **Method choice flips >50% of conclusions (Claim 3):** Naive Pearson cross-correlation finds 100% significance at the null control (α=0.00), demonstrating spurious detection. FDR-corrected permutation Granger correctly yields 0% at α=0.00. Across all conditions, naive-vs-robust method flip rate is 50-57%, with inter-method κ=0.185 (poor agreement). The headline: a researcher choosing naive methods would conclude "early warning works everywhere", while a researcher using robust methods would conclude "early warning works only at α≥0.75."

4. **Cross-seed reproducibility confirmed at α=0.25:** Diversity drift differences between s42 and s43 are <1.2 percentage points across all distinct-N metrics. The collapse trajectory is not a single-seed artifact. ECE shows larger seed variance (18.9pp) but preserves the qualitative pattern.

5. **α=0.75 is the critical boundary, not α=1.0:** The strongest robust detectability occurs at α=0.75 (11/16 consensus pairs) rather than α=1.0 (6/16). This is because α=1.0 uses a stricter 4-seed consensus criterion, while α=0.75 uses single-seed method agreement. However, even the raw Granger p-values at α=0.75 (min 0.003) are comparable to α=1.0 (min 0.001), suggesting genuine signal emergence at this contamination level.
