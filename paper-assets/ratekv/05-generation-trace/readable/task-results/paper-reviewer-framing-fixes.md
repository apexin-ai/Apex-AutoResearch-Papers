# paper reviewer framing fixes

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reviewer_framing_fixes_20260516T073046_result.json`
- **Structured JSON:** [`75cddbc176875215c1d0.json`](../../sessions/75/75cddbc176875215c1d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications pass:

1. **Yi 8K description** (experiments.tex:144) — now includes "+0.06 PPL" and "no benefit or slight degradation"
2. **KV head count caveat** (experiments.tex:146) — added after the long-context discussion
3. **Appendix long-context table** (appendix.tex) — removed "Yi-1.5 excluded" from caption, added Mistral-7B-v0.3 and Yi-1.5-9B rows
4. **Phi-3 concentration explanation** (analysis.tex:30) — added the sentence about concentration 0.17 and insufficient absolute magnitude
5. **"Yi-1.5 excluded"** — only remains in main.aux (stale LaTeX build cache, will be overwritten on next compile)
6. **"8/8"** — no matches found

---
