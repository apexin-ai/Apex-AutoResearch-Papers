# fix checker et normalization

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_checker_et_normalization_20260514T144616_result.json`
- **Structured JSON:** [`912e6bf3dc5419fee4bb.json`](../../sessions/91/912e6bf3dc5419fee4bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，结果符合预期。

## 修复结果

### 修改内容
在 `violation_checker_docred.py` 中：
1. **添加 `.strip()`** — 修复前导空格（如 `' TIME'` → `'TIME'`），消除 507 个假阳性
2. **添加 alias mapping** — `PERSON→PER`, `ORGANIZATION→ORG`, `LOCATION→LOC` 等，消除 1108 个假阳性

### 修复后消融表

| Mode | ET% | DR% | RV% | CF% | Entities | Triples |
|------|-----|-----|-----|-----|----------|---------|
| unconstrained | 8.18 | 18.46 | 29.66 | 0.10 | 20171 | 17497 |
| grammar_only | 0.00 | 26.17 | 0.03 | 0.07 | 20150 | 17341 |
| semantic_only | 10.44 | 13.84 | 29.87 | 1.05 | 20185 | 17571 |
| full_s1 | 0.00 | 10.19 | 0.03 | 2.57 | 20218 | 17372 |

### 修复前后对比

| Mode | ET before | ET after | Delta |
|------|-----------|----------|-------|
| unconstrained | 8.18% | 8.18% | 0.00pp |
| grammar_only | 0.00% | 0.00% | 0.00pp |
| **semantic_only** | **18.44%** | **10.44%** | **-8.00pp** |
| full_s1 | 0.00% | 0.00% | 0.00pp |

ET 减少量精确吻合：507 (strip) + 1108 (alias) = **1615**，即 3722→2107。

semantic_only 的 DR 也从 15.05%→13.84% (-1.21pp)，因为 normalize 同样应用于 domain_range pair 匹配，消除了因 `PERSON`/`' PER'` 导致的假阳性 DR violation。CF 从 2.29%→1.05%，因为 `PERSON` 和 `PER` 不再被视为同一实体的冲突类型。

unconstrained / grammar_only / full_s1 的所有指标不变，验证修复的隔离性。

### Alias Map

```python
ENTITY_TYPE_ALIASES = {
    'PERSON': 'PER',     # 1081 instances in semantic_only
    'PEOPLE': 'PER',
    'ORGANIZATION': 'ORG',  # 13 instances
    'ORGANISATION': 'ORG',
    'LOCATION': 'LOC',      # 14 instances
    'NUMBER': 'NUM',
    'NUMERICAL': 'NUM',
    'MISCELLANEOUS': 'MISC',
}
```

剩余 2107 个 ET violations (10.44%) 是真实退化：WORK(823)、EVENT(743)、ETHNIC_GROUP(137) 等——模型生成了 DocRED schema 中不存在的类型，属于论文 limitation。

---
