# analysis q1 nomarker regex

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q1_nomarker_regex_20260521T184306_result.json`
- **Structured JSON:** [`476b0ed44251edfbe5b7.json`](../../sessions/47/476b0ed44251edfbe5b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### Nomarker 条件 Regex Baseline 结果（n=1190, pass=851, fail=339）

| Baseline | Marker Acc | Nomarker Acc | Delta |
|---|---|---|---|
| **B5 (no_exception_heuristic)** | **99.33%** | **28.49%** | **-70.84pp** |
| B1 (ERROR_tag) | 93.45% | 71.51% | -21.93pp |
| B4 (exception_regex) | 93.61% | **93.61%** | +0.00pp |
| B5b (empty_trace_heuristic) | — | 93.45% | — |

关键发现：

1. **B5 完全崩溃**（99.33% → 28.49%）：nomarker 条件下没有 `[No exception data in trace]` 标记，B5 把所有样本预测为 fail，直接退化为多数类的反面。

2. **B1/B2/B3 退化到多数类** (71.51%)：nomarker 数据中 `[ERROR]` 和 `Traceback` 标签也没有了，这些baseline全部预测 pass，等于多数类准确率。

3. **B4 (exception_regex) 不受影响** (93.61%)：它匹配 trace 文本中的异常类名（`ValueError`, `TypeError` 等），这些在 nomarker 条件下仍然存在于 269 个 fail 样本中。

4. **B5b (empty_trace → pass)** 达到 93.45%：这是 nomarker 条件下最直觉的 heuristic —— 空 trace 判 pass、非空判 fail。但仍有 70 个 fail 样本 trace 为空（无法区分），以及 8 个 pass 样本有异常内容（caught exception）。

**结论**：去掉 marker 后，最强 regex baseline 从 99.33% 骤降到 93.61%（B4），gap vs SFT 从 ~0.5pp 扩大到 ~6.4pp（假设 SFT nomarker 性能类似）。这证明 marker 条件下的 B5 高分确实是 data artifact。

---
