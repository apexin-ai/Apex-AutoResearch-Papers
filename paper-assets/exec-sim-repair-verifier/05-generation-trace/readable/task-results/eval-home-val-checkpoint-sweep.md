# eval home val checkpoint sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-val-checkpoint-sweep_20260514T144953_result.json`
- **Structured JSON:** [`9799feb3e517c54494fd.json`](../../sessions/97/9799feb3e517c54494fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Val sweep 已全部完成，无需启动新 eval。** 以下是完整结果汇总：

---

### CLS seed123-home — Val Results (9335 instances, 1883 unparseable, seq_len=2048)

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass | Gap vs Majority |
|-----------|----------|----------|---------|---------|-----------------|
| ckpt-200  | 62.51    | 55.54    | 37.94   | 73.14   | -13.37          |
| ckpt-400  | 80.72    | 67.03    | 45.78   | 88.27   | +4.84           |
| ckpt-600  | 76.78    | 66.81    | 48.63   | 85.00   | +0.90           |
| **ckpt-800**  | **81.81** | **69.14** | **49.37** | 88.91 | +5.93       |
| ckpt-1000 | 82.30    | 67.63    | 45.84   | 89.42   | +6.43           |

**Val best by f1_macro: ckpt-800 (69.14)**  
**Val best by accuracy: ckpt-1000 (82.30)**  
Test best 是 ckpt-600 → **val-test 不一致**（f1_macro 排序: 800 > 400 > 600）

---

### CLS v5 seed42 — Val Results (9335 instances, 1883 unparseable, seq_len=2048)

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass | Gap vs Majority |
|-----------|----------|----------|---------|---------|-----------------|
| ckpt-600  | 77.25    | 70.81    | 57.11   | 84.52   | +1.37           |
| ckpt-4000 | 83.32    | 70.26    | 50.56   | 89.97   | +7.45           |
| ckpt-4200 | 82.82    | 69.54    | 49.43   | 89.65   | +6.94           |
| ckpt-4400 | 83.49    | 71.63    | 53.29   | 89.97   | +7.62           |
| **ckpt-4600** | **83.63** | **71.72** | 53.36 | **90.07** | **+7.76** |

**Val best by f1_macro: ckpt-4600 (71.72)**  
**Val best by accuracy: ckpt-4600 (83.63)**  
Test best 也是 ckpt-4600 → **val-test 一致**

---

### test@4096 结果 (seed123 ckpt-600)

| Metric | Value |
|--------|-------|
| Accuracy | 81.27 |
| F1_macro | 77.91 |
| F1_fail | 69.30 |
| F1_pass | 86.52 |
| Truncation rate | 0% (0/9784) |

---

### 关键发现

1. **v5 seed42**: val 和 test 最佳 checkpoint 一致（都是 ckpt-4600），checkpoint selection 可靠
2. **seed123**: val best = ckpt-800 (f1_macro 69.14), test best = ckpt-600 — **val-test 不一致**。如果用 val 做 checkpoint selection，seed123 应选 ckpt-800 而非 ckpt-600
3. 所有 val eval 有 **1883 unparseable** (20.2%)，可能因为 seq_len=2048 截断导致。test@4096 则 0 truncation。这个 unparseable rate 差异可能影响 val 的 checkpoint ranking 可靠性
4. GPU cuda:0 当前空闲，如需用 seq_len=4096 重跑 val eval 可随时启动

---
