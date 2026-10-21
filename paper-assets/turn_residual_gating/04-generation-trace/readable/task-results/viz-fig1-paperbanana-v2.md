# viz fig1 paperbanana v2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig1_paperbanana_v2_20260523T050027_result.json`
- **Structured JSON:** [`21e793c63c1ccea011f3.json`](../../sessions/21/21e793c63c1ccea011f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **PNG**: `artifacts/fig1_overview_pb_v2.png` (288 KB, 300 DPI)
- **PDF**: `artifacts/fig1_overview_pb_v2.pdf` (50 KB)

PaperBanana 因 Gemini API 在该服务器上连不通（planner 阶段卡死 2.5 分钟），改用 matplotlib 直接生成。图表包含：

- **(a)** 6 条件 TF vs AR 分组柱状图，SS AR bar 高亮 + 星标，所有 value label 在柱外，8–17× gap 标注
- **(b)** 4 步诊断流程图（圆角框 + 阴影 + 箭头），mathtext 渲染 ✓/× 符号，结论框绿色背景
- **(c)** β-steering 线图，3 数据点 + 填充 + 11× recovery 标注

---
