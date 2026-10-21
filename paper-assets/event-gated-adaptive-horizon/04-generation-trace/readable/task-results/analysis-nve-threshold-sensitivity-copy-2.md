# analysis nve threshold sensitivity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_threshold_sensitivity_20260515T144605_result.json`
- **Structured JSON:** [`ccc5a382d646ecfa1a73.json`](../../sessions/cc/ccc5a382d646ecfa1a73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/nve_sensitivity_analysis.md`。核心结论：

**推荐 threshold: Max NVE = 1.95**（F1=0.89, Precision=1.00, Recall=0.80, Accuracy=87.5%）

AUROC = 0.8667（Max NVE strategy），在三种策略中最优。

两个 NVE 检测不到的 failure mode：
- **exp_007_fixed_dt4**：value 和 eval 同时崩到零，NVE 只在 25K 短暂飙升到 1.97 后迅速下降。threshold < 1.97 可以勉强捕获。
- **exp_008c**：唯一的漏检（max NVE=1.23）。critic 相对于糟糕的 eval 保持了校准，NVE 无法单独检测这类 collapse，需要辅助指标（如 eval_return < 50% baseline）。

---
