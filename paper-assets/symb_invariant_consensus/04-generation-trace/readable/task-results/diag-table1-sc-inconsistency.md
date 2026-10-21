# diag table1 sc inconsistency

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_table1-sc-inconsistency_20260519T041626_result.json`
- **Structured JSON:** [`f6bb9c797e873970b855.json`](../../sessions/f6/f6bb9c797e873970b855.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因找到了。对比两处 SC tie-breaking 实现：

**exp-026** (`baselines/self_consistency.py:21`):
```python
best_answer = max(groups, key=lambda k: len(groups[k]))
```
平局时返回 dict 中**第一个出现的 key**（取决于 traces 中答案出现顺序）。

**exp-031** (`scripts/run_exp031_oracle_folio_regen.py:353-354`):
```python
candidates = sorted(answer_counts.keys())   # 字母序
sc_answer = max(candidates, key=lambda a: answer_counts[a])
```
平局时返回**字母序最小的**（False < True < Unknown）。

验证 4 个平局题：

| 题目 | 票型 | exp-026 (首次出现序) | exp-031 (字母序) | GT |
|------|------|---------------------|-----------------|-----|
| folio_0 | 4:4:4 (F/T/U) | True | **False** | Unknown |
| folio_123 | 6:6 (U/F) | Unknown | **False** | **False** |
| folio_41 | 6:6 (U/T) | Unknown | **True** | False |
| folio_84 | 6:6 (T/F) | True | **False** | Unknown |

folio_123 正是造成差异的题：exp-031 字母序 tie-break 碰巧选中正确答案 False，exp-026 没有。

---

**产出总结：**

1. **exp-026 精确 SC**: 153/204 = 75.00%
2. **exp-031 精确 SC**: 154/204 = 75.49%
3. **差异原因**: tie-breaking 实现不同。`self_consistency.py` 按 trace 出现顺序 break tie，`run_exp031_oracle_folio_regen.py` 按字母序 break tie。4 个平局题中 folio_123 (Unknown vs False, gt=False) 导致 1 题之差。
4. **建议统一值**: 应统一 tie-breaking 为字母序（deterministic、可复现），Table 1 中 Qwen2.5-14B FOLIO-204 SC 报 **75.49% (154/204)** 或 **75.00% (153/204)** 取决于选哪种策略，但两种策略的结果都应一致。推荐修复 `self_consistency.py` 中的 `max(groups, ...)` 为 `max(sorted(groups.keys()), key=...)` 后统一为 **75.49%**，或者更严谨地报 **75.00%**（原始实验跑出的值），并在 exp-031 重跑 SC 以保持一致。

---
