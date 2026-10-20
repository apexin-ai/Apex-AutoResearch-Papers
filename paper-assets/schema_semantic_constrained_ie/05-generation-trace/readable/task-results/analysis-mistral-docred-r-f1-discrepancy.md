# analysis mistral docred r f1 discrepancy

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral_docred_r_f1_discrepancy_20260516T092032_result.json`
- **Structured JSON:** [`654be36458088fff7f5d.json`](../../sessions/65/654be36458088fff7f5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已找到根因。让我确认一下 posthoc 的 `_str` 函数对 head/tail 的处理（它调用的是 `r["head"].lower().strip()`）。

结果确认了差异来源。以下是完整报告：

---

## 排查结论

### 差异来源

两个脚本计算 R_F1 的关键区别在 **relation matching 策略**：

| | posthoc_filter.py (4.34%) | "strict" 评估 (3.50%) |
|---|---|---|
| **关系匹配** | fuzzy: 精确匹配 → token overlap >80% → Levenshtein ≤2 | 精确字符串匹配 (无 fuzzy) |
| **比较空间** | pred→PID vs gold PID | pred name vs gold name |
| **TP** | 518 | 420 |
| **Delta TP** | +98 来自 fuzzy matching | — |

### 差异 98 TP 的来源（fuzzy match 示例）

Mistral 输出带下划线/省略词的 relation name，posthoc 的 fuzzy 逻辑能匹配到正确 PID：

```
"part_of"           → P361 ("part of")           # underscore vs space
"founded_by"        → P112 ("founded by")
"place_of_birth"    → P19  ("place of birth")
"date_of_birth"     → P569 ("date of birth")
"country_of_origin" → P495 ("country of origin")
"located in administrative territorial entity" → P131 ("located in the administrative territorial entity")  # 少一个 "the"
```

其他 5 组（Qwen/Llama）差异 <0.1pp，因为它们直接输出 P-code 或精确的 relation name，fuzzy matching 几乎不被触发。

### 是否影响其他指标

- **violation rates**: `violation_checker_docred.py` 也使用相同的 fuzzy normalization，所以 RV/DR 违规率是在 fuzzy 基础上计算的（一致）
- **reject_pct**: posthoc_filter 的 rejection rate 同样基于 fuzzy → 一致
- **只有 R_F1 存在两种口径**

### 论文建议

**用 posthoc_filter 的 fuzzy 口径 (4.34%)**，原因：

1. 本文论点是 constrained decoding 的效果（不是评测模型能否记住精确 relation name）。Mistral 输出 "part_of" 而非 "part of" 属于格式差异，不应当作 IE 错误
2. violation_checker 已经用了相同的 fuzzy normalization 来计算违规率——如果 F1 用 strict 而违规率用 fuzzy，两个指标的口径不一致
3. 所有 6 组实验统一用 posthoc_filter 的评估逻辑（对 Qwen/Llama 差异 <0.1pp，不影响结论）

如果 reviewer 质疑，可在 appendix 注明："Relation matching uses case-insensitive normalization with token-overlap (>80%) and edit-distance (≤2) fallback to handle formatting variants (e.g., underscores vs. spaces). This affects only Mistral DocRED (+0.84pp F1); other configurations show <0.1pp impact."

---
