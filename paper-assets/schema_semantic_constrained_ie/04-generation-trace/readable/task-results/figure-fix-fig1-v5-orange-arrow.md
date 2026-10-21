# figure fix fig1 v5 orange arrow

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fix-fig1-v5-orange-arrow_20260522T065118_result.json`
- **Structured JSON:** [`8d6861cf2ba035147dae.json`](../../sessions/8d/8d6861cf2ba035147dae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。查看生成的图像：

**改动：**
- **蓝色箭头**：`rad=0.25` → `rad=-0.2`，弧线改为向下弯曲，避开了 TC Processor 区域
- **橙色箭头**：`rad=0.15` → `rad=-0.15`，弧线向下弯曲，远离 Semantic Rules 文字

**已知限制：** 蓝色箭头从 Grammar Automaton 右侧 (x=2.65) 到 Grammar Layer 左侧 (x=5.9) 的任何路径，都会经过 TC Processor (x: 2.95–5.05, y: 3.25–3.67) 或 Semantic Rules (x: 2.95–5.05, y: 2.35–2.77) 的区域——这两个方框填满了两端之间的空间。当前 `rad=-0.2` 选择了经过 Semantic Rules 上方边缘的路径（白色描边保持可辨识度），完全避开了 TC Processor。

**产出文件：**
- `gen_fig1.py`（本地已更新）
- `fig1_framework.png` + `.pdf`（本地 artifacts 目录已更新）

---
