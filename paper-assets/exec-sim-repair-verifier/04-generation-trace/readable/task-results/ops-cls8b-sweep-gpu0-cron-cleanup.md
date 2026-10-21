# ops cls8b sweep gpu0 cron cleanup

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cls8b-sweep-gpu0-cron-cleanup_20260515T223230_result.json`
- **Structured JSON:** [`c738fe656c5e133417d4.json`](../../sessions/c7/c738fe656c5e133417d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 结果汇总

**已完成 checkpoint（v2 sweep 独有范围 1800→3800）：**

| Checkpoint | Accuracy | F1_macro |
|------------|----------|----------|
| 1800 | 87.91 | 82.13 |
| 2000 | 87.06 | 79.32 |
| 2200 | 86.51 | — |
| 2400 | 86.82 | — |
| 2600 | 86.40 | — |
| 2800 | 88.38 | 82.58 |
| 3000 | 87.71 | — |
| 3200 | 86.16 | — |
| 3400 | 85.33 | — |
| **3600** | **90.28** | — |
| 3800 | 89.78 | 84.33 |

峰值在 **ckpt-3600 (90.28%)**，ckpt-3800 紧随其后 (89.78%)。

**退出原因：** 进程在 ckpt-4000 推理到 130/9335 时被 kill（日志末尾 `Terminated`）。ckpt-4000+ 结果由 cuda:1 sweep 覆盖，无数据损失。

**资源释放：** cuda:0 已释放（0 MiB），cuda:1 空闲，cuda:2/3 在使用中。

**清理：** Registry → DONE/success，cron 已删除。

---
