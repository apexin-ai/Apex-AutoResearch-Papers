# check exp 097 100 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_097_100_status_20260526T075041_result.json`
- **Structured JSON:** [`90ea632100419afad156.json`](../../sessions/90/90ea632100419afad156.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部提取。汇总如下：

---

## 实验状态汇总

### exp_097_cheetah_008d_s3 — **COMPLETED (DEAD)**

| 指标 | 值 |
|------|-----|
| 最终 step | 112K (train), 105K (last eval) |
| eval_return@105K | **61.67** |
| eval peak | 216.6 @ step 15K (之后剧烈波动) |
| civo/ve_ratio@105K | 0.3069 |
| civo/alert | **0.0 (全程无 CIVO 触发)** |
| gate_dt_mean | **2.0 (恒定)** |
| gate_dt_2_frac | **1.0** (100% dt=2, 零熵) |
| checkpoint | `logdir/exp_097_cheetah_008d_s3/latest.pt` (231MB) |

**结论**: C1 trigger 未生效。gate 完全锁定在 dt=2，无任何 horizon 变化。eval_return 极不稳定（peak 216→最终 61），学习曲线崩溃。onset rate 2/3 的假设未验证——gate 始终无变化。

---

### exp_100_walker_008a_s1 — **COMPLETED (DEAD)**

| 指标 | 值 |
|------|-----|
| 最终 step | 112K (train), 105K (last eval) |
| eval_return@105K | **750.59** |
| eval trajectory | 单调递增: 31→169→158→203→306→457→629→687→657→718→751 |
| civo/ve_ratio@105K | 0.3278 |
| civo/alert | **0.0 (全程无 CIVO)** |
| gate_dt_mean | **2.0 (恒定)** |
| gate_dt_2_frac | **1.0** (100% dt=2, 零熵) |
| checkpoint | `logdir/exp_100_walker_008a_s1/latest.pt` (231MB) |

**结论**: 符合 C3 假设——dt_emb 未暴露于 dt>1，预期无 CIVO，实际确认无 CIVO。Walker Walk 学习曲线健康，eval_return 稳步上升至 750.6。

---

### 建议 Registry 更新

**exp_097**:
- status: `COMPLETED`
- conclusion: `NEGATIVE — C1 trigger failed, gate locked at dt=2 throughout. Eval return collapsed (peak 216→final 62). No CIVO detected.`
- metrics: `{eval_return: 61.7, ve_ratio: 0.307, civo_alert: false, gate_entropy: 0.0}`

**exp_100**:
- status: `COMPLETED`
- conclusion: `CONFIRMED — C3 hypothesis validated. No CIVO as predicted (dt_emb unexposed). Healthy learning curve, eval_return 750.6.`
- metrics: `{eval_return: 750.6, ve_ratio: 0.328, civo_alert: false, gate_entropy: 0.0}`

---
