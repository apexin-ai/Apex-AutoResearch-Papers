# exp_016e NVE Diagnostic Report (2026-05-16)

## Status
- **Process**: PID 527392, running, elapsed 2h43m
- **Current step**: 96K (train), 95K (latest eval)
- **Target**: 105K steps
- **Verdict**: ⚠️ CIVO CONFIRMED — NVE 6.59x

## Eval Return Trajectory
| Step | eval_return | delta |
|------|------------|-------|
| 5K   | 31.00      | —     |
| 15K  | 140.30     | +109  |
| 25K  | 141.75     | +1    |
| 35K  | 173.01     | +31   |
| 45K  | 184.03     | +11   |
| 55K  | 153.79     | -30   |
| 65K  | 324.30     | +171  |
| 75K  | **326.67** | +2 (peak) |
| 85K  | 256.21     | -70   |
| 95K  | **31.73**  | -225 (collapse) |

## NVE Analysis
| Metric | @85K | @95K |
|--------|------|------|
| eval_return | 256.21 | 31.73 |
| value_mean (imagination) | 215.39 | 208.88 |
| **NVE = V(s)/actual** | **0.84x** ✅ | **6.59x** 🚨 |
| target_mean | 216.11 | 208.35 |
| value_loss | 0.989 | 0.992 |
| actor_entropy | -3.83 | -4.65 |
| EMA_005 / EMA_095 | 200.95 / 230.05 | 191.55 / 232.58 |

## Supporting Evidence
1. **Actor entropy collapse**: -3.83 → -4.65 (premature policy commitment)
2. **Value loss flat**: 0.989 → 0.992 (critic blind to performance collapse)
3. **Train returns collapsed**: ~290 @84K → ~47 @92K → ~69 @96K
4. **EMA bands stale**: normalization range hasn't tracked the distribution shift
5. **Gate fixed**: dt_mean=2.0, entropy=0.0 (by design, gate_fixed_dt=2)

## Mechanism
Stale critic (V≈209) → actor exploits inflated value landscape → entropy collapse → gradient starvation → actual returns collapse → CIVO positive feedback loop.

## Comparison
| Experiment | NVE peak | Step | Outcome |
|-----------|----------|------|---------|
| 008d | 4.12x | 55K | diverged |
| 015b | 1.45x | 55K | self-corrected |
| **016e** | **6.59x** | **95K** | **CIVO collapse** |

## Prognosis
Unrecoverable with ~10K steps remaining. Experiment effectively failed at ~85K-90K.
