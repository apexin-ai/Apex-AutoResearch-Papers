# paper figure fig scaling

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_scaling_20260517T142547_result.json`
- **Structured JSON:** [`2718b33e4af3a28fd138.json`](../../sessions/27/2718b33e4af3a28fd138.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

fig_scaling 已生成并注册 (`art_20260517_d17d53`)。

输出文件:
- PDF: `figures/paper/fig_scaling.pdf`
- PNG: `figures/paper/fig_scaling.png`

视觉检查结果:
- 4 组 grouped bars 清晰区分，4B 组有红色背景高亮，视觉上 with-evidence bar (39.7) 明显矮于 no-evidence bar (47.2)
- 1.7B 组反转效果明确：蓝色 bar 高于灰色 bar，+8.0pp 绿色粗体标注醒目
- Qwen3-8B no-evidence bar 用半透明虚线边框标记为占位值，附 "(eval running)" 注释
- LLaMA-3.1-8B 两个 bar 接近等高，-0.7pp 灰色标注
- 配色、字号、spine 移除、grid 样式均符合要求

---
