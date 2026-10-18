# eval read v7 2 final gate

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_read-v7_2-final-gate_20260515T223906_result.json`
- **Structured JSON:** [`07e3487dc0b0786f1324.json`](../../sessions/07/07e3487dc0b0786f1324.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v7.2 Final Eval 结果 + Gate 报告

### Key Metrics (eval_imm_v7_2_final.json)

| Metric | eps=0 (clean) | eps=0.01 | eps=0.02 | eps=0.05 |
|--------|:---:|:---:|:---:|:---:|
| action_loss | 0.0130 | 0.0124 | 0.0180 | 0.0299 |
| margin_median | 0.6627 | 0.6701 | 0.6717 | 0.7077 |
| preservation | 1.0000 | 0.9253 | 0.8482 | 0.6597 |
| LED median | 0.1638 | 0.1620 | 0.3232 | 0.7656 |
| kendall_tau | 1.0000 | 0.7795 | 0.5429 | 0.1589 |

- **lipschitz_empirical**: 0.3393
- **lipschitz_spectral**: 1.0672

### Gate 判定 (gate_report_v7_2.json)

| Gate | 数值 | 阈值 | 判定 |
|------|------|------|------|
| **G1**: Margin ratio (IMM/BL median) | **64.25x** | >= 2.0x | **PASS** |
| **G2**: Preservation diff | **+47.46pp** | >= +10pp | **PASS** |
| **G3**: Clean action_loss ratio | **3.19x** (IMM=0.0130 / BL=0.0041) | <= 1.10x | **FAIL** |
| **G4**: LED median | **0.323** | < 1.0 | **PASS** |

### **OVERALL: FAIL**

G1/G2/G4 均大幅通过，但 **G3 严重不通过**：IMM clean action_loss (0.0130) 是 baseline (0.0041) 的 3.19 倍，远超 1.10x 阈值。模型在 importance margin 训练后 clean prediction quality 下降明显。

---
