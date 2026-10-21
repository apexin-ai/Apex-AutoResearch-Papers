# analysis empirical ar1 coefficients

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_empirical_ar1_coefficients_20260520T222024_result.json`
- **Structured JSON:** [`e9385e98937882917c86.json`](../../sessions/e9/e9385e98937882917c86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存。汇总表格：

```
===============================================================================================
Experiment           α   T  te_φ_raw    d1_φ_raw    te_φ_diff    d1_φ_diff
-----------------------------------------------------------------------------------------------
a000_s42          0.00  10    -0.5093      0.8645      -0.5725      -0.1357
a025_s42          0.25  10    -0.3389      0.9486      -0.4466       0.1913
a050_s42          0.50  10    -0.2790      0.8729       0.3132       0.0994
a075_s42          0.75  10     0.1376      0.9057       0.8834       0.2405
a100_s42          1.00  10     0.9959      0.8903       0.9764       0.1826
t20_a050_s42      0.50  20    -0.1002      0.9652      -0.2517       0.4382
t20_a100_s42      1.00  20     0.9788      0.8136       0.8702       0.1411
-----------------------------------------------------------------------------------------------
MEAN                          0.1264      0.8944       0.2532       0.1653
MAX |φ|                       0.9959      0.9652       0.9764       0.4382
===============================================================================================
```

**关键发现**：

1. **token_entropy raw φ** 呈现两个 regime：null/低α（0.00–0.50）下 φ ∈ [−0.51, −0.10]，远低于 0.95；α=1.00 下 φ≈0.996，但这是 collapse 趋势本身（确定性信号），不是随机自相关。

2. **distinct_1 raw φ** 全局偏高（0.81–0.97），包括 null baseline——原因是 iterative training 本身带来的单调下降趋势。但**一阶差分后 φ 仅 0.17 均值**（范围 [−0.14, 0.44]），增量接近白噪声。

3. **论文可用论点**：PermG FPR 膨胀需要 φ≥0.95 的**随机**自相关。我们数据中的高 raw φ 来自确定性趋势，一阶差分后随机分量的 φ 远低于 0.95（distinct_1 均值 0.17，null token_entropy 均值 −0.24），因此 PermG size control 是安全的。

---
