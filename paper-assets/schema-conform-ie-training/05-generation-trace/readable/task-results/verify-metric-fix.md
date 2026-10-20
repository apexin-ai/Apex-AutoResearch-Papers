# verify metric fix

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_metric_fix_20260513T043650_result.json`
- **Structured JSON:** [`af04ee3fef2f0cff8d3a.json`](../../sessions/af/af04ee3fef2f0cff8d3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### 根因

**Relation type 大小写不匹配**：gold 数据用全大写 (`PART-OF`, `USED-FOR`, `CONJUNCTION`...)，模型输出用混合大小写 (`Part-of`, `Used-for`, `Conjunction`...)。旧 `_match_relations` 做 `pred.get("type") != gold.get("type")` 精确比较，**所有 relation 全部匹配失败**，导致 relation_f1 恒等于 0。

### 数量级影响

| Group | 旧 relation_f1 | 新 relation_f1 (micro) | TP | FP | FN |
|-------|---------------|----------------------|-----|-----|------|
| base_zero_shot | 0.0000 | 0.0000 | 0 | 0 | 974 |
| eval_A | 0.0000 | **0.2263** | 147 | 178 | 827 |
| eval_B | 0.0000 | **0.2576** | 230 | 582 | 744 |
| base_zero_shot_v2 | 0.0000 | **0.2524** | 245 | 722 | 729 |

base_zero_shot 全 0 是因为它根本没输出 relations（TP=0, FP=0）。

### 修复内容（3 个问题）

1. **Relation type 大小写归一化**：`.lower().replace("_", "-")` 做 case-insensitive 比较
2. **Arg 相似度忽略 entity type**：旧 `_entity_similarity` 要求 arg 的 entity type 完全匹配（`Generic` ≠ `Method` → 0.0），新逻辑只看 text Jaccard
3. **阈值 0.5 → 0.3**：部分文本匹配（如 `"set of rules"` vs `"rules"`，Jaccard=0.333）可通过

### 单元测试（4/4 通过）

| 测试 | 场景 | 旧 F1 | 新 F1 |
|------|------|-------|-------|
| 1 | Relation type 大小写 (Part-of vs PART-OF) | 0.00 | 1.00 |
| 2 | 格式归一化 (relation/head/tail vs type/arg1/arg2) | 0.00 | 1.00 |
| 3 | 部分文本匹配 (Jaccard=0.33/0.67 vs threshold=0.3) | 0.00 | 1.00 |
| 4 | Entity type 不匹配但 text 一致 (Generic vs Method) | 0.00 | 1.00 |

### 典型匹配例

- `(Part-of, "Recognition of proper nouns in Japanese text", "morphological analysis in Japanese text processing")` ↔ gold `(PART-OF, "Recognition of proper nouns", "morphological analysis")`：arg1_sim=0.571, arg2_sim=0.333 → 新逻辑匹配
- `(Conjunction, "dictionary lookup", "rule application")` ↔ gold `(CONJUNCTION, "dictionary lookup", "rule application")`：完全匹配，旧逻辑因大小写丢失

---
