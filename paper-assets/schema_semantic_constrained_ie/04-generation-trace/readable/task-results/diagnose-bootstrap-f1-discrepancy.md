# diagnose bootstrap f1 discrepancy

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bootstrap-f1-discrepancy_20260522T072049_result.json`
- **Structured JSON:** [`568131d7f8ef871f8bb9.json`](../../sessions/56/568131d7f8ef871f8bb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。

## 对比结果

| 维度 | `compute_bootstrap_ci_ft.py` | `violation_checker.py` |
|------|------------------------------|------------------------|
| F1 类型 | micro（全局聚合 TP/gold/pred） | micro（同上） |
| Relation key | `(head.lower().strip(), tail.lower().strip(), type)` | 完全相同 |
| Entity normalization | `scierc_normalize_type` | 相同的 `normalize_type` |
| Relation type normalization | **不做** | **不做**（F1 用原始 type） |
| **parse failure 处理** | **计入 gold，TP=0, pred=0** | **整个样本跳过（continue）** |

## 根因：parse failure 处理不同

**violation_checker.py** (line 142-144):
```python
if parsed is None:
    json_fail += 1
    continue  # 跳过整个样本，gold_rels 不计入分母
```

**compute_bootstrap_ci_ft.py** (`scierc_sample_stats`):
```python
if parsed is None:
    return {"rel_tp": 0, "rel_gold": len(gold_rel_set), "rel_pred": 0}
    # gold 仍然计入分母
```

当 `parsed_output` 为 None 时：
- **violation_checker** 完全跳过该样本，gold relations 不进入 recall 的分母 → recall 偏高 → F1 偏高
- **bootstrap 脚本** 正确地将 gold 计入分母，TP=0 → recall 被惩罚 → F1 更低

这就是 47.15 vs 43.86 的 ~3.3pp 差异来源。

## 结论

**bootstrap 脚本是正确的。** parse failure 应该惩罚模型（pred=0 但 gold 仍在），不应跳过。violation_checker 的 `continue` 逻辑人为抬高了 F1。

## 建议

需要修复 `violation_checker.py`：当 `parsed is None` 时，仍然计算 F1（gold 计入分母，pred 为空）。修复后 registry 的 R-F1 会降到与 bootstrap 一致的 ~43.86。是否要我修？

---
