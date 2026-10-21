# analysis q1 alpha eff vs ess

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q1_alpha_eff_vs_ess_20260515T064924_result.json`
- **Structured JSON:** [`603ebe796d31cc1a1e91.json`](../../sessions/60/603ebe796d31cc1a1e91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已写入。总结完成的工作：

---

## 分析结论

**α_eff 方法与 ESS 阈值法不等价。** Reviewer 的论断错误。

**根本原因**：Reviewer 假设优化目标是 max_b α_eff(b) s.t. ESS ≥ n_min（此时确实总推到 ESS 边界）。但实际目标是 **inf{b : α_eff(b) ≥ τ}**——最小化干预强度。这是 min-intervention vs max-intervention 的区别。

**实证数据**（51,913 micro-batches）：
- 49.9% clean batch (b=0)
- **20.2% α_eff binding**（α_eff 精确达到 τ=0.8，ESS 有余量）
- 30.0% ESS binding（ESS 触底，α_eff 未达 τ）

**MC 对比**（2000 synthetic batches）：
- 两种方法仅 33.5% 完全一致
- α_eff binding 时，b* 仅为 ESS-only 方法的 45%
- Mean |Δb| = 0.95，Pearson r = 0.64

**回应策略**：强调 b* 是 inf（最小化）语义，τ 有收敛理论基础（ESS 的 n_min 没有），建议加 ESS-only baseline 消融对比。

产出：
- 服务器: `/root/provenance_weight_training/output/analysis/q1_ess_equivalence_report.txt`
- 本地 artifact: `artifacts/q1_ess_equivalence_analysis.md`

---
