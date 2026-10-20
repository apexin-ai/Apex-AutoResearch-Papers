# α=0.25 fp32 3-Seed Onset Verification Summary

## 3-Seed Consistency Table

| Metric          | s42      | s43      | s44      | Mean     | Std    |
|-----------------|----------|----------|----------|----------|--------|
| PermG_fwd       | 0/8      | 0/8      | 0/8      | 0/8      | —      |
| PermG_rev       | 0/8      | 0/8      | 0/8      | 0/8      | —      |
| K≥4             | 0/8      | 0/8      | 0/8      | 0/8      | —      |
| MMCT            | 0        | 0        | 0        | 0        | —      |
| d1_drift (%)    | -39.15   | -38.95   | -38.35   | -38.82   | 0.34   |
| d2_drift (%)    | —        | -53.35   | —        | —        | —      |
| d3_drift (%)    | —        | -54.80   | —        | —        | —      |
| entropy_drift   | —        | -4.94    | —        | —        | —      |
| ppl_drift       | —        | -18.38   | —        | —        | —      |
| ece_drift       | —        | +64.77   | —        | —        | —      |
| mauve_drift     | —        | -35.59   | —        | —        | —      |

## Conclusion

**α=0.25 is in the blind zone.** 3/3 seeds unanimously show:
- PermG=0/8 (no Granger causality in either direction)
- K≥4=0/8 (no consensus lead-lag signal)
- MMCT=0 (no multi-metric detection)
- d1_drift tightly clustered: mean=-38.82%, σ=0.34% (very stable across seeds)

Note: TY Granger shows 6/8 sig for s43, but per C003 constraint, TY at α≤0.50 is unreliable due to seed instability in d_max estimation with T=11 time points.

The diversity metrics (d1/d2/d3) still degrade substantially (~39-55%), confirming that model collapse drift occurs at α=0.25, but the canary metrics (entropy, ECE) do NOT lead the downstream metrics — no detectable early warning signal exists at this contamination level.

Onset boundary: α=0.25 confirmed below detection threshold. Combined with prior results showing onset at higher α values, this narrows the blind zone upper bound.