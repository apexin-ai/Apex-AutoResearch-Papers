# diagnose westd41074 pi05 failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd41074-pi05-failures_20260521T091929_result.json`
- **Structured JSON:** [`9f738d1c9001c044abba.json`](../../sessions/9f/9f738d1c9001c044abba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：两个实验均已正常完成

**根因：进程正常退出，没有写 sentinel 文件。** Cron reconcile 找不到 sentinel 所以误报进程消失。

### 实验结果

| 实验 | 完成时间 | SR | 耗时 |
|------|---------|-----|------|
| **random k=0.3** | 17:12:36 | **36.4%** (182/500) | 106.5 min |
| **l2norm k=0.3** | 17:16:21 | **51.0%** (255/500) | 90.8 min |

### 结果文件
- `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.30_libero_object.json`
- `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.30_libero_object.json`

两个文件完整包含 10 个 task 的 per-task SR 和总体 SR，数据完整。

### GPU 空闲情况
- **GPU 0**: 空闲（1MiB / 97887MiB）— 可用
- **GPU 1**: 空闲（1MiB / 97887MiB）— 可用
- GPU 2: 被占用（28546MiB, PID 68539）
- GPU 3: 被占用（~38GB, PID 51513 + 59671）

### 不需要重跑
两个实验结果完整，无需重跑。需要修复的是 eval 脚本缺少 sentinel 写入逻辑，导致 cron 无法检测到正常完成。

---
