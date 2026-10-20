# analysis exp 015b final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_015b_final_20260515T182848_result.json`
- **Structured JSON:** [`4ca911727f88228b8f42.json`](../../sessions/4c/4ca911727f88228b8f42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Final Metrics Summary
- **final_step:** 105K (eval), training continued to ~112K env steps
- **exit_status:** normal (EXIT_CODE=0)
- **checkpoint_path:** `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb/latest.pt`

## Eval Trajectory (85K onwards)

| Step | eval_return | value_mean | value_std | ve_ratio | nve (vs baseline) | actor_loss | actor_entropy | model_loss | gate_dt_mean | gate_dt_1_frac |
|------|-------------|------------|-----------|----------|--------------------|------------|---------------|------------|--------------|----------------|
| 85K  | 183.48      | 60.088     | 14.043    | 0.327    | 0.467 (bl=0.701)   | 0.000609   | -5.101        | 4.437      | 2.0          | 0.0            |
| 95K  | 238.38      | 59.341     | 13.889    | 0.249    | 0.394 (bl=0.632)   | 0.001614   | -5.015        | 4.425      | 2.0          | 0.0            |
| 105K | 204.20      | 56.212     | 13.818    | 0.275    | 0.420 (bl=0.656)   | 0.000179   | -4.855        | 4.431      | 2.0          | 0.0            |

## Full Eval Trajectory (for reference)

| Step | eval_return |
|------|-------------|
| 5K   | 31.0        |
| 15K  | 167.9       |
| 25K  | 171.8       |
| 35K  | 201.6       |
| 45K  | 122.3       |
| 55K  | 105.8       |
| 65K  | 160.3       |
| 75K  | 80.0        |
| 85K  | 183.5       |
| 95K  | **238.4** (peak) |
| 105K | 204.2       |

## Diagnosis

- **CIVO signature (sustained NVE > 1.5x at 35K+): NO** — NVE is 0.39–0.47, far below 1.0. The critic is massively *under*-estimating, not over-estimating.

- **Gradient starvation signature: YES** — actor_loss collapsed to ~0 (0.0002 at 105K). The actor receives essentially no gradient signal. Value_mean is *declining* (60.1 → 56.2) while being far below eval_return, meaning the critic is becoming more pessimistic even as the policy occasionally achieves high returns.

- **Gate collapse: COMPLETE** — gate_dt is locked at 2.0 with 100% dt_2_frac and zero entropy across all checkpoints. This is by design (frozen dt embedding), but confirms the gate never explores other horizons.

- **Actor entropy trend:** -5.10 → -5.01 → -4.86. Slightly *increasing* (less concentrated), which is unusual — typically entropy drops with gradient starvation. This suggests the policy is drifting rather than converging, consistent with near-zero actor gradients providing no directional signal.

- **Final assessment:** The frozen-dt-emb ablation confirms that without adaptive horizon gating, the critic severely underestimates returns (V/E ~0.27 vs baseline ~0.65), actor gradients vanish, and eval performance is highly volatile (80–238 range) with no stable convergence. The 95K peak of 238.4 exceeds some baseline checkpoints but is not sustained, dropping to 204.2 at 105K. This is consistent with the hypothesis that adaptive dt is necessary for stable value estimation — freezing it at dt=2 creates a systematic negative bias in the critic that starves the actor of useful gradients.

---
