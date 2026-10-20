# paper figure fig2 training pcgrad

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig2_training_pcgrad_20260519T194759_result.json`
- **Structured JSON:** [`09ec35aed73e89e6f9c1.json`](../../sessions/09/09ec35aed73e89e6f9c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 2 已完成。

**输出文件**:
- PDF: `figures/paper/fig2_training_pcgrad.pdf` (47 KB, 矢量)
- PNG: `figures/paper/fig2_training_pcgrad.png` (238 KB, 300 DPI)

**数据来源**:
- Panel (a): v7 micro-step 日志 (ms 0–1600, 转换为 gs 0–200)，mean_GAR 由 L_GAR 反算 (0.5 − √L_GAR)
- Panel (b): v7 同上 + v9 PCGrad 全局步日志 (gs 0–1100)，L_NTP 的 epoch 级数据 (2.03 → 0.93)

**关键数据验证**:
- Panel (a) GAR 范围 0.016–0.50，符合三阶段描述
- Panel (b) L_GAR 范围 0–0.235，v7 在 gs ~144 收敛，v9 延迟至 gs ~400 开始下降

---
