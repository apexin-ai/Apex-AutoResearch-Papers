# code mmct implementation v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mmct_implementation_v2_20260518T153850_result.json`
- **Structured JSON:** [`11f1b9226f36bd449c13.json`](../../sessions/11/11f1b9226f36bd449c13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files created and validated. Summary of results:

**Files created on remote server** (`/root/autodl-tmp/distrib_canary_collapse/`):

| File | Purpose |
|------|---------|
| `mmct/__init__.py` | Package init |
| `mmct/methods.py` | Wrapper for 5method_leadlag.json (handles both JSON formats) |
| `mmct/null_distribution.py` | Null distribution from α=0.00, per-method FPR, vectorized bootstrap |
| `mmct/consensus_test.py` | MMCT class with weighted/bidirectional params |
| `mmct/run_mmct.py` | Full sweep runner, generates 4 output files |
| `artifacts/mmct_results/mmct_results.json` | Full results (332KB) |
| `artifacts/mmct_results/null_distribution.json` | Null distribution + FPR profiles |
| `artifacts/mmct_results/mmct_report.md` | Per-condition tables |
| `artifacts/mmct_results/fpr_fnr_comparison.md` | 4-way tradeoff comparison |

**Key findings:**

| Mode | FPR (α=0.00) | Det. α=0.25 | Det. α=0.50 | Det. α=0.75 |
|------|-------------|-------------|-------------|-------------|
| uniform_forward | **0.000** | 0.000 | 0.000 | 0.333 |
| uniform_bidirectional | **0.000** | 0.000 | 0.000 | 0.333 |
| weighted_forward | **0.000** | 0.438 | 0.542 | **0.875** |
| weighted_bidirectional | **0.000** | 0.125 | 0.167 | 0.375 |

- All 4 modes achieve perfect Type I error control (0/24 FP at α=0.00)
- **Weighted forward** is the best power mode: 87.5% detection at α=0.75 while maintaining FPR=0
- naive_xcorr has 95.8% FPR on null data, confirming the paper's core finding that single methods are unreliable
- Weighted consensus dramatically improves power by up-weighting low-FPR methods (threshold_onset, perm_granger get 100x weight vs naive_xcorr at 1x)
- Bidirectional filter is conservative, reducing detection rate because some reverse correlations also appear significant
- No α=1.0 data was available; α=0.25 only has 2 seeds (s43, s44)

---
