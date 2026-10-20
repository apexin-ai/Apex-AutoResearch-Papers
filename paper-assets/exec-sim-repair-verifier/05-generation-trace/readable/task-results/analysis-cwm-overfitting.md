# analysis cwm overfitting

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm-overfitting_20260521T075005_result.json`
- **Structured JSON:** [`7798061a5af22c42dae9.json`](../../sessions/77/7798061a5af22c42dae9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。写入 `artifacts/cwm_overfitting_analysis.md` 并已注册。

核心结论：

**过拟合证据强度：中等偏弱**，原因是关键的 same-seed epoch 曲线缺失。

可用数据：
- **s42 within-seed**：epoch 2 partial (66.85%) → epoch 3 (61.49%) = -5.36pp，但 epoch 2 只有 31.2% coverage
- **Cross-seed**：s123-v2 epoch 1 (75.45%) vs s42 epoch 3 (61.49%) = +14pp，但 seed variance 未解耦
- **CLS 对照**：CLS eval_loss 也涨 123%，但 accuracy 仅 -0.1pp → classification formulation 对 overfitting 天然鲁棒，CWM 更敏感

**建议**：方向 A（加强 CWM fails），但用词审慎，等 s123-v3 和 s456-v2 完成后再看 same-seed 曲线是否确认。主表仍用 3-epoch final（与 CLS 公平对比），过拟合现象放 supplementary 讨论。

---
