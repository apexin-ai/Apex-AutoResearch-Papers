# analysis fix statistical analysis critical

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fix-statistical-analysis-critical_20260520T045526_result.json`
- **Structured JSON:** [`220c56c2b987c39547a2.json`](../../sessions/22/220c56c2b987c39547a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script ran successfully. Output saved to `artifacts/statistical_analysis_output.txt`.

---

## 修正后 Summary Table

| Benchmark | Method | n | Mean | Std | Δ vs VLA | p-value | Sig |
|---|---|---|---|---|---|---|---|
| LIBERO-Spatial | CRM obs_only | 6 | 0.3433 | 0.0137 | +0.0478 | 0.000046 | *** |
| LIBERO-Spatial | VLA-only | 9 | 0.2956 | 0.0113 | — | — | — |
| LIBERO-Long | CRM obs_only | 6 | 0.1750 | 0.0164 | +0.0336 | 0.016373 | * |
| LIBERO-Long | VLA-only | 7 | 0.1414 | 0.0254 | — | — | — |
| LIBERO-Goal | CRM obs_only | 6 | 0.6817 | 0.0343 | -0.0123 | 0.593106 | n.s. |
| LIBERO-Goal | VLA-only | 5 | 0.6940 | 0.0385 | — | — | — |
| LIBERO-Object | CRM norm02 K=10 | 6 | 0.1683 | 0.0183 | +0.0596 | 0.000095 | *** |
| LIBERO-Object | CRM norm01 (supp) | 6 | 0.1750 | 0.0105 | +0.0663 | <0.000001 | *** |
| LIBERO-Object | CRM norm02 K=5 (supp) | 7 | 0.1600 | 0.0216 | +0.0512 | 0.000312 | *** |
| LIBERO-Object | VLA-only | 8 | 0.1088 | 0.0136 | — | — | — |
| LIBERO-Object | Argmin K=10 | 5 | 0.1240 | 0.0288 | +0.0152 | 0.316589 | n.s. |
| LIBERO-Object | Argmin K=5 | 4 | 0.1300 | 0.0163 | +0.0212 | 0.073136 | n.s. |
| LIBERO-Object | Adaptive-K (all) | 11 | 0.1409 | 0.0151 | +0.0322 | 0.000170 | *** |

## 修正内容总结

1. **Object 主配置改为 norm02 (ε=0.2) K=10** — 所有 summary table 和 comparison 中 Object 的 CRM 用 `crm_object` (norm02 K=10)，norm01 降为 supplementary
2. **新增数据**: CRM-Goal seed47=0.69 (n:5→6), VLA-Spatial seed48=0.30/seed49=0.29/seed50=0.30 (n:7→9)
3. **VLA-Long seed48 = 0.14** 已确认
4. **Argmin K=10 seed43 = 0.17**: 在 4 台服务器均未找到原始 JSON，registry 值保留但标注为 unverified outlier

---
