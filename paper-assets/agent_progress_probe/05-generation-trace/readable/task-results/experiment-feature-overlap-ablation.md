# experiment feature overlap ablation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_feature-overlap-ablation_20260515T015411_result.json`
- **Structured JSON:** [`0daa899161881fecbae4.json`](../../sessions/0d/0daa899161881fecbae4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results

| Setting | #Feat | RF In-domain | Δ | GB In-domain | Δ | RF Cross-agent | Δ | GB Cross-agent | Δ |
|---------|-------|-------------|---|-------------|---|---------------|---|---------------|---|
| full_30 | 30 | 0.9951 | — | 0.9951 | — | 0.9123 | — | 0.9674 | — |
| no_cmd_rep | 25 | 0.9550 | -4.0pp | 0.9683 | -2.7pp | 0.6884 | -22.4pp | 0.5616 | -40.6pp |
| no_file_diff | 25 | 0.9833 | -1.2pp | 0.9847 | -1.0pp | 0.6687 | -24.4pp | 0.6590 | -30.8pp |
| no_outcome_bp | 29 | 0.9951 | 0.0pp | 0.9951 | 0.0pp | 0.9119 | -0.0pp | 0.9655 | -0.2pp |
| **no_all_lf** | **19** | **0.9326** | **-6.2pp** | **0.9515** | **-4.4pp** | **0.4601** | **-45.2pp** | **0.5656** | **-40.2pp** |

### Key findings:

1. **In-domain residual F1**: Removing all 11 LF-overlapping features, the 19 residual features still achieve **GB=0.952 / RF=0.933 macro_f1** in-domain. This is a modest drop (-4.4pp / -6.2pp), suggesting the in-domain task has enough redundancy in non-LF features.

2. **Cross-agent collapse**: The residual features **collapse on cross-agent transfer**: GB drops from 0.967 to **0.566** (-40.2pp), RF from 0.912 to **0.460** (-45.2pp). The cross-agent generalization was almost entirely driven by LF-overlapping features.

3. **cmd_rep features are the most critical**: Removing just the 5 cmd_rep features causes the largest single-LF drop on cross-agent GB (-40.6pp), confirming command repetition patterns are the dominant structural signal.

4. **outcome_bp overlap is negligible**: Removing `is_short_trajectory` has essentially zero effect.

5. **Circularity concern is validated**: The dream review's concern is correct — structural features' high cross-agent F1 (0.967) is largely circular with LF signals. The non-circular residual achieves only 0.566 cross-agent, which is close to majority-class baseline.

### Outputs:
- Script: `/root/autodl-tmp/agent_progress_probe/src/analysis/feature_overlap_ablation.py`
- Results: `/root/autodl-tmp/agent_progress_probe/artifacts/feature-overlap-ablation/ablation_results.json`
- Classification: `artifacts/feature-overlap-ablation/feature_classification.md` (local)

---
