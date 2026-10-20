# analysis nve threshold sensitivity plan034

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_threshold_sensitivity_plan034_20260515T164353_result.json`
- **Structured JSON:** [`321157121db7eb93118b.json`](../../sessions/32/321157121db7eb93118b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**NVE 时间序列**

| 实验 | 类型 | 25K | 35K | 45K | 55K | 65K | Peak |
|------|------|-----|-----|-----|-----|-----|------|
| exp_006 | collapse | — | 1.29 | 1.61 | 2.31 | **4.84** | 4.84 |
| exp_008d | collapse | 1.78 | 1.71 | 2.09 | **4.12** | — | 4.12 |
| exp_008a | stable | — | — | — | 0.93 | 0.66 | 0.93 |
| exp_008e | stable | 1.93* | 0.94 | 0.88 | 0.87 | 0.72 | 0.80 |
| exp_008f | stable | 1.02 | 0.73 | 0.83 | 0.97 | 0.37 | 0.30 |
| exp_009a | stable | 1.62* | — | — | 1.18 | — | 0.98 |

*\* = 早期 transient，后续衰减*

**AUROC = 1.0**（从 55K 步开始，collapse 与 stable 完全可分）

**推荐监控规则（二选一）**
1. **NVE > 2.0 单步即报警** — 零 false positive，55K 检测到
2. **NVE > 1.5 连续 2 个 checkpoint** — 同样零 FP，更早检测（35K-45K）

**实际部署**：两个条件取 OR，从 25K 步开始监控。

Artifact 已注册：`art_20260515_cce925`

---
