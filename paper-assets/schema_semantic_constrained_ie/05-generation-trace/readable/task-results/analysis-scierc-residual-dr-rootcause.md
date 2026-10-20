# analysis scierc residual dr rootcause

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_residual_dr_rootcause_20260515T143327_result.json`
- **Structured JSON:** [`151331d21896b627b437.json`](../../sessions/15/151331d21896b627b437.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

### 根因：**CF Registry-Consistent Fallback (W1) — 14/16 violations (87.5%)**

`compiler/type_mask_processor.py:_mask_tail_type` (lines 372–383) 显式编码了以下行为：

```python
if actual_type and actual_type in self._type_first_token:
    if allowed_dr is None or actual_type in allowed_dr:
        return self._apply_type_mask(logits, {actual_type})
    else:
        # W1 registry-consistent fallback
        self._cf_fallback_count += 1
        return self._apply_type_mask(logits, {actual_type})   # ← 绕过 pair-based check
```

当 entity registry 中 tail_text 已登记为类型 T，而 T ∉ σ(r)|head_type 时，代码**故意强制注册类型 T**而非回退到 `allowed_dr` (pair-based)。Docstring 明示设计意图："W1: registry consistency > DR compliance, prevents CF violations"。

**证据**：14/16 violations 中 `tail_type_in_relation` 与 entities section 中该 mention 的类型**完全一致**（如 'syntactic coverage' 登记为 Metric，violation 也是 Metric；'inheritance-based lexica' 登记为 OtherScientificTerm，violation 也是 OtherScientificTerm）。

### 集中度（与 tightness 相关）

| Relation | Violations | σ(r)\|head 大小 |
|---|---|---|
| Evaluate-for, head=OtherScientificTerm | 8 | **1** ({Method}) |
| Feature-of, head=Generic | 6 | **2** ({OST, Task}) |
| Compare, head=Task | 2 | **1** ({Task}) |

100% 的 violations 都集中在 σ(r)\|head ≤ 2 的最紧约束位置——这是 W1 trade-off 最频繁触发的地方（模型词汇偏好与小集合冲突几率最大）。

### 2 个 outliers

- **#2 INTERSPEECH_2008_20_abs_sent5**: tail='mismatch' 不在 entity registry（CF fallback 未触发）。最可能：position detector 未捕获 head_type，allowed_dr 退化到 `valid_tail_types()` (union, 含 Generic)。
- **#9 ECCV_2016_99_abs_sent5**: tail='sliding window design' 登记为 OtherScientificTerm 但输出 Generic。最可能：`_apply_type_mask` 内的 grammar-first safety check（OtherScientificTerm first token 被 XGrammar 标为 < -1e8 → `any_allowed_valid=False` → 跳过 semantic mask）。

### 论文 §5 启示

- 残余 0.93% (16/1729) 不是 bug 也不是 checker 口径不一致——`violation_checker.py` 与 enforcement 使用相同的 `ontology_constraints.json` valid_pairs。
- 这是 **W1 设计的可量化代价**：用 0.93% DR violations 换取近 0% CF violations 在 high-tightness relations 上的可行实现。
- §5 可以直接量化展示：所有残余 DR violations 都在 σ(r)\|head ∈ {1,2} 的 cells；如果禁用 W1 fallback，DR=0 但 CF rate 会上升（可补一个 ablation）。

完整数据已保存至 `outputs/scierc_residual_dr_investigation.json`（含 16 条 violations 的全字段诊断 + cause 标签）。

---
