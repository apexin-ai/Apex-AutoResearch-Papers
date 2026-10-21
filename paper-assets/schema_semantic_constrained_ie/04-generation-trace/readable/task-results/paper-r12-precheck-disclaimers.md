# paper r12 precheck disclaimers

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r12_precheck_disclaimers_20260520T125228_result.json`
- **Structured JSON:** [`df2beee8a91a2aa34e43.json`](../../sessions/df/df2beee8a91a2aa34e43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，0 errors，32 pages。

**修改 1** — `appendix_prompt_sensitivity.tex:33`
在最后一段末尾追加：
> Schema-informed prompting results serve as an upper bound on zero-shot prompt-level intervention; training-based approaches (e.g., GoLLIE) achieve compliance through code-generation format but with different coverage trade-offs (§\ref{sec:related_work}).

**修改 2** — `appendix_reproducibility.tex:49–52`
在 seed-variance 表格后新增段落：
> \paragraph{Beam search non-determinism.} Greedy decoding is deterministic (§\ref{app:greedy-determinism} above). Beam search ($k{\geq}2$) introduces non-determinism from GPU floating-point accumulation order; we report single-run results. Based on the greedy cross-hardware variance ($\sigma < 0.5$ pp, Table~\ref{tab:seed-variance}), beam search variance is expected to be of similar magnitude.

---
