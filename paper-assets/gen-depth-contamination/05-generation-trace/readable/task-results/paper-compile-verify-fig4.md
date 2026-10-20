# paper compile verify fig4

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile-verify-fig4_20260523T175408_result.json`
- **Structured JSON:** [`6cdd6ceeda0a3d28f290.json`](../../sessions/6c/6cdd6ceeda0a3d28f290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Page 6 captured. Here's the verification:

1. **Figure 4 位置**: 在第 6 页左栏中部，✓
2. **两个面板**: 可以看到两个 heatmap 面板（accuracy 和 retention），✓
3. **4 个模型**: 图中有 4×4 的 heatmap 格子，caption 提到 "continuation-mode models"，行列对应 4 个模型，✓
4. **Caption**: "Cross-model transfer heatmap (continuation-mode models). Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by its in-domain accuracy (retention rate); Pythia=OLMo: 90–92%" ✓
5. **字号**: heatmap 内的数值和轴标签在 200 dpi 下清晰可读，✓

Figure 4 渲染正确，v1 版本（6-class ordinal accuracy + retention，4 模型 heatmap）已确认。PDF 保存在 `artifacts/paper_compile_fig4_verify.pdf`，截图在 `artifacts/page_check_fig4/page-06.png`。

---
