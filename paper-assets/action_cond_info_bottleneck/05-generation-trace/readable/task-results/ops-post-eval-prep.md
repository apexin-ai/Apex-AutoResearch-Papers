# ops post eval prep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-eval-prep_20260516T195248_result.json`
- **Structured JSON:** [`2cf081c79668798e3907.json`](../../sessions/2c/2cf081c79668798e3907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 memory.md。核心结论：

**磁盘**：充足（root 17G / data 167G 剩余）

**v5 eval**：checkpoint-10000 就绪（无 20000），命令已准备好，两 GPU 各跑两个 suite。无需传 `--conditioning_mode`。

**ACIB-H**：代码已完整实现（scorer.py `_hard_topk` + straight-through estimator），训练只需加 `--mode hard`。

**v7 eval 进度**：两 seed 均完成 spatial、正在跑 object，预估还剩 ~1.5-2h 完成全部 4 suites。PID 均存活。

---
