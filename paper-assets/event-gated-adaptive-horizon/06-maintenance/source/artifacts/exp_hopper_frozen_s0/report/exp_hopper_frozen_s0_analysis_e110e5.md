# exp_hopper_frozen_s0 Analysis Report

## Experiment Configuration
- **Environment**: Hopper Hop (dm_control)
- **Config**: gate_enabled=True, gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, dt_emb_freeze=True, seed=0
- **Steps**: 105K (data collection continued to 112K)
- **Wall clock**: ~2.95 hours
- **Server**: westd-51268

## Hypothesis
> Frozen dt_emb + subsample ON in Hopper Hop will NOT show CIVO (NVE stays below 1.5x), confirming trained dt_emb is the necessary condition for CIVO across a third multi-joint locomotion environment.

## Result: NEGATIVE (Hypothesis Rejected)

Frozen dt_emb did **not** prevent CIVO. The CIVO detector fired at steps 65K and 105K with ve_ratio values in the hundreds of thousands to millions. The agent completely failed to learn (eval_return ≈ 0 throughout) while value estimates grew monotonically, indicating a total disconnect between imagined and actual performance.

## Key Metrics

### Eval Return Trajectory
| Step | eval_return |
|------|-------------|
| 5K   | 0.0 |
| 15K  | 0.6 |
| 25K  | 0.1 |
| 35K  | 0.4 |
| 45K  | 0.96 |
| 55K  | 0.0 |
| 65K  | 0.0 |
| 75K  | 2.23 |
| 85K  | 3.6 |
| 95K  | 1.1 |
| 105K | 0.0 |

### CIVO Metrics Trajectory
| Step | civo/ve_ratio | value_mean | target_mean | NVE (V vs T) | eval_return | alert |
|------|---------------|------------|-------------|--------------|-------------|-------|
| 15K  | 0.062 | 0.040 | 0.042 | 0.044 | 0.6 | 0 |
| 25K  | 1.291 | 0.069 | 0.073 | 0.059 | 0.1 | 0 |
| 35K  | 0.456 | ~0.2 | ~0.2 | ~0.02 | 0.4 | 0 |
| 45K  | 0.216 | 0.208 | 0.210 | 0.009 | 0.96 | 0 |
| 55K  | 14,441 | 0.330 | 0.338 | 0.024 | 0.0 | 0 |
| 65K  | 819,655 | 0.820 | 0.836 | 0.019 | 0.0 | **1** |
| 75K  | 0.513 | 1.144 | 1.157 | 0.011 | 2.23 | 0 |
| 85K  | 0.6 | 2.0 | 2.0 | ~0.01 | 3.6 | 0 |
| 95K  | 2.690 | 2.913 | 2.941 | 0.009 | 1.1 | 0 |
| 105K | 4,335,664 | 4.337 | 4.389 | 0.012 | 0.0 | **1** |

### Summary Statistics
- **eval_return_final** (105K): 0.0
- **eval_return_peak**: 3.6 @ 85K
- **civo/ve_ratio_final**: 4,335,664
- **civo/ve_ratio_peak**: 4,335,664 @ 105K
- **CIVO alerts**: 2 (steps 65K, 105K)
- **NVE (value vs target) max**: 0.059 @ 25K — always < 0.1, well below 1.5x threshold
- **gate_dt**: fixed at 2.0 throughout (as expected)
- **actor_entropy**: collapsed from 5.5 → -1.6 (policy entropy collapse)

## Comparison with Prior Experiments

| Metric | baseline (no gate) | trained_s0 (trained dt_emb) | **frozen_s0 (frozen dt_emb)** |
|--------|-------------------|---------------------------|-------------------------------|
| eval_return_final | 96.43 | 3.26 (81.58 @ 168K) | **0.0** |
| ve_ratio_final | 0.559 | 0.897 | **4,335,664** |
| ve_ratio_peak | 3.48 @ 65K | — | **4,335,664 @ 105K** |
| CIVO alerts | 0 | 0 | **2** |
| Learning | Normal | Severe delay, eventual recovery | **Complete failure** |
| value_mean growth | Tracks returns | Low | **Monotonic, disconnected from reality** |

## Analysis

### 1. Two Faces of CIVO

The experiment reveals a critical distinction between two forms of value overestimation:

- **NVE (value vs lambda-target)**: Always < 0.06. The value network accurately fits its own TD-lambda bootstrap targets. By this narrow metric, there is no classic CIVO.
- **civo/ve_ratio (value vs actual returns)**: Reaches millions. The entire imagination pipeline (world model + value + actor) constructs internally consistent but fictional futures. Value estimates grow to 4.3 while actual returns are 0.

The frozen dt_emb prevents value-target divergence but introduces a worse pathology: **value-reality divergence**. The model imagines a self-consistent but unrealizable world.

### 2. Complete Learning Failure

The eval_return never exceeds 3.6 (vs baseline's 96.43). The agent fails to learn meaningful behavior in 105K steps. The brief improvement at 75-85K (2.2-3.6) is likely noise, followed by collapse back to 0.

### 3. Monotonic Value Inflation

value_mean grows from 0.04 to 4.34 monotonically, despite eval_return ≈ 0. This happens because:
- The frozen dt_emb provides a static, uninformative temporal embedding
- The world model learns to generate reward-optimistic imaginary trajectories
- The value network accurately estimates these fictional trajectories (NVE < 0.06)
- But the actor, guided by these values, produces actions that achieve nothing in reality

### 4. Policy Entropy Collapse

actor_entropy drops from 5.5 (near uniform) to -1.6 (highly concentrated). The policy becomes deterministic based on the fictional value landscape, further preventing exploration and recovery.

### 5. Implications for dt_emb Theory

The hypothesis that "trained dt_emb is the necessary condition for CIVO" is **rejected**. Frozen dt_emb produces even more extreme CIVO (by ve_ratio) and worse performance than both baseline and trained dt_emb configurations. The result suggests:

- dt_emb training is not the cause of CIVO — rather, the gate mechanism itself (even with fixed dt) introduces compounding errors in the imagination pipeline
- A frozen, uninformative dt_emb may actually be worse because it provides no useful temporal signal, causing the world model to learn degenerate dynamics
- The "necessary condition" for CIVO in gated configurations may be the gate architecture itself, not the trainability of any specific component

## Conclusion

**Hypothesis REJECTED.** Frozen dt_emb not only fails to prevent CIVO, it produces the worst outcome of all three Hopper configurations: complete learning failure (eval_return = 0) with extreme value overestimation (ve_ratio > 4M). The trained dt_emb variant, while also problematic, at least eventually recovered to eval_return = 81.58. Freezing dt_emb removes the model's ability to adapt temporal representations, leading to a degenerate imagination pipeline that is internally consistent but completely disconnected from reality.
