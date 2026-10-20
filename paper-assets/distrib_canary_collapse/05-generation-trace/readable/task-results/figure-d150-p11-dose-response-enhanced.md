# figure d150 p11 dose response enhanced

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_d150_p11_dose_response_enhanced_20260520T144253_result.json`
- **Structured JSON:** [`9ecedcf94f11eda01172.json`](../../sessions/9e/9ecedcf94f11eda01172.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure looks good — regime labels now above the plot, annotation arrow curves cleanly to the highlighted α=0.45 point, and the legend doesn't overlap with regime labels.

Output:
- `docs/paper/figures/fig_dose_response.pdf`
- `docs/paper/figures/fig_dose_response.png`

Generation script: `figures/paper/gen_fig_dose_response.py`

Elements added:
- **Bootstrap 95% CI band**: 1000 sigmoid draws from log-normal k ∈ [73.6, 500], normal α_c ∈ [0.425, 0.558], normal y_max ∈ [0.691, 0.895]
- **Sub-threshold annotation**: red open circle at α=0.45 with arrow and text box showing p_FDR = .059, .091
- **4 regime bands**: Blind (α < 0.35), Onset (0.35–0.50), Sync Collapse (0.50–0.65), Detection (α > 0.65) with labels above the plot
- Individual seed scatter (gray) + mean ± SD diamonds (black) + locked sigmoid fit (blue, α_c = 0.476)

---
