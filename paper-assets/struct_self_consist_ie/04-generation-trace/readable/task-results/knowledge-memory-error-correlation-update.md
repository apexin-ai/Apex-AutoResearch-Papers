# knowledge memory error correlation update

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_memory-error-correlation-update_20260520T014418_result.json`
- **Structured JSON:** [`81cdf9139ca6dacbbba5.json`](../../sessions/81/81cdf9139ca6dacbbba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件均已更新：

**memory.md** — Error Correlation 分析结果已存在（之前的 session 写入），补充了数据源路径 `artifacts/fs_vs_zs_error_correlation.json`。

**report.md** — 近期结论中 exp_qwen25_72b_fewshot 条目已修正：
- 删除 "归因于 demonstration-induced error correlation"
- 替换为：error correlation 分析推翻该假说（FS/ZS Jaccard 无显著差异，entropy 方向相反），LP signal 区分力退化（ρ 0.081→0.060）是更可能的直接原因
- "论文 framing 不需调整" → "论文 Discussion 中该解释需弱化或替换"

---
