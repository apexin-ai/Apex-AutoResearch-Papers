# code relaunch sensitivity v2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_relaunch_sensitivity_v2_20260522T185531_result.json`
- **Structured JSON:** [`4221d86dc55758dfb905.json`](../../sessions/42/4221d86dc55758dfb905.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇报如下：

**1. 旧进程 kill** — PID 93351 (`advbench_classifier_sensitivity.py` v1) 已成功终止（SIGTERM，非 force kill）

**2. v2 脚本启动** — PID 98451 运行中，已加载 520 traces，正在处理 threshold=1（159 JB / 361 safe，30.6%）。输出文件：`/tmp/classifier_sensitivity_v2.log`

**3. Bootstrap CI 进度** — PID 97210 仍在运行，日志显示：
- 520 traces (159 JB, 361 safe)，split 312 train / 208 test
- 当前处于 Phase 1（Train probes + pre-compute test predictions），尚未进入 bootstrap 采样阶段

---
