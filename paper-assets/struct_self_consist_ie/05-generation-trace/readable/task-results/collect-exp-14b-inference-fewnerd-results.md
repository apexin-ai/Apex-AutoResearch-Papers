# collect exp 14b inference fewnerd results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_exp_14b_inference_fewnerd_results_20260521T071849_result.json`
- **Structured JSON:** [`f0f1e5fe963f079d2222.json`](../../sessions/f0/f0f1e5fe963f079d2222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## exp_14b_inference_fewnerd — DONE/success

**Process**: PID 217692 finished and was killed by `kill_after_n8.sh` after completing N=8 (N=16 intentionally cut per Director). GPUs now running other experiments (PIDs 293xxx-294xxx).

**Results** (`output/14b_final_inference/`):

| N | greedy_f1 | oracle_f1 | oracle_headroom | soft_jaccard ρ | ρ_advantage | structural > surface | verdict |
|---|-----------|-----------|-----------------|----------------|-------------|----------------------|---------|
| 1 | 0.7985 | 0.7541 | -0.044 | — | — | — | FAIL |
| 2 | 0.7985 | 0.8086 | +0.010 | 0.205 | -0.006 | no | FAIL |
| 4 | 0.7984 | 0.8544 | +0.056 | 0.314 | +0.042 | **yes** | MARGINAL |
| 8 | 0.7984 | 0.8791 | +0.081 | 0.324 | +0.083 | **yes** | MARGINAL |

**Key patterns**:
- greedy_f1 stable at ~0.798 regardless of N
- oracle_f1 grows strongly: 0.754 → 0.879 (N=1→8), headroom +8.1pp at N=8
- structural consistency beats surface (logprob) starting at N=4, with rho_advantage widening from +0.042 to +0.083
- Cross-domain SciERC/CoNLL results also completed (15 subdirs total) but expected poor

Registry updated: conclusion → success, failure_reason cleared, metrics and checkpoint_path set.

---
