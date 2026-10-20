# code theta fixed recompute

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_theta-fixed-recompute_20260520T185056_result.json`
- **Structured JSON:** [`58e5f4b224d846a0c19a.json`](../../sessions/58/58e5f4b224d846a0c19a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已注册。以下是最终结果：

---

## θ-fixed lz* 重算结果

**θ_fixed = -0.0914**（clean_s1 与 clean_s2 的 θ_MLE 均值）

| Condition | θ_MLE | θ_fixed | lz\*_free | lz\*_fixed | Δlz\*_free | Δlz\*_fixed | θ-shift absorbed |
|-----------|-------|---------|-----------|------------|------------|-------------|-----------------|
| clean_s1 | -0.0987 | -0.0914 | 8.0101 | 7.7977 | +1.0330 | +0.8228 | -0.2102 |
| clean_s2 | -0.0842 | -0.0914 | 5.9440 | 6.1521 | -1.0330 | -0.8228 | +0.2102 |
| contam_15 | 0.1971 | -0.0914 | 3.0046 | **9.9317** | -3.9725 | **+2.9567** | **+6.9292** |
| contam_50 | 0.3703 | -0.0914 | 5.4480 | **15.6424** | -1.5291 | **+8.6674** | **+10.1965** |

## Dose-response 单调性

| 模式 | \|Δlz\*_50\| | \|Δlz\*_15\| | 单调？ | ratio |
|------|-------------|-------------|--------|-------|
| θ-free (MLE) | 1.5291 | 3.9725 | **No** | 0.38 |
| θ-fixed (clean) | 8.6674 | 2.9567 | **Yes** | 2.93 |

## 结论

**θ-fixed 下 dose-response 恢复单调性。** |Δlz\*_50| / |Δlz\*_15| 从 0.38（倒置）变为 2.93（正常递增）。

θ-shift 分别吸收了 contam_15 的 6.93 和 contam_50 的 10.20 个 lz\* 单位的异常信号——contamination 越重，θ_MLE 上移越大，吸收的信号也越多，这就是 free-θ 下信号倒置的直接原因。

---
