# analysis trajectory data compile

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_trajectory-data-compile_20260521T112144_result.json`
- **Structured JSON:** [`3ea1ccbdfbbfc9bd9711.json`](../../sessions/3e/3ea1ccbdfbbfc9bd9711.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入并注册。

产出：`artifacts/trajectory_data_compiled.md` (art_20260521_e457b3)

内容覆盖：
- **Condition 1** (R3-only Seed 1): 11 个 checkpoint (1000–7500)，ckpt-8000 标注 RUNNING
- **Condition 2** (R3-only Seed 2): 7 个 checkpoint (500–3500)，训练仍在继续
- **Condition 3** (SFT ACT): 14 个 checkpoint (1000–8000)，ckpt-8000 仅有 SYCONScore=0.301（来自 parent summary）
- Cross-seed comparison: 3 个重叠步数 (1000/2000/3000) 差异极小 (max Δ=0.01)，确认可复现性
- 所有已知数据点与提供的交叉验证值完全吻合
- Data Gaps 表列出 6 项缺失

---
