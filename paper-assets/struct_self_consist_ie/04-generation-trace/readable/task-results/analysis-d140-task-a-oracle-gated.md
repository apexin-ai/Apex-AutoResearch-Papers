# analysis d140 task a oracle gated

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d140_task_a_oracle_gated_20260518T132211_result.json`
- **Structured JSON:** [`78df9df59e3d2a16e3e8.json`](../../sessions/78/78df9df59e3d2a16e3e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here are the key results:

## D140 Oracle Degeneracy-Gated LP Selection: Results Summary

**The hypothesis that degeneracy gates LP selection effectiveness is NOT supported by the data.** The results tell a different story:

### Overall Picture
| Dataset | Degen% | LP vs Greedy | NonDeg LP vs Greedy | Gated vs LP |
|---------|--------|-------------|---------------------|-------------|
| SciERC | 17.8% | -0.31 (ns) | -0.29 (ns) | +0.06 (ns) |
| CoNLL | 48.4% | **-2.37** (sig) | **-3.58** (sig) | +0.05 (ns) |
| Few-NERD | 13.8% | +0.07 (ns) | +0.15 (marginal) | **+0.06** (sig) |

### Key Takeaways

1. **LP selection hurts or is neutral everywhere.** On CoNLL it's significantly negative (-2.37, CI excludes 0). On SciERC and Few-NERD the CI includes 0.

2. **The gating hypothesis doesn't hold.** On non-degenerate instances (where oracle CAN improve), LP selection is *worse* than on degenerate ones for CoNLL (-3.58 non-deg vs -2.37 overall) and roughly the same for SciERC. The problem isn't that LP picks from identical-F1 candidates; it's that LP picks *wrong* even when there's signal.

3. **Gated > ungated LP is technically true but tiny.** Gated improves over ungated LP by +0.05-0.06 across all datasets, but only Few-NERD's Gated vs LP CI is fully positive [+0.04, +0.08]. The improvement comes purely from substituting greedy on degenerate instances (where LP might pick a logprob-higher but identical-F1 sample that happens to have different tp/fp/fn counts).

4. **Oracle gap is huge (5-11 F1 points)** but LP selection cannot exploit it. The selection signal (mean logprob) is fundamentally miscalibrated for entity-level quality.

Script saved at `code/analysis_d140_oracle_gated.py`, results at `output/d140_oracle_gated/{results.json, report.md}`.

---
