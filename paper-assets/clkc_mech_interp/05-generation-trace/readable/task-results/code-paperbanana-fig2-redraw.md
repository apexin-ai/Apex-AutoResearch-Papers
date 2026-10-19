# code paperbanana fig2 redraw

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paperbanana-fig2-redraw_20260526T043636_result.json`
- **Structured JSON:** [`7226f46cbf896701250e.json`](../../sessions/72/7226f46cbf896701250e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出报告

**最终文件路径：**
- PNG: `figures/paper/fig2_pipeline.png`
- PDF: `figures/paper/fig2_pipeline.pdf` + `docs/paper/fig2_pipeline.pdf`

**迭代记录（5 轮）：**

| 轮次 | 改动 | 效果 |
|------|------|------|
| v1 | 初始 intent，基础生成 | 缺双向箭头、缺 Δ_asym、缺 L13 标注、stage 间无连接箭头 |
| v2 | 增加详细组件描述、双向箭头、Δ_asym、L13、subtitles | 全部标注出现，但 stage 间箭头过粗、有垂直分隔带 |
| v3 | 去掉分隔带、加 ZH→EN 金色高亮、优化箭头粗细 | 背景更干净、高亮出现，但 probing grid 颜色太淡 |
| v4 | 强调颜色饱和度、调整连接箭头、紧凑布局 | **最佳版本**——饱和色彩、清晰箭头、全部标注、干净背景 |
| v5 | 修复 "Detection ≠ Decision" 折行、红色 ✗ | 折行修复，但模型名变竖排、Controls 合并成单框，整体不如 v4 |

**最终选择 v4**，视觉评估结论：
- 5 stage 信息密度充足，probing grid 蓝/玫红饱和鲜明
- ZH→EN 金色高亮准确标识核心发现
- 所有关键标注完整（Δ_asym=+7pp、L13 41%、COMET ✓、Detection ≠ Decision）
- 达到顶会论文标准

---
