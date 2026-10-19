# analysis pi05 crm always on spatial s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-crm-always-on-spatial-s42_20260528T012208_result.json`
- **Structured JSON:** [`0f4cac3c7b4570da6892.json`](../../sessions/0f/0f4cac3c7b4570da6892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

## pi05-crm-always-on-spatial-s42 结果

| 指标 | 值 |
|---|---|
| **Success Rate** | **96.0%** (192/200) |
| **Trigger Rate** | **100%** (22455/22455 steps) |
| **Mean Uncertainty** | 0.1096 |
| **Mean Correction Norm** | 0.200 (maxed out) |

## 与 Pi05 VLA-only baseline 对比

| | VLA-only | CRM always-on | Δ |
|---|---|---|---|
| **Overall** | **97.0%** | **96.0%** | **-1.0%** |
| top_drawer | 95% | 90% | -5% |
| wooden_cabinet | 100% | 95% | -5% |
| 其余 8 tasks | 一致 | 一致 | 0 |

## Conclusion: **success**

CRM always-on 确实降低了 Pi05 的 SR（97% → 96%，Δ=-1%），验证了"CRM always-on harmful"假设。但降幅远小于 SmolVLA（SmolVLA Spatial CRM always-on 约 76-79% vs baseline ~83%，Δ ≈ -4~7%）。

原因：Pi05 本身在 Spatial 上已接近 ceiling（97%），且 correction_norm 被 cap 在 0.2，对强模型的干扰有限。降幅集中在两个较难 task（top_drawer、wooden_cabinet），其余 8 task 无变化。

对 Table 2 的意义：Pi05 CRM always-on 在 Spatial 上仍然有害，与 SmolVLA pattern 一致，支持 MC3 cross-VLA claim（conformal gating 的必要性跨 VLA 成立）。

---
