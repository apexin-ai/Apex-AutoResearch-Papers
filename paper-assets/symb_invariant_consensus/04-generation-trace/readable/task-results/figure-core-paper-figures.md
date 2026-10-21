# figure core paper figures

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_core-paper-figures_20260517T172302_result.json`
- **Structured JSON:** [`9e8d0b85a5f1fd83b0ba.json`](../../sessions/9e/9e8d0b85a5f1fd83b0ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图表已生成，输出路径：

| 文件 | 大小 |
|------|------|
| `artifacts/figures/paper/operating_regime.pdf` | 22.8 KB |
| `artifacts/figures/paper/operating_regime.png` | 77.1 KB |
| `artifacts/figures/paper/capability_scatter.pdf` | 39.8 KB |
| `artifacts/figures/paper/capability_scatter.png` | 74.2 KB |

**Figure 1 (operating_regime)**: 8 个 model×domain 条件的散点图，点大小 ∝ √n，4 种模型用不同颜色+marker 区分，y=0 参考线，domain 标签标注，含 size legend。单栏宽 3.25"。

**Figure 2 (capability_scatter)**: 307 个 multi-candidate problem 的散点，绿色=SICA correct，红色=SICA wrong，蓝色菱形=flipped 问题高亮。散点层 rasterized 以控制 PDF 体积。

脚本已同步保存到本地 `scripts/plot_paper_figures_v2.py`。LaTeX 中 `\includegraphics` 指向 `figures/paper/operating_regime.pdf` 和 `figures/paper/capability_scatter.pdf` 即可。

---
