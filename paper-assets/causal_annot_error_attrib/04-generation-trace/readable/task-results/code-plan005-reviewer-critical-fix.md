# code plan005 reviewer critical fix

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan005-reviewer-critical-fix_20260520T145906_result.json`
- **Structured JSON:** [`f0fe869ac1318889fb60.json`](../../sessions/f0/f0fe869ac1318889fb60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修复版脚本已创建并运行成功。

**修复内容：**
- **C1**: 添加 `compute_signif_asv_fast`（line 423）
- **C2**: `compute_magnitude_asv_fast` 在 τ≈0 时返回 `0.0`（line 409）
- **W1**: IV τ_true 改用 `plim_iv(I)=0.6598`（原为 DGP β=0.5）
- **W2**: M-bias τ_true 改用 `plim_mbias(I)[1]=0.5128`（原为 DGP τ=0.5）
- **Part 5**: 完全重写为 significance-based ASV rejection rule

**关键结果：**

| 拓扑 | Type I (ASV filter) | Power (τ=0.05) | Power (τ=0.1) |
|------|-------------------|----------------|----------------|
| M-bias | **0%** | 95.8–99.2% | 100% |
| IV | **0%** | 0% | 0% |
| Front-door | **0%** | 100% | 100% |

- Type I = 0% 对所有拓扑成立
- IV power=0% 是正确行为：Wald 估计量极度脆弱（signif_ASV≈0），ASV filter 保守地阻止所有拒绝
- 运行耗时 46.2s

**输出文件：**
- `/home/sonny/causal_annot_error_attrib/plan_005_asv_extended_fixed.py`
- `/home/sonny/causal_annot_error_attrib/plan005_fixed_run.log`
- `/home/sonny/causal_annot_error_attrib/plan005_fixed_summary.md`

---
