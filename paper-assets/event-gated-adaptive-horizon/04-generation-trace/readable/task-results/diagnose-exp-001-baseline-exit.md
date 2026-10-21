# diagnose exp 001 baseline exit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_baseline_exit_20260513T205646_result.json`
- **Structured JSON:** [`31f3353ccd849e05b8e1.json`](../../sessions/31/31f3353ccd849e05b8e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**判定：成功完成 ✓**

| 指标 | 值 |
|------|-----|
| 最终 step | 512,000 |
| eval_return (step 505K) | 970.41 |
| eval_return (last 10 mean±std) | 950.9 ± 10.5 |
| train_return (step 512K) | 828~988 |
| return trend | +25.7 / 10K steps (上升中) |
| checkpoint | `latest.pt` (229MB) |
| FPS | 7.59 |

**mvp_eval.py 输出：**
- **Return**: PASS — eval_return 950.9 ± 10.5，趋势上升
- **Gate Entropy / Effective Horizon / Temporal Structure**: N/A（baseline 无 gate 机制，预期结果）
- **Overall**: PARTIAL 1/4

**GPU 状态：cuda:0 空闲**（0 MiB / 97887 MiB, 0% utilization）。cuda:1 占用 4349 MiB。

**已完成操作：**
- Registry 已更新为 DONE + success + metrics
- Cron 监控已删除

---
