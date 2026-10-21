# fix crossseed table audit and fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_crossseed_table_audit_and_fix_20260519T024119_result.json`
- **Structured JSON:** [`36027ce3b4bf97603200.json`](../../sessions/36/36027ce3b4bf97603200.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

论文中**不存在**包含这 12 个数据点的 cross-seed 表格。用户提供的数值（93.61, 96.00, 97.65 等）与论文中任何现有表格或 registry 中的数据都不匹配。

以下是论文中实际的 cross-seed 数据：

**exception_only 条件（registry 数据）：**

| 模型 | seed42 | seed123 | seed456 | Mean ± Std |
|------|--------|---------|---------|------------|
| Qwen-7B | 99.83 | 99.83 | 99.83 | 99.83 ± 0.00 |
| DeepSeek-6.7B | 99.33 | 91.09 | 99.33 | 96.58 ± 4.76 |
| Qwen-1.5B | 99.83 | — | — | — |
| CodeLlama-13B | 99.83 | 100.0 | RUNNING | — |

**nomarker 消融（Qwen-7B only）：**

| seed42 | seed123 | seed456 | Mean ± Std |
|--------|---------|---------|------------|
| 96.55 | 98.32 | 98.07 | 97.65 ± 0.96 |

用户提供的 12 个"正确值"（Qwen-7B: 93.61/96.00/97.65, DeepSeek: 93.95/95.04/96.10, Qwen-1.5B: 95.63/97.65/96.72, CodeLlama: 98.24/98.24/98.24）在论文 .tex 文件和 registry 数据中**均不存在**。这些值与任何已知的实验条件都不对应——不是 exception_only，不是 nomarker，也不是任何其他条件。

**结论：论文中没有需要修正的 cross-seed 表格。** 用户提供的数据点可能来自一个尚未创建的表格，或者是对某个不同实验的混淆。请确认这些数据点对应的具体实验条件和表格标签。

---
