# Lead-Lag Analysis: GPT-2 Medium (α=1.0, seed=42)

**Experiment:** gen_wiki_gpt2m_a100_s42_v3  
**Model:** GPT-2 Medium, WikiText-103, α=1.0, T=10 generations, batch_size=32, 5000 steps/gen  
**Method:** Cross-correlation (lag 0–5) + Permutation Granger (5000 perms, BH FDR q=0.05, max_lag=1, first-differenced)

---

## Gen 0 / Gen 10 Metrics

| Metric | Gen 0 | Gen 10 | Drift % |
|--------|-------|--------|---------|
| token_entropy | 3.5714 | 0.4822 | −86.50% |
| ece | 0.0112 | 0.5185 | +4543.4% |
| perplexity | 32.6315 | 14616.60 | +44703% |
| distinct_1 | 0.1044 | 0.0914 | −12.41% |
| distinct_2 | 0.5483 | 0.4675 | −14.73% |
| distinct_3 | 0.8441 | 0.7368 | −12.72% |

---

## Window A: Full (gen 0–10, T=11)

### Forward: Canary → Diversity

| Pair | xcorr |r| | best lag | Granger F | p_raw | p_fdr | sig | f² | df_resid |
|------|-----------|----------|-----------|-------|-------|-----|------|----------|
| entropy→d1 | 0.9948 | 1 | 1271.33 | 0.0018 | 0.0030 | * | 211.89 | 6 |
| entropy→d2 | 0.9929 | 2 | 299.43 | 0.0022 | 0.0030 | * | 49.90 | 6 |
| entropy→d3 | 0.9893 | 2 | 141.46 | 0.0030 | 0.0030 | * | 23.58 | 6 |
| ece→d1 | 0.9920 | 1 | 436.55 | 0.0014 | 0.0030 | * | 72.76 | 6 |
| ece→d2 | 0.9961 | 1 | 142.20 | 0.0024 | 0.0030 | * | 23.70 | 6 |
| ece→d3 | 0.9947 | 1 | 90.47 | 0.0028 | 0.0030 | * | 15.08 | 6 |

**6/6 pairs significant** after FDR correction. All f² > 15 (huge effect sizes).  
Entropy leads diversity at lag 1–2; ECE leads at lag 1.

### Reverse: Diversity → Canary

| Pair | xcorr |r| | best lag | Granger F | p_raw | p_fdr | sig | f² | df_resid |
|------|-----------|----------|-----------|-------|-------|-----|------|----------|
| d1→entropy | 0.9484 | 3 | 7.04 | 0.1102 | 0.1156 | | 1.17 | 6 |
| d2→entropy | 0.9456 | 3 | 4.75 | 0.1156 | 0.1156 | | 0.79 | 6 |
| d3→entropy | 0.9448 | 3 | 4.95 | 0.1154 | 0.1156 | | 0.82 | 6 |
| d1→ece | 0.9467 | 0 | 45.80 | 0.0176 | 0.0352 | * | 7.63 | 6 |
| d2→ece | 0.9355 | 0 | 29.33 | 0.0098 | 0.0294 | * | 4.89 | 6 |
| d3→ece | 0.9356 | 0 | 31.74 | 0.0078 | 0.0294 | * | 5.29 | 6 |

**3/6 pairs significant** (diversity→ece only). diversity→entropy: 0/3 significant.  
Reverse ECE effects are weaker (f² = 5–8 vs forward f² = 15–212).

### Directionality Summary (Full Window)

| Direction | Significant / Total | Mean f² |
|-----------|-------------------|---------|
| Forward (canary→diversity) | **6/6** | 66.15 |
| Reverse (diversity→canary) | 3/6 | 3.45 (all 6) |

**Clear asymmetry:** canary metrics Granger-cause diversity, not vice versa.  
The 3 significant reverse pairs (diversity→ece) have ~10× smaller effect sizes than forward.

---

## Window B: Sub-window (gen 0–5, T=6)

### Forward: Canary → Diversity

