# eval v7 2 final gate analysis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v7_2-final-gate-analysis_20260515T230441_result.json`
- **Structured JSON:** [`1382d03d943abcf276bb.json`](../../sessions/13/1382d03d943abcf276bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Gate 报告已读取。Registry 中 `mvp_imm_anchor_v7_2` 已有 metrics 字段（含 eval_500batch_soft、bypass_acis、gate_v7_2），内容与本次分析一致，无需再更新。

## Gate Report v7.2 完整结果

### Per-condition 详情

| Condition | Margin Ratio | BL Margin | IMM Margin | Pres Diff | BL Pres | IMM Pres | LED Median |
|---|---|---|---|---|---|---|---|
| eps0.01 | 64.87x | 0.0103 | 0.6701 | +59.00pp | 0.3352 | 0.9253 | 0.162 |
| eps0.02 | 63.21x | 0.0106 | 0.6717 | +51.20pp | 0.3362 | 0.8482 | 0.323 |
| eps0.05 | 64.67x | 0.0109 | 0.7077 | +32.16pp | 0.3381 | 0.6597 | 0.766 |

### Gate 判定

| Gate | Metric | Value | Threshold | Result |
|---|---|---|---|---|
| **G1** | Margin median ratio | **64.25x** | ≥ 2.0 | **PASS** |
| **G2** | Preservation diff | **+47.46pp** | ≥ +10pp | **PASS** |
| **G3** | Clean action loss ratio | **3.19x** | ≤ 1.10 | **FAIL** |
| **G4** | LED median | **0.323** | < 1.0 | **PASS** |

### **OVERALL: FAIL**

G3 失败：clean action loss 0.01301 vs baseline 0.00408，比值 3.19x（阈值 ≤ 1.10）。与 v7 的 3.28x 相比仅微幅改善，lambda 从 0.5 降到 0.2 未能实质解决 clean performance 退化问题。

---
