# paper update figures dose response factorial

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update-figures-dose-response-factorial_20260525T065724_result.json`
- **Structured JSON:** [`fd2d2fd0e4883bbb8186.json`](../../sessions/fd/fd2d2fd0e4883bbb8186.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图已生成并注册：

**图 1 — Dose-Response Curve** (`fig_dose_response_2seed.pdf/png`, 21KB PDF)
- 蓝色渐变系表示 early-cutoff（浅→深 = 少→多梯度流），橙色三角为 late-onset reverse_cutoff
- 个体 seed 小圆点散点 + 均值大圆点连线，3-seed 点带 error bar
- Vanilla baseline 灰色虚线

**图 2 — 2×2 Factorial** (`fig_factorial_2x2.pdf/png`, 25KB PDF)
- BN（蓝）vs LN（橙）分组柱状图，error bar = 3-seed std
- Vanilla baseline 虚线，交互效应 p=0.025 标注带 bracket

生成脚本保留在 artifacts 目录下（`gen_dose_response.py`, `gen_factorial_2x2.py`），数据修改后可直接重新运行。

---
