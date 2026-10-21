# fix bootstrap ci entity filter

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap_ci_entity_filter_20260514T184012_result.json`
- **Structured JSON:** [`8ff221114741c3e074f1.json`](../../sessions/8f/8ff221114741c3e074f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

---

## 修复内容

**`compute_bootstrap_ci.py` 的 `docred_sample_stats` 函数（3 处修改）：**

1. **Line 117** — `gold_ent_set`: 移除 `docred_normalize_entity_type()` 调用，使用原始类型（与 registry 的 `posthoc_filter.py` 一致）
2. **Line 127** — `pred_ent_set`: 移除 `DOCRED_VALID_ENTITY_TYPES` filter 和 `docred_normalize_entity_type()` normalization。改为直接 `set((text, type) for e in entities)`，与 registry 完全一致
3. **Line 119-120** — `parsed is None` 时返回全零（之前返回 `ent_gold=len(gold_ent_set)`），匹配 registry 跳过 parse-failure 文档的行为

SciERC 无需修复（bootstrap 和 registry 都使用 normalize+filter 逻辑，已一致）。

---

## Bootstrap CI 结果 (B=10,000)

### DocRED (unconstrained → full_s1)
| Metric | Δ | 95% CI | p-value |
|--------|------|--------|---------|
| **Rel F1** | **+0.50pp** | [+0.23, +0.81] | **<0.001** |
| **Ent F1** | **+1.23pp** | [+0.94, +1.55] | **<0.001** |

### SciERC (unconstrained → full_s1)
| Metric | Δ | 95% CI | p-value |
|--------|------|--------|---------|
| Rel F1 | +0.13pp | [-0.23, +0.58] | 0.58 |
| Ent F1 | -0.03pp | [-0.11, +0.08] | 0.53 |

### Grammar-only Entity F1
**DocRED grammar_only Entity F1 = 59.38%** (P=58.47%, R=60.32%)
- 之前 registry 为 null，现已更新
- grammar_only vs unconstrained: Ent F1 +1.23pp [+0.93, +1.55], p<0.001
- grammar_only 与 full_s1 的 Entity F1 几乎相同（Δ=+0.00pp, p=0.66），说明 entity F1 的提升完全来自 grammar 层的 JSON schema enum 约束

---
