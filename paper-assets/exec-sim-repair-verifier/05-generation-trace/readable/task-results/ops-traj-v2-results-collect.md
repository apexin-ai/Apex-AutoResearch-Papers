# ops traj v2 results collect

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-v2-results-collect_20260516T142006_result.json`
- **Structured JSON:** [`8b9e447f302e492c5538.json`](../../sessions/8b/8b9e447f302e492c5538.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### s42 — 完成 ✓

| 指标 | 值 |
|------|-----|
| **Test Accuracy** | **83.24%** |
| Best Eval Loss | 0.0796 (step 504) |
| Majority Baseline | 53.59% |
| Gap vs Baseline | +29.65pp |

与 CLS/CWM 对比：**TRAJ v2 (83.24%) 低于 CLS (86.85%) 和 CWM (86.83%) 约 3.6pp**。符合预期——trajectory 格式在 function-level 效率低于直接分类。

### s123 — 训练中

- PID 513115，step 635/756 (~84%)，预计 ~8 分钟后完成
- 当前 best eval_loss = 0.0770（优于 s42 的 0.0796）
- 训练完成后需要在 cuda:3 上跑 eval

Registry 已更新（s42→DONE, s123→RUNNING）。报告写入 `artifacts/traj-v2-results.md`。

---
