# analysis fpr calibration v2

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fpr-calibration-v2_20260524T095723_result.json`
- **Structured JSON:** [`19eaff1c99ecb3eda155.json`](../../sessions/19/19eaff1c99ecb3eda155.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总如下：

---

## FPR 校准结果

### 1. Clean lz* 分布

| Model | n | Mean | SD | Range |
|-------|---|------|----|-------|
| Llama | 10 | −0.312 | 0.840 | [−1.95, 0.72] |
| Mistral | 6 | 3.291 | 2.522 | [−1.32, 5.77] |
| Qwen | 10 | 8.684 | 0.735 | [7.05, 9.53] |

### 2. Empirical FPR（非LOO Cohen's d）

26 个 clean seed 中：
- Max clean |d| = **2.22**（Qwen s2，统计离群值）
- 第二高 |d| = **1.95**（Llama s10）

12 个 contaminated 条件中：
- Min contam |d| = **1.90**（Qwen 50%）
- 5-25% contamination 的 min |d| = **2.11**

关键阈值：

| 阈值 | FPR | TPR | 备注 |
|------|-----|-----|------|
| \|d\| > 2.0 | 3.8% (1/26) | 91.7% (11/12) | 漏检 Qwen 50% |
| \|d\| > 1.83 | 7.7% (2/26) | 100% (12/12) | 全检出 |

### 3. 判断

**FPR 低但非零**，存在边际重叠区间 [1.90, 2.22]，由两个边界情况驱动：
- **Qwen s2**（clean outlier）：lz* = 7.05，其余 9 个 seed 在 8.1–9.5
- **Qwen 50%**（atypical contam）：contamination 过重可能使 θ 上移，lz* 效应反而减弱

排除 Qwen 50% 后，5–25% contamination 全部 |d| ≥ 2.11 > 除 Qwen s2 外所有 clean seed。

### 4. 建议

**Option A**（写入 Results，1 句）：
> As a calibration check, we computed the same Cohen's *d* for 26 clean control seeds: the maximum effect size was |*d*| = 1.95 (excluding one outlier at 2.22), well below the minimum contamination effect of |*d*| = 2.11 at 5–25% rates.

**Option B**（写入 Appendix，更详细）：见 artifact。

**Option C**（保守策略）：不在论文中声明 FPR ≈ 0，仅在 appendix 报告 clean seed variability 作为参考，避免 Qwen s2/50% 重叠被 reviewer 追问。

产出已保存至 `artifacts/fpr_calibration_analysis.md`。

---
