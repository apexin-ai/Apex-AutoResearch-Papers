# figure baseline comparison v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_baseline_comparison_v2_20260520T144802_result.json`
- **Structured JSON:** [`f704a134d795369f845a.json`](../../sessions/f7/f704a134d795369f845a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。

- **脚本**：`/root/gen-depth-fingerprint/scripts/plot_fig3_baseline_v2.py`
- **输出**：`fig3_baseline_comparison.pdf` (19KB) + `.png` (74KB)
- **数据源**：`8gen_table3_v6_unified.json`（pooled LOGO 8-fold binary F1）+ `efficiency_comparison.json`（推理耗时）
- **7 个方法**：4-Det+Surface / DDR 7-Feature (ours, 红色菱形+浅红背景) / 4-Det Ensemble / LM-D Score / Avg Log-Prob / Fast-DetectGPT / Binoculars，按 F1 降序排列，右侧灰色标注推理耗时

---
