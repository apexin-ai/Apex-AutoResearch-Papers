# paper fix broken ref hedge

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-broken-ref-hedge_20260522T185328_result.json`
- **Structured JSON:** [`b786f14a1a55b5fe7301.json`](../../sessions/b7/b786f14a1a55b5fe7301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Bug 1 修复**: `results.tex:83` — `fig:feature-drift` → `fig:ddr-trajectory`（两份副本均已修改）

**Bug 2 修复**: `conclusion.tex:7` — "shape is preserved" → "shape is approximately preserved"（两份副本均已修改）

**编译验证通过**:
- 0 undefined references
- `fig:feature-drift` 在 `artifacts/_project/paper/*.tex` 中已完全清除
- 主文 ≤ 8 页 ✓（conclusion 在 page 8，limitations/ethics/references 不计入）
- PDF 已拉回到 `artifacts/_project/paper/main.pdf` 和 `docs/paper/main.pdf`

**注意**: `docs/paper/appendix_feature_distributions.tex` 仍有 `fig:feature-drift`（label + 自引用，lines 3/9），这是 docs 与 artifacts 副本的结构性差异，不影响 artifacts 编译。如需同步可单独处理。

---
