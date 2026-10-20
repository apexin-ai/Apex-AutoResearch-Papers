# exp_032_dual_critic_walker Analysis

## Summary
- **Conclusion: success**
- Dual-critic (min of two independent critics) suppresses CIVO. NVE peak 1.1 at 95K, well below 1.5× threshold, final 0.1.
- Eval peak 787.7 (205K), final 739.7 (215K). Strong performance.
- Consistent with exp_032b (seed=1): CIVO suppressed across both seeds.

| Metric | Value |
|--------|-------|
| Final eval return | 739.7 |
| Peak eval return | 787.7 (205K) |
| Final NVE | 0.1 |
| Peak NVE | 1.1 (95K) |
| v1-v2 gap | <0.1 (negligible) |
| Gate dt=2 frac | 1.0 (collapsed) |
| Final step | 224K (last eval 215K) |
| CIVO alerts | 1 soft warning (65K, ve=0.565) |
| Exit code | 0 (clean) |

## NVE Trajectory

| Step | NVE | v1_mean | v2_mean |
|------|-----|---------|---------|
| 15K  | 0.0 | 2.9     | 2.9     |
| 25K  | 0.1 | 22.1    | 22.1    |
| 35K  | 0.1 | 51.6    | 51.6    |
| 45K  | 0.2 | 104.1   | 104.0   |
| 55K  | 0.4 | 153.9   | 153.9   |
| 65K  | 0.6 | 206.8   | 206.8   |
| 75K  | 0.6 | 296.5   | 296.5   |
| 85K  | 0.9 | 329.8   | 329.8   |
| 95K  | **1.1** | 280.0 | 280.0  |
| 105K | 0.5 | 211.6   | 211.6   |
| 115K | 0.4 | 167.1   | 167.1   |
| 125K | 0.3 | 134.5   | 134.5   |
| 135K | 0.2 | 109.4   | 109.4   |
| 145K | 0.2 | 92.0    | 92.0    |
| 155K | 0.1 | 77.0    | 77.0    |
| 165K | 0.2 | 66.8    | 66.8    |
| 175K | 0.1 | 59.4    | 59.4    |
| 185K | 0.1 | 55.3    | 55.4    |
| 195K | 0.1 | 51.1    | 51.1    |
| 205K | 0.1 | 46.6    | 46.6    |
| 215K | 0.1 | 44.0    | 44.0    |

NVE rises gradually from 0 to peak 1.1 at 95K, then monotonically decays to 0.1. No CIVO blowup. The single CIVO detector warning at 65K (ve_ratio=0.565) was a soft signal based on acceleration + eval decline pattern, not a high NVE event. NVE resolved naturally without intervention.

## Eval Trajectory

| Step | eval_return |
|------|-------------|
| 5K   | 35.6        |
| 15K  | 94.0        |
| 25K  | 172.0       |
| 35K  | 385.5       |
| 45K  | 449.4       |
| 55K  | 414.5       |
| 65K  | 364.9       |
| 75K  | 460.2       |
| 85K  | 371.5       |
| 95K  | 256.6       |
| 105K | 421.4       |
| 115K | 438.7       |
| 125K | 486.4       |
| 135K | 456.7       |
| 145K | 416.3       |
| 155K | 514.0       |
| 165K | 406.9       |
| 175K | 472.2       |
| 185K | 624.8       |
| 195K | 599.9       |
| 205K | **787.7**   |
| 215K | 739.7       |

Eval shows a dip at 95K (256.6) coinciding with NVE peak, then steady recovery. Performance continues climbing through 185K+, reaching strong values (787.7 peak). Late-stage eval (185K+) substantially exceeds mid-stage (65K-155K range ~400-500).

## Dual-critic Mechanism

### v1 vs v2 gap
v1 and v2 are essentially identical throughout training:
- Maximum absolute gap: 0.1 (at 45K: v1=104.1 vs v2=104.0; at 185K: v1=55.3 vs v2=55.4)
- Relative gap: <0.1% at all checkpoints
- The min(v1, v2) operation has **no pessimism effect** — both critics converge to the same function

### Gate behavior
- gate_dt_2_frac = 1.0 at every checkpoint (100%)
- gate_dt_mean = 2.0, gate_dt_std = 0.0
- Gate completely collapsed to minimum horizon dt=2
- Adaptive horizon mechanism is inactive

### Actor gradient
- actor_loss ≈ 0 in late training (105K+: actor_loss = -0.0 to 0.0)
- actor_grad_norm = 0.1 throughout late training
- Low but nonzero actor gradients — actor is still learning slowly, as evidenced by eval improvement from 421 (105K) to 787 (205K)

## Comparison with exp_032b (seed=1)

| Metric | exp_032 (s0) | exp_032b (s1) | Delta |
|--------|-------------|---------------|-------|
| NVE peak | 1.1 (95K) | 1.4 (85K) | s0 lower |
| NVE final | 0.1 | 0.1 | same |
| Eval peak | 787.7 (205K) | 551.8 | s0 +43% |
| Eval final | 739.7 (215K) | 516 | s0 +43% |
| v1≈v2 gap | <0.1% | <0.5% | both negligible |
| Gate collapse | dt=2, 100% | dt=2, 100% | same |
| CIVO suppressed | yes | yes | both |

Both seeds confirm:
1. **CIVO suppression**: NVE stays below 1.5× threshold
2. **v1≈v2 convergence**: Min operation has no pessimism effect
3. **Gate collapse**: Adaptive horizon inactive

Seed=0 achieves substantially higher eval (787.7 vs 551.8 peak). This may reflect normal seed variance rather than a systematic difference — the CIVO suppression pattern is consistent.

## Conclusion

**Success.** Dual-critic (min of two independent critics for actor loss) effectively suppresses CIVO, as hypothesized. NVE peaks at 1.1× (below 1.5× threshold) and decays to 0.1× by end of training. This is consistent across both seeds (032 and 032b).

Key observations:
- The mechanism works via CIVO prevention, not via pessimistic value estimation (v1≈v2 throughout)
- The actual mechanism by which dual-critic suppresses CIVO remains unclear — it may be through implicit regularization of the value function rather than the intended min-of-two pessimism
- Gate collapse to dt=2 is a shared confound with exp_032b; adaptive horizon is not being tested under dual-critic
- Eval performance is strong (787.7 peak), suggesting dual-critic does not harm learning while suppressing CIVO
