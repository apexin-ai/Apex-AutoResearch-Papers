# ssh exp016 015 status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp016_015_status_check_20260523T075304_result.json`
- **Structured JSON:** [`651b803c7519a1ab3256.json`](../../sessions/65/651b803c7519a1ab3256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

### exp-016 Prior Sensitivity (PID 316023)

- **状态**: 运行中，已 53 分钟
- **进度**: 仍在第 1 个 prior（HalfNormal(1.5)）的 **warmup 阶段**，step 1340/6000（22%）
- **结果**: 空，尚无 CSV 输出
- **问题**: warmup 速度在 step 1324 处从 ~4.6 it/s 骤降至 ~1.2 s/it（慢了约 5.5 倍）
- **GPU 2**: 仅用 667 MiB / 97887 MiB，利用率 70%——进程主要跑在 CPU（100% CPU, 1.7GB RSS）
- **预估**: 按当前速度，仅第一个 prior 的 warmup 还需 ~93 分钟，4 个 prior 全部完成可能需要 **10+ 小时**
- **注意**: 日志末尾有前一次运行 (PID 293733) 被 Kill 的痕迹（EXIT_CODE=129）

### exp-015 Synthetic N=8 (PID 291466)

- **状态**: 运行中，已 2h 3min
- **进度**: seed 12/20（60%），已输出 24 行（12 seeds × 2 methods）
- **GPU 1**: 73583 MiB / 97887 MiB，61% 利用率
- **收敛**: 全部 R-hat=1.000，ESS 健康（2000-3900）
- **预估**: 剩余 8 seeds，每 seed ~10 min，约 **80 分钟**后完成

**exp-015 已有结果汇总（12 seeds 均值）:**

| 指标 | Sequential | Joint GMFRM | 改进 |
|------|-----------|-------------|------|
| theta_RMSE | 0.165 | 0.083 | **-50%** |
| theta_tau (Kendall) | 0.853 | 0.964 | **+13%** |
| c_RMSE | 1.389 | 0.597 | **-57%** |
| c_pearson | 0.807 | 0.838 | +4% |
| elapsed (s) | 256 | 345 | +35% |

Joint GMFRM 在 theta 估计和 ranking agreement 上全面碾压 sequential，代价是每 seed 多 ~90 秒。

---