| Pair | xcorr |r| | best lag | Granger F | p_raw | p_fdr | sig | f² | df_resid |
|------|-----------|----------|-----------|-------|-------|-----|------|----------|
| entropy→d1 | 0.9986 | 2 | 427.70 | 0.0560 | 0.1232 | | 427.70 | 1 |
| entropy→d2 | 0.9960 | 2 | 29.27 | 0.0958 | 0.1341 | | 29.27 | 1 |
| entropy→d3 | 0.9915 | 2 | 11.15 | 0.1912 | 0.1912 | | 11.15 | 1 |
| ece→d1 | 0.9952 | 1 | 54.24 | 0.0616 | 0.1232 | | 54.24 | 1 |
| ece→d2 | 0.9978 | 1 | 15.57 | 0.0532 | 0.1232 | | 15.57 | 1 |
| ece→d3 | 0.9963 | 1 | 9.71 | 0.1118 | 0.1341 | | 9.71 | 1 |

**0/6 significant.** df_resid = 1 — near-zero statistical power after first-differencing a T=6 series.  
Cross-correlations remain extremely high (>0.99), indicating the pattern exists but Granger cannot detect it.

### Reverse: Diversity → Canary

| Pair | xcorr |r| | best lag | Granger F | p_raw | p_fdr | sig | f² | df_resid |
|------|-----------|----------|-----------|-------|-------|-----|------|----------|
| d1→entropy | 0.8368 | 0 | 20.52 | 0.1018 | 0.1018 | | 20.52 | 1 |
| d2→entropy | 0.8195 | 2 | 33.64 | 0.0526 | 0.0789 | | 33.64 | 1 |
| d3→entropy | 0.8202 | 2 | 190.66 | 0.0088 | 0.0264 | * | 190.66 | 1 |
| d1→ece | 0.9260 | 0 | 21.97 | 0.0966 | 0.1018 | | 21.97 | 1 |
| d2→ece | 0.9107 | 0 | 40.13 | 0.0272 | 0.0544 | | 40.13 | 1 |
| d3→ece | 0.9107 | 0 | 181.67 | 0.0088 | 0.0264 | * | 181.67 | 1 |

**2/6 significant** (d3→entropy, d3→ece). With df_resid=1, these results are unreliable.

### Sub-window Summary

The sub-window confirms the Reviewer's concern: **Granger tests have near-zero power at T=6 (df_resid=1).** Forward cross-correlations (|r|>0.99) are actually stronger than the full window, suggesting the canary→diversity coupling is tightest in the early collapse phase (gen 0–5). The Granger test simply cannot confirm this with so few time points.

---

## Full vs Sub-window Comparison

| Aspect | Full (T=11) | Sub (T=6) |
|--------|-------------|-----------|
| Forward sig (FDR) | **6/6** | 0/6 |
| Reverse sig (FDR) | 3/6 | 2/6 |
| df_resid | 6 | 1 |
| Forward xcorr mean |r| | 0.9933 | 0.9959 |
| Granger power | Adequate | Near-zero |

---

## Conclusions

1. **GPT-2 Medium replicates Pythia's lead-lag pattern.** In the full window, all 6 forward pairs (canary→diversity) are significant with huge effect sizes (f²=15–212). The canary metrics (entropy, ECE) reliably lead diversity decline by 1–2 generations.

2. **Directionality is clear.** Forward effects (mean f²=66.15) are ~19× stronger than reverse (mean f²=3.45). Only diversity→ece shows marginal reverse significance, and at much weaker effect sizes.

3. **Sub-window power collapse confirmed.** At T=6 with first-differencing, df_resid=1 renders Granger tests uninformative. Cross-correlations (|r|>0.99) remain very strong, suggesting the signal exists but the test lacks power. This supports reporting cross-correlation as the primary evidence for short windows, with Granger as supplementary for T≥11.

4. **Diversity plateau visible from gen 5 onward.** distinct_1/d2/d3 flatten after gen 5 (d1: 0.0915→0.0914, d2: 0.4675→0.4675, d3: 0.7366→0.7368), confirming the Reviewer's hypothesis. The coupling is strongest in the early collapse phase.

5. **Cross-architecture consistency.** The entropy-leads-diversity pattern and the Granger power limitation at short T are consistent across Pythia-410M and GPT-2-medium, supporting the paper's generalization claims.
