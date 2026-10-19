# code diag gru probe

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diag_gru_probe_20260516T193950_result.json`
- **Structured JSON:** [`15ffaebcb5308ee9a603.json`](../../sessions/15/15ffaebcb5308ee9a603.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRU Probe 结果 — conclusion: **negative**

### Test 指标

| 指标 | GRU | Temporal LR (w=15) | Static LR |
|------|-----|---------------------|-----------|
| Step Acc | **0.8305** ± 0.186 | 0.8478 | 0.8172 |
| Crossing Rate | 67.4% | **76.7%** | 46.5% |
| Lead Mean | **-0.2** | -1.1 | -2.0 |
| Lead Median | **-1.0** | -2.0 | -2.0 |
| Positive Lead | 10/29 (34.5%) | — | — |

### 关键判据

**Lead time 仍为负值。** GRU 将 mean lead 从 -1.1 提升到 -0.2，方向正确但未突破零点。34.5% 的 trace 有正 lead，但 std=13.0 方差极大，不可靠。

### 训练行为
- Early stopping at epoch 14（patience=10），验证集 lead 一度达到 +5.2 但测试集未复现
- 1.6M 参数的 GRU 在 125 条训练 trace 上快速过拟合（train acc 98.9% vs test 83.1%）

### 含义
单层表示 + 序列建模不足以实现可靠的提前预警。下一步可能需要：多层融合、对比学习特征、或更大的训练集。

---
