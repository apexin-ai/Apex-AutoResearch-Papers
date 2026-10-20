# ssh check docred f1 normalization

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_docred_f1_normalization_20260518T215716_result.json`
- **Structured JSON:** [`ba73a256a46d3f3912a1.json`](../../sessions/ba/ba73a256a46d3f3912a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论清晰了。

## 报告

### 1. F1 evaluator 的关系匹配逻辑

**存在两套评估脚本，逻辑不同：**

| 脚本 | 关系匹配方式 | name→P-code 映射 |
|---|---|---|
| `scripts/compute_metrics.py` (LLaMA 8B) | gold P-code → name，pred name 直接对比 | **反向**：gold 降级为 name，在 name 空间匹配 |
| `scripts/compute_metrics_qwen_unconstrained.py` (Qwen) | 同上 | 同上 |
| `unified_f1_eval.py` | pred name → P-code（含 fuzzy），在 P-code 空间匹配 gold | **正向规范化** |
| `analyze_docred_semantic_only.py` | pred name → P-code（含 fuzzy），在 P-code 空间匹配 gold | **正向规范化** |

### 2. 关键发现

**`compute_metrics.py` 和 `compute_metrics_qwen_unconstrained.py` 的做法是正确的**，但方向与 violation_checker 相反：
```python
# gold P-code → name
rtype_name = RELATION_TYPES.get(rtype_pcode, rtype_pcode).lower().strip()
gold_rel_set.add((r["head"], r["tail"], rtype_name))

# pred 直接用 name
pred_rel_set.add((r["head"], r["tail"], rtype_name))
```
这是 **exact match on name**。没有 fuzzy matching，没有 token overlap，没有 Levenshtein。如果模型输出 `"location"` 而 ontology 中是 `"country"`（P17），这两个 name 就不匹配。

**`unified_f1_eval.py` 和 `analyze_docred_semantic_only.py`** 则在 P-code 空间匹配，用了 fuzzy matching（token overlap > 0.8 或 Levenshtein ≤ 2）。

### 3. 模型实际输出格式

从 `w9_qwen_docred_zs_sampling_r2.jsonl` 可以看到，70B 模型输出的是**自然语言关系名**：
- `"date of birth"`, `"employer"`, `"educated at"`, `"location"`, `"composer"`, `"participant of"`, `"location of formation"` 等

Gold 标注用的是 **P-code**：`P17`, `P27`, `P194`, `P1001` 等。

### 4. 结论

**`compute_metrics.py` 系列不会人为压低 F1**，因为它把 gold 降级到 name 空间匹配。只要 ontology 里 P-code→name 的映射表完整，gold 和 pred 就在同一空间对比。

**但有一个隐患**：`compute_metrics.py` 用的是 **exact string match on name**。如果模型输出的关系名和 ontology 中的 canonical name 有轻微差异（如 `"place of birth"` vs `"place of birth "`，或 `"country"` vs `"country of citizenship"`），就会 miss。`unified_f1_eval.py` 和 `analyze_docred_semantic_only.py` 通过 fuzzy matching 缓解了这个问题。

**实际影响**：取决于哪个脚本的数字进了论文。如果用的是 `compute_metrics.py` 的结果，F1 可能因 exact match 被轻微压低（差异取决于 fuzzy 匹配覆盖多少）。如果用的是 `unified_f1_eval.py` 或 `analyze_docred_semantic_only.py`，则**已做了正确的 name→P-code 规范化（含 fuzzy）**，F1 不会被人为压低。

---
