# analysis cross family irt v5 final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_family_irt_v5_final_20260517T040857_result.json`
- **Structured JSON:** [`9dac3cd1ad7517aadce5.json`](../../sessions/9d/9dac3cd1ad7517aadce5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v5 完成。结果汇总：

## Cross-Family Pooled IRT v5 — 完整 s1+s2+s4 RRF（s1 bug 已修复）

| Benchmark | N | γ | 95% CI | Significant? | PPP | calMAE | ΔMAE |
|-----------|---|---|--------|:---:|---|---|---|
| **MMLU** | 18 | 0.35 | [-0.63, 1.32] | NO | 0.624 | 0.008 | 0.030 |
| **GSM8K** | 28 | -0.13 | [-0.52, 0.27] | NO | 0.842 | 0.008 | 0.171 |
| **ARC** | 20 | 0.01 | [-0.57, 0.56] | NO | 0.435 | 0.015 | 0.055 |

## v4 vs v5 对比

| Benchmark | v4 γ | v5 γ | Δγ | v4 sig? | v5 sig? |
|-----------|------|------|-----|:---:|:---:|
| MMLU | 0.41 | 0.35 | -0.07 | NO | NO |
| GSM8K | -0.11 | -0.13 | -0.02 | NO | NO |
| ARC | 0.00 | 0.01 | +0.01 | NO | NO |

## 关键判断

1. **ARC γ 没有变显著。** v5 ARC γ=0.01，与 v4 基本一致（≈0），加入修正后的 s1 没有改变结论。

2. **整体 cross-family claim：所有三个 benchmark 的 γ 95% CI 都包含 0**。修正 s1 后结果几乎不变 — 说明 s1 bug 对 Llama 模型的 RRF exposure 影响有限（s2+s4 已经 dominant），cross-family pooled 分析结论稳健。

3. **MMLU γ 略有下降**（0.41→0.35），方向趋向无效应，但变化不大。

4. **模型拟合质量良好**：所有 benchmark 无 divergent transitions，R̂正常，PPP 合理（0.43-0.84）。

结果已保存到 `/root/autodl-tmp/exp006/cross_family_v5/`。

---
