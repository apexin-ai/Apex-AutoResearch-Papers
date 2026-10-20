# analysis d127 track a csd v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d127_track_a_csd_v2_20260520T095809_result.json`
- **Structured JSON:** [`5d46d41f347c191b5a80.json`](../../sessions/5d/5d46d41f347c191b5a80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D127 Track A 完成。

## 结果摘要

**19 个实验，12 个 α 值 (0.00–1.00)，T=11 代**

### 核心发现：Dissociated CSD Pattern

| | AR(1) trend | Variance trend | Blind zone (α≤0.45) |
|---|---|---|---|
| **Canary metrics** (token_entropy, ece) | τ=0.79–0.82, p<0.001 | τ=0.73–0.88, p<0.001 | 3/4 显著 |
| **Downstream metrics** (distinct_1/2/3) | τ=0.03–0.30, p>0.19 | τ=-0.06–0.12, p>0.63 | 1/6 显著 |

### 解读

1. **Canary 指标确实存在 CSD**：AR(1) 和 variance 随 α 单调增长，甚至在 blind zone 内就可检测到（ece AR(1) blind zone τ=0.71, p=0.014）
2. **Downstream 指标无 CSD**：distinct_1/2/3 的 CSD 指标在全 α 范围内均不显著，与 Class 1 一阶相变预测一致
3. **Onset 跳变**：α=0.45→0.50 处，downstream AR(1) 实际上**下降**（distinct_1: 0.57→0.48），说明 collapse 改变了动力学模式从 "persistence" 变为 "monotone decline"

### 论文意义

这不是简单的 "CSD absent"。Canary/downstream 的分裂支持 **canary-triggered cascade** 机制：canary 通道渐进失稳（二阶类），但下游崩溃是突变的（一阶类）。Truong & Truong (2025) 的 Class 1 预测对 downstream 成立，但 canary 本身在相变前有预警信号。

### 产出文件

- JSON: `artifacts/d127_csd/d127_csd_indicators.json`
- PNG: `artifacts/d127_csd/csd_indicators.png`
- Script: `scripts/d127_csd_analysis.py`

**Caveat**: T=11 天然限制 CSD 检测功效，论文中应作为 limitation 讨论。

---
