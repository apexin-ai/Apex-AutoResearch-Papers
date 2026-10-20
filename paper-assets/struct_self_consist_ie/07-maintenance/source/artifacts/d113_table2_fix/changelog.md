# D113 Table 2 Fix Changelog

## Summary
Fixed Table 2 "Single" row mislabeling and Greedy F1 metric confusion. The old Greedy value (0.663) was micro F1 incorrectly placed in a macro F1 table; the "Single" row (0.645) was actually the correct greedy macro F1. All "greedy surpasses selection" claims replaced with "selection approximately matches greedy" framing.

## Files Modified

### experiments.tex
- **Table 2 caption**: Changed `$p$ vs. single-sample` → `$p$ vs. greedy baseline`; removed Single footnote; updated Random description to note `= expected F1 of a single T=1.0 draw`
- **Table 2 Greedy row**: `$0.663$` → `$0.645 \pm 0.001$`
- **Table 2 Single row**: Deleted entirely (was redundant with corrected Greedy)
- **Line ~84**: `none improves over single-sample` �� `none improves over the greedy baseline`
- **Line ~87**: `\paragraph{No significant improvement over single-sample.}` → `\paragraph{No significant improvement over greedy.}`
- **Line ~88**: `headroom above single-sample (0.645)` → `headroom above greedy (0.645)`
- **Line ~92-93**: Replaced "Greedy achieves F1=0.663, surpassing all N=8 selection strategies" with "LP approximately matches greedy decoding (T=0; Δ=+0.2pp, not significant); neither significantly outperforms the other, yet both fall far short of the oracle (0.778, 13.3pp gap)"

### introduction.tex
- **Line ~11**: `selection fails to improve over greedy decoding` → `selection approximately matches greedy decoding ($T{=}0$) without significant improvement despite 13--18pp oracle headroom`
- **Line ~17 (figure caption)**: `fail to outperform greedy decoding` → `approximately match greedy decoding ($T{=}0$) without significant improvement`
- **Line ~35 (C3 contribution)**: Replaced "Greedy decoding (T=0, F1=0.663) surpasses all N=8 selection strategies" with "Selection recovers T=1.0 sampling degradation (F1≈0.645--0.647, matching greedy) but fails to close the 13.3pp oracle gap"

### discussion.tex
- **Line ~16**: Replaced "achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies" with "LP selection approximately matches greedy decoding (T=0; Δ=+0.2pp, p=0.29); both fall far short of the oracle (0.778, 13.3pp gap)---multi-sample selection adds cost without closing the gap"
- **Line ~43**: `fail to improve over single-sample (best: +0.1pp)` → `fail to improve over greedy (best: +0.2pp)`

### abstract.tex
- **Line ~4**: `selection fails to outperform greedy decoding` → `selection approximately matches greedy decoding ($T{=}0$) without significant improvement`

### conclusion.tex
- **Line ~3**: `selection that fails to outperform greedy decoding` → `selection that approximately matches greedy decoding ($T{=}0$) without significantly outperforming it`

### limitations.tex
- **Line ~10**: `+0.4pp over greedy` → `+0.1pp over greedy` (corrected: combo best is +0.1pp over greedy 0.645)

## Key Numeric Changes
| Metric | Old (wrong) | New (correct) | Source |
|--------|-------------|---------------|--------|
| Greedy macro F1 | 0.663 (was micro) | 0.645 ± 0.001 | Registry |
| Single row | 0.645 (mislabeled) | Deleted (= Greedy) | --- |
| LP vs Greedy Δ | -1.6pp (LP "fails") | +0.2pp (approximately matches) | 0.647 - 0.645 |
| Combo vs Greedy | +0.4pp | +0.1pp | Discussion §Signal combinations |

## Framing Change
- **Old**: "Greedy surpasses all selection methods" (wrong because 0.663 was micro, not macro)
- **New**: "Selection approximately matches greedy; neither significantly outperforms the other" (correct: LP 0.647 vs Greedy 0.645, p=0.29)
