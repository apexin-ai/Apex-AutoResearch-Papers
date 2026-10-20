# analysis lf firing rate fixed

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lf-firing-rate-fixed_20260514T230953_result.json`
- **Structured JSON:** [`a04febb6d8b4693d6922.json`](../../sessions/a0/a04febb6d8b4693d6922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here are the results:

---

## Part 1: LF Firing Rate Table (Fixed OH Labels)

**OH stag rate: 20.32%** (all windows) / **21.45%** (embeddings_fixed.pt after filtering) — confirmed fixed from old 6.56%.

| LF | Dataset | Fire Rate (stag vote %) | Precision | Recall | FP Rate |
|---|---|---|---|---|---|
| cmd_rep (λ1) | **OH** | **5.39%** | **97.91%** | **25.99%** | **0.15%** |
| cmd_rep (λ1) | SWE | 17.36% | 69.42% | 45.96% | 8.06% |
| file_diff (λ2) | **OH** | **17.78%** | **99.93%** | **87.46%** | **0.02%** |
| file_diff (λ2) | SWE | 14.61% | 99.91% | 55.66% | 0.02% |
| outcome_bp (λ3) | **OH** | **16.79%** | **20.40%** | **16.85%** | **17.35%** |
| outcome_bp (λ3) | SWE | 21.48% | 47.78% | 39.14% | 17.02% |

Key cross-agent differences:
- **cmd_rep** fires much less on OH (5.39% vs 17.36%) but with much higher precision (97.91% vs 69.42%)
- **file_diff** has similar precision on both but much higher recall on OH (87.46% vs 55.66%)
- **outcome_bp** has near-random precision on OH (20.40%) — essentially useless as a standalone signal

## Part 2: cmd_rep Temporal Offset

| Dataset | Mean Offset | Median | Std | Leading% | Exact% | Lagging% |
|---|---|---|---|---|---|---|
| **OH (fixed)** | **+3.32** | **+1.0** | 8.03 | 9.8% | 32.4% | 57.7% |
| SWE | -1.87 | 0.0 | 7.14 | 36.1% | 41.4% | 22.5% |

cmd_rep on OH remains a **lagging indicator** (mean +3.32 steps, 57.7% lagging) — identical to the old value. This is expected: the label fix affected how majority_label maps to embeddings.pt training labels, but the windows_labeled.jsonl LF votes and majority_labels were already correct. The +3.32 offset is the authoritative number.

On SWE-Agent, cmd_rep is a **leading indicator** (mean -1.87 steps). This cross-agent contrast is a notable finding.

Results saved to registry as `lf-firing-rate-fixed` and artifact at `/root/autodl-tmp/agent_progress_probe/artifacts/lf_firing_rate_fixed_results.json`.

---
