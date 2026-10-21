# paper narrative audit d034

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_narrative_audit_d034_20260516T012026_result.json`
- **Structured JSON:** [`2d1f44b241b328d8ddc1.json`](../../sessions/2d/2d1f44b241b328d8ddc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`Appendix~\ref{app:truncation}` 只存在于 artifacts 版本（未编译），编译版 `docs/paper/method.tex` 没有这个引用。编译论文无悬空引用问题。

## 最终判定

**编译论文（docs/paper/）叙事一致性全部通过。** 具体结论：

1. **所有描述 VOTA 跨模型 gap（84.45% vs 99.41%）的地方**：全部使用 "trace truncation" / "trace content truncation" / "truncates the trace content"，verdict label 被明确说明是 preserved。✅

2. **描述 DeepSeek full_trace v1 坍塌（28.5%）的地方**（discussion.tex:60）：使用 "truncating the verdict label"，正确描述旧 bug。✅

3. **通用截断说明**（method.tex:32, 77）：使用中性措辞 "truncated to fit" / "truncated from the input content while preserving the complete verdict label"，精确无歧义。✅

4. **artifacts/main_results_tables.tex:85**："v1 collapsed due to label truncation"——这是 v1 旧 bug 的正确描述。✅

**无需修改任何文件。D034 叙事一致性终审通过 ✅**

关于任务提到的 "appendix Table 10 标题 label truncation bug 措辞"：当前编译论文的 appendix 中不存在 Table 10 或包含 "label truncation bug" 的标题。该问题可能已在之前的 audit 中修复，或指的是 artifacts 版本中的 `main_results_tables.tex:85`（"v1 collapsed due to label truncation"），该处描述 v1 旧 bug，措辞正确。

---
