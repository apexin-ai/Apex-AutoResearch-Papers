# code plan004 asv v3 rejection fix

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan004-asv-v3-rejection-fix_20260520T134535_result.json`
- **Structured JSON:** [`6b566bddc2544238e0c6.json`](../../sessions/6b/6b566bddc2544238e0c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

## 修改内容
- **文件**: `/home/sonny/causal_annot_error_attrib/plan_004_asv_v3_fixed.py`（新建，未覆盖旧文件）
- **核心修复**: Part 5 rejection filter 从 magnitude ASV 改为 significance-based ASV（v2 逻辑）
  - `compute_signif_asv_fast(tau_curve, deltas, se)`: 找 min δ 使 |plim τ̂(C(δ))| < 1.96×SE
  - Filter: reject if p<0.05 AND (signif_ASV is None OR signif_ASV > 1)
- **Magnitude ASV**: 仅报告，τ=0 返回 0.0（不再是 None）
- **Part 6**: 新增论文格式 aggregated summary table

## 关键结果

| Topology | τ | naive Type I | **ASV Type I** | naive Power | **ASV Power** |
|----------|------|-------------|----------------|-------------|---------------|
| Confounding | 0.05 | 100% | **0%** | 100% | **100%** |
| Mediation | 0.05 | 100% | **0%** | 100% | 0%* |
| Collider | 0.05 | 37.8% | **0%** | 39-94% | 0%* |
| Confounding | 0.10 | 100% | **0%** | 100% | **100%** |
| Mediation | 0.10 | 100% | **0%** | 100% | **100%** |
| Collider | 0.10 | 37.8% | **0%** | 100% | **100%** |

*τ=0.05 mediation/collider power=0%：效应太小，即使 δ=0（无误差）也 barely significant（SE 较大），ASV 保守但正确地阻止了 reject。

---
