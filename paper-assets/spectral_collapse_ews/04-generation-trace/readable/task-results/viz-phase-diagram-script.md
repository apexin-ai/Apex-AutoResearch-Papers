# viz phase diagram script

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_phase-diagram-script_20260518T134300_result.json`
- **Structured JSON:** [`e34f74fbf125a8921cd2.json`](../../sessions/e3/e34f74fbf125a8921cd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成完毕，效果符合预期：

- **r=0 (红)**: Gen 0-10 完整数据，先升后降，清晰的 spectral collapse 趋势
- **r=0.5 (蓝)**: Gen 0-10 完整数据，持续上升，mixing 有效稳定了 SLV
- **r=0.2 (橙)**: Gen 0-2，目前只有 3 个点
- **r=0.3 (绿)**: Gen 0-1，目前只有 2 个点

脚本位置和输出：
- 脚本: `/root/spectral_collapse_ews/scripts/plot_phase_diagram.py`
- PDF: `/root/spectral_collapse_ews/figures/phase_diagram.pdf`
- PNG: `/root/spectral_collapse_ews/figures/phase_diagram.png`

脚本从 JSON 动态读取，r=0.2 和 r=0.3 实验推进后重跑即可自动更新。Legend 放在左下区域不遮挡数据线，r=0.3 的短线段也能在图上看到（gen 0-1 附近绿色三角）。

---
