# analysis exp quadruped baseline s0 r2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_quadruped_baseline_s0_r2_20260529T105036_result.json`
- **Structured JSON:** [`485b359371368466c275.json`](../../sessions/48/485b359371368466c275.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是终态分析报告。

---

## exp_quadruped_baseline_s0_r2 终态报告

```
eval_return:          83.7  (at 205K, last eval checkpoint)
NVE_final (205K):     4.7×
NVE_trend:            worsening → volatile → partially recovering, never healthy
civo_alert:           yes (4 triggers: 75K, 95K, 125K, 195K)
baseline_health:      unhealthy
```

### NVE 轨迹

| Step | ve_ratio | eval_return | CIVO Alert |
|------|----------|-------------|------------|
| 15K  | 0.1      | 67.0        | —          |
| 25K  | 2.7      | 18.6        | —          |
| 35K  | 4.3      | 25.1        | —          |
| 45K  | 1.1      | 141.7       | —          |
| 55K  | 3.3      | 66.2        | —          |
| 75K  | **6.5**  | 45.8        | **CIVO**   |
| 95K  | **17.4** | 22.5        | **CIVO**   |
| 125K | **6.6**  | 61.3        | **CIVO**   |
| 155K | 7.4      | 52.0        | —          |
| 165K | 9.8      | 39.6        | —          |
| 175K | 3.4      | 119.7       | —          |
| 185K | 3.7      | 108.9       | —          |
| 195K | **4.7**  | 81.4        | **CIVO**   |
| 205K | 4.7      | 83.7        | —          |

### 关键观察

1. **NVE 始终 > 2.0×**（25K 之后从未降回健康区间），与 D180 @ 125K 的判定一致
2. **峰值 NVE = 17.4×**（95K），对应 eval_return 最低点 22.5——典型的 value overestimation 崩溃
3. **后半段（175K-205K）NVE 稍收敛至 3.4–4.7×**，但仍远超 2.0× 阈值
4. **eval_return 极不稳定**：范围 18.6–217.4，无收敛趋势。最终 83.7，value_mean 却高达 392.9（5× 高估）
5. **4 次 CIVO 告警**，最后一次在 195K，说明 value overestimation 问题贯穿整个训练
6. 训练正常结束（EXIT_CODE=0），共 ~212K env steps，无 W&B 记录

**结论**：Quadruped Walk baseline (dt=1, no gate) 在 200K steps 确认 unhealthy，NVE_final = 4.7× >> 2.0× 阈值，与 D179/D180 中期判定一致。

---
