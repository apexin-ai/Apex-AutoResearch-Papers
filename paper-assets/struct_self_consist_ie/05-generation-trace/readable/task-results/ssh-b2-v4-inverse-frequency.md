# ssh b2 v4 inverse frequency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b2-v4-inverse-frequency_20260520T115649_result.json`
- **Structured JSON:** [`74a932365d7c352298da.json`](../../sessions/74/74a932365d7c352298da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有结果已保存到 `artifacts/b2_v4_inverse_freq/`（results.json + summary.md）。

## 关键结果：Fold 3 (FewNERD 跨域泛化)

| 版本 | XGB AUC | LGB AUC | ECE (LGB) | Best F1 Δ vs Greedy |
|------|---------|---------|-----------|---------------------|
| B2 orig | 0.8282 | 0.8335 | - | - |
| B2-v2 (joint) | 0.8603 | 0.8477 | 0.1357 | -0.008 |
| B2-v3 (invariant) | 0.8518 | 0.8562 | 0.1373 | -0.010 |
| **B2-v4 replace** | 0.8224 | 0.8340 | 0.2188 | -0.013 |
| **B2-v4 augment** | 0.8554 | 0.8541 | 0.1934 | -0.009 |

## 分析

**Variant A (replace)** 失败 — 直接替换 ac/vc/sj 为 IFW 版本导致 AUC 全面下降，ECE 恶化。IFW 破坏了原始特征的判别力。

**Variant B (augment)** 表现中性偏积极 — LGB AUC 0.8541 略优于 v2 的 0.8477 (+0.006)，接近 v3 的 0.8562。但 ECE 恶化（0.19 vs 0.14），F1 delta 仍为负。

**Feature stability 分析验证了 IFW 假设的部分有效性**：
- `ac_ifw` cross-domain std: 0.110 vs `agreement_count`: 0.122（降低 10%）
- `sj_ifw` cross-domain std: 0.063 vs `sj`: 0.138（降低 54%）
- 但代价是均值相关性也下降（`sj_ifw`: 0.22 vs `sj`: 0.55）

**结论**：IFW 确实提高了特征的跨域稳定性，但同时削弱了判别力。作为补充特征（augment）有微弱正效果，但不足以解决跨域 F1 负迁移问题。

---
