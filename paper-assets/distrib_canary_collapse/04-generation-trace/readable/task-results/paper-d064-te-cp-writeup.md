# paper d064 te cp writeup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d064_te_cp_writeup_20260518T141929_result.json`
- **Structured JSON:** [`d491b4864ef047ec9cd2.json`](../../sessions/d4/d491b4864ef047ec9cd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改摘要：

**discussion.tex**：在 `\paragraph{Future work.}` (原 line 114) 前插入了 `\paragraph{Method sensitivity extends beyond parametric tests.}` 段落（现 line 114-120），内容为 TE 0/192 FDR-significant 结果及其对 Claim 3 的扩展。

**appendix.tex**：末尾追加了两个 section：
- `\section{Transfer Entropy Analysis}` (App. `\ref{app:transfer_entropy}`)：TE 表格填入实际数据（12 runs 跨所有 α 的 mean TE 和 mean p-values），所有 pair 均无 BH 显著性。
- `\section{Change-Point Detection Analysis}` (App. `\ref{app:change_point}`)：CP 表格使用 `cp_summary_a075.json` 实际数据，修正了模板中 distinct-3（3.3→3.7）和 perplexity（4.3→4.0）的错误值，同步修正了正文 prose 中 "perplexity at generations~4--5" → "generation~4" 和 ECE/distinct-1 共享 gen 的不准确描述。

---
