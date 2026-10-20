# analysis d073 s1b acr adapted lf

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-s1b-acr-adapted-lf_20260516T033555_result.json`
- **Structured JSON:** [`ec527fd5d38a27658b20.json`](../../sessions/ec/ec527fd5d38a27658b20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment `d073-s1b-acr-adapted` registered as DONE. Here's the analysis:

## Results Summary

### Phase 1: ACR LF Statistics (1946 windows)
| LF | Stag | Coverage | Trigger Rate |
|---|---|---|---|
| command_repetition | 29 | 81.7% | 1.5% |
| **action_entropy** | **771** | **39.6%** | **39.6%** |
| output_stagnation | 0 | 0% | 0% |
| error_repetition | 0 | 0% | 0% |

**output_stagnation and error_repetition have zero coverage on ACR** — ACR trajectories never produce consecutive similar observations or repeated errors in the patterns these LFs detect. The adapted label set is effectively driven by **action_entropy alone** (plus cmd_rep's small contribution).

### Phase 3: Cross-Agent Transfer Delta (all non-abstain)
| Model | Orig macro_f1 | Adapted macro_f1 | Delta | Orig f1_stag | Adapted f1_stag | Delta |
|---|---|---|---|---|---|---|
| GB | 0.6078 | 0.5719 | **-3.6pp** | 0.2613 | 0.2094 | -5.2pp |
| **RF** | **0.6645** | **0.7686** | **+10.4pp** | **0.4155** | **0.6049** | **+18.9pp** |
| LR | 0.6561 | 0.6746 | +1.9pp | 0.3630 | 0.4074 | +4.4pp |

### Phase 4: LF Contribution
- action_entropy is the **sole stag trigger** on 219/248 (88.3%) adapted stagnation windows
- Adapted 3-LF = Adapted 4-LF (error_repetition adds nothing)
- conf≥2 subset is degenerate: only 27 windows, all stagnation (no progress class to evaluate)

### Key Takeaways
1. **RF benefits strongly from adapted labels** (+10.4pp macro_f1), confirming that LF portability matters for cross-agent transfer
2. **GB degrades** — it was already overfitting to the original label distribution pattern; the shifted stag rate (10.1%→13.7%) hurts its calibration
3. **action_entropy is doing all the heavy lifting** — output_stagnation contributes nothing on ACR, meaning the adapted 3-LF set is effectively a 2-LF system (cmd_rep + action_entropy)
4. The improvement is real but model-specific — not a universal transfer ceiling lift, but rather RF's ensemble structure handles the relabeled signal better

---
