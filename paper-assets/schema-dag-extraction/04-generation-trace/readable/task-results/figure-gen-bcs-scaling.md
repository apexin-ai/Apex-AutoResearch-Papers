# figure gen bcs scaling

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_gen_bcs_scaling_20260515T231958_result.json`
- **Structured JSON:** [`1e7f13793960ee7f7d8a.json`](../../sessions/1e/1e7f13793960ee7f7d8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完毕。

**输出**: `/root/schema-dag-extraction/figures/paper/fig_bcs_scaling.pdf` (30K, PDF 1.4, 1 page)

**图表结构**: 双 panel 布局
- **(a) BCS Effect Scales with Pool Size** — 折线图，x=pool size (16/40/80)，y=|Δacc| in pp。Qwen2.5-7B 三点连线 + LLaMA-3.1-8B 80-rel 单点。标注 3.4× amplification（仅 16→80，符合 C002）。饱和区阴影显示 40→80 基本持平。
- **(b) Low vs High BCS Accuracy** — 分组柱状图，每个 pool size 一组 low/high BCS bars，标注 Δ 值。

**数据验证通过**:
- 16-rel: 9.1pp, 40-rel: 33.3pp, 80-rel: 31.2pp
- LLaMA 80-rel: 27.1pp
- 40-rel x 轴标注 "(80-pool subset)" 符合 C001

---
