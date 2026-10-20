# compute mmlu domain irt no05b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_mmlu_domain_irt_no05b_20260517T063601_result.json`
- **Structured JSON:** [`61865be8027513fe426e.json`](../../sessions/61/61865be8027513fe426e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Running confirmed. Let me record the previous J=16 results for later comparison and report what's been set up.

The run is active in tmux session `irt_no05b` on cqa1-21977. Summary:

**Setup complete:**
- Script: `/root/contamcal-irt-calibration/exp006/run_mmlu_domain_gamma_no05b.py`
- Output: `/root/autodl-tmp/exp006/mmlu_domain_irt_no05B/`
- J=13 models confirmed (8×1.5B + 5×3B, no 0.5B)
- 8 domains + 1 pooled fit, 2PL+γ, 4 chains × 1000w + 1000s
- Estimated runtime: ~45-90 min total

**Previous J=16 results (for later comparison):**

| Domain | γ_mean | 95% CI | PPP |
|--------|--------|--------|-----|
| Other | 1.3415 | [0.675, 2.029] | 0.000 |
| Business_Law | 0.6084 | [0.215, 1.004] | 0.003 |
| Humanities | 0.4729 | [0.202, 0.749] | 0.001 |
| STEM_Science | 0.3608 | [-0.057, 0.814] | 0.041 |
| STEM_CS_Eng | 0.2937 | [-0.496, 1.122] | 0.227 |
| Social_Sciences | 0.2828 | [0.028, 0.524] | 0.011 |
| Medical | 0.2655 | [-0.110, 0.645] | 0.074 |
| STEM_Math | -0.549 | [-1.266, 0.093] | 0.964 |

The run will produce `summary.json` with all diagnostics and a `pooled/` subdirectory for the aggregate γ test. I'll check back when it's done.

---
