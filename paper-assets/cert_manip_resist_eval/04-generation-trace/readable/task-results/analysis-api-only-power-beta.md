# analysis api only power beta

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_api-only-power-beta_20260524T190116_result.json`
- **Structured JSON:** [`9862b900b5a7e4587349.json`](../../sessions/98/9862b900b5a7e4587349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A3 API-only power analysis complete. Results saved to `/root/cert_manip_resist_eval/artifacts/results/plan001/api_only_power_beta.json`.

## Key Findings

**Interpretation: `power_issue`** — API-only β_std is 164% of full pool; effect size is preserved, low significance is purely from fewer panels/clusters.

### β_std Comparison (full pool vs API-only)

| K | Full Pool β_std | API-only β_std | Ratio | API Panels | Full Panels |
|---|----------------|----------------|-------|------------|-------------|
| 3 | 0.349 | 0.634 | 1.82× | 84 | 455 |
| 5 | 0.437 | 0.796 | 1.82× | 126 | 3,003 |
| 7 | 0.401 | 0.511 | 1.27× | 36 | 6,435 |

### WCB Significance (API-only, α=0.05)

| K | Sig Count | Significant Conditions |
|---|-----------|----------------------|
| 3 | **4/12** | arc×position_bias (p=0.016), mmlu×authority_bias (p=0.047), mmlu×score_manipulation (p=0.047), mmlu×sycophancy (p=0.023) |
| 5 | **1/12** | arc×position_bias (p=0.041) |
| 7 | **0/12** | — |

### Power Curves (average across 12 conditions)

| β_std | K=3 Power | K=5 Power | K=7 Power |
|-------|-----------|-----------|-----------|
| 0.3 | 0.082 | 0.013 | 0.0 |
| 0.5 | 0.322 | 0.055 | 0.0 |
| 0.7 | 0.591 | 0.128 | 0.0 |
| 1.0 | 0.785 | 0.271 | 0.0 |

**MDE@80%**: `null` for all K values — power never reaches 80% within the tested β_std grid [0.1, 1.0].

### Conclusion

The API-only subset's K_eff effect on manipulation resistance is **at least as strong** as the full 15-model pool (ratio ~1.6×). The dramatic drop in significance counts (from full pool's 7-9/12 to API-only's 0-4/12) is entirely attributable to reduced statistical power: 9 API models produce far fewer panel combinations and only 7-9 clusters per position (vs 15), making the wild cluster bootstrap extremely conservative. K=7 with only 36 panels and 3 clusters per position has literally zero power at any effect size tested.

---
