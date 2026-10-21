# paper patch regex debugbench

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_patch-regex-debugbench_20260516T052010_result.json`
- **Structured JSON:** [`2a7ab4a9ca4910e9c9af.json`](../../sessions/2a/2a7ab4a9ca4910e9c9af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，0 错误，12 页（正文 + appendix）。

总结完成的修改：

1. **Abstract** (`main.tex:24`): 新增 DebugBench 跨数据集验证句 — "Cross-dataset evaluation on DebugBench (N=426) confirms that exception dominance generalizes, with exception_only achieving 100% accuracy on an out-of-distribution bug dataset."

2. **Introduction contribution 1** (`introduction.tex:20`): 扩展为包含 DebugBench (100%) 和 regex baseline (6.22pp gap, McNemar p<0.001) 交叉验证引用，增加 `\S\ref{sec:debugbench}` 交叉引用。

3. **Appendix Qwen 全结果表** (`appendix.tex:176`): ae_only S123/S456 从 `---` 改为 `\textit{[TODO]}` placeholder，caption 注明 pending。

4. **Appendix regex 表** (`appendix.tex:473`): 新增 B6 (Error count ≥2, 92.02%) 行，caption 更新，intro 文本 "five" → "six"。

5. **数字一致性**: 全文 27 个关键数字交叉验证通过，无不一致。

---
