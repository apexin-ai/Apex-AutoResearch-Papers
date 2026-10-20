# code wikievents per sample fallback

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_per_sample_fallback_20260517T164128_result.json`
- **Structured JSON:** [`cf024afcb2d098d72a55.json`](../../sessions/cf/cf024afcb2d098d72a55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes verified. Here's the complete report:

---

## 修改总结

### 1. 代码修改

**`compiler/type_mask_processor.py`** (3 处修改):

| 行号 | 修改 |
|------|------|
| L36 | 新增 `import logging` |
| L47 | 新增 `logger = logging.getLogger(__name__)` |
| L272 | `__init__` 中新增 `self._fallback_count = 0` |
| L456-479 | `__call__` 内部：整个 batch_idx 循环体包裹在 `try/except Exception`，初始化 `position = FieldPosition.UNKNOWN`，错误时记录诊断日志（step、position、event_type、role、ids_tail、error type+message），不修改 scores（grammar-only fallback） |

**`run_constrained_extraction.py`** (1 处修改):

| 行号 | 修改 |
|------|------|
| L582-585 | `run_single_pass` 中 generate() 后、decode 前：遍历 processors 找 TypeConstraintProcessor，如 `_fallback_count > 0` 则打印统计 |

### 2. 诊断日志格式

```
Semantic fallback step=N pos=POSITION evt=EVENT_TYPE role=ROLE ids_tail=[...last 20 ids...] err=ExceptionType: message
```

### 3. Re-Dry-Run 对比表 (10 docs, Qwen3-8B)

| 指标 | unconstrained | full_s1 (per-step fallback) |
|------|:------------:|:---------------------------:|
| Parse success | 9/10 (90%) | 9/10 (90%) |
| EV (Event Vocab) | 38.5% | **0.0%** |
| RoV (Role Vocab) | 59.8% | **28.6%** |
| AC (Arg Constraint) | 0.0% | 1.9% |
| CF (Cross-Field) | 0.0% | 12.2% |
| Entity F1 | 0.00 | **0.145** |
| Trigger F1 | 0.129 | **0.137** |
| Argument F1 | 0.000 | **0.006** |

### 4. Fallback 触发频率

**0 次**。10 个 doc 全部完成，没有触发任何 per-step semantic fallback。`_GRAMMAR_MASK_THRESHOLD` 安全检查在 mask 层面已经阻止了所有可能导致 assertion error 的情况。try/except 作为安全网存在，未需要实际触发。

### 关键发现

- **EV 从 38.5% 降至 0%**：event type 约束完全消除了 event vocab violations
- **RoV 从 59.8% 降至 28.6%**：显著下降但未完全消除，剩余 28.6% 来自 position detection 未识别到 role 位置的 step（非 fallback 导致，是 detector coverage 问题）
- **之前的 generate-level fallback 导致整个 sample 放弃 semantic masking；现在这不再发生**（per-step fallback 粒度更细，但本次实验中未触发）
- 之前的 full_s1 在 doc 3 崩溃（assertion error），现在 10/10 完成

---
