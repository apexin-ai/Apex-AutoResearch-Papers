# code sign reversal fix tau003

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sign-reversal-fix-tau003_20260523T151911_result.json`
- **Structured JSON:** [`642968739b04e27fae85.json`](../../sessions/64/642968739b04e27fae85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Key results:

**τ(0)=0.03 Sign-Reversal Analysis:**

| Metric | Value |
|---|---|
| Z=0 sign reversals | **163/1092 (14.9%)** |
| Most extreme global CATE | **-0.0593** (true = +0.03, naive = +0.0425) |
| Critical τ threshold | τ(0) < **0.0893** for sign reversal to occur |
| EC-HTE correct sign | **100%** of cases |

**τ(0) Sweep:**

| τ(0) | Reversal rate (Z=0) | Most extreme global CATE |
|---|---|---|
| 0.01 | **31.0%** | -0.079 |
| 0.03 | **14.9%** | -0.059 |
| 0.05 | **6.1%** | -0.039 |
| 0.10 | 0% | — |

**Outputs:**
- `artifacts/sign_reversal_figure.pdf` + `.png` — 3-panel figure (scatter, bar chart, τ sweep)
- `artifacts/sign_reversal_corrected.csv` — full data with CATE estimates
- `artifacts/sign_reversal_tau_sweep.csv` — sweep results

The corrected analysis now shows **genuine sign reversals**: the global-corrected CATE estimate flips from positive (+0.0425 naive) to negative (-0.0593), meaning global correction would lead a researcher to conclude the treatment is harmful when it's actually beneficial. EC-HTE preserves the correct sign in all cases.

---
