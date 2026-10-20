# Full Re-Audit Change Summary

**Date**: 2026-05-15
**Scope**: All 9 .tex files + writing_plan.yaml

---

## Files Modified

### method.tex
- **Table 1 OH column**: cmd_rep 92.2→5.4, file_diff 42.1→17.8, outcome_bp 19.8→16.8
- **Line 44**: "92.2% of OH windows; elevated rate reflects..." → "5.4% of OH windows; lower rate reflects OH's greater action diversity" + added precision/recall/temporal dynamics
- **Line 49**: "87% correctness on progress windows" → "87.5% recall on stagnation windows (precision 99.9%)" (fixed metric semantics)
- **Table 1 caption**: Added "fire rate" definition and note about corrected embeddings

### experiments.tex
- **Table 2**: GB Conf≥2 0.9919→0.9984 (now bold, RF underlined)
- **Dataset table**: OH stag rate 21.4→21.45
- **§5.2 line 92**: Fixed gap comparison to use conf≥2 (0.998 vs 0.976 = 2.2pp)
- **§5.4 cross-agent reversal**: Removed "pathology" framing, replaced with corrected fire rate/precision stats

### analysis.tex
- **Line 12**: cmd_rep fire rate 92.2%→5.4%

### appendix.tex
- **§A.4 complete rewrite**: Old two-subtable cmd_rep ablation (3-LF vs 2-LF with +17.6pp) replaced with:
  - Few-shot transfer table (ZS 0.598 → 5% 0.850 → 100% 0.976)
  - Prevalence-matched ablation narrative (-29.4pp, coverage not noise)

### writing_plan.yaml
- **core_claim**: "fundamentally structural" → "zero-shot transfer dominance", removed 0.751
- **abstract bullet**: "+17.6pp" → label quality + coverage narrative
- **intro hook**: 90%/80% → 77%/75.5% (SlopCodeBench)
- **intro insight**: "fundamentally structural" → "zero-shot transfer dominance"
- **experiments setup**: 20.9% → 21.45%
- **§5.2 bullet**: 0.528/0.751 → 0.598/0.968/0.976
- **§5.5 bullet**: 92.3%/71% → 5.39%/97.91%/-29.4pp
- **tab_oh_cmdrep caption**: Updated to prevalence-matched framing

### abstract.tex, introduction.tex, conclusion.tex
- Already updated in prior revision (D050/D051). Verified correct — no changes needed.

---

## Verification: No Residual Old Values in docs/paper/sections/

| Pattern | Result |
|---------|--------|
| `17.6` (in claim context) | Clean — only in artifacts/ history |
| `71%` (FP rate context) | Clean |
| `92.2` / `92.3` | Only as "previously reported" historical reference in experiments.tex |
| `6.6%` (OH stag rate) | Clean — only as "correcting from 6.56% to 21.45%" |
| `0.751` | Only as "previously 0.751 under corrupted labels" |
| `0.528` / `0.530` | Clean |
| `21.6` (gap context) | Clean |
| `fundamentally structural` | Clean |
| `90%` / `80%` (SlopCodeBench) | Clean |
| `0.9919` (old GB conf≥2) | Clean |
| `adversarial` | Clean |

---

## Key Narrative Changes

1. **"fundamentally structural" → "zero-shot transfer dominance"**: Structural features dominate in zero-data regime (+36.9pp), but probe closes gap with FT (2.2pp at 100%)
2. **cmd_rep: "noise source" → "coverage provider"**: High precision (97.9%), low fire rate (5.4% on OH), value is expanding training data 10x
3. **Cross-agent gap: 21.6pp → 2.21pp**: Old comparison invalid (stale labels). New: GB conf≥2 0.998 vs probe FT 0.976
4. **Transfer bottleneck: LF noise → label quality**: Embedding version mismatch was root cause, not cmd_rep being "adversarial"
