# viz fig1 overview v3

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig1_overview_v3_20260523T023906_result.json`
- **Structured JSON:** [`f7d4402a45029376eeec.json`](../../sessions/f7/f7d4402a45029376eeec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v3 已生成，两个文件确认存在：
- `fig1_overview_v3.pdf` (37 KB)
- `fig1_overview_v3.png` (183 KB)

三个修复总结：
1. **Panel (b)** — 改为垂直流程图，每步两行（粗体标题 + 结论），步骤间用浅灰箭头连接，最终结论行用浅绿色背景高亮，✓/✗ 右对齐
2. **Panel (a)** — 主图右下角加 inset axes 放大 AR bars（y 范围 0–0.022），主图 AR bar 顶部标注数值
3. **Panel (c)** — 所有数据点标签统一放到点**上方**（`va='bottom'`, `g + 0.03`），β=0 不再与 x 轴重叠

---
