# maintenance registry cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_registry_cleanup_20260515T200152_result.json`
- **Structured JSON:** [`b70a0bd9ad6ded8bb23a.json`](../../sessions/b7/b70a0bd9ad6ded8bb23a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。Registry 现在没有 RUNNING 或 PREPARING 状态的残留实验。

---

## 清理操作汇总

| 实验 | 原状态 | 操作 | 原因 |
|------|--------|------|------|
| `exp_qwen3_4b_conll_merge_inference_v2` | RUNNING → DONE(killed) | 标记 killed | 与 `exp_qwen3_4b_conll_scs_inference_v2` 完全重复：相同 checkpoint (ckpt-4200 merged)、数据 (conll2003)、seed (42)、全部推理参数 |
| `exp_qwen3_4b_scierc_merge_inference` | PREPARING → DONE(killed) | 标记 killed | 从未启动，已被 `exp_qwen3_4b_scierc_scs_inference` 替代 |

## 问题 2 结论：`exp_scale_qwen3_4b_conll`

**Registry 中不存在此实验。** 关于 SJ_ρ 微差 (0.432 vs 0.422)，registry 中 CoNLL 4B 的两个已完成实验是：

| 实验 | Checkpoint | SJ_ρ (full) | Greedy F1 |
|------|-----------|-------------|-----------|
| `exp_qwen3_4b_conll_scs_inference` (v1) | ckpt-3800 merged | 0.4045 | 0.9251 |
| `exp_qwen3_4b_conll_scs_inference_v2` | ckpt-4200 merged | 0.4217 | 0.9234 |

差异来源：**不同 checkpoint**（3800 vs 4200），同一数据/seed。ckpt-4200 多训练了 ~400 steps，correlation metrics 全面提升 (+1.7pp SJ_ρ)，但 greedy F1 略降 (-0.17pp)。不存在 0.432 的 SJ_ρ 值。

---
