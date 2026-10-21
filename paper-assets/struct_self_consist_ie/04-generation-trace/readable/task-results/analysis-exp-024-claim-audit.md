# analysis exp 024 claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_024_claim_audit_20260517T104228_result.json`
- **Structured JSON:** [`9a5b058a6aac5596288d.json`](../../sessions/9a/9a5b058a6aac5596288d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report saved to `artifacts/exp_024_claim_audit/audit_report.md`.

**Summary: 97 ✅ / 1 ❌ / 5 ⚠️**

**1 issue requiring fix:**
- **experiments.tex L52**: "EM strongest (ρ=0.360)" in the WNUT paragraph is wrong for WNUT. The ρ=0.360 comes from SciERC conditional (Figure signal_heatmap), not WNUT. On WNUT conditional, LP (0.350) > EM (0.333). Misleading cross-reference.

**5 items to review (not errors but worth noting):**
1. T ablation table shows degen=17.6% at T=1.0 vs 17.8% everywhere else (different subtask protocol)
2. LP range 0.041 (main text, NER-only) vs 0.060 (T ablation table) at T=1.0 -- larger discrepancy than subtask alone explains
3. N=8 Few-NERD LP Δ: +1.37 (paired subset n=4,351) vs +1.36 (full-set) -- minor rounding from subset
4. SciERC N=16 "+0.52 pp (p=0.003)" -- no secondary source to cross-verify
5. VC AUROC=0.706 in verifier section -- from N=16 analysis, not verifiable from QE table (N=8: 0.663)

**No old value residuals found** (58%, 21%, 10%, 11.1%→4.5%, +0.62pp all absent).

---
