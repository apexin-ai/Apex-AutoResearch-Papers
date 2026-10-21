# paper p1e ordinal and ci fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p1e-ordinal-and-ci-fix_20260515T162553_result.json`
- **Structured JSON:** [`1e572fc37e5ef5b7e109.json`](../../sessions/1e/1e572fc37e5ef5b7e109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Task A**: 两份 results.tex（`artifacts/_project/paper/` 和 `docs/paper/`）的 ordinal regression 段落已扩展，新增：
- Binary F1: XGBoost 0.721, CORAL 0.728
- Concordance index: XGBoost 0.821, CORAL 0.810, Frank-Hall 0.825
- 结尾解释：3-class 粒度不足以让 ranking-aware loss 产生优势

**Task B**: related_work.tex 无 CI width 相关描述（grep 确认）。唯一的数值声明是 line 13 的 "per-generator F1 ranging from 0.42 to 0.81"，这是 per-generator F1 范围而非 CI width，与当前 baselines 表一致，无需修改。

**Discussion**: 未新增独立段落——ordinal 不优于 nominal 的解释（3-class 粒度不足）已嵌入 results 段落末句，避免重复。

---
