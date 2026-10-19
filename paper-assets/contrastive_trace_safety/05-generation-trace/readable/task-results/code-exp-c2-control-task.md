# code exp c2 control task

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_c2_control_task_20260516T224705_result.json`
- **Structured JSON:** [`251d518fa7e264b1e24e.json`](../../sessions/25/251d518fa7e264b1e24e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。汇总结果：

## C2 Control Task 结果

### Part A: CP 位置分布
CP 位置方差大 (std=0.29-0.34)，覆盖 [0.02, 0.99] 全范围。虽然中位数在 72-86%，但大量 trace 的 CP 在前半段。

### Part B: Selectivity (核心结果)
| Model | Real Acc | Random Acc | Selectivity | 判定 |
|-------|----------|------------|-------------|------|
| r1-8b (L14) | 0.854 | 0.730 | **12.5pp** | PASS |
| R1-32B (L2) | 0.677 | 0.509 | **16.8pp** | PASS |
| QwQ-32B (L1) | 0.758 | 0.569 | **18.9pp** | PASS |

全部远超 5pp 阈值。

### Part C: Position Baseline vs HS Probe (r1-8b)
| Method | Pre-CP FPR | Precision |
|--------|-----------|-----------|
| position_temporal_w15 | 15.8% | 0.601 |
| **hs_temporal_lr_w15** | **8.1%** | **0.765** |
| text_temporal (exp_015 ref) | 27.2% | 0.487 |

### 结论
Position confound 被排除：
1. Selectivity 12-19pp（阈值 5pp）
2. HS probe pre-CP FPR 显著低于 position baseline
3. HS vs text FPR gap（8.1% vs 27.2%）在相同 position 信息下存在，证明 HS 编码了 position 之外的 safety-specific 信号

---
