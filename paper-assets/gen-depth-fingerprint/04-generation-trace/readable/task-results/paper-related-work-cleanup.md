# paper related work cleanup

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related-work-cleanup_20260515T175029_result.json`
- **Structured JSON:** [`5463310f8fb7ff41a0bf.json`](../../sessions/54/5463310f8fb7ff41a0bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修复完成，已同步到 `docs/paper/`。

**问题清单：**

| # | 位置 | 问题 | 修复 |
|---|------|------|------|
| 1 | line 8 | "shape-based measures" — 孤立术语，全文其他地方均未使用 | → "distributional features"，与 method/results 用语一致 |
| 2 | line 13 | "per-generator F1 ranging from 0.42 to 0.81" — 与当前 Table 5 不符（binary F1 实际范围 0.524–0.712），且原引用 `\S\ref{}` 指向无表格的小节 | → "binary F1 from 0.52 to 0.71 across individual baselines; Table~\ref{tab:baselines}"，引用改为具体表格 |

**验证通过项：**
- 全部 29 个 `\cite{}`/`\citet{}` key 均存在于 references.bib
- `\S\ref{sec:results-baselines}` 指向 results.tex:110，label 存在
- 无 novelty overclaim（line 15 明确说 "not a new detection method"）
- framing 一致：6 generators / 3 families / base models / LOGO / diagnostic tool

---
