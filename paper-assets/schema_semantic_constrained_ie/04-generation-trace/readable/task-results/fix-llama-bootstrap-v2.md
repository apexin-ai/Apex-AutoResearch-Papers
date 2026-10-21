# fix llama bootstrap v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_llama_bootstrap_v2_20260514T224058_result.json`
- **Structured JSON:** [`ed9dc7f91b68b467e91a.json`](../../sessions/ed/ed9dc7f91b68b467e91a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查结果清楚了。按照任务要求，registry alignment 失败，停下来报告。

---

## Registry Alignment 报告

### 问题 1: SciERC unconstrained E-F1 不对齐

| 指标 | 计算值 | Registry 值 | Delta |
|------|--------|------------|-------|
| SciERC U E-F1 | **23.5294%** (TP=484, Gold=1673, Pred=2441) | 23.56% | **0.0306pp > 0.01pp** |
| SciERC U R-F1 | 2.67% | 2.68% | 0.0086pp PASS |
| SciERC S1 E-F1 | 23.4867% | 23.49% | 0.0033pp PASS |
| SciERC S1 R-F1 | 2.54% | 2.54% | 0.0005pp PASS |

只有 SciERC unconstrained 的 E-F1 超出容差，差 0.03pp。可能原因：
- Registry 值由不同的评估脚本计算（D012 fix 前？）
- Entity type normalization 边界 case 差异

### 问题 2: DocRED unconstrained 有 10 条记录 entity text 是 int

```
rec 115: {'text': 1945, 'type': 'TIME'}
rec 393: {'text': 1970, 'type': 'NUM'}
```

Llama 输出年份/数字为 int 而非 string，导致 `docred_sample_stats` 在 `.lower()` 时崩溃。DocRED full_s1 无此问题。

### 需要你决定

1. **SciERC 0.03pp delta**: 放宽容差到 0.05pp 继续跑？还是需要追查 registry 值来源？
2. **DocRED int entities**: 在 Llama 脚本中加 `str()` 转换预处理（不改 compute_bootstrap_ci.py 核心逻辑），是否可以？

---
