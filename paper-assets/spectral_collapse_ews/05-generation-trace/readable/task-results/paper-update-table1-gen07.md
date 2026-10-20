# paper update table1 gen07

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update_table1_gen07_20260517T111932_result.json`
- **Structured JSON:** [`95efe2a0871540bff4ad.json`](../../sessions/95/95efe2a0871540bff4ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Part A: Table 1 更新**
- `experiments.tex` 表格列从 6 列扩展到 8 列（Gen 0-7）
- Gen 6/7 各指标已填入，格式与已有行一致
- HellaSwag Gen 6-7 标记为 `---`（数据待补）
- σ₁ 值从 JSON 提取：Gen 6 = 758.4, Gen 7 = 791.3

**Part B: Spectral trajectory 图**
- 绘图脚本已更新为 Gen 0-7（8 代），ylim 范围已调整（PPL 上限 42, Log-Det 下限 2280, Eff Rank 下限 440）
- HellaSwag 面板仅绘制 Gen 0-5（现有数据）
- `spectral_trajectory.pdf` (27KB) 和 `.png` (330KB) 已生成到 `paper/figures/`

---
