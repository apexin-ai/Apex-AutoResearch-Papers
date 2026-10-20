# ssh exp017 018 progress v2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp017_018_progress_v2_20260523T105802_result.json`
- **Structured JSON:** [`8b83f546fed6a5816f94.json`](../../sessions/8b/8b83f546fed6a5816f94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度汇总

### GPU 状态
```
GPU 0:  0% util,  73613 / 97887 MiB  ← exp-017 (JAX 预分配显存，MCMC 实际计算量低)
GPU 1:  0% util,      0 / 97887 MiB
GPU 2: 70% util,  73609 / 97887 MiB  ← exp-018 活跃
GPU 3:  0% util,      0 / 97887 MiB
```

---

### exp-018 (cuda:2, N=20 synthetic)

**进度: 15/20 seeds (75%)**，正在运行 seed=15

CSV 31 行 (header + 30 rows = 15 seeds × 2 methods)

最近 5 行：
```
seed | method        | theta_RMSE | tau    | c_RMSE | c_r    | Rhat | ESS  | time(s)
12   | sequential    | 0.1712     | 0.9368 | 1.0764 | 0.8689 | 1.01 | 667  | 162
12   | joint_gmfrm   | 0.0886     | 0.9579 | 0.3349 | 0.9001 | 1.01 | 1367 | 328
13   | sequential    | 0.1754     | 0.9368 | 1.5775 | 0.8229 | 1.01 | 601  | 164
13   | joint_gmfrm   | 0.0847     | 0.9789 | 0.6215 | 0.9047 | 1.01 | 809  | 254
14   | sequential    | 0.1661     | 0.9368 | 1.2335 | 0.8740 | 1.01 | 699  | 162
14   | joint_gmfrm   | 0.0917     | 0.9895 | 0.5126 | 0.9235 | 1.00 | 1195 | 302
```

每 seed 约 ~464s (sequential ~162s + joint ~302s)，剩 5 seeds ≈ **~39 分钟完成**。

---

### exp-017 (cuda:0, Murphy-Topel coverage)

**进度: 48/800 iterations (6%)**，ETA 日志显示 ~260000s ≈ **~72 小时**

CSV 48 行 (header + 47 rows)

最近 5 行：
```
N | seed | cov1  | cov2  | RMSE   | SE     | Rhat | ESS  | time(s)
8 | 43   | 0.75  | 1.0   | 0.726  | 0.291  | 1.0  | 3010 | 332
8 | 44   | 0.375 | 1.0   | 1.074  | 0.307  | 1.0  | 3012 | 343
8 | 45   | 0.5   | 0.875 | 0.815  | 0.288  | 1.0  | 2710 | 348
8 | 46   | 0.375 | 0.875 | 0.592  | 0.275  | 1.0  | 2901 | 346
```

**警告**: 4 chains 在单设备上顺序执行（非并行），每 iteration ~345s。如果能 `numpyro.set_host_device_count(4)` 或分配多 GPU 可显著加速。

---

**总结**: exp-018 约 39 分钟内完成，数据质量良好(Rhat≤1.01)。exp-017 仅完成 6%，按当前速度需 ~3 天，是瓶颈。

---
