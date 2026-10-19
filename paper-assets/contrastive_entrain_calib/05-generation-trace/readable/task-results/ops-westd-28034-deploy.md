# ops westd 28034 deploy

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-28034-deploy_20260518T223126_result.json`
- **Structured JSON:** [`0c785aa74c43acbe30ff.json`](../../sessions/0c/0c785aa74c43acbe30ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 步完成。

### 执行结果汇总

| Step | 结果 |
|------|------|
| **1. Kill exp-008 v2** | PID 45993/45997/45998 已终止，GPU 3 释放至 4 MiB |
| **2. exp-016 启动** | PID 74242 运行中，GPU 3 占用 16374 MiB (61% util)。已加载 362 eval pairs，正在进行 alpha sweep (0.0, 0.5, 1.0, 2.0, 5.0) |
| **3. 磁盘清理** | 清除 exp008_binary_probe_penalty (2.0G) + 6个 dry-run 目录 (~3.4G)，共释放 ~5.4G。清理后可用 20G (36% used) |
| **4. exp-008 v3 dry-run** | Import OK，`BinaryProbeTrainer` 就绪，`RETRAIN_SAMPLES=362`，`RETRAIN_INTERVAL=500` 确认正确 |

---
