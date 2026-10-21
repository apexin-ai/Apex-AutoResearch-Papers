# paper abstract intro headline

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_abstract-intro-headline_20260515T190436_result.json`
- **Structured JSON:** [`c381ef5a46348d96889b.json`](../../sessions/c3/c381ef5a46348d96889b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件（abstract.tex、introduction.tex、conclusion.tex）的 headline 数字**已经是 binary F1=0.723**，无需修改。

具体现状：
- **abstract.tex L6**: `binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729])` — 已是 binary metric
- **introduction.tex L25, L34**: 同上，均为 binary F1=0.723
- **conclusion.tex L6**: 同上

检查项：
- 无 7-gen aggregate 数字（0.768）残留 ✓
- 3-class 0.789 仅出现在 results.tex、method.tex、appendix 等正文/附录中，作为 supplementary metric 并附有 gen-0 leakage caveat ✓
- abstract 中未提及 3-class 0.789（空间紧凑，合理） ✓

这三个文件的 D017 更新已完成，不需要额外改动。

---
