# diagnose exp 004 sim sweep extreme gamma

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_004_sim_sweep_extreme_gamma_20260515T195037_result.json`
- **Structured JSON:** [`9d39ed40057c5feb06b4.json`](../../sessions/9d/9d39ed40057c5feb06b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**判断：success** — 实验正常完成，Cron 报告是误判。

**日志关键内容（末尾）：**
```
seed 9 (10/10): OK γ=3.9021 θ_corr=0.9481 (712.2s)

=== EXTREME GAMMA SWEEP COMPLETE (11.1h) ===
Summary written to .../results_extreme_gamma/sweep_summary.json (8 conditions)
EXTREME_GAMMA_SWEEP_DONE
```

**进程状态：** 已正常退出，无残留进程。

**结果概览（8 条件 × 10 seeds）：**

| γ_true | 条件 | γ_bias | γ_RMSE | CI95% coverage | θ_corr |
|--------|------|--------|--------|----------------|--------|
| 2.0 | 4 条件 | 0.005~0.034 | 0.09~0.12 | **1.00** | 0.95~0.97 |
| 4.0 | 4 条件 | -0.23~0.04 | 0.18~0.29 | **0.90** | 0.91~0.96 |

γ=2.0 恢复准确（bias<0.04, CI95 全覆盖）；γ=4.0 有轻微负偏（低AUC+少模型时 bias=-0.23），CI95 覆盖 90%。

**Registry 更新：**
- 创建 `exp_004_sim_sweep_extreme_gamma`（QUEUED → RUNNING → DONE）
- conclusion = success
- log_path, checkpoint_path, metrics 已设置

---
