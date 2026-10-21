# Progress Check — 2026-05-15

## exp_008e_v3_walker_s2 (gate_fixed_dt=1, subsample_max_dt=2, seed 2)

| 指标 | 值 |
|------|-----|
| PID | 43437 |
| 状态 | **RUNNING** (已运行 ~28 min) |
| 当前 step | 8,000 / 105,000 (7.6%) |
| 最新 eval (step 5K) | eval_return=39.27 |
| value_mean | 0.00193 |
| v/e ratio | ~0.00005 (太早，无意义) |
| gate_dt_mean | 1.0 (100% dt=1) |
| fps | 刚启动，尚未稳定 |

**备注**: 刚启动不到 30 分钟，仍处于极早期。按 seed 1 经验 (~15h 跑完 112K steps)，预计 ~15h 后完成，约 2026-05-16 凌晨。

---

## exp_009a_baseline_walker_s2 (vanilla dreamer, seed 2)

| 指标 | 值 |
|------|-----|
| PID | 142508 |
| 状态 | **RUNNING** (已运行 15h 41m) |
| 当前 step | 368,000 / 500,000 (73.6%) |
| 最新 eval (step 365K) | eval_return=**943.13** |
| value_mean | 664.18 |
| v/e ratio | 664.18 / 943.13 = **0.704** |
| EMA_005 / EMA_095 | 647.73 / 667.57 |
| fps | 3.42 |
| 剩余 steps | 132,000 |
| 预估 ETA | ~5.6h (约 2026-05-15 晚间) |

### eval_return 趋势 (每 10K eval)

| step | eval_return |
|------|------------|
| 5K | 41.21 |
| 25K | 325.33 |
| 55K | 534.13 |
| 105K | 836.51 |
| 215K | 956.04 |
| 245K | 950.32 |
| 285K | 960.20 |
| 315K | 948.66 |
| 335K | 919.23 |
| 345K | 816.18 |
| 355K | 932.45 |
| 365K | 943.13 |

**备注**: eval_return 在 200K+ 后稳定在 900-960 区间，v/e ratio 从上次的 0.699 (336K) 微升至 0.704 (365K)。345K 处有一次 dip 到 816，但已恢复。
