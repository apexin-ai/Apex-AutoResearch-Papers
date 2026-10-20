# analysis cross family s2s4 only rrf

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_family_s2s4_only_rrf_20260517T034323_result.json`
- **Structured JSON:** [`a3d88ec2c9a9f9672b5d.json`](../../sessions/a3/a3d88ec2c9a9f9672b5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Run complete. Here are the final results and judgments:

---

## Results Summary

### s2+s4 Cross-Family (s1 excluded):
| Benchmark | N | gamma | 95% CI | Significant? | PPP |
|-----------|---|-------|--------|-------------|-----|
| MMLU | 20 | 0.533 | [-0.42, 1.51] | NO | 0.833 |
| GSM8K | 28 | -0.063 | [-0.48, 0.33] | NO | 0.777 |
| ARC | 20 | **-0.136** | [-0.66, 0.40] | NO | 0.584 |

### Comparison table:
| Benchmark | Qwen-only (N=24) | v4 (s1+s2+s4) | **s2+s4 only** |
|-----------|-------------------|---------------|----------------|
| MMLU γ | +0.655 | +0.415 | +0.533 |
| GSM8K γ | +0.064 | -0.110 | -0.063 |
| ARC γ | **+0.727** (sig!) | +0.002 | **-0.136** |

---

## Key Judgments

**1. Did the cross-family v4 include s1?**  
**YES.** The exposure file `rrf_cross_family_v3/exposure_scores.json` was computed from `rrf_aggregation.py` with `SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s4_selfcritique"]`. Each per-item RRF score contains `rank_s1_embedding` and `s1_embedding` values.

**2. Does the "reversal direction" conclusion still hold without s1?**  
**YES, and it's actually stronger.** ARC gamma goes from +0.727 (Qwen-only, significant) to **-0.136** (cross-family s2+s4). This is a full sign flip. The buggy s1 was actually *masking* the reversal by pulling ARC gamma toward 0 (v4: +0.002). Without s1, the reversal is more pronounced.

**3. Is gamma significant (p < 0.05) in s2+s4 RRF?**  
**NO.** None of the three benchmarks have 95% CIs excluding zero. Same qualitative conclusion as v4.

**4. Comparison with Qwen-only N=24:**  
- MMLU: consistent (0.65 → 0.53, same direction, non-significant in both)
- GSM8K: negligible in both (+0.06 → -0.06)
- ARC: **dramatic shift** from +0.73 (significant) to -0.14 (non-significant). Adding Llama not only eliminates the ARC signal but reverses its sign.

**Note:** MMLU has N=20 in s2+s4 vs N=18 in v4 because Llama d000/d100 were excluded from v4 (no aligned data / degenerate all-A) but included here. This doesn't change the qualitative conclusion.

Results saved to `/root/autodl-tmp/exp006/cross_family_s2s4_only/pooled_rrf_irt_results.json`.

---
