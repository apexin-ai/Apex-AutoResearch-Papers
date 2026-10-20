# analysis roc prf regenerate

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_roc-prf-regenerate_20260527T173221_result.json`
- **Structured JSON:** [`d3b888601de8adcb601c.json`](../../sessions/d3/d3b888601de8adcb601c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**生成结果**：
- `nve_roc_curve.pdf` (art_20260527_debb78) — ROC 曲线，AUROC=1.000，τ=2.0 操作点标记在 (0, 1) 完美分类位置
- `nve_threshold_prf.pdf` (art_20260527_01dc4e) — PRF 曲线，F1=1.00@τ=2.0，separation gap [1.88, 3.78] 绿色阴影标注

**数据集**：N=36 (9 CIVO + 27 No-CIVO)，含 D165 标签修正（009b_s2/008d_s3/018_s1→No-CIVO，008e_v3_s2→CIVO）+ 4 个新增实验（008f_s0=1.69, no_dt_s1=0.88, ch_008a_s0=0.449, ch_008a_s1=0.584，均为 No-CIVO）。CIVO min=3.78, No-CIVO max=1.88, τ=2.0 完美分离。

---
