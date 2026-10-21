## Complete Diagnostic Cascade Table v2 — CORRECTED (2026-05-22)

All finetuned, N=8, seed=42.

### Bugs Fixed in RE Data
1. Wrong data source: used weak model output (greedy F1=0.07) → correct: exp_012_rerun_1024 (greedy F1=0.40)
2. Wrong matching: text-based → span-based
3. Wrong zero-F1 def: "all 8 samples F1=0" → "greedy F1=0"

### Corrected Table

| Task | Dataset | Degen% | LP-F1 ρ (pooled) | MV Δ(pp) | LP-best Δ(pp) | Zero-F1% | Oracle Δ(pp) |
|------|---------|--------|-------------------|----------|---------------|----------|-------------|
| NER | FewNERD | 8.8 | 0.674 | −2.74 | — | 5.4 | — |
| NER | SciERC | 13.4 | 0.312 | −1.24 | −0.32 | 4.7 | +11.57 |
| NER | CoNLL | 56.7 | 0.411 | +0.20 | −1.62 | 2.7 | +4.15 |
| RE | SciERC | 10.1 | 0.350 | −5.90 | −0.94 | 40.1 | +18.08 |

### Key Insight
RE has the worst MV Δ (-5.90pp) despite moderate degeneracy (10.1%) —
the driver is the 40% zero-F1 rate creating noise that MV amplifies.
Oracle headroom (+18.08pp) is massive, confirming the selection gap is real.