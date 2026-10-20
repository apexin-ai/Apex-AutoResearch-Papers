# diag phi4 s123 mmlu check3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phi4-s123-mmlu-check3_20260520T155003_result.json`
- **Structured JSON:** [`d51555c4a12041f9ed93.json`](../../sessions/d5/d51555c4a12041f9ed93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**PID 365465 已退出**（原 eval 进程完成）。GPU 2 上有新进程 **PID 369044**（运行 ~7min），正在跑 **d100_s123** MMLU eval。

### 已完成 4/5 dosage：

| Dosage | Accuracy |
|--------|----------|
| d000 | 76.31% |
| d005 | 75.92% |
| d025 | 77.02% |
| d050 | 77.30% |
| d100 | 运行中（PID 369044） |

d100_s123 按之前每个 dosage ~13min 的节奏，预计 **~10 分钟后完成**。

这次不是误报——原进程确实完成了前 4 个 dosage 后退出，新进程 369044 启动了 d100 的 eval。等 d100 完成后再统一更新 registry。

---
