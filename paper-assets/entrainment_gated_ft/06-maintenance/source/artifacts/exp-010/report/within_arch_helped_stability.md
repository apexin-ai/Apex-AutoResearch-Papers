## Within-Architecture Helped/Hurt Stability Analysis

### Core Finding
Within-architecture Jaccard ≈ 0.31–0.35, significantly higher than cross-architecture ~0.10, but still far below 1.0.

| Architecture | Mean helped J | Mean hurt J | Notes |
|---|---|---|---|
| GatedDeltaNet | 0.338 | 0.319 | Most uniform across ratios |
| RetNet | 0.333 | 0.321 | Similar to GDN |
| HGRN2 | 0.373 | 0.291 | Highest helped, lowest hurt |

### Key Observations
- **Within-arch J (~0.33) >> Cross-arch J (~0.10)**: 3x higher overlap within same architecture, but still ~65% examples are ratio-specific
- **Adjacent ratios don't have higher overlap**: h24-1 vs h12-1 J ≈ h24-1 vs h3-1 J (e.g., GDN helped: 0.345 vs 0.311) — helped/hurt sets don't change monotonically with attention amount
- **HGRN2 asymmetry**: helped set most stable (J ≈ 0.37) but hurt set least stable (J ≈ 0.29) — attention consistently helps the same HGRN2 examples but hurts different ones depending on ratio

### Implications for Paper
- Supports Claim 3 (architecture-specific per-example effects): architecture identity matters more than attention ratio for determining which examples benefit
- Strengthens decoupling narrative: even within one architecture, the per-example effect is largely ratio-specific
