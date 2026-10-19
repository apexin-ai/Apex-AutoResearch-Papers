# harvest bjb2 28827 completed results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827-completed-results_20260525T053618_result.json`
- **Structured JSON:** [`67939943e4f659f5ca65.json`](../../sessions/67/67939943e4f659f5ca65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有结果已收割。注意：**所有 6 GPU 均已空闲**（0 MiB），s45/s47 实验也已完成。

## 已完成实验

### τ-sweep（K=2 Adaptive Spatial, seed=42）

| τ | SR | trigger_rate | mean_unc | crm_steps/total |
|---|---|---|---|---|
| 0.10 | **0.780** | 0.744 | 0.185 | 22081/29666 |
| 0.15 | **0.800** | 0.412 | 0.186 | 11675/28361 |
| 0.25 (baseline) | **0.800** | 0.201 | 0.186 | 5751/28643 |
| 0.30 | **0.800** | 0.169 | 0.192 | 4810/28467 |

### K=2 Adaptive Spatial 多 seed（τ=0.25）

| seed | SR | trigger_rate | mean_unc |
|---|---|---|---|
| s45 | **0.800** | 0.201 | 0.186 |
| s47 | **0.795** | 0.208 | 0.188 |

### VLA-only Spatial 多 seed

| seed | SR |
|---|---|
| s45 | **0.805** |
| s47 | **0.765** |

### K=2 Mean baseline（seed=42）

| mode | SR |
|---|---|
| vla_only (K=2 mean) | **0.815** |

## 仍在运行

| GPU | PID | 实验描述 | 状态 |
|---|---|---|---|
| 0-5 | — | — | **全部空闲 (0 MiB)** |

所有实验均已完成，服务器完全空闲。

### 关键发现

τ-sweep 结论：τ 从 0.15 到 0.30 几乎不影响 SR（都是 0.80），但 trigger_rate 从 74.4%→41.2%→20.1%→16.9% 大幅变化。τ=0.10 时 SR 略降到 0.78，CRM 过度介入（74.4%）反而有害。τ=0.25 是个好的甜蜜点——20% trigger 就够维持 0.80 SR。

---
