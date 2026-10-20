# analysis dose response cross seed m035

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose_response_cross_seed_m035_20260520T041622_result.json`
- **Structured JSON:** [`90836bdcb5fa8981ca85.json`](../../sessions/90/90836bdcb5fa8981ca85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**Registry 更新**
- `alpha_sweep_a050_s43_fp32`: PermG=6/8, K≥3=6/8, threshold_3σ=8/8, TY=5/8
- `alpha_sweep_a075_s43`: PermG=5/8, K≥3=7/8, threshold_3σ=8/8, TY=6/8

**Cross-seed 比较**
| α | s42 PermG | s43 PermG | 差异 |
|---|-----------|-----------|------|
| 0.50 | 6/8 | 6/8 | onset 稳健 |
| 0.75 | 6/8 | 5/8 | te→d1 FDR p=0.056 边界 |

ROADMAP 值确认，1-pair 差异来源定位到 te→d1 的 FDR p=0.056。

**Artifacts**
- `dose_response_m035.csv` — 全 α (0.00–1.00) × s42+s43, 所有 12 个 s42 和 7 个 s43 实验均用 batch_analysis.py 重新分析（M035/D105/D111 compliant）
- `dose_response_analysis.md` — 4-regime 结构、method FPR 对比、M037 注意事项

---
