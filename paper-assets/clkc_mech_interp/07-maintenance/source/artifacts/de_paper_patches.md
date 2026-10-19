# DE Bootstrap Results — Paper Patch Templates

Reference data:
- EN-ZH: Δ = +7.27pp [0.37, 13.97], p = 0.038 (Llama-3.1, n=2000)
- EN-DE token overlap: 14.77% (vs EN-ZH: 3.4%)

---

## Scenario A: DE Δ ≈ 0, not significant

**Use when**: `p_value >= 0.05`
**Position**: Discussion / Confound Analysis (near Table 2)

> To further investigate whether token-level overlap drives the observed asymmetry, we replicate our probing protocol on English–German knowledge conflicts, where per-sample Jaccard token overlap (14.77\%) is more than four times that of English–Chinese (3.4\%). Despite this substantially higher lexical similarity, the German transfer asymmetry is {delta_de}pp (95\% CI [{ci_lower}, {ci_upper}], $p={p_value}$), far smaller than the Chinese result (+7.3pp, $p=0.038$) and not statistically significant. This dissociation—higher token overlap yet no significant asymmetry—provides direct evidence that surface-level lexical sharing is not the mechanism underlying the ZH→EN advantage observed in §\ref{sec:results}.

---

## Scenario B: DE Δ > 0, significant

**Use when**: `p_value < 0.05`
**Position**: Results section (after Table 1 or as a standalone paragraph)

> We extend the cross-lingual probing analysis to a second language pair, English–German, to test whether the L2→L1 advantage generalizes beyond typologically distant languages. On Llama-3.1 with German knowledge conflicts, the asymmetry is {delta_de}pp (95\% CI [{ci_lower}, {ci_upper}], $p={p_value}$), replicating the direction and significance of the Chinese result (+7.3pp, $p=0.038$). Notably, this occurs despite a much higher token overlap between English and German (14.77\% vs.\ 3.4\%), suggesting that the asymmetry reflects a structural property of multilingual knowledge encoding rather than a confound of lexical similarity.
