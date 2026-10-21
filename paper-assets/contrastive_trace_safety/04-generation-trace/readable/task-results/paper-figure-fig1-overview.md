# paper figure fig1 overview

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_overview_20260516T234406_result.json`
- **Structured JSON:** [`e8a613d786684986adf9.json`](../../sessions/e8/e8a613d786684986adf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成并注册。

**输出文件**:
- PDF: `artifacts/figures/paper/fig1_overview.pdf` (35 KB, 矢量)
- PNG: `artifacts/figures/paper/fig1_overview.png` (183 KB, 300 DPI)

**图表内容**:
- 左侧: 6 步 Reasoning Trace，括号标注 "Safe reasoning" (Steps 1-3) 和 "Committed" (Steps 5-6)，虚线标注 CP (commitment point)
- 中间: Feature Extraction 分叉为 Hidden State (d=4096) 和 Text Embedding (d=384) 双路径
- 核心高亮: Temporal Windowing (W=15) 加粗蓝色边框 + 浅蓝背景，标注 "+15-30pp coverage" 和 "modality-agnostic"
- 右侧: Probe → Committed / Safe 二分类检测输出

---
