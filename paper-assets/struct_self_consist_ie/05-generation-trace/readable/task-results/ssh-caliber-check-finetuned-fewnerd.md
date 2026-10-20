# ssh caliber check finetuned fewnerd

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_caliber_check_finetuned_fewnerd_20260521T185449_result.json`
- **Structured JSON:** [`a1047ff645ebaa8878e8.json`](../../sessions/a1/a1047ff645ebaa8878e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果出来了。

## 结论

### 口径确认
**finetuned FewNERD MV Δ = −2.74pp 用的是 gold-nonempty 口径（n=32565），与 pretrained 一致。**

`recompute_alpha_crit_unified.py` 硬编码 `if len(gold_entities) == 0: continue`，无全量模式。所有 recompute 输出都是 gold-nonempty。

### Finetuned 3-seed 明细（gold-nonempty, n=32565）

| Seed | greedy_f1 | mv_strict_f1 | Δ_SC strict | degen (keyset) | α_crit_eff |
|------|-----------|--------------|-------------|----------------|------------|
| 42   | 0.7914    | 0.7581       | −3.33pp     | 9.1%           | 0.4353     |
| 123  | 0.7913    | 0.7650       | −2.63pp     | 9.2%           | 0.4360     |
| 456  | 0.7915    | 0.7689       | −2.27pp     | 8.1%           | 0.4307     |
| **Mean** | **0.7914** | **0.7640** | **−2.74pp** | **8.8%** | **0.4340** |

### Pretrained 对比（同口径，gold-nonempty, n=32565）

| Model | greedy_f1 | mv_strict_f1 | Δ_SC strict | degen (keyset) | α_crit_eff |
|-------|-----------|--------------|-------------|----------------|------------|
| Pretrained (exp_021) | 0.7910 | 0.7668 | −2.42pp | 10.0% | 0.4396 |
| Finetuned (3-seed mean) | 0.7914 | 0.7640 | −2.74pp | 8.8% | 0.4340 |

### 关键发现

1. **两者口径一致**，都是 gold-nonempty（32565/37648）。无需重算。
2. **−2.74pp 确认正确**：是 3-seed strict MV Δ 均值（−3.33, −2.63, −2.27）。
3. **degen ~13% 有误**：finetuned keyset degeneracy 实际 ~8.8%。13% 可能来自 `recompute_tab_fewnerd_results.json` 中 pretrained 的 `degen_f1_pct`（13.75%），那是 F1-level degeneracy（所有 sample 产生相同 F1），与 keyset degeneracy（所有 sample entity-set 完全相同）是不同定义。

---
