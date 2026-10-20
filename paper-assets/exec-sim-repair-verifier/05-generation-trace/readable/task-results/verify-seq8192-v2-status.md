# verify seq8192 v2 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_seq8192-v2-status_20260515T174607_result.json`
- **Structured JSON:** [`2c1055f94ece8c748ef9.json`](../../sessions/2c/2c1055f94ece8c748ef9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志仅 173 行，评估实际 4 分钟前才开始。这可能是 v2 重启。计算 ETA：

**汇报：**

| 项目 | 状态 |
|------|------|
| **PID** | 398981，存活，etime 3h52m（wrapper 进程；实际评估 01:42:38 才开始） |
| **GPU 占用** | GPU0: 18.5/32.6GB (79%), GPU1: 27.3/32.6GB (97%), GPU2: 空闲, GPU3: 22.5/32.6GB (88%) |
| **PYTORCH_ALLOC_CONF** | `expandable_segments:True` ✓ |
| **seq8192** | `--max_seq_length 8192 --batch_size 1` ✓ |
| **当前进度** | checkpoint-1800（第 1/21 个），1360/9335 samples，running_acc=87.9% |
| **速率** | 1350 samples in ~226s ≈ **6.0 samples/sec**（10 samples 约 1.5-2s） |

**ETA 计算：**
- 每个 checkpoint：9335 / 6.0 ≈ 1556s + ~8s 加载 ≈ **26 min**
- 当前 checkpoint 剩余：(9335-1360) / 6.0 ≈ **22 min**
- 剩余 20 个 checkpoint：20 × 26 ≈ **520 min**
- **总剩余 ≈ 542 min ≈ 9.0 小时**
- **预计完成：2026-05-16 ~10:50 AM**

注意：wrapper PID 已运行 3h52m，但日志显示评估刚开始 4 分钟（v2 应该是重启后的新日志）。

---
