# analysis exp004 incremental

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004-incremental_20260514T082606_result.json`
- **Structured JSON:** [`f62f6d2e04bdcec14a30.json`](../../sessions/f6/f62f6d2e04bdcec14a30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。43/120 seeds (35.8%)，5/12 conditions 有数据。

关键更新（vs 上次 27/120）：

1. **AUC=0.80 CI 异常已确认**：16 seeds 跨 N=20 和 N=50，CI 宽度稳定为 AUC=0.55 的 ~1.9×。机制是后验方差膨胀（exposure-ability collinearity），而非 bias。
2. **新发现：bias 方向反转**——AUC=0.55 时 γ 被高估 (+0.02)，AUC=0.80 时被低估 (−0.016)。高 AUC 下 collinearity 使部分 contamination signal 被吸收进 θ。
3. **1/√N 缩放**在两个 AUC 水平下都精确成立（偏差 <5%）。
4. **Power 仍为 100%**（43/43 runs）。
5. **MCMC 质量完美**：零 divergence，Rhat < 1.011。

当前正在跑 auc0.80_n50 seed 6。还缺 AUC=0.65 和 0.90 的数据来画完整曲线。

---
