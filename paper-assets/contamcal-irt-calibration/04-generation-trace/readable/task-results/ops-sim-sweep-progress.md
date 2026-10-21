# ops sim sweep progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sim-sweep-progress_20260515T175936_result.json`
- **Structured JSON:** [`df00a545f34170c68334.json`](../../sessions/df/df00a545f34170c68334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**进程状态**：PID 528993 已结束，sweep 已完成（日志显示 `SWEEP COMPLETE (0.5h)`）。

**完成度**：12/12 条件全部执行完毕，但其中 **4 个条件全部失败**（0 seeds 成功）：
- `auc0.65_n20`, `auc0.65_n50`, `auc0.65_n100`, `auc0.9_n100`

**失败原因**：CmdStanPy 临时目录文件丢失——`/home/ubuntu/tmp_cmdstan/tmprn3ailon/*.json` 不存在。看起来 CmdStan 的 tmpdir 在采样过程中被清理了。所有 auc0.65 条件和 auc0.9_n100 都受此影响，10/10 seeds 全部 FAIL。

**8 个成功条件的 coverage 汇总**：

| Condition | seeds_ok | γ_bias | γ_RMSE | CI95% | θ_corr |
|-----------|----------|--------|--------|-------|--------|
| auc0.55_n20 | 10 | +0.020 | 0.040 | 80.0% | 0.958 |
| auc0.55_n50 | 10 | +0.015 | 0.026 | 90.0% | 0.947 |
| auc0.55_n100 | 7 | -0.003 | 0.005 | 100% | 0.951 |
| auc0.8_n20 | 10 | -0.016 | 0.081 | 90.0% | 0.972 |
| auc0.8_n50 | 10 | +0.006 | 0.030 | 100% | 0.971 |
| auc0.8_n100 | 9 | +0.011 | 0.033 | 88.9% | 0.969 |
| auc0.9_n20 | 10 | -0.025 | 0.085 | 100% | 0.973 |
| auc0.9_n50 | 7 | +0.004 | 0.038 | 100% | 0.970 |

**关键发现**：
- CI95% coverage 在 80%-100% 之间，大部分条件达到标称水平
- γ bias 很小（|bias| < 0.03），RMSE 随 n_models 增大而减小，符合预期
- θ 相关性始终 > 0.94，说明能力参数恢复良好
- **缺失的 4 个条件（所有 auc0.65 + auc0.9_n100）需要重新运行**

**关于 extreme gamma**：当前 sweep 的 `gamma_true=0.5`（固定值），不涉及 gamma 变化的 sweep。没有 gamma > 0.3 或 < -0.3 的变化条件——所有条件都用相同的 gamma_true=0.5。如果需要研究 extreme gamma 条件下的 coverage 行为，sweep 的设计需要包含 gamma_true 作为变化维度。

**下一步**：需要修复 CmdStanPy tmpdir 问题后重跑失败的 4 个条件。根因是 `/home/ubuntu/tmp_cmdstan/` 下的临时目录在并行运行时被其他进程/清理脚本删除。

---
