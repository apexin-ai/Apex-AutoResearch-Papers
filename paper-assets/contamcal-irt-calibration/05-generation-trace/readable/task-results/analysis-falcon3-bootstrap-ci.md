# analysis falcon3 bootstrap ci

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_falcon3-bootstrap-ci_20260522T144958_result.json`
- **Structured JSON:** [`4bf1a9a5f2f2fd497232.json`](../../sessions/4b/4bf1a9a5f2f2fd497232.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**MMLU**: Δ = +4.19pp, 95% BCa CI [+3.60, +4.79], Pattern = Benefit (96.1% stable)

**ARC**: Δ = +4.01pp, 95% BCa CI [+2.22, +5.72], Pattern = Benefit-sat (61.3% stable)

关键观察：
- MMLU 的 CI 窄且远离零（CI 下界 +3.60），effect 高度显著，96.1% bootstrap 样本一致分类为 Benefit
- ARC 的 CI 较宽（N=1172 vs 14042），但 CI 下界仍 >0。Pattern stability 较低（61.3%），因为 Benefit 和 Benefit-sat 之间的分界在 bootstrap 中波动（38.7% 被分类为 Benefit 而非 Benefit-sat）
- 两个 benchmark 的 point estimate 都与预期值完全吻合

结果已保存至 `falcon3_bootstrap_ci.md` 并注册为 artifact，JSON 结果保存在 westd 的 `/root/contamcal-irt-calibration/artifacts/falcon3_bootstrap_results.json`。

---
