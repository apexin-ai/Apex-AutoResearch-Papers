# paper fix type3 fonts

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-type3-fonts_20260523T005638_result.json`
- **Structured JSON:** [`bb2166cf8257880c59df.json`](../../sessions/bb/bb2166cf8257880c59df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

```
Phase 1 诊断：15/16 个 PDF 含 Type 3 字体（仅 fig_appendix_ddr_trends.pdf 干净）
  + 额外发现 paper/ 目录下 4 个旧副本也含 Type 3

Phase 2 脚本映射：
  fig1_differential_response.pdf  → charts/gen_fig1.py (远程)
  fig2_framework.pdf              → paper/figures/gen_fig2_framework.py (远程)
  fig3_baseline_comparison.pdf    → charts/gen_fig3.py (远程)
  fig_appendix_cross_temp.pdf     → charts/fig_appendix_cross_temp.py (远程)
  fig_appendix_instruct_ddr.pdf   → scripts/plot_instruct_ddr_comparison.py (远程)
  fig_appendix_nll_distribution.pdf → scripts/plot_nll_distribution.py (远程)
  fig_appendix_umap.pdf           → scripts/plot_umap_appendix.py (远程)
  fig_convergence_dynamics.pdf    → 本地 → 上传 fix_convergence_dynamics.py
  fig_ddr_scatter.pdf             → 本地 → 上传 fix_fig_ddr_scatter.py
  fig_ddr_trajectory.pdf          → 本地 → 上传 fix_ddr_trajectory.py
  fig_transfer_heatmap.pdf        → 本地 → 上传 fix_transfer_heatmap.py
  fig_appendix_confusion.pdf      → 日志恢复 → fix_appendix_confusion.py
  fig_appendix_per_gen.pdf        → 日志恢复 → fix_appendix_per_gen.py
  fig_appendix_violin.pdf         → 日志恢复 → fix_appendix_violin.py
  fig_ddr_holdout_split.pdf       → 日志恢复 → fix_ddr_holdout_split.py

Phase 3 修复：成功 15 个，失败 0 个

Phase 5 编译：0 errors, 36 pages, Conclusion 第 1615 行

Phase 6 验证：Type 3 字体数量 = 0
MD5：b6b4de0bd353470084debd07bd6e0e8b
```

---
