# code t2 1 deff parametric curve

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_t2_1_deff_parametric_curve_20260523T030002_result.json`
- **Structured JSON:** [`bcfef275321f7a90d3de.json`](../../sessions/bc/bcfef275321f7a90d3de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure is clean. All outputs saved to `artifacts/deff_parametric_curve/`:

| File | Description |
|------|-------------|
| `deff_parametric_curve.pdf/png` | Two-panel figure: (a) ICC vs family size, (b) Adj. C% vs family size |
| `family_icc_data.csv` | 30 families with (family, size, ICC, DEFF, adj_c_pct) |
| `fit_results.csv` | Log-linear and power-law fit parameters + R² |
| `deff_curve_report.md` | Summary with continuous DEFF lookup table |

Key results:
- **Best fit**: power-law ICC = 0.550 × m^(-0.060), **R² = 0.026** — ICC is essentially flat (~0.46) across family sizes, confirming R18
- Both models have negligible R², meaning DEFF scales linearly with m (not modulated by ICC variation)
- Small families (m < 10) show high ICC variance: near-clone pairs (wizardlm-2: 0.99) vs. dissimilar ones (olmo: 0.12)
- At m = 63 (simple m̄): DEFF ≈ 28, Adj. C% ≈ 1.1%

---
