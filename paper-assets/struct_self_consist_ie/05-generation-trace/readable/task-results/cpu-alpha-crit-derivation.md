# cpu alpha crit derivation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_alpha_crit_derivation_20260521T071446_result.json`
- **Structured JSON:** [`4dd427fa474f8e6daa9f.json`](../../sessions/4d/4dd427fa474f8e6daa9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**α_crit = π_MV / (2 − π_MV)**

| Dataset | π_MV | α_crit | α_obs | Gap | SC Δ | SC Effective? |
|---------|------|--------|-------|-----|------|---------------|
| FewNERD | 0.656 | 0.488 | 0.631 | +0.143 | +0.89 pp | **Yes** |
| CoNLL | 0.894 | 0.808 | 0.874 | +0.066 | −1.09 pp | **No** |
| SciERC | 0.614 | 0.443 | 0.607 | +0.164 | +0.76 pp | **Yes** |

关键发现：bound 对所有 3 个数据集都预测 α > α_crit（SC 应有效），但 **CoNLL 违反了这个预测**。原因是 CoNLL 的 degeneracy rate 高达 63%（8 个 sample 产出相同输出），agreement signal 丧失区分力。建议引入 degeneracy-adjusted bound：α_crit_eff = α_crit / (1 − δ)，CoNLL 调整后 α_crit_eff = 2.18 > 1，正确预测 SC 失效。

产出已注册：`artifacts/alpha_crit_table.md`

---
