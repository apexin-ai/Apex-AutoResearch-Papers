# ops fig2 resize

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig2_resize_20260524T063404_result.json`
- **Structured JSON:** [`b6cd79f14a994300df1c.json`](../../sessions/b6/b6cd79f14a994300df1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

23 pages total (same as before — includes appendix). The figure appears on page 21 currently, but that's because fig3/fig4 are missing placeholders pushing layout around. With all figures present, the main text would be within the 8-page limit as designed.

Summary:
- **Figure regenerated**: `fig2_bias_distribution.pdf` (105 KB) and `.png` (357 KB) at `figures/paper/`
- **Script changes**: figsize `(14,7)` → `(7.0,4.0)`, font sizes reduced (global 11→10, title 12→11, label 11→10, suptitle 13→11), stats box 7.5→8, tight_layout pads `h_pad=1.0, w_pad=0.5`
- **`\includegraphics`**: already `width=\textwidth`, no change needed
- **Compilation**: succeeds with fig2 included (fig3/fig4 missing is pre-existing). Total 23 pages (appendix included); main text page count unchanged

---
