# cpu d220 proposition fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_d220_proposition_fix_20260521T085641_result.json`
- **Structured JSON:** [`da18dd2effb8c12dee4e.json`](../../sessions/da/da18dd2effb8c12dee4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。总结：

**修正内容：SC Δ 定义错误**

| | 旧定义 (θ2n−greedy) | 新定义 (MV−greedy) | Empirical |
|---|---|---|---|
| FewNERD | +0.89 pp | **−9.21 pp** | Yes → **No** |
| CoNLL | −1.09 pp | **−1.37 pp** | No → No |
| SciERC | +0.76 pp | **−3.03 pp** | Yes → **No** |

**关键变化**：旧表显示 2/3 数据集验证 bound，1/3 违反（CoNLL）。修正后 **全部 3 个数据集都违反** — SC（MV 聚合）对 NER 普遍失败。这反而强化了论文论点：

1. Degeneracy-adjusted bound 仍可解释 CoNLL（δ=63% → α_crit_eff=2.184>1）
2. FewNERD/SciERC 失败的原因是 entity-level span mismatch — MV 聚合引入了单个 sample 中不存在的错误
3. Sample-level selection（LP +1.36pp on FewNERD）仍然有效，因为保持了 span 内部一致性

α_crit 公式、π_MV、α_obs、degeneracy 等其他值均无误，仅 Δ_SC 列和 Empirical 列有变。两个文件已注册：`alpha_crit_table.md`（覆盖）+ `d220_correction_notes.md`（新建）。

---
