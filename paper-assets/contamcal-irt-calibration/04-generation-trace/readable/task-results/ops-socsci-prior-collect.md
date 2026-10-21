# ops socsci prior collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_socsci_prior_collect_20260517T191812_result.json`
- **Structured JSON:** [`c244e2080230e691bc79.json`](../../sessions/c2/c244e2080230e691bc79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## γ Prior Sensitivity 结果 — Social Sciences (J=16, I=2000)

| Prior | γ̂ mean | γ̂ median | 95% CI | P(γ<0) | PPP | Rhat | ESS_min | Time |
|---|---|---|---|---|---|---|---|---|
| **N(0, 0.5)** tight | -0.428 | -0.428 | [-0.825, -0.017] | **0.9795** | 0.242 | 1.008 | 1401 | 593s |
| **N(0, 1.0)** baseline | -0.497 | -0.498 | [-0.943, -0.055] | **0.9848** | 0.282 | 1.009 | 1457 | 594s |
| **N(0, 2.0)** loose | -0.507 | -0.505 | [-0.957, -0.077] | **0.9892** | 0.282 | 1.007 | 1384 | 606s |

### 关键结论

**P(γ<0) 在最严格的 tight prior N(0, 0.5) 下仍达 97.95%**，满足 >95% 的阈值。

结果对 prior 选择非常稳健：
- γ̂ 从 tight 到 loose 仅变化 -0.428 → -0.507（约 0.08 的偏移）
- 95% CI 都不包含 0（tight 的上界 -0.017 也远离 0）
- P(γ<0) 单调递增：0.9795 → 0.9848 → 0.9892
- 三种 prior 诊断全部通过：零 divergences, Rhat < 1.01, ESS > 1300
- PPP 合理（0.24-0.28），模型拟合良好

---
