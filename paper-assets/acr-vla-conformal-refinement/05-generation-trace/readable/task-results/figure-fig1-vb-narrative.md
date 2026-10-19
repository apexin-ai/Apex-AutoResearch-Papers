# figure fig1 vB narrative

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1-vB-narrative_20260524T091315_result.json`
- **Structured JSON:** [`8284b6313d20432b83d7.json`](../../sessions/82/8284b6313d20432b83d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出已注册。

---

**视觉检查报告**

| 轮次 | 来源 | 结果 |
|------|------|------|
| Round 1 | PaperBanana intent v1 | **废弃** — 生成了完全无关的 "Data Fragmentation" 图，内容、指标全错 |
| Round 2 | PaperBanana intent v2 (强调 robotics 领域) | **内容正确**：三行布局、pipeline pills、指标卡均匹配。缺少 Row 2 gauge 图标，Adaptive Gate 无双色 |
| Round 3 | PaperBanana intent v3 (详细样式) | **最佳版本** (iter 2)：颜色更精致，结果面板三角标记 ▲ 到位，比例更协调。iter 3 时 critic 崩溃 |
| Round 4 | PaperBanana intent v4 (gauge 强调) | **崩溃** — stylist 返回 None，未生成图像 |

**最终版本 (Round 3 iter 2) 评估：**
1. **高级感**: 7.5/10 — 专业、干净，接近顶会水准但非 best paper 级
2. **三行布局**: ✅ 清晰，Row 1 叙事流 Problem→Solution→Result 顺畅
3. **Row 2 insight strip**: ⚠️ 文字正确，但缺少 semicircular gauge 图标（PaperBanana 图像生成模型的局限）
4. **Row 3 metric cards**: ✅ 四卡均匀，数字和副标题正确
5. **配色**: ✅ 和谐，红/蓝/绿语义区分明确

**产出文件：**
- PNG: `artifacts/figures/fig1_vB_narrative.png` (2.2 MB, 2752×1536)
- PDF: `artifacts/figures/fig1_vB_narrative.pdf` (3.7 MB, 300 DPI)

---
