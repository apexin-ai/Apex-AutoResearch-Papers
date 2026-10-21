# paper mistral 50pct multiseed and appendix

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_mistral-50pct-multiseed-and-appendix_20260524T110903_result.json`
- **Structured JSON:** [`9aa12c0d92e27d17a747.json`](../../sessions/9a/9aa12c0d92e27d17a747.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Changes committed. Summary:

1. **Table 1**: Mistral 50% updated from `$-3.50$ [$-9.4$, $-2.1$]` → `$-4.09$ ($\pm$0.53)`
2. **Table 3 (degradation)**: Mistral lz* 50% updated from `$3.50$ [$2.1$, $9.4$]` → `$4.09$ ($\pm$0.53)`
3. **Prose** (line 10): `Mistral ($|d|{=}3.37$/$3.50$)` → `Mistral ($|d|{=}3.37$/$4.09$)`
4. **Appendix**: Added `tab:mistral_multiseed` with per-seed d values for 5% (n=2), 15% (n=3), 50% (n=3)

Computed values from server data:
- 50% seeds: s1=-3.50, s2=-4.25 (lz*=-4.695), s3=-4.51 (lz*=-5.236) → mean=-4.09, SD=0.53
- 5% also included (n=2): s1=-2.82, s2=-4.83 → mean=-3.83, SD=1.42

Note: The heatmap figure (`fig_heatmap.pdf`) still shows the old 3.50 value. If you want it regenerated, let me know.

---
