# writing figure1 teaser design

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_figure1_teaser_design_20260527T082825_result.json`
- **Structured JSON:** [`96962965c1eab248c94e.json`](../../sessions/96/96962965c1eab248c94e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计方案已写入 `artifacts/figure1_teaser_design.md` 并注册。

**推荐方案：2-panel "Illusion Revealed"**

- **Panel (a) "Decomposing CAR"**：100%-stacked 水平条形图，4 个 model 各一条 bar，分为 frozen-safe (hatched gray) / genuine-safe (blue) / collision (coral) 三段。Pi0 系列 bar 几乎全灰，Pi0.5 系列无灰，一眼看出 "safety 是假的"。

- **Panel (b) "Raw CAR vs dfCAR"**：grouped 垂直条形图，每个 model 一对 bars (raw vs filtered)。核心视觉焦点：红色大箭头标注 Pi0+A1 从 91.5% 暴跌到 ≈0%，Pi0.5 系列不变。

**放弃 v1 (robot-arm schematic) 的原因**：matplotlib schematic 实现质量难保证，3-panel 信息密度过高，3 秒内难以 parse。新方案用标准 chart 可靠实现，读者沿 "左看 stacked bar → 右看 drop arrow" 路径即可 get message。

尺寸 5.5 × 2.3 inches（CoRL 单栏），CORAL/BLUE 双色系与全文统一。

---
