# code exp 004 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_004_v2_20260514T152021_result.json`
- **Structured JSON:** [`0fea168f24d662921908.json`](../../sessions/0f/0fea168f24d662921908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 更新为 DONE，artifact 已注册。

## 结果摘要

**数据**: 551 实例，397 有 gold RE 关系。7 种关系类型分层分析。

**核心发现**:

| 信号 | 最佳 rho 范围 | 说明 |
|------|-------------|------|
| **Voting Confidence** | **0.42–0.64** | 所有类型最强信号 |
| Fleiss Kappa | 0.15–0.37 | 第二梯队 |
| Mean Logprob | 0.08–0.32 | 中等 |
| Soft Jaccard | 0.06–0.22 | 仅 USED-FOR 显著 |
| Exact Match | -0.22–0.12 | 多数类型为负/无效 |

**Bootstrap CI**: SJ 仅对 USED-FOR 显著 (ρ=0.22, CI=[0.11, 0.33])，其余 6 种类型 CI 均含 0。

**Type-filtered voting**: PART-OF 关系的 type-specific voting confidence 达到 ρ=0.69 (CI=[0.50, 0.82])，说明分关系类型设阈值有价值。

**Threshold sensitivity**: VC ≥ 0.7 时覆盖率 17%，但 F1 从 0.373 提升到 0.616，正确率 76%。

**Cross-type comparisons**: 21 对 pairwise SJ ρ 差异均不显著。

产出位于 `/root/autodl-tmp/struct_self_consist_ie/output/exp004v2_re_diagnostic/`（4 个 JSON 文件）。

---
