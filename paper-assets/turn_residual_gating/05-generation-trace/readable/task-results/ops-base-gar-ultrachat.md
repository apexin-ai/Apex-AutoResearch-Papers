# ops base gar ultrachat

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_base_gar_ultrachat_20260519T065444_result.json`
- **Structured JSON:** [`8c53a696fd559d097795.json`](../../sessions/8c/8c53a696fd559d097795.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手。汇总报告：

---

## D017 结果：Base Model GAR on UltraChat

### 1. Base model GAR on ultrachat (ours variant)

| 指标 | 值 |
|---|---|
| Turn 1 avg GAR | 0.0494 |
| Mid-turns avg GAR | **0.0107** |
| Mid-turns avg nGAR | 0.2878 |
| Per-turn nGAR 趋势 | 0.424 → 0.311 → 0.287 → 0.288 |

### 2. Base model GAR on ultrachat (dongre variant)

| 指标 | 值 |
|---|---|
| Turn 1 avg GAR | 0.0122 |
| Mid-turns avg GAR | **0.0030** |
| Mid-turns avg nGAR | 0.1684 |
| Per-turn nGAR 趋势 | 0.217 → 0.162 → 0.160 → 0.177 |

### 3. 对比 Phase1 eval data (standard_conversations, ours variant)

| 指标 | Phase1 eval | UltraChat (ours) | UltraChat (dongre) |
|---|---|---|---|
| Turn 1 avg GAR | 0.0418 | 0.0494 | 0.0122 |
| Mid-turns avg GAR | **0.0122** | **0.0107** | **0.0030** |

### 4. 结论

**UltraChat 训练数据的 base GAR 并未显著高于 eval 数据。** Ours variant 下 ultrachat mid-turn GAR (0.0107) 甚至略低于 phase1 eval (0.0122)。

这意味着 **30x 训练-推理 GAR 断层完全来自 gating/LoRA 过拟合，而非数据分布差异**。Base model 在两种数据上的 GAR 基本处于同一量级（~0.01），排除了"训练数据本身就包含更高 goal attention 信号"的假设。

---
