# paper writing results

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_results_20260516T051606_result.json`
- **Structured JSON:** [`e1004db3d62f50276333.json`](../../sessions/e1/e1004db3d62f50276333.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results section written. Four subsections covering all three claims:

- **§5.1 Main Results**: Table 1 with 3-seed data. Adaptive captures 89.6% of grid-best improvement within seed variance. ESS-only worse than uniform on all seeds. Golden Ratio (oracle) matched without known ρ.
- **§5.2 Contamination Level Robustness**: ρ=0.6 single-seed results. ESS-only collapses to within 0.004 of uniform; adaptive still improves by 0.026.
- **§5.3 Hyperparameter Sensitivity**: τ sweep table (safe range [0.5, 0.8]) and n_min ablation (n_min=2 stable default). Both proportion-free.
- **§5.4 Constraint Regime Analysis**: 49.9%/20.2%/30.0% regime breakdown. Minimum intervention principle. Context for small absolute PPL differences in a highly optimized regime.

All numbers sourced exclusively from the provided registry data. Single-seed results marked explicitly. No "significantly" without test, no "state-of-the-art", no "consistently outperforms".

---
