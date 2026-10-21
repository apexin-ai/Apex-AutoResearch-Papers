# ssh eval status and results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-status-and-results_20260520T003516_result.json`
- **Structured JSON:** [`f96d16635e7fbf7b1dec.json`](../../sessions/f9/f96d16635e7fbf7b1dec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 两个 eval 均已完成
- PID 876210 (CLS 8B s456): **已结束**
- PID 876070 (DeepSeek CLS s456): **已结束**

### 2. CLS 8B repo s456 (ckpt-2200)

| Metric | Value |
|--------|-------|
| Accuracy | 84.40 |
| F1 Macro | 76.19 |
| F1 Fail | 62.21 |
| F1 Pass | 90.17 |
| Precision Fail | **90.23** |
| Recall Fail | 47.47 |

### 3. DeepSeek CLS repo s456 (ckpt-2163)

| Metric | Value |
|--------|-------|
| Accuracy | **86.15** |
| F1 Macro | **80.43** |
| F1 Fail | **69.84** |
| F1 Pass | 91.01 |
| Precision Fail | 84.95 |
| Recall Fail | **59.30** |

DeepSeek s456 全面优于 CLS 8B s456：accuracy +1.75pp, f1_macro +4.24pp, recall_fail +11.83pp。CLS 8B 的 precision_fail 更高 (90.23 vs 84.95)，但 recall_fail 很低 (47.47)，偏保守。

### 4. GPU 2 DeepSeek CWM eval
PID 833672 仍在运行，GPU 2 占用 29.6GB/32.6GB, 88% util。

### 5. GPU 空闲状况

| GPU | Memory | Util | 状态 |
|-----|--------|------|------|
| 0 | 0MiB | 0% | 空闲 |
| 1 | 0MiB | 100% | 异常（无显存但满载，可能驱动残留） |
| 2 | 29.6GB | 88% | CWM eval 运行中 |
| 3 | 0MiB | 0% | 空闲 |

GPU 0/3 完全空闲可用，RAM 42Gi/754Gi 充裕。

---
